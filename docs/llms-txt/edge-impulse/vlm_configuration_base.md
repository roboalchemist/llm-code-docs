# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/vlm_configuration_base.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.vlm_configuration_base

## Classes

### VlmConfigurationBase

```python  theme={"system"}
edgeimpulse_api.models.vlm_configuration_base.VlmConfigurationBase(
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

| Class variables        |                                                                                         |
| ---------------------- | --------------------------------------------------------------------------------------- |
| `Config`               | ` `                                                                                     |
| `candidate_labels_map` | `edgeimpulse_api.models.vlm_candidate_label_map.VlmCandidateLabelMap \| None`           |
| `deployment_id`        | `float \| None`                                                                         |
| `model_id`             | `float`                                                                                 |
| `parameters`           | `edgeimpulse_api.models.vlm_prompt_config_parameters.VlmPromptConfigParameters \| None` |
| `prompt_components`    | `edgeimpulse_api.models.vlm_prompt_component_config.VlmPromptComponentConfig \| None`   |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.vlm_configuration_base.VlmConfigurationBase.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.vlm_configuration_base.VlmConfigurationBase
```

Create an instance of VlmConfigurationBase from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                              |
| -------------------------------------------------------------------- |
| `edgeimpulse_api.models.vlm_configuration_base.VlmConfigurationBase` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.vlm_configuration_base.VlmConfigurationBase.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.vlm_configuration_base.VlmConfigurationBase
```

Create an instance of VlmConfigurationBase from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                              |
| -------------------------------------------------------------------- |
| `edgeimpulse_api.models.vlm_configuration_base.VlmConfigurationBase` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.vlm_configuration_base.VlmConfigurationBase.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.vlm_configuration_base.VlmConfigurationBase.to_json(
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
edgeimpulse_api.models.vlm_configuration_base.VlmConfigurationBase.to_str(
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