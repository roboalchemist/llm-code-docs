# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/performance_calibration_parameter_set.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.performance_calibration_parameter_set

## Classes

### PerformanceCalibrationParameterSet

```python  theme={"system"}
edgeimpulse_api.models.performance_calibration_parameter_set.PerformanceCalibrationParameterSet(
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

| Class variables   |                                                                                                                                 |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `Config`          | ` `                                                                                                                             |
| `aggregate_stats` | `edgeimpulse_api.models.performance_calibration_parameter_set_aggregate_stats.PerformanceCalibrationParameterSetAggregateStats` |
| `detections`      | `List[edgeimpulse_api.models.performance_calibration_detection.PerformanceCalibrationDetection]`                                |
| `is_best`         | `pydantic.v1.types.StrictBool`                                                                                                  |
| `labels`          | `List[pydantic.v1.types.StrictStr]`                                                                                             |
| `params`          | `edgeimpulse_api.models.performance_calibration_parameters.PerformanceCalibrationParameters`                                    |
| `stats`           | `List[edgeimpulse_api.models.performance_calibration_parameter_set_stats_inner.PerformanceCalibrationParameterSetStatsInner]`   |
| `window_size_ms`  | `float`                                                                                                                         |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.performance_calibration_parameter_set.PerformanceCalibrationParameterSet.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.performance_calibration_parameter_set.PerformanceCalibrationParameterSet
```

Create an instance of PerformanceCalibrationParameterSet from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                           |
| ------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.performance_calibration_parameter_set.PerformanceCalibrationParameterSet` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.performance_calibration_parameter_set.PerformanceCalibrationParameterSet.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.performance_calibration_parameter_set.PerformanceCalibrationParameterSet
```

Create an instance of PerformanceCalibrationParameterSet from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                           |
| ------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.performance_calibration_parameter_set.PerformanceCalibrationParameterSet` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.performance_calibration_parameter_set.PerformanceCalibrationParameterSet.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.performance_calibration_parameter_set.PerformanceCalibrationParameterSet.to_json(
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
edgeimpulse_api.models.performance_calibration_parameter_set.PerformanceCalibrationParameterSet.to_str(
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