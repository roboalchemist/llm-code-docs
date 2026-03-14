# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/optimize_state_response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.optimize_state_response

## Classes

### OptimizeStateResponse

```python  theme={"system"}
edgeimpulse_api.models.optimize_state_response.OptimizeStateResponse(
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

| Class variables                |                                                                                                         |
| ------------------------------ | ------------------------------------------------------------------------------------------------------- |
| `Config`                       | ` `                                                                                                     |
| `can_extend_search`            | `pydantic.v1.types.StrictBool`                                                                          |
| `config`                       | `edgeimpulse_api.models.optimize_config.OptimizeConfig`                                                 |
| `continuation_job_id`          | `pydantic.v1.types.StrictInt \| None`                                                                   |
| `error`                        | `pydantic.v1.types.StrictStr \| None`                                                                   |
| `is_whitelabel`                | `pydantic.v1.types.StrictBool`                                                                          |
| `job_error`                    | `pydantic.v1.types.StrictStr \| None`                                                                   |
| `next_run_index`               | `pydantic.v1.types.StrictInt`                                                                           |
| `project_data_type`            | `pydantic.v1.types.StrictStr`                                                                           |
| `status`                       | `edgeimpulse_api.models.optimize_state_response_all_of_status.OptimizeStateResponseAllOfStatus`         |
| `success`                      | `pydantic.v1.types.StrictBool`                                                                          |
| `total_training_time_exceeded` | `pydantic.v1.types.StrictBool`                                                                          |
| `trials`                       | `List[edgeimpulse_api.models.tuner_trial.TunerTrial]`                                                   |
| `tuner_coordinator_job_id`     | `pydantic.v1.types.StrictInt \| None`                                                                   |
| `tuner_job_id`                 | `pydantic.v1.types.StrictInt \| None`                                                                   |
| `tuner_job_is_running`         | `pydantic.v1.types.StrictBool`                                                                          |
| `tuning_algorithm`             | `pydantic.v1.types.StrictStr \| None`                                                                   |
| `workers`                      | `List[edgeimpulse_api.models.optimize_state_response_all_of_workers.OptimizeStateResponseAllOfWorkers]` |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.optimize_state_response.OptimizeStateResponse.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.optimize_state_response.OptimizeStateResponse
```

Create an instance of OptimizeStateResponse from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.optimize_state_response.OptimizeStateResponse` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.optimize_state_response.OptimizeStateResponse.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.optimize_state_response.OptimizeStateResponse
```

Create an instance of OptimizeStateResponse from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.optimize_state_response.OptimizeStateResponse` |

#### project\_data\_type\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.optimize_state_response.OptimizeStateResponse.project_data_type_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

#### tuning\_algorithm\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.optimize_state_response.OptimizeStateResponse.tuning_algorithm_validate_enum(
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
edgeimpulse_api.models.optimize_state_response.OptimizeStateResponse.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.optimize_state_response.OptimizeStateResponse.to_json(
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
edgeimpulse_api.models.optimize_state_response.OptimizeStateResponse.to_str(
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