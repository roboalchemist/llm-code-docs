# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/get_inference_metrics_request_metrics_inner.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.get_inference_metrics_request_metrics_inner

## Classes

### GetInferenceMetricsRequestMetricsInner

```python  theme={"system"}
edgeimpulse_api.models.get_inference_metrics_request_metrics_inner.GetInferenceMetricsRequestMetricsInner(
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

| Class variables |                                                                                                                                        |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `Config`        | ` `                                                                                                                                    |
| `aggregate`     | `edgeimpulse_api.models.get_inference_metrics_request_metrics_inner_aggregate.GetInferenceMetricsRequestMetricsInnerAggregate \| None` |
| `filters`       | `pydantic.v1.types.StrictStr \| None`                                                                                                  |
| `metric_key`    | `pydantic.v1.types.StrictStr`                                                                                                          |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_inference_metrics_request_metrics_inner.GetInferenceMetricsRequestMetricsInner.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.get_inference_metrics_request_metrics_inner.GetInferenceMetricsRequestMetricsInner
```

Create an instance of GetInferenceMetricsRequestMetricsInner from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                     |
| ----------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_inference_metrics_request_metrics_inner.GetInferenceMetricsRequestMetricsInner` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.get_inference_metrics_request_metrics_inner.GetInferenceMetricsRequestMetricsInner.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.get_inference_metrics_request_metrics_inner.GetInferenceMetricsRequestMetricsInner
```

Create an instance of GetInferenceMetricsRequestMetricsInner from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                     |
| ----------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_inference_metrics_request_metrics_inner.GetInferenceMetricsRequestMetricsInner` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_inference_metrics_request_metrics_inner.GetInferenceMetricsRequestMetricsInner.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.get_inference_metrics_request_metrics_inner.GetInferenceMetricsRequestMetricsInner.to_json(
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
edgeimpulse_api.models.get_inference_metrics_request_metrics_inner.GetInferenceMetricsRequestMetricsInner.to_str(
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