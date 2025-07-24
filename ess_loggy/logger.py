'''
Python module for creating and configuring loggers.
This module provides a function to create a logger with a specified name,
and it sets up a console handler with a specific format for log messages.
'''
import logging
import json
import sys


class JsonFormatter(logging.Formatter):
    """
    Custom formatter that formats log records as JSON.
    """

    def format(self, record: logging.LogRecord) -> str:
        log_record = {
            'level': record.levelname,
            'name': record.name,
            'message': record.getMessage(),
            # 'time': self.formatTime(record, self.datefmt),
            'time': self.formatTime(record, datefmt="%Y-%m-%dT%H:%M:%S.%fZ"),

        }
        return json.dumps(log_record)


def get_logger(name: str = "ess_loggy", level=logging.INFO) -> logging.Logger:
    """
    Create and configure a logger with the specified name.

    Args:
        name (str): The name of the logger.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        handler = logging.StreamHandler(sys.stdout)
        formatter = JsonFormatter()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(level)
    return logger
