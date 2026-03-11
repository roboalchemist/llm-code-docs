# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/deploy_pretrained_model_request_model_info_input.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.deploy_pretrained_model_request_model_info_input

## Classes

### DeployPretrainedModelRequestModelInfoInput

```python  theme={"system"}
edgeimpulse_api.models.deploy_pretrained_model_request_model_info_input.DeployPretrainedModelRequestModelInfoInput(
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

| Class variables            |                                                                                                                 |
| -------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `Config`                   | ` `                                                                                                             |
| `actual_instance`          | `Any`                                                                                                           |
| `one_of_schemas`           | `List[str]`                                                                                                     |
| `oneof_schema_1_validator` | `edgeimpulse_api.models.deploy_pretrained_model_input_time_series.DeployPretrainedModelInputTimeSeries \| None` |
| `oneof_schema_2_validator` | `edgeimpulse_api.models.deploy_pretrained_model_input_audio.DeployPretrainedModelInputAudio \| None`            |
| `oneof_schema_3_validator` | `edgeimpulse_api.models.deploy_pretrained_model_input_image.DeployPretrainedModelInputImage \| None`            |
| `oneof_schema_4_validator` | `edgeimpulse_api.models.deploy_pretrained_model_input_other.DeployPretrainedModelInputOther \| None`            |

***

**STATIC METHODS**

#### actual\_instance\_must\_validate\_oneof

```python  theme={"system"}
edgeimpulse_api.models.deploy_pretrained_model_request_model_info_input.DeployPretrainedModelRequestModelInfoInput.actual_instance_must_validate_oneof(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.deploy_pretrained_model_request_model_info_input.DeployPretrainedModelRequestModelInfoInput.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.deploy_pretrained_model_request_model_info_input.DeployPretrainedModelRequestModelInfoInput
```

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.deploy_pretrained_model_request_model_info_input.DeployPretrainedModelRequestModelInfoInput` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.deploy_pretrained_model_request_model_info_input.DeployPretrainedModelRequestModelInfoInput.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.deploy_pretrained_model_request_model_info_input.DeployPretrainedModelRequestModelInfoInput
```

Returns the object represented by the json string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.deploy_pretrained_model_request_model_info_input.DeployPretrainedModelRequestModelInfoInput` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.deploy_pretrained_model_request_model_info_input.DeployPretrainedModelRequestModelInfoInput.to_dict(
	self
) ‑> dict
```

Returns the dict representation of the actual instance

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

| Returns |
| ------- |
| `dict`  |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.deploy_pretrained_model_request_model_info_input.DeployPretrainedModelRequestModelInfoInput.to_json(
	self,
	indent=None
) ‑> str
```

Returns the JSON representation of the actual instance

| Parameters    |     |
| ------------- | --- |
| `self`        | ` ` |
| `indent=None` | ` ` |

| Returns |
| ------- |
| `str`   |

#### to\_str

```python  theme={"system"}
edgeimpulse_api.models.deploy_pretrained_model_request_model_info_input.DeployPretrainedModelRequestModelInfoInput.to_str(
	self
) ‑> str
```

Returns the string representation of the actual instance

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

| Returns |
| ------- |
| `str`   |


Built with [Mintlify](https://mintlify.com).