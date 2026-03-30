# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/get_post_processing_results_for_sample_response_all_of.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.get_post_processing_results_for_sample_response_all_of

## Classes

### GetPostProcessingResultsForSampleResponseAllOf

```python  theme={"system"}
edgeimpulse_api.models.get_post_processing_results_for_sample_response_all_of.GetPostProcessingResultsForSampleResponseAllOf(
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
| `has_results`    | `pydantic.v1.types.StrictStr`                                                                                                                                     |
| `job_is_running` | `edgeimpulse_api.models.get_post_processing_results_for_sample_response_all_of_job_is_running.GetPostProcessingResultsForSampleResponseAllOfJobIsRunning \| None` |
| `results`        | `edgeimpulse_api.models.get_post_processing_results_for_sample_response_all_of_results.GetPostProcessingResultsForSampleResponseAllOfResults \| None`             |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_post_processing_results_for_sample_response_all_of.GetPostProcessingResultsForSampleResponseAllOf.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.get_post_processing_results_for_sample_response_all_of.GetPostProcessingResultsForSampleResponseAllOf
```

Create an instance of GetPostProcessingResultsForSampleResponseAllOf from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.get_post_processing_results_for_sample_response_all_of.GetPostProcessingResultsForSampleResponseAllOf` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.get_post_processing_results_for_sample_response_all_of.GetPostProcessingResultsForSampleResponseAllOf.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.get_post_processing_results_for_sample_response_all_of.GetPostProcessingResultsForSampleResponseAllOf
```

Create an instance of GetPostProcessingResultsForSampleResponseAllOf from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.get_post_processing_results_for_sample_response_all_of.GetPostProcessingResultsForSampleResponseAllOf` |

#### has\_results\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.get_post_processing_results_for_sample_response_all_of.GetPostProcessingResultsForSampleResponseAllOf.has_results_validate_enum(
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
edgeimpulse_api.models.get_post_processing_results_for_sample_response_all_of.GetPostProcessingResultsForSampleResponseAllOf.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.get_post_processing_results_for_sample_response_all_of.GetPostProcessingResultsForSampleResponseAllOf.to_json(
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
edgeimpulse_api.models.get_post_processing_results_for_sample_response_all_of.GetPostProcessingResultsForSampleResponseAllOf.to_str(
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