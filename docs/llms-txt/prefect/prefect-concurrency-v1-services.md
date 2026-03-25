# Source: https://docs.prefect.io/v3/api-ref/python/prefect-concurrency-v1-services.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# services

# `prefect.concurrency.v1.services`

## Classes

### `ConcurrencySlotAcquisitionServiceError` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/concurrency/v1/services.py#L21" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Raised when an error occurs while acquiring concurrency slots.

### `ConcurrencySlotAcquisitionService` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/concurrency/v1/services.py#L25" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `acquire` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/concurrency/v1/services.py#L39" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
acquire(self, task_run_id: UUID, timeout_seconds: Optional[float] = None) -> httpx.Response
```


Built with [Mintlify](https://mintlify.com).