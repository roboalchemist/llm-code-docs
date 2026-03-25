# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-models-variables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# variables

# `prefect.server.models.variables`

## Functions

### `create_variable` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/variables.py#L13" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create_variable(db: PrefectDBInterface, session: AsyncSession, variable: VariableCreate) -> orm_models.Variable
```

Create a variable

**Args:**

* `session`: async database session
* `variable`: variable to create

**Returns:**

* orm\_models.Variable

### `read_variable` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/variables.py#L34" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_variable(db: PrefectDBInterface, session: AsyncSession, variable_id: UUID) -> Optional[orm_models.Variable]
```

Reads a variable by id.

### `read_variable_by_name` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/variables.py#L48" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_variable_by_name(db: PrefectDBInterface, session: AsyncSession, name: str) -> Optional[orm_models.Variable]
```

Reads a variable by name.

### `read_variables` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/variables.py#L62" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_variables(db: PrefectDBInterface, session: AsyncSession, variable_filter: Optional[filters.VariableFilter] = None, sort: sorting.VariableSort = sorting.VariableSort.NAME_ASC, offset: Optional[int] = None, limit: Optional[int] = None) -> Sequence[orm_models.Variable]
```

Read variables, applying filers.

### `count_variables` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/variables.py#L88" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
count_variables(db: PrefectDBInterface, session: AsyncSession, variable_filter: Optional[filters.VariableFilter] = None) -> int
```

Count variables, applying filters.

### `update_variable` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/variables.py#L107" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
update_variable(db: PrefectDBInterface, session: AsyncSession, variable_id: UUID, variable: VariableUpdate) -> bool
```

Updates a variable by id.

### `update_variable_by_name` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/variables.py#L127" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
update_variable_by_name(db: PrefectDBInterface, session: AsyncSession, name: str, variable: VariableUpdate) -> bool
```

Updates a variable by name.

### `delete_variable` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/variables.py#L144" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete_variable(db: PrefectDBInterface, session: AsyncSession, variable_id: UUID) -> bool
```

Delete a variable by id.

### `delete_variable_by_name` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/variables.py#L158" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete_variable_by_name(db: PrefectDBInterface, session: AsyncSession, name: str) -> bool
```

Delete a variable by name.


Built with [Mintlify](https://mintlify.com).