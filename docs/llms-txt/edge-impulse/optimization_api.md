# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/optimization_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api.optimization_api

## Classes

### OptimizationApi

```python  theme={"system"}
edgeimpulse_api.api.optimization_api.OptimizationApi(
	api_client=None
)
```

| Parameters        |     |
| ----------------- | --- |
| `api_client=None` | ` ` |

***

**METHODS**

#### complete\_search

```python  theme={"system"}
edgeimpulse_api.api.optimization_api.OptimizationApi.complete_search(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	job_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Job ID', extra={})],
	tuner_complete_search: edgeimpulse_api.models.tuner_complete_search.TunerCompleteSearch,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Complete EON tuner run

Complete EON tuner run and mark it as succesful

| Parameters              |                                                                                                           |
| ----------------------- | --------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                       |
| `project_id`            | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `job_id`                | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Job ID', extra={})]`     |
| `tuner_complete_search` | `edgeimpulse_api.models.tuner_complete_search.TunerCompleteSearch`                                        |
| `**kwargs`              | ` `                                                                                                       |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### create\_trial

```python  theme={"system"}
edgeimpulse_api.api.optimization_api.OptimizationApi.create_trial(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	job_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Job ID', extra={})],
	tuner_create_trial_impulse: edgeimpulse_api.models.tuner_create_trial_impulse.TunerCreateTrialImpulse,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Create trial

Create trial

| Parameters                   |                                                                                                           |
| ---------------------------- | --------------------------------------------------------------------------------------------------------- |
| `self`                       | ` `                                                                                                       |
| `project_id`                 | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `job_id`                     | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Job ID', extra={})]`     |
| `tuner_create_trial_impulse` | `edgeimpulse_api.models.tuner_create_trial_impulse.TunerCreateTrialImpulse`                               |
| `**kwargs`                   | ` `                                                                                                       |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### delete\_state

```python  theme={"system"}
edgeimpulse_api.api.optimization_api.OptimizationApi.delete_state(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Delete EON tuner state

Completely clears the EON tuner state for this project.

| Parameters   |                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                       |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `**kwargs`   | ` `                                                                                                       |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### end\_trial

```python  theme={"system"}
edgeimpulse_api.api.optimization_api.OptimizationApi.end_trial(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	job_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Job ID', extra={})],
	trial_id: Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='trial ID', extra={})],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

End EON tuner trial

End an EON trial early. This can for example be used to implement early stopping.

| Parameters   |                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                       |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `job_id`     | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Job ID', extra={})]`     |
| `trial_id`   | `Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='trial ID', extra={})]`   |
| `**kwargs`   | ` `                                                                                                       |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### get\_all\_blocks

```python  theme={"system"}
edgeimpulse_api.api.optimization_api.OptimizationApi.get_all_blocks(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	**kwargs
) ‑> edgeimpulse_api.models.all_blocks_response.AllBlocksResponse
```

Get impulse blocks

Lists all possible blocks that can be used in the impulse, including any additional information required by the EON tuner that the getImpulseBlocks endpoint does not return

| Parameters   |                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                       |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `**kwargs`   | ` `                                                                                                       |

| Returns                                                        |
| -------------------------------------------------------------- |
| `edgeimpulse_api.models.all_blocks_response.AllBlocksResponse` |

#### get\_all\_learn\_blocks

```python  theme={"system"}
edgeimpulse_api.api.optimization_api.OptimizationApi.get_all_learn_blocks(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	**kwargs
) ‑> edgeimpulse_api.models.all_learn_blocks_response.AllLearnBlocksResponse
```

Get all available learn blocks

Get all available learn blocks

| Parameters   |                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                       |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `**kwargs`   | ` `                                                                                                       |

| Returns                                                                   |
| ------------------------------------------------------------------------- |
| `edgeimpulse_api.models.all_learn_blocks_response.AllLearnBlocksResponse` |

#### get\_config

```python  theme={"system"}
edgeimpulse_api.api.optimization_api.OptimizationApi.get_config(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	**kwargs
) ‑> edgeimpulse_api.models.optimize_config_response.OptimizeConfigResponse
```

Get config

Get config

| Parameters   |                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                       |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `**kwargs`   | ` `                                                                                                       |

| Returns                                                                  |
| ------------------------------------------------------------------------ |
| `edgeimpulse_api.models.optimize_config_response.OptimizeConfigResponse` |

#### get\_dsp\_parameters

```python  theme={"system"}
edgeimpulse_api.api.optimization_api.OptimizationApi.get_dsp_parameters(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	organization_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Organization ID', extra={})],
	organization_dsp_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Organization DSP ID', extra={})],
	**kwargs
) ‑> edgeimpulse_api.models.optimize_dsp_parameters_response.OptimizeDSPParametersResponse
```

Retrieves DSP block parameters

Retrieves DSP block parameters

| Parameters            |                                                                                                                    |
| --------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `self`                | ` `                                                                                                                |
| `project_id`          | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`          |
| `organization_id`     | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Organization ID', extra={})]`     |
| `organization_dsp_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Organization DSP ID', extra={})]` |
| `**kwargs`            | ` `                                                                                                                |

