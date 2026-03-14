# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/whitelabels_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api.whitelabels_api

## Classes

### WhitelabelsApi

```python  theme={"system"}
edgeimpulse_api.api.whitelabels_api.WhitelabelsApi(
	api_client=None
)
```

| Parameters        |     |
| ----------------- | --- |
| `api_client=None` | ` ` |

***

**METHODS**

#### get\_all\_impulse\_blocks

```python  theme={"system"}
edgeimpulse_api.api.whitelabels_api.WhitelabelsApi.get_all_impulse_blocks(
	self,
	whitelabel_identifier: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Whitelabel ID')],
	**kwargs
) ‑> edgeimpulse_api.models.get_impulse_blocks_response.GetImpulseBlocksResponse
```

Get impulse blocks

Lists all possible DSP and ML blocks available for this white label.

| Parameters              |                                                                                                                   |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                               |
| `whitelabel_identifier` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Whitelabel ID')]` |
| `**kwargs`              | ` `                                                                                                               |

| Returns                                                                       |
| ----------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_impulse_blocks_response.GetImpulseBlocksResponse` |

#### get\_whitelabel\_domain

```python  theme={"system"}
edgeimpulse_api.api.whitelabels_api.WhitelabelsApi.get_whitelabel_domain(
	self,
	whitelabel_identifier: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Whitelabel ID')],
	**kwargs
) ‑> edgeimpulse_api.models.get_whitelabel_domain_response.GetWhitelabelDomainResponse
```

Get white label domain

Get a white label domain given its unique identifier.

| Parameters              |                                                                                                                   |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                               |
| `whitelabel_identifier` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Whitelabel ID')]` |
| `**kwargs`              | ` `                                                                                                               |

| Returns                                                                             |
| ----------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_whitelabel_domain_response.GetWhitelabelDomainResponse` |

#### update\_deployment\_targets

```python  theme={"system"}
edgeimpulse_api.api.whitelabels_api.WhitelabelsApi.update_deployment_targets(
	self,
	whitelabel_identifier: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Whitelabel ID')],
	update_whitelabel_deployment_targets_request: edgeimpulse_api.models.update_whitelabel_deployment_targets_request.UpdateWhitelabelDeploymentTargetsRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Update deployment targets

Update some or all of the deployment targets enabled for this white label.

| Parameters                                     |                                                                                                                   |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `self`                                         | ` `                                                                                                               |
| `whitelabel_identifier`                        | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Whitelabel ID')]` |
| `update_whitelabel_deployment_targets_request` | `edgeimpulse_api.models.update_whitelabel_deployment_targets_request.UpdateWhitelabelDeploymentTargetsRequest`    |
| `**kwargs`                                     | ` `                                                                                                               |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |


Built with [Mintlify](https://mintlify.com).