Source: https://docs.slack.dev/tools/bolt-python/reference/logger

# Module slack_bolt.logger

Bolt for Python relies on the standard `logging` module.

## Sub-modules

`[slack_bolt.logger.messages](messages.html "slack_bolt.logger.messages")`

## Functions

`def get_bolt_app_logger(app_name: str, cls: object = None, base_logger: logging.Logger | None = None) ‑> logging.Logger`

Expand source code

```python
def get_bolt_app_logger(app_name: str, cls: object = None, base_logger: Optional[Logger] = None) -> Logger:
    logger: Logger = (
        logging.getLogger(f"{app_name}:{cls.__name__}") if cls and hasattr(cls, "__name__") else logging.getLogger(app_name)
    )

    if base_logger is not None:
        _configure_from_base_logger(logger, base_logger)
    else:
        _configure_from_root(logger)
    return logger
```

`def get_bolt_logger(cls: Any, base_logger: logging.Logger | None = None) ‑> logging.Logger`

Expand source code

```python
def get_bolt_logger(cls: Any, base_logger: Optional[Logger] = None) -> Logger:
    logger = logging.getLogger(f"slack_bolt.{cls.__name__}")
    if base_logger is not None:
        _configure_from_base_logger(logger, base_logger)
    else:
        _configure_from_root(logger)
    return logger
```
