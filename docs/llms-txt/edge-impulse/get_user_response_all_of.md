# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/get_user_response_all_of.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.get_user_response_all_of

## Classes

### GetUserResponseAllOf

```python  theme={"system"}
edgeimpulse_api.models.get_user_response_all_of.GetUserResponseAllOf(
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
| `email`                                        | `pydantic.v1.types.StrictStr`                                                                                                           |
| `eulas`                                        | `List[edgeimpulse_api.models.user_eula.UserEula]`                                                                                       |
| `evaluation`                                   | `pydantic.v1.types.StrictBool \| None`                                                                                                  |
| `experiments`                                  | `List[edgeimpulse_api.models.user_experiment.UserExperiment]`                                                                           |
| `has_enterprise_features_access`               | `pydantic.v1.types.StrictBool`                                                                                                          |
| `last_accepted_terms_of_service`               | `edgeimpulse_api.models.get_user_response_all_of_last_accepted_terms_of_service.GetUserResponseAllOfLastAcceptedTermsOfService \| None` |
| `last_accessed_projects`                       | `edgeimpulse_api.models.get_user_response_all_of_last_accessed_projects.GetUserResponseAllOfLastAccessedProjects`                       |
| `notifications`                                | `List[pydantic.v1.types.StrictStr]`                                                                                                     |
| `organizations`                                | `List[edgeimpulse_api.models.user_organization.UserOrganization]`                                                                       |
| `password_configured`                          | `pydantic.v1.types.StrictBool`                                                                                                          |
| `pay_as_you_go_subscription_period_end_date`   | `datetime.datetime \| None`                                                                                                             |
| `pay_as_you_go_subscription_period_start_date` | `datetime.datetime \| None`                                                                                                             |
| `private_personal_projects_used`               | `pydantic.v1.types.StrictInt`                                                                                                           |
| `projects`                                     | `List[edgeimpulse_api.models.project.Project]`                                                                                          |
| `projects_sort_order`                          | `edgeimpulse_api.models.user_projects_sort_order.UserProjectsSortOrder`                                                                 |
| `subscription_cancellation_request_date`       | `datetime.datetime \| None`                                                                                                             |
| `subscription_downgrade_date`                  | `datetime.datetime \| None`                                                                                                             |
| `subscription_termination_date`                | `datetime.datetime \| None`                                                                                                             |
| `suspended`                                    | `pydantic.v1.types.StrictBool`                                                                                                          |
| `suspension_reason`                            | `pydantic.v1.types.StrictStr \| None`                                                                                                   |
| `timezone`                                     | `pydantic.v1.types.StrictStr \| None`                                                                                                   |
| `whitelabels`                                  | `List[edgeimpulse_api.models.get_user_response_all_of_whitelabels.GetUserResponseAllOfWhitelabels] \| None`                             |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_user_response_all_of.GetUserResponseAllOf.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.get_user_response_all_of.GetUserResponseAllOf
```

Create an instance of GetUserResponseAllOf from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_user_response_all_of.GetUserResponseAllOf` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.get_user_response_all_of.GetUserResponseAllOf.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.get_user_response_all_of.GetUserResponseAllOf
```

Create an instance of GetUserResponseAllOf from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_user_response_all_of.GetUserResponseAllOf` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_user_response_all_of.GetUserResponseAllOf.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.get_user_response_all_of.GetUserResponseAllOf.to_json(
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
edgeimpulse_api.models.get_user_response_all_of.GetUserResponseAllOf.to_str(
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