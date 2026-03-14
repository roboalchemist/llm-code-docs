# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/jobs_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api.jobs_api

## Classes

### JobsApi

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi(
	api_client=None
)
```

| Parameters        |     |
| ----------------- | --- |
| `api_client=None` | ` ` |

***

**METHODS**

#### autotune\_dsp\_job

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.autotune_dsp_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	autotune_dsp_request: edgeimpulse_api.models.autotune_dsp_request.AutotuneDspRequest,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Autotune DSP parameters

Autotune DSP block parameters. Updates are streamed over the websocket API.

| Parameters             |                                                                                                                |
| ---------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                 | ` `                                                                                                            |
| `project_id`           | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `autotune_dsp_request` | `edgeimpulse_api.models.autotune_dsp_request.AutotuneDspRequest`                                               |
| `**kwargs`             | ` `                                                                                                            |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### build\_on\_device\_model\_job

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.build_on_device_model_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	type: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The name of the built target. You can find this by listing all deployment targets through `listDeploymentTargetsForProject` (via `GET /v1/api/{projectId}/deployment/targets`) and see the `format` type.')],
	build_on_device_model_request: edgeimpulse_api.models.build_on_device_model_request.BuildOnDeviceModelRequest,
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.build_on_device_model_response.BuildOnDeviceModelResponse
```

Build on-device model

Generate code to run the impulse on an embedded device. When this step is complete use `downloadHistoricDeployment` to download the artefacts. Updates are streamed over the websocket API.

| Parameters                      |                                                                                                                                                                                                                                                                                                                 |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                          | ` `                                                                                                                                                                                                                                                                                                             |
| `project_id`                    | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                                                                                                                  |
| `type`                          | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The name of the built target. You can find this by listing all deployment targets through `listDeploymentTargetsForProject` (via `GET /v1/api/`{projectId}`/deployment/targets`) and see the `format` type.')]` |
| `build_on_device_model_request` | `edgeimpulse_api.models.build_on_device_model_request.BuildOnDeviceModelRequest`                                                                                                                                                                                                                                |
| `impulse_id`                    | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None`                                                                                                                    |
| `**kwargs`                      | ` `                                                                                                                                                                                                                                                                                                             |

| Returns                                                                            |
| ---------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.build_on_device_model_response.BuildOnDeviceModelResponse` |

#### build\_organization\_on\_device\_model\_job

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.build_organization_on_device_model_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	build_organization_on_device_model_request: edgeimpulse_api.models.build_organization_on_device_model_request.BuildOrganizationOnDeviceModelRequest,
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.build_on_device_model_response.BuildOnDeviceModelResponse
```

Build organizational on-device model

Generate code to run the impulse on an embedded device using an organizational deployment block. When this step is complete use `downloadHistoricDeployment` to download the artefacts.  Updates are streamed over the websocket API.

| Parameters                                   |                                                                                                                                                                                              |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                                       | ` `                                                                                                                                                                                          |
| `project_id`                                 | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                               |
| `build_organization_on_device_model_request` | `edgeimpulse_api.models.build_organization_on_device_model_request.BuildOrganizationOnDeviceModelRequest`                                                                                    |
| `impulse_id`                                 | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None` |
| `**kwargs`                                   | ` `                                                                                                                                                                                          |

