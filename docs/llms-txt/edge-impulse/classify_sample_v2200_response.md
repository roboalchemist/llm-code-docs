# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/classify_sample_v2200_response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.classify_sample_v2200_response

## Classes

### ClassifySampleV2200Response

```python  theme={"system"}
edgeimpulse_api.models.classify_sample_v2200_response.ClassifySampleV2200Response(
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

| Class variables            |                                                                                  |
| -------------------------- | -------------------------------------------------------------------------------- |
| `Config`                   | ` `                                                                              |
| `actual_instance`          | `Any`                                                                            |
| `any_of_schemas`           | `List[str]`                                                                      |
| `anyof_schema_1_validator` | `edgeimpulse_api.models.classify_sample_response.ClassifySampleResponse \| None` |
| `anyof_schema_2_validator` | `edgeimpulse_api.models.start_job_response.StartJobResponse \| None`             |

***

**STATIC METHODS**

#### actual\_instance\_must\_validate\_anyof

```python  theme={"system"}
edgeimpulse_api.models.classify_sample_v2200_response.ClassifySampleV2200Response.actual_instance_must_validate_anyof(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.classify_sample_v2200_response.ClassifySampleV2200Response.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.classify_sample_v2200_response.ClassifySampleV2200Response
```

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                             |
| ----------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.classify_sample_v2200_response.ClassifySampleV2200Response` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.classify_sample_v2200_response.ClassifySampleV2200Response.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.classify_sample_v2200_response.ClassifySampleV2200Response
```

Returns the object represented by the json string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                             |
| ----------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.classify_sample_v2200_response.ClassifySampleV2200Response` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.classify_sample_v2200_response.ClassifySampleV2200Response.to_dict(
	self
) ‑> dict
```

Returns the dict representation of the actual instance

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

| Returns |
| ------- |
| `dict`  |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.classify_sample_v2200_response.ClassifySampleV2200Response.to_json(
	self,
	indent=None
) ‑> str
```

Returns the JSON representation of the actual instance

| Parameters    |     |
| ------------- | --- |
| `self`        | ` ` |
| `indent=None` | ` ` |

| Returns |
| ------- |
| `str`   |

#### to\_str

```python  theme={"system"}
edgeimpulse_api.models.classify_sample_v2200_response.ClassifySampleV2200Response.to_str(
	self
) ‑> str
```

Returns the string representation of the actual instance

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

| Returns |
| ------- |
| `str`   |


Built with [Mintlify](https://mintlify.com).