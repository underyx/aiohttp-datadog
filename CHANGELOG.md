# CHANGELOG

## 0.3.0 (2018-02-15)

:warning: Removed the Datadog tags `http_version`, `http_path`, and `request_type`.

Calculating the list of tags has been extracted to a method called `get_tags`.
If you need these (or any other tags,) you can readd them by subclassing
and overriding this method, like so:

```python
class CustomDatadogMiddleware(DatadogMiddleware):

    def get_tags(self, request):
        tags = super().get_tags(request)
        tags.append(f'http_version:{request.version}')
        return tags
```
## 0.2.0-1 (2017-12-20)

Added changelog entry for 0.2.0.

## 0.2.0 (2017-12-20)

The kwargs passed as the second parameter are now sent to `Dogstatsd`
instead of `datadog.initialize` to expose more useful options,
such as `constant_tags`.

:warning: This means you need to update your keys
from `statsd_host` and `statsd_port` to `host` and `port`.

## 0.1.0 (2016-12-16)

Initial release.
