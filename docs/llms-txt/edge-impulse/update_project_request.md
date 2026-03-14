# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/update_project_request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.update_project_request

## Classes

### UpdateProjectRequest

```python  theme={"system"}
edgeimpulse_api.models.update_project_request.UpdateProjectRequest(
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

| Class variables                                 |                                                                                       |
| ----------------------------------------------- | ------------------------------------------------------------------------------------- |
| `Config`                                        | ` `                                                                                   |
| `ai_actions_grid_column_count`                  | `pydantic.v1.types.StrictInt \| None`                                                 |
| `compute_time_limit_m`                          | `pydantic.v1.types.StrictInt \| None`                                                 |
| `csv_import_config`                             | `Dict[str, Any] \| None`                                                              |
| `data_acquisition_grid_column_count`            | `pydantic.v1.types.StrictInt \| None`                                                 |
| `data_acquisition_grid_column_count_detailed`   | `pydantic.v1.types.StrictInt \| None`                                                 |
| `data_acquisition_page_size`                    | `pydantic.v1.types.StrictInt \| None`                                                 |
| `data_acquisition_view_type`                    | `pydantic.v1.types.StrictStr \| None`                                                 |
| `default_profiling_variant`                     | `edgeimpulse_api.models.keras_model_variant_enum.KerasModelVariantEnum \| None`       |
| `description`                                   | `pydantic.v1.types.StrictStr \| None`                                                 |
| `dsp_file_size_mb`                              | `pydantic.v1.types.StrictInt \| None`                                                 |
| `dsp_job_notification_uids`                     | `List[pydantic.v1.types.StrictInt] \| None`                                           |
| `dsp_page_size`                                 | `pydantic.v1.types.StrictInt \| None`                                                 |
| `enabled_model_profiling_variants`              | `List[edgeimpulse_api.models.keras_model_variant_enum.KerasModelVariantEnum] \| None` |
| `enterprise_performance`                        | `pydantic.v1.types.StrictBool \| None`                                                |
| `experiments`                                   | `List[pydantic.v1.types.StrictStr] \| None`                                           |
| `export_job_notification_uids`                  | `List[pydantic.v1.types.StrictInt] \| None`                                           |
| `getting_started_classes`                       | `List[pydantic.v1.types.StrictStr] \| None`                                           |
| `getting_started_step`                          | `pydantic.v1.types.StrictInt \| None`                                                 |
| `getting_started_tutorial`                      | `edgeimpulse_api.models.tutorial_type.TutorialType \| None`                           |
| `impulse_list_additional_metrics_shown_columns` | `List[pydantic.v1.types.StrictStr] \| None`                                           |
| `impulse_list_core_metrics_hidden_columns`      | `List[pydantic.v1.types.StrictStr] \| None`                                           |
| `impulse_list_extra_columns`                    | `List[pydantic.v1.types.StrictStr] \| None`                                           |
| `in_pretrained_model_flow`                      | `pydantic.v1.types.StrictBool \| None`                                                |
| `ind_pause_processing_samples`                  | `pydantic.v1.types.StrictBool \| None`                                                |
| `inline_edit_bounding_boxes`                    | `pydantic.v1.types.StrictBool \| None`                                                |
| `labeling_method`                               | `edgeimpulse_api.models.project_labeling_method.ProjectLabelingMethod \| None`        |
| `last_acquisition_label`                        | `pydantic.v1.types.StrictStr \| None`                                                 |
| `last_deploy_eon_compiler`                      | `pydantic.v1.types.StrictBool \| None`                                                |
| `last_deploy_model_engine`                      | `pydantic.v1.types.StrictStr \| None`                                                 |
| `last_deployment_target`                        | `pydantic.v1.types.StrictStr \| None`                                                 |
| `last_shown_model_engine`                       | `edgeimpulse_api.models.model_engine_short_enum.ModelEngineShortEnum \| None`         |
| `latency_device`                                | `pydantic.v1.types.StrictStr \| None`                                                 |
| `logo`                                          | `pydantic.v1.types.StrictStr \| None`                                                 |
| `metadata`                                      | `Dict[str, Any] \| None`                                                              |
| `model_testing_job_notification_uids`           | `List[pydantic.v1.types.StrictInt] \| None`                                           |
| `name`                                          | `pydantic.v1.types.StrictStr \| None`                                                 |
| `project_visibility`                            | `edgeimpulse_api.models.project_visibility.ProjectVisibility \| None`                 |
| `public_project_listed`                         | `pydantic.v1.types.StrictBool \| None`                                                |
| `readme`                                        | `pydantic.v1.types.StrictStr \| None`                                                 |
| `selected_project_type_in_wizard`               | `pydantic.v1.types.StrictStr \| None`                                                 |
| `show_create_first_impulse`                     | `pydantic.v1.types.StrictBool \| None`                                                |
| `show_exact_sample_length`                      | `pydantic.v1.types.StrictBool \| None`                                                |
| `show_sensor_data_in_acquisition_graph`         | `pydantic.v1.types.StrictBool \| None`                                                |
| `train_job_notification_uids`                   | `List[pydantic.v1.types.StrictInt] \| None`                                           |
| `train_job_ram_mb`                              | `pydantic.v1.types.StrictInt \| None`                                                 |
| `use_gpu`                                       | `pydantic.v1.types.StrictBool \| None`                                                |
| `versioning_storage_size_mib`                   | `pydantic.v1.types.StrictInt \| None`                                                 |

***

**STATIC METHODS**

#### data\_acquisition\_view\_type\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.update_project_request.UpdateProjectRequest.data_acquisition_view_type_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.update_project_request.UpdateProjectRequest.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.update_project_request.UpdateProjectRequest
```

Create an instance of UpdateProjectRequest from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                              |
| -------------------------------------------------------------------- |
| `edgeimpulse_api.models.update_project_request.UpdateProjectRequest` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.update_project_request.UpdateProjectRequest.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.update_project_request.UpdateProjectRequest
```

Create an instance of UpdateProjectRequest from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                              |
| -------------------------------------------------------------------- |
| `edgeimpulse_api.models.update_project_request.UpdateProjectRequest` |

#### selected\_project\_type\_in\_wizard\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.update_project_request.UpdateProjectRequest.selected_project_type_in_wizard_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.update_project_request.UpdateProjectRequest.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.update_project_request.UpdateProjectRequest.to_json(
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
edgeimpulse_api.models.update_project_request.UpdateProjectRequest.to_str(
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