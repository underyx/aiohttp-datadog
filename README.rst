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
            DatadogMiddleware(
                "my_app",
                {"host": "localhost", "port": 8126},
            ),
        ),
    )

If you're using a custom DogStatsd class,
you can supply it via a keyword argument:

.. code-block:: python

    app = web.Application(
        middlewares=(
            DatadogMiddleware(
                "my_app",
                {"host": "localhost", "port": 8126},
                dogstatsd_class=CatStatsd,
            ),
        ),
    )

Or if you're even more of a control freak,
you can instantiate it yourself:

.. code-block:: python

    app = web.Application(
        middlewares=(
            DatadogMiddleware(
                "my_app",
                dogstatsd_instance=CatStatsd(meow=False),
            ),
        ),
    )

.. _aiohttp: http://aiohttp.readthedocs.io/en/stable/
.. _Datadog: https://www.datadoghq.com/
