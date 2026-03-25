# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/projects_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api.projects_api

## Classes

### ProjectsApi

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi(
	api_client=None
)
```

| Parameters        |     |
| ----------------- | --- |
| `api_client=None` | ` ` |

***

**METHODS**

#### add\_collaborator

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.add_collaborator(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	add_collaborator_request: edgeimpulse_api.models.add_collaborator_request.AddCollaboratorRequest,
	**kwargs
) ‑> edgeimpulse_api.models.entity_created_response.EntityCreatedResponse
```

Add collaborator

Add a collaborator to a project.

| Parameters                 |                                                                                                                |
| -------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                     | ` `                                                                                                            |
| `project_id`               | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `add_collaborator_request` | `edgeimpulse_api.models.add_collaborator_request.AddCollaboratorRequest`                                       |
| `**kwargs`                 | ` `                                                                                                            |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.entity_created_response.EntityCreatedResponse` |

#### add\_project\_api\_key

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.add_project_api_key(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	add_project_api_key_request: edgeimpulse_api.models.add_project_api_key_request.AddProjectApiKeyRequest,
	**kwargs
) ‑> edgeimpulse_api.models.add_api_key_response.AddApiKeyResponse
```

Add API key

Add an API key. If you set `developmentKey` to `true` this flag will be removed from the current development API key.

| Parameters                    |                                                                                                                |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                        | ` `                                                                                                            |
| `project_id`                  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `add_project_api_key_request` | `edgeimpulse_api.models.add_project_api_key_request.AddProjectApiKeyRequest`                                   |
| `**kwargs`                    | ` `                                                                                                            |

| Returns                                                         |
| --------------------------------------------------------------- |
| `edgeimpulse_api.models.add_api_key_response.AddApiKeyResponse` |

#### add\_project\_hmac\_key

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.add_project_hmac_key(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	add_hmac_key_request: edgeimpulse_api.models.add_hmac_key_request.AddHmacKeyRequest,
	**kwargs
) ‑> edgeimpulse_api.models.entity_created_response.EntityCreatedResponse
```

Add HMAC key

Add an HMAC key. If you set `developmentKey` to `true` this flag will be removed from the current development HMAC key.

| Parameters             |                                                                                                                |
| ---------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                 | ` `                                                                                                            |
| `project_id`           | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `add_hmac_key_request` | `edgeimpulse_api.models.add_hmac_key_request.AddHmacKeyRequest`                                                |
| `**kwargs`             | ` `                                                                                                            |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.entity_created_response.EntityCreatedResponse` |

