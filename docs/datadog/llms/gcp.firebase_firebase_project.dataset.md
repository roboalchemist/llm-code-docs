# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.firebase_firebase_project.dataset.md

---
title: Firebase Firebase Project
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Firebase Firebase Project
---

# Firebase Firebase Project

This table represents the firebase_firebase_project resource from Google Cloud Platform.

```
gcp.firebase_firebase_project
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| annotations          | core | hstore        | A set of user-defined annotations for the FirebaseProject. Learn more about annotations in Google's [AIP-128 standard](https://google.aip.dev/128#annotations). These annotations are intended solely for developers and client-side tools. Firebase services will not mutate this annotations set.                                                                                                                                                                                  |
| datadog_display_name | core | string        |
| etag                 | core | string        | This checksum is computed by the server based on the value of other fields, and it may be sent with update requests to ensure the client has an up-to-date value before proceeding. Learn more about `etag` in Google's [AIP-154 standard](https://google.aip.dev/154#declarative-friendly-resources). This etag is strongly validated.                                                                                                                                              |
| gcp_display_name     | core | string        | The user-assigned display name of the Project.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| labels               | core | array<string> |
| name                 | core | string        | The resource name of the Project, in the format: projects/PROJECT_IDENTIFIER PROJECT_IDENTIFIER: the Project's [`ProjectNumber`](../projects#FirebaseProject.FIELDS.project_number) ***(recommended)*** or its [`ProjectId`](../projects#FirebaseProject.FIELDS.project_id). Learn more about using project identifiers in Google's [AIP 2510 standard](https://google.aip.dev/cloud/2510). Note that the value for PROJECT_IDENTIFIER in any response body will be the `ProjectId`. |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| resources            | core | json          | Output only. **DEPRECATED.** _Auto-provisioning of these resources is changing, so this object no longer reliably provides information about the Project. Instead, retrieve information about each resource directly from its resource-specific API._ The default Firebase resources associated with the Project.                                                                                                                                                                    |
| state                | core | string        | Output only. The lifecycle state of the Project. Possible values: ['STATE_UNSPECIFIED', 'ACTIVE', 'DELETED']. Values descriptions: ['Unspecified state.', 'The Project is active.', 'The Project has been soft-deleted.']                                                                                                                                                                                                                                                            |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
