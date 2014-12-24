"""Simple helper moudle for configuring Python logging.

For more details on logging config:

https://docs.python.org/library/logging.config.html
"""

from .__meta__ import (
    __title__,
    __summary__,
    __url__,
    __version__,
    __author__,
    __email__,
    __license__,
)


from .loaders import (
    from_autodetect,
    from_dict,
    from_env,
    from_file,
    from_filename,
    from_json,
    from_yaml,
)


from .utils import (
    get_all_loggers,
    Queue,
    QueueHandler,
    QueueListener,
    queuify_logger,
)


from .exceptions import (
    LogConfigException,
)
