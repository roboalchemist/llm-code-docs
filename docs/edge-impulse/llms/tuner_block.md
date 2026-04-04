# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/tuner_block.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.tuner_block

## Classes

### TunerBlock

```python  theme={"system"}
edgeimpulse_api.models.tuner_block.TunerBlock(
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

| Class variables         |                                                                                                |
| ----------------------- | ---------------------------------------------------------------------------------------------- |
| `Config`                | ` `                                                                                            |
| `author`                | `pydantic.v1.types.StrictStr \| None`                                                          |
| `block_type`            | `edgeimpulse_api.models.block_type.BlockType`                                                  |
| `default_config`        | `Dict[str, Any] \| None`                                                                       |
| `description`           | `pydantic.v1.types.StrictStr \| None`                                                          |
| `name`                  | `pydantic.v1.types.StrictStr \| None`                                                          |
| `organization_model_id` | `float \| None`                                                                                |
| `params`                | `Dict[str, edgeimpulse_api.models.dsp_group_item.DSPGroupItem] \| None`                        |
| `recommended`           | `pydantic.v1.types.StrictBool \| None`                                                         |
| `title`                 | `pydantic.v1.types.StrictStr`                                                                  |
| `type`                  | `pydantic.v1.types.StrictStr`                                                                  |
| `variants`              | `Dict[str, edgeimpulse_api.models.tuner_block_variants_value.TunerBlockVariantsValue] \| None` |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.tuner_block.TunerBlock.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.tuner_block.TunerBlock
```

Create an instance of TunerBlock from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                         |
| ----------------------------------------------- |
| `edgeimpulse_api.models.tuner_block.TunerBlock` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.tuner_block.TunerBlock.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.tuner_block.TunerBlock
```

Create an instance of TunerBlock from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                         |
| ----------------------------------------------- |
| `edgeimpulse_api.models.tuner_block.TunerBlock` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.tuner_block.TunerBlock.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.tuner_block.TunerBlock.to_json(
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
edgeimpulse_api.models.tuner_block.TunerBlock.to_str(
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