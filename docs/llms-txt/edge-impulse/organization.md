# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/organization.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.organization

## Classes

### Organization

```python  theme={"system"}
edgeimpulse_api.models.organization.Organization(
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

| Class variables        |                                                                   |
| ---------------------- | ----------------------------------------------------------------- |
| `Config`               | ` `                                                               |
| `contract_start_date`  | `datetime.datetime \| None`                                       |
| `created`              | `datetime.datetime`                                               |
| `deleted_date`         | `datetime.datetime \| None`                                       |
| `header_img`           | `pydantic.v1.types.StrictStr \| None`                             |
| `id`                   | `pydantic.v1.types.StrictInt`                                     |
| `is_developer_profile` | `pydantic.v1.types.StrictBool`                                    |
| `logo`                 | `pydantic.v1.types.StrictStr \| None`                             |
| `name`                 | `pydantic.v1.types.StrictStr`                                     |
| `projects`             | `List[edgeimpulse_api.models.project.Project] \| None`            |
| `show_header_img_mask` | `pydantic.v1.types.StrictBool`                                    |
| `trial_expired_date`   | `datetime.datetime \| None`                                       |
| `trial_id`             | `pydantic.v1.types.StrictInt \| None`                             |
| `trial_upgraded_date`  | `datetime.datetime \| None`                                       |
| `users`                | `List[edgeimpulse_api.models.organization_user.OrganizationUser]` |
| `whitelabel_id`        | `pydantic.v1.types.StrictInt \| None`                             |
| `whitelabel_name`      | `pydantic.v1.types.StrictStr \| None`                             |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization.Organization.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.organization.Organization
```

Create an instance of Organization from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                            |
| -------------------------------------------------- |
| `edgeimpulse_api.models.organization.Organization` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.organization.Organization.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.organization.Organization
```

Create an instance of Organization from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                            |
| -------------------------------------------------- |
| `edgeimpulse_api.models.organization.Organization` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization.Organization.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.organization.Organization.to_json(
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
edgeimpulse_api.models.organization.Organization.to_str(
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