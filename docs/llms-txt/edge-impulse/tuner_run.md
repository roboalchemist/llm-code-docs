# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/tuner_run.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.tuner_run

## Classes

### TunerRun

```python  theme={"system"}
edgeimpulse_api.models.tuner_run.TunerRun(
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

| Class variables            |                                                                              |
| -------------------------- | ---------------------------------------------------------------------------- |
| `Config`                   | ` `                                                                          |
| `continuation_job_id`      | `pydantic.v1.types.StrictInt \| None`                                        |
| `created`                  | `datetime.datetime`                                                          |
| `index`                    | `pydantic.v1.types.StrictInt`                                                |
| `job_status`               | `edgeimpulse_api.models.job_status.JobStatus`                                |
| `name`                     | `pydantic.v1.types.StrictStr \| None`                                        |
| `space`                    | `List[edgeimpulse_api.models.tuner_space_impulse.TunerSpaceImpulse] \| None` |
| `tuner_coordinator_job_id` | `pydantic.v1.types.StrictInt`                                                |
| `tuner_job_id`             | `pydantic.v1.types.StrictInt`                                                |
| `visible`                  | `pydantic.v1.types.StrictBool`                                               |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.tuner_run.TunerRun.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.tuner_run.TunerRun
```

Create an instance of TunerRun from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                     |
| ------------------------------------------- |
| `edgeimpulse_api.models.tuner_run.TunerRun` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.tuner_run.TunerRun.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.tuner_run.TunerRun
```

Create an instance of TunerRun from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                     |
| ------------------------------------------- |
| `edgeimpulse_api.models.tuner_run.TunerRun` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.tuner_run.TunerRun.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.tuner_run.TunerRun.to_json(
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
edgeimpulse_api.models.tuner_run.TunerRun.to_str(
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