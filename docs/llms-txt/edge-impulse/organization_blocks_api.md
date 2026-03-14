# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/organization_blocks_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api.organization_blocks_api

## Classes

### OrganizationBlocksApi

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi(
	api_client=None
)
```

| Parameters        |     |
| ----------------- | --- |
| `api_client=None` | ` ` |

***

**METHODS**

#### add\_organization\_deploy\_block

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.add_organization_deploy_block(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	name: Annotated[str, Strict(strict=True)],
	docker_container: Annotated[str, Strict(strict=True)],
	description: Annotated[str, Strict(strict=True)],
	cli_arguments: Annotated[str, Strict(strict=True)],
	requests_cpu: float | None = None,
	requests_memory: Annotated[int, Strict(strict=True)] | None = None,
	limits_cpu: float | None = None,
	limits_memory: Annotated[int, Strict(strict=True)] | None = None,
	photo: Annotated[str, Strict(strict=True)] | None = None,
	integrate_url: Annotated[str, Strict(strict=True)] | None = None,
	privileged: Annotated[bool, Strict(strict=True)] | None = None,
	mount_learn_block: Annotated[bool, Strict(strict=True)] | None = None,
	supports_eon_compiler: Annotated[bool, Strict(strict=True)] | None = None,
	show_optimizations: Annotated[bool, Strict(strict=True)] | None = None,
	category: Annotated[str, Strict(strict=True)] | None = None,
	source_code_download_staff_only: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Whether the source code is only available for staff users.')] = None,
	parameters: Annotated[List[Dict[str, Any]] | None, FieldInfo(annotation=NoneType, required=True, description="List of parameters, spec'ed according to https://docs.edgeimpulse.com/docs/tips-and-tricks/adding-parameters-to-custom-blocks")] = None,
	**kwargs
) ‑> edgeimpulse_api.models.entity_created_response.EntityCreatedResponse
```

Add deploy block

Adds a deploy block.

| Parameters                        |                                                                                                                                                                                           |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                            | ` `                                                                                                                                                                                       |
| `organization_id`                 | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                       |
| `name`                            | `Annotated[str, Strict(strict=True)]`                                                                                                                                                     |
| `docker_container`                | `Annotated[str, Strict(strict=True)]`                                                                                                                                                     |
| `description`                     | `Annotated[str, Strict(strict=True)]`                                                                                                                                                     |
| `cli_arguments`                   | `Annotated[str, Strict(strict=True)]`                                                                                                                                                     |
| `requests_cpu`                    | `float \| None = None`                                                                                                                                                                    |
| `requests_memory`                 | `Annotated[int, Strict(strict=True)] \| None = None`                                                                                                                                      |
| `limits_cpu`                      | `float \| None = None`                                                                                                                                                                    |
| `limits_memory`                   | `Annotated[int, Strict(strict=True)] \| None = None`                                                                                                                                      |
| `photo`                           | `Annotated[str, Strict(strict=True)] \| None = None`                                                                                                                                      |
| `integrate_url`                   | `Annotated[str, Strict(strict=True)] \| None = None`                                                                                                                                      |
| `privileged`                      | `Annotated[bool, Strict(strict=True)] \| None = None`                                                                                                                                     |
| `mount_learn_block`               | `Annotated[bool, Strict(strict=True)] \| None = None`                                                                                                                                     |
| `supports_eon_compiler`           | `Annotated[bool, Strict(strict=True)] \| None = None`                                                                                                                                     |
| `show_optimizations`              | `Annotated[bool, Strict(strict=True)] \| None = None`                                                                                                                                     |
| `category`                        | `Annotated[str, Strict(strict=True)] \| None = None`                                                                                                                                      |
| `source_code_download_staff_only` | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Whether the source code is only available for staff users.')] = None` |
| `parameters`                      | `Annotated[List[Dict[str, Any]] \| None, FieldInfo(annotation=NoneType, required=True, description="List of parameters, spec'ed according to https`                                       |
| `**kwargs`                        | ` `                                                                                                                                                                                       |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.entity_created_response.EntityCreatedResponse` |

#### add\_organization\_dsp\_block

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.add_organization_dsp_block(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	add_organization_dsp_block_request: edgeimpulse_api.models.add_organization_dsp_block_request.AddOrganizationDspBlockRequest,
	**kwargs
) ‑> edgeimpulse_api.models.entity_created_response.EntityCreatedResponse
```

Add dsp block

Adds a dsp block.

