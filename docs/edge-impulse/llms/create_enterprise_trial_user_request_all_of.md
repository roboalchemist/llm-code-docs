# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/create_enterprise_trial_user_request_all_of.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.create_enterprise_trial_user_request_all_of

## Classes

### CreateEnterpriseTrialUserRequestAllOf

```python  theme={"system"}
edgeimpulse_api.models.create_enterprise_trial_user_request_all_of.CreateEnterpriseTrialUserRequestAllOf(
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

| Class variables             |                                       |
| --------------------------- | ------------------------------------- |
| `Config`                    | ` `                                   |
| `company_name`              | `pydantic.v1.types.StrictStr \| None` |
| `email`                     | `pydantic.v1.types.StrictStr`         |
| `job_title`                 | `pydantic.v1.types.StrictStr \| None` |
| `name`                      | `pydantic.v1.types.StrictStr`         |
| `password`                  | `pydantic.v1.types.StrictStr \| None` |
| `privacy_policy`            | `pydantic.v1.types.StrictBool`        |
| `redirect_url_origin`       | `pydantic.v1.types.StrictStr \| None` |
| `redirect_url_query_params` | `pydantic.v1.types.StrictStr \| None` |
| `turnstile_response`        | `pydantic.v1.types.StrictStr`         |
| `username`                  | `pydantic.v1.types.StrictStr`         |
| `utm_params`                | `List[Dict[str, Any]] \| None`        |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.create_enterprise_trial_user_request_all_of.CreateEnterpriseTrialUserRequestAllOf.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.create_enterprise_trial_user_request_all_of.CreateEnterpriseTrialUserRequestAllOf
```

Create an instance of CreateEnterpriseTrialUserRequestAllOf from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                    |
| ---------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.create_enterprise_trial_user_request_all_of.CreateEnterpriseTrialUserRequestAllOf` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.create_enterprise_trial_user_request_all_of.CreateEnterpriseTrialUserRequestAllOf.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.create_enterprise_trial_user_request_all_of.CreateEnterpriseTrialUserRequestAllOf
```

Create an instance of CreateEnterpriseTrialUserRequestAllOf from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                    |
| ---------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.create_enterprise_trial_user_request_all_of.CreateEnterpriseTrialUserRequestAllOf` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.create_enterprise_trial_user_request_all_of.CreateEnterpriseTrialUserRequestAllOf.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.create_enterprise_trial_user_request_all_of.CreateEnterpriseTrialUserRequestAllOf.to_json(
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
edgeimpulse_api.models.create_enterprise_trial_user_request_all_of.CreateEnterpriseTrialUserRequestAllOf.to_str(
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