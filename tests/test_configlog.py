
import logging
import os
from copy import deepcopy

import pytest
import logconfig
from logconfig._compat import PY2, QueueHandler, QueueListener, Queue

from .logging_dict import logging_dict


if PY2:
    # StringIO doesn't work as stream for StreamHandler.
    from io import BytesIO as IOCapture
else:
    from io import StringIO as IOCapture


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
    logconfig.from_json(config)
    assert_basic_config()


@parametrize('config', [
    logging_yaml
])
def test_from_yaml(config):
    logconfig.from_yaml(config)
    assert_basic_config()


@parametrize('config', [
    logging_file
])
def test_from_file(config):
    logconfig.from_file(config)
    assert_basic_config()


@parametrize('config', [
    logging_dict
])
def test_from_dict(config):
    logconfig.from_dict(config)
    assert_basic_config()


@parametrize('config', [
    logging_json,
    logging_yaml,
    logging_file,
])
def test_from_filename(config):
    logconfig.from_filename(config)
    assert_basic_config()


@parametrize('config', [
    'invalid'
])
def test_from_filename_exception(config):
    raised = False
    try:
        logconfig.from_filename(config)
    except logconfig.LogConfigException:
        raised = True

    assert raised


@parametrize('config', [
    logging_dict,
    logging_json,
    logging_yaml,
    logging_file,
])
def test_from_autodetect(config):
    logconfig.from_autodetect(config)
    assert_basic_config()


@parametrize('config', [
    'invalid',
    []
])
def test_from_autodetect_exception(config):
    raised = False
    try:
        logconfig.from_autodetect(config)
    except logconfig.LogConfigException:
        raised = True

    assert raised


@parametrize('var,config', [
    ('CL_TESTING', logging_json)
])
def test_from_env(var, config):
    os.environ[var] = config
    logconfig.from_env(var)
    assert_basic_config()
    del os.environ[var]


@parametrize('logger, config', [
    (logging.getLogger(), logging_dict),
    ('', logging_dict),
])
def test_queuify_handlers(logger, config):
    queue = Queue(-1)
    queue_listener = logconfig.QueueListener(queue)
    queue_handler = QueueHandler(queue)

    config = deepcopy(config)
    stream = IOCapture()
    config['handlers']['console']['stream'] = stream

    logconfig.from_dict(config)

    real_logger = (logger if hasattr(logger, 'handlers')
                   else logging.getLogger(logger))

    original_handlers = real_logger.handlers[:]

    logconfig.queuify_logger(logger, queue_handler, queue_listener)

    assert real_logger.handlers[0] == queue_handler

    for hdlr in original_handlers:
        assert hdlr in queue_listener.handlers

    queue_listener.start()
    logging.debug('foo')
    queue_listener.stop()
    stream.seek(0)

    assert 'foo' in stream.read()


@parametrize('names', [
    ('foo', 'bar', 'baz')
])
def test_get_all_loggers(names):
    assert logconfig.get_all_loggers() == {}

    loggers = [logging.getLogger(name) for name in names]
    all_loggers = logconfig.get_all_loggers()

    assert set(all_loggers.keys()) == set(names)
    assert set(all_loggers.values()) == set(loggers)
