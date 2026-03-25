# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/public_organization_transformation_block.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.public_organization_transformation_block

## Classes

### PublicOrganizationTransformationBlock

```python  theme={"system"}
edgeimpulse_api.models.public_organization_transformation_block.PublicOrganizationTransformationBlock(
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

| Class variables                     |                                                                                              |
| ----------------------------------- | -------------------------------------------------------------------------------------------- |
| `Config`                            | ` `                                                                                          |
| `ai_actions_operates_on`            | `List[edgeimpulse_api.models.ai_actions_operates_on.AIActionsOperatesOn] \| None`            |
| `allow_extra_cli_arguments`         | `pydantic.v1.types.StrictBool`                                                               |
| `created`                           | `datetime.datetime`                                                                          |
| `description`                       | `pydantic.v1.types.StrictStr`                                                                |
| `id`                                | `pydantic.v1.types.StrictInt`                                                                |
| `last_updated`                      | `datetime.datetime \| None`                                                                  |
| `name`                              | `pydantic.v1.types.StrictStr`                                                                |
| `operates_on`                       | `edgeimpulse_api.models.transformation_job_operates_on_enum.TransformationJobOperatesOnEnum` |
| `owner_organization_id`             | `pydantic.v1.types.StrictInt`                                                                |
| `owner_organization_name`           | `pydantic.v1.types.StrictStr`                                                                |
| `parameters`                        | `List[Dict[str, Any]] \| None`                                                               |
| `parameters_ui`                     | `List[edgeimpulse_api.models.dsp_group_item.DSPGroupItem] \| None`                           |
| `repository_url`                    | `pydantic.v1.types.StrictStr \| None`                                                        |
| `show_in_ai_actions`                | `pydantic.v1.types.StrictBool`                                                               |
| `show_in_create_transformation_job` | `pydantic.v1.types.StrictBool`                                                               |
| `show_in_data_sources`              | `pydantic.v1.types.StrictBool`                                                               |
| `show_in_synthetic_data`            | `pydantic.v1.types.StrictBool`                                                               |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.public_organization_transformation_block.PublicOrganizationTransformationBlock.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.public_organization_transformation_block.PublicOrganizationTransformationBlock
```

Create an instance of PublicOrganizationTransformationBlock from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                 |
| ------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.public_organization_transformation_block.PublicOrganizationTransformationBlock` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.public_organization_transformation_block.PublicOrganizationTransformationBlock.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.public_organization_transformation_block.PublicOrganizationTransformationBlock
```

Create an instance of PublicOrganizationTransformationBlock from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                 |
| ------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.public_organization_transformation_block.PublicOrganizationTransformationBlock` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.public_organization_transformation_block.PublicOrganizationTransformationBlock.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.public_organization_transformation_block.PublicOrganizationTransformationBlock.to_json(
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
edgeimpulse_api.models.public_organization_transformation_block.PublicOrganizationTransformationBlock.to_str(
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