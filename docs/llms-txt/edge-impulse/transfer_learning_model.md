# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/transfer_learning_model.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.transfer_learning_model

## Classes

### TransferLearningModel

```python  theme={"system"}
edgeimpulse_api.models.transfer_learning_model.TransferLearningModel(
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

| Class variables             |                                                                                                                                |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `Config`                    | ` `                                                                                                                            |
| `abbreviated_name`          | `pydantic.v1.types.StrictStr \| None`                                                                                          |
| `author`                    | `pydantic.v1.types.StrictStr`                                                                                                  |
| `block_no_longer_available` | `edgeimpulse_api.models.transfer_learning_model_block_no_longer_available.TransferLearningModelBlockNoLongerAvailable \| None` |
| `block_type`                | `edgeimpulse_api.models.block_type.BlockType`                                                                                  |
| `custom_parameters`         | `List[edgeimpulse_api.models.dsp_group_item.DSPGroupItem] \| None`                                                             |
| `default_dropout`           | `float \| None`                                                                                                                |
| `default_learning_rate`     | `float \| None`                                                                                                                |
| `default_neurons`           | `pydantic.v1.types.StrictInt \| None`                                                                                          |
| `default_training_cycles`   | `float \| None`                                                                                                                |
| `description`               | `pydantic.v1.types.StrictStr`                                                                                                  |
| `display_category`          | `edgeimpulse_api.models.block_display_category.BlockDisplayCategory \| None`                                                   |
| `has_dropout`               | `pydantic.v1.types.StrictBool`                                                                                                 |
| `has_expert_mode`           | `pydantic.v1.types.StrictBool`                                                                                                 |
| `has_image_augmentation`    | `pydantic.v1.types.StrictBool \| None`                                                                                         |
| `has_neurons`               | `pydantic.v1.types.StrictBool`                                                                                                 |
| `implementation_version`    | `pydantic.v1.types.StrictInt \| None`                                                                                          |
| `learn_block_type`          | `edgeimpulse_api.models.learn_block_type.LearnBlockType`                                                                       |
| `name`                      | `pydantic.v1.types.StrictStr`                                                                                                  |
| `organization_model_id`     | `pydantic.v1.types.StrictInt \| None`                                                                                          |
| `repository_url`            | `pydantic.v1.types.StrictStr \| None`                                                                                          |
| `short_name`                | `pydantic.v1.types.StrictStr`                                                                                                  |
| `type`                      | `edgeimpulse_api.models.keras_visual_layer_type.KerasVisualLayerType`                                                          |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.transfer_learning_model.TransferLearningModel.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.transfer_learning_model.TransferLearningModel
```

Create an instance of TransferLearningModel from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.transfer_learning_model.TransferLearningModel` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.transfer_learning_model.TransferLearningModel.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.transfer_learning_model.TransferLearningModel
```

Create an instance of TransferLearningModel from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.transfer_learning_model.TransferLearningModel` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.transfer_learning_model.TransferLearningModel.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.transfer_learning_model.TransferLearningModel.to_json(
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
edgeimpulse_api.models.transfer_learning_model.TransferLearningModel.to_str(
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