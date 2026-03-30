# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/set_impulse_thresholds_response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.set_impulse_thresholds_response

## Classes

### SetImpulseThresholdsResponse

```python  theme={"system"}
edgeimpulse_api.models.set_impulse_thresholds_response.SetImpulseThresholdsResponse(
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
| `error`                                   | `pydantic.v1.types.StrictStr \| None` |
| `had_model_testing_results`               | `pydantic.v1.types.StrictBool`        |
| `regenerate_model_testing_results_job_id` | `pydantic.v1.types.StrictInt \| None` |
| `regenerate_model_testing_status`         | `pydantic.v1.types.StrictStr`         |
| `success`                                 | `pydantic.v1.types.StrictBool`        |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.set_impulse_thresholds_response.SetImpulseThresholdsResponse.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.set_impulse_thresholds_response.SetImpulseThresholdsResponse
```

Create an instance of SetImpulseThresholdsResponse from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                               |
| ------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.set_impulse_thresholds_response.SetImpulseThresholdsResponse` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.set_impulse_thresholds_response.SetImpulseThresholdsResponse.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.set_impulse_thresholds_response.SetImpulseThresholdsResponse
```

Create an instance of SetImpulseThresholdsResponse from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                               |
| ------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.set_impulse_thresholds_response.SetImpulseThresholdsResponse` |

#### regenerate\_model\_testing\_status\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.set_impulse_thresholds_response.SetImpulseThresholdsResponse.regenerate_model_testing_status_validate_enum(
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
edgeimpulse_api.models.set_impulse_thresholds_response.SetImpulseThresholdsResponse.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.set_impulse_thresholds_response.SetImpulseThresholdsResponse.to_json(
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
edgeimpulse_api.models.set_impulse_thresholds_response.SetImpulseThresholdsResponse.to_str(
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