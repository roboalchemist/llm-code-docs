# Source: https://docs.prefect.io/v3/how-to-guides/workflows/pass-inputs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# How to pass inputs to a workflow

### Define workflow inputs

Define the inputs to a workflow by adding parameters to the function definition.

```python  theme={null}
from prefect import flow


@flow
def my_workflow(name: str = "World"):
    return f"Hello, {name}!"
```

Pass arguments to the function call to provide inputs to the workflow.

```python  theme={null}
my_workflow(name="Marvin")
```

### Validate inputs

By default, Prefect will validate the types of inputs to your workflow.

```python  theme={null}
from prefect import flow


@flow
def my_workflow(name: str = "World"):
    return f"Hello, {name}!"

my_workflow(name=1) # This will fail with a type validation error
```

To turn off type validation, set the `validate_parameters` parameter to `False`:

```python  theme={null}
from prefect import flow


@flow(validate_parameters=False)
def my_workflow(name: str = "World"):
    return f"Hello, {name}!"

my_workflow(name=1)
```

If you use `pydantic`, parameters typed with a `BaseModel` subclass will be coerced to the appropriate types and validated.

```python  theme={null}
from prefect import flow
from pydantic import BaseModel


class Model(BaseModel):
    a: int
    b: str


@flow
def flow_that_validates_parameters(model: Model): ...

flow_that_validates_parameters(
    model={"a": "WRONG", "b": "fine"}
)
```


Built with [Mintlify](https://mintlify.com).