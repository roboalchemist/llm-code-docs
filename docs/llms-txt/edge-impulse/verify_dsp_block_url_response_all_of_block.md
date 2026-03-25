# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/verify_dsp_block_url_response_all_of_block.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.verify_dsp_block_url_response_all_of_block

## Classes

### VerifyDspBlockUrlResponseAllOfBlock

```python  theme={"system"}
edgeimpulse_api.models.verify_dsp_block_url_response_all_of_block.VerifyDspBlockUrlResponseAllOfBlock(
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
| `description`                   | `pydantic.v1.types.StrictStr`                                      |
| `latest_implementation_version` | `pydantic.v1.types.StrictInt`                                      |
| `name`                          | `pydantic.v1.types.StrictStr`                                      |
| `named_axes`                    | `List[edgeimpulse_api.models.dsp_named_axis.DSPNamedAxis] \| None` |
| `title`                         | `pydantic.v1.types.StrictStr`                                      |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.verify_dsp_block_url_response_all_of_block.VerifyDspBlockUrlResponseAllOfBlock.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.verify_dsp_block_url_response_all_of_block.VerifyDspBlockUrlResponseAllOfBlock
```

Create an instance of VerifyDspBlockUrlResponseAllOfBlock from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                 |
| ------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.verify_dsp_block_url_response_all_of_block.VerifyDspBlockUrlResponseAllOfBlock` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.verify_dsp_block_url_response_all_of_block.VerifyDspBlockUrlResponseAllOfBlock.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.verify_dsp_block_url_response_all_of_block.VerifyDspBlockUrlResponseAllOfBlock
```

Create an instance of VerifyDspBlockUrlResponseAllOfBlock from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                 |
| ------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.verify_dsp_block_url_response_all_of_block.VerifyDspBlockUrlResponseAllOfBlock` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.verify_dsp_block_url_response_all_of_block.VerifyDspBlockUrlResponseAllOfBlock.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.verify_dsp_block_url_response_all_of_block.VerifyDspBlockUrlResponseAllOfBlock.to_json(
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
edgeimpulse_api.models.verify_dsp_block_url_response_all_of_block.VerifyDspBlockUrlResponseAllOfBlock.to_str(
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