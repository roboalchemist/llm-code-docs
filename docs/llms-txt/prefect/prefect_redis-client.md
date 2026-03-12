# Source: https://docs.prefect.io/integrations/prefect-redis/api-ref/prefect_redis-client.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# client

# `prefect_redis.client`

## Functions

### `cached` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-redis/prefect_redis/client.py#L58" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
cached(fn: Callable[..., Any]) -> Callable[..., Any]
```

### `close_all_cached_connections` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-redis/prefect_redis/client.py#L69" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
close_all_cached_connections() -> None
```

Close all cached Redis connections.

### `clear_cached_clients` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-redis/prefect_redis/client.py#L80" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
clear_cached_clients() -> None
```

Clear all cached Redis clients to force fresh connections.

This should be called when a connection error is detected to ensure
subsequent calls to get\_async\_redis\_client() return fresh clients
rather than stale ones with broken connections.

### `get_async_redis_client` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-redis/prefect_redis/client.py#L93" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_async_redis_client(host: Union[str, None] = None, port: Union[int, None] = None, db: Union[int, None] = None, password: Union[str, None] = None, username: Union[str, None] = None, health_check_interval: Union[int, None] = None, decode_responses: bool = True, ssl: Union[bool, None] = None) -> Redis
```

Retrieves an async Redis client.

**Args:**

* `host`: The host location.
* `port`: The port to connect to the host with.
* `db`: The Redis database to interact with.
* `password`: The password for the redis host
* `username`: Username for the redis instance
* `decode_responses`: Whether to decode binary responses from Redis to
  unicode strings.

**Returns:**

* a Redis client

### `async_redis_from_settings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-redis/prefect_redis/client.py#L132" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
async_redis_from_settings(settings: RedisMessagingSettings, **options: Any) -> Redis
```

## Classes

### `RedisMessagingSettings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-redis/prefect_redis/client.py#L15" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>


Built with [Mintlify](https://mintlify.com).