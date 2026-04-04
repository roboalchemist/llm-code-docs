# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-models-saved_searches.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# saved_searches

# `prefect.server.models.saved_searches`

Functions for interacting with saved search ORM objects.
Intended for internal use by the Prefect REST API.

## Functions

### `create_saved_search` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/saved_searches.py#L18" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create_saved_search(db: PrefectDBInterface, session: AsyncSession, saved_search: schemas.core.SavedSearch) -> orm_models.SavedSearch
```

Upserts a SavedSearch.

If a SavedSearch with the same name exists, all properties will be updated.

**Args:**

* `session`: a database session
* `saved_search`: a SavedSearch model

**Returns:**

* orm\_models.SavedSearch: the newly-created or updated SavedSearch

### `read_saved_search` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/saved_searches.py#L61" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_saved_search(db: PrefectDBInterface, session: AsyncSession, saved_search_id: UUID) -> Union[orm_models.SavedSearch, None]
```

Reads a SavedSearch by id.

**Args:**

* `session`: A database session
* `saved_search_id`: a SavedSearch id

**Returns:**

* orm\_models.SavedSearch: the SavedSearch

### `read_saved_search_by_name` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/saved_searches.py#L79" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_saved_search_by_name(db: PrefectDBInterface, session: AsyncSession, name: str) -> Union[orm_models.SavedSearch, None]
```

Reads a SavedSearch by name.

**Args:**

* `session`: A database session
* `name`: a SavedSearch name

**Returns:**

* orm\_models.SavedSearch: the SavedSearch

### `read_saved_searches` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/saved_searches.py#L99" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_saved_searches(db: PrefectDBInterface, session: AsyncSession, offset: Optional[int] = None, limit: Optional[int] = None) -> Sequence[orm_models.SavedSearch]
```

Read SavedSearches.

**Args:**

* `session`: A database session
* `offset`: Query offset
* `limit`: Query limit

**Returns:**

* List\[orm\_models.SavedSearch]: SavedSearches

### `delete_saved_search` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/saved_searches.py#L129" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete_saved_search(db: PrefectDBInterface, session: AsyncSession, saved_search_id: UUID) -> bool
```

Delete a SavedSearch by id.

**Args:**

* `session`: A database session
* `saved_search_id`: a SavedSearch id

**Returns:**

* whether or not the SavedSearch was deleted


Built with [Mintlify](https://mintlify.com).