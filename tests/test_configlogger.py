
import unittest
import logging

import configlogging

from .logging_dict import logging_dict

# Py3 compatibility
if 'reload' not in dir(__builtins__):
    from imp import reload


logging_json = 'tests/logging.json'
logging_yaml = 'tests/logging.yml'
logging_file = 'tests/logging.cfg'


class TestConfiglogging(unittest.TestCase):
    """Tests for configlogging module."""

    def setUp(self):
        """Set up logging module to initial state."""
        logging.getLogger().setLevel(logging.NOTSET)

    def tearDown(self):
        """Reset logging module to remove current configuration."""
        logging.shutdown()
        reload(logging)

    def assert_config(self):
        """Assert that root logger is configured via configuration method."""
        logger = logging.getLogger()
        self.assertEqual(logger.level, logging.DEBUG)
        self.assertTrue(len(logger.handlers) > 0)
        self.assertIsInstance(logger.handlers[0], logging.StreamHandler)

    def test_from_json(self):
        """Test that from_json loads config object."""
        configlogging.from_json(logging_json)
        self.assert_config()

    def test_from_yaml(self):
        """Test that from_yaml loads config object."""
        configlogging.from_yaml(logging_yaml)
        self.assert_config()

    def test_from_file(self):
        """Test that from_file loads config object."""
        configlogging.from_file(logging_file)
        self.assert_config()

    def test_from_dict(self):
        """Test that from_dict loads config object."""
        configlogging.from_dict(logging_dict)
        self.assert_config()
