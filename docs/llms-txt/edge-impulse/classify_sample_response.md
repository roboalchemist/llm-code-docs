# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/classify_sample_response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.classify_sample_response

## Classes

### ClassifySampleResponse

```python  theme={"system"}
edgeimpulse_api.models.classify_sample_response.ClassifySampleResponse(
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

| Class variables       |                                                                                                             |
| --------------------- | ----------------------------------------------------------------------------------------------------------- |
| `Config`              | ` `                                                                                                         |
| `already_in_database` | `pydantic.v1.types.StrictBool`                                                                              |
| `classifications`     | `List[edgeimpulse_api.models.classify_sample_response_classification.ClassifySampleResponseClassification]` |
| `error`               | `pydantic.v1.types.StrictStr \| None`                                                                       |
| `sample`              | `edgeimpulse_api.models.raw_sample_data.RawSampleData`                                                      |
| `success`             | `pydantic.v1.types.StrictBool`                                                                              |
| `warning`             | `pydantic.v1.types.StrictStr \| None`                                                                       |
| `window_increase_ms`  | `pydantic.v1.types.StrictInt`                                                                               |
| `window_size_ms`      | `pydantic.v1.types.StrictInt`                                                                               |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.classify_sample_response.ClassifySampleResponse.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.classify_sample_response.ClassifySampleResponse
```

Create an instance of ClassifySampleResponse from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                  |
| ------------------------------------------------------------------------ |
| `edgeimpulse_api.models.classify_sample_response.ClassifySampleResponse` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.classify_sample_response.ClassifySampleResponse.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.classify_sample_response.ClassifySampleResponse
```

Create an instance of ClassifySampleResponse from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                  |
| ------------------------------------------------------------------------ |
| `edgeimpulse_api.models.classify_sample_response.ClassifySampleResponse` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.classify_sample_response.ClassifySampleResponse.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.classify_sample_response.ClassifySampleResponse.to_json(
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
edgeimpulse_api.models.classify_sample_response.ClassifySampleResponse.to_str(
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