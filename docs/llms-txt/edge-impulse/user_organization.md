# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/user_organization.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.user_organization

## Classes

### UserOrganization

```python  theme={"system"}
edgeimpulse_api.models.user_organization.UserOrganization(
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

| Class variables          |                                                                                                        |
| ------------------------ | ------------------------------------------------------------------------------------------------------ |
| `Config`                 | ` `                                                                                                    |
| `admin_count`            | `pydantic.v1.types.StrictInt`                                                                          |
| `created`                | `datetime.datetime`                                                                                    |
| `entitlement_limits`     | `edgeimpulse_api.models.entitlement_limits.EntitlementLimits`                                          |
| `id`                     | `pydantic.v1.types.StrictInt`                                                                          |
| `is_admin`               | `pydantic.v1.types.StrictBool`                                                                         |
| `is_developer_profile`   | `pydantic.v1.types.StrictBool`                                                                         |
| `last_accessed`          | `datetime.datetime \| None`                                                                            |
| `logo`                   | `pydantic.v1.types.StrictStr \| None`                                                                  |
| `name`                   | `pydantic.v1.types.StrictStr`                                                                          |
| `private_project_count`  | `pydantic.v1.types.StrictInt`                                                                          |
| `public_project_license` | `edgeimpulse_api.models.user_organization_public_project_license.UserOrganizationPublicProjectLicense` |
| `trial_expired_date`     | `datetime.datetime \| None`                                                                            |
| `trial_id`               | `float \| None`                                                                                        |
| `trial_upgraded_date`    | `datetime.datetime \| None`                                                                            |
| `user_count`             | `pydantic.v1.types.StrictInt`                                                                          |
| `whitelabel_id`          | `pydantic.v1.types.StrictInt \| None`                                                                  |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.user_organization.UserOrganization.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.user_organization.UserOrganization
```

Create an instance of UserOrganization from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                     |
| ----------------------------------------------------------- |
| `edgeimpulse_api.models.user_organization.UserOrganization` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.user_organization.UserOrganization.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.user_organization.UserOrganization
```

Create an instance of UserOrganization from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                     |
| ----------------------------------------------------------- |
| `edgeimpulse_api.models.user_organization.UserOrganization` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.user_organization.UserOrganization.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.user_organization.UserOrganization.to_json(
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
edgeimpulse_api.models.user_organization.UserOrganization.to_str(
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