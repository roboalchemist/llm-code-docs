# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/get_inference_history_response_all_of.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.get_inference_history_response_all_of

## Classes

### GetInferenceHistoryResponseAllOf

```python  theme={"system"}
edgeimpulse_api.models.get_inference_history_response_all_of.GetInferenceHistoryResponseAllOf(
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

| Class variables     |                                                                                                                                    |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `Config`            | ` `                                                                                                                                |
| `all_classes`       | `List[pydantic.v1.types.StrictStr]`                                                                                                |
| `all_devices`       | `List[edgeimpulse_api.models.get_inference_history_response_all_of_all_devices.GetInferenceHistoryResponseAllOfAllDevices]`        |
| `all_metrics`       | `List[pydantic.v1.types.StrictStr]`                                                                                                |
| `summary_by_device` | `List[edgeimpulse_api.models.inference_history_aggregate.InferenceHistoryAggregate]`                                               |
| `summary_by_time`   | `List[edgeimpulse_api.models.get_inference_history_response_all_of_summary_by_time.GetInferenceHistoryResponseAllOfSummaryByTime]` |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_inference_history_response_all_of.GetInferenceHistoryResponseAllOf.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.get_inference_history_response_all_of.GetInferenceHistoryResponseAllOf
```

Create an instance of GetInferenceHistoryResponseAllOf from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                         |
| ----------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_inference_history_response_all_of.GetInferenceHistoryResponseAllOf` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.get_inference_history_response_all_of.GetInferenceHistoryResponseAllOf.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.get_inference_history_response_all_of.GetInferenceHistoryResponseAllOf
```

Create an instance of GetInferenceHistoryResponseAllOf from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                         |
| ----------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_inference_history_response_all_of.GetInferenceHistoryResponseAllOf` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_inference_history_response_all_of.GetInferenceHistoryResponseAllOf.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.get_inference_history_response_all_of.GetInferenceHistoryResponseAllOf.to_json(
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
edgeimpulse_api.models.get_inference_history_response_all_of.GetInferenceHistoryResponseAllOf.to_str(
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