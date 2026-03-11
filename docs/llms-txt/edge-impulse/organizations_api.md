# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/organizations_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api.organizations_api

## Classes

### OrganizationsApi

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi(
	api_client=None
)
```

| Parameters        |     |
| ----------------- | --- |
| `api_client=None` | ` ` |

***

**METHODS**

#### add\_organization\_api\_key

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.add_organization_api_key(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	add_organization_api_key_request: edgeimpulse_api.models.add_organization_api_key_request.AddOrganizationApiKeyRequest,
	**kwargs
) ‑> edgeimpulse_api.models.add_api_key_response.AddApiKeyResponse
```

Add API key

Add an API key.

| Parameters                         |                                                                                                                     |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                             | ` `                                                                                                                 |
| `organization_id`                  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `add_organization_api_key_request` | `edgeimpulse_api.models.add_organization_api_key_request.AddOrganizationApiKeyRequest`                              |
| `**kwargs`                         | ` `                                                                                                                 |

| Returns                                                         |
| --------------------------------------------------------------- |
| `edgeimpulse_api.models.add_api_key_response.AddApiKeyResponse` |

#### add\_organization\_member

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.add_organization_member(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	add_member_request: edgeimpulse_api.models.add_member_request.AddMemberRequest,
	**kwargs
) ‑> edgeimpulse_api.models.entity_created_response.EntityCreatedResponse
```

Add member

Add a member to an organization.

| Parameters           |                                                                                                                     |
| -------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`               | ` `                                                                                                                 |
| `organization_id`    | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `add_member_request` | `edgeimpulse_api.models.add_member_request.AddMemberRequest`                                                        |
| `**kwargs`           | ` `                                                                                                                 |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.entity_created_response.EntityCreatedResponse` |

#### create\_multi\_project\_deployment

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.create_multi_project_deployment(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	create_multi_project_deployment_request: edgeimpulse_api.models.create_multi_project_deployment_request.CreateMultiProjectDeploymentRequest,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Create multi-project deployment

WIP

| Parameters                                |                                                                                                                     |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                                    | ` `                                                                                                                 |
| `organization_id`                         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `create_multi_project_deployment_request` | `edgeimpulse_api.models.create_multi_project_deployment_request.CreateMultiProjectDeploymentRequest`                |
| `**kwargs`                                | ` `                                                                                                                 |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### delete\_organization

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.delete_organization(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Remove organization

Remove the current organization, and all data associated with it. This is irrevocable!

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### download\_multi\_project\_deployment

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.download_multi_project_deployment(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	job_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Job ID')],
	**kwargs
) ‑> str
```

Download multi-project deployment

WIP

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `job_id`          | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Job ID')]`          |
| `**kwargs`        | ` `                                                                                                                 |

| Returns |
| ------- |
| `str`   |

#### download\_organization\_data\_export

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.download_organization_data_export(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	export_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Export ID')],
	**kwargs
) ‑> None
```

Download organization data export

Download a data export for an organization.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `export_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Export ID')]`       |
| `**kwargs`        | ` `                                                                                                                 |

| Returns |
| ------- |
| `None`  |

#### get\_organization\_data\_export

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.get_organization_data_export(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	export_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Export ID')],
	**kwargs
) ‑> edgeimpulse_api.models.get_organization_data_export_response.GetOrganizationDataExportResponse
```

Get organization data export

Get a data export for an organization.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `export_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Export ID')]`       |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                                                          |
| ------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.get_organization_data_export_response.GetOrganizationDataExportResponse` |

#### get\_organization\_data\_exports

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.get_organization_data_exports(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	limit: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None,
	offset: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.get_organization_data_exports_response.GetOrganizationDataExportsResponse
```

Get all organization data exports

Get all data exports for an organization.

| Parameters        |                                                                                                                                                                                                                             |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                                                                                                                         |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                                                         |
| `limit`           | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None`                                                                     |
| `offset`          | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None` |
| `**kwargs`        | ` `                                                                                                                                                                                                                         |

| Returns                                                                                            |
| -------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_organization_data_exports_response.GetOrganizationDataExportsResponse` |

#### get\_organization\_info

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.get_organization_info(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	**kwargs
) ‑> edgeimpulse_api.models.organization_info_response.OrganizationInfoResponse
```

Organization information

List all information about this organization.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                                      |
| ---------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_info_response.OrganizationInfoResponse` |

#### get\_organization\_metrics

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.get_organization_metrics(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	exclude_edge_impulse_users: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Whether to exclude Edge Impulse users when counting enterprise entitlements usage')] = None,
	project_visibility: Annotated[edgeimpulse_api.models.project_visibility.ProjectVisibility | None, FieldInfo(annotation=NoneType, required=True, description='What project visibility type to include when counting enterprise entitlements usage')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.organization_metrics_response.OrganizationMetricsResponse
```

Organization metrics

Get general metrics for this organization.

| Parameters                   |                                                                                                                                                                                                                                           |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                       | ` `                                                                                                                                                                                                                                       |
| `organization_id`            | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                                                                       |
| `exclude_edge_impulse_users` | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Whether to exclude Edge Impulse users when counting enterprise entitlements usage')] = None`                          |
| `project_visibility`         | `Annotated[edgeimpulse_api.models.project_visibility.ProjectVisibility \| None, FieldInfo(annotation=NoneType, required=True, description='What project visibility type to include when counting enterprise entitlements usage')] = None` |
| `**kwargs`                   | ` `                                                                                                                                                                                                                                       |

| Returns                                                                            |
| ---------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_metrics_response.OrganizationMetricsResponse` |

#### invite\_organization\_member

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.invite_organization_member(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	invite_organization_member_request: edgeimpulse_api.models.invite_organization_member_request.InviteOrganizationMemberRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Invite member

Invite a member to an organization.

| Parameters                           |                                                                                                                     |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| `self`                               | ` `                                                                                                                 |
| `organization_id`                    | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `invite_organization_member_request` | `edgeimpulse_api.models.invite_organization_member_request.InviteOrganizationMemberRequest`                         |
| `**kwargs`                           | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### list\_organization\_api\_keys

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.list_organization_api_keys(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	**kwargs
) ‑> edgeimpulse_api.models.list_organization_api_keys_response.ListOrganizationApiKeysResponse
```

