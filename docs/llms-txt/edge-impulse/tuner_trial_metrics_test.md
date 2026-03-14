# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/tuner_trial_metrics_test.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.tuner_trial_metrics_test

## Classes

### TunerTrialMetricsTest

```python  theme={"system"}
edgeimpulse_api.models.tuner_trial_metrics_test.TunerTrialMetricsTest(
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

| Class variables |                                                                                         |
| --------------- | --------------------------------------------------------------------------------------- |
| `Config`        | ` `                                                                                     |
| `float32`       | `edgeimpulse_api.models.keras_model_metadata_metrics.KerasModelMetadataMetrics \| None` |
| `int8`          | `edgeimpulse_api.models.keras_model_metadata_metrics.KerasModelMetadataMetrics \| None` |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.tuner_trial_metrics_test.TunerTrialMetricsTest.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.tuner_trial_metrics_test.TunerTrialMetricsTest
```

Create an instance of TunerTrialMetricsTest from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                 |
| ----------------------------------------------------------------------- |
| `edgeimpulse_api.models.tuner_trial_metrics_test.TunerTrialMetricsTest` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.tuner_trial_metrics_test.TunerTrialMetricsTest.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.tuner_trial_metrics_test.TunerTrialMetricsTest
```

Create an instance of TunerTrialMetricsTest from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                 |
| ----------------------------------------------------------------------- |
| `edgeimpulse_api.models.tuner_trial_metrics_test.TunerTrialMetricsTest` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.tuner_trial_metrics_test.TunerTrialMetricsTest.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.tuner_trial_metrics_test.TunerTrialMetricsTest.to_json(
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
edgeimpulse_api.models.tuner_trial_metrics_test.TunerTrialMetricsTest.to_str(
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