# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/performance_calibration_ground_truth.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.performance_calibration_ground_truth

## Classes

### PerformanceCalibrationGroundTruth

```python  theme={"system"}
edgeimpulse_api.models.performance_calibration_ground_truth.PerformanceCalibrationGroundTruth(
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

| Class variables |                                                                                                                                         |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `Config`        | ` `                                                                                                                                     |
| `label_idx`     | `pydantic.v1.types.StrictInt`                                                                                                           |
| `label_string`  | `pydantic.v1.types.StrictStr`                                                                                                           |
| `length`        | `pydantic.v1.types.StrictInt`                                                                                                           |
| `samples`       | `List[edgeimpulse_api.models.performance_calibration_ground_truth_samples_inner.PerformanceCalibrationGroundTruthSamplesInner] \| None` |
| `start`         | `pydantic.v1.types.StrictInt`                                                                                                           |
| `type`          | `pydantic.v1.types.StrictStr`                                                                                                           |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.performance_calibration_ground_truth.PerformanceCalibrationGroundTruth.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.performance_calibration_ground_truth.PerformanceCalibrationGroundTruth
```

Create an instance of PerformanceCalibrationGroundTruth from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                         |
| ----------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.performance_calibration_ground_truth.PerformanceCalibrationGroundTruth` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.performance_calibration_ground_truth.PerformanceCalibrationGroundTruth.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.performance_calibration_ground_truth.PerformanceCalibrationGroundTruth
```

Create an instance of PerformanceCalibrationGroundTruth from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                         |
| ----------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.performance_calibration_ground_truth.PerformanceCalibrationGroundTruth` |

#### type\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.performance_calibration_ground_truth.PerformanceCalibrationGroundTruth.type_validate_enum(
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
edgeimpulse_api.models.performance_calibration_ground_truth.PerformanceCalibrationGroundTruth.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.performance_calibration_ground_truth.PerformanceCalibrationGroundTruth.to_json(
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
edgeimpulse_api.models.performance_calibration_ground_truth.PerformanceCalibrationGroundTruth.to_str(
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