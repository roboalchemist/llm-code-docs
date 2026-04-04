# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/impulse.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.impulse

## Classes

### Impulse

```python  theme={"system"}
edgeimpulse_api.models.impulse.Impulse(
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

| Class variables          |                                                                                         |
| ------------------------ | --------------------------------------------------------------------------------------- |
| `Config`                 | ` `                                                                                     |
| `dsp_blocks`             | `List[edgeimpulse_api.models.impulse_dsp_block.ImpulseDspBlock]`                        |
| `id`                     | `pydantic.v1.types.StrictInt`                                                           |
| `input_blocks`           | `List[edgeimpulse_api.models.impulse_input_block.ImpulseInputBlock]`                    |
| `learn_blocks`           | `List[edgeimpulse_api.models.impulse_learn_block.ImpulseLearnBlock]`                    |
| `name`                   | `pydantic.v1.types.StrictStr`                                                           |
| `post_processing_blocks` | `List[edgeimpulse_api.models.impulse_post_processing_block.ImpulsePostProcessingBlock]` |
| `type`                   | `edgeimpulse_api.models.impulse_type.ImpulseType`                                       |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.impulse.Impulse.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.impulse.Impulse
```

Create an instance of Impulse from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                  |
| ---------------------------------------- |
| `edgeimpulse_api.models.impulse.Impulse` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.impulse.Impulse.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.impulse.Impulse
```

Create an instance of Impulse from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                  |
| ---------------------------------------- |
| `edgeimpulse_api.models.impulse.Impulse` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.impulse.Impulse.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.impulse.Impulse.to_json(
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
edgeimpulse_api.models.impulse.Impulse.to_str(
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