# pylint: skip-file
"""Python 2/3 compatibility
"""

import sys


PY2 = sys.version_info[0] == 2
PY26 = sys.version_info[0] == 2 and sys.version_info[1] == 6


if PY26:  # pragma: no cover
    from logutils.dictconfig import dictConfig
else:  # pragma: no cover
    from logging.config import dictConfig


if PY2:  # pragma: no cover
    from logutils.queue import QueueHandler, QueueListener
    from Queue import Queue

    text_type = unicode
    string_types = (str, unicode)
else:  # pragma: no cover
    from logging.handlers import QueueHandler, QueueListener
    from queue import Queue

    text_type = str
    string_types = (str,)
