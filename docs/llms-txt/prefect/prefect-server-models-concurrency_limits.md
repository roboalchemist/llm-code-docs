# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-models-concurrency_limits.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# concurrency_limits

# `prefect.server.models.concurrency_limits`

Functions for interacting with concurrency limit ORM objects.
Intended for internal use by the Prefect REST API.

## Functions

### `create_concurrency_limit` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/concurrency_limits.py#L22" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create_concurrency_limit(db: PrefectDBInterface, session: AsyncSession, concurrency_limit: schemas.core.ConcurrencyLimit) -> orm_models.ConcurrencyLimit
```

### `read_concurrency_limit` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/concurrency_limits.py#L61" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_concurrency_limit(db: PrefectDBInterface, session: AsyncSession, concurrency_limit_id: UUID) -> Union[orm_models.ConcurrencyLimit, None]
```

Reads a concurrency limit by id. If used for orchestration, simultaneous read race
conditions might allow the concurrency limit to be temporarily exceeded.

### `read_concurrency_limit_by_tag` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/concurrency_limits.py#L80" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_concurrency_limit_by_tag(db: PrefectDBInterface, session: AsyncSession, tag: str) -> Union[orm_models.ConcurrencyLimit, None]
```

Reads a concurrency limit by tag. If used for orchestration, simultaneous read race
conditions might allow the concurrency limit to be temporarily exceeded.

### `reset_concurrency_limit_by_tag` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/concurrency_limits.py#L97" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
reset_concurrency_limit_by_tag(db: PrefectDBInterface, session: AsyncSession, tag: str, slot_override: Optional[List[UUID]] = None) -> Union[orm_models.ConcurrencyLimit, None]
```

Resets a concurrency limit by tag.

### `filter_concurrency_limits_for_orchestration` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/concurrency_limits.py#L118" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
filter_concurrency_limits_for_orchestration(db: PrefectDBInterface, session: AsyncSession, tags: List[str]) -> Sequence[orm_models.ConcurrencyLimit]
```

Filters concurrency limits by tag. This will apply a "select for update" lock on
these rows to prevent simultaneous read race conditions from enabling the
the concurrency limit on these tags from being temporarily exceeded.

### `delete_concurrency_limit` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/concurrency_limits.py#L143" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete_concurrency_limit(db: PrefectDBInterface, session: AsyncSession, concurrency_limit_id: UUID) -> bool
```

### `delete_concurrency_limit_by_tag` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/concurrency_limits.py#L157" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete_concurrency_limit_by_tag(db: PrefectDBInterface, session: AsyncSession, tag: str) -> bool
```

### `read_concurrency_limits` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/concurrency_limits.py#L169" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_concurrency_limits(db: PrefectDBInterface, session: AsyncSession, limit: Optional[int] = None, offset: Optional[int] = None) -> Sequence[orm_models.ConcurrencyLimit]
```

Reads a concurrency limits. If used for orchestration, simultaneous read race
conditions might allow the concurrency limit to be temporarily exceeded.

**Args:**

* `session`: A database session
* `offset`: Query offset
* `limit`: Query limit

**Returns:**

* List\[orm\_models.ConcurrencyLimit]: concurrency limits


Built with [Mintlify](https://mintlify.com).