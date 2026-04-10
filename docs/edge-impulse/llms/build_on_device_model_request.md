# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/build_on_device_model_request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.build_on_device_model_request

## Classes

### BuildOnDeviceModelRequest

```python  theme={"system"}
edgeimpulse_api.models.build_on_device_model_request.BuildOnDeviceModelRequest(
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

| Class variables |                                                                                 |
| --------------- | ------------------------------------------------------------------------------- |
| `Config`        | ` `                                                                             |
| `engine`        | `edgeimpulse_api.models.deployment_target_engine.DeploymentTargetEngine`        |
| `model_type`    | `edgeimpulse_api.models.keras_model_variant_enum.KerasModelVariantEnum \| None` |
| `parameters`    | `Dict[str, pydantic.v1.types.StrictStr] \| None`                                |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.build_on_device_model_request.BuildOnDeviceModelRequest.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.build_on_device_model_request.BuildOnDeviceModelRequest
```

Create an instance of BuildOnDeviceModelRequest from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                          |
| -------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.build_on_device_model_request.BuildOnDeviceModelRequest` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.build_on_device_model_request.BuildOnDeviceModelRequest.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.build_on_device_model_request.BuildOnDeviceModelRequest
```

Create an instance of BuildOnDeviceModelRequest from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                          |
| -------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.build_on_device_model_request.BuildOnDeviceModelRequest` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.build_on_device_model_request.BuildOnDeviceModelRequest.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.build_on_device_model_request.BuildOnDeviceModelRequest.to_json(
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
edgeimpulse_api.models.build_on_device_model_request.BuildOnDeviceModelRequest.to_str(
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