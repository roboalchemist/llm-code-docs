# Source: https://docs.prefect.io/v3/api-ref/python/prefect-deployments-schedules.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# schedules

# `prefect.deployments.schedules`

## Functions

### `create_deployment_schedule_create` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/deployments/schedules.py#L18" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create_deployment_schedule_create(schedule: Union['SCHEDULE_TYPES', 'Schedule'], active: Optional[bool] = True) -> DeploymentScheduleCreate
```

Create a DeploymentScheduleCreate object from common schedule parameters.

### `normalize_to_deployment_schedule` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/deployments/schedules.py#L32" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
normalize_to_deployment_schedule(schedules: Optional['FlexibleScheduleList']) -> List[Union[DeploymentScheduleCreate, DeploymentScheduleUpdate]]
```


Built with [Mintlify](https://mintlify.com).