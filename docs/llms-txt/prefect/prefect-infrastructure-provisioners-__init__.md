# Source: https://docs.prefect.io/v3/api-ref/python/prefect-infrastructure-provisioners-__init__.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# __init__

# `prefect.infrastructure.provisioners`

## Functions

### `get_infrastructure_provisioner_for_work_pool_type` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/infrastructure/provisioners/__init__.py#L55" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_infrastructure_provisioner_for_work_pool_type(work_pool_type: str) -> Type[Provisioner]
```

Retrieve an instance of the infrastructure provisioner for the given work pool type.

**Args:**

* `work_pool_type`: the work pool type

**Returns:**

* an instance of the infrastructure provisioner for the given work pool type

**Raises:**

* `ValueError`: if the work pool type is not supported

## Classes

### `Provisioner` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/infrastructure/provisioners/__init__.py#L40" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `console` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/infrastructure/provisioners/__init__.py#L42" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
console(self) -> rich.console.Console
```

#### `console` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/infrastructure/provisioners/__init__.py#L45" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
console(self, value: rich.console.Console) -> None
```

#### `provision` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/infrastructure/provisioners/__init__.py#L47" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
provision(self, work_pool_name: str, base_job_template: Dict[str, Any], client: Optional['PrefectClient'] = None) -> Dict[str, Any]
```


Built with [Mintlify](https://mintlify.com).