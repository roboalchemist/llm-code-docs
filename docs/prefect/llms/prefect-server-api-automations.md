# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-api-automations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# automations

# `prefect.server.api.automations`

## Functions

### `create_automation` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/automations.py#L39" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create_automation(automation: AutomationCreate, db: PrefectDBInterface = Depends(provide_database_interface)) -> Automation
```

Create an automation.

For more information, see [https://docs.prefect.io/v3/concepts/automations](https://docs.prefect.io/v3/concepts/automations).

### `update_automation` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/automations.py#L96" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
update_automation(automation: AutomationUpdate, automation_id: UUID = Path(..., alias='id'), db: PrefectDBInterface = Depends(provide_database_interface)) -> None
```

### `patch_automation` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/automations.py#L139" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
patch_automation(automation: AutomationPartialUpdate, automation_id: UUID = Path(..., alias='id'), db: PrefectDBInterface = Depends(provide_database_interface)) -> None
```

### `delete_automation` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/automations.py#L165" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete_automation(automation_id: UUID = Path(..., alias='id'), db: PrefectDBInterface = Depends(provide_database_interface)) -> None
```

### `read_automations` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/automations.py#L180" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_automations(sort: AutomationSort = Body(AutomationSort.NAME_ASC), limit: int = LimitBody(), offset: int = Body(0, ge=0), automations: Optional[AutomationFilter] = None, db: PrefectDBInterface = Depends(provide_database_interface)) -> Sequence[Automation]
```

### `count_automations` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/automations.py#L198" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
count_automations(db: PrefectDBInterface = Depends(provide_database_interface)) -> int
```

### `read_automation` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/automations.py#L206" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_automation(automation_id: UUID = Path(..., alias='id'), db: PrefectDBInterface = Depends(provide_database_interface)) -> Automation
```

### `read_automations_related_to_resource` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/automations.py#L222" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_automations_related_to_resource(resource_id: str = Path(..., alias='resource_id'), db: PrefectDBInterface = Depends(provide_database_interface)) -> Sequence[Automation]
```

### `delete_automations_owned_by_resource` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/automations.py#L234" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete_automations_owned_by_resource(resource_id: str = Path(..., alias='resource_id'), db: PrefectDBInterface = Depends(provide_database_interface)) -> None
```


Built with [Mintlify](https://mintlify.com).