# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/organization_jobs_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api.organization_jobs_api

## Classes

### OrganizationJobsApi

```python  theme={"system"}
edgeimpulse_api.api.organization_jobs_api.OrganizationJobsApi(
	api_client=None
)
```

| Parameters        |     |
| ----------------- | --- |
| `api_client=None` | ` ` |

***

**METHODS**

#### cancel\_organization\_job

```python  theme={"system"}
edgeimpulse_api.api.organization_jobs_api.OrganizationJobsApi.cancel_organization_job(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	job_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Job ID')],
	force_cancel: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description="If set to 'true', we won't wait for the job cluster to cancel the job, and will mark the job as finished.")] = None,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Cancel job

Cancel a running job.

| Parameters        |                                                                                                                                                                                                                                         |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                                                                                                                                     |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                                                                     |
| `job_id`          | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Job ID')]`                                                                                                                              |
| `force_cancel`    | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description="If set to 'true', we won't wait for the job cluster to cancel the job, and will mark the job as finished.")] = None` |
| `**kwargs`        | ` `                                                                                                                                                                                                                                     |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### download\_organization\_jobs\_logs

```python  theme={"system"}
edgeimpulse_api.api.organization_jobs_api.OrganizationJobsApi.download_organization_jobs_logs(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	job_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Job ID')],
	limit: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None,
	log_level: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Log level (error, warn, info, debug)')] = None,
	**kwargs
) ‑> str
```

Download logs

Download the logs for a job (as a text file).

| Parameters        |                                                                                                                                                                    |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `self`            | ` `                                                                                                                                                                |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                |
| `job_id`          | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Job ID')]`                                                         |
| `limit`           | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None`            |
| `log_level`       | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Log level (error, warn, info, debug)')] = None` |
| `**kwargs`        | ` `                                                                                                                                                                |

| Returns |
| ------- |
| `str`   |

#### get\_organization\_job\_status

```python  theme={"system"}
edgeimpulse_api.api.organization_jobs_api.OrganizationJobsApi.get_organization_job_status(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	job_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Job ID')],
	**kwargs
) ‑> edgeimpulse_api.models.get_job_response.GetJobResponse
```

Get job status

Get the status for a job.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `job_id`          | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Job ID')]`          |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                  |
| -------------------------------------------------------- |
| `edgeimpulse_api.models.get_job_response.GetJobResponse` |

#### get\_organization\_jobs\_logs

```python  theme={"system"}
edgeimpulse_api.api.organization_jobs_api.OrganizationJobsApi.get_organization_jobs_logs(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	job_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Job ID')],
	limit: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None,
	log_level: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Log level (error, warn, info, debug)')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.log_stdout_response.LogStdoutResponse
```

Get logs

Get the logs for a job.

| Parameters        |                                                                                                                                                                    |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `self`            | ` `                                                                                                                                                                |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                |
| `job_id`          | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Job ID')]`                                                         |
| `limit`           | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None`            |
| `log_level`       | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Log level (error, warn, info, debug)')] = None` |
| `**kwargs`        | ` `                                                                                                                                                                |

| Returns                                                        |
| -------------------------------------------------------------- |
| `edgeimpulse_api.models.log_stdout_response.LogStdoutResponse` |

#### get\_organization\_socket\_token

```python  theme={"system"}
edgeimpulse_api.api.organization_jobs_api.OrganizationJobsApi.get_organization_socket_token(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	**kwargs
) ‑> edgeimpulse_api.models.socket_token_response.SocketTokenResponse
```

Get socket token for an organization

Get a token to authenticate with the web socket interface.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.socket_token_response.SocketTokenResponse` |

#### list\_active\_organization\_jobs

```python  theme={"system"}
edgeimpulse_api.api.organization_jobs_api.OrganizationJobsApi.list_active_organization_jobs(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	root_only: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Whether to exclude jobs with a parent ID (so jobs started as part of another job)')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.list_jobs_response.ListJobsResponse
```

List active jobs

Get all active jobs for this organization

| Parameters        |                                                                                                                                                                                                                  |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                                                                                                              |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                                              |
| `root_only`       | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Whether to exclude jobs with a parent ID (so jobs started as part of another job)')] = None` |
| `**kwargs`        | ` `                                                                                                                                                                                                              |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.list_jobs_response.ListJobsResponse` |

#### list\_all\_organization\_jobs

```python  theme={"system"}
edgeimpulse_api.api.organization_jobs_api.OrganizationJobsApi.list_all_organization_jobs(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	start_date: Annotated[datetime.datetime | None, FieldInfo(annotation=NoneType, required=True, description='Start date')] = None,
	end_date: Annotated[datetime.datetime | None, FieldInfo(annotation=NoneType, required=True, description='End date')] = None,
	limit: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None,
	offset: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None,
	exclude_pipeline_transform_jobs: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Whether to exclude pipeline / transformation jobs')] = None,
	root_only: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Whether to exclude jobs with a parent ID (so jobs started as part of another job)')] = None,
	key: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Job key to filter on')] = None,
	category: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Job category to filter on')] = None,
	finished: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Job finish status to filter on')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.list_jobs_response.ListJobsResponse
```

List all jobs

Get all jobs for this organization

| Parameters                        |                                                                                                                                                                                                                             |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                            | ` `                                                                                                                                                                                                                         |
| `organization_id`                 | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                                                         |
| `start_date`                      | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Start date')] = None`                                                                                                      |
| `end_date`                        | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='End date')] = None`                                                                                                        |
| `limit`                           | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None`                                                                     |
| `offset`                          | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None` |
| `exclude_pipeline_transform_jobs` | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Whether to exclude pipeline / transformation jobs')] = None`                                            |
| `root_only`                       | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Whether to exclude jobs with a parent ID (so jobs started as part of another job)')] = None`            |
| `key`                             | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Job key to filter on')] = None`                                                                          |
| `category`                        | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Job category to filter on')] = None`                                                                     |
| `finished`                        | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Job finish status to filter on')] = None`                                                                |
| `**kwargs`                        | ` `                                                                                                                                                                                                                         |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.list_jobs_response.ListJobsResponse` |

#### list\_finished\_organization\_jobs

```python  theme={"system"}
edgeimpulse_api.api.organization_jobs_api.OrganizationJobsApi.list_finished_organization_jobs(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	start_date: Annotated[datetime.datetime | None, FieldInfo(annotation=NoneType, required=True, description='Start date')] = None,
	end_date: Annotated[datetime.datetime | None, FieldInfo(annotation=NoneType, required=True, description='End date')] = None,
	limit: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None,
	offset: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None,
	root_only: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Whether to exclude jobs with a parent ID (so jobs started as part of another job)')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.list_jobs_response.ListJobsResponse
```

List finished jobs

Get all finished jobs for this organization

| Parameters        |                                                                                                                                                                                                                             |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                                                                                                                         |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                                                         |
| `start_date`      | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Start date')] = None`                                                                                                      |
| `end_date`        | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='End date')] = None`                                                                                                        |
| `limit`           | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None`                                                                     |
| `offset`          | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None` |
| `root_only`       | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Whether to exclude jobs with a parent ID (so jobs started as part of another job)')] = None`            |
| `**kwargs`        | ` `                                                                                                                                                                                                                         |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.list_jobs_response.ListJobsResponse` |


Built with [Mintlify](https://mintlify.com).