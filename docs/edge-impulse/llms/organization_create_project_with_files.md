# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/organization_create_project_with_files.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.organization_create_project_with_files

## Classes

### OrganizationCreateProjectWithFiles

```python  theme={"system"}
edgeimpulse_api.models.organization_create_project_with_files.OrganizationCreateProjectWithFiles(
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

| Class variables                   |                                                                                                                                 |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `Config`                          | ` `                                                                                                                             |
| `builtin_transformation_block`    | `Dict[str, Any] \| None`                                                                                                        |
| `category`                        | `pydantic.v1.types.StrictStr`                                                                                                   |
| `created`                         | `datetime.datetime`                                                                                                             |
| `created_by_user`                 | `edgeimpulse_api.models.created_updated_by_user.CreatedUpdatedByUser \| None`                                                   |
| `email_recipient_uids`            | `List[pydantic.v1.types.StrictInt] \| None`                                                                                     |
| `file_count_for_filter`           | `pydantic.v1.types.StrictInt`                                                                                                   |
| `files`                           | `List[edgeimpulse_api.models.organization_create_project_with_files_all_of_files.OrganizationCreateProjectWithFilesAllOfFiles]` |
| `filter_query`                    | `pydantic.v1.types.StrictStr \| None`                                                                                           |
| `id`                              | `pydantic.v1.types.StrictInt`                                                                                                   |
| `in_progress`                     | `pydantic.v1.types.StrictBool`                                                                                                  |
| `label`                           | `pydantic.v1.types.StrictStr \| None`                                                                                           |
| `name`                            | `pydantic.v1.types.StrictStr`                                                                                                   |
| `operates_on`                     | `edgeimpulse_api.models.transformation_job_operates_on_enum.TransformationJobOperatesOnEnum`                                    |
| `organization_id`                 | `pydantic.v1.types.StrictInt`                                                                                                   |
| `output_dataset_bucket_id`        | `pydantic.v1.types.StrictInt \| None`                                                                                           |
| `output_dataset_bucket_path`      | `pydantic.v1.types.StrictStr \| None`                                                                                           |
| `output_dataset_name`             | `pydantic.v1.types.StrictStr \| None`                                                                                           |
| `pipeline_id`                     | `pydantic.v1.types.StrictInt \| None`                                                                                           |
| `pipeline_name`                   | `pydantic.v1.types.StrictStr \| None`                                                                                           |
| `pipeline_run_id`                 | `pydantic.v1.types.StrictInt \| None`                                                                                           |
| `pipeline_step`                   | `pydantic.v1.types.StrictInt \| None`                                                                                           |
| `project_id`                      | `pydantic.v1.types.StrictInt \| None`                                                                                           |
| `project_name`                    | `pydantic.v1.types.StrictStr \| None`                                                                                           |
| `project_owner`                   | `pydantic.v1.types.StrictStr \| None`                                                                                           |
| `status`                          | `edgeimpulse_api.models.transformation_job_status_enum.TransformationJobStatusEnum`                                             |
| `total_download_file_count`       | `pydantic.v1.types.StrictInt`                                                                                                   |
| `total_download_file_size`        | `pydantic.v1.types.StrictInt`                                                                                                   |
| `total_download_file_size_string` | `pydantic.v1.types.StrictStr`                                                                                                   |
| `total_time_spent_seconds`        | `pydantic.v1.types.StrictInt`                                                                                                   |
| `total_time_spent_string`         | `pydantic.v1.types.StrictStr`                                                                                                   |
| `total_upload_file_count`         | `pydantic.v1.types.StrictInt`                                                                                                   |
| `transform_job_status`            | `edgeimpulse_api.models.transformation_job_status_enum.TransformationJobStatusEnum`                                             |
| `transformation_block_id`         | `pydantic.v1.types.StrictInt \| None`                                                                                           |
| `transformation_block_name`       | `pydantic.v1.types.StrictStr \| None`                                                                                           |
| `transformation_parallel`         | `pydantic.v1.types.StrictInt`                                                                                                   |
| `transformation_summary`          | `edgeimpulse_api.models.organization_create_project_transformation_summary.OrganizationCreateProjectTransformationSummary`      |
| `upload_job_files_uploaded`       | `pydantic.v1.types.StrictInt \| None`                                                                                           |
| `upload_job_id`                   | `pydantic.v1.types.StrictInt \| None`                                                                                           |
| `upload_job_status`               | `edgeimpulse_api.models.transformation_job_status_enum.TransformationJobStatusEnum`                                             |
| `upload_type`                     | `pydantic.v1.types.StrictStr`                                                                                                   |

***

**STATIC METHODS**

#### category\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.organization_create_project_with_files.OrganizationCreateProjectWithFiles.category_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization_create_project_with_files.OrganizationCreateProjectWithFiles.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.organization_create_project_with_files.OrganizationCreateProjectWithFiles
```

Create an instance of OrganizationCreateProjectWithFiles from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                            |
| -------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_create_project_with_files.OrganizationCreateProjectWithFiles` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_create_project_with_files.OrganizationCreateProjectWithFiles.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.organization_create_project_with_files.OrganizationCreateProjectWithFiles
```

Create an instance of OrganizationCreateProjectWithFiles from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                            |
| -------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_create_project_with_files.OrganizationCreateProjectWithFiles` |

#### upload\_type\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.organization_create_project_with_files.OrganizationCreateProjectWithFiles.upload_type_validate_enum(
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
edgeimpulse_api.models.organization_create_project_with_files.OrganizationCreateProjectWithFiles.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_create_project_with_files.OrganizationCreateProjectWithFiles.to_json(
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
edgeimpulse_api.models.organization_create_project_with_files.OrganizationCreateProjectWithFiles.to_str(
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