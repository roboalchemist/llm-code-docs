# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/performance_calibration_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api.performance_calibration_api

## Classes

### PerformanceCalibrationApi

```python  theme={"system"}
edgeimpulse_api.api.performance_calibration_api.PerformanceCalibrationApi(
	api_client=None
)
```

| Parameters        |     |
| ----------------- | --- |
| `api_client=None` | ` ` |

***

**METHODS**

#### clear\_performance\_calibration\_state

```python  theme={"system"}
edgeimpulse_api.api.performance_calibration_api.PerformanceCalibrationApi.clear_performance_calibration_state(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	impulse_id: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Clear Performance Calibration state

Deletes all state related to performance calibration (used in tests for example).

| Parameters   |                                                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                   |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                             |
| `impulse_id` | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                   |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### delete\_performance\_calibration\_saved\_parameters

```python  theme={"system"}
edgeimpulse_api.api.performance_calibration_api.PerformanceCalibrationApi.delete_performance_calibration_saved_parameters(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	impulse_id: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Clear performance calibration parameters

Clears the current performance calibration parameters

| Parameters   |                                                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                   |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                             |
| `impulse_id` | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                   |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### get\_performance\_calibration\_ground\_truth

```python  theme={"system"}
edgeimpulse_api.api.performance_calibration_api.PerformanceCalibrationApi.get_performance_calibration_ground_truth(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	impulse_id: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None,
	**kwargs
) ‑> edgeimpulse_api.models.get_performance_calibration_ground_truth_response.GetPerformanceCalibrationGroundTruthResponse
```

Get ground truth

Get performance calibration ground truth data

| Parameters   |                                                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                   |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                             |
| `impulse_id` | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                   |

| Returns                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_performance_calibration_ground_truth_response.GetPerformanceCalibrationGroundTruthResponse` |

#### get\_performance\_calibration\_parameter\_sets

```python  theme={"system"}
edgeimpulse_api.api.performance_calibration_api.PerformanceCalibrationApi.get_performance_calibration_parameter_sets(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	impulse_id: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None,
	**kwargs
) ‑> edgeimpulse_api.models.get_performance_calibration_parameter_sets_response.GetPerformanceCalibrationParameterSetsResponse
```

Get parameter sets

Get performance calibration parameter sets

| Parameters   |                                                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                   |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                             |
| `impulse_id` | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                   |

| Returns                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_performance_calibration_parameter_sets_response.GetPerformanceCalibrationParameterSetsResponse` |

#### get\_performance\_calibration\_raw\_result

```python  theme={"system"}
edgeimpulse_api.api.performance_calibration_api.PerformanceCalibrationApi.get_performance_calibration_raw_result(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	impulse_id: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None,
	**kwargs
) ‑> edgeimpulse_api.models.get_performance_calibration_raw_result_response.GetPerformanceCalibrationRawResultResponse
```

Get raw result

Get performance calibration raw result

| Parameters   |                                                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                   |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                             |
| `impulse_id` | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                   |

| Returns                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_performance_calibration_raw_result_response.GetPerformanceCalibrationRawResultResponse` |

#### get\_performance\_calibration\_saved\_parameters

```python  theme={"system"}
edgeimpulse_api.api.performance_calibration_api.PerformanceCalibrationApi.get_performance_calibration_saved_parameters(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	impulse_id: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None,
	**kwargs
) ‑> edgeimpulse_api.models.get_performance_calibration_parameters_response.GetPerformanceCalibrationParametersResponse
```

Get parameters

Get performance calibration stored parameters

| Parameters   |                                                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                   |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                             |
| `impulse_id` | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                   |

| Returns                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_performance_calibration_parameters_response.GetPerformanceCalibrationParametersResponse` |

#### get\_performance\_calibration\_status

```python  theme={"system"}
edgeimpulse_api.api.performance_calibration_api.PerformanceCalibrationApi.get_performance_calibration_status(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	impulse_id: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None,
	**kwargs
) ‑> edgeimpulse_api.models.get_performance_calibration_status_response.GetPerformanceCalibrationStatusResponse
```

Get status

Get performance calibration status

| Parameters   |                                                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                   |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                             |
| `impulse_id` | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                   |

| Returns                                                                                                      |
| ------------------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.get_performance_calibration_status_response.GetPerformanceCalibrationStatusResponse` |

#### get\_wav\_file

```python  theme={"system"}
edgeimpulse_api.api.performance_calibration_api.PerformanceCalibrationApi.get_wav_file(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	impulse_id: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None,
	**kwargs
) ‑> str
```

Get WAV file

Get the synthetic sample as a WAV file

| Parameters   |                                                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                   |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                             |
| `impulse_id` | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                   |

| Returns |
| ------- |
| `str`   |

#### set\_performance\_calibration\_saved\_parameters

```python  theme={"system"}
edgeimpulse_api.api.performance_calibration_api.PerformanceCalibrationApi.set_performance_calibration_saved_parameters(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	performance_calibration_save_parameter_set_request: edgeimpulse_api.models.performance_calibration_save_parameter_set_request.PerformanceCalibrationSaveParameterSetRequest,
	impulse_id: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Save performance calibration parameters

Set the current performance calibration parameters

| Parameters                                           |                                                                                                                                                                                       |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                                               | ` `                                                                                                                                                                                   |
| `project_id`                                         | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                             |
| `performance_calibration_save_parameter_set_request` | `edgeimpulse_api.models.performance_calibration_save_parameter_set_request.PerformanceCalibrationSaveParameterSetRequest`                                                             |
| `impulse_id`                                         | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None` |
| `**kwargs`                                           | ` `                                                                                                                                                                                   |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### upload\_labeled\_audio

```python  theme={"system"}
edgeimpulse_api.api.performance_calibration_api.PerformanceCalibrationApi.upload_labeled_audio(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	zip: pydantic.v1.types.StrictStr,
	impulse_id: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None,
	**kwargs
) ‑> edgeimpulse_api.models.performance_calibration_upload_labeled_audio_response.PerformanceCalibrationUploadLabeledAudioResponse
```

Upload Performance Calibration Audio files

Upload a zip files with a wav file and its Label metadata to run performance calibration on it.

| Parameters   |                                                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                   |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                             |
| `zip`        | `pydantic.v1.types.StrictStr`                                                                                                                                                         |
| `impulse_id` | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                   |

| Returns                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.performance_calibration_upload_labeled_audio_response.PerformanceCalibrationUploadLabeledAudioResponse` |


Built with [Mintlify](https://mintlify.com).