
import unittest
import logging
import os

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

    def test_from_filename_json(self):
        """Test that from_filename loads config object from json."""
        configlogging.from_filename(logging_json)
        self.assert_config()

    def test_from_filename_yaml(self):
        """Test that from_filename loads config object from yaml."""
        configlogging.from_filename(logging_yaml)
        self.assert_config()

    def test_from_filename_file(self):
        """Test that from_filename loads config object from file."""
        configlogging.from_filename(logging_file)
        self.assert_config()

    def test_from_filename_exception(self):
        """Test that from_autodetect() throws exception on invalid object."""
        self.assertRaises(configlogging.ConfigException,
                          configlogging.from_filename,
                          'invalid')

    def test_from_autodetect_dict(self):
        """Test that from_autodetect() loads config object from dict."""
        configlogging.from_autodetect(logging_dict)
        self.assert_config()

    def test_from_autodetect_json(self):
        """Test that from_autodetect() loads config object from json."""
        configlogging.from_autodetect(logging_json)
        self.assert_config()

    def test_from_autodetect_yaml(self):
        """Test that from_autodetect() loads config object from yaml."""
        configlogging.from_autodetect(logging_yaml)
        self.assert_config()

    def test_from_autodetect_file(self):
        """Test that from_autodetect() loads config object from file."""
        configlogging.from_autodetect(logging_file)
        self.assert_config()

    def test_from_autodetect_exception(self):
        """Test that from_autodetect() throws exception on invalid object."""
        self.assertRaises(configlogging.ConfigException,
                          configlogging.from_autodetect,
                          'invalid')

        self.assertRaises(configlogging.ConfigException,
                          configlogging.from_autodetect,
                          [])


    def test_from_env(self):
        """Test that from_env() loads config object from filename via
        environment variable.
        """
        var = 'CL_TESTING'
        os.environ[var] = logging_json
        configlogging.from_env(var)
        self.assert_config()
        del os.environ[var]
