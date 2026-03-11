# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/tuner_block_variants_value.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.tuner_block_variants_value

## Classes

### TunerBlockVariantsValue

```python  theme={"system"}
edgeimpulse_api.models.tuner_block_variants_value.TunerBlockVariantsValue(
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

| Class variables          |                                                                                                                                                 |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `Config`                 | ` `                                                                                                                                             |
| `key`                    | `pydantic.v1.types.StrictStr \| None`                                                                                                           |
| `object_detection`       | `pydantic.v1.types.StrictBool \| None`                                                                                                          |
| `params`                 | `Dict[str, List[Dict[str, Any]]] \| None`                                                                                                       |
| `project_data_type`      | `pydantic.v1.types.StrictStr \| None`                                                                                                           |
| `regression`             | `pydantic.v1.types.StrictBool \| None`                                                                                                          |
| `search_space_templates` | `List[edgeimpulse_api.models.tuner_block_variants_value_search_space_templates_inner.TunerBlockVariantsValueSearchSpaceTemplatesInner] \| None` |
| `title`                  | `pydantic.v1.types.StrictStr \| None`                                                                                                           |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.tuner_block_variants_value.TunerBlockVariantsValue.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.tuner_block_variants_value.TunerBlockVariantsValue
```

Create an instance of TunerBlockVariantsValue from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                     |
| --------------------------------------------------------------------------- |
| `edgeimpulse_api.models.tuner_block_variants_value.TunerBlockVariantsValue` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.tuner_block_variants_value.TunerBlockVariantsValue.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.tuner_block_variants_value.TunerBlockVariantsValue
```

Create an instance of TunerBlockVariantsValue from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                     |
| --------------------------------------------------------------------------- |
| `edgeimpulse_api.models.tuner_block_variants_value.TunerBlockVariantsValue` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.tuner_block_variants_value.TunerBlockVariantsValue.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.tuner_block_variants_value.TunerBlockVariantsValue.to_json(
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
edgeimpulse_api.models.tuner_block_variants_value.TunerBlockVariantsValue.to_str(
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