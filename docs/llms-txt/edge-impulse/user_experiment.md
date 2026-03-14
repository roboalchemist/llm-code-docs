# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/user_experiment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.user_experiment

## Classes

### UserExperiment

```python  theme={"system"}
edgeimpulse_api.models.user_experiment.UserExperiment(
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

| Class variables |                                       |
| --------------- | ------------------------------------- |
| `Config`        | ` `                                   |
| `enabled`       | `pydantic.v1.types.StrictBool`        |
| `help`          | `pydantic.v1.types.StrictStr \| None` |
| `show_to_user`  | `pydantic.v1.types.StrictBool`        |
| `title`         | `pydantic.v1.types.StrictStr`         |
| `type`          | `pydantic.v1.types.StrictStr`         |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.user_experiment.UserExperiment.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.user_experiment.UserExperiment
```

Create an instance of UserExperiment from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                 |
| ------------------------------------------------------- |
| `edgeimpulse_api.models.user_experiment.UserExperiment` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.user_experiment.UserExperiment.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.user_experiment.UserExperiment
```

Create an instance of UserExperiment from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                 |
| ------------------------------------------------------- |
| `edgeimpulse_api.models.user_experiment.UserExperiment` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.user_experiment.UserExperiment.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.user_experiment.UserExperiment.to_json(
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
edgeimpulse_api.models.user_experiment.UserExperiment.to_str(
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