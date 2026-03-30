# Source: https://docs.prefect.io/v3/how-to-guides/workflows/access-runtime-info.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# How to access runtime information

Use the `prefect.runtime` module to access runtime information from within a workflow.

```python  theme={null}
from prefect import flow
from prefect.runtime import flow_run


@flow
def moody_workflow(name: str):
    return f"I wish my parents had named me {name} instead of {flow_run.name}."
```

The value of `flow_run.name` will change between workflow runs to match the name of the flow run.

<Note>
  **Attributes of `prefect.runtime` are `None` if a value is not available**

  Attributes of `prefect.runtime` will never error when accessed. If a value is not available, the attribute will be `None`.

  ```python  theme={null}
  from prefect.runtime import flow_run

  assert flow_run.name is None
  ```
</Note>

See the `prefect.runtime` module [reference](/v3/api-ref/python) for all available attributes.


Built with [Mintlify](https://mintlify.com).