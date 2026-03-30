# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/organization_get_create_projects_response_all_of_jobs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.organization_get_create_projects_response_all_of_jobs

## Classes

### OrganizationGetCreateProjectsResponseAllOfJobs

```python  theme={"system"}
edgeimpulse_api.models.organization_get_create_projects_response_all_of_jobs.OrganizationGetCreateProjectsResponseAllOfJobs(
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

| Class variables                   |                                                                                                      |
| --------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `Config`                          | ` `                                                                                                  |
| `builtin_transformation_block`    | `Dict[str, Any] \| None`                                                                             |
| `created`                         | `datetime.datetime`                                                                                  |
| `created_by_user`                 | `edgeimpulse_api.models.created_updated_by_user.CreatedUpdatedByUser \| None`                        |
| `id`                              | `pydantic.v1.types.StrictInt`                                                                        |
| `name`                            | `pydantic.v1.types.StrictStr`                                                                        |
| `organization_id`                 | `pydantic.v1.types.StrictInt \| None`                                                                |
| `output_dataset_bucket_id`        | `pydantic.v1.types.StrictInt \| None`                                                                |
| `output_dataset_bucket_path`      | `pydantic.v1.types.StrictStr \| None`                                                                |
| `output_dataset_name`             | `pydantic.v1.types.StrictStr \| None`                                                                |
| `project_id`                      | `pydantic.v1.types.StrictInt \| None`                                                                |
| `project_name`                    | `pydantic.v1.types.StrictStr \| None`                                                                |
| `project_owner`                   | `pydantic.v1.types.StrictStr \| None`                                                                |
| `total_download_file_count`       | `pydantic.v1.types.StrictInt`                                                                        |
| `total_download_file_size`        | `pydantic.v1.types.StrictInt`                                                                        |
| `total_download_file_size_string` | `pydantic.v1.types.StrictStr`                                                                        |
| `total_time_spent_seconds`        | `pydantic.v1.types.StrictInt \| None`                                                                |
| `total_time_spent_string`         | `pydantic.v1.types.StrictStr`                                                                        |
| `total_upload_file_count`         | `pydantic.v1.types.StrictInt \| None`                                                                |
| `transform_job_status`            | `edgeimpulse_api.models.transformation_job_status_enum.TransformationJobStatusEnum`                  |
| `transformation_block_id`         | `pydantic.v1.types.StrictInt \| None`                                                                |
| `transformation_block_name`       | `pydantic.v1.types.StrictStr \| None`                                                                |
| `transformation_operates_on`      | `edgeimpulse_api.models.transformation_job_operates_on_enum.TransformationJobOperatesOnEnum \| None` |
| `upload_job_id`                   | `pydantic.v1.types.StrictInt \| None`                                                                |
| `upload_job_status`               | `edgeimpulse_api.models.transformation_job_status_enum.TransformationJobStatusEnum`                  |
| `upload_type`                     | `pydantic.v1.types.StrictStr`                                                                        |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization_get_create_projects_response_all_of_jobs.OrganizationGetCreateProjectsResponseAllOfJobs.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.organization_get_create_projects_response_all_of_jobs.OrganizationGetCreateProjectsResponseAllOfJobs
```

Create an instance of OrganizationGetCreateProjectsResponseAllOfJobs from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_get_create_projects_response_all_of_jobs.OrganizationGetCreateProjectsResponseAllOfJobs` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_get_create_projects_response_all_of_jobs.OrganizationGetCreateProjectsResponseAllOfJobs.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.organization_get_create_projects_response_all_of_jobs.OrganizationGetCreateProjectsResponseAllOfJobs
```

Create an instance of OrganizationGetCreateProjectsResponseAllOfJobs from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_get_create_projects_response_all_of_jobs.OrganizationGetCreateProjectsResponseAllOfJobs` |

#### upload\_type\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.organization_get_create_projects_response_all_of_jobs.OrganizationGetCreateProjectsResponseAllOfJobs.upload_type_validate_enum(
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
edgeimpulse_api.models.organization_get_create_projects_response_all_of_jobs.OrganizationGetCreateProjectsResponseAllOfJobs.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_get_create_projects_response_all_of_jobs.OrganizationGetCreateProjectsResponseAllOfJobs.to_json(
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
edgeimpulse_api.models.organization_get_create_projects_response_all_of_jobs.OrganizationGetCreateProjectsResponseAllOfJobs.to_str(
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