# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/dsp_run_response_with_sample.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.dsp_run_response_with_sample

## Classes

### DspRunResponseWithSample

```python  theme={"system"}
edgeimpulse_api.models.dsp_run_response_with_sample.DspRunResponseWithSample(
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

| Class variables           |                                                                 |
| ------------------------- | --------------------------------------------------------------- |
| `Config`                  | ` `                                                             |
| `can_profile_performance` | `pydantic.v1.types.StrictBool`                                  |
| `error`                   | `pydantic.v1.types.StrictStr \| None`                           |
| `features`                | `List[float]`                                                   |
| `graphs`                  | `List[edgeimpulse_api.models.dsp_run_graph.DspRunGraph]`        |
| `label_at_end_of_window`  | `pydantic.v1.types.StrictStr \| None`                           |
| `label_for_window`        | `pydantic.v1.types.StrictStr \| None`                           |
| `labels`                  | `List[pydantic.v1.types.StrictStr] \| None`                     |
| `performance`             | `edgeimpulse_api.models.dsp_performance.DspPerformance \| None` |
| `sample`                  | `edgeimpulse_api.models.raw_sample_data.RawSampleData`          |
| `state_string`            | `pydantic.v1.types.StrictStr \| None`                           |
| `success`                 | `pydantic.v1.types.StrictBool`                                  |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.dsp_run_response_with_sample.DspRunResponseWithSample.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.dsp_run_response_with_sample.DspRunResponseWithSample
```

Create an instance of DspRunResponseWithSample from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                        |
| ------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.dsp_run_response_with_sample.DspRunResponseWithSample` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.dsp_run_response_with_sample.DspRunResponseWithSample.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.dsp_run_response_with_sample.DspRunResponseWithSample
```

Create an instance of DspRunResponseWithSample from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                        |
| ------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.dsp_run_response_with_sample.DspRunResponseWithSample` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.dsp_run_response_with_sample.DspRunResponseWithSample.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.dsp_run_response_with_sample.DspRunResponseWithSample.to_json(
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
edgeimpulse_api.models.dsp_run_response_with_sample.DspRunResponseWithSample.to_str(
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