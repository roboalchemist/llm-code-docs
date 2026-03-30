# Source: https://docs.prefect.io/v3/api-ref/python/prefect-logging-filters.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# filters

# `prefect.logging.filters`

## Functions

### `redact_substr` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/filters.py#L8" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
redact_substr(obj: Any, substr: str) -> Any
```

Redact a string from a potentially nested object.

**Args:**

* `obj`: The object to redact the string from
* `substr`: The string to redact.

**Returns:**

* The object with the API key redacted.

## Classes

### `ObfuscateApiKeyFilter` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/filters.py#L29" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

A logging filter that obfuscates any string that matches the obfuscate\_string function.

**Methods:**

#### `filter` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/filters.py#L34" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
filter(self, record: logging.LogRecord) -> bool
```


Built with [Mintlify](https://mintlify.com).