# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/organization_pipeline_run_step.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.organization_pipeline_run_step

## Classes

### OrganizationPipelineRunStep

```python  theme={"system"}
edgeimpulse_api.models.organization_pipeline_run_step.OrganizationPipelineRunStep(
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

| Class variables                |                                                                                        |
| ------------------------------ | -------------------------------------------------------------------------------------- |
| `Config`                       | ` `                                                                                    |
| `builtin_transformation_block` | `Dict[str, Any] \| None`                                                               |
| `category`                     | `pydantic.v1.types.StrictStr \| None`                                                  |
| `extra_cli_arguments`          | `pydantic.v1.types.StrictStr \| None`                                                  |
| `filter`                       | `pydantic.v1.types.StrictStr \| None`                                                  |
| `label`                        | `pydantic.v1.types.StrictStr \| None`                                                  |
| `name`                         | `pydantic.v1.types.StrictStr`                                                          |
| `new_project_name`             | `pydantic.v1.types.StrictStr \| None`                                                  |
| `output_dataset_bucket_id`     | `pydantic.v1.types.StrictInt \| None`                                                  |
| `output_dataset_bucket_path`   | `pydantic.v1.types.StrictStr \| None`                                                  |
| `output_dataset_name`          | `pydantic.v1.types.StrictStr \| None`                                                  |
| `parameters`                   | `Dict[str, pydantic.v1.types.StrictStr] \| None`                                       |
| `project_api_key`              | `pydantic.v1.types.StrictStr \| None`                                                  |
| `project_hmac_key`             | `pydantic.v1.types.StrictStr \| None`                                                  |
| `project_id`                   | `pydantic.v1.types.StrictInt \| None`                                                  |
| `transformation_block_id`      | `pydantic.v1.types.StrictInt \| None`                                                  |
| `transformation_job`           | `edgeimpulse_api.models.organization_create_project.OrganizationCreateProject \| None` |
| `upload_type`                  | `pydantic.v1.types.StrictStr \| None`                                                  |

***

**STATIC METHODS**

#### category\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.organization_pipeline_run_step.OrganizationPipelineRunStep.category_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization_pipeline_run_step.OrganizationPipelineRunStep.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.organization_pipeline_run_step.OrganizationPipelineRunStep
```

Create an instance of OrganizationPipelineRunStep from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                             |
| ----------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_pipeline_run_step.OrganizationPipelineRunStep` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_pipeline_run_step.OrganizationPipelineRunStep.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.organization_pipeline_run_step.OrganizationPipelineRunStep
```

Create an instance of OrganizationPipelineRunStep from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                             |
| ----------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_pipeline_run_step.OrganizationPipelineRunStep` |

#### upload\_type\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.organization_pipeline_run_step.OrganizationPipelineRunStep.upload_type_validate_enum(
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
edgeimpulse_api.models.organization_pipeline_run_step.OrganizationPipelineRunStep.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_pipeline_run_step.OrganizationPipelineRunStep.to_json(
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
edgeimpulse_api.models.organization_pipeline_run_step.OrganizationPipelineRunStep.to_str(
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