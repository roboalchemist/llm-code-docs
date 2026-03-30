# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/organization_data_campaigns_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api.organization_data_campaigns_api

## Classes

### OrganizationDataCampaignsApi

```python  theme={"system"}
edgeimpulse_api.api.organization_data_campaigns_api.OrganizationDataCampaignsApi(
	api_client=None
)
```

| Parameters        |     |
| ----------------- | --- |
| `api_client=None` | ` ` |

***

**METHODS**

#### add\_organization\_data\_campaign

```python  theme={"system"}
edgeimpulse_api.api.organization_data_campaigns_api.OrganizationDataCampaignsApi.add_organization_data_campaign(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	add_organization_data_campaign_request: edgeimpulse_api.models.add_organization_data_campaign_request.AddOrganizationDataCampaignRequest,
	**kwargs
) ‑> edgeimpulse_api.models.add_organization_data_campaign_response.AddOrganizationDataCampaignResponse
```

Add a data campaign

Add a new data campaign to a data campaign dashboard

| Parameters                               |                                                                                                                     |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                                   | ` `                                                                                                                 |
| `organization_id`                        | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `add_organization_data_campaign_request` | `edgeimpulse_api.models.add_organization_data_campaign_request.AddOrganizationDataCampaignRequest`                  |
| `**kwargs`                               | ` `                                                                                                                 |

| Returns                                                                                              |
| ---------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.add_organization_data_campaign_response.AddOrganizationDataCampaignResponse` |

#### add\_organization\_data\_campaign\_dashboard

```python  theme={"system"}
edgeimpulse_api.api.organization_data_campaigns_api.OrganizationDataCampaignsApi.add_organization_data_campaign_dashboard(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	add_organization_data_campaign_dashboard_request: edgeimpulse_api.models.add_organization_data_campaign_dashboard_request.AddOrganizationDataCampaignDashboardRequest,
	**kwargs
) ‑> edgeimpulse_api.models.add_organization_data_campaign_dashboard_response.AddOrganizationDataCampaignDashboardResponse
```

Add data campaign dashboard

Add a new data campaign dashboard

| Parameters                                         |                                                                                                                       |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `self`                                             | ` `                                                                                                                   |
| `organization_id`                                  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`   |
| `add_organization_data_campaign_dashboard_request` | `edgeimpulse_api.models.add_organization_data_campaign_dashboard_request.AddOrganizationDataCampaignDashboardRequest` |
| `**kwargs`                                         | ` `                                                                                                                   |

