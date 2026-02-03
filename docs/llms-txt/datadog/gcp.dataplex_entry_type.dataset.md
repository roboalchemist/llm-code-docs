# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dataplex_entry_type.dataset.md

---
title: Dataplex Entry Type
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Dataplex Entry Type
---

# Dataplex Entry Type

Dataplex Entry Type in Google Cloud defines a custom metadata schema for data assets managed within Dataplex. It allows users to create structured metadata entries that describe data entities such as tables, files, or streams. This helps in organizing, discovering, and governing data across different storage systems by providing consistent metadata definitions and enabling advanced data cataloging and lineage tracking.

```
gcp.dataplex_entry_type
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                           | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| authorization        | core | json          | Immutable. Authorization defined for this type.                                                                                                                     |
| create_time          | core | timestamp     | Output only. The time when the EntryType was created.                                                                                                               |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. Description of the EntryType.                                                                                                                             |
| etag                 | core | string        | Optional. This checksum is computed by the service, and might be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| gcp_display_name     | core | string        | Optional. User friendly display name.                                                                                                                               |
| labels               | core | array<string> | Optional. User-defined labels for the EntryType.                                                                                                                    |
| name                 | core | string        | Output only. The relative resource name of the EntryType, of the form: projects/{project_number}/locations/{location_id}/entryTypes/{entry_type_id}.                |
| organization_id      | core | string        |
| parent               | core | string        |
| platform             | core | string        | Optional. The platform that Entries of this type belongs to.                                                                                                        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| required_aspects     | core | json          | AspectInfo for the entry type.                                                                                                                                      |
| resource_name        | core | string        |
| system               | core | string        | Optional. The system that Entries of this type belongs to. Examples include CloudSQL, MariaDB etc                                                                   |
| tags                 | core | hstore_csv    |
| type_aliases         | core | array<string> | Optional. Indicates the classes this Entry Type belongs to, for example, TABLE, DATABASE, MODEL.                                                                    |
| uid                  | core | string        | Output only. System generated globally unique ID for the EntryType. This ID will be different if the EntryType is deleted and re-created with the same name.        |
| update_time          | core | timestamp     | Output only. The time when the EntryType was last updated.                                                                                                          |
| zone_id              | core | string        |
