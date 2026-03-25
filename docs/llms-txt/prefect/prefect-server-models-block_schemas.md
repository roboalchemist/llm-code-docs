# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-models-block_schemas.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# block_schemas

# `prefect.server.models.block_schemas`

Functions for interacting with block schema ORM objects.
Intended for internal use by the Prefect REST API.

## Functions

### `create_block_schema` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/block_schemas.py#L33" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create_block_schema(db: PrefectDBInterface, session: AsyncSession, block_schema: Union[schemas.actions.BlockSchemaCreate, schemas.core.BlockSchema, 'ClientBlockSchemaCreate', 'ClientBlockSchema'], override: bool = False, definitions: Optional[dict[str, Any]] = None) -> Union[BlockSchema, orm_models.BlockSchema]
```

Create a new block schema.

**Args:**

* `session`: A database session
* `block_schema`: a block schema object
* `definitions`: Definitions of fields from block schema fields
  attribute. Used when recursively creating nested block schemas

**Returns:**

* an ORM block schema model

### `delete_block_schema` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/block_schemas.py#L286" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete_block_schema(db: PrefectDBInterface, session: AsyncSession, block_schema_id: UUID) -> bool
```

Delete a block schema by id.

**Args:**

* `session`: A database session
* `block_schema_id`: a block schema id

**Returns:**

* whether or not the block schema was deleted

### `read_block_schema` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/block_schemas.py#L307" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_block_schema(db: PrefectDBInterface, session: AsyncSession, block_schema_id: UUID) -> Union[BlockSchema, None]
```

Reads a block schema by id. Will reconstruct the block schema's fields attribute
to include block schema references.

**Args:**

* `session`: A database session
* `block_schema_id`: a block\_schema id

**Returns:**

* orm\_models..BlockSchema: the block\_schema

### `read_block_schemas` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/block_schemas.py#L592" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_block_schemas(db: PrefectDBInterface, session: AsyncSession, block_schema_filter: Optional[schemas.filters.BlockSchemaFilter] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> List[BlockSchema]
```

Reads block schemas, optionally filtered by type or name.

**Args:**

* `session`: A database session
* `block_schema_filter`: a block schema filter object
* `limit`: query limit
* `offset`: query offset

**Returns:**

* List\[orm\_models.BlockSchema]: the block\_schemas

### `read_block_schema_by_checksum` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/block_schemas.py#L705" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_block_schema_by_checksum(db: PrefectDBInterface, session: AsyncSession, checksum: str, version: Optional[str] = None) -> Optional[BlockSchema]
```

Reads a block\_schema by checksum. Will reconstruct the block schema's fields
attribute to include block schema references.

**Args:**

* `session`: A database session
* `checksum`: a block\_schema checksum
* `version`: A block\_schema version

**Returns:**

* orm\_models.BlockSchema: the block\_schema

### `read_available_block_capabilities` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/block_schemas.py#L786" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_available_block_capabilities(db: PrefectDBInterface, session: AsyncSession) -> List[str]
```

Retrieves a list of all available block capabilities.

**Args:**

* `session`: A database session.

**Returns:**

* List\[str]: List of all available block capabilities.

### `create_block_schema_reference` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/block_schemas.py#L811" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create_block_schema_reference(db: PrefectDBInterface, session: AsyncSession, block_schema_reference: schemas.core.BlockSchemaReference) -> Union[orm_models.BlockSchemaReference, None]
```

Retrieves a list of all available block capabilities.

**Args:**

* `session`: A database session.
* `block_schema_reference`: A block schema reference object.

**Returns:**

* orm\_models.BlockSchemaReference: The created BlockSchemaReference

## Classes

### `MissingBlockTypeException` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/block_schemas.py#L28" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Raised when the block type corresponding to a block schema cannot be found


Built with [Mintlify](https://mintlify.com).