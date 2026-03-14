# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/organization_user.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.organization_user

## Classes

### OrganizationUser

```python  theme={"system"}
edgeimpulse_api.models.organization_user.OrganizationUser(
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

| Class variables                      |                                                                          |
| ------------------------------------ | ------------------------------------------------------------------------ |
| `Config`                             | ` `                                                                      |
| `activated`                          | `pydantic.v1.types.StrictBool`                                           |
| `added`                              | `datetime.datetime`                                                      |
| `company_name`                       | `pydantic.v1.types.StrictStr \| None`                                    |
| `created`                            | `datetime.datetime`                                                      |
| `datasets`                           | `List[pydantic.v1.types.StrictStr]`                                      |
| `email`                              | `pydantic.v1.types.StrictStr`                                            |
| `has_pending_payments`               | `pydantic.v1.types.StrictBool \| None`                                   |
| `id`                                 | `pydantic.v1.types.StrictInt`                                            |
| `idps`                               | `List[pydantic.v1.types.StrictStr] \| None`                              |
| `job_title`                          | `pydantic.v1.types.StrictStr \| None`                                    |
| `last_access_to_organization`        | `datetime.datetime \| None`                                              |
| `last_organization_project_accessed` | `pydantic.v1.types.StrictInt \| None`                                    |
| `last_seen`                          | `datetime.datetime \| None`                                              |
| `mfa_configured`                     | `pydantic.v1.types.StrictBool`                                           |
| `name`                               | `pydantic.v1.types.StrictStr`                                            |
| `pending`                            | `pydantic.v1.types.StrictBool`                                           |
| `permissions`                        | `List[edgeimpulse_api.models.permission.Permission] \| None`             |
| `photo`                              | `pydantic.v1.types.StrictStr \| None`                                    |
| `project_count`                      | `pydantic.v1.types.StrictInt`                                            |
| `role`                               | `edgeimpulse_api.models.organization_member_role.OrganizationMemberRole` |
| `staff_info`                         | `edgeimpulse_api.models.staff_info.StaffInfo`                            |
| `stripe_customer_id`                 | `pydantic.v1.types.StrictStr \| None`                                    |
| `tier`                               | `edgeimpulse_api.models.user_tier_enum.UserTierEnum \| None`             |
| `username`                           | `pydantic.v1.types.StrictStr`                                            |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization_user.OrganizationUser.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.organization_user.OrganizationUser
```

Create an instance of OrganizationUser from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                     |
| ----------------------------------------------------------- |
| `edgeimpulse_api.models.organization_user.OrganizationUser` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_user.OrganizationUser.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.organization_user.OrganizationUser
```

Create an instance of OrganizationUser from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                     |
| ----------------------------------------------------------- |
| `edgeimpulse_api.models.organization_user.OrganizationUser` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization_user.OrganizationUser.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_user.OrganizationUser.to_json(
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
edgeimpulse_api.models.organization_user.OrganizationUser.to_str(
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