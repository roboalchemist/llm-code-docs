# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/profile_model_info.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.profile_model_info

## Classes

### ProfileModelInfo

```python  theme={"system"}
edgeimpulse_api.models.profile_model_info.ProfileModelInfo(
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

| Class variables          |                                                                                   |
| ------------------------ | --------------------------------------------------------------------------------- |
| `Config`                 | ` `                                                                               |
| `custom_metrics`         | `List[edgeimpulse_api.models.keras_custom_metric.KerasCustomMetric]`              |
| `device`                 | `pydantic.v1.types.StrictStr`                                                     |
| `has_performance`        | `pydantic.v1.types.StrictBool`                                                    |
| `is_supported_on_mcu`    | `pydantic.v1.types.StrictBool`                                                    |
| `mcu_support_error`      | `pydantic.v1.types.StrictStr \| None`                                             |
| `memory`                 | `edgeimpulse_api.models.profile_model_info_memory.ProfileModelInfoMemory \| None` |
| `profiling_error`        | `pydantic.v1.types.StrictStr \| None`                                             |
| `tflite_file_size_bytes` | `pydantic.v1.types.StrictInt`                                                     |
| `time_per_inference_ms`  | `pydantic.v1.types.StrictInt \| None`                                             |
| `variant`                | `edgeimpulse_api.models.keras_model_variant_enum.KerasModelVariantEnum`           |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.profile_model_info.ProfileModelInfo.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.profile_model_info.ProfileModelInfo
```

Create an instance of ProfileModelInfo from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.profile_model_info.ProfileModelInfo` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.profile_model_info.ProfileModelInfo.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.profile_model_info.ProfileModelInfo
```

Create an instance of ProfileModelInfo from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.profile_model_info.ProfileModelInfo` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.profile_model_info.ProfileModelInfo.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.profile_model_info.ProfileModelInfo.to_json(
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
edgeimpulse_api.models.profile_model_info.ProfileModelInfo.to_str(
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