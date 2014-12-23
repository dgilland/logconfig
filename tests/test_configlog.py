
import logging
import os

import pytest
import configlog

from .logging_dict import logging_dict


# Py3 compatibility
if 'reload' not in dir(__builtins__):
    from imp import reload


parametrize = pytest.mark.parametrize

logging_json = 'tests/logging.json'
logging_yaml = 'tests/logging.yml'
logging_file = 'tests/logging.cfg'


def assert_basic_config(handler_class=logging.StreamHandler):
    logger = logging.getLogger()
    assert logger.level == logging.DEBUG
    assert len(logger.handlers) == 1
    assert isinstance(logger.handlers[0], handler_class)


@parametrize('config', [
    logging_json
])
def test_from_json(config):
    configlog.from_json(config)
    assert_basic_config()


@parametrize('config', [
    logging_yaml
])
def test_from_yaml(config):
    configlog.from_yaml(config)
    assert_basic_config()


@parametrize('config', [
    logging_file
])
def test_from_file(config):
    configlog.from_file(config)
    assert_basic_config()


@parametrize('config', [
    logging_dict
])
def test_from_dict(config):
    configlog.from_dict(config)
    assert_basic_config()


@parametrize('config', [
    logging_json,
    logging_yaml,
    logging_file,
])
def test_from_filename(config):
    configlog.from_filename(config)
    assert_basic_config()


@parametrize('config', [
    'invalid'
])
def test_from_filename_exception(config):
    raised = False
    try:
        configlog.from_filename(config)
    except configlog.ConfigLogException:
        raised = True

    assert raised


@parametrize('config', [
    logging_dict,
    logging_json,
    logging_yaml,
    logging_file,
])
def test_from_autodetect(config):
    configlog.from_autodetect(config)
    assert_basic_config()


@parametrize('config', [
    'invalid',
    []
])
def test_from_autodetect_exception(config):
    raised = False
    try:
        configlog.from_autodetect(config)
    except configlog.ConfigLogException:
        raised = True

    assert raised


@parametrize('var,config', [
    ('CL_TESTING', logging_json)
])
def test_from_env(var, config):
    os.environ[var] = config
    configlog.from_env(var)
    assert_basic_config()
    del os.environ[var]
