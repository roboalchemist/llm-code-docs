# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/project_info_response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.project_info_response

## Classes

### ProjectInfoResponse

```python  theme={"system"}
edgeimpulse_api.models.project_info_response.ProjectInfoResponse(
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

| Class variables                         |                                                                                                                                    |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `Config`                                | ` `                                                                                                                                |
| `acquisition_settings`                  | `edgeimpulse_api.models.project_info_response_all_of_acquisition_settings.ProjectInfoResponseAllOfAcquisitionSettings`             |
| `collaborators`                         | `List[edgeimpulse_api.models.user.User]`                                                                                           |
| `compute_time`                          | `edgeimpulse_api.models.project_info_response_all_of_compute_time.ProjectInfoResponseAllOfComputeTime`                             |
| `csv_import_config`                     | `Dict[str, Any] \| None`                                                                                                           |
| `data_summary`                          | `edgeimpulse_api.models.project_data_summary.ProjectDataSummary`                                                                   |
| `data_summary_per_category`             | `edgeimpulse_api.models.project_info_response_all_of_data_summary_per_category.ProjectInfoResponseAllOfDataSummaryPerCategory`     |
| `default_impulse_id`                    | `pydantic.v1.types.StrictInt \| None`                                                                                              |
| `deploy_settings`                       | `edgeimpulse_api.models.project_info_response_all_of_deploy_settings.ProjectInfoResponseAllOfDeploySettings`                       |
| `development_keys`                      | `edgeimpulse_api.models.development_keys.DevelopmentKeys`                                                                          |
| `devices`                               | `List[edgeimpulse_api.models.device.Device]`                                                                                       |
| `dsp_job_notification_uids`             | `List[pydantic.v1.types.StrictInt]`                                                                                                |
| `dsp_page_size`                         | `pydantic.v1.types.StrictInt \| None`                                                                                              |
| `error`                                 | `pydantic.v1.types.StrictStr \| None`                                                                                              |
| `experiments`                           | `List[edgeimpulse_api.models.project_info_response_all_of_experiments.ProjectInfoResponseAllOfExperiments]`                        |
| `export_job_notification_uids`          | `List[pydantic.v1.types.StrictInt]`                                                                                                |
| `has_new_training_data`                 | `pydantic.v1.types.StrictBool`                                                                                                     |
| `impulse`                               | `edgeimpulse_api.models.project_info_response_all_of_impulse.ProjectInfoResponseAllOfImpulse`                                      |
| `in_pretrained_model_flow`              | `pydantic.v1.types.StrictBool`                                                                                                     |
| `last_shown_model_engine`               | `edgeimpulse_api.models.model_engine_short_enum.ModelEngineShortEnum \| None`                                                      |
| `latency_devices`                       | `List[edgeimpulse_api.models.latency_device.LatencyDevice]`                                                                        |
| `model_testing_job_notification_uids`   | `List[pydantic.v1.types.StrictInt]`                                                                                                |
| `notifications`                         | `List[pydantic.v1.types.StrictStr]`                                                                                                |
| `performance`                           | `edgeimpulse_api.models.project_info_response_all_of_performance.ProjectInfoResponseAllOfPerformance`                              |
| `project`                               | `edgeimpulse_api.models.project.Project`                                                                                           |
| `readme`                                | `edgeimpulse_api.models.project_info_response_all_of_readme.ProjectInfoResponseAllOfReadme \| None`                                |
| `show_create_first_impulse`             | `pydantic.v1.types.StrictBool`                                                                                                     |
| `show_getting_started_wizard`           | `edgeimpulse_api.models.project_info_response_all_of_show_getting_started_wizard.ProjectInfoResponseAllOfShowGettingStartedWizard` |
| `show_sensor_data_in_acquisition_graph` | `pydantic.v1.types.StrictBool`                                                                                                     |
| `studio_url`                            | `pydantic.v1.types.StrictStr`                                                                                                      |
| `success`                               | `pydantic.v1.types.StrictBool`                                                                                                     |
| `target_constraints`                    | `edgeimpulse_api.models.target_constraints.TargetConstraints \| None`                                                              |
| `train_job_notification_uids`           | `List[pydantic.v1.types.StrictInt]`                                                                                                |
| `urls`                                  | `edgeimpulse_api.models.project_info_response_all_of_urls.ProjectInfoResponseAllOfUrls`                                            |
| `versioning_storage_size_mib`           | `pydantic.v1.types.StrictInt \| None`                                                                                              |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.project_info_response.ProjectInfoResponse.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.project_info_response.ProjectInfoResponse
```

Create an instance of ProjectInfoResponse from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.project_info_response.ProjectInfoResponse` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.project_info_response.ProjectInfoResponse.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.project_info_response.ProjectInfoResponse
```

Create an instance of ProjectInfoResponse from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.project_info_response.ProjectInfoResponse` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.project_info_response.ProjectInfoResponse.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.project_info_response.ProjectInfoResponse.to_json(
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
edgeimpulse_api.models.project_info_response.ProjectInfoResponse.to_str(
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