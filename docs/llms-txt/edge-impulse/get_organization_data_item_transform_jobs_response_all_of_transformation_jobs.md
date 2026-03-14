# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/get_organization_data_item_transform_jobs_response_all_of_transformation_jobs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.get_organization_data_item_transform_jobs_response_all_of_transformation_jobs

## Classes

### GetOrganizationDataItemTransformJobsResponseAllOfTransformationJobs

```python  theme={"system"}
edgeimpulse_api.models.get_organization_data_item_transform_jobs_response_all_of_transformation_jobs.GetOrganizationDataItemTransformJobsResponseAllOfTransformationJobs(
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

| Class variables             |                                        |
| --------------------------- | -------------------------------------- |
| `Config`                    | ` `                                    |
| `create_project_id`         | `pydantic.v1.types.StrictInt`          |
| `created`                   | `datetime.datetime`                    |
| `id`                        | `pydantic.v1.types.StrictInt`          |
| `job_finished`              | `datetime.datetime \| None`            |
| `job_finished_successful`   | `pydantic.v1.types.StrictBool \| None` |
| `job_id`                    | `pydantic.v1.types.StrictInt`          |
| `job_started`               | `datetime.datetime \| None`            |
| `pipeline_name`             | `pydantic.v1.types.StrictStr \| None`  |
| `transformation_block_name` | `pydantic.v1.types.StrictStr`          |
| `transformation_job_id`     | `pydantic.v1.types.StrictInt`          |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_organization_data_item_transform_jobs_response_all_of_transformation_jobs.GetOrganizationDataItemTransformJobsResponseAllOfTransformationJobs.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.get_organization_data_item_transform_jobs_response_all_of_transformation_jobs.GetOrganizationDataItemTransformJobsResponseAllOfTransformationJobs
```

Create an instance of GetOrganizationDataItemTransformJobsResponseAllOfTransformationJobs from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_organization_data_item_transform_jobs_response_all_of_transformation_jobs.GetOrganizationDataItemTransformJobsResponseAllOfTransformationJobs` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.get_organization_data_item_transform_jobs_response_all_of_transformation_jobs.GetOrganizationDataItemTransformJobsResponseAllOfTransformationJobs.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.get_organization_data_item_transform_jobs_response_all_of_transformation_jobs.GetOrganizationDataItemTransformJobsResponseAllOfTransformationJobs
```

Create an instance of GetOrganizationDataItemTransformJobsResponseAllOfTransformationJobs from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_organization_data_item_transform_jobs_response_all_of_transformation_jobs.GetOrganizationDataItemTransformJobsResponseAllOfTransformationJobs` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_organization_data_item_transform_jobs_response_all_of_transformation_jobs.GetOrganizationDataItemTransformJobsResponseAllOfTransformationJobs.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.get_organization_data_item_transform_jobs_response_all_of_transformation_jobs.GetOrganizationDataItemTransformJobsResponseAllOfTransformationJobs.to_json(
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
edgeimpulse_api.models.get_organization_data_item_transform_jobs_response_all_of_transformation_jobs.GetOrganizationDataItemTransformJobsResponseAllOfTransformationJobs.to_str(
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