# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/impulse_post_processing_block.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.impulse_post_processing_block

## Classes

### ImpulsePostProcessingBlock

```python  theme={"system"}
edgeimpulse_api.models.impulse_post_processing_block.ImpulsePostProcessingBlock(
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

| Class variables          |                                         |
| ------------------------ | --------------------------------------- |
| `Config`                 | ` `                                     |
| `created_at`             | `datetime.datetime \| None`             |
| `created_by`             | `pydantic.v1.types.StrictStr \| None`   |
| `id`                     | `pydantic.v1.types.ConstrainedIntValue` |
| `implementation_version` | `pydantic.v1.types.StrictInt`           |
| `name`                   | `pydantic.v1.types.StrictStr`           |
| `title`                  | `pydantic.v1.types.StrictStr`           |
| `type`                   | `pydantic.v1.types.StrictStr`           |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.impulse_post_processing_block.ImpulsePostProcessingBlock.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.impulse_post_processing_block.ImpulsePostProcessingBlock
```

Create an instance of ImpulsePostProcessingBlock from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                           |
| --------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.impulse_post_processing_block.ImpulsePostProcessingBlock` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.impulse_post_processing_block.ImpulsePostProcessingBlock.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.impulse_post_processing_block.ImpulsePostProcessingBlock
```

Create an instance of ImpulsePostProcessingBlock from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                           |
| --------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.impulse_post_processing_block.ImpulsePostProcessingBlock` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.impulse_post_processing_block.ImpulsePostProcessingBlock.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.impulse_post_processing_block.ImpulsePostProcessingBlock.to_json(
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
edgeimpulse_api.models.impulse_post_processing_block.ImpulsePostProcessingBlock.to_str(
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