# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/organization_info_response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.organization_info_response

## Classes

### OrganizationInfoResponse

```python  theme={"system"}
edgeimpulse_api.models.organization_info_response.OrganizationInfoResponse(
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

| Class variables          |                                                                                                                                     |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| `Config`                 | ` `                                                                                                                                 |
| `cli_lists`              | `edgeimpulse_api.models.organization_info_response_all_of_cli_lists.OrganizationInfoResponseAllOfCliLists`                          |
| `datasets`               | `List[edgeimpulse_api.models.organization_dataset.OrganizationDataset]`                                                             |
| `default_compute_limits` | `edgeimpulse_api.models.organization_info_response_all_of_default_compute_limits.OrganizationInfoResponseAllOfDefaultComputeLimits` |
| `entitlement_limits`     | `edgeimpulse_api.models.entitlement_limits.EntitlementLimits \| None`                                                               |
| `error`                  | `pydantic.v1.types.StrictStr \| None`                                                                                               |
| `experiments`            | `List[edgeimpulse_api.models.project_info_response_all_of_experiments.ProjectInfoResponseAllOfExperiments]`                         |
| `organization`           | `edgeimpulse_api.models.organization.Organization`                                                                                  |
| `performance`            | `edgeimpulse_api.models.organization_info_response_all_of_performance.OrganizationInfoResponseAllOfPerformance`                     |
| `readme`                 | `edgeimpulse_api.models.project_info_response_all_of_readme.ProjectInfoResponseAllOfReadme \| None`                                 |
| `success`                | `pydantic.v1.types.StrictBool`                                                                                                      |
| `whitelabel_id`          | `pydantic.v1.types.StrictInt \| None`                                                                                               |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization_info_response.OrganizationInfoResponse.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.organization_info_response.OrganizationInfoResponse
```

Create an instance of OrganizationInfoResponse from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                      |
| ---------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_info_response.OrganizationInfoResponse` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_info_response.OrganizationInfoResponse.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.organization_info_response.OrganizationInfoResponse
```

Create an instance of OrganizationInfoResponse from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                      |
| ---------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_info_response.OrganizationInfoResponse` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization_info_response.OrganizationInfoResponse.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_info_response.OrganizationInfoResponse.to_json(
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
edgeimpulse_api.models.organization_info_response.OrganizationInfoResponse.to_str(
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