# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/organization_portals_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api.organization_portals_api

## Classes

### OrganizationPortalsApi

```python  theme={"system"}
edgeimpulse_api.api.organization_portals_api.OrganizationPortalsApi(
	api_client=None
)
```

| Parameters        |     |
| ----------------- | --- |
| `api_client=None` | ` ` |

***

**METHODS**

#### create\_organization\_portal

```python  theme={"system"}
edgeimpulse_api.api.organization_portals_api.OrganizationPortalsApi.create_organization_portal(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	create_organization_portal_request: edgeimpulse_api.models.create_organization_portal_request.CreateOrganizationPortalRequest,
	**kwargs
) ‑> edgeimpulse_api.models.create_organization_portal_response.CreateOrganizationPortalResponse
```

Create upload portal

Creates a new upload portal for the organization.

| Parameters                           |                                                                                                                     |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| `self`                               | ` `                                                                                                                 |
| `organization_id`                    | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `create_organization_portal_request` | `edgeimpulse_api.models.create_organization_portal_request.CreateOrganizationPortalRequest`                         |
| `**kwargs`                           | ` `                                                                                                                 |

| Returns                                                                                       |
| --------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.create_organization_portal_response.CreateOrganizationPortalResponse` |

#### delete\_organization\_portal

```python  theme={"system"}
edgeimpulse_api.api.organization_portals_api.OrganizationPortalsApi.delete_organization_portal(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	portal_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Portal ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Delete upload portal

Deletes an upload portal for the organization.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `portal_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Portal ID')]`       |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### get\_organization\_portal

```python  theme={"system"}
edgeimpulse_api.api.organization_portals_api.OrganizationPortalsApi.get_organization_portal(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	portal_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Portal ID')],
	**kwargs
) ‑> edgeimpulse_api.models.get_organization_portal_response.GetOrganizationPortalResponse
```

Retrieve upload portal information

Retrieve a single upload portals identified by ID.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `portal_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Portal ID')]`       |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                                                 |
| --------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_organization_portal_response.GetOrganizationPortalResponse` |

#### list\_organization\_portals

```python  theme={"system"}
edgeimpulse_api.api.organization_portals_api.OrganizationPortalsApi.list_organization_portals(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	**kwargs
) ‑> edgeimpulse_api.models.list_organization_portals_response.ListOrganizationPortalsResponse
```

List upload portals

Retrieve all configured upload portals.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                                                     |
| ------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_organization_portals_response.ListOrganizationPortalsResponse` |

#### rotate\_organization\_portal\_token

```python  theme={"system"}
edgeimpulse_api.api.organization_portals_api.OrganizationPortalsApi.rotate_organization_portal_token(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	portal_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Portal ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Rotate upload portal token

Rotates the token for an upload portal.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `portal_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Portal ID')]`       |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### update\_organization\_portal

```python  theme={"system"}
edgeimpulse_api.api.organization_portals_api.OrganizationPortalsApi.update_organization_portal(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	portal_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Portal ID')],
	create_organization_portal_request: edgeimpulse_api.models.create_organization_portal_request.CreateOrganizationPortalRequest,
	**kwargs
) ‑> edgeimpulse_api.models.update_organization_portal_response.UpdateOrganizationPortalResponse
```

Update upload portal

Updates an upload portal for the organization.

| Parameters                           |                                                                                                                     |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| `self`                               | ` `                                                                                                                 |
| `organization_id`                    | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `portal_id`                          | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Portal ID')]`       |
| `create_organization_portal_request` | `edgeimpulse_api.models.create_organization_portal_request.CreateOrganizationPortalRequest`                         |
| `**kwargs`                           | ` `                                                                                                                 |

| Returns                                                                                       |
| --------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.update_organization_portal_response.UpdateOrganizationPortalResponse` |

#### verify\_organization\_portal

```python  theme={"system"}
edgeimpulse_api.api.organization_portals_api.OrganizationPortalsApi.verify_organization_portal(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	portal_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Portal ID')],
	**kwargs
) ‑> edgeimpulse_api.models.verify_organization_bucket_response.VerifyOrganizationBucketResponse
```

Verify upload portal information

Retrieve a subset of files from the portal, to be used in the data source wizard.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `portal_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Portal ID')]`       |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                                                       |
| --------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.verify_organization_bucket_response.VerifyOrganizationBucketResponse` |


Built with [Mintlify](https://mintlify.com).