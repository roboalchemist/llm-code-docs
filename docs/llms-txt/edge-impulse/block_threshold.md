# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/block_threshold.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.block_threshold

## Classes

### BlockThreshold

```python  theme={"system"}
edgeimpulse_api.models.block_threshold.BlockThreshold(
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

| Class variables        |                                                                                                                  |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `Config`               | ` `                                                                                                              |
| `description`          | `pydantic.v1.types.StrictStr`                                                                                    |
| `dropdown_options`     | `List[edgeimpulse_api.models.block_threshold_dropdown_options_inner.BlockThresholdDropdownOptionsInner] \| None` |
| `help_text`            | `pydantic.v1.types.StrictStr`                                                                                    |
| `key`                  | `pydantic.v1.types.StrictStr`                                                                                    |
| `suggested_value`      | `float \| None`                                                                                                  |
| `suggested_value_text` | `pydantic.v1.types.StrictStr \| None`                                                                            |
| `value`                | `edgeimpulse_api.models.block_threshold_value.BlockThresholdValue`                                               |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.block_threshold.BlockThreshold.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.block_threshold.BlockThreshold
```

Create an instance of BlockThreshold from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                 |
| ------------------------------------------------------- |
| `edgeimpulse_api.models.block_threshold.BlockThreshold` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.block_threshold.BlockThreshold.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.block_threshold.BlockThreshold
```

Create an instance of BlockThreshold from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                 |
| ------------------------------------------------------- |
| `edgeimpulse_api.models.block_threshold.BlockThreshold` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.block_threshold.BlockThreshold.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.block_threshold.BlockThreshold.to_json(
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
edgeimpulse_api.models.block_threshold.BlockThreshold.to_str(
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