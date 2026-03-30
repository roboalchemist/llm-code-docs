# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/get_user_response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.get_user_response

## Classes

### GetUserResponse

```python  theme={"system"}
edgeimpulse_api.models.get_user_response.GetUserResponse(
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

| Class variables                                |                                                                                                                                         |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `Config`                                       | ` `                                                                                                                                     |
| `activated`                                    | `pydantic.v1.types.StrictBool`                                                                                                          |
| `active_enterprise_trial`                      | `edgeimpulse_api.models.enterprise_trial.EnterpriseTrial \| None`                                                                       |
| `ambassador`                                   | `pydantic.v1.types.StrictBool \| None`                                                                                                  |
| `company_name`                                 | `pydantic.v1.types.StrictStr \| None`                                                                                                   |
| `created`                                      | `datetime.datetime`                                                                                                                     |
| `email`                                        | `pydantic.v1.types.StrictStr`                                                                                                           |
| `error`                                        | `pydantic.v1.types.StrictStr \| None`                                                                                                   |
| `eulas`                                        | `List[edgeimpulse_api.models.user_eula.UserEula]`                                                                                       |
| `evaluation`                                   | `pydantic.v1.types.StrictBool \| None`                                                                                                  |
| `experiments`                                  | `List[edgeimpulse_api.models.user_experiment.UserExperiment]`                                                                           |
| `has_enterprise_features_access`               | `pydantic.v1.types.StrictBool`                                                                                                          |
| `has_pending_payments`                         | `pydantic.v1.types.StrictBool \| None`                                                                                                  |
| `id`                                           | `pydantic.v1.types.StrictInt`                                                                                                           |
| `idps`                                         | `List[pydantic.v1.types.StrictStr] \| None`                                                                                             |
| `job_title`                                    | `pydantic.v1.types.StrictStr \| None`                                                                                                   |
| `last_accepted_terms_of_service`               | `edgeimpulse_api.models.get_user_response_all_of_last_accepted_terms_of_service.GetUserResponseAllOfLastAcceptedTermsOfService \| None` |
| `last_accessed_projects`                       | `edgeimpulse_api.models.get_user_response_all_of_last_accessed_projects.GetUserResponseAllOfLastAccessedProjects`                       |
| `last_seen`                                    | `datetime.datetime \| None`                                                                                                             |
| `mfa_configured`                               | `pydantic.v1.types.StrictBool`                                                                                                          |
| `name`                                         | `pydantic.v1.types.StrictStr`                                                                                                           |
| `notifications`                                | `List[pydantic.v1.types.StrictStr]`                                                                                                     |
| `organizations`                                | `List[edgeimpulse_api.models.user_organization.UserOrganization]`                                                                       |
| `password_configured`                          | `pydantic.v1.types.StrictBool`                                                                                                          |
| `pay_as_you_go_subscription_period_end_date`   | `datetime.datetime \| None`                                                                                                             |
| `pay_as_you_go_subscription_period_start_date` | `datetime.datetime \| None`                                                                                                             |
| `pending`                                      | `pydantic.v1.types.StrictBool`                                                                                                          |
| `permissions`                                  | `List[edgeimpulse_api.models.permission.Permission] \| None`                                                                            |
| `photo`                                        | `pydantic.v1.types.StrictStr \| None`                                                                                                   |
| `private_personal_projects_used`               | `pydantic.v1.types.StrictInt`                                                                                                           |
| `projects`                                     | `List[edgeimpulse_api.models.project.Project]`                                                                                          |
| `projects_sort_order`                          | `edgeimpulse_api.models.user_projects_sort_order.UserProjectsSortOrder`                                                                 |
| `staff_info`                                   | `edgeimpulse_api.models.staff_info.StaffInfo`                                                                                           |
| `stripe_customer_id`                           | `pydantic.v1.types.StrictStr \| None`                                                                                                   |
| `subscription_cancellation_request_date`       | `datetime.datetime \| None`                                                                                                             |
| `subscription_downgrade_date`                  | `datetime.datetime \| None`                                                                                                             |
| `subscription_termination_date`                | `datetime.datetime \| None`                                                                                                             |
| `success`                                      | `pydantic.v1.types.StrictBool`                                                                                                          |
| `suspended`                                    | `pydantic.v1.types.StrictBool`                                                                                                          |
| `suspension_reason`                            | `pydantic.v1.types.StrictStr \| None`                                                                                                   |
| `tier`                                         | `edgeimpulse_api.models.user_tier_enum.UserTierEnum`                                                                                    |
| `timezone`                                     | `pydantic.v1.types.StrictStr \| None`                                                                                                   |
| `username`                                     | `pydantic.v1.types.StrictStr`                                                                                                           |
| `whitelabels`                                  | `List[edgeimpulse_api.models.get_user_response_all_of_whitelabels.GetUserResponseAllOfWhitelabels] \| None`                             |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_user_response.GetUserResponse.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.get_user_response.GetUserResponse
```

Create an instance of GetUserResponse from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                    |
| ---------------------------------------------------------- |
| `edgeimpulse_api.models.get_user_response.GetUserResponse` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.get_user_response.GetUserResponse.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.get_user_response.GetUserResponse
```

Create an instance of GetUserResponse from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                    |
| ---------------------------------------------------------- |
| `edgeimpulse_api.models.get_user_response.GetUserResponse` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_user_response.GetUserResponse.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.get_user_response.GetUserResponse.to_json(
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
edgeimpulse_api.models.get_user_response.GetUserResponse.to_str(
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