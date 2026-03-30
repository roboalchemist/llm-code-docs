# Source: https://docs.prefect.io/v3/api-ref/python/prefect-infrastructure-provisioners-cloud_run.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# cloud_run

# `prefect.infrastructure.provisioners.cloud_run`

## Classes

### `CloudRunPushProvisioner` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/infrastructure/provisioners/cloud_run.py#L33" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `console` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/infrastructure/provisioners/cloud_run.py#L43" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
console(self) -> Console
```

#### `console` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/infrastructure/provisioners/cloud_run.py#L47" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
console(self, value: Console) -> None
```

#### `provision` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/infrastructure/provisioners/cloud_run.py#L302" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
provision(self, work_pool_name: str, base_job_template: dict, client: Optional['PrefectClient'] = None) -> Dict[str, Any]
```


Built with [Mintlify](https://mintlify.com).