# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-models-csrf_token.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# csrf_token

# `prefect.server.models.csrf_token`

## Functions

### `create_or_update_csrf_token` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/csrf_token.py#L14" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create_or_update_csrf_token(db: PrefectDBInterface, session: AsyncSession, client: str) -> core.CsrfToken
```

Create or update a CSRF token for a client. If the client already has a
token, it will be updated.

**Args:**

* `session`: The database session
* `client`: The client identifier

**Returns:**

* core.CsrfToken: The CSRF token

### `read_token_for_client` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/csrf_token.py#L57" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_token_for_client(db: PrefectDBInterface, session: AsyncSession, client: str) -> Optional[core.CsrfToken]
```

Read a CSRF token for a client.

**Args:**

* `session`: The database session
* `client`: The client identifier

**Returns:**

* Optional\[core.CsrfToken]: The CSRF token, if it exists and is not
  expired.

### `delete_expired_tokens` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/csrf_token.py#L90" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete_expired_tokens(db: PrefectDBInterface, session: AsyncSession) -> int
```

Delete expired CSRF tokens.

**Args:**

* `session`: The database session

**Returns:**

* The number of tokens deleted


Built with [Mintlify](https://mintlify.com).