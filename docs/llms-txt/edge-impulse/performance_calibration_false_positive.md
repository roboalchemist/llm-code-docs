# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/performance_calibration_false_positive.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.performance_calibration_false_positive

## Classes

### PerformanceCalibrationFalsePositive

```python  theme={"system"}
edgeimpulse_api.models.performance_calibration_false_positive.PerformanceCalibrationFalsePositive(
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

| Class variables      |                                             |
| -------------------- | ------------------------------------------- |
| `Config`             | ` `                                         |
| `detection_time`     | `pydantic.v1.types.StrictInt`               |
| `ground_truth_label` | `pydantic.v1.types.StrictStr \| None`       |
| `ground_truth_start` | `float \| None`                             |
| `sample_ids`         | `List[pydantic.v1.types.StrictInt] \| None` |
| `type`               | `pydantic.v1.types.StrictStr`               |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.performance_calibration_false_positive.PerformanceCalibrationFalsePositive.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.performance_calibration_false_positive.PerformanceCalibrationFalsePositive
```

Create an instance of PerformanceCalibrationFalsePositive from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                             |
| --------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.performance_calibration_false_positive.PerformanceCalibrationFalsePositive` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.performance_calibration_false_positive.PerformanceCalibrationFalsePositive.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.performance_calibration_false_positive.PerformanceCalibrationFalsePositive
```

Create an instance of PerformanceCalibrationFalsePositive from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                             |
| --------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.performance_calibration_false_positive.PerformanceCalibrationFalsePositive` |

#### type\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.performance_calibration_false_positive.PerformanceCalibrationFalsePositive.type_validate_enum(
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
edgeimpulse_api.models.performance_calibration_false_positive.PerformanceCalibrationFalsePositive.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.performance_calibration_false_positive.PerformanceCalibrationFalsePositive.to_json(
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
edgeimpulse_api.models.performance_calibration_false_positive.PerformanceCalibrationFalsePositive.to_str(
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