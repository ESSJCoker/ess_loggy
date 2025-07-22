"""
ess_loggy - A Python logging utility with JSON formatting.

This package provides a simple interface for creating loggers with JSON formatting.
"""

from .logger import get_logger, JsonFormatter

__version__ = "0.1.0"
__all__ = ["get_logger", "JsonFormatter"]
