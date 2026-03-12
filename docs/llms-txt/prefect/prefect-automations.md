# Source: https://docs.prefect.io/v3/api-ref/python/prefect-automations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# automations

# `prefect.automations`

## Classes

### `Automation` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/automations.py#L78" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `acreate` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/automations.py#L81" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
acreate(self: Self) -> Self
```

Asynchronously create a new automation.

Examples:

```python  theme={null}
auto_to_create = Automation(
    name="woodchonk",
    trigger=EventTrigger(
        expect={"animal.walked"},
        match={
            "genus": "Marmota",
            "species": "monax",
        },
        posture="Reactive",
        threshold=3,
        within=timedelta(seconds=10),
    ),
    actions=[CancelFlowRun()]
)
created_automation = await auto_to_create.acreate()
```

#### `adelete` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/automations.py#L273" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
adelete(self: Self) -> bool
```

Asynchronously delete an automation.

Examples:

```python  theme={null}
auto = Automation.read(id = 123)
await auto.adelete()
```

#### `adisable` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/automations.py#L320" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
adisable(self: Self) -> bool
```

Asynchronously disable an automation.

**Raises:**

* `ValueError`: If the automation does not have an id
* `PrefectHTTPStatusError`: If the automation cannot be disabled

Example:

```python  theme={null}
auto = await Automation.aread(id = 123)
await auto.adisable()
```

#### `aenable` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/automations.py#L374" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
aenable(self: Self) -> bool
```

Asynchronously enable an automation.

**Raises:**

* `ValueError`: If the automation does not have an id
* `PrefectHTTPStatusError`: If the automation cannot be enabled

Example:

```python  theme={null}
auto = await Automation.aread(id = 123)
await auto.aenable()
```

#### `aread` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/automations.py#L182" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
aread(cls, id: UUID, name: Optional[str] = ...) -> Self
```

#### `aread` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/automations.py#L186" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
aread(cls, id: None = None, name: str = ...) -> Self
```

#### `aread` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/automations.py#L189" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
aread(cls, id: Optional[UUID] = None, name: Optional[str] = None) -> Self
```

Asynchronously read an automation by ID or name.

Examples:

```python  theme={null}
automation = await Automation.aread(name="woodchonk")
```

```python  theme={null}
automation = await Automation.aread(id=UUID("b3514963-02b1-47a5-93d1-6eeb131041cb"))
```

#### `aupdate` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/automations.py#L140" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
aupdate(self: Self) -> None
```

Updates an existing automation.

Examples:

```python  theme={null}
auto = Automation.read(id=123)
auto.name = "new name"
auto.update()
```

#### `create` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/automations.py#L111" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create(self: Self) -> Self
```

Create a new automation.

Examples:

```python  theme={null}
auto_to_create = Automation(
    name="woodchonk",
    trigger=EventTrigger(
        expect={"animal.walked"},
        match={
            "genus": "Marmota",
            "species": "monax",
        },
        posture="Reactive",
        threshold=3,
        within=timedelta(seconds=10),
    ),
    actions=[CancelFlowRun()]
)
created_automation = auto_to_create.create()
```

#### `delete` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/automations.py#L297" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete(self: Self) -> bool
```

Delete an automation.

Examples:

```python  theme={null}
auto = Automation.read(id = 123)
auto.delete()
```

#### `disable` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/automations.py#L347" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
disable(self: Self) -> bool
```

Disable an automation.

**Raises:**

* `ValueError`: If the automation does not have an id
* `PrefectHTTPStatusError`: If the automation cannot be disabled

Example:

```python  theme={null}
auto = Automation.read(id = 123)
auto.disable()
```

#### `enable` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/automations.py#L401" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
enable(self: Self) -> bool
```

Enable an automation.

**Raises:**

* `ValueError`: If the automation does not have an id
* `PrefectHTTPStatusError`: If the automation cannot be enabled

Example:

```python  theme={null}
auto = Automation.read(id = 123)
auto.enable()
```

#### `read` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/automations.py#L228" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read(cls, id: UUID, name: Optional[str] = ...) -> Self
```

#### `read` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/automations.py#L232" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read(cls, id: None = None, name: str = ...) -> Self
```

#### `read` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/automations.py#L236" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read(cls, id: Optional[UUID] = None, name: Optional[str] = None) -> Self
```

Read an automation by ID or name.

Examples:

```python  theme={null}
automation = Automation.read(name="woodchonk")
```

```python  theme={null}
automation = Automation.read(id=UUID("b3514963-02b1-47a5-93d1-6eeb131041cb"))
```

#### `update` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/automations.py#L160" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
update(self: Self)
```

Updates an existing automation.

Examples:

```python  theme={null}
auto = Automation.read(id=123)
auto.name = "new name"
auto.update()
```


Built with [Mintlify](https://mintlify.com).