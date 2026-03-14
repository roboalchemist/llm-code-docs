# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/set_impulse_thresholds_request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.set_impulse_thresholds_request

## Classes

### SetImpulseThresholdsRequest

```python  theme={"system"}
edgeimpulse_api.models.set_impulse_thresholds_request.SetImpulseThresholdsRequest(
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

| Class variables                                |                                                                                                                           |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `Config`                                       | ` `                                                                                                                       |
| `allow_creating_regenerate_model_testing_jobs` | `pydantic.v1.types.StrictBool`                                                                                            |
| `force_run_regenerate_model_testing_in_job`    | `pydantic.v1.types.StrictBool \| None`                                                                                    |
| `thresholds`                                   | `List[edgeimpulse_api.models.set_impulse_thresholds_request_thresholds_inner.SetImpulseThresholdsRequestThresholdsInner]` |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.set_impulse_thresholds_request.SetImpulseThresholdsRequest.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.set_impulse_thresholds_request.SetImpulseThresholdsRequest
```

Create an instance of SetImpulseThresholdsRequest from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                             |
| ----------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.set_impulse_thresholds_request.SetImpulseThresholdsRequest` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.set_impulse_thresholds_request.SetImpulseThresholdsRequest.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.set_impulse_thresholds_request.SetImpulseThresholdsRequest
```

Create an instance of SetImpulseThresholdsRequest from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                             |
| ----------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.set_impulse_thresholds_request.SetImpulseThresholdsRequest` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.set_impulse_thresholds_request.SetImpulseThresholdsRequest.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.set_impulse_thresholds_request.SetImpulseThresholdsRequest.to_json(
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
edgeimpulse_api.models.set_impulse_thresholds_request.SetImpulseThresholdsRequest.to_str(
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