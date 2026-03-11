# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/deployment_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api.deployment_api

## Classes

### DeploymentApi

```python  theme={"system"}
edgeimpulse_api.api.deployment_api.DeploymentApi(
	api_client=None
)
```

| Parameters        |     |
| ----------------- | --- |
| `api_client=None` | ` ` |

***

**METHODS**

#### download\_build

```python  theme={"system"}
edgeimpulse_api.api.deployment_api.DeploymentApi.download_build(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	type: Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='The name of the built target. You can find this by listing all deployment targets through `listDeploymentTargetsForProject` (via `GET /v1/api/{projectId}/deployment/targets`) and see the `format` type.', extra={})],
	model_type: Annotated[edgeimpulse_api.models.keras_model_type_enum.KerasModelTypeEnum | None, FieldInfo(default=PydanticUndefined, description='Optional model type of the build (if not, it uses the settings in the Keras block)', extra={})] = None,
	engine: Annotated[edgeimpulse_api.models.deployment_target_engine.DeploymentTargetEngine | None, FieldInfo(default=PydanticUndefined, description='Optional engine for the build (if not, it uses the default engine for the deployment target)', extra={})] = None,
	impulse_id: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None,
	**kwargs
) ‑> str
```

Download

DEPRECATED, use downloadHistoricDeployment instead. Download the build artefacts for a project.

| Parameters   |                                                                                                                                                                                                                                                                                                            |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                                                                                                                                        |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                                                                                                                                                  |
| `type`       | `Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='The name of the built target. You can find this by listing all deployment targets through `listDeploymentTargetsForProject` (via `GET /v1/api/`{projectId}`/deployment/targets`) and see the `format` type.', extra={})]` |
| `model_type` | `Annotated[edgeimpulse_api.models.keras_model_type_enum.KerasModelTypeEnum \| None, FieldInfo(default=PydanticUndefined, description='Optional model type of the build (if not, it uses the settings in the Keras block)', extra={})] = None`                                                              |
| `engine`     | `Annotated[edgeimpulse_api.models.deployment_target_engine.DeploymentTargetEngine \| None, FieldInfo(default=PydanticUndefined, description='Optional engine for the build (if not, it uses the default engine for the deployment target)', extra={})] = None`                                             |
| `impulse_id` | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None`                                                                                                                      |
| `**kwargs`   | ` `                                                                                                                                                                                                                                                                                                        |

| Returns |
| ------- |
| `str`   |

#### download\_historic\_deployment

```python  theme={"system"}
edgeimpulse_api.api.deployment_api.DeploymentApi.download_historic_deployment(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	deployment_version: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Deployment version ID', extra={})],
	**kwargs
) ‑> str
```

Download historic deployment

Download a previously built deployment (use listDeploymentHistory to see all deployments).

| Parameters           |                                                                                                                      |
| -------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `self`               | ` `                                                                                                                  |
| `project_id`         | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`            |
| `deployment_version` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Deployment version ID', extra={})]` |
| `**kwargs`           | ` `                                                                                                                  |

| Returns |
| ------- |
| `str`   |

#### find\_syntiant\_posterior

