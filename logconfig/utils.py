"""Utility functions.
"""

import logging

from ._compat import (
    string_types,
    QueueHandler,
    QueueListener as _QueueListener,
    Queue
)


__all__ = (
    'get_all_loggers',
    'Queue',
    'QueueHandler',
    'QueueListener',
    'queuify_logger',
)


class QueueListener(_QueueListener):
    """Extension of default ``QueueListener`` that respects ``handler.level``
    when handling records.

    .. versionadded:: 0.3.0
    """
    def handle(self, record):
        """Delegate handling of log records to listened handlers if record's
        log level is greater than or equal to handler's level.
        """
        record = self.prepare(record)
        for handler in self.handlers:
            # CHANGED HERE TO ADD A CONDITION TO CHECK THE HANDLER LEVEL
            if record.levelno >= handler.level:
                handler.handle(record)


def get_all_loggers():
    """Return ``dict`` of all loggers than have been accessed.

    .. versionadded:: 0.3.0
    """
    return logging.Logger.manager.loggerDict


def queuify_logger(logger, queue_handler, queue_listener):
    """Replace logger's handlers with a queue handler while adding existing
    handlers to a queue listener.

    This is useful when you want to use a default logging config but then
    optionally add a logger's handlers to a queue during runtime.

    Args:
        logger (mixed): Logger instance or string name of logger to queue-ify
            handlers.
        queue_handler (QueueHandler): Instance of a ``QueueHandler``.
        queue_listener (QueueListener): Instance of a ``QueueListener``.

    .. versionadded:: 0.3.0
    """
    if isinstance(logger, string_types):
        logger = logging.getLogger(logger)

    # Get handlers that aren't being listened for.
    handlers = [hdlr for hdlr in logger.handlers
                if hdlr not in queue_listener.handlers]

    if handlers:
        # The default QueueListener stores handlers as a tuple.
        queue_listener.handlers = tuple(list(queue_listener.handlers)
                                        + handlers)

    # Remove logger's handlers and replace with single queue handler.
    del logger.handlers[:]
    logger.addHandler(queue_handler)
