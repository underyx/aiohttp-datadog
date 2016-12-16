from functools import partial

import datadog


class DatadogMiddleware:

    def __init__(self, app_prefix, datadog_kwargs=None):
        if datadog_kwargs is None:
            datadog_kwargs = {}

        datadog.initialize(**datadog_kwargs)

        self.app_prefix = app_prefix

    async def __call__(self, app, handler):
        return partial(self.middleware, handler)

    async def middleware(self, handler, request):
        tags = [
            'http_method:{0}'.format(request.method),
            'http_version:{0}'.format(request.version),
            'http_host:{0}'.format(request.host),
            'http_path:{0}'.format(request.path),
            'request_type:{0}'.format(request.GET.getone('type', None)),
        ]
        with datadog.statsd.timed('{0}.request.time'.format(self.app_prefix), tags=tags):
            return await handler(request)
