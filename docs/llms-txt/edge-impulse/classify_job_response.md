# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/classify_job_response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.classify_job_response

## Classes

### ClassifyJobResponse

```python  theme={"system"}
edgeimpulse_api.models.classify_job_response.ClassifyJobResponse(
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

| Class variables                         |                                                                                                                                                     |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Config`                                | ` `                                                                                                                                                 |
| `accuracy`                              | `edgeimpulse_api.models.classify_job_response_all_of_accuracy.ClassifyJobResponseAllOfAccuracy`                                                     |
| `additional_metrics_by_learn_block`     | `List[edgeimpulse_api.models.classify_job_response_all_of_additional_metrics_by_learn_block.ClassifyJobResponseAllOfAdditionalMetricsByLearnBlock]` |
| `available_variants`                    | `List[edgeimpulse_api.models.keras_model_variant_enum.KerasModelVariantEnum]`                                                                       |
| `error`                                 | `pydantic.v1.types.StrictStr \| None`                                                                                                               |
| `no_results_because_thresholds_changed` | `pydantic.v1.types.StrictStr \| None`                                                                                                               |
| `predictions`                           | `List[edgeimpulse_api.models.model_prediction.ModelPrediction]`                                                                                     |
| `result`                                | `List[edgeimpulse_api.models.model_result.ModelResult]`                                                                                             |
| `success`                               | `pydantic.v1.types.StrictBool`                                                                                                                      |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.classify_job_response.ClassifyJobResponse.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.classify_job_response.ClassifyJobResponse
```

Create an instance of ClassifyJobResponse from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.classify_job_response.ClassifyJobResponse` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.classify_job_response.ClassifyJobResponse.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.classify_job_response.ClassifyJobResponse
```

Create an instance of ClassifyJobResponse from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.classify_job_response.ClassifyJobResponse` |

#### no\_results\_because\_thresholds\_changed\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.classify_job_response.ClassifyJobResponse.no_results_because_thresholds_changed_validate_enum(
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
edgeimpulse_api.models.classify_job_response.ClassifyJobResponse.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.classify_job_response.ClassifyJobResponse.to_json(
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
edgeimpulse_api.models.classify_job_response.ClassifyJobResponse.to_str(
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