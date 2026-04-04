# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/update_organization_transformation_block_request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.update_organization_transformation_block_request

## Classes

### UpdateOrganizationTransformationBlockRequest

```python  theme={"system"}
edgeimpulse_api.models.update_organization_transformation_block_request.UpdateOrganizationTransformationBlockRequest(
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

| Class variables                     |                                                                                                                            |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `Config`                            | ` `                                                                                                                        |
| `additional_mount_points`           | `List[edgeimpulse_api.models.transformation_block_additional_mount_point.TransformationBlockAdditionalMountPoint] \| None` |
| `ai_actions_operates_on`            | `List[edgeimpulse_api.models.ai_actions_operates_on.AIActionsOperatesOn] \| None`                                          |
| `allow_extra_cli_arguments`         | `pydantic.v1.types.StrictBool \| None`                                                                                     |
| `cli_arguments`                     | `pydantic.v1.types.StrictStr \| None`                                                                                      |
| `description`                       | `pydantic.v1.types.StrictStr \| None`                                                                                      |
| `docker_container`                  | `pydantic.v1.types.StrictStr \| None`                                                                                      |
| `environment_variables`             | `List[edgeimpulse_api.models.environment_variable.EnvironmentVariable] \| None`                                            |
| `ind_metadata`                      | `pydantic.v1.types.StrictBool \| None`                                                                                     |
| `is_public`                         | `pydantic.v1.types.StrictBool \| None`                                                                                     |
| `limits_cpu`                        | `float \| None`                                                                                                            |
| `limits_memory`                     | `pydantic.v1.types.StrictInt \| None`                                                                                      |
| `max_running_time_str`              | `pydantic.v1.types.StrictStr \| None`                                                                                      |
| `name`                              | `pydantic.v1.types.StrictStr \| None`                                                                                      |
| `operates_on`                       | `edgeimpulse_api.models.transformation_job_operates_on_enum.TransformationJobOperatesOnEnum \| None`                       |
| `parameters`                        | `List[Dict[str, Any]] \| None`                                                                                             |
| `public_project_tier_availability`  | `edgeimpulse_api.models.public_project_tier_availability.PublicProjectTierAvailability \| None`                            |
| `repository_url`                    | `pydantic.v1.types.StrictStr \| None`                                                                                      |
| `requests_cpu`                      | `float \| None`                                                                                                            |
| `requests_memory`                   | `pydantic.v1.types.StrictInt \| None`                                                                                      |
| `show_in_ai_actions`                | `pydantic.v1.types.StrictBool \| None`                                                                                     |
| `show_in_create_transformation_job` | `pydantic.v1.types.StrictBool \| None`                                                                                     |
| `show_in_data_sources`              | `pydantic.v1.types.StrictBool \| None`                                                                                     |
| `show_in_synthetic_data`            | `pydantic.v1.types.StrictBool \| None`                                                                                     |
| `source_code_download_staff_only`   | `pydantic.v1.types.StrictBool \| None`                                                                                     |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.update_organization_transformation_block_request.UpdateOrganizationTransformationBlockRequest.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.update_organization_transformation_block_request.UpdateOrganizationTransformationBlockRequest
```

Create an instance of UpdateOrganizationTransformationBlockRequest from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.update_organization_transformation_block_request.UpdateOrganizationTransformationBlockRequest` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.update_organization_transformation_block_request.UpdateOrganizationTransformationBlockRequest.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.update_organization_transformation_block_request.UpdateOrganizationTransformationBlockRequest
```

Create an instance of UpdateOrganizationTransformationBlockRequest from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.update_organization_transformation_block_request.UpdateOrganizationTransformationBlockRequest` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.update_organization_transformation_block_request.UpdateOrganizationTransformationBlockRequest.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.update_organization_transformation_block_request.UpdateOrganizationTransformationBlockRequest.to_json(
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
edgeimpulse_api.models.update_organization_transformation_block_request.UpdateOrganizationTransformationBlockRequest.to_str(
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