.. _api:

*************
API Reference
*************


Loaders
=======

Functions that load ``logging`` configurations from various sources.


.. autofunction:: logconfig.from_autodetect

.. autofunction:: logconfig.from_dict

.. autofunction:: logconfig.from_env

.. autofunction:: logconfig.from_file

.. autofunction:: logconfig.from_filename

.. autofunction:: logconfig.from_json

.. autofunction:: logconfig.from_yaml


Utilities
=========

Basic utility functions and classes.


.. autofunction:: logconfig.get_all_loggers

.. autoclass:: logconfig.Queue
    :members:

.. autoclass:: logconfig.QueueHandler
    :members:

.. autoclass:: logconfig.QueueListener
    :members:

.. autofunction:: logconfig.queuify_logger


Exceptions
==========

Custom exceptions used within module.


.. autoexception:: logconfig.LogConfigException
