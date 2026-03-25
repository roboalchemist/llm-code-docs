# Source: https://docs.prefect.io/v3/api-ref/python/prefect-testing-utilities.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# utilities

# `prefect.testing.utilities`

Internal utilities for tests.

## Functions

### `exceptions_equal` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/testing/utilities.py#L43" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
exceptions_equal(a: Exception, b: Exception) -> bool
```

Exceptions cannot be compared by `==`. They can be compared using `is` but this
will fail if the exception is serialized/deserialized so this utility does its
best to assert equality using the type and args used to initialize the exception

### `kubernetes_environments_equal` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/testing/utilities.py#L54" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
kubernetes_environments_equal(actual: list[dict[str, str]], expected: list[dict[str, str]] | dict[str, str]) -> bool
```

### `assert_does_not_warn` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/testing/utilities.py#L91" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
assert_does_not_warn(ignore_warnings: list[type[Warning]] | None = None) -> Generator[None, None, None]
```

Converts warnings to errors within this context to assert warnings are not raised,
except for those specified in ignore\_warnings.

Parameters:

* ignore\_warnings: List of warning types to ignore. Example: \[DeprecationWarning, UserWarning]

### `prefect_test_harness` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/testing/utilities.py#L114" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
prefect_test_harness(server_startup_timeout: int | None = 30)
```

Temporarily run flows against a local SQLite database for testing.

**Args:**

* `server_startup_timeout`: The maximum time to wait for the server to start.
  Defaults to 30 seconds. If set to `None`, the value of
  `PREFECT_SERVER_EPHEMERAL_STARTUP_TIMEOUT_SECONDS` will be used.

**Examples:**

```python  theme={null}
from prefect import flow
from prefect.testing.utilities import prefect_test_harness


@flow
def my_flow():
    return 'Done!'

with prefect_test_harness():
    assert my_flow() == 'Done!' # run against temporary db
```

### `get_most_recent_flow_run` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/testing/utilities.py#L200" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_most_recent_flow_run(client: 'PrefectClient | None' = None, flow_name: str | None = None) -> 'FlowRun'
```

### `assert_blocks_equal` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/testing/utilities.py#L217" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
assert_blocks_equal(found: Block, expected: Block, exclude_private: bool = True, **kwargs: Any) -> None
```

### `assert_uses_result_serializer` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/testing/utilities.py#L234" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
assert_uses_result_serializer(state: State, serializer: str | Serializer, client: 'PrefectClient') -> None
```

### `assert_uses_result_storage` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/testing/utilities.py#L270" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
assert_uses_result_storage(state: State, storage: 'str | ReadableFileSystem', client: 'PrefectClient') -> None
```

### `a_test_step` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/testing/utilities.py#L298" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
a_test_step(**kwargs: Any) -> dict[str, Any]
```

### `b_test_step` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/testing/utilities.py#L309" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
b_test_step(**kwargs: Any) -> dict[str, Any]
```


Built with [Mintlify](https://mintlify.com).