# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/get_organization_portal_response_all_of.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.get_organization_portal_response_all_of

## Classes

### GetOrganizationPortalResponseAllOf

```python  theme={"system"}
edgeimpulse_api.models.get_organization_portal_response_all_of.GetOrganizationPortalResponseAllOf(
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

| Class variables    |                                       |
| ------------------ | ------------------------------------- |
| `Config`           | ` `                                   |
| `bucket_id`        | `pydantic.v1.types.StrictInt \| None` |
| `bucket_name`      | `pydantic.v1.types.StrictStr`         |
| `bucket_path`      | `pydantic.v1.types.StrictStr`         |
| `bucket_url`       | `pydantic.v1.types.StrictStr \| None` |
| `description`      | `pydantic.v1.types.StrictStr \| None` |
| `id`               | `pydantic.v1.types.StrictInt`         |
| `name`             | `pydantic.v1.types.StrictStr`         |
| `storage_provider` | `pydantic.v1.types.StrictStr \| None` |
| `token`            | `pydantic.v1.types.StrictStr`         |
| `url`              | `pydantic.v1.types.StrictStr`         |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_organization_portal_response_all_of.GetOrganizationPortalResponseAllOf.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.get_organization_portal_response_all_of.GetOrganizationPortalResponseAllOf
```

Create an instance of GetOrganizationPortalResponseAllOf from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                             |
| --------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_organization_portal_response_all_of.GetOrganizationPortalResponseAllOf` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.get_organization_portal_response_all_of.GetOrganizationPortalResponseAllOf.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.get_organization_portal_response_all_of.GetOrganizationPortalResponseAllOf
```

Create an instance of GetOrganizationPortalResponseAllOf from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                             |
| --------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_organization_portal_response_all_of.GetOrganizationPortalResponseAllOf` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_organization_portal_response_all_of.GetOrganizationPortalResponseAllOf.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.get_organization_portal_response_all_of.GetOrganizationPortalResponseAllOf.to_json(
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
edgeimpulse_api.models.get_organization_portal_response_all_of.GetOrganizationPortalResponseAllOf.to_str(
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