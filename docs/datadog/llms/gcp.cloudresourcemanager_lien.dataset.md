# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.cloudresourcemanager_lien.dataset.md

---
title: Lien
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Lien
---

# Lien

A Lien in Google Cloud is a restriction placed on a project or resource to prevent accidental deletion or modification. It ensures that critical resources, such as billing accounts or organizational policies, remain protected until the lien is explicitly removed. Liens are often used by administrators to enforce compliance and safeguard essential infrastructure.

```
gcp.cloudresourcemanager_lien
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                          | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | The creation time of this Lien.                                                                                                                                                                                                                                                                                    |
| datadog_display_name | core | string        |
| labels               | core | array<string> |
| name                 | core | string        | A system-generated unique identifier for this Lien. Example: `liens/1234abcd`                                                                                                                                                                                                                                      |
| organization_id      | core | string        |
| origin               | core | string        | A stable, user-visible/meaningful string identifying the origin of the Lien, intended to be inspected programmatically. Maximum length of 200 characters. Example: 'compute.googleapis.com'                                                                                                                        |
| parent               | core | string        | A reference to the resource this Lien is attached to. The server will validate the parent against those for which Liens are supported. Example: `projects/1234`                                                                                                                                                    |
| project_id           | core | string        |
| project_number       | core | string        |
| reason               | core | string        | Concise user-visible strings indicating why an action cannot be performed on a resource. Maximum length of 200 characters. Example: 'Holds production API key'                                                                                                                                                     |
| region_id            | core | string        |
| resource_name        | core | string        |
| restrictions         | core | array<string> | The types of operations which should be blocked as a result of this Lien. Each value should correspond to an IAM permission. The server will validate the permissions against those for which Liens are supported. An empty list is meaningless and will be rejected. Example: ['resourcemanager.projects.delete'] |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
