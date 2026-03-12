# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-events-models-automations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# automations

# `prefect.server.events.models.automations`

## Functions

### `automations_session` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/models/automations.py#L34" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
automations_session(db: PrefectDBInterface, begin_transaction: bool = False) -> AsyncGenerator[AsyncSession, None]
```

### `read_automations_for_workspace` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/models/automations.py#L42" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_automations_for_workspace(db: PrefectDBInterface, session: AsyncSession, sort: AutomationSort = AutomationSort.NAME_ASC, limit: Optional[int] = None, offset: Optional[int] = None, automation_filter: Optional[filters.AutomationFilter] = None) -> Sequence[Automation]
```

### `count_automations_for_workspace` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/models/automations.py#L70" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
count_automations_for_workspace(db: PrefectDBInterface, session: AsyncSession) -> int
```

### `read_automation` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/models/automations.py#L82" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_automation(db: PrefectDBInterface, session: AsyncSession, automation_id: UUID) -> Optional[Automation]
```

### `read_automation_by_id` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/models/automations.py#L96" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_automation_by_id(db: PrefectDBInterface, session: AsyncSession, automation_id: UUID) -> Optional[Automation]
```

### `create_automation` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/models/automations.py#L168" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create_automation(db: PrefectDBInterface, session: AsyncSession, automation: Automation) -> Automation
```

### `update_automation` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/models/automations.py#L183" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
update_automation(db: PrefectDBInterface, session: AsyncSession, automation_update: Union[AutomationUpdate, AutomationPartialUpdate], automation_id: UUID) -> bool
```

### `delete_automation` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/models/automations.py#L227" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete_automation(db: PrefectDBInterface, session: AsyncSession, automation_id: UUID) -> bool
```

### `delete_automations_for_workspace` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/models/automations.py#L267" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete_automations_for_workspace(db: PrefectDBInterface, session: AsyncSession) -> bool
```

### `disable_automations_for_workspace` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/models/automations.py#L289" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
disable_automations_for_workspace(db: PrefectDBInterface, session: AsyncSession) -> bool
```

### `disable_automation` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/models/automations.py#L301" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
disable_automation(db: PrefectDBInterface, session: AsyncSession, automation_id: UUID) -> bool
```

### `relate_automation_to_resource` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/models/automations.py#L354" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
relate_automation_to_resource(db: PrefectDBInterface, session: AsyncSession, automation_id: UUID, resource_id: str, owned_by_resource: bool) -> None
```

### `read_automations_related_to_resource` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/models/automations.py#L385" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_automations_related_to_resource(db: PrefectDBInterface, session: AsyncSession, resource_id: str, owned_by_resource: Optional[bool] = None, automation_filter: Optional[filters.AutomationFilter] = None) -> Sequence[Automation]
```

### `delete_automations_owned_by_resource` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/models/automations.py#L416" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete_automations_owned_by_resource(db: PrefectDBInterface, session: AsyncSession, resource_id: str, automation_filter: Optional[filters.AutomationFilter] = None) -> Sequence[UUID]
```


Built with [Mintlify](https://mintlify.com).