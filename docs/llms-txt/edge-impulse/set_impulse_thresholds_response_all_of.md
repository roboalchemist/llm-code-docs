# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/set_impulse_thresholds_response_all_of.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.set_impulse_thresholds_response_all_of

## Classes

### SetImpulseThresholdsResponseAllOf

```python  theme={"system"}
edgeimpulse_api.models.set_impulse_thresholds_response_all_of.SetImpulseThresholdsResponseAllOf(
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

| Class variables                           |                                       |
| ----------------------------------------- | ------------------------------------- |
| `Config`                                  | ` `                                   |
| `had_model_testing_results`               | `pydantic.v1.types.StrictBool`        |
| `regenerate_model_testing_results_job_id` | `pydantic.v1.types.StrictInt \| None` |
| `regenerate_model_testing_status`         | `pydantic.v1.types.StrictStr`         |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.set_impulse_thresholds_response_all_of.SetImpulseThresholdsResponseAllOf.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.set_impulse_thresholds_response_all_of.SetImpulseThresholdsResponseAllOf
```

Create an instance of SetImpulseThresholdsResponseAllOf from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                           |
| ------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.set_impulse_thresholds_response_all_of.SetImpulseThresholdsResponseAllOf` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.set_impulse_thresholds_response_all_of.SetImpulseThresholdsResponseAllOf.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.set_impulse_thresholds_response_all_of.SetImpulseThresholdsResponseAllOf
```

Create an instance of SetImpulseThresholdsResponseAllOf from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                           |
| ------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.set_impulse_thresholds_response_all_of.SetImpulseThresholdsResponseAllOf` |

#### regenerate\_model\_testing\_status\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.set_impulse_thresholds_response_all_of.SetImpulseThresholdsResponseAllOf.regenerate_model_testing_status_validate_enum(
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
edgeimpulse_api.models.set_impulse_thresholds_response_all_of.SetImpulseThresholdsResponseAllOf.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.set_impulse_thresholds_response_all_of.SetImpulseThresholdsResponseAllOf.to_json(
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
edgeimpulse_api.models.set_impulse_thresholds_response_all_of.SetImpulseThresholdsResponseAllOf.to_str(
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