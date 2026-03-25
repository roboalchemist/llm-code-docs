# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/anomaly_model_metadata_response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.anomaly_model_metadata_response

## Classes

### AnomalyModelMetadataResponse

```python  theme={"system"}
edgeimpulse_api.models.anomaly_model_metadata_response.AnomalyModelMetadataResponse(
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

| Class variables                     |                                                                                                        |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `Config`                            | ` `                                                                                                    |
| `available_model_types`             | `List[edgeimpulse_api.models.keras_model_type_enum.KerasModelTypeEnum] \| None`                        |
| `axes`                              | `List[pydantic.v1.types.StrictInt]`                                                                    |
| `clusters`                          | `List[edgeimpulse_api.models.anomaly_model_metadata_clusters_inner.AnomalyModelMetadataClustersInner]` |
| `created`                           | `datetime.datetime`                                                                                    |
| `default_minimum_confidence_rating` | `float`                                                                                                |
| `error`                             | `pydantic.v1.types.StrictStr \| None`                                                                  |
| `has_trained_model`                 | `pydantic.v1.types.StrictBool \| None`                                                                 |
| `mean`                              | `List[float]`                                                                                          |
| `model_validation_metrics`          | `List[edgeimpulse_api.models.keras_model_metadata_metrics.KerasModelMetadataMetrics] \| None`          |
| `recommended_model_type`            | `edgeimpulse_api.models.keras_model_type_enum.KerasModelTypeEnum \| None`                              |
| `scale`                             | `List[float]`                                                                                          |
| `success`                           | `pydantic.v1.types.StrictBool`                                                                         |
| `thresholds`                        | `List[edgeimpulse_api.models.block_threshold.BlockThreshold]`                                          |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.anomaly_model_metadata_response.AnomalyModelMetadataResponse.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.anomaly_model_metadata_response.AnomalyModelMetadataResponse
```

Create an instance of AnomalyModelMetadataResponse from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                               |
| ------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.anomaly_model_metadata_response.AnomalyModelMetadataResponse` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.anomaly_model_metadata_response.AnomalyModelMetadataResponse.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.anomaly_model_metadata_response.AnomalyModelMetadataResponse
```

Create an instance of AnomalyModelMetadataResponse from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                               |
| ------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.anomaly_model_metadata_response.AnomalyModelMetadataResponse` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.anomaly_model_metadata_response.AnomalyModelMetadataResponse.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.anomaly_model_metadata_response.AnomalyModelMetadataResponse.to_json(
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
edgeimpulse_api.models.anomaly_model_metadata_response.AnomalyModelMetadataResponse.to_str(
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