| Returns                                                                            |
| ---------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.build_on_device_model_response.BuildOnDeviceModelResponse` |

#### calculate\_data\_quality\_metrics

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.calculate_data_quality_metrics(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	calculate_data_quality_metrics_request: edgeimpulse_api.models.calculate_data_quality_metrics_request.CalculateDataQualityMetricsRequest,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Calculate data quality metrics. Only available for EI staff.

Calculate data quality metrics for the dataset

| Parameters                               |                                                                                                                |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                                   | ` `                                                                                                            |
| `project_id`                             | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `calculate_data_quality_metrics_request` | `edgeimpulse_api.models.calculate_data_quality_metrics_request.CalculateDataQualityMetricsRequest`             |
| `**kwargs`                               | ` `                                                                                                            |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### cancel\_job

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.cancel_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	job_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Job ID')],
	force_cancel: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description="If set to 'true', we won't wait for the job cluster to cancel the job, and will mark the job as finished.")] = None,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Cancel job

Cancel a running job.

| Parameters     |                                                                                                                                                                                                                                         |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`         | ` `                                                                                                                                                                                                                                     |
| `project_id`   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                                          |
| `job_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Job ID')]`                                                                                                                              |
| `force_cancel` | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description="If set to 'true', we won't wait for the job cluster to cancel the job, and will mark the job as finished.")] = None` |
| `**kwargs`     | ` `                                                                                                                                                                                                                                     |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### create\_ai\_actions\_job

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.create_ai_actions_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	action_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='AI Action ID')],
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Create AI Actions job

Run an AI Actions job over a subset of data. This will instruct the block to apply the changes directly to your dataset. To preview, use "createPreviewAIActionsJob". To set the config use `updateAIAction`.

| Parameters   |                                                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                              |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`   |
| `action_id`  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='AI Action ID')]` |
| `**kwargs`   | ` `                                                                                                              |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### create\_preview\_ai\_actions\_job

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.create_preview_ai_actions_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	action_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='AI Action ID')],
	create_preview_ai_actions_job_request: edgeimpulse_api.models.create_preview_ai_actions_job_request.CreatePreviewAIActionsJobRequest,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Create preview AI Actions job

Do a dry-run of an AI Actions job over a subset of data. This will instruct the block to propose changes to data items (via "setSampleProposedChanges") rather than apply the changes directly.

| Parameters                              |                                                                                                                  |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `self`                                  | ` `                                                                                                              |
| `project_id`                            | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`   |
| `action_id`                             | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='AI Action ID')]` |
| `create_preview_ai_actions_job_request` | `edgeimpulse_api.models.create_preview_ai_actions_job_request.CreatePreviewAIActionsJobRequest`                  |
| `**kwargs`                              | ` `                                                                                                              |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### create\_synthetic\_data\_job

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.create_synthetic_data_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	create_synthetic_data_request: edgeimpulse_api.models.create_synthetic_data_request.CreateSyntheticDataRequest,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Create synthetic data

Generate new synthetic data

| Parameters                      |                                                                                                                |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                          | ` `                                                                                                            |
| `project_id`                    | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `create_synthetic_data_request` | `edgeimpulse_api.models.create_synthetic_data_request.CreateSyntheticDataRequest`                              |
| `**kwargs`                      | ` `                                                                                                            |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### download\_jobs\_logs

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.download_jobs_logs(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	job_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Job ID')],
	limit: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None,
	log_level: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Log level (error, warn, info, debug)')] = None,
	**kwargs
) ‑> str
```

Download logs

Download the logs for a job (as a text file).

| Parameters   |                                                                                                                                                                    |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `self`       | ` `                                                                                                                                                                |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                     |
| `job_id`     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Job ID')]`                                                         |
| `limit`      | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None`            |
| `log_level`  | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Log level (error, warn, info, debug)')] = None` |
| `**kwargs`   | ` `                                                                                                                                                                |

| Returns |
| ------- |
| `str`   |

