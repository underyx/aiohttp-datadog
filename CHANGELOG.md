# CHANGELOG

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
