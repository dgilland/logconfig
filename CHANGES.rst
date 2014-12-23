Changelog
=========


vx.x.x (xxxx-xx-xx)
-------------------

- Add support for Python 2.6
- Add ``queuify_logger()`` for moving logger's handlers to a queue.
- Add ``get_all_loggers()`` which returns a ``dict`` of all loggers that have been accessed.
- Proxy access to ``QueueHandler`` and ``QueueListener`` from either ``logutils`` if on Python 2 or ``logging.handlers`` if on Python 3.
- Extend base ``QueueListener`` class to respect log level of handler. The current stdlib version doesn't do this.


v0.2.0 (2014-12-23)
-------------------

- Renamed project to ``configlog``. (**breaking change**)
- Rename ``ConfigException`` to ``ConfigLogException``. (**breaking change**)


v0.1.1 (2014-07-16)
-------------------

Brown bag release.


v0.1.0 (2014-07-16)
-------------------

- Add ``from_filename()``.
- Add ``from_autodetect()``.
- Add ``from_env()``.


v0.0.1 (2014-07-15)
-------------------

- First release
