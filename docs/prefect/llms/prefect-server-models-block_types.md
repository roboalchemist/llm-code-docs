# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-models-block_types.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# block_types

# `prefect.server.models.block_types`

Functions for interacting with block type ORM objects.
Intended for internal use by the Prefect REST API.

## Functions

### `create_block_type` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/block_types.py#L23" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create_block_type(db: PrefectDBInterface, session: AsyncSession, block_type: Union[schemas.core.BlockType, 'ClientBlockType'], override: bool = False) -> Union[BlockType, None]
```

Create a new block type.

**Args:**

* `session`: A database session
* `block_type`: a block type object

**Returns:**

* an ORM block type model

### `read_block_type` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/block_types.py#L81" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_block_type(db: PrefectDBInterface, session: AsyncSession, block_type_id: UUID) -> Union[BlockType, None]
```

Reads a block type by id.

**Args:**

* `session`: A database session
* `block_type_id`: a block\_type id

**Returns:**

* an ORM block type model

### `read_block_type_by_slug` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/block_types.py#L100" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_block_type_by_slug(db: PrefectDBInterface, session: AsyncSession, block_type_slug: str) -> Union[BlockType, None]
```

Reads a block type by slug.

**Args:**

* `session`: A database session
* `block_type_slug`: a block type slug

**Returns:**

* an ORM block type model

### `read_block_types` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/block_types.py#L121" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_block_types(db: PrefectDBInterface, session: AsyncSession, block_type_filter: Optional[schemas.filters.BlockTypeFilter] = None, block_schema_filter: Optional[schemas.filters.BlockSchemaFilter] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> Sequence[BlockType]
```

Reads block types with an optional limit and offset

Args:

**Returns:**

* List\[BlockType]: List of

### `update_block_type` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/block_types.py#L160" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
update_block_type(db: PrefectDBInterface, session: AsyncSession, block_type_id: Union[str, UUID], block_type: Union[schemas.actions.BlockTypeUpdate, schemas.core.BlockType, 'ClientBlockTypeUpdate', 'ClientBlockType']) -> bool
```

Update a block type by id.

**Args:**

* `session`: A database session
* `block_type_id`: Data to update block type with
* `block_type`: A block type id

**Returns:**

* True if the block type was updated

### `delete_block_type` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/block_types.py#L204" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete_block_type(db: PrefectDBInterface, session: AsyncSession, block_type_id: str) -> bool
```

Delete a block type by id.

**Args:**

* `session`: A database session
* `block_type_id`: A block type id

**Returns:**

* True if the block type was updated


Built with [Mintlify](https://mintlify.com).