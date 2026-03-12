# Source: https://docs.prefect.io/v3/api-ref/python/prefect-logging-formatters.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# formatters

# `prefect.logging.formatters`

## Functions

### `format_exception_info` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/formatters.py#L38" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
format_exception_info(exc_info: ExceptionInfoType) -> dict[str, Any]
```

## Classes

### `JsonFormatter` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/formatters.py#L56" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Formats log records as a JSON string.

The format may be specified as "pretty" to format the JSON with indents and
newlines.

**Methods:**

#### `format` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/formatters.py#L77" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
format(self, record: logging.LogRecord) -> str
```

### `PrefectFormatter` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/formatters.py#L99" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `formatMessage` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/formatters.py#L148" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
formatMessage(self, record: logging.LogRecord) -> str
```


Built with [Mintlify](https://mintlify.com).