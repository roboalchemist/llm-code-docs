# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.cloudbilling_project_billing_info.dataset.md

---
title: ProjectBillingInfo
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > ProjectBillingInfo
---

# ProjectBillingInfo

ProjectBillingInfo represents the billing configuration for a Google Cloud project. It contains information about which billing account is linked to the project and whether the project is currently billed. This resource helps manage and track billing relationships, ensuring that usage costs are correctly associated with the appropriate billing account.

```
gcp.cloudbilling_project_billing_info
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                      | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| billing_account_name | core | string        | The resource name of the billing account associated with the project, if any. For example, `billingAccounts/012345-567890-ABCDEF`.                                                                                                                             |
| billing_enabled      | core | bool          | Output only. True if the project is associated with an open billing account, to which usage on the project is charged. False if the project is associated with a closed billing account, or no billing account at all, and therefore cannot use paid services. |
| datadog_display_name | core | string        |
| labels               | core | array<string> |
| name                 | core | string        | Output only. The resource name for the `ProjectBillingInfo`; has the form `projects/{project_id}/billingInfo`. For example, the resource name for the billing information for project `tokyo-rain-123` would be `projects/tokyo-rain-123/billingInfo`.         |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        | Output only. The ID of the project that this `ProjectBillingInfo` represents, such as `tokyo-rain-123`. This is a convenience field so that you don't need to parse the `name` field to obtain a project ID.                                                   |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
