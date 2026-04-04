# Source: https://docs.prefect.io/v3/api-ref/python/prefect-utilities-schema_tools-hydration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# hydration

# `prefect.utilities.schema_tools.hydration`

## Functions

### `handler` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L172" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
handler(kind: PrefectKind) -> Callable[[Handler], Handler]
```

### `call_handler` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L180" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
call_handler(kind: PrefectKind, obj: dict[str, Any], ctx: HydrationContext) -> Any
```

### `null_handler` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L191" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
null_handler(obj: dict[str, Any], ctx: HydrationContext)
```

### `json_handler` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L200" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
json_handler(obj: dict[str, Any], ctx: HydrationContext)
```

### `jinja_handler` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L226" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
jinja_handler(obj: dict[str, Any], ctx: HydrationContext) -> Any
```

### `workspace_variable_handler` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L257" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
workspace_variable_handler(obj: dict[str, Any], ctx: HydrationContext) -> Any
```

### `hydrate` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L287" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
hydrate(obj: dict[str, Any], ctx: Optional[HydrationContext] = None) -> dict[str, Any]
```

## Classes

### `HydrationContext` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L14" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `build` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L25" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
build(cls, session: AsyncSession, raise_on_error: bool = False, render_jinja: bool = False, render_workspace_variables: bool = False) -> Self
```

### `Placeholder` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L59" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `is_error` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L64" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
is_error(self) -> bool
```

### `RemoveValue` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L68" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `is_error` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L64" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
is_error(self) -> bool
```

### `HydrationError` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L76" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `is_error` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L81" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
is_error(self) -> bool
```

#### `is_error` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L64" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
is_error(self) -> bool
```

#### `message` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L86" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
message(self) -> str
```

### `KeyNotFound` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L96" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `is_error` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L81" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
is_error(self) -> bool
```

#### `key` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L103" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
key(self) -> str
```

#### `message` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L98" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
message(self) -> str
```

#### `message` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L86" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
message(self) -> str
```

### `ValueNotFound` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L107" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `key` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L109" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
key(self) -> str
```

#### `key` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L103" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
key(self) -> str
```

#### `message` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L98" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
message(self) -> str
```

### `TemplateNotFound` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L113" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `key` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L115" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
key(self) -> str
```

#### `key` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L103" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
key(self) -> str
```

#### `message` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L98" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
message(self) -> str
```

### `VariableNameNotFound` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L119" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `key` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L121" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
key(self) -> str
```

#### `key` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L103" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
key(self) -> str
```

#### `message` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L98" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
message(self) -> str
```

### `InvalidJSON` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L125" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `is_error` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L81" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
is_error(self) -> bool
```

#### `message` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L127" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
message(self) -> str
```

#### `message` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L86" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
message(self) -> str
```

### `InvalidJinja` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L134" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `is_error` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L81" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
is_error(self) -> bool
```

#### `message` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L136" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
message(self) -> str
```

#### `message` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L86" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
message(self) -> str
```

### `WorkspaceVariableNotFound` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L143" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `is_error` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L81" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
is_error(self) -> bool
```

#### `message` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L150" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
message(self) -> str
```

#### `message` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L86" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
message(self) -> str
```

#### `variable_name` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L145" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
variable_name(self) -> str
```

### `WorkspaceVariable` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L154" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `is_error` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L64" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
is_error(self) -> bool
```

### `ValidJinja` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L164" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `is_error` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/hydration.py#L64" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
is_error(self) -> bool
```


Built with [Mintlify](https://mintlify.com).