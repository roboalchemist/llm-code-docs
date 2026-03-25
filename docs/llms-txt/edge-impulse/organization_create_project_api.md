# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/organization_create_project_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api.organization_create_project_api

## Classes

### OrganizationCreateProjectApi

```python  theme={"system"}
edgeimpulse_api.api.organization_create_project_api.OrganizationCreateProjectApi(
	api_client=None
)
```

| Parameters        |     |
| ----------------- | --- |
| `api_client=None` | ` ` |

***

**METHODS**

#### clear\_organization\_transform

```python  theme={"system"}
edgeimpulse_api.api.organization_create_project_api.OrganizationCreateProjectApi.clear_organization_transform(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	create_project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Create project job ID.')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Clear failed transform jobs

Clear all failed transform job from a create project job. Only jobs that have failed will be cleared.

| Parameters          |                                                                                                                            |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `self`              | ` `                                                                                                                        |
| `organization_id`   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`        |
| `create_project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Create project job ID.')]` |
| `**kwargs`          | ` `                                                                                                                        |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### delete\_organization\_create\_project

```python  theme={"system"}
edgeimpulse_api.api.organization_create_project_api.OrganizationCreateProjectApi.delete_organization_create_project(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	create_project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Create project job ID.')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Delete transformation job

Remove a transformation job. This will stop all running jobs.

| Parameters          |                                                                                                                            |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `self`              | ` `                                                                                                                        |
| `organization_id`   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`        |
| `create_project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Create project job ID.')]` |
| `**kwargs`          | ` `                                                                                                                        |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### delete\_organization\_create\_project\_file

```python  theme={"system"}
edgeimpulse_api.api.organization_create_project_api.OrganizationCreateProjectApi.delete_organization_create_project_file(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	create_project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Create project job ID.')],
	create_project_file_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Create project job file ID.')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Delete create project file

Remove a file from a create project job. Only files for which no jobs are running can be deleted.

| Parameters               |                                                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| `self`                   | ` `                                                                                                                             |
| `organization_id`        | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`             |
| `create_project_id`      | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Create project job ID.')]`      |
| `create_project_file_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Create project job file ID.')]` |
| `**kwargs`               | ` `                                                                                                                             |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### get\_organization\_create\_project\_status

```python  theme={"system"}
edgeimpulse_api.api.organization_create_project_api.OrganizationCreateProjectApi.get_organization_create_project_status(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	create_project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Create project job ID.')],
	transform_limit: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Maximum number of results of transformation jobs')],
	transform_offset: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Offset in results of transformation jobs, can be used in conjunction with TransformLimitResultsParameter to implement paging.')],
	selection: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description="Type of selected rows, either 'all', 'created', 'in-progress' or 'failed' (defaults to 'all')")] = None,
	**kwargs
) ‑> edgeimpulse_api.models.organization_create_project_status_response.OrganizationCreateProjectStatusResponse
```

Get transformation job status

Get the current status of a transformation job job.

| Parameters          |                                                                                                                                                                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`              | ` `                                                                                                                                                                                                                               |
| `organization_id`   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                                                               |
| `create_project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Create project job ID.')]`                                                                                                        |
| `transform_limit`   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Maximum number of results of transformation jobs')]`                                                                              |
| `transform_offset`  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Offset in results of transformation jobs, can be used in conjunction with TransformLimitResultsParameter to implement paging.')]` |
| `selection`         | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description="Type of selected rows, either 'all', 'created', 'in-progress' or 'failed' (defaults to 'all')")] = None`       |
| `**kwargs`          | ` `                                                                                                                                                                                                                               |

| Returns                                                                                                      |
| ------------------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.organization_create_project_status_response.OrganizationCreateProjectStatusResponse` |

#### get\_organization\_create\_projects

```python  theme={"system"}
edgeimpulse_api.api.organization_create_project_api.OrganizationCreateProjectApi.get_organization_create_projects(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	limit: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None,
	offset: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None,
	include_pipeline_jobs: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='If enabled, also includes jobs that are part of a pipeline')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.organization_get_create_projects_response.OrganizationGetCreateProjectsResponse
```

List transformation jobs

Get list of transformation jobs.

| Parameters              |                                                                                                                                                                                                                             |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                                                                                                                                         |
| `organization_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                                                         |
| `limit`                 | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None`                                                                     |
| `offset`                | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None` |
| `include_pipeline_jobs` | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='If enabled, also includes jobs that are part of a pipeline')] = None`                                   |
| `**kwargs`              | ` `                                                                                                                                                                                                                         |

