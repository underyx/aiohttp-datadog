aiohttp-datadog
===============

.. image:: https://circleci.com/gh/underyx/aiohttp-datadog.svg?style=shield
   :target: https://circleci.com/gh/underyx/aiohttp-datadog
   :alt: CI Status

An aiohttp_ middleware for reporting metrics to Datadog_. Python 3.5+ is required.

Usage
-----

.. code-block:: python

    from aiohttp import web
    from aiohttp_datadog import DatadogMiddleware
    app = web.Application(
        middlewares=(
            DatadogMiddleware('my_app', {
                'host': 'localhost',
                'port': 8126,
            }),
            # ...
        ),
    )

.. _aiohttp: http://aiohttp.readthedocs.io/en/stable/
.. _Datadog: https://www.datadoghq.com/
