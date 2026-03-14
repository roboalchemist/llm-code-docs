# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/daily_metrics_record.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.daily_metrics_record

## Classes

### DailyMetricsRecord

```python  theme={"system"}
edgeimpulse_api.models.daily_metrics_record.DailyMetricsRecord(
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

| Class variables                                   |                                       |
| ------------------------------------------------- | ------------------------------------- |
| `Config`                                          | ` `                                   |
| `compute_time_calculated_since`                   | `datetime.datetime`                   |
| `compute_time_seconds`                            | `pydantic.v1.types.StrictInt`         |
| `cpu_compute_time_seconds`                        | `pydantic.v1.types.StrictInt`         |
| `gpu_compute_time_seconds`                        | `pydantic.v1.types.StrictInt`         |
| `projects_added`                                  | `pydantic.v1.types.StrictInt`         |
| `projects_deleted`                                | `pydantic.v1.types.StrictInt`         |
| `staff_users_added`                               | `pydantic.v1.types.StrictInt \| None` |
| `staff_users_deleted`                             | `pydantic.v1.types.StrictInt \| None` |
| `storage_bytes_added`                             | `pydantic.v1.types.StrictInt`         |
| `storage_bytes_deleted`                           | `pydantic.v1.types.StrictInt`         |
| `total_current_contract_compute_time_seconds`     | `pydantic.v1.types.StrictInt`         |
| `total_current_contract_cpu_compute_time_seconds` | `pydantic.v1.types.StrictInt`         |
| `total_current_contract_gpu_compute_time_seconds` | `pydantic.v1.types.StrictInt`         |
| `total_projects`                                  | `pydantic.v1.types.StrictInt`         |
| `total_staff_users`                               | `pydantic.v1.types.StrictInt`         |
| `total_storage_size_bytes`                        | `pydantic.v1.types.StrictInt`         |
| `total_users`                                     | `pydantic.v1.types.StrictInt`         |
| `users_added`                                     | `pydantic.v1.types.StrictInt`         |
| `users_deleted`                                   | `pydantic.v1.types.StrictInt`         |
| `var_date`                                        | `datetime.datetime`                   |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.daily_metrics_record.DailyMetricsRecord.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.daily_metrics_record.DailyMetricsRecord
```

Create an instance of DailyMetricsRecord from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.daily_metrics_record.DailyMetricsRecord` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.daily_metrics_record.DailyMetricsRecord.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.daily_metrics_record.DailyMetricsRecord
```

Create an instance of DailyMetricsRecord from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.daily_metrics_record.DailyMetricsRecord` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.daily_metrics_record.DailyMetricsRecord.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.daily_metrics_record.DailyMetricsRecord.to_json(
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
edgeimpulse_api.models.daily_metrics_record.DailyMetricsRecord.to_str(
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