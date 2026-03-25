# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/preview_ai_actions_samples_request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.preview_ai_actions_samples_request

## Classes

### PreviewAIActionsSamplesRequest

```python  theme={"system"}
edgeimpulse_api.models.preview_ai_actions_samples_request.PreviewAIActionsSamplesRequest(
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

| Class variables          |                                                                         |
| ------------------------ | ----------------------------------------------------------------------- |
| `Config`                 | ` `                                                                     |
| `data_category`          | `edgeimpulse_api.models.ai_actions_data_category.AIActionsDataCategory` |
| `data_metadata_key`      | `pydantic.v1.types.StrictStr \| None`                                   |
| `data_metadata_value`    | `pydantic.v1.types.StrictStr \| None`                                   |
| `max_data_preview_count` | `pydantic.v1.types.StrictInt`                                           |
| `save_config`            | `pydantic.v1.types.StrictBool`                                          |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.preview_ai_actions_samples_request.PreviewAIActionsSamplesRequest.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.preview_ai_actions_samples_request.PreviewAIActionsSamplesRequest
```

Create an instance of PreviewAIActionsSamplesRequest from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                    |
| ------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.preview_ai_actions_samples_request.PreviewAIActionsSamplesRequest` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.preview_ai_actions_samples_request.PreviewAIActionsSamplesRequest.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.preview_ai_actions_samples_request.PreviewAIActionsSamplesRequest
```

Create an instance of PreviewAIActionsSamplesRequest from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                    |
| ------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.preview_ai_actions_samples_request.PreviewAIActionsSamplesRequest` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.preview_ai_actions_samples_request.PreviewAIActionsSamplesRequest.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.preview_ai_actions_samples_request.PreviewAIActionsSamplesRequest.to_json(
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
edgeimpulse_api.models.preview_ai_actions_samples_request.PreviewAIActionsSamplesRequest.to_str(
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