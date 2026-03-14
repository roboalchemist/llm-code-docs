# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/job.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.job

## Classes

### Job

```python  theme={"system"}
edgeimpulse_api.models.job.Job(
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

| Class variables         |                                                                               |
| ----------------------- | ----------------------------------------------------------------------------- |
| `Config`                | ` `                                                                           |
| `additional_info`       | `pydantic.v1.types.StrictStr \| None`                                         |
| `category`              | `pydantic.v1.types.StrictStr`                                                 |
| `category_count`        | `pydantic.v1.types.StrictInt \| None`                                         |
| `category_key`          | `pydantic.v1.types.StrictStr`                                                 |
| `compute_time`          | `float \| None`                                                               |
| `created`               | `datetime.datetime`                                                           |
| `created_by_user`       | `edgeimpulse_api.models.created_updated_by_user.CreatedUpdatedByUser \| None` |
| `finished`              | `datetime.datetime \| None`                                                   |
| `finished_successful`   | `pydantic.v1.types.StrictBool \| None`                                        |
| `id`                    | `pydantic.v1.types.StrictInt`                                                 |
| `job_notification_uids` | `List[pydantic.v1.types.StrictInt]`                                           |
| `key`                   | `pydantic.v1.types.StrictStr`                                                 |
| `metadata`              | `Dict[str, Any] \| None`                                                      |
| `started`               | `datetime.datetime \| None`                                                   |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.job.Job.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.job.Job
```

Create an instance of Job from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                          |
| -------------------------------- |
| `edgeimpulse_api.models.job.Job` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.job.Job.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.job.Job
```

Create an instance of Job from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                          |
| -------------------------------- |
| `edgeimpulse_api.models.job.Job` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.job.Job.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.job.Job.to_json(
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
edgeimpulse_api.models.job.Job.to_str(
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