```python  theme={"system"}
edgeimpulse_api.api.deployment_api.DeploymentApi.find_syntiant_posterior(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	target_words: List[pydantic.v1.types.StrictStr],
	reference_set: pydantic.v1.types.StrictStr,
	impulse_id: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None,
	wav_file: pydantic.v1.types.StrictStr | None = None,
	meta_csv_file: pydantic.v1.types.StrictStr | None = None,
	deployment_target: pydantic.v1.types.StrictStr | None = None,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Find Syntiant posterior parameters

Automatically find the current posterior parameters for the Syntiant deployment target

| Parameters          |                                                                                                                                                                                       |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`              | ` `                                                                                                                                                                                   |
| `project_id`        | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                             |
| `target_words`      | `List[pydantic.v1.types.StrictStr]`                                                                                                                                                   |
| `reference_set`     | `pydantic.v1.types.StrictStr`                                                                                                                                                         |
| `impulse_id`        | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None` |
| `wav_file`          | `pydantic.v1.types.StrictStr \| None = None`                                                                                                                                          |
| `meta_csv_file`     | `pydantic.v1.types.StrictStr \| None = None`                                                                                                                                          |
| `deployment_target` | `pydantic.v1.types.StrictStr \| None = None`                                                                                                                                          |
| `**kwargs`          | ` `                                                                                                                                                                                   |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### get\_deployment

```python  theme={"system"}
edgeimpulse_api.api.deployment_api.DeploymentApi.get_deployment(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	type: Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='The name of the built target. You can find this by listing all deployment targets through `listDeploymentTargetsForProject` (via `GET /v1/api/{projectId}/deployment/targets`) and see the `format` type.', extra={})],
	model_type: Annotated[edgeimpulse_api.models.keras_model_type_enum.KerasModelTypeEnum | None, FieldInfo(default=PydanticUndefined, description='Optional model type of the build (if not, it uses the settings in the Keras block)', extra={})] = None,
	engine: Annotated[edgeimpulse_api.models.deployment_target_engine.DeploymentTargetEngine | None, FieldInfo(default=PydanticUndefined, description='Optional engine for the build (if not, it uses the default engine for the deployment target)', extra={})] = None,
	impulse_id: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None,
	**kwargs
) ‑> edgeimpulse_api.models.get_deployment_response.GetDeploymentResponse
```

Get deployment info

Gives information on whether a deployment was already built for a type

| Parameters   |                                                                                                                                                                                                                                                                                                            |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                                                                                                                                        |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                                                                                                                                                  |
| `type`       | `Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='The name of the built target. You can find this by listing all deployment targets through `listDeploymentTargetsForProject` (via `GET /v1/api/`{projectId}`/deployment/targets`) and see the `format` type.', extra={})]` |
| `model_type` | `Annotated[edgeimpulse_api.models.keras_model_type_enum.KerasModelTypeEnum \| None, FieldInfo(default=PydanticUndefined, description='Optional model type of the build (if not, it uses the settings in the Keras block)', extra={})] = None`                                                              |
| `engine`     | `Annotated[edgeimpulse_api.models.deployment_target_engine.DeploymentTargetEngine \| None, FieldInfo(default=PydanticUndefined, description='Optional engine for the build (if not, it uses the default engine for the deployment target)', extra={})] = None`                                             |
| `impulse_id` | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None`                                                                                                                      |
| `**kwargs`   | ` `                                                                                                                                                                                                                                                                                                        |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_deployment_response.GetDeploymentResponse` |

#### get\_evaluate\_job\_result

```python  theme={"system"}
edgeimpulse_api.api.deployment_api.DeploymentApi.get_evaluate_job_result(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	impulse_id: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None,
	**kwargs
) ‑> edgeimpulse_api.models.evaluate_job_response.EvaluateJobResponse
```

Evaluate job result

Get evaluate job result, containing detailed performance statistics for every possible variant of the impulse.

| Parameters   |                                                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                   |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                             |
| `impulse_id` | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                   |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.evaluate_job_response.EvaluateJobResponse` |

#### get\_evaluate\_job\_result\_cache

```python  theme={"system"}
edgeimpulse_api.api.deployment_api.DeploymentApi.get_evaluate_job_result_cache(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	impulse_id: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None,
	**kwargs
) ‑> edgeimpulse_api.models.evaluate_job_response.EvaluateJobResponse
```

Check evaluate job result (cache)

Get evaluate job result, containing detailed performance statistics for every possible variant of the impulse. This only checks cache, and throws an error if there is no data in cache.

| Parameters   |                                                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                   |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                             |
| `impulse_id` | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                   |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.evaluate_job_response.EvaluateJobResponse` |

#### get\_historic\_deployment

```python  theme={"system"}
edgeimpulse_api.api.deployment_api.DeploymentApi.get_historic_deployment(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	deployment_version: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Deployment version ID', extra={})],
	**kwargs
) ‑> edgeimpulse_api.models.get_deployment_history_response.GetDeploymentHistoryResponse
```

Get historic deployment

Get info about a previously built deployment.

| Parameters           |                                                                                                                      |
| -------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `self`               | ` `                                                                                                                  |
| `project_id`         | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`            |
| `deployment_version` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Deployment version ID', extra={})]` |
| `**kwargs`           | ` `                                                                                                                  |

| Returns                                                                               |
| ------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_deployment_history_response.GetDeploymentHistoryResponse` |

#### get\_last\_deployment\_build

```python  theme={"system"}
edgeimpulse_api.api.deployment_api.DeploymentApi.get_last_deployment_build(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	impulse_id: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None,
	**kwargs
) ‑> edgeimpulse_api.models.get_last_deployment_build_response.GetLastDeploymentBuildResponse
```

Get information on the last deployment build

Get information on the result of the last successful deployment job, including info on the build e.g. whether it is still valid.

| Parameters   |                                                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                   |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                             |
| `impulse_id` | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                   |

| Returns                                                                                    |
| ------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.get_last_deployment_build_response.GetLastDeploymentBuildResponse` |

