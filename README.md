# ess_loggy

A simple Python logging utility that provides JSON-formatted logging with custom formatters.

## Features

- JSON-formatted log output
- Custom JsonFormatter class
- Simple logger configuration
- Structured logging for better log analysis

## Installation

```bash
pip install ess_loggy
```

## Quick Start

```python
from ess_loggy import get_logger

# Create a logger
logger = get_logger("my_app")

# Log some messages
logger.info("Application started")
logger.warning("This is a warning")
logger.error("An error occurred")
```

## Output

The logger produces JSON-formatted output like this:

```json
{"level": "INFO", "name": "my_app", "message": "Application started", "time": "2025-07-22 10:30:45"}
{"level": "WARNING", "name": "my_app", "message": "This is a warning", "time": "2025-07-22 10:30:46"}
{"level": "ERROR", "name": "my_app", "message": "An error occurred", "time": "2025-07-22 10:30:47"}
```

## API Reference

### get_logger(name, level)

Creates and configures a logger with JSON formatting.

**Parameters:**

- `name` (str, optional): The name of the logger. Defaults to "ess_loggy".
- `level` (int, optional): The logging level. Defaults to `logging.INFO`.

**Returns:**

- `logging.Logger`: Configured logger instance.

### JsonFormatter

A custom formatter that formats log records as JSON.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
