# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/organization_pipeline_step.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.organization_pipeline_step

## Classes

### OrganizationPipelineStep

```python  theme={"system"}
edgeimpulse_api.models.organization_pipeline_step.OrganizationPipelineStep(
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

| Class variables                |                                                                                                                                      |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `Config`                       | ` `                                                                                                                                  |
| `builtin_transformation_block` | `Dict[str, Any] \| None`                                                                                                             |
| `category`                     | `pydantic.v1.types.StrictStr \| None`                                                                                                |
| `extra_cli_arguments`          | `pydantic.v1.types.StrictStr \| None`                                                                                                |
| `filter`                       | `pydantic.v1.types.StrictStr \| None`                                                                                                |
| `label`                        | `pydantic.v1.types.StrictStr \| None`                                                                                                |
| `name`                         | `pydantic.v1.types.StrictStr`                                                                                                        |
| `new_project_name`             | `pydantic.v1.types.StrictStr \| None`                                                                                                |
| `output_dataset_bucket_id`     | `pydantic.v1.types.StrictInt \| None`                                                                                                |
| `output_dataset_bucket_path`   | `pydantic.v1.types.StrictStr \| None`                                                                                                |
| `output_dataset_name`          | `pydantic.v1.types.StrictStr \| None`                                                                                                |
| `output_dataset_path_rule`     | `edgeimpulse_api.models.organization_create_project_output_dataset_path_rule.OrganizationCreateProjectOutputDatasetPathRule \| None` |
| `output_path_in_dataset`       | `pydantic.v1.types.StrictStr \| None`                                                                                                |
| `parameters`                   | `Dict[str, pydantic.v1.types.StrictStr] \| None`                                                                                     |
| `path_filters`                 | `List[edgeimpulse_api.models.organization_create_project_path_filter.OrganizationCreateProjectPathFilter] \| None`                   |
| `project_api_key`              | `pydantic.v1.types.StrictStr \| None`                                                                                                |
| `project_hmac_key`             | `pydantic.v1.types.StrictStr \| None`                                                                                                |
| `project_id`                   | `pydantic.v1.types.StrictInt \| None`                                                                                                |
| `transformation_block_id`      | `pydantic.v1.types.StrictInt \| None`                                                                                                |
| `transformation_parallel`      | `pydantic.v1.types.StrictInt \| None`                                                                                                |
| `upload_type`                  | `pydantic.v1.types.StrictStr \| None`                                                                                                |

***

**STATIC METHODS**

#### category\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.organization_pipeline_step.OrganizationPipelineStep.category_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization_pipeline_step.OrganizationPipelineStep.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.organization_pipeline_step.OrganizationPipelineStep
```

Create an instance of OrganizationPipelineStep from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                      |
| ---------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_pipeline_step.OrganizationPipelineStep` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_pipeline_step.OrganizationPipelineStep.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.organization_pipeline_step.OrganizationPipelineStep
```

Create an instance of OrganizationPipelineStep from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                      |
| ---------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_pipeline_step.OrganizationPipelineStep` |

#### upload\_type\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.organization_pipeline_step.OrganizationPipelineStep.upload_type_validate_enum(
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
edgeimpulse_api.models.organization_pipeline_step.OrganizationPipelineStep.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_pipeline_step.OrganizationPipelineStep.to_json(
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
edgeimpulse_api.models.organization_pipeline_step.OrganizationPipelineStep.to_str(
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