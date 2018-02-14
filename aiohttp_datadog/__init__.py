from functools import partial

from datadog import DogStatsd


class DatadogMiddleware:

    def __init__(self, app_prefix, dogstatsd_kwargs=None):
        if dogstatsd_kwargs is None:
            dogstatsd_kwargs = {}

        self.dogstatsd = DogStatsd(**dogstatsd_kwargs)
        self.app_prefix = app_prefix

    async def __call__(self, app, handler):
        return partial(self.middleware, handler)

    async def middleware(self, handler, request):
        tags = [
            'http_method:{0}'.format(request.method),
            'http_version:{0}'.format(request.version),
            'http_host:{0}'.format(request.host),
            'http_path:{0}'.format(request.path),
            'request_type:{0}'.format(request.query.getone('type', None)),
        ]

        with self.dogstatsd.timed('{0}.request.time'.format(self.app_prefix), tags=tags):
            return await handler(request)
