# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/device_inference_info.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.device_inference_info

## Classes

### DeviceInferenceInfo

```python  theme={"system"}
edgeimpulse_api.models.device_inference_info.DeviceInferenceInfo(
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

| Class variables    |                                       |
| ------------------ | ------------------------------------- |
| `Config`           | ` `                                   |
| `deployed_version` | `pydantic.v1.types.StrictInt`         |
| `model_type`       | `pydantic.v1.types.StrictStr \| None` |
| `project_id`       | `pydantic.v1.types.StrictInt`         |
| `project_name`     | `pydantic.v1.types.StrictStr`         |
| `project_owner`    | `pydantic.v1.types.StrictStr`         |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.device_inference_info.DeviceInferenceInfo.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.device_inference_info.DeviceInferenceInfo
```

Create an instance of DeviceInferenceInfo from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.device_inference_info.DeviceInferenceInfo` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.device_inference_info.DeviceInferenceInfo.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.device_inference_info.DeviceInferenceInfo
```

Create an instance of DeviceInferenceInfo from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.device_inference_info.DeviceInferenceInfo` |

#### model\_type\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.device_inference_info.DeviceInferenceInfo.model_type_validate_enum(
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
edgeimpulse_api.models.device_inference_info.DeviceInferenceInfo.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.device_inference_info.DeviceInferenceInfo.to_json(
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
edgeimpulse_api.models.device_inference_info.DeviceInferenceInfo.to_str(
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