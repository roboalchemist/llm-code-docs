# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/all_learn_blocks_response_all_of_learn_blocks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.all_learn_blocks_response_all_of_learn_blocks

## Classes

### AllLearnBlocksResponseAllOfLearnBlocks

```python  theme={"system"}
edgeimpulse_api.models.all_learn_blocks_response_all_of_learn_blocks.AllLearnBlocksResponseAllOfLearnBlocks(
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
| `description`                      | `pydantic.v1.types.StrictStr`                                                                   |
| `display_category`                 | `edgeimpulse_api.models.block_display_category.BlockDisplayCategory \| None`                    |
| `experiment`                       | `pydantic.v1.types.StrictStr \| None`                                                           |
| `name`                             | `pydantic.v1.types.StrictStr`                                                                   |
| `organization_model_id`            | `float \| None`                                                                                 |
| `public_project_tier_availability` | `edgeimpulse_api.models.public_project_tier_availability.PublicProjectTierAvailability \| None` |
| `title`                            | `pydantic.v1.types.StrictStr`                                                                   |
| `type`                             | `edgeimpulse_api.models.learn_block_type.LearnBlockType`                                        |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.all_learn_blocks_response_all_of_learn_blocks.AllLearnBlocksResponseAllOfLearnBlocks.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.all_learn_blocks_response_all_of_learn_blocks.AllLearnBlocksResponseAllOfLearnBlocks
```

Create an instance of AllLearnBlocksResponseAllOfLearnBlocks from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                       |
| ------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.all_learn_blocks_response_all_of_learn_blocks.AllLearnBlocksResponseAllOfLearnBlocks` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.all_learn_blocks_response_all_of_learn_blocks.AllLearnBlocksResponseAllOfLearnBlocks.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.all_learn_blocks_response_all_of_learn_blocks.AllLearnBlocksResponseAllOfLearnBlocks
```

Create an instance of AllLearnBlocksResponseAllOfLearnBlocks from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                       |
| ------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.all_learn_blocks_response_all_of_learn_blocks.AllLearnBlocksResponseAllOfLearnBlocks` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.all_learn_blocks_response_all_of_learn_blocks.AllLearnBlocksResponseAllOfLearnBlocks.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.all_learn_blocks_response_all_of_learn_blocks.AllLearnBlocksResponseAllOfLearnBlocks.to_json(
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
edgeimpulse_api.models.all_learn_blocks_response_all_of_learn_blocks.AllLearnBlocksResponseAllOfLearnBlocks.to_str(
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