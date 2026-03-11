# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/keras_response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.keras_response

## Classes

### KerasResponse

```python  theme={"system"}
edgeimpulse_api.models.keras_response.KerasResponse(
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

| Class variables                       |                                                                                                |
| ------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `Config`                              | ` `                                                                                            |
| `akida_edge_learning_config`          | `edgeimpulse_api.models.akida_edge_learning_config.AkidaEdgeLearningConfig \| None`            |
| `anomaly_capacity`                    | `edgeimpulse_api.models.anomaly_capacity.AnomalyCapacity \| None`                              |
| `augmentation_policy_image`           | `edgeimpulse_api.models.augmentation_policy_image_enum.AugmentationPolicyImageEnum`            |
| `augmentation_policy_spectrogram`     | `edgeimpulse_api.models.augmentation_policy_spectrogram.AugmentationPolicySpectrogram \| None` |
| `auto_class_weights`                  | `pydantic.v1.types.StrictBool \| None`                                                         |
| `batch_size`                          | `pydantic.v1.types.StrictInt \| None`                                                          |
| `block_parameters`                    | `edgeimpulse_api.models.block_parameters.BlockParameters \| None`                              |
| `custom_parameters`                   | `Dict[str, pydantic.v1.types.StrictStr] \| None`                                               |
| `custom_validation_metadata_key`      | `pydantic.v1.types.StrictStr \| None`                                                          |
| `default_batch_size`                  | `pydantic.v1.types.StrictInt`                                                                  |
| `dependencies`                        | `edgeimpulse_api.models.dependency_data.DependencyData`                                        |
| `error`                               | `pydantic.v1.types.StrictStr \| None`                                                          |
| `last_shown_model_variant`            | `edgeimpulse_api.models.keras_model_variant_enum.KerasModelVariantEnum \| None`                |
| `learning_rate`                       | `float`                                                                                        |
| `minimum_confidence_rating`           | `float`                                                                                        |
| `mode`                                | `pydantic.v1.types.StrictStr`                                                                  |
| `name`                                | `pydantic.v1.types.StrictStr`                                                                  |
| `profile_int8`                        | `pydantic.v1.types.StrictBool`                                                                 |
| `script`                              | `pydantic.v1.types.StrictStr`                                                                  |
| `selected_model_type`                 | `edgeimpulse_api.models.keras_model_type_enum.KerasModelTypeEnum`                              |
| `shape`                               | `pydantic.v1.types.StrictStr`                                                                  |
| `show_advanced_training_settings`     | `pydantic.v1.types.StrictBool`                                                                 |
| `show_augmentation_training_settings` | `pydantic.v1.types.StrictBool`                                                                 |
| `skip_embeddings_and_memory`          | `pydantic.v1.types.StrictBool`                                                                 |
| `success`                             | `pydantic.v1.types.StrictBool`                                                                 |
| `thresholds`                          | `List[edgeimpulse_api.models.block_threshold.BlockThreshold]`                                  |
| `train_test_split`                    | `float \| None`                                                                                |
| `trained`                             | `pydantic.v1.types.StrictBool`                                                                 |
| `training_cycles`                     | `pydantic.v1.types.StrictInt`                                                                  |
| `transfer_learning_models`            | `List[edgeimpulse_api.models.transfer_learning_model.TransferLearningModel]`                   |
| `type`                                | `edgeimpulse_api.models.learn_block_type.LearnBlockType \| None`                               |
| `use_learned_optimizer`               | `pydantic.v1.types.StrictBool \| None`                                                         |
| `visual_layers`                       | `List[edgeimpulse_api.models.keras_visual_layer.KerasVisualLayer]`                             |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.keras_response.KerasResponse.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.keras_response.KerasResponse
```

Create an instance of KerasResponse from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                               |
| ----------------------------------------------------- |
| `edgeimpulse_api.models.keras_response.KerasResponse` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.keras_response.KerasResponse.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.keras_response.KerasResponse
```

Create an instance of KerasResponse from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                               |
| ----------------------------------------------------- |
| `edgeimpulse_api.models.keras_response.KerasResponse` |

#### mode\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.keras_response.KerasResponse.mode_validate_enum(
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
edgeimpulse_api.models.keras_response.KerasResponse.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.keras_response.KerasResponse.to_json(
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
edgeimpulse_api.models.keras_response.KerasResponse.to_str(
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