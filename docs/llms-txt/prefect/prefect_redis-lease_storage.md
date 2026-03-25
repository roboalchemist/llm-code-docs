# Source: https://docs.prefect.io/integrations/prefect-redis/api-ref/prefect_redis-lease_storage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# lease_storage

# `prefect_redis.lease_storage`

## Classes

### `ConcurrencyLeaseStorage` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-redis/prefect_redis/lease_storage.py#L25" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

A Redis-based concurrency lease storage implementation.

**Methods:**

#### `create_lease` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-redis/prefect_redis/lease_storage.py#L151" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create_lease(self, resource_ids: list[UUID], ttl: timedelta, metadata: ConcurrencyLimitLeaseMetadata | None = None) -> ResourceLease[ConcurrencyLimitLeaseMetadata]
```

#### `list_holders_for_limit` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-redis/prefect_redis/lease_storage.py#L330" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
list_holders_for_limit(self, limit_id: UUID) -> list[tuple[UUID, ConcurrencyLeaseHolder]]
```

#### `read_active_lease_ids` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-redis/prefect_redis/lease_storage.py#L299" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_active_lease_ids(self, limit: int = 100, offset: int = 0) -> list[UUID]
```

#### `read_expired_lease_ids` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-redis/prefect_redis/lease_storage.py#L316" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_expired_lease_ids(self, limit: int = 100) -> list[UUID]
```

#### `read_lease` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-redis/prefect_redis/lease_storage.py#L203" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_lease(self, lease_id: UUID) -> ResourceLease[ConcurrencyLimitLeaseMetadata] | None
```

#### `renew_lease` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-redis/prefect_redis/lease_storage.py#L218" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
renew_lease(self, lease_id: UUID, ttl: timedelta) -> bool
```

Atomically renew a concurrency lease by updating its expiration.

Uses a Lua script to atomically check if the lease exists, update its expiration
in the lease data, and update the index - all in a single atomic operation,
preventing race conditions from creating orphaned index entries.

**Args:**

* `lease_id`: The ID of the lease to renew
* `ttl`: The new time-to-live duration

**Returns:**

* True if the lease was renewed, False if it didn't exist

#### `revoke_lease` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-redis/prefect_redis/lease_storage.py#L282" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
revoke_lease(self, lease_id: UUID) -> None
```


Built with [Mintlify](https://mintlify.com).