| Returns                                                                                 |
| --------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.optimize_dsp_parameters_response.OptimizeDSPParametersResponse` |

#### get\_space

```python  theme={"system"}
edgeimpulse_api.api.optimization_api.OptimizationApi.get_space(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	**kwargs
) ‑> edgeimpulse_api.models.optimize_space_response.OptimizeSpaceResponse
```

Search space

Search space

| Parameters   |                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                       |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `**kwargs`   | ` `                                                                                                       |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.optimize_space_response.OptimizeSpaceResponse` |

#### get\_state

```python  theme={"system"}
edgeimpulse_api.api.optimization_api.OptimizationApi.get_state(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	**kwargs
) ‑> edgeimpulse_api.models.optimize_state_response.OptimizeStateResponse
```

Retrieves the EON tuner state

Retrieves the EON tuner state

| Parameters   |                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                       |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `**kwargs`   | ` `                                                                                                       |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.optimize_state_response.OptimizeStateResponse` |

#### get\_transfer\_learning\_models

```python  theme={"system"}
edgeimpulse_api.api.optimization_api.OptimizationApi.get_transfer_learning_models(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	**kwargs
) ‑> edgeimpulse_api.models.optimize_transfer_learning_models_response.OptimizeTransferLearningModelsResponse
```

Retrieves available transfer learning models

Retrieves available transfer learning models

| Parameters   |                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                       |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `**kwargs`   | ` `                                                                                                       |

| Returns                                                                                                    |
| ---------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.optimize_transfer_learning_models_response.OptimizeTransferLearningModelsResponse` |

#### get\_trial\_logs

```python  theme={"system"}
edgeimpulse_api.api.optimization_api.OptimizationApi.get_trial_logs(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	trial_id: Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='trial ID', extra={})],
	**kwargs
) ‑> edgeimpulse_api.models.log_stdout_response.LogStdoutResponse
```

Get trial logs

Get the logs for a trial.

| Parameters   |                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                       |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `trial_id`   | `Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='trial ID', extra={})]`   |
| `**kwargs`   | ` `                                                                                                       |

| Returns                                                        |
| -------------------------------------------------------------- |
| `edgeimpulse_api.models.log_stdout_response.LogStdoutResponse` |

#### get\_tuner\_run\_state

```python  theme={"system"}
edgeimpulse_api.api.optimization_api.OptimizationApi.get_tuner_run_state(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	tuner_coordinator_job_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Tuner coordinator job ID', extra={})],
	**kwargs
) ‑> edgeimpulse_api.models.optimize_state_response.OptimizeStateResponse
```

Retrieves EON tuner state for a run.

Retrieves the EON tuner state for a specific run.

| Parameters                 |                                                                                                                         |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `self`                     | ` `                                                                                                                     |
| `project_id`               | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`               |
| `tuner_coordinator_job_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Tuner coordinator job ID', extra={})]` |
| `**kwargs`                 | ` `                                                                                                                     |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.optimize_state_response.OptimizeStateResponse` |

#### get\_window\_settings

```python  theme={"system"}
edgeimpulse_api.api.optimization_api.OptimizationApi.get_window_settings(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	**kwargs
) ‑> edgeimpulse_api.models.window_settings_response.WindowSettingsResponse
```

Get window settings

Get window settings

| Parameters   |                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                       |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `**kwargs`   | ` `                                                                                                       |

| Returns                                                                  |
| ------------------------------------------------------------------------ |
| `edgeimpulse_api.models.window_settings_response.WindowSettingsResponse` |

#### list\_tuner\_runs

```python  theme={"system"}
edgeimpulse_api.api.optimization_api.OptimizationApi.list_tuner_runs(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	**kwargs
) ‑> edgeimpulse_api.models.list_tuner_runs_response.ListTunerRunsResponse
```

List all tuner runs

List all the tuner runs for a project.

| Parameters   |                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                       |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `**kwargs`   | ` `                                                                                                       |

| Returns                                                                 |
| ----------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_tuner_runs_response.ListTunerRunsResponse` |

#### update\_config

```python  theme={"system"}
edgeimpulse_api.api.optimization_api.OptimizationApi.update_config(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	optimize_config: edgeimpulse_api.models.optimize_config.OptimizeConfig,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Update config

Update config

| Parameters        |                                                                                                           |
| ----------------- | --------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                       |
| `project_id`      | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `optimize_config` | `edgeimpulse_api.models.optimize_config.OptimizeConfig`                                                   |
| `**kwargs`        | ` `                                                                                                       |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### update\_tuner\_run

```python  theme={"system"}
edgeimpulse_api.api.optimization_api.OptimizationApi.update_tuner_run(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	tuner_coordinator_job_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Tuner coordinator job ID', extra={})],
	update_tuner_run_request: edgeimpulse_api.models.update_tuner_run_request.UpdateTunerRunRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Update EON tuner state

Updates the EON tuner state for a specific run.

| Parameters                 |                                                                                                                         |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `self`                     | ` `                                                                                                                     |
| `project_id`               | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`               |
| `tuner_coordinator_job_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Tuner coordinator job ID', extra={})]` |
| `update_tuner_run_request` | `edgeimpulse_api.models.update_tuner_run_request.UpdateTunerRunRequest`                                                 |
| `**kwargs`                 | ` `                                                                                                                     |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |


Built with [Mintlify](https://mintlify.com).