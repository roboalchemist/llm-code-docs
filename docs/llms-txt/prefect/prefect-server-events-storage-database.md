# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-events-storage-database.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# database

# `prefect.server.events.storage.database`

## Functions

### `build_distinct_queries` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/storage/database.py#L35" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
build_distinct_queries(db: PrefectDBInterface, events_filter: EventFilter) -> list[sa.Column['ORMEvent']]
```

### `query_events` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/storage/database.py#L47" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
query_events(session: AsyncSession, filter: EventFilter, page_size: int = INTERACTIVE_PAGE_SIZE) -> tuple[list[ReceivedEvent], int, Optional[str]]
```

### `query_next_page` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/storage/database.py#L60" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
query_next_page(session: AsyncSession, page_token: str) -> tuple[list[ReceivedEvent], int, Optional[str]]
```

### `count_events` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/storage/database.py#L72" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
count_events(session: AsyncSession, filter: EventFilter, countable: Countable, time_unit: TimeUnit, time_interval: float) -> list[EventCount]
```

### `raw_count_events` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/storage/database.py#L97" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
raw_count_events(db: PrefectDBInterface, session: AsyncSession, events_filter: EventFilter) -> int
```

Count events from the database with the given filter.

Only returns the count and does not return any addition metadata. For additional
metadata, use `count_events`.

**Args:**

* `session`: a database session
* `events_filter`: filter criteria for events

**Returns:**

* The count of events in the database that match the filter criteria.

### `read_events` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/storage/database.py#L130" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_events(db: PrefectDBInterface, session: AsyncSession, events_filter: EventFilter, limit: Optional[int] = None, offset: Optional[int] = None) -> Sequence['ORMEvent']
```

Read events from the Postgres database.

**Args:**

* `session`: a Postgres events session.
* `filter`: filter criteria for events.
* `limit`: limit for the query.
* `offset`: offset for the query.

**Returns:**

* A list of events ORM objects.

### `write_events` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/storage/database.py#L200" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
write_events(session: AsyncSession, events: list[ReceivedEvent]) -> None
```

Write events to the database.

**Args:**

* `session`: a database session
* `events`: the events to insert

### `get_max_query_parameters` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/storage/database.py#L288" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_max_query_parameters() -> int
```

### `get_number_of_event_fields` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/storage/database.py#L297" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_number_of_event_fields() -> int
```

### `get_number_of_resource_fields` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/storage/database.py#L302" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_number_of_resource_fields() -> int
```


Built with [Mintlify](https://mintlify.com).