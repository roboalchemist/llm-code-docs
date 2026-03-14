# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/list_samples_response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.list_samples_response

## Classes

### ListSamplesResponse

```python  theme={"system"}
edgeimpulse_api.models.list_samples_response.ListSamplesResponse(
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

| Class variables |                                              |
| --------------- | -------------------------------------------- |
| `Config`        | ` `                                          |
| `error`         | `pydantic.v1.types.StrictStr \| None`        |
| `samples`       | `List[edgeimpulse_api.models.sample.Sample]` |
| `success`       | `pydantic.v1.types.StrictBool`               |
| `total_count`   | `pydantic.v1.types.StrictInt`                |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.list_samples_response.ListSamplesResponse.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.list_samples_response.ListSamplesResponse
```

Create an instance of ListSamplesResponse from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.list_samples_response.ListSamplesResponse` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.list_samples_response.ListSamplesResponse.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.list_samples_response.ListSamplesResponse
```

Create an instance of ListSamplesResponse from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.list_samples_response.ListSamplesResponse` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.list_samples_response.ListSamplesResponse.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.list_samples_response.ListSamplesResponse.to_json(
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
edgeimpulse_api.models.list_samples_response.ListSamplesResponse.to_str(
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