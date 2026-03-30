# Source: https://docs.prefect.io/v3/api-ref/python/prefect-client-attribution.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# attribution

# `prefect.client.attribution`

Attribution context for API requests.

This module provides functions to gather attribution headers that identify
the source of API requests (flow runs, deployments, workers) for usage tracking
and rate limit debugging.

## Functions

### `get_attribution_headers` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/client/attribution.py#L18" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_attribution_headers() -> dict[str, str]
```

Gather attribution headers from the current execution context.

These headers help Cloud track which flow runs, deployments, and workers
are generating API requests for usage attribution and rate limit debugging.

Headers are only included when values are available. All headers are optional.

**Returns:**

* A dictionary of attribution headers to include in API requests.


Built with [Mintlify](https://mintlify.com).