# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/store_inference_history_request_summaries_inner.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.store_inference_history_request_summaries_inner

## Classes

### StoreInferenceHistoryRequestSummariesInner

```python  theme={"system"}
edgeimpulse_api.models.store_inference_history_request_summaries_inner.StoreInferenceHistoryRequestSummariesInner(
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

| Class variables          |                                                                                |
| ------------------------ | ------------------------------------------------------------------------------ |
| `Config`                 | ` `                                                                            |
| `classification_counter` | `List[edgeimpulse_api.models.inference_history_entry.InferenceHistoryEntry]`   |
| `end`                    | `edgeimpulse_api.models.inference_history_timestamp.InferenceHistoryTimestamp` |
| `mean`                   | `List[edgeimpulse_api.models.inference_history_entry.InferenceHistoryEntry]`   |
| `metrics`                | `Dict[str, Any]`                                                               |
| `standard_deviation`     | `List[edgeimpulse_api.models.inference_history_entry.InferenceHistoryEntry]`   |
| `start`                  | `edgeimpulse_api.models.inference_history_timestamp.InferenceHistoryTimestamp` |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.store_inference_history_request_summaries_inner.StoreInferenceHistoryRequestSummariesInner.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.store_inference_history_request_summaries_inner.StoreInferenceHistoryRequestSummariesInner
```

Create an instance of StoreInferenceHistoryRequestSummariesInner from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.store_inference_history_request_summaries_inner.StoreInferenceHistoryRequestSummariesInner` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.store_inference_history_request_summaries_inner.StoreInferenceHistoryRequestSummariesInner.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.store_inference_history_request_summaries_inner.StoreInferenceHistoryRequestSummariesInner
```

Create an instance of StoreInferenceHistoryRequestSummariesInner from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.store_inference_history_request_summaries_inner.StoreInferenceHistoryRequestSummariesInner` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.store_inference_history_request_summaries_inner.StoreInferenceHistoryRequestSummariesInner.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.store_inference_history_request_summaries_inner.StoreInferenceHistoryRequestSummariesInner.to_json(
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
edgeimpulse_api.models.store_inference_history_request_summaries_inner.StoreInferenceHistoryRequestSummariesInner.to_str(
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