"""Dead simple helper for configuring Python's logging module

For more details on logging config:

https://docs.python.org/library/logging.config.html
"""

import os
import json
import yaml
import logging.config


def from_json(filename):
    """Configure logging module using JSON file."""
    with open(filename, 'r') as fileobj:
        config = json.load(fileobj)

    logging.config.dictConfig(config)


def from_yaml(filename):
    """Configure logging module using YAML file."""
    with open(filename, 'r') as fileobj:
        config = yaml.load(fileobj)

    logging.config.dictConfig(config)


def from_file(filename, **kargs):
    """Configure logging module using configparser-format file."""
    logging.config.fileConfig(filename, **kargs)


def from_dict(dct):
    """Configure logging module using dict object."""
    logging.config.dictConfig(dct)
