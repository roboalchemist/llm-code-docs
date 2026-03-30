# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-utilities-postgres_listener.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# postgres_listener

# `prefect.server.utilities.postgres_listener`

## Functions

### `get_pg_notify_connection` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/postgres_listener.py#L19" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_pg_notify_connection() -> Connection | None
```

Establishes and returns a raw asyncpg connection for LISTEN/NOTIFY.
Returns None if not a PostgreSQL connection URL.

### `pg_listen` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/postgres_listener.py#L102" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
pg_listen(connection: Connection, channel_name: str, heartbeat_interval: float = 5.0) -> AsyncGenerator[str, None]
```

Listens to a specific Postgres channel and yields payloads.
Manages adding and removing the listener on the given connection.


Built with [Mintlify](https://mintlify.com).