# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/update_organization_request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.update_organization_request

## Classes

### UpdateOrganizationRequest

```python  theme={"system"}
edgeimpulse_api.models.update_organization_request.UpdateOrganizationRequest(
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

| Class variables        |                                             |
| ---------------------- | ------------------------------------------- |
| `Config`               | ` `                                         |
| `experiments`          | `List[pydantic.v1.types.StrictStr] \| None` |
| `header_img`           | `pydantic.v1.types.StrictStr \| None`       |
| `job_limit_m`          | `pydantic.v1.types.StrictInt \| None`       |
| `logo`                 | `pydantic.v1.types.StrictStr \| None`       |
| `name`                 | `pydantic.v1.types.StrictStr \| None`       |
| `readme`               | `pydantic.v1.types.StrictStr \| None`       |
| `show_header_img_mask` | `pydantic.v1.types.StrictBool \| None`      |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.update_organization_request.UpdateOrganizationRequest.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.update_organization_request.UpdateOrganizationRequest
```

Create an instance of UpdateOrganizationRequest from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                        |
| ------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.update_organization_request.UpdateOrganizationRequest` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.update_organization_request.UpdateOrganizationRequest.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.update_organization_request.UpdateOrganizationRequest
```

Create an instance of UpdateOrganizationRequest from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                        |
| ------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.update_organization_request.UpdateOrganizationRequest` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.update_organization_request.UpdateOrganizationRequest.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.update_organization_request.UpdateOrganizationRequest.to_json(
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
edgeimpulse_api.models.update_organization_request.UpdateOrganizationRequest.to_str(
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