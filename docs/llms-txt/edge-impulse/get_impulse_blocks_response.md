# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/get_impulse_blocks_response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.get_impulse_blocks_response

## Classes

### GetImpulseBlocksResponse

```python  theme={"system"}
edgeimpulse_api.models.get_impulse_blocks_response.GetImpulseBlocksResponse(
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

| Class variables          |                                                                          |
| ------------------------ | ------------------------------------------------------------------------ |
| `Config`                 | ` `                                                                      |
| `dsp_blocks`             | `List[edgeimpulse_api.models.dsp_block.DSPBlock]`                        |
| `error`                  | `pydantic.v1.types.StrictStr \| None`                                    |
| `input_blocks`           | `List[edgeimpulse_api.models.input_block.InputBlock]`                    |
| `learn_blocks`           | `List[edgeimpulse_api.models.learn_block.LearnBlock]`                    |
| `post_processing_blocks` | `List[edgeimpulse_api.models.post_processing_block.PostProcessingBlock]` |
| `success`                | `pydantic.v1.types.StrictBool`                                           |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_impulse_blocks_response.GetImpulseBlocksResponse.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.get_impulse_blocks_response.GetImpulseBlocksResponse
```

Create an instance of GetImpulseBlocksResponse from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                       |
| ----------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_impulse_blocks_response.GetImpulseBlocksResponse` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.get_impulse_blocks_response.GetImpulseBlocksResponse.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.get_impulse_blocks_response.GetImpulseBlocksResponse
```

Create an instance of GetImpulseBlocksResponse from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                       |
| ----------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_impulse_blocks_response.GetImpulseBlocksResponse` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_impulse_blocks_response.GetImpulseBlocksResponse.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.get_impulse_blocks_response.GetImpulseBlocksResponse.to_json(
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
edgeimpulse_api.models.get_impulse_blocks_response.GetImpulseBlocksResponse.to_str(
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