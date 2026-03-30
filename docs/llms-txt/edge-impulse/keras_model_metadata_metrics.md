# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/keras_model_metadata_metrics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.keras_model_metadata_metrics

## Classes

### KerasModelMetadataMetrics

```python  theme={"system"}
edgeimpulse_api.models.keras_model_metadata_metrics.KerasModelMetadataMetrics(
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

| Class variables         |                                                                                                                                           |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `Config`                | ` `                                                                                                                                       |
| `accuracy`              | `float \| None`                                                                                                                           |
| `additional_metrics`    | `List[edgeimpulse_api.models.additional_metric.AdditionalMetric]`                                                                         |
| `confusion_matrix`      | `List[List[float]]`                                                                                                                       |
| `is_supported_on_mcu`   | `pydantic.v1.types.StrictBool`                                                                                                            |
| `loss`                  | `float`                                                                                                                                   |
| `mcu_support_error`     | `pydantic.v1.types.StrictStr \| None`                                                                                                     |
| `on_device_performance` | `List[edgeimpulse_api.models.keras_model_metadata_metrics_on_device_performance_inner.KerasModelMetadataMetricsOnDevicePerformanceInner]` |
| `predictions`           | `List[edgeimpulse_api.models.model_prediction.ModelPrediction] \| None`                                                                   |
| `profiling_job_failed`  | `pydantic.v1.types.StrictBool \| None`                                                                                                    |
| `profiling_job_id`      | `pydantic.v1.types.StrictInt \| None`                                                                                                     |
| `report`                | `Dict[str, Any]`                                                                                                                          |
| `type`                  | `edgeimpulse_api.models.keras_model_type_enum.KerasModelTypeEnum`                                                                         |
| `visualization`         | `pydantic.v1.types.StrictStr`                                                                                                             |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.keras_model_metadata_metrics.KerasModelMetadataMetrics.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.keras_model_metadata_metrics.KerasModelMetadataMetrics
```

Create an instance of KerasModelMetadataMetrics from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                         |
| ------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.keras_model_metadata_metrics.KerasModelMetadataMetrics` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.keras_model_metadata_metrics.KerasModelMetadataMetrics.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.keras_model_metadata_metrics.KerasModelMetadataMetrics
```

Create an instance of KerasModelMetadataMetrics from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                         |
| ------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.keras_model_metadata_metrics.KerasModelMetadataMetrics` |

#### visualization\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.keras_model_metadata_metrics.KerasModelMetadataMetrics.visualization_validate_enum(
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
edgeimpulse_api.models.keras_model_metadata_metrics.KerasModelMetadataMetrics.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.keras_model_metadata_metrics.KerasModelMetadataMetrics.to_json(
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
edgeimpulse_api.models.keras_model_metadata_metrics.KerasModelMetadataMetrics.to_str(
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