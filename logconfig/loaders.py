"""Loader functions that configure logging from various sources.
"""

import os
import json
import yaml
import logging.config

from .exceptions import LogConfigException
from ._compat import string_types, dictConfig


__all__ = (
    'from_autodetect',
    'from_dict',
    'from_env',
    'from_file',
    'from_filename',
    'from_json',
    'from_yaml',
)


def from_autodetect(obj):
    """Dispatch logging configuration based on autodetecting object type.

    Args:
        obj (mixed): Object to load configuration from.

    .. versionadded:: 0.1.0
    """
    if isinstance(obj, dict):
        from_dict(obj)
    elif isinstance(obj, string_types):
        from_filename(obj)
    else:
        raise LogConfigException(('Unable to autodetect object: {0}'
                                  .format(repr(obj))))


def from_dict(dct):
    """Configure logging module using dict object.

    Args:
        dct (dict): Dict to load configuration from.

    .. versionadded:: 0.0.1
    """
    dictConfig(dct)


def from_env(var):
    """Dispatch logging configuration based on filename provided through
    environment variable.

    Args:
        var (str): Environtment variable name to load configuration from.

    .. versionadded:: 0.1.0
    """
    value = os.getenv(var)
    from_filename(value)


def from_file(filename, **kargs):
    """Configure logging module using configparser-format file.

    Args:
        filename (str): String filename to load configuration from.

    Keyword Args:
        defaults (dict, optional): Defaults to be passed to the ConfigParser.
        disable_existing_loggers (bool, optional): Whether to disable existing
            loggers. Defaults to ``True``. The default ``True`` is what the
            default ``logging.config.fileConfig`` uses.

    .. versionadded:: 0.0.1
    """
    logging.config.fileConfig(filename, **kargs)


def from_filename(filename):
    """Dispatch logging configuration based on filename.

    Args:
        filename (str): String filename to load configuration from. Supported
            filename extensions: `.json`, `yml`, `.yaml`, `.cfg`, `.ini`,
            `.conf`, `.config`.

    Raises:
        LogConfigException: Raised if unsupported filename extension is used.

    .. versionadded:: 0.1.0
    """
    ext = os.path.splitext(filename)[1]

    if ext in ('.json',):
        from_json(filename)
    elif ext in ('.yml', '.yaml'):
        from_yaml(filename)
    elif ext in ('.cfg', '.ini', '.conf', '.config'):
        from_file(filename)
    else:
        raise LogConfigException(('Unrecognized filename. '
                                  'Supported filename extensions: '
                                  'json, yml, yaml, cfg, ini, conf, config'))


def from_json(filename):
    """Configure logging module using JSON file.

    Args:
        filename (str): String filename to load configuration from.

    .. versionadded:: 0.0.1
    """
    with open(filename, 'r') as fileobj:
        config = json.load(fileobj)

    from_dict(config)


def from_yaml(filename):
    """Configure logging module using YAML file.

    Args:
        filename (str): String filename to load configuration from.

    .. versionadded:: 0.0.1
    """
    with open(filename, 'r') as fileobj:
        config = yaml.load(fileobj)

    from_dict(config)
