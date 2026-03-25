# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/list_versions_response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.list_versions_response

## Classes

### ListVersionsResponse

```python  theme={"system"}
edgeimpulse_api.models.list_versions_response.ListVersionsResponse(
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

| Class variables                      |                                                                                                                             |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| `Config`                             | ` `                                                                                                                         |
| `custom_learn_blocks`                | `List[edgeimpulse_api.models.list_versions_response_all_of_custom_learn_blocks.ListVersionsResponseAllOfCustomLearnBlocks]` |
| `error`                              | `pydantic.v1.types.StrictStr \| None`                                                                                       |
| `next_version`                       | `pydantic.v1.types.StrictInt`                                                                                               |
| `run_model_testing_while_versioning` | `pydantic.v1.types.StrictBool`                                                                                              |
| `success`                            | `pydantic.v1.types.StrictBool`                                                                                              |
| `versions`                           | `List[edgeimpulse_api.models.list_versions_response_all_of_versions.ListVersionsResponseAllOfVersions]`                     |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.list_versions_response.ListVersionsResponse.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.list_versions_response.ListVersionsResponse
```

Create an instance of ListVersionsResponse from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                              |
| -------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_versions_response.ListVersionsResponse` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.list_versions_response.ListVersionsResponse.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.list_versions_response.ListVersionsResponse
```

Create an instance of ListVersionsResponse from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                              |
| -------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_versions_response.ListVersionsResponse` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.list_versions_response.ListVersionsResponse.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.list_versions_response.ListVersionsResponse.to_json(
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
edgeimpulse_api.models.list_versions_response.ListVersionsResponse.to_str(
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