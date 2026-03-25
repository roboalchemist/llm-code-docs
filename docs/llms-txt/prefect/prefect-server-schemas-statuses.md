# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-schemas-statuses.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# statuses

# `prefect.server.schemas.statuses`

## Classes

### `WorkPoolStatus` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/schemas/statuses.py#L4" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Enumeration of work pool statuses.

**Methods:**

#### `auto` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/collections.py#L70" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
auto() -> str
```

Exposes `enum.auto()` to avoid requiring a second import to use `AutoEnum`

#### `in_kebab_case` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/schemas/statuses.py#L11" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
in_kebab_case(self) -> str
```

### `WorkerStatus` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/schemas/statuses.py#L15" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Enumeration of worker statuses.

**Methods:**

#### `auto` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/collections.py#L70" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
auto() -> str
```

Exposes `enum.auto()` to avoid requiring a second import to use `AutoEnum`

### `DeploymentStatus` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/schemas/statuses.py#L22" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Enumeration of deployment statuses.

**Methods:**

#### `auto` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/collections.py#L70" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
auto() -> str
```

Exposes `enum.auto()` to avoid requiring a second import to use `AutoEnum`

#### `in_kebab_case` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/schemas/statuses.py#L28" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
in_kebab_case(self) -> str
```

### `WorkQueueStatus` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/schemas/statuses.py#L32" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Enumeration of work queue statuses.

**Methods:**

#### `auto` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/collections.py#L70" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
auto() -> str
```

Exposes `enum.auto()` to avoid requiring a second import to use `AutoEnum`

#### `in_kebab_case` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/schemas/statuses.py#L39" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
in_kebab_case(self) -> str
```


Built with [Mintlify](https://mintlify.com).