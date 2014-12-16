*************
configlogging
*************

|version| |travis| |coveralls| |license|

Simple helper moudle for configuring Python logging.


Requirements
============


Compatibility
-------------

- Python 2.7
- Python 3.2
- Python 3.3
- Python 3.4


Dependencies
------------

- PyYAML


Installation
============


::

    pip install configlogging


Overview
========

This simple library exposes several helper methods for configuring the standard library's ``logging`` module. There's nothing fancy about it. Under the hood ``configlogging`` uses ``logging.config`` to load various configuartion formats.


Supported Configuration Formats
-------------------------------

- JSON
- YAML
- ConfigParser
- Python Dict


Quickstart
----------


.. code-block:: python

    import configlogging
    import logging

    # Load config from JSON file
    configlogging.from_json('path/to/file.json')

    # Load config from YAML file
    configlogging.from_yaml('path/to/file.yml')

    # Load config from ConfigParser file
    configlogging.from_yaml('path/to/file.cfg')

    # Load config from dict
    configlogging.from_dict(config_dict)

    log = logging.getLogger()
    log.debug('Configuration loaded using configlogging')


Usage
=====

Use ``configlogging`` to easily load ``logging`` configurations. For more details on configuring ``logging``, visit https://docs.python.org/library/logging.config.html.


.. code-block:: python

    import configlogging


Configuration from JSON
-----------------------

Configure logging using JSON file.


.. code-block:: python

    configlogging.from_json(filename)


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

    configlogging.from_yaml(filename)


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

    configlogging.from_file(filename)


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

    configlogging.from_dict(dct)


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

    configlogging.from_filename(filename)
    configlogging.from_autodetect(filename_or_dict)

    try:
        configlogging.from_filename(filename)
        configlogging.from_autodetect(filename_or_dict)
    except configlogging.ConfigException as ex:
        # Unrecognized configuration argument.
        pass


These methods will try to dispatch the function argument to the proper configuration loader or fail trying.


Configuration from Environment Variable
---------------------------------------

Configure logging using filename provided via environment variable.


.. code-block:: python

    configlogging.from_env(variable_name)


**NOTE:** Environment variable value will be passed to ``from_filename()``.


.. |version| image:: http://img.shields.io/pypi/v/configlogging.svg?style=flat
    :target: https://pypi.python.org/pypi/configlogging/

.. |travis| image:: http://img.shields.io/travis/dgilland/configlogging/master.svg?style=flat
    :target: https://travis-ci.org/dgilland/configlogging

.. |coveralls| image:: http://img.shields.io/coveralls/dgilland/configlogging/master.svg?style=flat
    :target: https://coveralls.io/r/dgilland/configlogging

.. |license| image:: http://img.shields.io/pypi/l/configlogging.svg?style=flat
    :target: https://pypi.python.org/pypi/configlogging/
