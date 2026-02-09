# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.organization.dataset.md

---
title: Organization
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Organization
---

# Organization

This table represents the Organization resource from Google Cloud Platform.

```
gcp.organization
```

## Fields

| Title                 | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                     | Description |
| --------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string        |
| ancestors             | core | array<string> |
| create_time           | core | timestamp     | Output only. Timestamp when the Organization was created.                                                                                                                                                                                                                                                                     |
| datadog_display_name  | core | string        |
| delete_time           | core | timestamp     | Output only. Timestamp when the Organization was requested for deletion.                                                                                                                                                                                                                                                      |
| directory_customer_id | core | string        | Immutable. The G Suite / Workspace customer id used in the Directory API.                                                                                                                                                                                                                                                     |
| etag                  | core | string        | Output only. A checksum computed by the server based on the current value of the Organization resource. This may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.                                                                                                        |
| gcp_display_name      | core | string        | Output only. A human-readable string that refers to the organization in the Google Cloud Console. This string is set by the server and cannot be changed. The string will be set to the primary domain (for example, "google.com") of the Google Workspace customer that owns the organization.                               |
| labels                | core | array<string> |
| name                  | core | string        | Output only. The resource name of the organization. This is the organization's relative path in the API. Its format is "organizations/[organization_id]". For example, "organizations/1234".                                                                                                                                  |
| organization_id       | core | string        |
| parent                | core | string        |
| project_id            | core | string        |
| project_number        | core | string        |
| region_id             | core | string        |
| resource_name         | core | string        |
| state                 | core | string        | Output only. The organization's current lifecycle state. Possible values: ['STATE_UNSPECIFIED', 'ACTIVE', 'DELETE_REQUESTED']. Values descriptions: ['Unspecified state. This is only useful for distinguishing unset values.', 'The normal and active state.', 'The organization has been marked for deletion by the user.'] |
| tags                  | core | hstore_csv    |
| update_time           | core | timestamp     | Output only. Timestamp when the Organization was last modified.                                                                                                                                                                                                                                                               |
| zone_id               | core | string        |
