# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/impulse_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api.impulse_api

## Classes

### ImpulseApi

```python  theme={"system"}
edgeimpulse_api.api.impulse_api.ImpulseApi(
	api_client=None
)
```

| Parameters        |     |
| ----------------- | --- |
| `api_client=None` | ` ` |

***

**METHODS**

#### clone\_impulse\_complete

```python  theme={"system"}
edgeimpulse_api.api.impulse_api.ImpulseApi.clone_impulse_complete(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	impulse_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Impulse ID', extra={})],
	clone_impulse_request: edgeimpulse_api.models.clone_impulse_request.CloneImpulseRequest,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Clone impulse (complete)

Clones the complete impulse (incl. config and data) of an existing impulse.

| Parameters              |                                                                                                           |
| ----------------------- | --------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                       |
| `project_id`            | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `impulse_id`            | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Impulse ID', extra={})]` |
| `clone_impulse_request` | `edgeimpulse_api.models.clone_impulse_request.CloneImpulseRequest`                                        |
| `**kwargs`              | ` `                                                                                                       |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### clone\_impulse\_structure

```python  theme={"system"}
edgeimpulse_api.api.impulse_api.ImpulseApi.clone_impulse_structure(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	impulse_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Impulse ID', extra={})],
	clone_impulse_request: edgeimpulse_api.models.clone_impulse_request.CloneImpulseRequest,
	**kwargs
) ‑> edgeimpulse_api.models.create_impulse_response.CreateImpulseResponse
```

Clone impulse (structure)

Clones the complete structure (incl. config) of an impulse. Does not copy data.

| Parameters              |                                                                                                           |
| ----------------------- | --------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                       |
| `project_id`            | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `impulse_id`            | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Impulse ID', extra={})]` |
| `clone_impulse_request` | `edgeimpulse_api.models.clone_impulse_request.CloneImpulseRequest`                                        |
| `**kwargs`              | ` `                                                                                                       |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.create_impulse_response.CreateImpulseResponse` |

#### create\_impulse

```python  theme={"system"}
edgeimpulse_api.api.impulse_api.ImpulseApi.create_impulse(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	impulse: edgeimpulse_api.models.create_impulse_request.CreateImpulseRequest,
	impulse_id: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None,
	**kwargs
) ‑> edgeimpulse_api.models.create_impulse_response.CreateImpulseResponse
```

Create impulse

Sets the impulse for this project.  If you specify `impulseId` then that impulse is created/updated, otherwise the default impulse is created/updated.

| Parameters   |                                                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                   |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                             |
| `impulse`    | `edgeimpulse_api.models.create_impulse_request.CreateImpulseRequest`                                                                                                                  |
| `impulse_id` | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                   |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.create_impulse_response.CreateImpulseResponse` |

#### create\_new\_empty\_impulse

```python  theme={"system"}
edgeimpulse_api.api.impulse_api.ImpulseApi.create_new_empty_impulse(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	create_new_empty_impulse_request: edgeimpulse_api.models.create_new_empty_impulse_request.CreateNewEmptyImpulseRequest | None = None,
	**kwargs
) ‑> edgeimpulse_api.models.create_new_empty_impulse_response.CreateNewEmptyImpulseResponse
```

Create new empty impulse

Create a new empty impulse, and return the ID.

| Parameters                         |                                                                                                           |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `self`                             | ` `                                                                                                       |
| `project_id`                       | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `create_new_empty_impulse_request` | `edgeimpulse_api.models.create_new_empty_impulse_request.CreateNewEmptyImpulseRequest \| None = None`     |
| `**kwargs`                         | ` `                                                                                                       |