#### get\_syntiant\_posterior

```python  theme={"system"}
edgeimpulse_api.api.deployment_api.DeploymentApi.get_syntiant_posterior(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	impulse_id: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None,
	**kwargs
) ‑> edgeimpulse_api.models.get_syntiant_posterior_response.GetSyntiantPosteriorResponse
```

Get Syntiant posterior parameters

Get the current posterior parameters for the Syntiant deployment target

| Parameters   |                                                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                   |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                             |
| `impulse_id` | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                   |

| Returns                                                                               |
| ------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_syntiant_posterior_response.GetSyntiantPosteriorResponse` |

#### list\_all\_deployment\_targets

```python  theme={"system"}
edgeimpulse_api.api.deployment_api.DeploymentApi.list_all_deployment_targets(
	self,
	**kwargs
) ‑> edgeimpulse_api.models.deployment_targets_response.DeploymentTargetsResponse
```

Deployment targets

List all deployment targets

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |
| `**kwargs` | ` ` |

| Returns                                                                        |
| ------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.deployment_targets_response.DeploymentTargetsResponse` |

#### list\_deployment\_history

```python  theme={"system"}
edgeimpulse_api.api.deployment_api.DeploymentApi.list_deployment_history(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	impulse_id: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset, data for all impulses is returned.', extra={})] = None,
	limit: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Maximum number of results', extra={})] = None,
	offset: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.', extra={})] = None,
	**kwargs
) ‑> edgeimpulse_api.models.list_deployment_history_response.ListDeploymentHistoryResponse
```

List deployment history

Lists all successfully built deployments.

| Parameters   |                                                                                                                                                                                                                      |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                                                  |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                                                            |
| `impulse_id` | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset, data for all impulses is returned.', extra={})] = None`                              |
| `limit`      | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Maximum number of results', extra={})] = None`                                                                     |
| `offset`     | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.', extra={})] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                                                  |

| Returns                                                                                 |
| --------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_deployment_history_response.ListDeploymentHistoryResponse` |

#### list\_deployment\_targets\_for\_project

```python  theme={"system"}
edgeimpulse_api.api.deployment_api.DeploymentApi.list_deployment_targets_for_project(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	impulse_id: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None,
	**kwargs
) ‑> edgeimpulse_api.models.project_deployment_targets_response.ProjectDeploymentTargetsResponse
```

Deployment targets

List deployment targets for a project

| Parameters   |                                                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                   |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                             |
| `impulse_id` | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                   |

| Returns                                                                                       |
| --------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.project_deployment_targets_response.ProjectDeploymentTargetsResponse` |

#### list\_deployment\_targets\_for\_project\_data\_sources

```python  theme={"system"}
edgeimpulse_api.api.deployment_api.DeploymentApi.list_deployment_targets_for_project_data_sources(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	impulse_id: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None,
	**kwargs
) ‑> edgeimpulse_api.models.deployment_targets_response.DeploymentTargetsResponse
```

Deployment targets (data sources)

List deployment targets for a project from data sources page  (it shows some things like all Linux deploys, and hides 'fake' deploy targets like mobile phone / computer)

| Parameters   |                                                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                   |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                             |
| `impulse_id` | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                   |

| Returns                                                                        |
| ------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.deployment_targets_response.DeploymentTargetsResponse` |

#### set\_syntiant\_posterior

```python  theme={"system"}
edgeimpulse_api.api.deployment_api.DeploymentApi.set_syntiant_posterior(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	set_syntiant_posterior_request: edgeimpulse_api.models.set_syntiant_posterior_request.SetSyntiantPosteriorRequest,
	impulse_id: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Set Syntiant posterior parameters

Set the current posterior parameters for the Syntiant deployment target

| Parameters                       |                                                                                                                                                                                       |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                           | ` `                                                                                                                                                                                   |
| `project_id`                     | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                             |
| `set_syntiant_posterior_request` | `edgeimpulse_api.models.set_syntiant_posterior_request.SetSyntiantPosteriorRequest`                                                                                                   |
| `impulse_id`                     | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None` |
| `**kwargs`                       | ` `                                                                                                                                                                                   |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |


Built with [Mintlify](https://mintlify.com).