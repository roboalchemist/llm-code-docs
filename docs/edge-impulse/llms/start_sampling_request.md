# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/start_sampling_request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.start_sampling_request

## Classes

### StartSamplingRequest

```python  theme={"system"}
edgeimpulse_api.models.start_sampling_request.StartSamplingRequest(
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

| Class variables          |                                                            |
| ------------------------ | ---------------------------------------------------------- |
| `Config`                 | ` `                                                        |
| `category`               | `edgeimpulse_api.models.raw_data_category.RawDataCategory` |
| `collected_sample_count` | `float \| None`                                            |
| `interval_ms`            | `float`                                                    |
| `label`                  | `pydantic.v1.types.StrictStr`                              |
| `label_color`            | `pydantic.v1.types.StrictStr \| None`                      |
| `length_ms`              | `pydantic.v1.types.StrictInt`                              |
| `sensor`                 | `pydantic.v1.types.StrictStr \| None`                      |
| `target_sample_count`    | `float \| None`                                            |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.start_sampling_request.StartSamplingRequest.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.start_sampling_request.StartSamplingRequest
```

Create an instance of StartSamplingRequest from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                              |
| -------------------------------------------------------------------- |
| `edgeimpulse_api.models.start_sampling_request.StartSamplingRequest` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.start_sampling_request.StartSamplingRequest.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.start_sampling_request.StartSamplingRequest
```

Create an instance of StartSamplingRequest from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                              |
| -------------------------------------------------------------------- |
| `edgeimpulse_api.models.start_sampling_request.StartSamplingRequest` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.start_sampling_request.StartSamplingRequest.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.start_sampling_request.StartSamplingRequest.to_json(
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
edgeimpulse_api.models.start_sampling_request.StartSamplingRequest.to_str(
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