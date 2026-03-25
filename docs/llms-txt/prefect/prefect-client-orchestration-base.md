# Source: https://docs.prefect.io/v3/api-ref/python/prefect-client-orchestration-base.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# base

# `prefect.client.orchestration.base`

## Classes

### `BaseClient` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/client/orchestration/base.py#L16" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `request` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/client/orchestration/base.py#L22" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
request(self, method: HTTP_METHODS, path: 'ServerRoutes', params: dict[str, Any] | None = None, path_params: dict[str, Any] | None = None, **kwargs: Any) -> 'Response'
```

### `BaseAsyncClient` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/client/orchestration/base.py#L36" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `request` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/client/orchestration/base.py#L42" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
request(self, method: HTTP_METHODS, path: 'ServerRoutes', params: dict[str, Any] | None = None, path_params: dict[str, Any] | None = None, **kwargs: Any) -> 'Response'
```


Built with [Mintlify](https://mintlify.com).