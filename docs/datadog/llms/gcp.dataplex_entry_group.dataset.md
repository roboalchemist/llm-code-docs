# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dataplex_entry_group.dataset.md

---
title: Dataplex Entry Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Dataplex Entry Group
---

# Dataplex Entry Group

A Dataplex Entry Group in Google Cloud is a logical container used to organize and manage metadata entries within Dataplex. It helps group related data assets, such as tables, files, or streams, under a common context for easier discovery, governance, and policy enforcement. Entry Groups enable consistent metadata management across data lakes and warehouses.

```
gcp.dataplex_entry_group
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                      | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The time when the EntryGroup was created.                                                                                                         |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. Description of the EntryGroup.                                                                                                                       |
| etag                 | core | string        | This checksum is computed by the service, and might be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.      |
| gcp_display_name     | core | string        | Optional. User friendly display name.                                                                                                                          |
| labels               | core | array<string> | Optional. User-defined labels for the EntryGroup.                                                                                                              |
| name                 | core | string        | Output only. The relative resource name of the EntryGroup, in the format projects/{project_id_or_number}/locations/{location_id}/entryGroups/{entry_group_id}. |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| transfer_status      | core | string        | Output only. Denotes the transfer status of the Entry Group. It is unspecified for Entry Group created from Dataplex API.                                      |
| uid                  | core | string        | Output only. System generated globally unique ID for the EntryGroup. If you delete and recreate the EntryGroup with the same name, this ID will be different.  |
| update_time          | core | timestamp     | Output only. The time when the EntryGroup was last updated.                                                                                                    |
| zone_id              | core | string        |
