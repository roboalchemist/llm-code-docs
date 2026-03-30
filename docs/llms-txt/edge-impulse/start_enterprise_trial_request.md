# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/start_enterprise_trial_request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.start_enterprise_trial_request

## Classes

### StartEnterpriseTrialRequest

```python  theme={"system"}
edgeimpulse_api.models.start_enterprise_trial_request.StartEnterpriseTrialRequest(
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

| Class variables                    |                                       |
| ---------------------------------- | ------------------------------------- |
| `Config`                           | ` `                                   |
| `company_name`                     | `pydantic.v1.types.StrictStr \| None` |
| `company_size`                     | `pydantic.v1.types.StrictStr \| None` |
| `country`                          | `pydantic.v1.types.StrictStr \| None` |
| `email`                            | `pydantic.v1.types.StrictStr \| None` |
| `expiration_date`                  | `datetime.datetime \| None`           |
| `name`                             | `pydantic.v1.types.StrictStr \| None` |
| `notes`                            | `pydantic.v1.types.StrictStr \| None` |
| `organization_name`                | `pydantic.v1.types.StrictStr \| None` |
| `redirect_url_origin`              | `pydantic.v1.types.StrictStr \| None` |
| `redirect_url_query_params`        | `pydantic.v1.types.StrictStr \| None` |
| `state_or_province`                | `pydantic.v1.types.StrictStr \| None` |
| `use_case`                         | `pydantic.v1.types.StrictStr \| None` |
| `user_has_ml_models_in_production` | `pydantic.v1.types.StrictStr \| None` |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.start_enterprise_trial_request.StartEnterpriseTrialRequest.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.start_enterprise_trial_request.StartEnterpriseTrialRequest
```

Create an instance of StartEnterpriseTrialRequest from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                             |
| ----------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.start_enterprise_trial_request.StartEnterpriseTrialRequest` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.start_enterprise_trial_request.StartEnterpriseTrialRequest.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.start_enterprise_trial_request.StartEnterpriseTrialRequest
```

Create an instance of StartEnterpriseTrialRequest from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                             |
| ----------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.start_enterprise_trial_request.StartEnterpriseTrialRequest` |

#### user\_has\_ml\_models\_in\_production\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.start_enterprise_trial_request.StartEnterpriseTrialRequest.user_has_ml_models_in_production_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.start_enterprise_trial_request.StartEnterpriseTrialRequest.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.start_enterprise_trial_request.StartEnterpriseTrialRequest.to_json(
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
edgeimpulse_api.models.start_enterprise_trial_request.StartEnterpriseTrialRequest.to_str(
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