# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/update_ai_action_request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.update_ai_action_request

## Classes

### UpdateAIActionRequest

```python  theme={"system"}
edgeimpulse_api.models.update_ai_action_request.UpdateAIActionRequest(
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

| Class variables              |                                                                                                                |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `Config`                     | ` `                                                                                                            |
| `data_category`              | `edgeimpulse_api.models.ai_actions_data_category.AIActionsDataCategory`                                        |
| `data_metadata_key`          | `pydantic.v1.types.StrictStr \| None`                                                                          |
| `data_metadata_value`        | `pydantic.v1.types.StrictStr \| None`                                                                          |
| `name`                       | `pydantic.v1.types.StrictStr \| None`                                                                          |
| `set_metadata_after_running` | `List[edgeimpulse_api.models.ai_action_set_metadata_after_running_inner.AIActionSetMetadataAfterRunningInner]` |
| `sort_order`                 | `pydantic.v1.types.StrictInt \| None`                                                                          |
| `steps`                      | `List[edgeimpulse_api.models.ai_actions_config_step.AIActionsConfigStep]`                                      |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.update_ai_action_request.UpdateAIActionRequest.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.update_ai_action_request.UpdateAIActionRequest
```

Create an instance of UpdateAIActionRequest from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                 |
| ----------------------------------------------------------------------- |
| `edgeimpulse_api.models.update_ai_action_request.UpdateAIActionRequest` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.update_ai_action_request.UpdateAIActionRequest.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.update_ai_action_request.UpdateAIActionRequest
```

Create an instance of UpdateAIActionRequest from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                 |
| ----------------------------------------------------------------------- |
| `edgeimpulse_api.models.update_ai_action_request.UpdateAIActionRequest` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.update_ai_action_request.UpdateAIActionRequest.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.update_ai_action_request.UpdateAIActionRequest.to_json(
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
edgeimpulse_api.models.update_ai_action_request.UpdateAIActionRequest.to_str(
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