| Parameters                           |                                                                                                                     |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| `self`                               | ` `                                                                                                                 |
| `organization_id`                    | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `add_organization_dsp_block_request` | `edgeimpulse_api.models.add_organization_dsp_block_request.AddOrganizationDspBlockRequest`                          |
| `**kwargs`                           | ` `                                                                                                                 |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.entity_created_response.EntityCreatedResponse` |

#### add\_organization\_secret

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.add_organization_secret(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	add_organization_secret_request: edgeimpulse_api.models.add_organization_secret_request.AddOrganizationSecretRequest,
	**kwargs
) ‑> edgeimpulse_api.models.entity_created_response.EntityCreatedResponse
```

Add secret

Adds a secret.

| Parameters                        |                                                                                                                     |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                            | ` `                                                                                                                 |
| `organization_id`                 | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `add_organization_secret_request` | `edgeimpulse_api.models.add_organization_secret_request.AddOrganizationSecretRequest`                               |
| `**kwargs`                        | ` `                                                                                                                 |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.entity_created_response.EntityCreatedResponse` |

#### add\_organization\_transfer\_learning\_block

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.add_organization_transfer_learning_block(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	add_organization_transfer_learning_block_request: edgeimpulse_api.models.add_organization_transfer_learning_block_request.AddOrganizationTransferLearningBlockRequest,
	**kwargs
) ‑> edgeimpulse_api.models.entity_created_response.EntityCreatedResponse
```

Add transfer learning block

Adds a transfer learning block.

| Parameters                                         |                                                                                                                       |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `self`                                             | ` `                                                                                                                   |
| `organization_id`                                  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`   |
| `add_organization_transfer_learning_block_request` | `edgeimpulse_api.models.add_organization_transfer_learning_block_request.AddOrganizationTransferLearningBlockRequest` |
| `**kwargs`                                         | ` `                                                                                                                   |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.entity_created_response.EntityCreatedResponse` |

#### add\_organization\_transformation\_block

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.add_organization_transformation_block(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	add_organization_transformation_block_request: edgeimpulse_api.models.add_organization_transformation_block_request.AddOrganizationTransformationBlockRequest,
	**kwargs
) ‑> edgeimpulse_api.models.entity_created_response.EntityCreatedResponse
```

Add transformation block

Adds a transformation block.

| Parameters                                      |                                                                                                                     |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                                          | ` `                                                                                                                 |
| `organization_id`                               | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `add_organization_transformation_block_request` | `edgeimpulse_api.models.add_organization_transformation_block_request.AddOrganizationTransformationBlockRequest`    |
| `**kwargs`                                      | ` `                                                                                                                 |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.entity_created_response.EntityCreatedResponse` |