#### clear\_ai\_actions\_proposed\_changes

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.clear_ai_actions_proposed_changes(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	action_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='AI Action ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Clear AI Actions proposed changes

Remove all proposed changes for an AI Actions job.

| Parameters   |                                                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                              |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`   |
| `action_id`  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='AI Action ID')]` |
| `**kwargs`   | ` `                                                                                                              |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### create\_ai\_action

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.create_ai_action(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.entity_created_response.EntityCreatedResponse
```

Create AI Action

Create a new AI Action.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.entity_created_response.EntityCreatedResponse` |

#### create\_project

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.create_project(
	self,
	create_project_request: edgeimpulse_api.models.create_project_request.CreateProjectRequest,
	**kwargs
) ‑> edgeimpulse_api.models.create_project_response.CreateProjectResponse
```

Create new project

Create a new project. This API can only be called using a JWT token.

| Parameters               |                                                                      |
| ------------------------ | -------------------------------------------------------------------- |
| `self`                   | ` `                                                                  |
| `create_project_request` | `edgeimpulse_api.models.create_project_request.CreateProjectRequest` |
| `**kwargs`               | ` `                                                                  |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.create_project_response.CreateProjectResponse` |

#### delete\_ai\_action

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.delete_ai_action(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	action_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='AI Action ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Delete AI Actions config

Deletes an AI Actions.

| Parameters   |                                                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                              |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`   |
| `action_id`  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='AI Action ID')]` |
| `**kwargs`   | ` `                                                                                                              |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### delete\_project

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.delete_project(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Remove project

Remove the current project, and all data associated with it. This is irrevocable!

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### delete\_version

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.delete_version(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	version_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Version ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Delete versions

Delete a version. This does not delete the version from cold storage.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `version_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Version ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### download\_csv\_wizard\_config

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.download_csv_wizard_config(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> str
```

Download CSV Wizard config

Returns a JSON file with the current CSV wizard config. If there is no config this will throw a 5xx error.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns |
| ------- |
| `str`   |

#### download\_csv\_wizard\_uploaded\_file

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.download_csv_wizard_uploaded_file(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> str
```

Download CSV Wizard uploaded file

Returns the file that was uploaded when the CSV wizard was configured. If there is no config this will throw a 5xx error.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns |
| ------- |
| `str`   |

#### get\_ai\_action

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.get_ai_action(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	action_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='AI Action ID')],
	**kwargs
) ‑> edgeimpulse_api.models.get_ai_action_response.GetAIActionResponse
```

Get AI Actions config

Get an AI Actions config

| Parameters   |                                                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                              |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`   |
| `action_id`  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='AI Action ID')]` |
| `**kwargs`   | ` `                                                                                                              |

| Returns                                                             |
| ------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_ai_action_response.GetAIActionResponse` |

#### get\_csv\_wizard\_uploaded\_file\_info

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.get_csv_wizard_uploaded_file_info(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.get_csv_wizard_uploaded_file_info.GetCsvWizardUploadedFileInfo
```

Get CSV Wizard uploaded file info

Returns whether the file that was uploaded when the CSV wizard was configured is available.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                                 |
| --------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_csv_wizard_uploaded_file_info.GetCsvWizardUploadedFileInfo` |

#### get\_model\_variants

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.get_model_variants(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.get_model_variants_response.GetModelVariantsResponse
```

Get a list of all model variants available for this project

Get a list of model variants applicable to all trained learn blocks in this project.

| Parameters   |                                                                                                                                                                                              |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                          |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                               |
| `impulse_id` | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                          |

| Returns                                                                       |
| ----------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_model_variants_response.GetModelVariantsResponse` |

#### get\_new\_ai\_action

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.get_new_ai_action(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.get_ai_action_response.GetAIActionResponse
```

Get new AI Actions config

Get the AI Actions config for a new action

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                             |
| ------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_ai_action_response.GetAIActionResponse` |

#### get\_project\_data\_axes\_summary

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.get_project_data_axes_summary(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	include_disabled: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Whether to include disabled samples. Defaults to true')] = None,
	include_not_processed: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Whether to include non-processed samples. Defaults to true')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.project_data_axes_summary_response.ProjectDataAxesSummaryResponse
```

Get data axes summary

Get a list of axes that are present in the training data.

| Parameters              |                                                                                                                                                                                           |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                                                                                                       |
| `project_id`            | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                            |
| `include_disabled`      | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Whether to include disabled samples. Defaults to true')] = None`      |
| `include_not_processed` | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Whether to include non-processed samples. Defaults to true')] = None` |
| `**kwargs`              | ` `                                                                                                                                                                                       |

| Returns                                                                                    |
| ------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.project_data_axes_summary_response.ProjectDataAxesSummaryResponse` |

#### get\_project\_info

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.get_project_info(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.project_info_response.ProjectInfoResponse
```

Project information

List all information about this project.

| Parameters   |                                                                                                                                                                                              |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                          |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                               |
| `impulse_id` | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                          |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.project_info_response.ProjectInfoResponse` |

#### get\_project\_info\_summary

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.get_project_info_summary(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.project_info_summary_response.ProjectInfoSummaryResponse
```

Public project information

List a summary about this project - available for public projects.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                           |
| --------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.project_info_summary_response.ProjectInfoSummaryResponse` |

#### get\_project\_last\_modification\_date

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.get_project_last_modification_date(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.last_modification_date_response.LastModificationDateResponse
```

Last modification

Get the last modification date for a project (will be upped when data is modified, or when an impulse is trained)

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                               |
| ------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.last_modification_date_response.LastModificationDateResponse` |

#### get\_project\_recommended\_data\_interval

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.get_project_recommended_data_interval(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.project_data_interval_response.ProjectDataIntervalResponse
```

Get the interval (in ms) of the training data

Get the interval of the training data; if multiple intervals are present, the interval of the longest data item is returned. This only takes data in your *training* set into account.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                             |
| ----------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.project_data_interval_response.ProjectDataIntervalResponse` |

#### get\_project\_training\_data\_summary

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.get_project_training_data_summary(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	include_disabled: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Whether to include disabled samples. Defaults to true')] = None,
	include_not_processed: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Whether to include non-processed samples. Defaults to true')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.project_training_data_summary_response.ProjectTrainingDataSummaryResponse
```

Get data summary

Get summary of all data present in the training set. This returns the number of data items, the total length of all data, and the labels. This is similar to `dataSummary` in `ProjectInfoResponse` but allows you to exclude disabled items or items that are still processing.

| Parameters              |                                                                                                                                                                                           |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                                                                                                       |
| `project_id`            | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                            |
| `include_disabled`      | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Whether to include disabled samples. Defaults to true')] = None`      |
| `include_not_processed` | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Whether to include non-processed samples. Defaults to true')] = None` |
| `**kwargs`              | ` `                                                                                                                                                                                       |

| Returns                                                                                            |
| -------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.project_training_data_summary_response.ProjectTrainingDataSummaryResponse` |

#### get\_socket\_token

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.get_socket_token(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.socket_token_response.SocketTokenResponse
```

Get socket token

Get a token to authenticate with the web socket interface.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.socket_token_response.SocketTokenResponse` |

#### get\_synthetic\_data\_config

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.get_synthetic_data_config(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.get_synthetic_data_config_response.GetSyntheticDataConfigResponse
```

Get synthetic data config

Get the last used synthetic data config

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                                    |
| ------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.get_synthetic_data_config_response.GetSyntheticDataConfigResponse` |

#### get\_target\_constraints

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.get_target_constraints(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.get_target_constraints_response.GetTargetConstraintsResponse
```

Get target constraints

Retrieve target constraints for a project. The constraints object captures hardware attributes of your target device, along with an application budget to allow guidance on performance and resource usage

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                               |
| ------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_target_constraints_response.GetTargetConstraintsResponse` |

#### launch\_getting\_started\_wizard

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.launch_getting_started_wizard(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Launch getting started wizard

This clears out *all data in your project*, and is irrevocable. This function is only available through a JWT token, and is not available to all users.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### list\_ai\_actions

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.list_ai_actions(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.list_ai_actions_response.ListAIActionsResponse
```

List AI Actions

Get all AI actions.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                 |
| ----------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_ai_actions_response.ListAIActionsResponse` |

#### list\_development\_boards

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.list_development_boards(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.development_boards_response.DevelopmentBoardsResponse
```

Development boards

List all development boards for a project

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                        |
| ------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.development_boards_response.DevelopmentBoardsResponse` |

#### list\_devkeys

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.list_devkeys(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.development_keys_response.DevelopmentKeysResponse
```

Get development keys

Retrieve the development API and HMAC keys for a project. These keys are specifically marked to be used during development. These keys can be `undefined` if no development keys are set. Only available through JWT token authentication, if you authenticate with an API key then all keys will return undefined (this is changed behavior since 28 January 2026).

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                    |
| -------------------------------------------------------------------------- |
| `edgeimpulse_api.models.development_keys_response.DevelopmentKeysResponse` |

#### list\_downloads

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.list_downloads(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.project_downloads_response.ProjectDownloadsResponse
```

Get downloads

Retrieve the downloads for a project.

| Parameters   |                                                                                                                                                                                              |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                          |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                               |
| `impulse_id` | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                          |

| Returns                                                                      |
| ---------------------------------------------------------------------------- |
| `edgeimpulse_api.models.project_downloads_response.ProjectDownloadsResponse` |

#### list\_emails

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.list_emails(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.list_email_response.ListEmailResponse
```

List emails

Get a list of all emails sent by Edge Impulse regarding this project.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                        |
| -------------------------------------------------------------- |
| `edgeimpulse_api.models.list_email_response.ListEmailResponse` |

#### list\_project\_api\_keys

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.list_project_api_keys(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.list_api_keys_response.ListApiKeysResponse
```

Get API keys

Retrieve all API keys. This does **not** return the full API key, but only a portion (for security purposes). The development key will be returned in full, as it'll be set in devices and is thus not private.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                             |
| ------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_api_keys_response.ListApiKeysResponse` |

#### list\_project\_hmac\_keys

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.list_project_hmac_keys(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.list_hmac_keys_response.ListHmacKeysResponse
```

Get HMAC keys

Retrieve all HMAC keys.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                               |
| --------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_hmac_keys_response.ListHmacKeysResponse` |

#### list\_projects

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.list_projects(
	self,
	**kwargs
) ‑> edgeimpulse_api.models.list_projects_response.ListProjectsResponse
```

List active projects

Retrieve list of active projects. If authenticating using JWT token this lists all the projects the user has access to, if authenticating using an API key, this only lists that project.

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |
| `**kwargs` | ` ` |

| Returns                                                              |
| -------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_projects_response.ListProjectsResponse` |

#### list\_public\_project\_types

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.list_public_project_types(
	self,
	**kwargs
) ‑> edgeimpulse_api.models.list_public_project_types_response.ListPublicProjectTypesResponse
```

List public project types

Retrieve the list of available public project types. You don't need any authentication for this method.

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |
| `**kwargs` | ` ` |

| Returns                                                                                    |
| ------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.list_public_project_types_response.ListPublicProjectTypesResponse` |

#### list\_public\_projects

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.list_public_projects(
	self,
	limit: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None,
	offset: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None,
	project: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include projects where the name or owner contains this string')] = None,
	project_types: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description="Comma separated list of project types to filter on. Supported values are 'audio', 'object-detection', 'image', 'accelerometer', 'other'.")] = None,
	sort: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Fields and order to sort query by')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.list_public_projects_response.ListPublicProjectsResponse
```

List public projects

Retrieve the list of all public projects. You don't need any authentication for this method.

| Parameters      |                                                                                                                                                                                                                                                                        |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`          | ` `                                                                                                                                                                                                                                                                    |
| `limit`         | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None`                                                                                                                |
| `offset`        | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None`                                            |
| `project`       | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include projects where the name or owner contains this string')] = None`                                                                       |
| `project_types` | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description="Comma separated list of project types to filter on. Supported values are 'audio', 'object-detection', 'image', 'accelerometer', 'other'.")] = None` |
| `sort`          | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Fields and order to sort query by')] = None`                                                                                                        |
| `**kwargs`      | ` `                                                                                                                                                                                                                                                                    |

| Returns                                                                           |
| --------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_public_projects_response.ListPublicProjectsResponse` |

#### list\_public\_versions

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.list_public_versions(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.list_public_versions_response.ListPublicVersionsResponse
```

List public versions

Get all public versions for this project. You don't need any authentication for this function.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                           |
| --------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_public_versions_response.ListPublicVersionsResponse` |

#### list\_versions

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.list_versions(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.list_versions_response.ListVersionsResponse
```

List versions

Get all versions for this project.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                              |
| -------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_versions_response.ListVersionsResponse` |

#### make\_version\_private

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.make_version_private(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	version_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Version ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Make version private

Make a public version private.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `version_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Version ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### preview\_ai\_actions\_samples

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.preview_ai_actions_samples(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	action_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='AI Action ID')],
	preview_ai_actions_samples_request: edgeimpulse_api.models.preview_ai_actions_samples_request.PreviewAIActionsSamplesRequest,
	**kwargs
) ‑> edgeimpulse_api.models.list_samples_response.ListSamplesResponse
```

Preview samples for AI Actions

Get a number of random samples to show in the AI Actions screen. If `saveConfig` is passed in, then a valid actionId is required in the URL. If you don't need to save the config (e.g. when creating a new action), you can use -1.

| Parameters                           |                                                                                                                  |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| `self`                               | ` `                                                                                                              |
| `project_id`                         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`   |
| `action_id`                          | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='AI Action ID')]` |
| `preview_ai_actions_samples_request` | `edgeimpulse_api.models.preview_ai_actions_samples_request.PreviewAIActionsSamplesRequest`                       |
| `**kwargs`                           | ` `                                                                                                              |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.list_samples_response.ListSamplesResponse` |

#### project\_dismiss\_notification

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.project_dismiss_notification(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	project_dismiss_notification_request: edgeimpulse_api.models.project_dismiss_notification_request.ProjectDismissNotificationRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Dismiss a notification

Dismiss a notification

| Parameters                             |                                                                                                                |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                                 | ` `                                                                                                            |
| `project_id`                           | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `project_dismiss_notification_request` | `edgeimpulse_api.models.project_dismiss_notification_request.ProjectDismissNotificationRequest`                |
| `**kwargs`                             | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### remove\_collaborator

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.remove_collaborator(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	remove_collaborator_request: edgeimpulse_api.models.remove_collaborator_request.RemoveCollaboratorRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Remove collaborator

Remove a collaborator to a project. Note that you cannot invoke this function if only a single collaborator is present.

| Parameters                    |                                                                                                                |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                        | ` `                                                                                                            |
| `project_id`                  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `remove_collaborator_request` | `edgeimpulse_api.models.remove_collaborator_request.RemoveCollaboratorRequest`                                 |
| `**kwargs`                    | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### revoke\_project\_api\_key

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.revoke_project_api_key(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	api_key_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='API key ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Revoke API key

Revoke an API key. Note that if you revoke the development API key some services (such as automatic provisioning of devices through the serial daemon) will no longer work.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `api_key_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='API key ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### revoke\_project\_hmac\_key

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.revoke_project_hmac_key(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	hmac_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Hmac key ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Remove HMAC key

Revoke an HMAC key. Note that if you revoke the development key some services (such as automatic provisioning of devices through the serial daemon) will no longer work.

| Parameters   |                                                                                                                 |
| ------------ | --------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                             |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`  |
| `hmac_id`    | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Hmac key ID')]` |
| `**kwargs`   | ` `                                                                                                             |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### set\_ai\_actions\_order

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.set_ai_actions_order(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	set_ai_actions_order_request: edgeimpulse_api.models.set_ai_actions_order_request.SetAIActionsOrderRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Set AI Actions order

Change the order of AI actions. Post the new order of all AI Actions by ID. You need to specify *all* AI Actions here. If not, an error will be thrown.

| Parameters                     |                                                                                                                |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`                         | ` `                                                                                                            |
| `project_id`                   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `set_ai_actions_order_request` | `edgeimpulse_api.models.set_ai_actions_order_request.SetAIActionsOrderRequest`                                 |
| `**kwargs`                     | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### set\_project\_compute\_time\_limit

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.set_project_compute_time_limit(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	set_project_compute_time_request: edgeimpulse_api.models.set_project_compute_time_request.SetProjectComputeTimeRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Set compute time limit

Change the job compute time limit for the project. This function is only available through a JWT token, and is not available to all users.

| Parameters                         |                                                                                                                |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                             | ` `                                                                                                            |
| `project_id`                       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `set_project_compute_time_request` | `edgeimpulse_api.models.set_project_compute_time_request.SetProjectComputeTimeRequest`                         |
| `**kwargs`                         | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### set\_project\_file\_size\_limit

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.set_project_file_size_limit(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	set_project_dsp_file_size_request: edgeimpulse_api.models.set_project_dsp_file_size_request.SetProjectDspFileSizeRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Set DSP file size limit

Change the DSP file size limit for the project. This function is only available through a JWT token, and is not available to all users.

| Parameters                          |                                                                                                                |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                              | ` `                                                                                                            |
| `project_id`                        | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `set_project_dsp_file_size_request` | `edgeimpulse_api.models.set_project_dsp_file_size_request.SetProjectDspFileSizeRequest`                        |
| `**kwargs`                          | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### set\_target\_constraints

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.set_target_constraints(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	target_constraints: edgeimpulse_api.models.target_constraints.TargetConstraints,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Set target constraints

Set target constraints for a project. Use the constraints object to capture hardware attributes of your target device, along with an application budget to allow guidance on performance and resource usage

| Parameters           |                                                                                                                |
| -------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`               | ` `                                                                                                            |
| `project_id`         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `target_constraints` | `edgeimpulse_api.models.target_constraints.TargetConstraints`                                                  |
| `**kwargs`           | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### transfer\_ownership

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.transfer_ownership(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	add_collaborator_request: edgeimpulse_api.models.add_collaborator_request.AddCollaboratorRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Transfer ownership (user)

Transfer ownership of a project to another user.

| Parameters                 |                                                                                                                |
| -------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                     | ` `                                                                                                            |
| `project_id`               | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `add_collaborator_request` | `edgeimpulse_api.models.add_collaborator_request.AddCollaboratorRequest`                                       |
| `**kwargs`                 | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### transfer\_ownership\_organization

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.transfer_ownership_organization(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	transfer_ownership_organization_request: edgeimpulse_api.models.transfer_ownership_organization_request.TransferOwnershipOrganizationRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Transfer ownership (organization)

Transfer ownership of a project to another organization.

| Parameters                                |                                                                                                                |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                                    | ` `                                                                                                            |
| `project_id`                              | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `transfer_ownership_organization_request` | `edgeimpulse_api.models.transfer_ownership_organization_request.TransferOwnershipOrganizationRequest`          |
| `**kwargs`                                | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### update\_ai\_action

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.update_ai_action(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	action_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='AI Action ID')],
	update_ai_action_request: edgeimpulse_api.models.update_ai_action_request.UpdateAIActionRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Save AI Actions config

Store an AI Actions config. Use `createAIActionsJob` to run the job. Post the full AI Action here w/ all parameters.

| Parameters                 |                                                                                                                  |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `self`                     | ` `                                                                                                              |
| `project_id`               | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`   |
| `action_id`                | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='AI Action ID')]` |
| `update_ai_action_request` | `edgeimpulse_api.models.update_ai_action_request.UpdateAIActionRequest`                                          |
| `**kwargs`                 | ` `                                                                                                              |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### update\_project

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.update_project(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	update_project_request: edgeimpulse_api.models.update_project_request.UpdateProjectRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Update project

Update project properties such as name and logo.

| Parameters               |                                                                                                                |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`                   | ` `                                                                                                            |
| `project_id`             | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `update_project_request` | `edgeimpulse_api.models.update_project_request.UpdateProjectRequest`                                           |
| `**kwargs`               | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### update\_project\_tags

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.update_project_tags(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	update_project_tags_request: edgeimpulse_api.models.update_project_tags_request.UpdateProjectTagsRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Update tags

Update the list of project tags.

| Parameters                    |                                                                                                                |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                        | ` `                                                                                                            |
| `project_id`                  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `update_project_tags_request` | `edgeimpulse_api.models.update_project_tags_request.UpdateProjectTagsRequest`                                  |
| `**kwargs`                    | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### update\_version

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.update_version(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	version_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Version ID')],
	update_version_request: edgeimpulse_api.models.update_version_request.UpdateVersionRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Update version

Updates a version, this only updates fields that were set in the body.

| Parameters               |                                                                                                                |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`                   | ` `                                                                                                            |
| `project_id`             | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `version_id`             | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Version ID')]` |
| `update_version_request` | `edgeimpulse_api.models.update_version_request.UpdateVersionRequest`                                           |
| `**kwargs`               | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### upload\_csv\_wizard\_uploaded\_file

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.upload_csv_wizard_uploaded_file(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	file: Annotated[str, Strict(strict=True)],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Store CSV Wizard uploaded file

Asynchronously called in the CSV Wizard to store the file that the CSV wizard was based on.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `file`       | `Annotated[str, Strict(strict=True)]`                                                                          |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### upload\_readme\_image

```python  theme={"system"}
edgeimpulse_api.api.projects_api.ProjectsApi.upload_readme_image(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	image: Annotated[str, Strict(strict=True)],
	**kwargs
) ‑> edgeimpulse_api.models.upload_readme_image_response.UploadReadmeImageResponse
```

Upload image for readme

Uploads an image to the user CDN and returns the path.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `image`      | `Annotated[str, Strict(strict=True)]`                                                                          |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                         |
| ------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.upload_readme_image_response.UploadReadmeImageResponse` |


Built with [Mintlify](https://mintlify.com).