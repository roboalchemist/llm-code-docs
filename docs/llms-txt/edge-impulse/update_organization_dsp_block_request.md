# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/update_organization_dsp_block_request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.update_organization_dsp_block_request

## Classes

### UpdateOrganizationDspBlockRequest

```python  theme={"system"}
edgeimpulse_api.models.update_organization_dsp_block_request.UpdateOrganizationDspBlockRequest(
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

| Class variables                   |                                        |
| --------------------------------- | -------------------------------------- |
| `Config`                          | ` `                                    |
| `description`                     | `pydantic.v1.types.StrictStr \| None`  |
| `docker_container`                | `pydantic.v1.types.StrictStr \| None`  |
| `limits_cpu`                      | `float \| None`                        |
| `limits_memory`                   | `pydantic.v1.types.StrictInt \| None`  |
| `name`                            | `pydantic.v1.types.StrictStr \| None`  |
| `port`                            | `pydantic.v1.types.StrictInt \| None`  |
| `requests_cpu`                    | `float \| None`                        |
| `requests_memory`                 | `pydantic.v1.types.StrictInt \| None`  |
| `source_code_download_staff_only` | `pydantic.v1.types.StrictBool \| None` |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.update_organization_dsp_block_request.UpdateOrganizationDspBlockRequest.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.update_organization_dsp_block_request.UpdateOrganizationDspBlockRequest
```

Create an instance of UpdateOrganizationDspBlockRequest from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                          |
| ------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.update_organization_dsp_block_request.UpdateOrganizationDspBlockRequest` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.update_organization_dsp_block_request.UpdateOrganizationDspBlockRequest.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.update_organization_dsp_block_request.UpdateOrganizationDspBlockRequest
```

Create an instance of UpdateOrganizationDspBlockRequest from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                          |
| ------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.update_organization_dsp_block_request.UpdateOrganizationDspBlockRequest` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.update_organization_dsp_block_request.UpdateOrganizationDspBlockRequest.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.update_organization_dsp_block_request.UpdateOrganizationDspBlockRequest.to_json(
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
edgeimpulse_api.models.update_organization_dsp_block_request.UpdateOrganizationDspBlockRequest.to_str(
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