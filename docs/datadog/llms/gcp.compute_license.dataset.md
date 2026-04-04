# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.compute_license.dataset.md

---
title: Compute Engine License
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Compute Engine License
---

# Compute Engine License

A Compute Engine License in Google Cloud represents the licensing terms associated with a virtual machine image or operating system used in Compute Engine instances. It defines usage rights, pricing, and compliance details for the software running on the VM.

```
gcp.compute_license
```

## Fields

| Title                 | ID   | Type          | Data Type                                                                                                                                     | Description |
| --------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string        |
| ancestors             | core | array<string> |
| charges_use_fee       | core | bool          | [Output Only] Deprecated. This field no longer reflects whether a license charges a usage fee.                                                |
| creation_timestamp    | core | timestamp     | Output only. [Output Only] Creation timestamp inRFC3339 text format.                                                                          |
| datadog_display_name  | core | string        |
| description           | core | string        | An optional textual description of the resource; provided by the client when the resource is created.                                         |
| id                    | core | string        | [Output Only] The unique identifier for the resource. This identifier is defined by the server.                                               |
| kind                  | core | string        | Output only. [Output Only] Type of resource. Always compute#license for licenses.                                                             |
| labels                | core | array<string> |
| license_code          | core | int64         | [Output Only] The unique code used to attach this license to images, snapshots, and disks.                                                    |
| name                  | core | string        | Name of the resource. The name must be 1-63 characters long and comply withRFC1035.                                                           |
| organization_id       | core | string        |
| parent                | core | string        |
| project_id            | core | string        |
| project_number        | core | string        |
| region_id             | core | string        |
| resource_name         | core | string        |
| resource_requirements | core | json          | [Input Only] Deprecated.                                                                                                                      |
| self_link             | core | string        | Output only. [Output Only] Server-defined URL for the resource.                                                                               |
| tags                  | core | hstore_csv    |
| transferable          | core | bool          | If false, licenses will not be copied from the source resource when creating an image from a disk, disk from snapshot, or snapshot from disk. |
| zone_id               | core | string        |