#### export\_keras\_block

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.export_keras_block(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	learn_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')],
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Export Keras block

Export the training pipeline of a Keras block. Updates are streamed over the websocket API.

| Parameters   |                                                                                                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                              |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                   |
| `learn_id`   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')]` |
| `**kwargs`   | ` `                                                                                                                                                              |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### export\_keras\_block\_data

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.export_keras_block_data(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	learn_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')],
	export_keras_block_data_request: edgeimpulse_api.models.export_keras_block_data_request.ExportKerasBlockDataRequest,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Export Keras block data

Export the data of a Keras block (already split in train/validate data). Updates are streamed over the websocket API.

| Parameters                        |                                                                                                                                                                  |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                            | ` `                                                                                                                                                              |
| `project_id`                      | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                   |
| `learn_id`                        | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')]` |
| `export_keras_block_data_request` | `edgeimpulse_api.models.export_keras_block_data_request.ExportKerasBlockDataRequest`                                                                             |
| `**kwargs`                        | ` `                                                                                                                                                              |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### generate\_data\_explorer\_features

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.generate_data_explorer_features(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Generate data explorer features

Generate features for the data explorer

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### generate\_features\_job

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.generate_features_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	generate_features_request: edgeimpulse_api.models.generate_features_request.GenerateFeaturesRequest,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Generate features

Take the raw training set and generate features from them. Updates are streamed over the websocket API.

| Parameters                  |                                                                                                                |
| --------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                      | ` `                                                                                                            |
| `project_id`                | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `generate_features_request` | `edgeimpulse_api.models.generate_features_request.GenerateFeaturesRequest`                                     |
| `**kwargs`                  | ` `                                                                                                            |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### get\_impulse\_migration\_job\_status

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.get_impulse_migration_job_status(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.get_job_response.GetJobResponse
```

Get impulse migration status

Get the status for the multi-impulse migration job in this project. This is a separate route so public projects can access it. If no multi-impulse migration jobs are present, an error will be thrown.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                  |
| -------------------------------------------------------- |
| `edgeimpulse_api.models.get_job_response.GetJobResponse` |

#### get\_impulse\_migration\_jobs\_logs

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.get_impulse_migration_jobs_logs(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	limit: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None,
	log_level: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Log level (error, warn, info, debug)')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.log_stdout_response.LogStdoutResponse
```

Get impulse migration logs

Get the logs for the multi-impulse migration job in this project. This is a separate route so public projects can access it. If no multi-impulse migration jobs are present, an error will be thrown.

| Parameters   |                                                                                                                                                                    |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `self`       | ` `                                                                                                                                                                |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                     |
| `limit`      | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None`            |
| `log_level`  | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Log level (error, warn, info, debug)')] = None` |
| `**kwargs`   | ` `                                                                                                                                                                |

| Returns                                                        |
| -------------------------------------------------------------- |
| `edgeimpulse_api.models.log_stdout_response.LogStdoutResponse` |

#### get\_job\_status

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.get_job_status(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	job_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Job ID')],
	**kwargs
) ‑> edgeimpulse_api.models.get_job_response.GetJobResponse
```

Get job status

Get the status for a job.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `job_id`     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Job ID')]`     |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                  |
| -------------------------------------------------------- |
| `edgeimpulse_api.models.get_job_response.GetJobResponse` |

#### get\_jobs\_logs

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.get_jobs_logs(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	job_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Job ID')],
	limit: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None,
	log_level: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Log level (error, warn, info, debug)')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.log_stdout_response.LogStdoutResponse
```

Get logs

Get the logs for a job.

| Parameters   |                                                                                                                                                                    |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `self`       | ` `                                                                                                                                                                |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                     |
| `job_id`     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Job ID')]`                                                         |
| `limit`      | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None`            |
| `log_level`  | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Log level (error, warn, info, debug)')] = None` |
| `**kwargs`   | ` `                                                                                                                                                                |

| Returns                                                        |
| -------------------------------------------------------------- |
| `edgeimpulse_api.models.log_stdout_response.LogStdoutResponse` |

#### get\_jobs\_summary

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.get_jobs_summary(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	start_date: Annotated[datetime.datetime, FieldInfo(annotation=NoneType, required=True, description='Start date')],
	end_date: Annotated[datetime.datetime, FieldInfo(annotation=NoneType, required=True, description='End date')],
	**kwargs
) ‑> edgeimpulse_api.models.job_summary_response.JobSummaryResponse
```

Job summary

Get a summary of jobs, grouped by key. Used to report to users how much compute they've used.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `start_date` | `Annotated[datetime.datetime, FieldInfo(annotation=NoneType, required=True, description='Start date')]`        |
| `end_date`   | `Annotated[datetime.datetime, FieldInfo(annotation=NoneType, required=True, description='End date')]`          |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.job_summary_response.JobSummaryResponse` |

#### get\_profile\_tflite\_job\_result

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.get_profile_tflite_job_result(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	job_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Job ID')],
	**kwargs
) ‑> edgeimpulse_api.models.profile_tf_lite_response.ProfileTfLiteResponse
```

Get TFLite profile result (GET)

Get the results from a job started from startProfileTfliteJob (via a GET request).

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `job_id`     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Job ID')]`     |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                 |
| ----------------------------------------------------------------------- |
| `edgeimpulse_api.models.profile_tf_lite_response.ProfileTfLiteResponse` |

#### get\_profile\_tflite\_job\_result\_via\_post\_request

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.get_profile_tflite_job_result_via_post_request(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	job_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Job ID')],
	**kwargs
) ‑> edgeimpulse_api.models.profile_tf_lite_response.ProfileTfLiteResponse
```

Get TFLite profile result (POST)

Get the results from a job started from startProfileTfliteJob (via a POST request).

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `job_id`     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Job ID')]`     |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                 |
| ----------------------------------------------------------------------- |
| `edgeimpulse_api.models.profile_tf_lite_response.ProfileTfLiteResponse` |

#### list\_active\_jobs

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.list_active_jobs(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	root_only: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Whether to exclude jobs with a parent ID (so jobs started as part of another job)')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.list_jobs_response.ListJobsResponse
```

List active jobs

Get all active jobs for this project

| Parameters   |                                                                                                                                                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                                              |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                   |
| `root_only`  | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Whether to exclude jobs with a parent ID (so jobs started as part of another job)')] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                                              |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.list_jobs_response.ListJobsResponse` |

#### list\_all\_jobs

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.list_all_jobs(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	start_date: Annotated[datetime.datetime | None, FieldInfo(annotation=NoneType, required=True, description='Start date')] = None,
	end_date: Annotated[datetime.datetime | None, FieldInfo(annotation=NoneType, required=True, description='End date')] = None,
	limit: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None,
	offset: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None,
	root_only: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Whether to exclude jobs with a parent ID (so jobs started as part of another job)')] = None,
	key: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Job key to filter on')] = None,
	category: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Job category to filter on')] = None,
	finished: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Job finish status to filter on')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.list_jobs_response.ListJobsResponse
```

List all jobs

Get all jobs for this project

| Parameters   |                                                                                                                                                                                                                             |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                                                         |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                              |
| `start_date` | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Start date')] = None`                                                                                                      |
| `end_date`   | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='End date')] = None`                                                                                                        |
| `limit`      | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None`                                                                     |
| `offset`     | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None` |
| `root_only`  | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Whether to exclude jobs with a parent ID (so jobs started as part of another job)')] = None`            |
| `key`        | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Job key to filter on')] = None`                                                                          |
| `category`   | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Job category to filter on')] = None`                                                                     |
| `finished`   | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Job finish status to filter on')] = None`                                                                |
| `**kwargs`   | ` `                                                                                                                                                                                                                         |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.list_jobs_response.ListJobsResponse` |

#### list\_finished\_jobs

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.list_finished_jobs(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	start_date: Annotated[datetime.datetime | None, FieldInfo(annotation=NoneType, required=True, description='Start date')] = None,
	end_date: Annotated[datetime.datetime | None, FieldInfo(annotation=NoneType, required=True, description='End date')] = None,
	limit: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None,
	offset: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None,
	root_only: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Whether to exclude jobs with a parent ID (so jobs started as part of another job)')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.list_jobs_response.ListJobsResponse
```

List finished jobs

Get all finished jobs for this project

| Parameters   |                                                                                                                                                                                                                             |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                                                         |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                              |
| `start_date` | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Start date')] = None`                                                                                                      |
| `end_date`   | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='End date')] = None`                                                                                                        |
| `limit`      | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None`                                                                     |
| `offset`     | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None` |
| `root_only`  | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Whether to exclude jobs with a parent ID (so jobs started as part of another job)')] = None`            |
| `**kwargs`   | ` `                                                                                                                                                                                                                         |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.list_jobs_response.ListJobsResponse` |

#### optimize\_job

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.optimize_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	extended_from_job_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Tuner coordinator job ID for the direct descendant job to extend this search from')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Optimize model

Evaluates optimal model architecture

| Parameters             |                                                                                                                                                                                                                 |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                 | ` `                                                                                                                                                                                                             |
| `project_id`           | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                  |
| `extended_from_job_id` | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Tuner coordinator job ID for the direct descendant job to extend this search from')] = None` |
| `**kwargs`             | ` `                                                                                                                                                                                                             |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### retry\_impulse\_migration

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.retry_impulse_migration(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Retry impulse migration

If an impulse migration previously failed, use this function to retry the job.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### set\_tuner\_primary\_job

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.set_tuner_primary_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	trial_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='trial ID')],
	set_tuner_primary_job_request: edgeimpulse_api.models.set_tuner_primary_job_request.SetTunerPrimaryJobRequest | None = None,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Sets EON tuner primary model

Sets EON tuner primary model

| Parameters                      |                                                                                                                |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                          | ` `                                                                                                            |
| `project_id`                    | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `trial_id`                      | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='trial ID')]`   |
| `set_tuner_primary_job_request` | `edgeimpulse_api.models.set_tuner_primary_job_request.SetTunerPrimaryJobRequest \| None = None`                |
| `**kwargs`                      | ` `                                                                                                            |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### start\_classify\_job

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.start_classify_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	start_classify_job_request: edgeimpulse_api.models.start_classify_job_request.StartClassifyJobRequest,
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Classify

Classifies all items in the testing dataset against the current impulse. Updates are streamed over the websocket API.

| Parameters                   |                                                                                                                                                                                              |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                       | ` `                                                                                                                                                                                          |
| `project_id`                 | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                               |
| `start_classify_job_request` | `edgeimpulse_api.models.start_classify_job_request.StartClassifyJobRequest`                                                                                                                  |
| `impulse_id`                 | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None` |
| `**kwargs`                   | ` `                                                                                                                                                                                          |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### start\_deploy\_pretrained\_model\_job

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.start_deploy_pretrained_model_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	deploy_pretrained_model_request: edgeimpulse_api.models.deploy_pretrained_model_request.DeployPretrainedModelRequest,
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Deploy pretrained model

