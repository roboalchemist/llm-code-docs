# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/keras_model_metadata_metrics_on_device_performance_inner.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.keras_model_metadata_metrics_on_device_performance_inner

## Classes

### KerasModelMetadataMetricsOnDevicePerformanceInner

```python  theme={"system"}
edgeimpulse_api.models.keras_model_metadata_metrics_on_device_performance_inner.KerasModelMetadataMetricsOnDevicePerformanceInner(
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

| Class variables     |                                                                                                                                                          |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Config`            | ` `                                                                                                                                                      |
| `custom_metrics`    | `List[edgeimpulse_api.models.keras_custom_metric.KerasCustomMetric] \| None`                                                                             |
| `eon`               | `edgeimpulse_api.models.keras_model_metadata_metrics_on_device_performance_inner_tflite.KerasModelMetadataMetricsOnDevicePerformanceInnerTflite`         |
| `eon_ram_optimized` | `edgeimpulse_api.models.keras_model_metadata_metrics_on_device_performance_inner_tflite.KerasModelMetadataMetricsOnDevicePerformanceInnerTflite \| None` |
| `has_performance`   | `pydantic.v1.types.StrictBool`                                                                                                                           |
| `is_default`        | `pydantic.v1.types.StrictBool`                                                                                                                           |
| `latency`           | `float`                                                                                                                                                  |
| `mcu`               | `pydantic.v1.types.StrictStr`                                                                                                                            |
| `name`              | `pydantic.v1.types.StrictStr`                                                                                                                            |
| `profiling_error`   | `pydantic.v1.types.StrictStr \| None`                                                                                                                    |
| `tflite`            | `edgeimpulse_api.models.keras_model_metadata_metrics_on_device_performance_inner_tflite.KerasModelMetadataMetricsOnDevicePerformanceInnerTflite`         |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.keras_model_metadata_metrics_on_device_performance_inner.KerasModelMetadataMetricsOnDevicePerformanceInner.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.keras_model_metadata_metrics_on_device_performance_inner.KerasModelMetadataMetricsOnDevicePerformanceInner
```

Create an instance of KerasModelMetadataMetricsOnDevicePerformanceInner from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.keras_model_metadata_metrics_on_device_performance_inner.KerasModelMetadataMetricsOnDevicePerformanceInner` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.keras_model_metadata_metrics_on_device_performance_inner.KerasModelMetadataMetricsOnDevicePerformanceInner.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.keras_model_metadata_metrics_on_device_performance_inner.KerasModelMetadataMetricsOnDevicePerformanceInner
```

Create an instance of KerasModelMetadataMetricsOnDevicePerformanceInner from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.keras_model_metadata_metrics_on_device_performance_inner.KerasModelMetadataMetricsOnDevicePerformanceInner` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.keras_model_metadata_metrics_on_device_performance_inner.KerasModelMetadataMetricsOnDevicePerformanceInner.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.keras_model_metadata_metrics_on_device_performance_inner.KerasModelMetadataMetricsOnDevicePerformanceInner.to_json(
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
edgeimpulse_api.models.keras_model_metadata_metrics_on_device_performance_inner.KerasModelMetadataMetricsOnDevicePerformanceInner.to_str(
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