| Returns                                                                                  |
| ---------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.create_new_empty_impulse_response.CreateNewEmptyImpulseResponse` |

#### delete\_impulse

```python  theme={"system"}
edgeimpulse_api.api.impulse_api.ImpulseApi.delete_impulse(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	impulse_id: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Delete impulse

Clears the impulse and all associated blocks for this project.  If you specify `impulseId` then that impulse is cleared, otherwise the default impulse is cleared.

| Parameters   |                                                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                   |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                             |
| `impulse_id` | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                   |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### download\_detailed\_impulses

```python  theme={"system"}
edgeimpulse_api.api.impulse_api.ImpulseApi.download_detailed_impulses(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	format: Annotated[pydantic.v1.types.StrictStr | None, FieldInfo(default=PydanticUndefined, description="Format of the detailed impulses response, either 'json' or 'csv'. If not set, defaults to 'json'.", extra={})] = None,
	**kwargs
) ‑> str
```

Download all impulses (incl. metrics), as JSON or CSV.

Download all impulse for a project, including accuracy and performance metrics, as JSON or CSV.

| Parameters   |                                                                                                                                                                                                                          |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `self`       | ` `                                                                                                                                                                                                                      |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                                                                |
| `format`     | `Annotated[pydantic.v1.types.StrictStr \| None, FieldInfo(default=PydanticUndefined, description="Format of the detailed impulses response, either 'json' or 'csv'. If not set, defaults to 'json'.", extra={})] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                                                      |

| Returns |
| ------- |
| `str`   |

#### get\_all\_detailed\_impulses

```python  theme={"system"}
edgeimpulse_api.api.impulse_api.ImpulseApi.get_all_detailed_impulses(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	**kwargs
) ‑> edgeimpulse_api.models.get_all_detailed_impulses_response.GetAllDetailedImpulsesResponse
```

Get all impulses (incl. metrics)

Retrieve all impulse for a project, including accuracy and performance metrics.

| Parameters   |                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                       |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `**kwargs`   | ` `                                                                                                       |

| Returns                                                                                    |
| ------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.get_all_detailed_impulses_response.GetAllDetailedImpulsesResponse` |

#### get\_all\_impulses

```python  theme={"system"}
edgeimpulse_api.api.impulse_api.ImpulseApi.get_all_impulses(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	**kwargs
) ‑> edgeimpulse_api.models.get_all_impulses_response.GetAllImpulsesResponse
```

Get all impulses

Retrieve all impulse for a project

| Parameters   |                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                       |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `**kwargs`   | ` `                                                                                                       |

| Returns                                                                   |
| ------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_all_impulses_response.GetAllImpulsesResponse` |

#### get\_all\_transfer\_learning\_models

```python  theme={"system"}
edgeimpulse_api.api.impulse_api.ImpulseApi.get_all_transfer_learning_models(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	**kwargs
) ‑> edgeimpulse_api.models.get_all_transfer_learning_models_response.GetAllTransferLearningModelsResponse
```

Get all transfer learning models

Retrieve all transfer learning models across all categories

| Parameters   |                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                       |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `**kwargs`   | ` `                                                                                                       |

| Returns                                                                                                 |
| ------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_all_transfer_learning_models_response.GetAllTransferLearningModelsResponse` |

#### get\_impulse

```python  theme={"system"}
edgeimpulse_api.api.impulse_api.ImpulseApi.get_impulse(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	impulse_id: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None,
	**kwargs
) ‑> edgeimpulse_api.models.get_impulse_response.GetImpulseResponse
```

Get impulse

Retrieve the impulse for this project. If you specify `impulseId` then that impulse is returned, otherwise the default impulse is returned.

| Parameters   |                                                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                   |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                             |
| `impulse_id` | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                   |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.get_impulse_response.GetImpulseResponse` |

#### get\_impulse\_all

```python  theme={"system"}
edgeimpulse_api.api.impulse_api.ImpulseApi.get_impulse_all(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	impulse_id: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None,
	**kwargs
) ‑> edgeimpulse_api.models.get_impulse_response.GetImpulseResponse
```

Get impulse including disabled blocks

Retrieve the impulse for this project including disabled blocks. If you specify `impulseId` then that impulse is returned, otherwise the default impulse is returned.

| Parameters   |                                                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                   |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                             |
| `impulse_id` | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                   |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.get_impulse_response.GetImpulseResponse` |

#### get\_impulse\_blocks

```python  theme={"system"}
edgeimpulse_api.api.impulse_api.ImpulseApi.get_impulse_blocks(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	**kwargs
) ‑> edgeimpulse_api.models.get_impulse_blocks_response.GetImpulseBlocksResponse
```

Get impulse blocks

Lists all possible blocks that can be used in the impulse

| Parameters   |                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                       |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `**kwargs`   | ` `                                                                                                       |

| Returns                                                                       |
| ----------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_impulse_blocks_response.GetImpulseBlocksResponse` |

#### get\_new\_block\_id

```python  theme={"system"}
edgeimpulse_api.api.impulse_api.ImpulseApi.get_new_block_id(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	**kwargs
) ‑> edgeimpulse_api.models.get_new_block_id_response.GetNewBlockIdResponse
```

Get new block ID

Returns an unused block ID. Use this function to determine new block IDs when you construct an impulse; so you won't accidentally re-use block IDs.

| Parameters   |                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                       |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `**kwargs`   | ` `                                                                                                       |

| Returns                                                                  |
| ------------------------------------------------------------------------ |
| `edgeimpulse_api.models.get_new_block_id_response.GetNewBlockIdResponse` |

#### regenerate\_model\_testing\_summary

```python  theme={"system"}
edgeimpulse_api.api.impulse_api.ImpulseApi.regenerate_model_testing_summary(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	impulse_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Impulse ID', extra={})],
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Regenerate model testing summary

Regenerate model testing results (without re-running feature generation). Use this if thresholds changed (e.g. via setImpulseThresholds), but no job was kicked off automatically.

| Parameters   |                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                       |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `impulse_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Impulse ID', extra={})]` |
| `**kwargs`   | ` `                                                                                                       |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### set\_impulse\_thresholds

```python  theme={"system"}
edgeimpulse_api.api.impulse_api.ImpulseApi.set_impulse_thresholds(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	impulse_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Impulse ID', extra={})],
	set_impulse_thresholds_request: edgeimpulse_api.models.set_impulse_thresholds_request.SetImpulseThresholdsRequest,
	**kwargs
) ‑> edgeimpulse_api.models.set_impulse_thresholds_response.SetImpulseThresholdsResponse
```

Set thresholds

Set thresholds (e.g. min. confidence rating, or min. anomaly score) for an impulse.

| Parameters                       |                                                                                                           |
| -------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `self`                           | ` `                                                                                                       |
| `project_id`                     | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `impulse_id`                     | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Impulse ID', extra={})]` |
| `set_impulse_thresholds_request` | `edgeimpulse_api.models.set_impulse_thresholds_request.SetImpulseThresholdsRequest`                       |
| `**kwargs`                       | ` `                                                                                                       |

| Returns                                                                               |
| ------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.set_impulse_thresholds_response.SetImpulseThresholdsResponse` |

#### update\_impulse

```python  theme={"system"}
edgeimpulse_api.api.impulse_api.ImpulseApi.update_impulse(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	update_impulse_request: edgeimpulse_api.models.update_impulse_request.UpdateImpulseRequest,
	impulse_id: Annotated[pydantic.v1.types.StrictInt | None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Update impulse

Update the impulse for this project.  If you specify `impulseId` then that impulse is created/updated, otherwise the default impulse is created/updated.

| Parameters               |                                                                                                                                                                                       |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                   | ` `                                                                                                                                                                                   |
| `project_id`             | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                             |
| `update_impulse_request` | `edgeimpulse_api.models.update_impulse_request.UpdateImpulseRequest`                                                                                                                  |
| `impulse_id`             | `Annotated[pydantic.v1.types.StrictInt \| None, FieldInfo(default=PydanticUndefined, description='Impulse ID. If this is unset then the default impulse is used.', extra={})] = None` |
| `**kwargs`               | ` `                                                                                                                                                                                   |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### verify\_dsp\_block\_url

```python  theme={"system"}
edgeimpulse_api.api.impulse_api.ImpulseApi.verify_dsp_block_url(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	verify_dsp_block_url_request: edgeimpulse_api.models.verify_dsp_block_url_request.VerifyDspBlockUrlRequest,
	**kwargs
) ‑> edgeimpulse_api.models.verify_dsp_block_url_response.VerifyDspBlockUrlResponse
```

Verify custom DSP block

Verify the validity of a custom DSP block

| Parameters                     |                                                                                                           |
| ------------------------------ | --------------------------------------------------------------------------------------------------------- |
| `self`                         | ` `                                                                                                       |
| `project_id`                   | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `verify_dsp_block_url_request` | `edgeimpulse_api.models.verify_dsp_block_url_request.VerifyDspBlockUrlRequest`                            |
| `**kwargs`                     | ` `                                                                                                       |

| Returns                                                                          |
| -------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.verify_dsp_block_url_response.VerifyDspBlockUrlResponse` |


Built with [Mintlify](https://mintlify.com).