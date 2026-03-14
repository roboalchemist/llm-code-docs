# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/ai_action.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.ai_action

## Classes

### AIAction

```python  theme={"system"}
edgeimpulse_api.models.ai_action.AIAction(
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
| `cache_unchanged_steps`      | `pydantic.v1.types.StrictBool`                                                                                 |
| `config`                     | `edgeimpulse_api.models.ai_actions_config.AIActionsConfig`                                                     |
| `display_name`               | `pydantic.v1.types.StrictStr`                                                                                  |
| `grid_column_count`          | `pydantic.v1.types.StrictInt`                                                                                  |
| `id`                         | `pydantic.v1.types.StrictInt`                                                                                  |
| `last_preview_state`         | `edgeimpulse_api.models.ai_action_last_preview_state.AIActionLastPreviewState \| None`                         |
| `max_data_preview_count`     | `pydantic.v1.types.StrictInt`                                                                                  |
| `name`                       | `pydantic.v1.types.StrictStr \| None`                                                                          |
| `preview_config`             | `edgeimpulse_api.models.ai_actions_config.AIActionsConfig`                                                     |
| `set_metadata_after_running` | `List[edgeimpulse_api.models.ai_action_set_metadata_after_running_inner.AIActionSetMetadataAfterRunningInner]` |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.ai_action.AIAction.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.ai_action.AIAction
```

Create an instance of AIAction from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                     |
| ------------------------------------------- |
| `edgeimpulse_api.models.ai_action.AIAction` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.ai_action.AIAction.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.ai_action.AIAction
```

Create an instance of AIAction from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                     |
| ------------------------------------------- |
| `edgeimpulse_api.models.ai_action.AIAction` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.ai_action.AIAction.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.ai_action.AIAction.to_json(
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
edgeimpulse_api.models.ai_action.AIAction.to_str(
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