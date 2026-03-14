# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/job_details.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.job_details

## Classes

### JobDetails

```python  theme={"system"}
edgeimpulse_api.models.job_details.JobDetails(
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
| `children_ids`          | `List[pydantic.v1.types.StrictInt] \| None`                                   |
| `compute_time`          | `float \| None`                                                               |
| `created`               | `datetime.datetime`                                                           |
| `created_by_user`       | `edgeimpulse_api.models.created_updated_by_user.CreatedUpdatedByUser \| None` |
| `finished`              | `datetime.datetime \| None`                                                   |
| `finished_successful`   | `pydantic.v1.types.StrictBool \| None`                                        |
| `id`                    | `pydantic.v1.types.StrictInt`                                                 |
| `job_notification_uids` | `List[pydantic.v1.types.StrictInt]`                                           |
| `key`                   | `pydantic.v1.types.StrictStr`                                                 |
| `metadata`              | `Dict[str, Any] \| None`                                                      |
| `spec`                  | `Dict[str, Any] \| None`                                                      |
| `started`               | `datetime.datetime \| None`                                                   |
| `states`                | `List[edgeimpulse_api.models.job_state.JobState]`                             |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.job_details.JobDetails.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.job_details.JobDetails
```

Create an instance of JobDetails from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                         |
| ----------------------------------------------- |
| `edgeimpulse_api.models.job_details.JobDetails` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.job_details.JobDetails.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.job_details.JobDetails
```

Create an instance of JobDetails from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                         |
| ----------------------------------------------- |
| `edgeimpulse_api.models.job_details.JobDetails` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.job_details.JobDetails.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.job_details.JobDetails.to_json(
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
edgeimpulse_api.models.job_details.JobDetails.to_str(
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