from aiohttp import web
from datadog import DogStatsd


@web.middleware
class DatadogMiddleware:
    def __init__(
        self,
        app_prefix,
        dogstatsd_kwargs=None,
        *,
        dogstatsd_class=DogStatsd,
        dogstatsd_instance=None,
    ):
        if dogstatsd_kwargs is not None and dogstatsd_instance is not None:
            raise ValueError(
                "You gave the DatadogMiddleware the instance {0} and the kwargs {1}. ".format(
                    dogstatsd_instance, dogstatsd_kwargs
                )
                + "This doesn't really make sense, as we can't pass arguments to an existing instance. "
                + "Please remove one of the two."
            )

        if dogstatsd_kwargs is None:
            dogstatsd_kwargs = {}

        if dogstatsd_instance is not None:
            self.dogstatsd = dogstatsd_instance
        else:
            self.dogstatsd = dogstatsd_class(**dogstatsd_kwargs)

        self.app_prefix = app_prefix

    async def __call__(self, request, handler):
        with self.dogstatsd.timed(
            "{0}.request.time".format(self.app_prefix), tags=self.get_tags(request)
        ):
            return await handler(request)

    def get_tags(self, request):
        return [
            "http_method:{0}".format(request.method),
            "http_host:{0}".format(request.host),
            "http_path:{0}".format(request.path),
        ]
