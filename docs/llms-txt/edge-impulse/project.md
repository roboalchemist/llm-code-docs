# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/project.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.project

## Classes

### Project

```python  theme={"system"}
edgeimpulse_api.models.project.Project(
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

| Class variables                |                                                                              |
| ------------------------------ | ---------------------------------------------------------------------------- |
| `Config`                       | ` `                                                                          |
| `allows_live_public_access`    | `pydantic.v1.types.StrictBool`                                               |
| `category`                     | `pydantic.v1.types.StrictStr \| None`                                        |
| `collaborators`                | `List[edgeimpulse_api.models.project_collaborator.ProjectCollaborator]`      |
| `created`                      | `datetime.datetime`                                                          |
| `data_explorer_screenshot`     | `pydantic.v1.types.StrictStr \| None`                                        |
| `deleted_date`                 | `datetime.datetime \| None`                                                  |
| `description`                  | `pydantic.v1.types.StrictStr`                                                |
| `developer_profile_user_id`    | `pydantic.v1.types.StrictInt \| None`                                        |
| `full_deletion_date`           | `datetime.datetime \| None`                                                  |
| `has_public_version`           | `pydantic.v1.types.StrictBool`                                               |
| `id`                           | `pydantic.v1.types.StrictInt`                                                |
| `ind_pause_processing_samples` | `pydantic.v1.types.StrictBool`                                               |
| `is_enterprise_project`        | `pydantic.v1.types.StrictBool`                                               |
| `is_public`                    | `pydantic.v1.types.StrictBool`                                               |
| `labeling_method`              | `edgeimpulse_api.models.project_labeling_method.ProjectLabelingMethod`       |
| `last_accessed`                | `datetime.datetime \| None`                                                  |
| `last_modification_details`    | `pydantic.v1.types.StrictStr \| None`                                        |
| `last_modified`                | `datetime.datetime \| None`                                                  |
| `license`                      | `edgeimpulse_api.models.public_project_license.PublicProjectLicense \| None` |
| `logo`                         | `pydantic.v1.types.StrictStr \| None`                                        |
| `metadata`                     | `Dict[str, Any]`                                                             |
| `name`                         | `pydantic.v1.types.StrictStr`                                                |
| `owner`                        | `pydantic.v1.types.StrictStr`                                                |
| `owner_avatar`                 | `pydantic.v1.types.StrictStr \| None`                                        |
| `owner_is_developer_profile`   | `pydantic.v1.types.StrictBool`                                               |
| `owner_organization_id`        | `pydantic.v1.types.StrictInt \| None`                                        |
| `owner_user_id`                | `pydantic.v1.types.StrictInt \| None`                                        |
| `public_project_listed`        | `pydantic.v1.types.StrictBool`                                               |
| `scheduled_full_deletion_date` | `datetime.datetime \| None`                                                  |
| `tags`                         | `List[pydantic.v1.types.StrictStr] \| None`                                  |
| `tier`                         | `edgeimpulse_api.models.project_tier_enum.ProjectTierEnum`                   |
| `whitelabel_id`                | `pydantic.v1.types.StrictInt \| None`                                        |
| `whitelabel_name`              | `pydantic.v1.types.StrictStr \| None`                                        |

***

**STATIC METHODS**

#### category\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.project.Project.category_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.project.Project.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.project.Project
```

Create an instance of Project from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                  |
| ---------------------------------------- |
| `edgeimpulse_api.models.project.Project` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.project.Project.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.project.Project
```

Create an instance of Project from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                  |
| ---------------------------------------- |
| `edgeimpulse_api.models.project.Project` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.project.Project.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.project.Project.to_json(
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
edgeimpulse_api.models.project.Project.to_str(
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