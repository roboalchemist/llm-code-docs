# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/organization_transformation_block.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.organization_transformation_block

## Classes

### OrganizationTransformationBlock

```python  theme={"system"}
edgeimpulse_api.models.organization_transformation_block.OrganizationTransformationBlock(
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

| Class variables                            |                                                                                                                    |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `Config`                                   | ` `                                                                                                                |
| `additional_mount_points`                  | `List[edgeimpulse_api.models.transformation_block_additional_mount_point.TransformationBlockAdditionalMountPoint]` |
| `ai_actions_operates_on`                   | `List[edgeimpulse_api.models.ai_actions_operates_on.AIActionsOperatesOn] \| None`                                  |
| `allow_extra_cli_arguments`                | `pydantic.v1.types.StrictBool`                                                                                     |
| `cli_arguments`                            | `pydantic.v1.types.StrictStr`                                                                                      |
| `created`                                  | `datetime.datetime`                                                                                                |
| `created_by_user`                          | `edgeimpulse_api.models.created_updated_by_user.CreatedUpdatedByUser \| None`                                      |
| `description`                              | `pydantic.v1.types.StrictStr`                                                                                      |
| `docker_container`                         | `pydantic.v1.types.StrictStr`                                                                                      |
| `docker_container_managed_by_edge_impulse` | `pydantic.v1.types.StrictBool`                                                                                     |
| `environment_variables`                    | `List[edgeimpulse_api.models.environment_variable.EnvironmentVariable]`                                            |
| `id`                                       | `pydantic.v1.types.StrictInt`                                                                                      |
| `ind_metadata`                             | `pydantic.v1.types.StrictBool`                                                                                     |
| `is_public`                                | `pydantic.v1.types.StrictBool`                                                                                     |
| `last_updated`                             | `datetime.datetime \| None`                                                                                        |
| `last_updated_by_user`                     | `edgeimpulse_api.models.created_updated_by_user.CreatedUpdatedByUser \| None`                                      |
| `limits_cpu`                               | `float \| None`                                                                                                    |
| `limits_memory`                            | `pydantic.v1.types.StrictInt \| None`                                                                              |
| `max_running_time_str`                     | `pydantic.v1.types.StrictStr \| None`                                                                              |
| `name`                                     | `pydantic.v1.types.StrictStr`                                                                                      |
| `operates_on`                              | `edgeimpulse_api.models.transformation_job_operates_on_enum.TransformationJobOperatesOnEnum`                       |
| `parameters`                               | `List[Dict[str, Any]] \| None`                                                                                     |
| `parameters_ui`                            | `List[edgeimpulse_api.models.dsp_group_item.DSPGroupItem] \| None`                                                 |
| `public_project_tier_availability`         | `edgeimpulse_api.models.public_project_tier_availability.PublicProjectTierAvailability`                            |
| `repository_url`                           | `pydantic.v1.types.StrictStr \| None`                                                                              |
| `requests_cpu`                             | `float \| None`                                                                                                    |
| `requests_memory`                          | `pydantic.v1.types.StrictInt \| None`                                                                              |
| `show_in_ai_actions`                       | `pydantic.v1.types.StrictBool`                                                                                     |
| `show_in_create_transformation_job`        | `pydantic.v1.types.StrictBool`                                                                                     |
| `show_in_data_sources`                     | `pydantic.v1.types.StrictBool`                                                                                     |
| `show_in_synthetic_data`                   | `pydantic.v1.types.StrictBool`                                                                                     |
| `source_code_available`                    | `pydantic.v1.types.StrictBool`                                                                                     |
| `source_code_download_staff_only`          | `pydantic.v1.types.StrictBool`                                                                                     |
| `user_id`                                  | `pydantic.v1.types.StrictInt \| None`                                                                              |
| `user_name`                                | `pydantic.v1.types.StrictStr \| None`                                                                              |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization_transformation_block.OrganizationTransformationBlock.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.organization_transformation_block.OrganizationTransformationBlock
```

Create an instance of OrganizationTransformationBlock from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                    |
| ------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.organization_transformation_block.OrganizationTransformationBlock` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_transformation_block.OrganizationTransformationBlock.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.organization_transformation_block.OrganizationTransformationBlock
```

Create an instance of OrganizationTransformationBlock from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                    |
| ------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.organization_transformation_block.OrganizationTransformationBlock` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization_transformation_block.OrganizationTransformationBlock.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_transformation_block.OrganizationTransformationBlock.to_json(
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
edgeimpulse_api.models.organization_transformation_block.OrganizationTransformationBlock.to_str(
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