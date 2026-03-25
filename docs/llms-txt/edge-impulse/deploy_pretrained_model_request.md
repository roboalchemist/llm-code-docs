# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/deploy_pretrained_model_request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.deploy_pretrained_model_request

## Classes

### DeployPretrainedModelRequest

```python  theme={"system"}
edgeimpulse_api.models.deploy_pretrained_model_request.DeployPretrainedModelRequest(
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

| Class variables                  |                                                                                                           |
| -------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `Config`                         | ` `                                                                                                       |
| `deploy_model_type`              | `pydantic.v1.types.StrictStr \| None`                                                                     |
| `deployment_type`                | `pydantic.v1.types.StrictStr`                                                                             |
| `engine`                         | `edgeimpulse_api.models.deployment_target_engine.DeploymentTargetEngine \| None`                          |
| `model_file_base64`              | `pydantic.v1.types.StrictStr`                                                                             |
| `model_file_type`                | `pydantic.v1.types.StrictStr`                                                                             |
| `model_info`                     | `edgeimpulse_api.models.deploy_pretrained_model_request_model_info.DeployPretrainedModelRequestModelInfo` |
| `override_input_shape`           | `List[pydantic.v1.types.StrictInt] \| None`                                                               |
| `representative_features_base64` | `pydantic.v1.types.StrictStr \| None`                                                                     |
| `use_converter`                  | `pydantic.v1.types.StrictStr \| None`                                                                     |

***

**STATIC METHODS**

#### deploy\_model\_type\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.deploy_pretrained_model_request.DeployPretrainedModelRequest.deploy_model_type_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.deploy_pretrained_model_request.DeployPretrainedModelRequest.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.deploy_pretrained_model_request.DeployPretrainedModelRequest
```

Create an instance of DeployPretrainedModelRequest from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                               |
| ------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.deploy_pretrained_model_request.DeployPretrainedModelRequest` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.deploy_pretrained_model_request.DeployPretrainedModelRequest.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.deploy_pretrained_model_request.DeployPretrainedModelRequest
```

Create an instance of DeployPretrainedModelRequest from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                               |
| ------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.deploy_pretrained_model_request.DeployPretrainedModelRequest` |

#### model\_file\_type\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.deploy_pretrained_model_request.DeployPretrainedModelRequest.model_file_type_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

#### use\_converter\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.deploy_pretrained_model_request.DeployPretrainedModelRequest.use_converter_validate_enum(
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
edgeimpulse_api.models.deploy_pretrained_model_request.DeployPretrainedModelRequest.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.deploy_pretrained_model_request.DeployPretrainedModelRequest.to_json(
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
edgeimpulse_api.models.deploy_pretrained_model_request.DeployPretrainedModelRequest.to_str(
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