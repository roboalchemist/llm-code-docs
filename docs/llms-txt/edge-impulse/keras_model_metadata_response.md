# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/keras_model_metadata_response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.keras_model_metadata_response

## Classes

### KerasModelMetadataResponse

```python  theme={"system"}
edgeimpulse_api.models.keras_model_metadata_response.KerasModelMetadataResponse(
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

| Class variables               |                                                                                           |
| ----------------------------- | ----------------------------------------------------------------------------------------- |
| `Config`                      | ` `                                                                                       |
| `available_model_types`       | `List[edgeimpulse_api.models.keras_model_type_enum.KerasModelTypeEnum]`                   |
| `class_names`                 | `List[pydantic.v1.types.StrictStr]`                                                       |
| `created`                     | `datetime.datetime`                                                                       |
| `error`                       | `pydantic.v1.types.StrictStr \| None`                                                     |
| `has_trained_model`           | `pydantic.v1.types.StrictBool`                                                            |
| `image_input_scaling`         | `edgeimpulse_api.models.image_input_scaling.ImageInputScaling`                            |
| `labels`                      | `List[pydantic.v1.types.StrictStr]`                                                       |
| `layers`                      | `List[edgeimpulse_api.models.keras_model_layer.KerasModelLayer]`                          |
| `mode`                        | `edgeimpulse_api.models.keras_model_mode.KerasModelMode`                                  |
| `model_validation_metrics`    | `List[edgeimpulse_api.models.keras_model_metadata_metrics.KerasModelMetadataMetrics]`     |
| `object_detection_last_layer` | `edgeimpulse_api.models.object_detection_last_layer.ObjectDetectionLastLayer \| None`     |
| `recommended_model_type`      | `edgeimpulse_api.models.keras_model_type_enum.KerasModelTypeEnum`                         |
| `success`                     | `pydantic.v1.types.StrictBool`                                                            |
| `tensorboard_graphs`          | `List[edgeimpulse_api.models.keras_model_metadata_graph.KerasModelMetadataGraph] \| None` |
| `thresholds`                  | `List[edgeimpulse_api.models.block_threshold.BlockThreshold]`                             |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.keras_model_metadata_response.KerasModelMetadataResponse.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.keras_model_metadata_response.KerasModelMetadataResponse
```

Create an instance of KerasModelMetadataResponse from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                           |
| --------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.keras_model_metadata_response.KerasModelMetadataResponse` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.keras_model_metadata_response.KerasModelMetadataResponse.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.keras_model_metadata_response.KerasModelMetadataResponse
```

Create an instance of KerasModelMetadataResponse from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                           |
| --------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.keras_model_metadata_response.KerasModelMetadataResponse` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.keras_model_metadata_response.KerasModelMetadataResponse.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.keras_model_metadata_response.KerasModelMetadataResponse.to_json(
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
edgeimpulse_api.models.keras_model_metadata_response.KerasModelMetadataResponse.to_str(
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