#### delete\_organization\_deploy\_block

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.delete_organization_deploy_block(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	deploy_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Deploy block ID.')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Delete deploy block

Deletes a deploy block.

| Parameters        |                                                                                                                      |
| ----------------- | -------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                  |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`  |
| `deploy_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Deploy block ID.')]` |
| `**kwargs`        | ` `                                                                                                                  |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### delete\_organization\_dsp\_block

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.delete_organization_dsp_block(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	dsp_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Delete dsp block

Deletes a dsp block.

| Parameters        |                                                                                                                                                                |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                                                            |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                            |
| `dsp_id`          | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')]` |
| `**kwargs`        | ` `                                                                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### delete\_organization\_secret

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.delete_organization_secret(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	secret_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Secret ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Delete secret

Deletes a secret

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `secret_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Secret ID')]`       |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### delete\_organization\_transfer\_learning\_block

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.delete_organization_transfer_learning_block(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	transfer_learning_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Transfer learning ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Delete transfer learning block

Deletes a transfer learning block.

| Parameters             |                                                                                                                          |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `self`                 | ` `                                                                                                                      |
| `organization_id`      | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`      |
| `transfer_learning_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Transfer learning ID')]` |
| `**kwargs`             | ` `                                                                                                                      |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### delete\_organization\_transformation\_block

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.delete_organization_transformation_block(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	transformation_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Transformation block ID.')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Delete transformation block

Deletes a transformation block.

| Parameters          |                                                                                                                              |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `self`              | ` `                                                                                                                          |
| `organization_id`   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`          |
| `transformation_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Transformation block ID.')]` |
| `**kwargs`          | ` `                                                                                                                          |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### export\_organization\_deploy\_block

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.export_organization_deploy_block(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	deploy_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Deploy block ID.')],
	**kwargs
) ‑> edgeimpulse_api.models.export_block_response.ExportBlockResponse
```

Export deploy block

Download the source code for this block.

| Parameters        |                                                                                                                      |
| ----------------- | -------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                  |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`  |
| `deploy_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Deploy block ID.')]` |
| `**kwargs`        | ` `                                                                                                                  |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.export_block_response.ExportBlockResponse` |

#### export\_organization\_dsp\_block

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.export_organization_dsp_block(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	dsp_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')],
	**kwargs
) ‑> edgeimpulse_api.models.export_block_response.ExportBlockResponse
```

Export dsp block

Download the source code for this block.

| Parameters        |                                                                                                                                                                |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                                                            |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                            |
| `dsp_id`          | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')]` |
| `**kwargs`        | ` `                                                                                                                                                            |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.export_block_response.ExportBlockResponse` |

#### export\_organization\_transfer\_learning\_block

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.export_organization_transfer_learning_block(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	transfer_learning_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Transfer learning ID')],
	**kwargs
) ‑> edgeimpulse_api.models.export_block_response.ExportBlockResponse
```

Export transfer learning block

Download the source code for this block.

| Parameters             |                                                                                                                          |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `self`                 | ` `                                                                                                                      |
| `organization_id`      | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`      |
| `transfer_learning_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Transfer learning ID')]` |
| `**kwargs`             | ` `                                                                                                                      |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.export_block_response.ExportBlockResponse` |

#### export\_organization\_transformation\_block

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.export_organization_transformation_block(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	transformation_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Transformation block ID.')],
	**kwargs
) ‑> edgeimpulse_api.models.export_block_response.ExportBlockResponse
```

Export transformation block

Download the source code for this block.

| Parameters          |                                                                                                                              |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `self`              | ` `                                                                                                                          |
| `organization_id`   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`          |
| `transformation_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Transformation block ID.')]` |
| `**kwargs`          | ` `                                                                                                                          |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.export_block_response.ExportBlockResponse` |

#### get\_organization\_deploy\_block

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.get_organization_deploy_block(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	deploy_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Deploy block ID.')],
	**kwargs
) ‑> edgeimpulse_api.models.get_organization_deploy_block_response.GetOrganizationDeployBlockResponse
```

Get deploy block

Gets a deploy block.

| Parameters        |                                                                                                                      |
| ----------------- | -------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                  |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`  |
| `deploy_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Deploy block ID.')]` |
| `**kwargs`        | ` `                                                                                                                  |

| Returns                                                                                            |
| -------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_organization_deploy_block_response.GetOrganizationDeployBlockResponse` |

#### get\_organization\_dsp\_block

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.get_organization_dsp_block(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	dsp_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')],
	**kwargs
) ‑> edgeimpulse_api.models.get_organization_dsp_block_response.GetOrganizationDspBlockResponse
```

Get dsp block

Gets a dsp block.

| Parameters        |                                                                                                                                                                |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                                                            |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                            |
| `dsp_id`          | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')]` |
| `**kwargs`        | ` `                                                                                                                                                            |

| Returns                                                                                      |
| -------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_organization_dsp_block_response.GetOrganizationDspBlockResponse` |

#### get\_organization\_transfer\_learning\_block

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.get_organization_transfer_learning_block(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	transfer_learning_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Transfer learning ID')],
	**kwargs
) ‑> edgeimpulse_api.models.get_organization_transfer_learning_block_response.GetOrganizationTransferLearningBlockResponse
```

Get transfer learning block

Gets a transfer learning block.

| Parameters             |                                                                                                                          |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `self`                 | ` `                                                                                                                      |
| `organization_id`      | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`      |
| `transfer_learning_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Transfer learning ID')]` |
| `**kwargs`             | ` `                                                                                                                      |

| Returns                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_organization_transfer_learning_block_response.GetOrganizationTransferLearningBlockResponse` |

#### get\_organization\_transformation\_block

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.get_organization_transformation_block(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	transformation_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Transformation block ID.')],
	**kwargs
) ‑> edgeimpulse_api.models.get_organization_transformation_block_response.GetOrganizationTransformationBlockResponse
```

Get transformation block

Get a transformation block.

| Parameters          |                                                                                                                              |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `self`              | ` `                                                                                                                          |
| `organization_id`   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`          |
| `transformation_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Transformation block ID.')]` |
| `**kwargs`          | ` `                                                                                                                          |

| Returns                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.get_organization_transformation_block_response.GetOrganizationTransformationBlockResponse` |

#### get\_public\_organization\_transformation\_block

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.get_public_organization_transformation_block(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	transformation_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Transformation block ID.')],
	**kwargs
) ‑> edgeimpulse_api.models.get_public_organization_transformation_block_response.GetPublicOrganizationTransformationBlockResponse
```

Get public transformation block

Retrieve a transformation blocks published by other organizations, available for all organizations.

| Parameters          |                                                                                                                              |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `self`              | ` `                                                                                                                          |
| `organization_id`   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`          |
| `transformation_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Transformation block ID.')]` |
| `**kwargs`          | ` `                                                                                                                          |

| Returns                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_public_organization_transformation_block_response.GetPublicOrganizationTransformationBlockResponse` |

#### list\_organization\_deploy\_blocks

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.list_organization_deploy_blocks(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	**kwargs
) ‑> edgeimpulse_api.models.list_organization_deploy_blocks_response.ListOrganizationDeployBlocksResponse
```

Get deploy blocks

Retrieve all deploy blocks.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                                                                |
| ------------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.list_organization_deploy_blocks_response.ListOrganizationDeployBlocksResponse` |

#### list\_organization\_dsp\_blocks

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.list_organization_dsp_blocks(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	**kwargs
) ‑> edgeimpulse_api.models.list_organization_dsp_blocks_response.ListOrganizationDspBlocksResponse
```

Get dsp blocks

Retrieve all dsp blocks.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                                                          |
| ------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.list_organization_dsp_blocks_response.ListOrganizationDspBlocksResponse` |

#### list\_organization\_secrets

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.list_organization_secrets(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	**kwargs
) ‑> edgeimpulse_api.models.list_organization_secrets_response.ListOrganizationSecretsResponse
```

Get secrets

Retrieve all secrets.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                                                     |
| ------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_organization_secrets_response.ListOrganizationSecretsResponse` |

#### list\_organization\_transfer\_learning\_blocks

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.list_organization_transfer_learning_blocks(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	**kwargs
) ‑> edgeimpulse_api.models.list_organization_transfer_learning_blocks_response.ListOrganizationTransferLearningBlocksResponse
```

Get transfer learning blocks

Retrieve all transfer learning blocks.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_organization_transfer_learning_blocks_response.ListOrganizationTransferLearningBlocksResponse` |

#### list\_organization\_transformation\_blocks

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.list_organization_transformation_blocks(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	**kwargs
) ‑> edgeimpulse_api.models.list_organization_transformation_blocks_response.ListOrganizationTransformationBlocksResponse
```

Get transformation blocks

Retrieve all transformation blocks.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_organization_transformation_blocks_response.ListOrganizationTransformationBlocksResponse` |

#### list\_public\_organization\_transformation\_blocks

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.list_public_organization_transformation_blocks(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	**kwargs
) ‑> edgeimpulse_api.models.list_public_organization_transformation_blocks_response.ListPublicOrganizationTransformationBlocksResponse
```

List public transformation blocks

Retrieve all transformation blocks published by other organizations, available for all organizations.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_public_organization_transformation_blocks_response.ListPublicOrganizationTransformationBlocksResponse` |

#### retry\_organization\_dsp\_block

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.retry_organization_dsp_block(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	dsp_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Retry connection to dsp block

Retry launch a dsp block.

| Parameters        |                                                                                                                                                                |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                                                            |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                            |
| `dsp_id`          | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')]` |
| `**kwargs`        | ` `                                                                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### update\_organization\_deploy\_block

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.update_organization_deploy_block(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	deploy_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Deploy block ID.')],
	name: Annotated[str, Strict(strict=True)] | None = None,
	docker_container: Annotated[str, Strict(strict=True)] | None = None,
	description: Annotated[str, Strict(strict=True)] | None = None,
	cli_arguments: Annotated[str, Strict(strict=True)] | None = None,
	requests_cpu: float | None = None,
	requests_memory: Annotated[int, Strict(strict=True)] | None = None,
	limits_cpu: float | None = None,
	limits_memory: Annotated[int, Strict(strict=True)] | None = None,
	photo: Annotated[str, Strict(strict=True)] | None = None,
	integrate_url: Annotated[str, Strict(strict=True)] | None = None,
	privileged: Annotated[bool, Strict(strict=True)] | None = None,
	mount_learn_block: Annotated[bool, Strict(strict=True)] | None = None,
	supports_eon_compiler: Annotated[bool, Strict(strict=True)] | None = None,
	show_optimizations: Annotated[bool, Strict(strict=True)] | None = None,
	category: Annotated[str, Strict(strict=True)] | None = None,
	source_code_download_staff_only: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Whether the source code is only available for staff users.')] = None,
	parameters: Annotated[List[Dict[str, Any]] | None, FieldInfo(annotation=NoneType, required=True, description="List of parameters, spec'ed according to https://docs.edgeimpulse.com/docs/tips-and-tricks/adding-parameters-to-custom-blocks")] = None,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Update deploy block

Updates a deploy block. Only values in the body will be updated.

| Parameters                        |                                                                                                                                                                                           |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                            | ` `                                                                                                                                                                                       |
| `organization_id`                 | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                       |
| `deploy_id`                       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Deploy block ID.')]`                                                                      |
| `name`                            | `Annotated[str, Strict(strict=True)] \| None = None`                                                                                                                                      |
| `docker_container`                | `Annotated[str, Strict(strict=True)] \| None = None`                                                                                                                                      |
| `description`                     | `Annotated[str, Strict(strict=True)] \| None = None`                                                                                                                                      |
| `cli_arguments`                   | `Annotated[str, Strict(strict=True)] \| None = None`                                                                                                                                      |
| `requests_cpu`                    | `float \| None = None`                                                                                                                                                                    |
| `requests_memory`                 | `Annotated[int, Strict(strict=True)] \| None = None`                                                                                                                                      |
| `limits_cpu`                      | `float \| None = None`                                                                                                                                                                    |
| `limits_memory`                   | `Annotated[int, Strict(strict=True)] \| None = None`                                                                                                                                      |
| `photo`                           | `Annotated[str, Strict(strict=True)] \| None = None`                                                                                                                                      |
| `integrate_url`                   | `Annotated[str, Strict(strict=True)] \| None = None`                                                                                                                                      |
| `privileged`                      | `Annotated[bool, Strict(strict=True)] \| None = None`                                                                                                                                     |
| `mount_learn_block`               | `Annotated[bool, Strict(strict=True)] \| None = None`                                                                                                                                     |
| `supports_eon_compiler`           | `Annotated[bool, Strict(strict=True)] \| None = None`                                                                                                                                     |
| `show_optimizations`              | `Annotated[bool, Strict(strict=True)] \| None = None`                                                                                                                                     |
| `category`                        | `Annotated[str, Strict(strict=True)] \| None = None`                                                                                                                                      |
| `source_code_download_staff_only` | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Whether the source code is only available for staff users.')] = None` |
| `parameters`                      | `Annotated[List[Dict[str, Any]] \| None, FieldInfo(annotation=NoneType, required=True, description="List of parameters, spec'ed according to https`                                       |
| `**kwargs`                        | ` `                                                                                                                                                                                       |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### update\_organization\_dsp\_block

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.update_organization_dsp_block(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	dsp_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')],
	update_organization_dsp_block_request: edgeimpulse_api.models.update_organization_dsp_block_request.UpdateOrganizationDspBlockRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Update dsp block

Updates a dsp block. Only values in the body will be updated.

| Parameters                              |                                                                                                                                                                |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                                  | ` `                                                                                                                                                            |
| `organization_id`                       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                            |
| `dsp_id`                                | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')]` |
| `update_organization_dsp_block_request` | `edgeimpulse_api.models.update_organization_dsp_block_request.UpdateOrganizationDspBlockRequest`                                                               |
| `**kwargs`                              | ` `                                                                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### update\_organization\_transfer\_learning\_block

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.update_organization_transfer_learning_block(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	transfer_learning_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Transfer learning ID')],
	update_organization_transfer_learning_block_request: edgeimpulse_api.models.update_organization_transfer_learning_block_request.UpdateOrganizationTransferLearningBlockRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Update transfer learning block

Updates a transfer learning block. Only values in the body will be updated.

| Parameters                                            |                                                                                                                             |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `self`                                                | ` `                                                                                                                         |
| `organization_id`                                     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`         |
| `transfer_learning_id`                                | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Transfer learning ID')]`    |
| `update_organization_transfer_learning_block_request` | `edgeimpulse_api.models.update_organization_transfer_learning_block_request.UpdateOrganizationTransferLearningBlockRequest` |
| `**kwargs`                                            | ` `                                                                                                                         |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### update\_organization\_transformation\_block

```python  theme={"system"}
edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi.update_organization_transformation_block(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	transformation_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Transformation block ID.')],
	update_organization_transformation_block_request: edgeimpulse_api.models.update_organization_transformation_block_request.UpdateOrganizationTransformationBlockRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Update transformation block

Updates a transformation block. Only values in the body will be updated.

| Parameters                                         |                                                                                                                              |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `self`                                             | ` `                                                                                                                          |
| `organization_id`                                  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`          |
| `transformation_id`                                | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Transformation block ID.')]` |
| `update_organization_transformation_block_request` | `edgeimpulse_api.models.update_organization_transformation_block_request.UpdateOrganizationTransformationBlockRequest`       |
| `**kwargs`                                         | ` `                                                                                                                          |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |


Built with [Mintlify](https://mintlify.com).