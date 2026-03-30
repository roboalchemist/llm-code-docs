# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/classify_sample_response_classification.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.classify_sample_response_classification

## Classes

### ClassifySampleResponseClassification

```python  theme={"system"}
edgeimpulse_api.models.classify_sample_response_classification.ClassifySampleResponseClassification(
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

| Class variables               |                                                                                                                                    |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `Config`                      | ` `                                                                                                                                |
| `anomaly_result`              | `List[edgeimpulse_api.models.anomaly_result.AnomalyResult] \| None`                                                                |
| `details`                     | `List[edgeimpulse_api.models.classify_sample_response_classification_details.ClassifySampleResponseClassificationDetails] \| None` |
| `expected_labels`             | `List[edgeimpulse_api.models.structured_label.StructuredLabel]`                                                                    |
| `is_multi_label`              | `pydantic.v1.types.StrictBool \| None`                                                                                             |
| `learn_block`                 | `edgeimpulse_api.models.impulse_learn_block.ImpulseLearnBlock`                                                                     |
| `minimum_confidence_rating`   | `float`                                                                                                                            |
| `object_detection_last_layer` | `edgeimpulse_api.models.object_detection_last_layer.ObjectDetectionLastLayer \| None`                                              |
| `result`                      | `List[Dict[str, float]]`                                                                                                           |
| `structured_result`           | `List[edgeimpulse_api.models.structured_classify_result.StructuredClassifyResult] \| None`                                         |
| `thresholds`                  | `List[edgeimpulse_api.models.block_threshold.BlockThreshold]`                                                                      |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.classify_sample_response_classification.ClassifySampleResponseClassification.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.classify_sample_response_classification.ClassifySampleResponseClassification
```

Create an instance of ClassifySampleResponseClassification from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                               |
| ----------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.classify_sample_response_classification.ClassifySampleResponseClassification` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.classify_sample_response_classification.ClassifySampleResponseClassification.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.classify_sample_response_classification.ClassifySampleResponseClassification
```

Create an instance of ClassifySampleResponseClassification from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                               |
| ----------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.classify_sample_response_classification.ClassifySampleResponseClassification` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.classify_sample_response_classification.ClassifySampleResponseClassification.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.classify_sample_response_classification.ClassifySampleResponseClassification.to_json(
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
edgeimpulse_api.models.classify_sample_response_classification.ClassifySampleResponseClassification.to_str(
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