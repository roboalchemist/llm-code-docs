# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/post_processing_block.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.post_processing_block

## Classes

### PostProcessingBlock

```python  theme={"system"}
edgeimpulse_api.models.post_processing_block.PostProcessingBlock(
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

| Class variables                 |                                                            |
| ------------------------------- | ---------------------------------------------------------- |
| `Config`                        | ` `                                                        |
| `author`                        | `pydantic.v1.types.StrictStr`                              |
| `block_type`                    | `edgeimpulse_api.models.block_type.BlockType`              |
| `default_parameters`            | `List[edgeimpulse_api.models.dsp_group_item.DSPGroupItem]` |
| `description`                   | `pydantic.v1.types.StrictStr`                              |
| `experimental`                  | `pydantic.v1.types.StrictBool`                             |
| `latest_implementation_version` | `pydantic.v1.types.StrictInt`                              |
| `name`                          | `pydantic.v1.types.StrictStr`                              |
| `recommended`                   | `pydantic.v1.types.StrictBool`                             |
| `supported_targets`             | `List[pydantic.v1.types.StrictStr] \| None`                |
| `title`                         | `pydantic.v1.types.StrictStr`                              |
| `type`                          | `pydantic.v1.types.StrictStr`                              |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.post_processing_block.PostProcessingBlock.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.post_processing_block.PostProcessingBlock
```

Create an instance of PostProcessingBlock from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.post_processing_block.PostProcessingBlock` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.post_processing_block.PostProcessingBlock.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.post_processing_block.PostProcessingBlock
```

Create an instance of PostProcessingBlock from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.post_processing_block.PostProcessingBlock` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.post_processing_block.PostProcessingBlock.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.post_processing_block.PostProcessingBlock.to_json(
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
edgeimpulse_api.models.post_processing_block.PostProcessingBlock.to_str(
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