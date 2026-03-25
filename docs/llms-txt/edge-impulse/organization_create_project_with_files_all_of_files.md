# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/organization_create_project_with_files_all_of_files.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.organization_create_project_with_files_all_of_files

## Classes

### OrganizationCreateProjectWithFilesAllOfFiles

```python  theme={"system"}
edgeimpulse_api.models.organization_create_project_with_files_all_of_files.OrganizationCreateProjectWithFilesAllOfFiles(
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

| Class variables             |                                                                                     |
| --------------------------- | ----------------------------------------------------------------------------------- |
| `Config`                    | ` `                                                                                 |
| `bucket_path`               | `pydantic.v1.types.StrictStr`                                                       |
| `file_name`                 | `pydantic.v1.types.StrictStr`                                                       |
| `id`                        | `pydantic.v1.types.StrictInt`                                                       |
| `length_string`             | `pydantic.v1.types.StrictStr`                                                       |
| `link_to_data_item`         | `pydantic.v1.types.StrictStr`                                                       |
| `source_dataset_type`       | `edgeimpulse_api.models.organization_dataset_type_enum.OrganizationDatasetTypeEnum` |
| `transformation_job_id`     | `pydantic.v1.types.StrictInt \| None`                                               |
| `transformation_job_status` | `edgeimpulse_api.models.transformation_job_status_enum.TransformationJobStatusEnum` |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization_create_project_with_files_all_of_files.OrganizationCreateProjectWithFilesAllOfFiles.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.organization_create_project_with_files_all_of_files.OrganizationCreateProjectWithFilesAllOfFiles
```

Create an instance of OrganizationCreateProjectWithFilesAllOfFiles from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_create_project_with_files_all_of_files.OrganizationCreateProjectWithFilesAllOfFiles` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_create_project_with_files_all_of_files.OrganizationCreateProjectWithFilesAllOfFiles.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.organization_create_project_with_files_all_of_files.OrganizationCreateProjectWithFilesAllOfFiles
```

Create an instance of OrganizationCreateProjectWithFilesAllOfFiles from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_create_project_with_files_all_of_files.OrganizationCreateProjectWithFilesAllOfFiles` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization_create_project_with_files_all_of_files.OrganizationCreateProjectWithFilesAllOfFiles.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_create_project_with_files_all_of_files.OrganizationCreateProjectWithFilesAllOfFiles.to_json(
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
edgeimpulse_api.models.organization_create_project_with_files_all_of_files.OrganizationCreateProjectWithFilesAllOfFiles.to_str(
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