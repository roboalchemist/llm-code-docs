# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/learn_block.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.learn_block

## Classes

### LearnBlock

```python  theme={"system"}
edgeimpulse_api.models.learn_block.LearnBlock(
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

| Class variables                    |                                                                                                 |
| ---------------------------------- | ----------------------------------------------------------------------------------------------- |
| `Config`                           | ` `                                                                                             |
| `author`                           | `pydantic.v1.types.StrictStr`                                                                   |
| `block_type`                       | `edgeimpulse_api.models.block_type.BlockType`                                                   |
| `description`                      | `pydantic.v1.types.StrictStr`                                                                   |
| `display_category`                 | `edgeimpulse_api.models.block_display_category.BlockDisplayCategory \| None`                    |
| `is_public_enterprise_only`        | `pydantic.v1.types.StrictBool \| None`                                                          |
| `name`                             | `pydantic.v1.types.StrictStr`                                                                   |
| `organization_model_id`            | `pydantic.v1.types.StrictInt \| None`                                                           |
| `public_project_tier_availability` | `edgeimpulse_api.models.public_project_tier_availability.PublicProjectTierAvailability \| None` |
| `recommended`                      | `pydantic.v1.types.StrictBool`                                                                  |
| `supported_targets`                | `List[pydantic.v1.types.StrictStr] \| None`                                                     |
| `title`                            | `pydantic.v1.types.StrictStr`                                                                   |
| `type`                             | `pydantic.v1.types.StrictStr`                                                                   |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.learn_block.LearnBlock.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.learn_block.LearnBlock
```

Create an instance of LearnBlock from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                         |
| ----------------------------------------------- |
| `edgeimpulse_api.models.learn_block.LearnBlock` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.learn_block.LearnBlock.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.learn_block.LearnBlock
```

Create an instance of LearnBlock from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                         |
| ----------------------------------------------- |
| `edgeimpulse_api.models.learn_block.LearnBlock` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.learn_block.LearnBlock.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.learn_block.LearnBlock.to_json(
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
edgeimpulse_api.models.learn_block.LearnBlock.to_str(
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