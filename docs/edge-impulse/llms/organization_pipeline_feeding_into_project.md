# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/organization_pipeline_feeding_into_project.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.organization_pipeline_feeding_into_project

## Classes

### OrganizationPipelineFeedingIntoProject

```python  theme={"system"}
edgeimpulse_api.models.organization_pipeline_feeding_into_project.OrganizationPipelineFeedingIntoProject(
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

| Class variables |                               |
| --------------- | ----------------------------- |
| `Config`        | ` `                           |
| `id`            | `pydantic.v1.types.StrictInt` |
| `item_count`    | `pydantic.v1.types.StrictInt` |
| `name`          | `pydantic.v1.types.StrictStr` |
| `project_link`  | `pydantic.v1.types.StrictStr` |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization_pipeline_feeding_into_project.OrganizationPipelineFeedingIntoProject.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.organization_pipeline_feeding_into_project.OrganizationPipelineFeedingIntoProject
```

Create an instance of OrganizationPipelineFeedingIntoProject from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                    |
| ---------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_pipeline_feeding_into_project.OrganizationPipelineFeedingIntoProject` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_pipeline_feeding_into_project.OrganizationPipelineFeedingIntoProject.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.organization_pipeline_feeding_into_project.OrganizationPipelineFeedingIntoProject
```

Create an instance of OrganizationPipelineFeedingIntoProject from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                    |
| ---------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_pipeline_feeding_into_project.OrganizationPipelineFeedingIntoProject` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization_pipeline_feeding_into_project.OrganizationPipelineFeedingIntoProject.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_pipeline_feeding_into_project.OrganizationPipelineFeedingIntoProject.to_json(
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
edgeimpulse_api.models.organization_pipeline_feeding_into_project.OrganizationPipelineFeedingIntoProject.to_str(
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