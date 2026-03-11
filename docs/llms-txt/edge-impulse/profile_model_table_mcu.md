# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/profile_model_table_mcu.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.profile_model_table_mcu

## Classes

### ProfileModelTableMcu

```python  theme={"system"}
edgeimpulse_api.models.profile_model_table_mcu.ProfileModelTableMcu(
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

| Class variables         |                                                                                            |
| ----------------------- | ------------------------------------------------------------------------------------------ |
| `Config`                | ` `                                                                                        |
| `description`           | `pydantic.v1.types.StrictStr`                                                              |
| `mcu_support_error`     | `pydantic.v1.types.StrictStr \| None`                                                      |
| `memory`                | `edgeimpulse_api.models.profile_model_table_mcu_memory.ProfileModelTableMcuMemory \| None` |
| `supported`             | `pydantic.v1.types.StrictBool`                                                             |
| `time_per_inference_ms` | `pydantic.v1.types.StrictInt \| None`                                                      |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.profile_model_table_mcu.ProfileModelTableMcu.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.profile_model_table_mcu.ProfileModelTableMcu
```

Create an instance of ProfileModelTableMcu from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                               |
| --------------------------------------------------------------------- |
| `edgeimpulse_api.models.profile_model_table_mcu.ProfileModelTableMcu` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.profile_model_table_mcu.ProfileModelTableMcu.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.profile_model_table_mcu.ProfileModelTableMcu
```

Create an instance of ProfileModelTableMcu from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                               |
| --------------------------------------------------------------------- |
| `edgeimpulse_api.models.profile_model_table_mcu.ProfileModelTableMcu` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.profile_model_table_mcu.ProfileModelTableMcu.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.profile_model_table_mcu.ProfileModelTableMcu.to_json(
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
edgeimpulse_api.models.profile_model_table_mcu.ProfileModelTableMcu.to_str(
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