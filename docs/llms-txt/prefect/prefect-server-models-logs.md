# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-models-logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# logs

# `prefect.server.models.logs`

Functions for interacting with log ORM objects.
Intended for internal use by the Prefect REST API.

## Functions

### `split_logs_into_batches` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/logs.py#L33" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
split_logs_into_batches(logs: Sequence[schemas.actions.LogCreate]) -> Generator[Tuple[LogCreate, ...], None, None]
```

### `create_logs` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/logs.py#L57" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create_logs(db: PrefectDBInterface, session: AsyncSession, logs: Sequence[LogCreate]) -> None
```

Creates new logs

**Args:**

* `session`: a database session
* `logs`: a list of log schemas

**Returns:**

* None

### `read_logs` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/logs.py#L91" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_logs(db: PrefectDBInterface, session: AsyncSession, log_filter: Optional[schemas.filters.LogFilter], offset: Optional[int] = None, limit: Optional[int] = None, sort: schemas.sorting.LogSort = schemas.sorting.LogSort.TIMESTAMP_ASC) -> Sequence[orm_models.Log]
```

Read logs.

**Args:**

* `session`: a database session
* `db`: the database interface
* `log_filter`: only select logs that match these filters
* `offset`: Query offset
* `limit`: Query limit
* `sort`: Query sort

**Returns:**

* List\[orm\_models.Log]: the matching logs

### `delete_logs` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/logs.py#L123" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete_logs(db: PrefectDBInterface, session: AsyncSession, log_filter: schemas.filters.LogFilter) -> int
```


Built with [Mintlify](https://mintlify.com).