# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-api-saved_searches.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# saved_searches

# `prefect.server.api.saved_searches`

Routes for interacting with saved search objects.

## Functions

### `create_saved_search` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/saved_searches.py#L21" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create_saved_search(saved_search: schemas.actions.SavedSearchCreate, response: Response, db: PrefectDBInterface = Depends(provide_database_interface)) -> schemas.core.SavedSearch
```

Creates a new saved search from the provided schema.

If a saved search with the same name already exists, the saved search's fields are
replaced.

### `read_saved_search` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/saved_searches.py#L49" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_saved_search(saved_search_id: UUID = Path(..., description='The saved search id', alias='id'), db: PrefectDBInterface = Depends(provide_database_interface)) -> schemas.core.SavedSearch
```

Get a saved search by id.

### `read_saved_searches` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/saved_searches.py#L68" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_saved_searches(limit: int = dependencies.LimitBody(), offset: int = Body(0, ge=0), db: PrefectDBInterface = Depends(provide_database_interface)) -> List[schemas.core.SavedSearch]
```

Query for saved searches.

### `delete_saved_search` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/saved_searches.py#L85" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete_saved_search(saved_search_id: UUID = Path(..., description='The saved search id', alias='id'), db: PrefectDBInterface = Depends(provide_database_interface)) -> None
```

Delete a saved search by id.


Built with [Mintlify](https://mintlify.com).