# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-api-csrf_token.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# csrf_token

# `prefect.server.api.csrf_token`

## Functions

### `create_csrf_token` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/csrf_token.py#L22" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create_csrf_token(db: PrefectDBInterface = Depends(provide_database_interface), client: str = Query(..., description='The client to create a CSRF token for')) -> schemas.core.CsrfToken
```

Create or update a CSRF token for a client


Built with [Mintlify](https://mintlify.com).