# Source: https://docs.prefect.io/v3/api-ref/python/prefect-utilities-timeout.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# timeout

# `prefect.utilities.timeout`

## Functions

### `fail_if_not_timeout_error` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/timeout.py#L11" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
fail_if_not_timeout_error(timeout_exc_type: type[Exception]) -> None
```

### `timeout_async` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/timeout.py#L19" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
timeout_async(seconds: Optional[float] = None, timeout_exc_type: type[TimeoutError] = TimeoutError)
```

### `timeout` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/timeout.py#L36" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
timeout(seconds: Optional[float] = None, timeout_exc_type: type[TimeoutError] = TimeoutError)
```


Built with [Mintlify](https://mintlify.com).