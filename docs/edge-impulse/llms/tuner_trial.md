# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/tuner_trial.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.tuner_trial

## Classes

### TunerTrial

```python  theme={"system"}
edgeimpulse_api.models.tuner_trial.TunerTrial(
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

| Class variables              |                                                                                                       |
| ---------------------------- | ----------------------------------------------------------------------------------------------------- |
| `Config`                     | ` `                                                                                                   |
| `blocks`                     | `List[edgeimpulse_api.models.tuner_trial_blocks_inner.TunerTrialBlocksInner]`                         |
| `created_in_post_processing` | `pydantic.v1.types.StrictBool \| None`                                                                |
| `current_epoch`              | `pydantic.v1.types.StrictInt \| None`                                                                 |
| `device_performance`         | `Dict[str, Any] \| None`                                                                              |
| `dsp_job_id`                 | `edgeimpulse_api.models.tuner_trial_dsp_job_id.TunerTrialDspJobId \| None`                            |
| `experiment`                 | `pydantic.v1.types.StrictStr \| None`                                                                 |
| `id`                         | `pydantic.v1.types.StrictStr`                                                                         |
| `impulse`                    | `edgeimpulse_api.models.tuner_trial_impulse.TunerTrialImpulse`                                        |
| `impulse_added_to_project`   | `edgeimpulse_api.models.tuner_trial_impulse_added_to_project.TunerTrialImpulseAddedToProject \| None` |
| `last_completed_epoch`       | `datetime.datetime \| None`                                                                           |
| `last_completed_training`    | `datetime.datetime \| None`                                                                           |
| `learn_job_id`               | `float \| None`                                                                                       |
| `metrics`                    | `edgeimpulse_api.models.tuner_trial_metrics.TunerTrialMetrics \| None`                                |
| `model`                      | `Dict[str, Any] \| None`                                                                              |
| `name`                       | `pydantic.v1.types.StrictStr`                                                                         |
| `optimization_round`         | `float \| None`                                                                                       |
| `original_trial_id`          | `pydantic.v1.types.StrictStr \| None`                                                                 |
| `progress`                   | `edgeimpulse_api.models.tuner_trial_progress.TunerTrialProgress \| None`                              |
| `retries`                    | `pydantic.v1.types.StrictInt \| None`                                                                 |
| `status`                     | `pydantic.v1.types.StrictStr`                                                                         |
| `worker_id`                  | `pydantic.v1.types.StrictStr \| None`                                                                 |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.tuner_trial.TunerTrial.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.tuner_trial.TunerTrial
```

Create an instance of TunerTrial from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                         |
| ----------------------------------------------- |
| `edgeimpulse_api.models.tuner_trial.TunerTrial` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.tuner_trial.TunerTrial.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.tuner_trial.TunerTrial
```

Create an instance of TunerTrial from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                         |
| ----------------------------------------------- |
| `edgeimpulse_api.models.tuner_trial.TunerTrial` |

#### status\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.tuner_trial.TunerTrial.status_validate_enum(
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
edgeimpulse_api.models.tuner_trial.TunerTrial.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.tuner_trial.TunerTrial.to_json(
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
edgeimpulse_api.models.tuner_trial.TunerTrial.to_str(
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