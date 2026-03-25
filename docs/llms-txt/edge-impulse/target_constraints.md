# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/target_constraints.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.target_constraints

## Classes

### TargetConstraints

```python  theme={"system"}
edgeimpulse_api.models.target_constraints.TargetConstraints(
	**data: Any
)
```

Create a new model by parsing and validating input data from keyword arguments.

Raises ValidationError if the input data cannot be parsed to form a valid model.

| Parameters |       |
| ---------- | ----- |
| `**data`   | `Any` |

| Bases                              |
| ---------------------------------- |
| `pydantic.v1.main.BaseModel`       |
| `pydantic.v1.utils.Representation` |

| Class variables            |                                                                                  |
| -------------------------- | -------------------------------------------------------------------------------- |
| `Config`                   | ` `                                                                              |
| `application_budgets`      | `List[edgeimpulse_api.models.application_budget.ApplicationBudget]`              |
| `selected_target_based_on` | `pydantic.v1.types.StrictStr \| None`                                            |
| `target_devices`           | `List[edgeimpulse_api.models.target_constraints_device.TargetConstraintsDevice]` |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.target_constraints.TargetConstraints.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.target_constraints.TargetConstraints
```

Create an instance of TargetConstraints from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                       |
| ------------------------------------------------------------- |
| `edgeimpulse_api.models.target_constraints.TargetConstraints` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.target_constraints.TargetConstraints.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.target_constraints.TargetConstraints
```

Create an instance of TargetConstraints from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                       |
| ------------------------------------------------------------- |
| `edgeimpulse_api.models.target_constraints.TargetConstraints` |

#### selected\_target\_based\_on\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.target_constraints.TargetConstraints.selected_target_based_on_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.target_constraints.TargetConstraints.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.target_constraints.TargetConstraints.to_json(
	self,
	indent=None
) ‑> str
```

Returns the JSON representation of the model using alias

| Parameters    |     |
| ------------- | --- |
| `self`        | ` ` |
| `indent=None` | ` ` |

| Returns |
| ------- |
| `str`   |

#### to\_str

```python  theme={"system"}
edgeimpulse_api.models.target_constraints.TargetConstraints.to_str(
	self
) ‑> str
```

Returns the string representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

| Returns |
| ------- |
| `str`   |


Built with [Mintlify](https://mintlify.com).