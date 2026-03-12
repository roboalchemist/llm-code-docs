# Source: https://docs.prefect.io/v3/api-ref/python/prefect-runtime-deployment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# deployment

# `prefect.runtime.deployment`

Access attributes of the current deployment run dynamically.

Note that if a deployment is not currently being run, all attributes will return empty values.

You can mock the runtime attributes for testing purposes by setting environment variables
prefixed with `PREFECT__RUNTIME__DEPLOYMENT`.

Example usage:

```python  theme={null}
from prefect.runtime import deployment

def get_task_runner():
    task_runner_config = deployment.parameters.get("runner_config", "default config here")
    return DummyTaskRunner(task_runner_specs=task_runner_config)
```

Available attributes:

* `id`: the deployment's unique ID
* `name`: the deployment's name
* `version`: the deployment's version
* `flow_run_id`: the current flow run ID for this deployment
* `parameters`: the parameters that were passed to this run; note that these do not necessarily
  include default values set on the flow function, only the parameter values set on the deployment
  object or those directly provided via API for this run

## Functions

### `get_id` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/runtime/deployment.py#L107" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_id() -> Optional[str]
```

### `get_parameters` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/runtime/deployment.py#L129" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_parameters() -> dict[str, Any]
```

### `get_name` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/runtime/deployment.py#L144" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_name() -> Optional[str]
```

### `get_version` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/runtime/deployment.py#L156" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_version() -> Optional[str]
```

### `get_flow_run_id` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/runtime/deployment.py#L168" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_flow_run_id() -> Optional[str]
```


Built with [Mintlify](https://mintlify.com).