Takes in a TFLite file and builds the model and SDK. Updates are streamed over the websocket API (or can be retrieved through the /stdout endpoint). Use getProfileTfliteJobResult to get the results when the job is completed.

| Parameters                        |                                                                                                                                                                                              |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                            | ` `                                                                                                                                                                                          |
| `project_id`                      | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                               |
| `deploy_pretrained_model_request` | `edgeimpulse_api.models.deploy_pretrained_model_request.DeployPretrainedModelRequest`                                                                                                        |
| `impulse_id`                      | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None` |
| `**kwargs`                        | ` `                                                                                                                                                                                          |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### start\_evaluate\_job

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.start_evaluate_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Evaluate

Evaluates every variant of the current impulse. Updates are streamed over the websocket API.

| Parameters   |                                                                                                                                                                                              |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                          |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                               |
| `impulse_id` | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                          |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### start\_import\_data\_from\_project\_job

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.start_import_data_from_project_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	import_data_from_another_project_job_request: edgeimpulse_api.models.import_data_from_another_project_job_request.ImportDataFromAnotherProjectJobRequest,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Import data from another project

Adds all data from an existing project into this project. This function is only available through a JWT token; and you can only add data from projects that you're a collaborator on.

| Parameters                                     |                                                                                                                |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                                         | ` `                                                                                                            |
| `project_id`                                   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `import_data_from_another_project_job_request` | `edgeimpulse_api.models.import_data_from_another_project_job_request.ImportDataFromAnotherProjectJobRequest`   |
| `**kwargs`                                     | ` `                                                                                                            |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### start\_keywords\_noise\_job

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.start_keywords_noise_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Add keywords and noise

Add keywords and noise data to a project (for getting started guide)

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### start\_make\_version\_public\_job

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.start_make_version_public_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	version_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Version ID')],
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Make a version public

Make a version of a project public. This makes all data and state available (read-only) on a public URL, and allows users to clone this project.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `version_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Version ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### start\_original\_export\_job

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.start_original_export_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	export_original_data_request: edgeimpulse_api.models.export_original_data_request.ExportOriginalDataRequest,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Export original data

