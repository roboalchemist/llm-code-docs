# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-utilities-http.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# http

# `prefect.server.utilities.http`

## Functions

### `should_redact_header` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/http.py#L1" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
should_redact_header(key: str) -> bool
```

Indicates whether an HTTP header is sensitive or noisy and should be redacted
from events and templates.


Built with [Mintlify](https://mintlify.com).