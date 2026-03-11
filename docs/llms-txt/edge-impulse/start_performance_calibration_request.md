# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/start_performance_calibration_request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.start_performance_calibration_request

## Classes

### StartPerformanceCalibrationRequest

```python  theme={"system"}
edgeimpulse_api.models.start_performance_calibration_request.StartPerformanceCalibrationRequest(
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

| Class variables          |                                             |
| ------------------------ | ------------------------------------------- |
| `Config`                 | ` `                                         |
| `background_noise_label` | `pydantic.v1.types.StrictStr`               |
| `other_noise_labels`     | `List[pydantic.v1.types.StrictStr] \| None` |
| `sample_length_minutes`  | `float \| None`                             |
| `upload_key`             | `pydantic.v1.types.StrictStr \| None`       |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.start_performance_calibration_request.StartPerformanceCalibrationRequest.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.start_performance_calibration_request.StartPerformanceCalibrationRequest
```

Create an instance of StartPerformanceCalibrationRequest from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                           |
| ------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.start_performance_calibration_request.StartPerformanceCalibrationRequest` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.start_performance_calibration_request.StartPerformanceCalibrationRequest.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.start_performance_calibration_request.StartPerformanceCalibrationRequest
```

Create an instance of StartPerformanceCalibrationRequest from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                           |
| ------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.start_performance_calibration_request.StartPerformanceCalibrationRequest` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.start_performance_calibration_request.StartPerformanceCalibrationRequest.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.start_performance_calibration_request.StartPerformanceCalibrationRequest.to_json(
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
edgeimpulse_api.models.start_performance_calibration_request.StartPerformanceCalibrationRequest.to_str(
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