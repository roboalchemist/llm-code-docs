# Source: https://docs.prefect.io/integrations/prefect-ray/api-ref/prefect_ray-context.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# context

# `prefect_ray.context`

Contexts to manage Ray clusters and tasks.

## Functions

### `remote_options` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-ray/prefect_ray/context.py#L36" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
remote_options(**new_remote_options: Dict[str, Any]) -> Generator[None, Dict[str, Any], None]
```

Context manager to add keyword arguments to Ray `@remote` calls
for task runs. If contexts are nested, new options are merged with options
in the outer context. If a key is present in both, the new option will be used.

**Examples:**

Use 4 CPUs and 2 GPUs for the `process` task:

```python  theme={null}
from prefect import flow, task
from prefect_ray.task_runners import RayTaskRunner
from prefect_ray.context import remote_options

@task
def process(x):
    return x + 1

@flow(task_runner=RayTaskRunner())
def my_flow():
    # equivalent to setting @ray.remote(num_cpus=4, num_gpus=2)
    with remote_options(num_cpus=4, num_gpus=2):
        process.submit(42)
```

## Classes

### `RemoteOptionsContext` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-ray/prefect_ray/context.py#L13" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

The context for Ray remote\_options management.

**Attributes:**

* `current_remote_options`: A set of current remote\_options in the context.

**Methods:**

#### `get` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-ray/prefect_ray/context.py#L25" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get(cls) -> 'RemoteOptionsContext'
```

Return an empty `RemoteOptionsContext`
instead of `None` if no context exists.


Built with [Mintlify](https://mintlify.com).