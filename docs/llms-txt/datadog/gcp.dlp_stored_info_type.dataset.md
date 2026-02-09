# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dlp_stored_info_type.dataset.md

---
title: StoredInfoType
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > StoredInfoType
---

# StoredInfoType

A StoredInfoType in Google Cloud is a reusable custom data type definition used by Cloud Data Loss Prevention (DLP). It allows users to define and store custom detectors, such as regular expressions, dictionaries, or stored patterns, that can be referenced across multiple DLP jobs or templates to identify sensitive information consistently.

```
gcp.dlp_stored_info_type
```

## Fields

| Title                | ID   | Type          | Data Type                                                                   | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| current_version      | core | json          | Current version of the stored info type.                                    |
| datadog_display_name | core | string        |
| labels               | core | array<string> |
| name                 | core | string        | Resource name.                                                              |
| organization_id      | core | string        |
| parent               | core | string        |
| pending_versions     | core | json          | Pending versions of the stored info type. Empty if no versions are pending. |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