| Returns                                                                                                  |
| -------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_get_create_projects_response.OrganizationGetCreateProjectsResponse` |

#### organization\_add\_collaborator

```python  theme={"system"}
edgeimpulse_api.api.organization_create_project_api.OrganizationCreateProjectApi.organization_add_collaborator(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	update_organization_add_collaborator_request: edgeimpulse_api.models.update_organization_add_collaborator_request.UpdateOrganizationAddCollaboratorRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Add a collaborator to a project within an organisation

Add a new collaborator to a project owned by an organisation.

| Parameters                                     |                                                                                                                     |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                                         | ` `                                                                                                                 |
| `organization_id`                              | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `update_organization_add_collaborator_request` | `edgeimpulse_api.models.update_organization_add_collaborator_request.UpdateOrganizationAddCollaboratorRequest`      |
| `**kwargs`                                     | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### organization\_create\_empty\_project

```python  theme={"system"}
edgeimpulse_api.api.organization_create_project_api.OrganizationCreateProjectApi.organization_create_empty_project(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	update_organization_create_empty_project_request: edgeimpulse_api.models.update_organization_create_empty_project_request.UpdateOrganizationCreateEmptyProjectRequest,
	**kwargs
) ‑> edgeimpulse_api.models.create_project_response.CreateProjectResponse
```

Create new empty project

Create a new empty project within an organization.

| Parameters                                         |                                                                                                                       |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `self`                                             | ` `                                                                                                                   |
| `organization_id`                                  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`   |
| `update_organization_create_empty_project_request` | `edgeimpulse_api.models.update_organization_create_empty_project_request.UpdateOrganizationCreateEmptyProjectRequest` |
| `**kwargs`                                         | ` `                                                                                                                   |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.create_project_response.CreateProjectResponse` |

#### organization\_create\_project

```python  theme={"system"}
edgeimpulse_api.api.organization_create_project_api.OrganizationCreateProjectApi.organization_create_project(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	organization_create_project_request: edgeimpulse_api.models.organization_create_project_request.OrganizationCreateProjectRequest,
	**kwargs
) ‑> edgeimpulse_api.models.organization_create_project_response.OrganizationCreateProjectResponse
```

Start transformation job

Start a transformation job to fetch data from the organization and put it in a project, or transform into new data.

| Parameters                            |                                                                                                                     |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                                | ` `                                                                                                                 |
| `organization_id`                     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `organization_create_project_request` | `edgeimpulse_api.models.organization_create_project_request.OrganizationCreateProjectRequest`                       |
| `**kwargs`                            | ` `                                                                                                                 |

| Returns                                                                                         |
| ----------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_create_project_response.OrganizationCreateProjectResponse` |

#### retry\_organization\_create\_project\_file

```python  theme={"system"}
edgeimpulse_api.api.organization_create_project_api.OrganizationCreateProjectApi.retry_organization_create_project_file(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	create_project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Create project job ID.')],
	create_project_file_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Create project job file ID.')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Retry transformation file

Retry a transformation action on a file from a transformation job. Only files that have failed can be retried.

| Parameters               |                                                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| `self`                   | ` `                                                                                                                             |
| `organization_id`        | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`             |
| `create_project_id`      | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Create project job ID.')]`      |
| `create_project_file_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Create project job file ID.')]` |
| `**kwargs`               | ` `                                                                                                                             |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### retry\_organization\_transform

```python  theme={"system"}
edgeimpulse_api.api.organization_create_project_api.OrganizationCreateProjectApi.retry_organization_transform(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	create_project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Create project job ID.')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Retry failed transform jobs

Retry all failed transform job from a transformation job. Only jobs that have failed will be retried.

| Parameters          |                                                                                                                            |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `self`              | ` `                                                                                                                        |
| `organization_id`   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`        |
| `create_project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Create project job ID.')]` |
| `**kwargs`          | ` `                                                                                                                        |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### retry\_organization\_upload

```python  theme={"system"}
edgeimpulse_api.api.organization_create_project_api.OrganizationCreateProjectApi.retry_organization_upload(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	create_project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Create project job ID.')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Retry transformation upload job

Retry the upload job from a transformation job. Only jobs that have failed can be retried.

| Parameters          |                                                                                                                            |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `self`              | ` `                                                                                                                        |
| `organization_id`   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`        |
| `create_project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Create project job ID.')]` |
| `**kwargs`          | ` `                                                                                                                        |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### update\_organization\_create\_project

```python  theme={"system"}
edgeimpulse_api.api.organization_create_project_api.OrganizationCreateProjectApi.update_organization_create_project(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	create_project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Create project job ID.')],
	update_organization_create_project_request: edgeimpulse_api.models.update_organization_create_project_request.UpdateOrganizationCreateProjectRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Update transformation job

Update the properties of a transformation job.

| Parameters                                   |                                                                                                                            |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `self`                                       | ` `                                                                                                                        |
| `organization_id`                            | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`        |
| `create_project_id`                          | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Create project job ID.')]` |
| `update_organization_create_project_request` | `edgeimpulse_api.models.update_organization_create_project_request.UpdateOrganizationCreateProjectRequest`                 |
| `**kwargs`                                   | ` `                                                                                                                        |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### upload\_custom\_block

```python  theme={"system"}
edgeimpulse_api.api.organization_create_project_api.OrganizationCreateProjectApi.upload_custom_block(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	tar: Annotated[str, Strict(strict=True)],
	type: Annotated[str, Strict(strict=True)],
	block_id: Annotated[int, Strict(strict=True)],
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Upload a custom block

Upload a zip file containing a custom transformation or deployment block.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `tar`             | `Annotated[str, Strict(strict=True)]`                                                                               |
| `type`            | `Annotated[str, Strict(strict=True)]`                                                                               |
| `block_id`        | `Annotated[int, Strict(strict=True)]`                                                                               |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |


Built with [Mintlify](https://mintlify.com).