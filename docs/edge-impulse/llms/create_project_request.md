# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/create_project_request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.create_project_request

## Classes

### CreateProjectRequest

```python  theme={"system"}
edgeimpulse_api.models.create_project_request.CreateProjectRequest(
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

| Class variables               |                                                                       |
| ----------------------------- | --------------------------------------------------------------------- |
| `Config`                      | ` `                                                                   |
| `original_project_version_id` | `pydantic.v1.types.StrictInt \| None`                                 |
| `project_name`                | `pydantic.v1.types.StrictStr`                                         |
| `project_visibility`          | `edgeimpulse_api.models.project_visibility.ProjectVisibility \| None` |
| `show_getting_started_wizard` | `pydantic.v1.types.StrictBool \| None`                                |
| `tutorial_key`                | `edgeimpulse_api.models.tutorial_type.TutorialType \| None`           |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.create_project_request.CreateProjectRequest.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.create_project_request.CreateProjectRequest
```

Create an instance of CreateProjectRequest from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                              |
| -------------------------------------------------------------------- |
| `edgeimpulse_api.models.create_project_request.CreateProjectRequest` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.create_project_request.CreateProjectRequest.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.create_project_request.CreateProjectRequest
```

Create an instance of CreateProjectRequest from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                              |
| -------------------------------------------------------------------- |
| `edgeimpulse_api.models.create_project_request.CreateProjectRequest` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.create_project_request.CreateProjectRequest.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.create_project_request.CreateProjectRequest.to_json(
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
edgeimpulse_api.models.create_project_request.CreateProjectRequest.to_str(
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