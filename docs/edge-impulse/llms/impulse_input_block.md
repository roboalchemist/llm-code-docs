# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/impulse_input_block.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.impulse_input_block

## Classes

### ImpulseInputBlock

```python  theme={"system"}
edgeimpulse_api.models.impulse_input_block.ImpulseInputBlock(
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

| Class variables                     |                                                                                                                            |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `Config`                            | ` `                                                                                                                        |
| `classification_window_increase_ms` | `pydantic.v1.types.StrictInt \| None`                                                                                      |
| `created_at`                        | `datetime.datetime \| None`                                                                                                |
| `created_by`                        | `pydantic.v1.types.StrictStr \| None`                                                                                      |
| `crop_anchor`                       | `pydantic.v1.types.StrictStr \| None`                                                                                      |
| `dataset_subset`                    | `edgeimpulse_api.models.impulse_input_block_dataset_subset.ImpulseInputBlockDatasetSubset \| None`                         |
| `frequency_hz`                      | `float \| None`                                                                                                            |
| `id`                                | `pydantic.v1.types.ConstrainedIntValue`                                                                                    |
| `image_height`                      | `pydantic.v1.types.StrictInt \| None`                                                                                      |
| `image_width`                       | `pydantic.v1.types.StrictInt \| None`                                                                                      |
| `labeling_method_multi_label`       | `edgeimpulse_api.models.impulse_input_block_labeling_method_multi_label.ImpulseInputBlockLabelingMethodMultiLabel \| None` |
| `name`                              | `pydantic.v1.types.StrictStr`                                                                                              |
| `pad_zeros`                         | `pydantic.v1.types.StrictBool \| None`                                                                                     |
| `resize_method`                     | `pydantic.v1.types.StrictStr \| None`                                                                                      |
| `resize_mode`                       | `edgeimpulse_api.models.image_input_resize_mode.ImageInputResizeMode \| None`                                              |
| `title`                             | `pydantic.v1.types.StrictStr`                                                                                              |
| `type`                              | `pydantic.v1.types.StrictStr`                                                                                              |
| `window_increase_ms`                | `pydantic.v1.types.StrictInt \| None`                                                                                      |
| `window_size_ms`                    | `pydantic.v1.types.StrictInt \| None`                                                                                      |

***

**STATIC METHODS**

#### crop\_anchor\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.impulse_input_block.ImpulseInputBlock.crop_anchor_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.impulse_input_block.ImpulseInputBlock.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.impulse_input_block.ImpulseInputBlock
```

Create an instance of ImpulseInputBlock from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                        |
| -------------------------------------------------------------- |
| `edgeimpulse_api.models.impulse_input_block.ImpulseInputBlock` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.impulse_input_block.ImpulseInputBlock.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.impulse_input_block.ImpulseInputBlock
```

Create an instance of ImpulseInputBlock from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                        |
| -------------------------------------------------------------- |
| `edgeimpulse_api.models.impulse_input_block.ImpulseInputBlock` |

#### resize\_method\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.impulse_input_block.ImpulseInputBlock.resize_method_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

#### type\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.impulse_input_block.ImpulseInputBlock.type_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.impulse_input_block.ImpulseInputBlock.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.impulse_input_block.ImpulseInputBlock.to_json(
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
edgeimpulse_api.models.impulse_input_block.ImpulseInputBlock.to_str(
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