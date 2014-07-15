
import unittest
import logging

import configlogging


# Py3 compatibility
if 'reload' not in dir(__builtins__):
    from imp import reload


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
        """Test that from_json() method loads config object."""
        filename = 'tests/logging.json'
        configlogging.from_json(filename)
        self.assert_config()

    def test_from_yaml(self):
        """Test that from_yaml() method loads config object."""
        filename = 'tests/logging.yml'
        configlogging.from_yaml(filename)
        self.assert_config()

    def test_from_file(self):
        """Test that from_file() method loads config object."""
        filename = 'tests/logging.cfg'
        configlogging.from_file(filename)
        self.assert_config()

    def test_from_dict(self):
        """Test that from_dict() method loads config object."""
        dct = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'simple': {
                    'format': ('%(asctime)s. - %(name)s - %(levelname)s - '
                               '%(message)s')
                },
                'verbose': {
                    'format': ('%(asctime)s - %(name)s - %(levelname)s - ',
                               '%(module)s %(funcName)s %(pathname)s ',
                               '%(lineno)s - %(message)s')
                }
            },
            'handlers': {
                'console': {
                    'formatter': 'simple',
                    'class': 'logging.StreamHandler',
                    'level':
                    'DEBUG'
                }
            },
            'root': {
                'handlers': ['console'],
                'level': 'DEBUG'
            }
        }

        configlogging.from_dict(dct)
        self.assert_config()