| Returns                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.add_organization_data_campaign_dashboard_response.AddOrganizationDataCampaignDashboardResponse` |

#### delete\_organization\_data\_campaign

```python  theme={"system"}
edgeimpulse_api.api.organization_data_campaigns_api.OrganizationDataCampaignsApi.delete_organization_data_campaign(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	campaign_id: Annotated[int, Strict(strict=True)],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Delete data campaign

Delete a data campaign

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `campaign_id`     | `Annotated[int, Strict(strict=True)]`                                                                               |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### delete\_organization\_data\_campaign\_dashboard

```python  theme={"system"}
edgeimpulse_api.api.organization_data_campaigns_api.OrganizationDataCampaignsApi.delete_organization_data_campaign_dashboard(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	campaign_dashboard_id: Annotated[int, Strict(strict=True)],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Delete data campaign dashboard

Delete a data campaign dashboard

| Parameters              |                                                                                                                     |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                                 |
| `organization_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `campaign_dashboard_id` | `Annotated[int, Strict(strict=True)]`                                                                               |
| `**kwargs`              | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### get\_organization\_data\_campaign

```python  theme={"system"}
edgeimpulse_api.api.organization_data_campaigns_api.OrganizationDataCampaignsApi.get_organization_data_campaign(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	campaign_id: Annotated[int, Strict(strict=True)],
	**kwargs
) ‑> edgeimpulse_api.models.get_organization_data_campaign_response.GetOrganizationDataCampaignResponse
```

Get data campaign

Get a data campaign

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `campaign_id`     | `Annotated[int, Strict(strict=True)]`                                                                               |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                                                              |
| ---------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_organization_data_campaign_response.GetOrganizationDataCampaignResponse` |

#### get\_organization\_data\_campaign\_dashboard

```python  theme={"system"}
edgeimpulse_api.api.organization_data_campaigns_api.OrganizationDataCampaignsApi.get_organization_data_campaign_dashboard(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	campaign_dashboard_id: Annotated[int, Strict(strict=True)],
	**kwargs
) ‑> edgeimpulse_api.models.get_organization_data_campaign_dashboard_response.GetOrganizationDataCampaignDashboardResponse
```

Get data campaign dashboard

Get a data campaign dashboard

| Parameters              |                                                                                                                     |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                                 |
| `organization_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `campaign_dashboard_id` | `Annotated[int, Strict(strict=True)]`                                                                               |
| `**kwargs`              | ` `                                                                                                                 |

| Returns                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_organization_data_campaign_dashboard_response.GetOrganizationDataCampaignDashboardResponse` |

#### get\_organization\_data\_campaign\_dashboards

```python  theme={"system"}
edgeimpulse_api.api.organization_data_campaigns_api.OrganizationDataCampaignsApi.get_organization_data_campaign_dashboards(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	**kwargs
) ‑> edgeimpulse_api.models.get_organization_data_campaign_dashboards_response.GetOrganizationDataCampaignDashboardsResponse
```

Get data campaign dashboards

List all data campaign dashboards

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_organization_data_campaign_dashboards_response.GetOrganizationDataCampaignDashboardsResponse` |

#### get\_organization\_data\_campaign\_diff

```python  theme={"system"}
edgeimpulse_api.api.organization_data_campaigns_api.OrganizationDataCampaignsApi.get_organization_data_campaign_diff(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	campaign_id: Annotated[int, Strict(strict=True)],
	organization_data_campaign_diff_request: edgeimpulse_api.models.organization_data_campaign_diff_request.OrganizationDataCampaignDiffRequest,
	**kwargs
) ‑> edgeimpulse_api.models.organization_data_campaign_diff_response.OrganizationDataCampaignDiffResponse
```

Get diff for data campaign

Get which items have changed for a data campaign. You post the data points and we'll return which data items are different in the past day.

| Parameters                                |                                                                                                                     |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                                    | ` `                                                                                                                 |
| `organization_id`                         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `campaign_id`                             | `Annotated[int, Strict(strict=True)]`                                                                               |
| `organization_data_campaign_diff_request` | `edgeimpulse_api.models.organization_data_campaign_diff_request.OrganizationDataCampaignDiffRequest`                |
| `**kwargs`                                | ` `                                                                                                                 |

| Returns                                                                                                |
| ------------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.organization_data_campaign_diff_response.OrganizationDataCampaignDiffResponse` |

#### get\_organization\_data\_campaigns\_for\_dashboard

```python  theme={"system"}
edgeimpulse_api.api.organization_data_campaigns_api.OrganizationDataCampaignsApi.get_organization_data_campaigns_for_dashboard(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	campaign_dashboard_id: Annotated[int, Strict(strict=True)],
	**kwargs
) ‑> edgeimpulse_api.models.get_organization_data_campaigns_response.GetOrganizationDataCampaignsResponse
```

Get data campaigns

Get a list of all data campaigns for a dashboard

| Parameters              |                                                                                                                     |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                                 |
| `organization_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `campaign_dashboard_id` | `Annotated[int, Strict(strict=True)]`                                                                               |
| `**kwargs`              | ` `                                                                                                                 |

| Returns                                                                                                |
| ------------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.get_organization_data_campaigns_response.GetOrganizationDataCampaignsResponse` |

#### update\_organization\_data\_campaign

```python  theme={"system"}
edgeimpulse_api.api.organization_data_campaigns_api.OrganizationDataCampaignsApi.update_organization_data_campaign(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	campaign_id: Annotated[int, Strict(strict=True)],
	update_organization_data_campaign_request: edgeimpulse_api.models.update_organization_data_campaign_request.UpdateOrganizationDataCampaignRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Update data campaign

Update a data campaign

| Parameters                                  |                                                                                                                     |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                                      | ` `                                                                                                                 |
| `organization_id`                           | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `campaign_id`                               | `Annotated[int, Strict(strict=True)]`                                                                               |
| `update_organization_data_campaign_request` | `edgeimpulse_api.models.update_organization_data_campaign_request.UpdateOrganizationDataCampaignRequest`            |
| `**kwargs`                                  | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### update\_organization\_data\_campaign\_dashboard

```python  theme={"system"}
edgeimpulse_api.api.organization_data_campaigns_api.OrganizationDataCampaignsApi.update_organization_data_campaign_dashboard(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	campaign_dashboard_id: Annotated[int, Strict(strict=True)],
	update_organization_data_campaign_dashboard_request: edgeimpulse_api.models.update_organization_data_campaign_dashboard_request.UpdateOrganizationDataCampaignDashboardRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Update data campaign dashboard

Update a data campaign dashboard

| Parameters                                            |                                                                                                                             |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `self`                                                | ` `                                                                                                                         |
| `organization_id`                                     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`         |
| `campaign_dashboard_id`                               | `Annotated[int, Strict(strict=True)]`                                                                                       |
| `update_organization_data_campaign_dashboard_request` | `edgeimpulse_api.models.update_organization_data_campaign_dashboard_request.UpdateOrganizationDataCampaignDashboardRequest` |
| `**kwargs`                                            | ` `                                                                                                                         |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |


Built with [Mintlify](https://mintlify.com).