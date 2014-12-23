*********
configlog
*********

|version| |travis| |coveralls| |license|

Simple helper moudle for configuring Python logging.


Requirements
============


Compatibility
-------------

- Python 2.6
- Python 2.7
- Python 3.2
- Python 3.3
- Python 3.4


Dependencies
------------

- PyYAML
- logutils (if using Python 2)


Installation
============


::

    pip install configlog


Overview
========

This simple library exposes several helper methods for configuring the standard library's ``logging`` module. There's nothing fancy about it. Under the hood ``configlog`` uses ``logging.config`` to load various configuartion formats.

In addition to configuration loading, ``configlog`` provides helpers for easily converting a configured logger's handlers utilize a queue.


Supported Configuration Formats
-------------------------------

- JSON
- YAML
- ConfigParser
- Python Dict


Quickstart
==========

Configuration Loading
---------------------

.. code-block:: python

    import configlog
    import logging

    # Load config from JSON file
    configlog.from_json('path/to/file.json')

    # Load config from YAML file
    configlog.from_yaml('path/to/file.yml')

    # Load config from ConfigParser file
    configlog.from_yaml('path/to/file.cfg')

    # Load config from dict
    configlog.from_dict(config_dict)

    log = logging.getLogger()
    log.debug('Configuration loaded using configlog')


Queue Utilization
-----------------

.. code-block:: python

    import configlog
    import logging

    configlog.from_dict({
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'DEBUG'
            }
        },
        'loggers': {
            'mylogger': {
                'handlers': ['console']
            }
        }
    })

    # Convert logger's handlers to utilize a queue
    queue = configlog.Queue(-1)
    listener = configlog.QueueListener(queue)
    handler = configlog.QueueHandler(queue)

    mylogger = logging.getLogger('mylogger')

    # You can also pass in the logger name instead of the actual logger.
    # configlog.queuify_logger('mylogger', handler, listener)
    configlog.queuify_logger(mylogger, handler, listener)

    assert isinstance(mylogger.handlers[0], configlog.QueueHandler)

    # Start the listener.
    listener.start()

    # When finished, stop the listener.
    # This is optional, but not doing so may prevent some logs from being processed.
    listener.stop()


Usage
=====

Use ``configlog`` to easily load ``logging`` configurations. For more details on configuring ``logging``, visit https://docs.python.org/library/logging.config.html.


.. code-block:: python

    import configlog


Configuration from JSON
-----------------------

Configure logging using JSON file.


.. code-block:: python

    configlog.from_json(filename)


Example JSON file:


.. code-block:: javascript

    {
        "version": 1,
        "disable_existing_loggers": false,
        "formatters": {
            "simple": {
                "format": "%(asctime)s. - %(name)s - %(levelname)s - %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "stream": "ext://sys.stdout"
            }
        },
        "root": {
            "level": "DEBUG",
            "handlers": ["console"]
        }
    }


Configuration from YAML
-----------------------

Configure logging using YAML file.


.. code-block:: python

    configlog.from_yaml(filename)


Example YAML file:


.. code-block:: yaml

    version: 1
    disable_existing_loggers: False
    formatters:
      simple:
        format: "%(asctime)s. - %(name)s - %(levelname)s - %(message)s"
    handlers:
      console:
        class: logging.StreamHandler
        level: DEBUG
        formatter: simple
        stream: ext://sys.stdout
    root:
      level: DEBUG
      handlers: [console]


Configuration from ConfigParser File
------------------------------------

Configure logging using ConfigParser compatible file.


.. code-block:: python

    configlog.from_file(filename)


Example CFG file:


.. code-block:: ini

    [loggers]
    keys=root

    [handlers]
    keys=console

    [formatters]
    keys=simple

    [logger_root]
    level=DEBUG
    handlers=console

    [handler_console]
    class=StreamHandler
    level=DEBUG
    formatter=simple
    args=(sys.stdout,)

    [formatter_simple]
    format=%(asctime)s - %(name)s - %(levelname)s - %(message)s


Configuration from Dict
-----------------------

Configure logging using Python dictionary.


.. code-block:: python

    configlog.from_dict(dct)


Example dict:


.. code-block:: python

    {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '%(asctime)s. - %(name)s - %(levelname)s - %(message)s'
            }
        },
        'handlers': {
            'console': {
                'formatter': 'simple',
                'class': 'logging.StreamHandler',
                'level': 'DEBUG',
                'stream': 'ext://sys.stdout'
            }
        },
        'root': {
            'handlers': ['console'],
            'level': 'DEBUG'
        }
    }


Configuration from Autodetection
--------------------------------

If, for whatever reason, you do not know what the source of the configuration will be (or if you're just feeling lucky), then you can try to coerce logging configuration using one of the autodetection methods:


.. code-block:: python

    configlog.from_filename(filename)
    configlog.from_autodetect(filename_or_dict)

    try:
        configlog.from_filename(filename)
        configlog.from_autodetect(filename_or_dict)
    except configlog.ConfiglogException as ex:
        # Unrecognized configuration argument.
        pass


These methods will try to dispatch the function argument to the proper configuration loader or fail trying.


Configuration from Environment Variable
---------------------------------------

Configure logging using filename provided via environment variable.


.. code-block:: python

    configlog.from_env(variable_name)


**NOTE:** Environment variable value will be passed to ``from_filename()``.


.. |version| image:: http://img.shields.io/pypi/v/configlog.svg?style=flat
    :target: https://pypi.python.org/pypi/configlog/

.. |travis| image:: http://img.shields.io/travis/dgilland/configlog/master.svg?style=flat
    :target: https://travis-ci.org/dgilland/configlog

.. |coveralls| image:: http://img.shields.io/coveralls/dgilland/configlog/master.svg?style=flat
    :target: https://coveralls.io/r/dgilland/configlog

.. |license| image:: http://img.shields.io/pypi/l/configlog.svg?style=flat
    :target: https://pypi.python.org/pypi/configlog/
