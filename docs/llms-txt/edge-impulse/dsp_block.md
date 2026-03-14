# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/dsp_block.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.dsp_block

## Classes

### DSPBlock

```python  theme={"system"}
edgeimpulse_api.models.dsp_block.DSPBlock(
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

| Class variables                 |                                                                    |
| ------------------------------- | ------------------------------------------------------------------ |
| `Config`                        | ` `                                                                |
| `author`                        | `pydantic.v1.types.StrictStr`                                      |
| `block_type`                    | `edgeimpulse_api.models.block_type.BlockType`                      |
| `description`                   | `pydantic.v1.types.StrictStr`                                      |
| `experimental`                  | `pydantic.v1.types.StrictBool`                                     |
| `latest_implementation_version` | `pydantic.v1.types.StrictInt`                                      |
| `name`                          | `pydantic.v1.types.StrictStr`                                      |
| `named_axes`                    | `List[edgeimpulse_api.models.dsp_named_axis.DSPNamedAxis] \| None` |
| `organization_dsp_id`           | `pydantic.v1.types.StrictInt \| None`                              |
| `organization_id`               | `pydantic.v1.types.StrictInt \| None`                              |
| `recommended`                   | `pydantic.v1.types.StrictBool`                                     |
| `supported_targets`             | `List[pydantic.v1.types.StrictStr] \| None`                        |
| `title`                         | `pydantic.v1.types.StrictStr`                                      |
| `type`                          | `pydantic.v1.types.StrictStr`                                      |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.dsp_block.DSPBlock.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.dsp_block.DSPBlock
```

Create an instance of DSPBlock from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                     |
| ------------------------------------------- |
| `edgeimpulse_api.models.dsp_block.DSPBlock` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.dsp_block.DSPBlock.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.dsp_block.DSPBlock
```

Create an instance of DSPBlock from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                     |
| ------------------------------------------- |
| `edgeimpulse_api.models.dsp_block.DSPBlock` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.dsp_block.DSPBlock.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.dsp_block.DSPBlock.to_json(
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
edgeimpulse_api.models.dsp_block.DSPBlock.to_str(
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