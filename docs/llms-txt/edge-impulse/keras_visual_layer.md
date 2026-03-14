# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/keras_visual_layer.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.keras_visual_layer

## Classes

### KerasVisualLayer

```python  theme={"system"}
edgeimpulse_api.models.keras_visual_layer.KerasVisualLayer(
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

| Class variables         |                                                                       |
| ----------------------- | --------------------------------------------------------------------- |
| `Config`                | ` `                                                                   |
| `columns`               | `pydantic.v1.types.StrictInt \| None`                                 |
| `dropout_rate`          | `float \| None`                                                       |
| `enabled`               | `pydantic.v1.types.StrictBool \| None`                                |
| `kernel_size`           | `pydantic.v1.types.StrictInt \| None`                                 |
| `neurons`               | `pydantic.v1.types.StrictInt \| None`                                 |
| `organization_model_id` | `pydantic.v1.types.StrictInt \| None`                                 |
| `stack`                 | `pydantic.v1.types.StrictInt \| None`                                 |
| `type`                  | `edgeimpulse_api.models.keras_visual_layer_type.KerasVisualLayerType` |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.keras_visual_layer.KerasVisualLayer.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.keras_visual_layer.KerasVisualLayer
```

Create an instance of KerasVisualLayer from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.keras_visual_layer.KerasVisualLayer` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.keras_visual_layer.KerasVisualLayer.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.keras_visual_layer.KerasVisualLayer
```

Create an instance of KerasVisualLayer from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.keras_visual_layer.KerasVisualLayer` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.keras_visual_layer.KerasVisualLayer.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.keras_visual_layer.KerasVisualLayer.to_json(
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
edgeimpulse_api.models.keras_visual_layer.KerasVisualLayer.to_str(
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