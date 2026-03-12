# Source: https://docs.prefect.io/v3/api-ref/python/prefect-client-schemas-events.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# events

# `prefect.client.schemas.events`

## Classes

### `EventPage` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/client/schemas/events.py#L12" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

a single page of events returned from the API

**Methods:**

#### `get_next_page` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/client/schemas/events.py#L21" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_next_page(self, client: 'PrefectClient') -> 'EventPage | None'
```

fetch the next page of events.

**Args:**

* `client`: the PrefectClient instance to use for fetching

**Returns:**

* the next EventPage, or None if there are no more pages

#### `get_next_page_sync` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/client/schemas/events.py#L35" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_next_page_sync(self, client: 'SyncPrefectClient') -> 'EventPage | None'
```

fetch the next page of events (sync version).

**Args:**

* `client`: the SyncPrefectClient instance to use for fetching

**Returns:**

* the next EventPage, or None if there are no more pages

#### `model_validate_list` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/_internal/schemas/bases.py#L56" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
model_validate_list(cls, obj: Any) -> list[Self]
```

#### `reset_fields` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/_internal/schemas/bases.py#L85" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
reset_fields(self: Self) -> Self
```

Reset the fields of the model that are in the `_reset_fields` set.

**Returns:**

* A new instance of the model with the reset fields.


Built with [Mintlify](https://mintlify.com).