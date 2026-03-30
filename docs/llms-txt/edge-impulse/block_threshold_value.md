# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/block_threshold_value.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.block_threshold_value

## Classes

### BlockThresholdValue

```python  theme={"system"}
edgeimpulse_api.models.block_threshold_value.BlockThresholdValue(
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

| Class variables            |                                       |
| -------------------------- | ------------------------------------- |
| `Config`                   | ` `                                   |
| `actual_instance`          | `Any`                                 |
| `one_of_schemas`           | `List[str]`                           |
| `oneof_schema_1_validator` | `float \| None`                       |
| `oneof_schema_2_validator` | `pydantic.v1.types.StrictStr \| None` |

***

**STATIC METHODS**

#### actual\_instance\_must\_validate\_oneof

```python  theme={"system"}
edgeimpulse_api.models.block_threshold_value.BlockThresholdValue.actual_instance_must_validate_oneof(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.block_threshold_value.BlockThresholdValue.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.block_threshold_value.BlockThresholdValue
```

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.block_threshold_value.BlockThresholdValue` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.block_threshold_value.BlockThresholdValue.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.block_threshold_value.BlockThresholdValue
```

Returns the object represented by the json string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.block_threshold_value.BlockThresholdValue` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.block_threshold_value.BlockThresholdValue.to_dict(
	self
) ‑> dict
```

Returns the dict representation of the actual instance

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

| Returns |
| ------- |
| `dict`  |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.block_threshold_value.BlockThresholdValue.to_json(
	self,
	indent=None
) ‑> str
```

Returns the JSON representation of the actual instance

| Parameters    |     |
| ------------- | --- |
| `self`        | ` ` |
| `indent=None` | ` ` |

| Returns |
| ------- |
| `str`   |

#### to\_str

```python  theme={"system"}
edgeimpulse_api.models.block_threshold_value.BlockThresholdValue.to_str(
	self
) ‑> str
```

Returns the string representation of the actual instance

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

| Returns |
| ------- |
| `str`   |


Built with [Mintlify](https://mintlify.com).