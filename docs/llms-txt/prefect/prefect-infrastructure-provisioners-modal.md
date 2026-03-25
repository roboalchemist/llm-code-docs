# Source: https://docs.prefect.io/v3/api-ref/python/prefect-infrastructure-provisioners-modal.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# modal

# `prefect.infrastructure.provisioners.modal`

## Classes

### `ModalPushProvisioner` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/infrastructure/provisioners/modal.py#L27" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

A infrastructure provisioner for Modal push work pools.

**Methods:**

#### `console` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/infrastructure/provisioners/modal.py#L36" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
console(self) -> Console
```

#### `console` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/infrastructure/provisioners/modal.py#L40" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
console(self, value: Console) -> None
```

#### `provision` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/infrastructure/provisioners/modal.py#L144" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
provision(self, work_pool_name: str, base_job_template: Dict[str, Any], client: Optional['PrefectClient'] = None) -> Dict[str, Any]
```

Provisions resources necessary for a Modal push work pool.

**Args:**

* `work_pool_name`: The name of the work pool to provision resources for
* `base_job_template`: The base job template to update

**Returns:**

* A copy of the provided base job template with the provisioned resources


Built with [Mintlify](https://mintlify.com).