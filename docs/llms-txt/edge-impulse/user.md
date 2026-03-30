# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/user.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.user

## Classes

### User

```python  theme={"system"}
edgeimpulse_api.models.user.User(
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

| Class variables        |                                                              |
| ---------------------- | ------------------------------------------------------------ |
| `Config`               | ` `                                                          |
| `activated`            | `pydantic.v1.types.StrictBool`                               |
| `company_name`         | `pydantic.v1.types.StrictStr \| None`                        |
| `created`              | `datetime.datetime`                                          |
| `email`                | `pydantic.v1.types.StrictStr`                                |
| `has_pending_payments` | `pydantic.v1.types.StrictBool \| None`                       |
| `id`                   | `pydantic.v1.types.StrictInt`                                |
| `idps`                 | `List[pydantic.v1.types.StrictStr] \| None`                  |
| `job_title`            | `pydantic.v1.types.StrictStr \| None`                        |
| `last_seen`            | `datetime.datetime \| None`                                  |
| `mfa_configured`       | `pydantic.v1.types.StrictBool`                               |
| `name`                 | `pydantic.v1.types.StrictStr`                                |
| `pending`              | `pydantic.v1.types.StrictBool`                               |
| `permissions`          | `List[edgeimpulse_api.models.permission.Permission] \| None` |
| `photo`                | `pydantic.v1.types.StrictStr \| None`                        |
| `staff_info`           | `edgeimpulse_api.models.staff_info.StaffInfo`                |
| `stripe_customer_id`   | `pydantic.v1.types.StrictStr \| None`                        |
| `tier`                 | `edgeimpulse_api.models.user_tier_enum.UserTierEnum \| None` |
| `username`             | `pydantic.v1.types.StrictStr`                                |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.user.User.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.user.User
```

Create an instance of User from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                            |
| ---------------------------------- |
| `edgeimpulse_api.models.user.User` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.user.User.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.user.User
```

Create an instance of User from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                            |
| ---------------------------------- |
| `edgeimpulse_api.models.user.User` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.user.User.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.user.User.to_json(
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
edgeimpulse_api.models.user.User.to_str(
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