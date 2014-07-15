configlogging
=============

[![Package Version](https://pypip.in/v/configlogging/badge.png)](https://pypi.python.org/pypi/configlogging/)
[![Build Status](https://travis-ci.org/dgilland/configlogging.png?branch=master)](https://travis-ci.org/dgilland/configlogging)
[![Coverage Status](https://coveralls.io/repos/dgilland/configlogging/badge.png?branch=master)](https://coveralls.io/r/dgilland/configlogging)
[![License](https://pypip.in/license/configlogging/badge.png)](https://pypi.python.org/pypi/configlogging/)


Dead simple helper for configuring Python's logging module.


## Requirements

### Compatibility

- Python 2.7
- Python 3.2
- Python 3.3
- Python 3.4

### Dependencies

- PyYAML


## Installation

```python
pip install configlogging
```


## Overview

This simple library exposes several helper methods for configuring the standard library's `logging` module. There's nothing fancy about it. Under the hood `configlogging` uses `logging.config` to load various configuartion formats.

### Supported Configuration Formats

- JSON
- YAML
- CFG
- Python dict


## Usage

Use `configlogging` to easily load `logging` configurations. For more details and examples, visit https://docs.python.org/library/logging.config.html.

```python
import configlogging
```

### Configuration from JSON

```python
configlogging.from_json(filename)
```

Example JSON file:

```json
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
            "formatter": "simple"
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console"]
    }
}
```

### Configuration from YAML

```python
configlogging.from_yaml(filename)
```

Example YAML file:

```yaml
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
root:
  level: DEBUG
  handlers: [console]
```

### Configuration from configparser-format File

```python
configlogging.from_file(filename)
```

Example CFG file:

```ini
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
```

### Configuration from Dict

```python
configlogging.from_dict(dct)
```

Example dict:

```python
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
            'level':
            'DEBUG'
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG'
    }
}
```
