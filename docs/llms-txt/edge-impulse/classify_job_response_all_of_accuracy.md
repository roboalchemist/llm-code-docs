# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/classify_job_response_all_of_accuracy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.classify_job_response_all_of_accuracy

## Classes

### ClassifyJobResponseAllOfAccuracy

```python  theme={"system"}
edgeimpulse_api.models.classify_job_response_all_of_accuracy.ClassifyJobResponseAllOfAccuracy(
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

| Class variables             |                                                                                                                                      |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `Config`                    | ` `                                                                                                                                  |
| `accuracy_score`            | `float \| None`                                                                                                                      |
| `all_labels`                | `List[pydantic.v1.types.StrictStr]`                                                                                                  |
| `anomaly_accuracy_score`    | `float \| None`                                                                                                                      |
| `balanced_accuracy_score`   | `float \| None`                                                                                                                      |
| `confusion_matrix_values`   | `Dict[str, Dict[str, float]]`                                                                                                        |
| `mse_score`                 | `float \| None`                                                                                                                      |
| `no_anomaly_accuracy_score` | `float \| None`                                                                                                                      |
| `summary_per_class`         | `Dict[str, edgeimpulse_api.models.classify_job_response_all_of_accuracy_total_summary.ClassifyJobResponseAllOfAccuracyTotalSummary]` |
| `total_summary`             | `edgeimpulse_api.models.classify_job_response_all_of_accuracy_total_summary.ClassifyJobResponseAllOfAccuracyTotalSummary`            |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.classify_job_response_all_of_accuracy.ClassifyJobResponseAllOfAccuracy.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.classify_job_response_all_of_accuracy.ClassifyJobResponseAllOfAccuracy
```

Create an instance of ClassifyJobResponseAllOfAccuracy from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                         |
| ----------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.classify_job_response_all_of_accuracy.ClassifyJobResponseAllOfAccuracy` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.classify_job_response_all_of_accuracy.ClassifyJobResponseAllOfAccuracy.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.classify_job_response_all_of_accuracy.ClassifyJobResponseAllOfAccuracy
```

Create an instance of ClassifyJobResponseAllOfAccuracy from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                         |
| ----------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.classify_job_response_all_of_accuracy.ClassifyJobResponseAllOfAccuracy` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.classify_job_response_all_of_accuracy.ClassifyJobResponseAllOfAccuracy.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.classify_job_response_all_of_accuracy.ClassifyJobResponseAllOfAccuracy.to_json(
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
edgeimpulse_api.models.classify_job_response_all_of_accuracy.ClassifyJobResponseAllOfAccuracy.to_str(
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