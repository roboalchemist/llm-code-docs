# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/keras_model_metadata_metrics_on_device_performance_inner_tflite.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.keras_model_metadata_metrics_on_device_performance_inner_tflite

## Classes

### KerasModelMetadataMetricsOnDevicePerformanceInnerTflite

```python  theme={"system"}
edgeimpulse_api.models.keras_model_metadata_metrics_on_device_performance_inner_tflite.KerasModelMetadataMetricsOnDevicePerformanceInnerTflite(
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

| Class variables |                               |
| --------------- | ----------------------------- |
| `Config`        | ` `                           |
| `arena_size`    | `pydantic.v1.types.StrictInt` |
| `model_size`    | `pydantic.v1.types.StrictInt` |
| `ram_required`  | `pydantic.v1.types.StrictInt` |
| `rom_required`  | `pydantic.v1.types.StrictInt` |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.keras_model_metadata_metrics_on_device_performance_inner_tflite.KerasModelMetadataMetricsOnDevicePerformanceInnerTflite.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.keras_model_metadata_metrics_on_device_performance_inner_tflite.KerasModelMetadataMetricsOnDevicePerformanceInnerTflite
```

Create an instance of KerasModelMetadataMetricsOnDevicePerformanceInnerTflite from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.keras_model_metadata_metrics_on_device_performance_inner_tflite.KerasModelMetadataMetricsOnDevicePerformanceInnerTflite` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.keras_model_metadata_metrics_on_device_performance_inner_tflite.KerasModelMetadataMetricsOnDevicePerformanceInnerTflite.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.keras_model_metadata_metrics_on_device_performance_inner_tflite.KerasModelMetadataMetricsOnDevicePerformanceInnerTflite
```

Create an instance of KerasModelMetadataMetricsOnDevicePerformanceInnerTflite from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.keras_model_metadata_metrics_on_device_performance_inner_tflite.KerasModelMetadataMetricsOnDevicePerformanceInnerTflite` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.keras_model_metadata_metrics_on_device_performance_inner_tflite.KerasModelMetadataMetricsOnDevicePerformanceInnerTflite.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.keras_model_metadata_metrics_on_device_performance_inner_tflite.KerasModelMetadataMetricsOnDevicePerformanceInnerTflite.to_json(
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
edgeimpulse_api.models.keras_model_metadata_metrics_on_device_performance_inner_tflite.KerasModelMetadataMetricsOnDevicePerformanceInnerTflite.to_str(
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