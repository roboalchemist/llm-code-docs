# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/organization_pipelines_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api.organization_pipelines_api

## Classes

### OrganizationPipelinesApi

```python  theme={"system"}
edgeimpulse_api.api.organization_pipelines_api.OrganizationPipelinesApi(
	api_client=None
)
```

| Parameters        |     |
| ----------------- | --- |
| `api_client=None` | ` ` |

***

**METHODS**

#### create\_organization\_pipeline

```python  theme={"system"}
edgeimpulse_api.api.organization_pipelines_api.OrganizationPipelinesApi.create_organization_pipeline(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	organization_update_pipeline_body: edgeimpulse_api.models.organization_update_pipeline_body.OrganizationUpdatePipelineBody,
	**kwargs
) ‑> edgeimpulse_api.models.entity_created_response.EntityCreatedResponse
```

Create pipeline

Create an organizational pipelines

| Parameters                          |                                                                                                                     |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                              | ` `                                                                                                                 |
| `organization_id`                   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `organization_update_pipeline_body` | `edgeimpulse_api.models.organization_update_pipeline_body.OrganizationUpdatePipelineBody`                           |
| `**kwargs`                          | ` `                                                                                                                 |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.entity_created_response.EntityCreatedResponse` |

#### delete\_organization\_pipeline

```python  theme={"system"}
edgeimpulse_api.api.organization_pipelines_api.OrganizationPipelinesApi.delete_organization_pipeline(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	pipeline_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Pipeline ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Delete pipeline

Delete an organizational pipelines

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `pipeline_id`     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Pipeline ID')]`     |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### get\_organization\_pipeline

```python  theme={"system"}
edgeimpulse_api.api.organization_pipelines_api.OrganizationPipelinesApi.get_organization_pipeline(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	pipeline_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Pipeline ID')],
	**kwargs
) ‑> edgeimpulse_api.models.get_organization_pipelines_response.GetOrganizationPipelinesResponse
```

Get pipeline

Retrieve an organizational pipelines

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `pipeline_id`     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Pipeline ID')]`     |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                                                       |
| --------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_organization_pipelines_response.GetOrganizationPipelinesResponse` |

#### list\_archived\_organization\_pipelines

```python  theme={"system"}
edgeimpulse_api.api.organization_pipelines_api.OrganizationPipelinesApi.list_archived_organization_pipelines(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	project_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='If set, filters on pipelines which are attached to this project.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.list_organization_pipelines_response.ListOrganizationPipelinesResponse
```

List archived pipelines

Retrieve all archived organizational pipelines

| Parameters        |                                                                                                                                                                                                |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                                                                                            |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                            |
| `project_id`      | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='If set, filters on pipelines which are attached to this project.')] = None` |
| `**kwargs`        | ` `                                                                                                                                                                                            |

| Returns                                                                                         |
| ----------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_organization_pipelines_response.ListOrganizationPipelinesResponse` |

#### list\_organization\_pipelines

```python  theme={"system"}
edgeimpulse_api.api.organization_pipelines_api.OrganizationPipelinesApi.list_organization_pipelines(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	project_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='If set, filters on pipelines which are attached to this project.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.list_organization_pipelines_response.ListOrganizationPipelinesResponse
```

List pipelines

Retrieve all organizational pipelines

| Parameters        |                                                                                                                                                                                                |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                                                                                            |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                            |
| `project_id`      | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='If set, filters on pipelines which are attached to this project.')] = None` |
| `**kwargs`        | ` `                                                                                                                                                                                            |

| Returns                                                                                         |
| ----------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_organization_pipelines_response.ListOrganizationPipelinesResponse` |

#### run\_organization\_pipeline

```python  theme={"system"}
edgeimpulse_api.api.organization_pipelines_api.OrganizationPipelinesApi.run_organization_pipeline(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	pipeline_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Pipeline ID')],
	ignore_last_successful_run: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='If set then `EI_LAST_SUCCESSFUL_RUN` is not set. You can use this to re-run a pipeline from scratch.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.run_organization_pipeline_response.RunOrganizationPipelineResponse
```

Run pipeline

Run an organizational pipeline

| Parameters                   |                                                                                                                                                                                                                                        |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                       | ` `                                                                                                                                                                                                                                    |
| `organization_id`            | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                                                                    |
| `pipeline_id`                | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Pipeline ID')]`                                                                                                                        |
| `ignore_last_successful_run` | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='If set then `EI\_LAST\_SUCCESSFUL\_RUN` is not set. You can use this to re-run a pipeline from scratch.')] = None` |
| `**kwargs`                   | ` `                                                                                                                                                                                                                                    |

| Returns                                                                                     |
| ------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.run_organization_pipeline_response.RunOrganizationPipelineResponse` |

#### stop\_organization\_pipeline

```python  theme={"system"}
edgeimpulse_api.api.organization_pipelines_api.OrganizationPipelinesApi.stop_organization_pipeline(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	pipeline_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Pipeline ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Stop a running pipeline

Stops the pipeline, and marks it as failed.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `pipeline_id`     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Pipeline ID')]`     |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### update\_organization\_pipeline

```python  theme={"system"}
edgeimpulse_api.api.organization_pipelines_api.OrganizationPipelinesApi.update_organization_pipeline(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	pipeline_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Pipeline ID')],
	organization_update_pipeline_body: edgeimpulse_api.models.organization_update_pipeline_body.OrganizationUpdatePipelineBody,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Update pipeline

Update an organizational pipelines

| Parameters                          |                                                                                                                     |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                              | ` `                                                                                                                 |
| `organization_id`                   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `pipeline_id`                       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Pipeline ID')]`     |
| `organization_update_pipeline_body` | `edgeimpulse_api.models.organization_update_pipeline_body.OrganizationUpdatePipelineBody`                           |
| `**kwargs`                          | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |


Built with [Mintlify](https://mintlify.com).