Get API keys

Retrieve all API keys. This does **not** return the full API key, but only a portion (for security purposes).

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                                                      |
| -------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_organization_api_keys_response.ListOrganizationApiKeysResponse` |

#### list\_organization\_projects

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.list_organization_projects(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	**kwargs
) ‑> edgeimpulse_api.models.list_projects_response.ListProjectsResponse
```

Get projects

Retrieve all projects for the organization.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                              |
| -------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_projects_response.ListProjectsResponse` |

#### list\_organizations

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.list_organizations(
	self,
	**kwargs
) ‑> edgeimpulse_api.models.list_organizations_response.ListOrganizationsResponse
```

List active organizations

Retrieve list of organizations that a user is a part of. If authenticating using JWT token this lists all the organizations the user has access to, if authenticating using an API key, this only lists that organization.

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |
| `**kwargs` | ` ` |

| Returns                                                                        |
| ------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.list_organizations_response.ListOrganizationsResponse` |

#### remove\_organization\_member

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.remove_organization_member(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	remove_member_request: edgeimpulse_api.models.remove_member_request.RemoveMemberRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Remove member

Remove a member from an organization. Note that you cannot invoke this function if only a single member is present to the organization.

| Parameters              |                                                                                                                     |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                                 |
| `organization_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `remove_member_request` | `edgeimpulse_api.models.remove_member_request.RemoveMemberRequest`                                                  |
| `**kwargs`              | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### request\_enterprise\_hr\_block\_license

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.request_enterprise_hr_block_license(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Request HR block license

Request a license required for the deployment of an impulse containing the Edge Impulse HR block.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### request\_enterprise\_limits\_increase

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.request_enterprise_limits_increase(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	enterprise_limits_increase_request: edgeimpulse_api.models.enterprise_limits_increase_request.EnterpriseLimitsIncreaseRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Request organization limits increase

Request an increase in the limits for this organization. Available limits are: users, projects, compute, storage.

| Parameters                           |                                                                                                                     |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| `self`                               | ` `                                                                                                                 |
| `organization_id`                    | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `enterprise_limits_increase_request` | `edgeimpulse_api.models.enterprise_limits_increase_request.EnterpriseLimitsIncreaseRequest`                         |
| `**kwargs`                           | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### request\_enterprise\_trial\_extension

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.request_enterprise_trial_extension(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	enterprise_upgrade_or_trial_extension_request: edgeimpulse_api.models.enterprise_upgrade_or_trial_extension_request.EnterpriseUpgradeOrTrialExtensionRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Request trial extension

Request an extension for an enterprise trial.

| Parameters                                      |                                                                                                                     |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                                          | ` `                                                                                                                 |
| `organization_id`                               | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `enterprise_upgrade_or_trial_extension_request` | `edgeimpulse_api.models.enterprise_upgrade_or_trial_extension_request.EnterpriseUpgradeOrTrialExtensionRequest`     |
| `**kwargs`                                      | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### resend\_organization\_member\_invite

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.resend_organization_member_invite(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	member_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Member ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Resend invitation

Resend an invitation to a member in an organization.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `member_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Member ID')]`       |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### revoke\_organization\_api\_key

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.revoke_organization_api_key(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	api_key_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='API key ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Revoke API key

Revoke an API key.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `api_key_id`      | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='API key ID')]`      |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### set\_organization\_member\_datasets

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.set_organization_member_datasets(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	member_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Member ID')],
	set_member_datasets_request: edgeimpulse_api.models.set_member_datasets_request.SetMemberDatasetsRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Set member datasets

Set the datasets a guest member has access to in an organization.

| Parameters                    |                                                                                                                     |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                        | ` `                                                                                                                 |
| `organization_id`             | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `member_id`                   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Member ID')]`       |
| `set_member_datasets_request` | `edgeimpulse_api.models.set_member_datasets_request.SetMemberDatasetsRequest`                                       |
| `**kwargs`                    | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### set\_organization\_member\_role

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.set_organization_member_role(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	member_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Member ID')],
	set_member_role_request: edgeimpulse_api.models.set_member_role_request.SetMemberRoleRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Set member role

Change the role of a member in an organization.

| Parameters                |                                                                                                                     |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                    | ` `                                                                                                                 |
| `organization_id`         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `member_id`               | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Member ID')]`       |
| `set_member_role_request` | `edgeimpulse_api.models.set_member_role_request.SetMemberRoleRequest`                                               |
| `**kwargs`                | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### test\_organization\_admin

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.test_organization_admin(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Admin endpoint

Test endpoint that can only be reached with admin rights.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### update\_organization

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.update_organization(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	update_organization_request: edgeimpulse_api.models.update_organization_request.UpdateOrganizationRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Update organization

Update organization properties such as name and logo.

| Parameters                    |                                                                                                                     |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                        | ` `                                                                                                                 |
| `organization_id`             | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `update_organization_request` | `edgeimpulse_api.models.update_organization_request.UpdateOrganizationRequest`                                      |
| `**kwargs`                    | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### upload\_organization\_header

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.upload_organization_header(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	image: Annotated[str, Strict(strict=True)] | None = None,
	**kwargs
) ‑> edgeimpulse_api.models.upload_asset_response.UploadAssetResponse
```

Upload organization header image

Uploads and updates the organization header image

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `image`           | `Annotated[str, Strict(strict=True)] \| None = None`                                                                |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.upload_asset_response.UploadAssetResponse` |

#### upload\_organization\_logo

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.upload_organization_logo(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	image: Annotated[str, Strict(strict=True)] | None = None,
	**kwargs
) ‑> edgeimpulse_api.models.upload_asset_response.UploadAssetResponse
```

Upload organization logo

Uploads and updates the organization logo

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `image`           | `Annotated[str, Strict(strict=True)] \| None = None`                                                                |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.upload_asset_response.UploadAssetResponse` |

#### upload\_organization\_readme\_image

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.upload_organization_readme_image(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	image: Annotated[str, Strict(strict=True)],
	**kwargs
) ‑> edgeimpulse_api.models.upload_readme_image_response.UploadReadmeImageResponse
```

Upload image for readme

Uploads an image to the user CDN and returns the path.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `image`           | `Annotated[str, Strict(strict=True)]`                                                                               |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                                         |
| ------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.upload_readme_image_response.UploadReadmeImageResponse` |

#### whitelabel\_admin\_add\_development\_board

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_add_development_board(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	development_board_request: edgeimpulse_api.models.development_board_request.DevelopmentBoardRequest,
	**kwargs
) ‑> edgeimpulse_api.models.entity_created_response.EntityCreatedResponse
```

White Label Admin - Add a development board to a whitelabel

White label admin only API to add a development board.

| Parameters                  |                                                                                                                     |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                      | ` `                                                                                                                 |
| `organization_id`           | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `development_board_request` | `edgeimpulse_api.models.development_board_request.DevelopmentBoardRequest`                                          |
| `**kwargs`                  | ` `                                                                                                                 |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.entity_created_response.EntityCreatedResponse` |

#### whitelabel\_admin\_add\_organization\_api\_key

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_add_organization_api_key(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	inner_organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')],
	admin_add_organization_api_key_request: edgeimpulse_api.models.admin_add_organization_api_key_request.AdminAddOrganizationApiKeyRequest,
	**kwargs
) ‑> edgeimpulse_api.models.add_api_key_response.AddApiKeyResponse
```

White Label Admin - Add organization API key

White label admin only API to add an API key to an organization. Add a temporary API key that can be used to make Organizations API (/api/organizations/`{organizationId}`/) requests on behalf of the organization. These API keys are not visible to the organization itself and have a customizable TTL defaulting to 1 minute.

| Parameters                               |                                                                                                                                                         |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                                   | ` `                                                                                                                                                     |
| `organization_id`                        | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                     |
| `inner_organization_id`                  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')]` |
| `admin_add_organization_api_key_request` | `edgeimpulse_api.models.admin_add_organization_api_key_request.AdminAddOrganizationApiKeyRequest`                                                       |
| `**kwargs`                               | ` `                                                                                                                                                     |

| Returns                                                         |
| --------------------------------------------------------------- |
| `edgeimpulse_api.models.add_api_key_response.AddApiKeyResponse` |

#### whitelabel\_admin\_add\_project\_api\_key

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_add_project_api_key(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	admin_add_project_api_key_request: edgeimpulse_api.models.admin_add_project_api_key_request.AdminAddProjectApiKeyRequest,
	**kwargs
) ‑> edgeimpulse_api.models.add_api_key_response.AddApiKeyResponse
```

White Label Admin - Add Project API key

White label admin only API to add an API key to a project. Add a temporary API key that can be used to make Projects API (/api/projects/`{projectId}`/) requests on behalf of the project admin. These API keys are not visible to the project itself and have a customizable TTL defaulting to 1 minute.

| Parameters                          |                                                                                                                     |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                              | ` `                                                                                                                 |
| `organization_id`                   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `project_id`                        | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`      |
| `admin_add_project_api_key_request` | `edgeimpulse_api.models.admin_add_project_api_key_request.AdminAddProjectApiKeyRequest`                             |
| `**kwargs`                          | ` `                                                                                                                 |

| Returns                                                         |
| --------------------------------------------------------------- |
| `edgeimpulse_api.models.add_api_key_response.AddApiKeyResponse` |

#### whitelabel\_admin\_add\_user\_to\_organization

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_add_user_to_organization(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	inner_organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')],
	admin_add_organization_user_request: edgeimpulse_api.models.admin_add_organization_user_request.AdminAddOrganizationUserRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

White Label Admin - Add user to an organization

DEPRECATED. White label admin only API to add a user to an organization. If no user is provided, the current user is used.

| Parameters                            |                                                                                                                                                         |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                                | ` `                                                                                                                                                     |
| `organization_id`                     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                     |
| `inner_organization_id`               | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')]` |
| `admin_add_organization_user_request` | `edgeimpulse_api.models.admin_add_organization_user_request.AdminAddOrganizationUserRequest`                                                            |
| `**kwargs`                            | ` `                                                                                                                                                     |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### whitelabel\_admin\_add\_user\_to\_project

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_add_user_to_project(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	admin_add_project_user_request: edgeimpulse_api.models.admin_add_project_user_request.AdminAddProjectUserRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

White Label Admin - Add user to a project

DEPRECATED. White label admin only API to add a user to a project. If no user is provided, the current user is used.

| Parameters                       |                                                                                                                     |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                           | ` `                                                                                                                 |
| `organization_id`                | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `project_id`                     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`      |
| `admin_add_project_user_request` | `edgeimpulse_api.models.admin_add_project_user_request.AdminAddProjectUserRequest`                                  |
| `**kwargs`                       | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### whitelabel\_admin\_create\_organization

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_create_organization(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	whitelabel_admin_create_organization_request: edgeimpulse_api.models.whitelabel_admin_create_organization_request.WhitelabelAdminCreateOrganizationRequest,
	**kwargs
) ‑> edgeimpulse_api.models.create_organization_response.CreateOrganizationResponse
```

White Label Admin - Create new organization within white label context

Create a new organization. This is an API only available to white label admins

| Parameters                                     |                                                                                                                     |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                                         | ` `                                                                                                                 |
| `organization_id`                              | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `whitelabel_admin_create_organization_request` | `edgeimpulse_api.models.whitelabel_admin_create_organization_request.WhitelabelAdminCreateOrganizationRequest`      |
| `**kwargs`                                     | ` `                                                                                                                 |

| Returns                                                                          |
| -------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.create_organization_response.CreateOrganizationResponse` |

#### whitelabel\_admin\_create\_organization\_export

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_create_organization_export(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	inner_organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')],
	admin_create_organization_data_export_request: edgeimpulse_api.models.admin_create_organization_data_export_request.AdminCreateOrganizationDataExportRequest,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

White Label Admin - Create a new organization data export

Create a new data export for an organization. A job is created to process the export request and the job details are returned in the response. This is an API only available to white label admins.

| Parameters                                      |                                                                                                                                                         |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                                          | ` `                                                                                                                                                     |
| `organization_id`                               | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                     |
| `inner_organization_id`                         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')]` |
| `admin_create_organization_data_export_request` | `edgeimpulse_api.models.admin_create_organization_data_export_request.AdminCreateOrganizationDataExportRequest`                                         |
| `**kwargs`                                      | ` `                                                                                                                                                     |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### whitelabel\_admin\_create\_organization\_project

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_create_organization_project(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	inner_organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')],
	admin_create_project_request: edgeimpulse_api.models.admin_create_project_request.AdminCreateProjectRequest,
	**kwargs
) ‑> edgeimpulse_api.models.create_project_response.CreateProjectResponse
```

White Label Admin - Create a new organization project

White label admin only API to create a new project for an organization.

| Parameters                     |                                                                                                                                                         |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                         | ` `                                                                                                                                                     |
| `organization_id`              | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                     |
| `inner_organization_id`        | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')]` |
| `admin_create_project_request` | `edgeimpulse_api.models.admin_create_project_request.AdminCreateProjectRequest`                                                                         |
| `**kwargs`                     | ` `                                                                                                                                                     |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.create_project_response.CreateProjectResponse` |

#### whitelabel\_admin\_create\_organization\_usage\_report

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_create_organization_usage_report(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	inner_organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')],
	start_date: Annotated[datetime.datetime, FieldInfo(annotation=NoneType, required=True, description='Start date')],
	end_date: Annotated[datetime.datetime, FieldInfo(annotation=NoneType, required=True, description='End date')],
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

White Label Admin - Creates a new usage report

Create a new usage report for an organization. A job is created to process the report request and the job details are returned in the response. This is an API only available to white label admins.

| Parameters              |                                                                                                                                                         |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                                                                     |
| `organization_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                     |
| `inner_organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')]` |
| `start_date`            | `Annotated[datetime.datetime, FieldInfo(annotation=NoneType, required=True, description='Start date')]`                                                 |
| `end_date`              | `Annotated[datetime.datetime, FieldInfo(annotation=NoneType, required=True, description='End date')]`                                                   |
| `**kwargs`              | ` `                                                                                                                                                     |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### whitelabel\_admin\_create\_project

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_create_project(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	admin_create_project_request: edgeimpulse_api.models.admin_create_project_request.AdminCreateProjectRequest,
	**kwargs
) ‑> edgeimpulse_api.models.create_project_response.CreateProjectResponse
```

White Label Admin - Create a new project within white label context.

Create a new free tier project. This is an API only available to white label admins.

| Parameters                     |                                                                                                                     |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| `self`                         | ` `                                                                                                                 |
| `organization_id`              | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `admin_create_project_request` | `edgeimpulse_api.models.admin_create_project_request.AdminCreateProjectRequest`                                     |
| `**kwargs`                     | ` `                                                                                                                 |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.create_project_response.CreateProjectResponse` |

#### whitelabel\_admin\_delete\_organization

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_delete_organization(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	inner_organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')],
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

White Label Admin - Delete an organization

White label admin only API to delete an organization.

| Parameters              |                                                                                                                                                         |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                                                                     |
| `organization_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                     |
| `inner_organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')]` |
| `**kwargs`              | ` `                                                                                                                                                     |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### whitelabel\_admin\_delete\_organization\_export

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_delete_organization_export(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	inner_organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')],
	export_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Export ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

White Label Admin - Delete organization data export

Delete a data export for an organization. This is an API only available to white label admins.

| Parameters              |                                                                                                                                                         |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                                                                     |
| `organization_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                     |
| `inner_organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')]` |
| `export_id`             | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Export ID')]`                                           |
| `**kwargs`              | ` `                                                                                                                                                     |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### whitelabel\_admin\_delete\_organization\_usage\_report

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_delete_organization_usage_report(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	inner_organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')],
	report_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Report ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

White Label Admin - Delete usage report

Delete a usage report for an organization. This is an API only available to white label admins.

| Parameters              |                                                                                                                                                         |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                                                                     |
| `organization_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                     |
| `inner_organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')]` |
| `report_id`             | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Report ID')]`                                           |
| `**kwargs`              | ` `                                                                                                                                                     |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### whitelabel\_admin\_delete\_project

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_delete_project(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

White Label Admin - Delete a project

White label admin only API to delete a project.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `project_id`      | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`      |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### whitelabel\_admin\_delete\_user

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_delete_user(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	user_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Delete a user

White label admin only API to delete a user.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `user_id`         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')]`         |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### whitelabel\_admin\_download\_organization\_usage\_report

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_download_organization_usage_report(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	inner_organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')],
	report_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Report ID')],
	**kwargs
) ‑> None
```

White Label Admin - Download usage report

Download a usage report for an organization. This is an API only available to white label admins.

| Parameters              |                                                                                                                                                         |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                                                                     |
| `organization_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                     |
| `inner_organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')]` |
| `report_id`             | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Report ID')]`                                           |
| `**kwargs`              | ` `                                                                                                                                                     |

| Returns |
| ------- |
| `None`  |

#### whitelabel\_admin\_get\_info

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_get_info(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	**kwargs
) ‑> edgeimpulse_api.models.get_whitelabel_response.GetWhitelabelResponse
```

White Label Admin - Get white label information

White label admin only API to get the white label information.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_whitelabel_response.GetWhitelabelResponse` |

#### whitelabel\_admin\_get\_metrics

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_get_metrics(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	**kwargs
) ‑> edgeimpulse_api.models.admin_get_metrics_response.AdminGetMetricsResponse
```

White Label Admin - Get global white label metrics

White label admin only API to get global metrics.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                                     |
| --------------------------------------------------------------------------- |
| `edgeimpulse_api.models.admin_get_metrics_response.AdminGetMetricsResponse` |

#### whitelabel\_admin\_get\_organization\_compute\_time\_usage

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_get_organization_compute_time_usage(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	inner_organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')],
	start_date: Annotated[datetime.datetime, FieldInfo(annotation=NoneType, required=True, description='Start date')],
	end_date: Annotated[datetime.datetime, FieldInfo(annotation=NoneType, required=True, description='End date')],
	**kwargs
) ‑> edgeimpulse_api.models.admin_get_organization_compute_time_usage_response.AdminGetOrganizationComputeTimeUsageResponse
```

White Label Admin - Get organization compute time usage

Get compute time usage for an organization over a period of time. This is an API only available to white label admins

| Parameters              |                                                                                                                                                         |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                                                                     |
| `organization_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                     |
| `inner_organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')]` |
| `start_date`            | `Annotated[datetime.datetime, FieldInfo(annotation=NoneType, required=True, description='Start date')]`                                                 |
| `end_date`              | `Annotated[datetime.datetime, FieldInfo(annotation=NoneType, required=True, description='End date')]`                                                   |
| `**kwargs`              | ` `                                                                                                                                                     |

| Returns                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.admin_get_organization_compute_time_usage_response.AdminGetOrganizationComputeTimeUsageResponse` |

#### whitelabel\_admin\_get\_organization\_export

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_get_organization_export(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	inner_organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')],
	export_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Export ID')],
	**kwargs
) ‑> edgeimpulse_api.models.get_organization_data_export_response.GetOrganizationDataExportResponse
```

White Label Admin - Get organization data export

Get a data export for an organization. This is an API only available to white label admins.

| Parameters              |                                                                                                                                                         |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                                                                     |
| `organization_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                     |
| `inner_organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')]` |
| `export_id`             | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Export ID')]`                                           |
| `**kwargs`              | ` `                                                                                                                                                     |

| Returns                                                                                          |
| ------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.get_organization_data_export_response.GetOrganizationDataExportResponse` |

#### whitelabel\_admin\_get\_organization\_exports

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_get_organization_exports(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	inner_organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')],
	limit: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None,
	offset: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.get_organization_data_exports_response.GetOrganizationDataExportsResponse
```

White Label Admin - Get all organization data exports

Get all data exports for an organization. This is an API only available to white label admins.

| Parameters              |                                                                                                                                                                                                                             |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                                                                                                                                         |
| `organization_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                                                         |
| `inner_organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')]`                                                                     |
| `limit`                 | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None`                                                                     |
| `offset`                | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None` |
| `**kwargs`              | ` `                                                                                                                                                                                                                         |

| Returns                                                                                            |
| -------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_organization_data_exports_response.GetOrganizationDataExportsResponse` |

#### whitelabel\_admin\_get\_organization\_info

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_get_organization_info(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	inner_organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')],
	include_deleted: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Whether to include deleted entities (users, projects, orgs)')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.admin_organization_info_response.AdminOrganizationInfoResponse
```

White Label Admin - Get organization information

White label admin only API to list all information about an organization.

| Parameters              |                                                                                                                                                                                            |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `self`                  | ` `                                                                                                                                                                                        |
| `organization_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                        |
| `inner_organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')]`                                    |
| `include_deleted`       | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Whether to include deleted entities (users, projects, orgs)')] = None` |
| `**kwargs`              | ` `                                                                                                                                                                                        |

| Returns                                                                                 |
| --------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.admin_organization_info_response.AdminOrganizationInfoResponse` |

#### whitelabel\_admin\_get\_organization\_jobs

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_get_organization_jobs(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	inner_organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')],
	limit: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None,
	offset: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.list_jobs_response.ListJobsResponse
```

White Label Admin - Get organization jobs

White label admin only API to get the list of all jobs for a organization.

| Parameters              |                                                                                                                                                                                                                             |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                                                                                                                                         |
| `organization_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                                                         |
| `inner_organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')]`                                                                     |
| `limit`                 | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None`                                                                     |
| `offset`                | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None` |
| `**kwargs`              | ` `                                                                                                                                                                                                                         |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.list_jobs_response.ListJobsResponse` |

#### whitelabel\_admin\_get\_organization\_usage\_report

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_get_organization_usage_report(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	inner_organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')],
	report_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Report ID')],
	**kwargs
) ‑> edgeimpulse_api.models.admin_get_report_response.AdminGetReportResponse
```

White Label Admin - Get usage report

Get a usage report for an organization. This is an API only available to white label admins.

| Parameters              |                                                                                                                                                         |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                                                                     |
| `organization_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                     |
| `inner_organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')]` |
| `report_id`             | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Report ID')]`                                           |
| `**kwargs`              | ` `                                                                                                                                                     |

| Returns                                                                   |
| ------------------------------------------------------------------------- |
| `edgeimpulse_api.models.admin_get_report_response.AdminGetReportResponse` |

#### whitelabel\_admin\_get\_organization\_usage\_reports

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_get_organization_usage_reports(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	inner_organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')],
	limit: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None,
	offset: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.admin_get_reports_response.AdminGetReportsResponse
```

White Label Admin - Get all usage reports

Get all usage reports for an organization. This is an API only available to white label admins.

| Parameters              |                                                                                                                                                                                                                             |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                                                                                                                                         |
| `organization_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                                                         |
| `inner_organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')]`                                                                     |
| `limit`                 | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None`                                                                     |
| `offset`                | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None` |
| `**kwargs`              | ` `                                                                                                                                                                                                                         |

| Returns                                                                     |
| --------------------------------------------------------------------------- |
| `edgeimpulse_api.models.admin_get_reports_response.AdminGetReportsResponse` |

#### whitelabel\_admin\_get\_organizations

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_get_organizations(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	active: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Whether to search for entities (users, orgs) active in the last X days')] = None,
	include_deleted: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Whether to include deleted entities (users, projects, orgs)')] = None,
	sort: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Fields and order to sort query by')] = None,
	filters: Annotated[str, Strict(strict=True)] | None = None,
	limit: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None,
	offset: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None,
	search: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Search query')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.admin_get_organizations_response.AdminGetOrganizationsResponse
```

White Label Admin - Get all organizations within a white label

White label admin only API to get the list of all organizations.

| Parameters        |                                                                                                                                                                                                                             |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                                                                                                                         |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                                                         |
| `active`          | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Whether to search for entities (users, orgs) active in the last X days')] = None`                        |
| `include_deleted` | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Whether to include deleted entities (users, projects, orgs)')] = None`                                  |
| `sort`            | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Fields and order to sort query by')] = None`                                                             |
| `filters`         | `Annotated[str, Strict(strict=True)] \| None = None`                                                                                                                                                                        |
| `limit`           | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None`                                                                     |
| `offset`          | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None` |
| `search`          | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Search query')] = None`                                                                                  |
| `**kwargs`        | ` `                                                                                                                                                                                                                         |

| Returns                                                                                 |
| --------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.admin_get_organizations_response.AdminGetOrganizationsResponse` |

#### whitelabel\_admin\_get\_project

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_get_project(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.admin_project_info_response.AdminProjectInfoResponse
```

White Label Admin - Get a white label project

White label admin only API to get project information.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `project_id`      | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`      |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                                       |
| ----------------------------------------------------------------------------- |
| `edgeimpulse_api.models.admin_project_info_response.AdminProjectInfoResponse` |

#### whitelabel\_admin\_get\_project\_jobs

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_get_project_jobs(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	limit: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None,
	offset: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.list_jobs_response.ListJobsResponse
```

White Label Admin - Get project jobs

White label admin only API to get the list of all jobs for a project.

| Parameters        |                                                                                                                                                                                                                             |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                                                                                                                         |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                                                         |
| `project_id`      | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                              |
| `limit`           | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None`                                                                     |
| `offset`          | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None` |
| `**kwargs`        | ` `                                                                                                                                                                                                                         |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.list_jobs_response.ListJobsResponse` |

#### whitelabel\_admin\_get\_projects

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_get_projects(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	active: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Whether to search for entities (users, orgs) active in the last X days')] = None,
	sort: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Fields and order to sort query by')] = None,
	filters: Annotated[str, Strict(strict=True)] | None = None,
	limit: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None,
	offset: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None,
	search: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Search query')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.admin_list_projects_response.AdminListProjectsResponse
```

White Label Admin - Get all white label projects

White label admin only API to get the list of all projects.

| Parameters        |                                                                                                                                                                                                                             |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                                                                                                                         |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                                                         |
| `active`          | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Whether to search for entities (users, orgs) active in the last X days')] = None`                        |
| `sort`            | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Fields and order to sort query by')] = None`                                                             |
| `filters`         | `Annotated[str, Strict(strict=True)] \| None = None`                                                                                                                                                                        |
| `limit`           | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None`                                                                     |
| `offset`          | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None` |
| `search`          | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Search query')] = None`                                                                                  |
| `**kwargs`        | ` `                                                                                                                                                                                                                         |

| Returns                                                                         |
| ------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.admin_list_projects_response.AdminListProjectsResponse` |

#### whitelabel\_admin\_get\_user

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_get_user(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	user_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')],
	**kwargs
) ‑> edgeimpulse_api.models.admin_get_user_response.AdminGetUserResponse
```

White Label Admin - Get a white label user

White label admin only API to get information about a user.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `user_id`         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')]`         |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                               |
| --------------------------------------------------------------------- |
| `edgeimpulse_api.models.admin_get_user_response.AdminGetUserResponse` |

#### whitelabel\_admin\_get\_user\_jobs

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_get_user_jobs(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	user_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')],
	limit: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None,
	offset: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.list_jobs_response.ListJobsResponse
```

White Label Admin - Get user jobs

White label admin only  API to get the list of all project jobs for a user.

| Parameters        |                                                                                                                                                                                                                             |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                                                                                                                         |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                                                         |
| `user_id`         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')]`                                                                                                                 |
| `limit`           | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None`                                                                     |
| `offset`          | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None` |
| `**kwargs`        | ` `                                                                                                                                                                                                                         |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.list_jobs_response.ListJobsResponse` |

#### whitelabel\_admin\_get\_user\_metrics

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_get_user_metrics(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	user_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')],
	**kwargs
) ‑> edgeimpulse_api.models.admin_get_user_metrics_response.AdminGetUserMetricsResponse
```

White Label Admin - Get white label user metrics

White label admin only API to get marketing metrics about a user.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `user_id`         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')]`         |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                                              |
| ------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.admin_get_user_metrics_response.AdminGetUserMetricsResponse` |

#### whitelabel\_admin\_get\_users

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_get_users(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	active: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Whether to search for entities (users, orgs) active in the last X days')] = None,
	tier: Annotated[edgeimpulse_api.models.user_tier_enum.UserTierEnum | None, FieldInfo(annotation=NoneType, required=True, description='Whether to search for free, community plus, professional, or enterprise entities (users, projects)')] = None,
	fields: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Comma separated list of fields to fetch in a query')] = None,
	sort: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Fields and order to sort query by')] = None,
	filters: Annotated[str, Strict(strict=True)] | None = None,
	limit: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None,
	offset: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None,
	search: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Search query')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.admin_get_users_response.AdminGetUsersResponse
```

White Label Admin - Get all white label users

White label admin only API to get the list of all registered users.

| Parameters        |                                                                                                                                                                                                                                                 |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                                                                                                                                             |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                                                                             |
| `active`          | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Whether to search for entities (users, orgs) active in the last X days')] = None`                                            |
| `tier`            | `Annotated[edgeimpulse_api.models.user_tier_enum.UserTierEnum \| None, FieldInfo(annotation=NoneType, required=True, description='Whether to search for free, community plus, professional, or enterprise entities (users, projects)')] = None` |
| `fields`          | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Comma separated list of fields to fetch in a query')] = None`                                                                |
| `sort`            | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Fields and order to sort query by')] = None`                                                                                 |
| `filters`         | `Annotated[str, Strict(strict=True)] \| None = None`                                                                                                                                                                                            |
| `limit`           | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None`                                                                                         |
| `offset`          | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None`                     |
| `search`          | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Search query')] = None`                                                                                                      |
| `**kwargs`        | ` `                                                                                                                                                                                                                                             |

| Returns                                                                 |
| ----------------------------------------------------------------------- |
| `edgeimpulse_api.models.admin_get_users_response.AdminGetUsersResponse` |

#### whitelabel\_admin\_remove\_development\_board

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_remove_development_board(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	development_board_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Development board ID.')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

White Label Admin - Remove a development board from a whitelabel

White label admin only API to remove a development board.

| Parameters             |                                                                                                                           |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `self`                 | ` `                                                                                                                       |
| `organization_id`      | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`       |
| `development_board_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Development board ID.')]` |
| `**kwargs`             | ` `                                                                                                                       |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### whitelabel\_admin\_remove\_user\_from\_organization

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_remove_user_from_organization(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	inner_organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')],
	user_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

White Label Admin - Remove user from an organization

DEPRECATED. White label admin only API to remove a user from an organization.

| Parameters              |                                                                                                                                                         |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                                                                     |
| `organization_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                     |
| `inner_organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')]` |
| `user_id`               | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')]`                                             |
| `**kwargs`              | ` `                                                                                                                                                     |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### whitelabel\_admin\_remove\_user\_from\_project

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_remove_user_from_project(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	user_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

White Label Admin - Remove user from a project

DEPRECATED. White label admin only API to remove a user from a project.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `project_id`      | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`      |
| `user_id`         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')]`         |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### whitelabel\_admin\_restore\_organization

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_restore_organization(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	inner_organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

White Label Admin - Restore an organization

White label admin only API to restore a deleted organization. All organization projects sharing the same deletion date as that of the organization will also be restored. If this is a trial organization that was never upgraded to a paid plan then the organization will be restored to its original trial state.

| Parameters              |                                                                                                                                                         |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                                                                     |
| `organization_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                     |
| `inner_organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')]` |
| `**kwargs`              | ` `                                                                                                                                                     |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### whitelabel\_admin\_update\_default\_deployment\_target

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_update_default_deployment_target(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	update_whitelabel_default_deployment_target_request: edgeimpulse_api.models.update_whitelabel_default_deployment_target_request.UpdateWhitelabelDefaultDeploymentTargetRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

White Label Admin - Update default deployment target

White label admin only API to update the default deployment target for this white label.

| Parameters                                            |                                                                                                                             |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `self`                                                | ` `                                                                                                                         |
| `organization_id`                                     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`         |
| `update_whitelabel_default_deployment_target_request` | `edgeimpulse_api.models.update_whitelabel_default_deployment_target_request.UpdateWhitelabelDefaultDeploymentTargetRequest` |
| `**kwargs`                                            | ` `                                                                                                                         |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### whitelabel\_admin\_update\_deployment\_options\_order

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_update_deployment_options_order(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	update_whitelabel_deployment_options_order_request: edgeimpulse_api.models.update_whitelabel_deployment_options_order_request.UpdateWhitelabelDeploymentOptionsOrderRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

White Label Admin - Update the order of deployment options in the deployment view

White label admin only API to customize the order of deployment options in the deployment view for this white label.

| Parameters                                           |                                                                                                                           |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `self`                                               | ` `                                                                                                                       |
| `organization_id`                                    | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`       |
| `update_whitelabel_deployment_options_order_request` | `edgeimpulse_api.models.update_whitelabel_deployment_options_order_request.UpdateWhitelabelDeploymentOptionsOrderRequest` |
| `**kwargs`                                           | ` `                                                                                                                       |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### whitelabel\_admin\_update\_deployment\_targets

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_update_deployment_targets(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	update_whitelabel_deployment_targets_request: edgeimpulse_api.models.update_whitelabel_deployment_targets_request.UpdateWhitelabelDeploymentTargetsRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

White Label Admin - Update deployment targets

White label admin only API to update some or all of the deployment targets enabled for this white label.

| Parameters                                     |                                                                                                                     |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                                         | ` `                                                                                                                 |
| `organization_id`                              | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `update_whitelabel_deployment_targets_request` | `edgeimpulse_api.models.update_whitelabel_deployment_targets_request.UpdateWhitelabelDeploymentTargetsRequest`      |
| `**kwargs`                                     | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### whitelabel\_admin\_update\_development\_board

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_update_development_board(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	development_board_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Development board ID.')],
	development_board_request_update: edgeimpulse_api.models.development_board_request_update.DevelopmentBoardRequestUpdate,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

White Label Admin - Update a development board in a whitelabel

White label admin only API to update a development board.

| Parameters                         |                                                                                                                           |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `self`                             | ` `                                                                                                                       |
| `organization_id`                  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`       |
| `development_board_id`             | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Development board ID.')]` |
| `development_board_request_update` | `edgeimpulse_api.models.development_board_request_update.DevelopmentBoardRequestUpdate`                                   |
| `**kwargs`                         | ` `                                                                                                                       |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### whitelabel\_admin\_update\_development\_board\_image

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_update_development_board_image(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	development_board_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Development board ID.')],
	image: Annotated[str, Strict(strict=True)] | None = None,
	**kwargs
) ‑> edgeimpulse_api.models.upload_asset_response.UploadAssetResponse
```

White Label Admin - Update the image of a whitelabel development board

White label admin only API to update the image of a development board.

| Parameters             |                                                                                                                           |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `self`                 | ` `                                                                                                                       |
| `organization_id`      | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`       |
| `development_board_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Development board ID.')]` |
| `image`                | `Annotated[str, Strict(strict=True)] \| None = None`                                                                      |
| `**kwargs`             | ` `                                                                                                                       |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.upload_asset_response.UploadAssetResponse` |

#### whitelabel\_admin\_update\_info

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_update_info(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	update_whitelabel_request: edgeimpulse_api.models.update_whitelabel_request.UpdateWhitelabelRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

White Label Admin - Update white label information

White label admin only API to update the white label information.

| Parameters                  |                                                                                                                     |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                      | ` `                                                                                                                 |
| `organization_id`           | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `update_whitelabel_request` | `edgeimpulse_api.models.update_whitelabel_request.UpdateWhitelabelRequest`                                          |
| `**kwargs`                  | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### whitelabel\_admin\_update\_learning\_blocks

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_update_learning_blocks(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	update_whitelabel_learning_blocks_request: edgeimpulse_api.models.update_whitelabel_learning_blocks_request.UpdateWhitelabelLearningBlocksRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

White Label Admin - Update learning blocks

White label admin only API to update some or all of the learning blocks enabled for this white label.

| Parameters                                  |                                                                                                                     |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                                      | ` `                                                                                                                 |
| `organization_id`                           | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `update_whitelabel_learning_blocks_request` | `edgeimpulse_api.models.update_whitelabel_learning_blocks_request.UpdateWhitelabelLearningBlocksRequest`            |
| `**kwargs`                                  | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### whitelabel\_admin\_update\_organization

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_update_organization(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	inner_organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')],
	admin_update_organization_request: edgeimpulse_api.models.admin_update_organization_request.AdminUpdateOrganizationRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

White Label Admin - Update organization

White label admin only API to update organization properties such as name and logo.

| Parameters                          |                                                                                                                                                         |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                              | ` `                                                                                                                                                     |
| `organization_id`                   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                     |
| `inner_organization_id`             | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')]` |
| `admin_update_organization_request` | `edgeimpulse_api.models.admin_update_organization_request.AdminUpdateOrganizationRequest`                                                               |
| `**kwargs`                          | ` `                                                                                                                                                     |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### whitelabel\_admin\_update\_organization\_export

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_update_organization_export(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	inner_organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')],
	export_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Export ID')],
	admin_update_organization_data_export_request: edgeimpulse_api.models.admin_update_organization_data_export_request.AdminUpdateOrganizationDataExportRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

White Label Admin - Update organization data export

Update a data export for an organization. This is an API only available to white label admins.

| Parameters                                      |                                                                                                                                                         |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                                          | ` `                                                                                                                                                     |
| `organization_id`                               | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                     |
| `inner_organization_id`                         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID within the context of a white label')]` |
| `export_id`                                     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Export ID')]`                                           |
| `admin_update_organization_data_export_request` | `edgeimpulse_api.models.admin_update_organization_data_export_request.AdminUpdateOrganizationDataExportRequest`                                         |
| `**kwargs`                                      | ` `                                                                                                                                                     |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### whitelabel\_admin\_update\_project

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_update_project(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	update_project_request: edgeimpulse_api.models.update_project_request.UpdateProjectRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

White Label Admin - Update white label project

White label admin only API to update project properties.

| Parameters               |                                                                                                                     |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| `self`                   | ` `                                                                                                                 |
| `organization_id`        | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `project_id`             | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`      |
| `update_project_request` | `edgeimpulse_api.models.update_project_request.UpdateProjectRequest`                                                |
| `**kwargs`               | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### whitelabel\_admin\_update\_theme\_colors

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_update_theme_colors(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	update_theme_colors_request: edgeimpulse_api.models.update_theme_colors_request.UpdateThemeColorsRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

White Label Admin - Update theme colors

White label admin only API to update some or all theme colors.

| Parameters                    |                                                                                                                     |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                        | ` `                                                                                                                 |
| `organization_id`             | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `update_theme_colors_request` | `edgeimpulse_api.models.update_theme_colors_request.UpdateThemeColorsRequest`                                       |
| `**kwargs`                    | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### whitelabel\_admin\_update\_theme\_device\_logo

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_update_theme_device_logo(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	image: Annotated[str, Strict(strict=True)] | None = None,
	**kwargs
) ‑> edgeimpulse_api.models.upload_asset_response.UploadAssetResponse
```

White Label Admin - Update theme device logo

White label admin only API to update the white label theme device logo.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `image`           | `Annotated[str, Strict(strict=True)] \| None = None`                                                                |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.upload_asset_response.UploadAssetResponse` |

#### whitelabel\_admin\_update\_theme\_favicon

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_update_theme_favicon(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	image: Annotated[str, Strict(strict=True)],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

White Label Admin - Update theme favicon

White label admin only API to update the theme favicon.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `image`           | `Annotated[str, Strict(strict=True)]`                                                                               |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### whitelabel\_admin\_update\_theme\_logo

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_update_theme_logo(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	image: Annotated[str, Strict(strict=True)] | None = None,
	**kwargs
) ‑> edgeimpulse_api.models.upload_asset_response.UploadAssetResponse
```

White Label Admin - Update theme logo

White label admin only API to update the white label theme logo.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `image`           | `Annotated[str, Strict(strict=True)] \| None = None`                                                                |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.upload_asset_response.UploadAssetResponse` |

#### whitelabel\_admin\_update\_user

```python  theme={"system"}
edgeimpulse_api.api.organizations_api.OrganizationsApi.whitelabel_admin_update_user(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	user_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')],
	admin_update_user_request: edgeimpulse_api.models.admin_update_user_request.AdminUpdateUserRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

White Label Admin - Update white label user

White label admin only API to update user properties.

| Parameters                  |                                                                                                                     |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                      | ` `                                                                                                                 |
| `organization_id`           | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `user_id`                   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')]`         |
| `admin_update_user_request` | `edgeimpulse_api.models.admin_update_user_request.AdminUpdateUserRequest`                                           |
| `**kwargs`                  | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |


Built with [Mintlify](https://mintlify.com).