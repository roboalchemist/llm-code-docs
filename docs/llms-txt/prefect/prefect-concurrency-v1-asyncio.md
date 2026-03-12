# Source: https://docs.prefect.io/v3/api-ref/python/prefect-concurrency-v1-asyncio.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# asyncio

# `prefect.concurrency.v1.asyncio`

## Functions

### `concurrency` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/concurrency/v1/asyncio.py#L26" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
concurrency(names: Union[str, list[str]], task_run_id: UUID, timeout_seconds: Optional[float] = None) -> AsyncGenerator[None, None]
```

A context manager that acquires and releases concurrency slots from the
given concurrency limits.

**Args:**

* `names`: The names of the concurrency limits to acquire slots from.
* `task_run_id`: The name of the task\_run\_id that is incrementing the slots.
* `timeout_seconds`: The number of seconds to wait for the slots to be acquired before
  raising a `TimeoutError`. A timeout of `None` will wait indefinitely.

**Raises:**

* `TimeoutError`: If the slots are not acquired within the given timeout.

Example:
A simple example of using the async `concurrency` context manager:

```python  theme={null}
from prefect.concurrency.v1.asyncio import concurrency

async def resource_heavy():
    async with concurrency("test", task_run_id):
        print("Resource heavy task")

async def main():
    await resource_heavy()
```


Built with [Mintlify](https://mintlify.com).