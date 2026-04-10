# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/dsp_info.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.dsp_info

## Classes

### DSPInfo

```python  theme={"system"}
edgeimpulse_api.models.dsp_info.DSPInfo(
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

| Class variables                    |                                                                 |
| ---------------------------------- | --------------------------------------------------------------- |
| `Config`                           | ` `                                                             |
| `calculate_feature_importance`     | `pydantic.v1.types.StrictBool`                                  |
| `can_calculate_feature_importance` | `pydantic.v1.types.StrictBool`                                  |
| `can_normalize_data`               | `pydantic.v1.types.StrictBool`                                  |
| `classes`                          | `List[pydantic.v1.types.StrictStr]`                             |
| `expected_window_count`            | `pydantic.v1.types.StrictInt`                                   |
| `features`                         | `edgeimpulse_api.models.dsp_info_features.DSPInfoFeatures`      |
| `has_auto_tune`                    | `pydantic.v1.types.StrictBool \| None`                          |
| `has_autotuner_results`            | `pydantic.v1.types.StrictBool \| None`                          |
| `id`                               | `pydantic.v1.types.StrictInt`                                   |
| `input_axes`                       | `List[pydantic.v1.types.StrictStr]`                             |
| `minimum_version_for_autotune`     | `float \| None`                                                 |
| `name`                             | `pydantic.v1.types.StrictStr`                                   |
| `normalize_data`                   | `edgeimpulse_api.models.dsp_normalize_data.DSPNormalizeData`    |
| `performance`                      | `edgeimpulse_api.models.dsp_performance.DspPerformance \| None` |
| `type`                             | `pydantic.v1.types.StrictStr`                                   |
| `uses_state`                       | `pydantic.v1.types.StrictBool \| None`                          |
| `window_length`                    | `pydantic.v1.types.StrictInt`                                   |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.dsp_info.DSPInfo.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.dsp_info.DSPInfo
```

Create an instance of DSPInfo from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                   |
| ----------------------------------------- |
| `edgeimpulse_api.models.dsp_info.DSPInfo` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.dsp_info.DSPInfo.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.dsp_info.DSPInfo
```

Create an instance of DSPInfo from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                   |
| ----------------------------------------- |
| `edgeimpulse_api.models.dsp_info.DSPInfo` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.dsp_info.DSPInfo.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.dsp_info.DSPInfo.to_json(
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
edgeimpulse_api.models.dsp_info.DSPInfo.to_str(
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