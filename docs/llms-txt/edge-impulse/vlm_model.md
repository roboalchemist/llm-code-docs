# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/vlm_model.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.vlm_model

## Classes

### VlmModel

```python  theme={"system"}
edgeimpulse_api.models.vlm_model.VlmModel(
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

| Class variables               |                                                                                      |
| ----------------------------- | ------------------------------------------------------------------------------------ |
| `Config`                      | ` `                                                                                  |
| `available_prompt_components` | `List[List[edgeimpulse_api.models.vlm_prompt_component.VlmPromptComponent]] \| None` |
| `default_parameters`          | `List[edgeimpulse_api.models.dsp_group.DSPGroup]`                                    |
| `description`                 | `pydantic.v1.types.StrictStr`                                                        |
| `model_id`                    | `float`                                                                              |
| `model_name`                  | `pydantic.v1.types.StrictStr`                                                        |
| `requires_warmup`             | `pydantic.v1.types.StrictBool \| None`                                               |
| `type`                        | `edgeimpulse_api.models.vlm_model_type.VlmModelType`                                 |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.vlm_model.VlmModel.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.vlm_model.VlmModel
```

Create an instance of VlmModel from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                     |
| ------------------------------------------- |
| `edgeimpulse_api.models.vlm_model.VlmModel` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.vlm_model.VlmModel.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.vlm_model.VlmModel
```

Create an instance of VlmModel from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                     |
| ------------------------------------------- |
| `edgeimpulse_api.models.vlm_model.VlmModel` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.vlm_model.VlmModel.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.vlm_model.VlmModel.to_json(
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
edgeimpulse_api.models.vlm_model.VlmModel.to_str(
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