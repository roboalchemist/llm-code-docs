# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/get_post_processing_results_for_sample_response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.get_post_processing_results_for_sample_response

## Classes

### GetPostProcessingResultsForSampleResponse

```python  theme={"system"}
edgeimpulse_api.models.get_post_processing_results_for_sample_response.GetPostProcessingResultsForSampleResponse(
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

| Class variables  |                                                                                                                                                                   |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Config`         | ` `                                                                                                                                                               |
| `error`          | `pydantic.v1.types.StrictStr \| None`                                                                                                                             |
| `has_results`    | `pydantic.v1.types.StrictStr`                                                                                                                                     |
| `job_is_running` | `edgeimpulse_api.models.get_post_processing_results_for_sample_response_all_of_job_is_running.GetPostProcessingResultsForSampleResponseAllOfJobIsRunning \| None` |
| `results`        | `edgeimpulse_api.models.get_post_processing_results_for_sample_response_all_of_results.GetPostProcessingResultsForSampleResponseAllOfResults \| None`             |
| `success`        | `pydantic.v1.types.StrictBool`                                                                                                                                    |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_post_processing_results_for_sample_response.GetPostProcessingResultsForSampleResponse.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.get_post_processing_results_for_sample_response.GetPostProcessingResultsForSampleResponse
```

Create an instance of GetPostProcessingResultsForSampleResponse from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.get_post_processing_results_for_sample_response.GetPostProcessingResultsForSampleResponse` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.get_post_processing_results_for_sample_response.GetPostProcessingResultsForSampleResponse.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.get_post_processing_results_for_sample_response.GetPostProcessingResultsForSampleResponse
```

Create an instance of GetPostProcessingResultsForSampleResponse from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.get_post_processing_results_for_sample_response.GetPostProcessingResultsForSampleResponse` |

#### has\_results\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.get_post_processing_results_for_sample_response.GetPostProcessingResultsForSampleResponse.has_results_validate_enum(
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
edgeimpulse_api.models.get_post_processing_results_for_sample_response.GetPostProcessingResultsForSampleResponse.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.get_post_processing_results_for_sample_response.GetPostProcessingResultsForSampleResponse.to_json(
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
edgeimpulse_api.models.get_post_processing_results_for_sample_response.GetPostProcessingResultsForSampleResponse.to_str(
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