Export all the data in the project as it was uploaded to Edge Impulse.  Updates are streamed over the websocket API.

| Parameters                     |                                                                                                                |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`                         | ` `                                                                                                            |
| `project_id`                   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `export_original_data_request` | `edgeimpulse_api.models.export_original_data_request.ExportOriginalDataRequest`                                |
| `**kwargs`                     | ` `                                                                                                            |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### start\_performance\_calibration\_job

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.start_performance_calibration_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	start_performance_calibration_request: edgeimpulse_api.models.start_performance_calibration_request.StartPerformanceCalibrationRequest,
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Performance Calibration

Simulates real world usage and returns performance metrics.

| Parameters                              |                                                                                                                                                                                              |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                                  | ` `                                                                                                                                                                                          |
| `project_id`                            | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                               |
| `start_performance_calibration_request` | `edgeimpulse_api.models.start_performance_calibration_request.StartPerformanceCalibrationRequest`                                                                                            |
| `impulse_id`                            | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None` |
| `**kwargs`                              | ` `                                                                                                                                                                                          |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### start\_post\_processing\_job

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.start_post_processing_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	start_post_processing_request: edgeimpulse_api.models.start_post_processing_request.StartPostProcessingRequest,
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Post-processing

Begins post processing job

| Parameters                      |                                                                                                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                          | ` `                                                                                                                                                                                          |
| `project_id`                    | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                               |
| `start_post_processing_request` | `edgeimpulse_api.models.start_post_processing_request.StartPostProcessingRequest`                                                                                                            |
| `impulse_id`                    | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None` |
| `**kwargs`                      | ` `                                                                                                                                                                                          |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### start\_profile\_tflite\_job

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.start_profile_tflite_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	profile_tf_lite_request: edgeimpulse_api.models.profile_tf_lite_request.ProfileTfLiteRequest,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Profile TFLite model

Takes in a TFLite model and returns the latency, RAM and ROM used for this model. Updates are streamed over the websocket API (or can be retrieved through the /stdout endpoint). Use getProfileTfliteJobResult to get the results when the job is completed.

| Parameters                |                                                                                                                |
| ------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                    | ` `                                                                                                            |
| `project_id`              | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `profile_tf_lite_request` | `edgeimpulse_api.models.profile_tf_lite_request.ProfileTfLiteRequest`                                          |
| `**kwargs`                | ` `                                                                                                            |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### start\_restore\_job

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.start_restore_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	restore_project_request: edgeimpulse_api.models.restore_project_request.RestoreProjectRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Restore project to version

Restore a project to a certain version. This can only applied to a project without data, and will overwrite your impulse and all settings.

| Parameters                |                                                                                                                |
| ------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                    | ` `                                                                                                            |
| `project_id`              | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `restore_project_request` | `edgeimpulse_api.models.restore_project_request.RestoreProjectRequest`                                         |
| `**kwargs`                | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### start\_restore\_job\_from\_public

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.start_restore_job_from_public(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	restore_project_from_public_request: edgeimpulse_api.models.restore_project_from_public_request.RestoreProjectFromPublicRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Restore project to public version

Restore a project to a certain public version. This can only applied to a project without data, and will overwrite your impulse and all settings.

| Parameters                            |                                                                                                                |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                                | ` `                                                                                                            |
| `project_id`                          | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `restore_project_from_public_request` | `edgeimpulse_api.models.restore_project_from_public_request.RestoreProjectFromPublicRequest`                   |
| `**kwargs`                            | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### start\_retrain\_job

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.start_retrain_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Retrain

Retrains the current impulse with the last known parameters. Updates are streamed over the websocket API.

| Parameters   |                                                                                                                                                                                              |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                          |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                               |
| `impulse_id` | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                          |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### start\_version\_job

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.start_version_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	project_version_request: edgeimpulse_api.models.project_version_request.ProjectVersionRequest,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Version project

Create a new version of the project. This stores all data and configuration offsite. If you have access to the enterprise version of Edge Impulse you can store your data in your own storage buckets (only through JWT token authentication).

| Parameters                |                                                                                                                |
| ------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                    | ` `                                                                                                            |
| `project_id`              | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `project_version_request` | `edgeimpulse_api.models.project_version_request.ProjectVersionRequest`                                         |
| `**kwargs`                | ` `                                                                                                            |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### start\_wav\_export\_job

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.start_wav_export_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	export_wav_data_request: edgeimpulse_api.models.export_wav_data_request.ExportWavDataRequest,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Export data as WAV

Export all the data in the project in WAV format.  Updates are streamed over the websocket API.

| Parameters                |                                                                                                                |
| ------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                    | ` `                                                                                                            |
| `project_id`              | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `export_wav_data_request` | `edgeimpulse_api.models.export_wav_data_request.ExportWavDataRequest`                                          |
| `**kwargs`                | ` `                                                                                                            |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### train\_anomaly\_job

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.train_anomaly_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	learn_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')],
	start_training_request_anomaly: edgeimpulse_api.models.start_training_request_anomaly.StartTrainingRequestAnomaly,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Train model (Anomaly)

Take the output from a DSP block and train an anomaly detection model using K-means or GMM. Updates are streamed over the websocket API.

| Parameters                       |                                                                                                                                                                  |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                           | ` `                                                                                                                                                              |
| `project_id`                     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                   |
| `learn_id`                       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')]` |
| `start_training_request_anomaly` | `edgeimpulse_api.models.start_training_request_anomaly.StartTrainingRequestAnomaly`                                                                              |
| `**kwargs`                       | ` `                                                                                                                                                              |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### train\_keras\_job

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.train_keras_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	learn_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')],
	set_keras_parameter_request: edgeimpulse_api.models.set_keras_parameter_request.SetKerasParameterRequest,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Train model (Keras)

Take the output from a DSP block and train a neural network using Keras. Updates are streamed over the websocket API.

| Parameters                    |                                                                                                                                                                  |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                        | ` `                                                                                                                                                              |
| `project_id`                  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                   |
| `learn_id`                    | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')]` |
| `set_keras_parameter_request` | `edgeimpulse_api.models.set_keras_parameter_request.SetKerasParameterRequest`                                                                                    |
| `**kwargs`                    | ` `                                                                                                                                                              |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### update\_job

```python  theme={"system"}
edgeimpulse_api.api.jobs_api.JobsApi.update_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	job_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Job ID')],
	update_job_request: edgeimpulse_api.models.update_job_request.UpdateJobRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Update job

Update a job.

| Parameters           |                                                                                                                |
| -------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`               | ` `                                                                                                            |
| `project_id`         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `job_id`             | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Job ID')]`     |
| `update_job_request` | `edgeimpulse_api.models.update_job_request.UpdateJobRequest`                                                   |
| `**kwargs`           | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |


Built with [Mintlify](https://mintlify.com).