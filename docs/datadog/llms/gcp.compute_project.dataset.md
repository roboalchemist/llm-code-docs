# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.compute_project.dataset.md

---
title: Project
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Project
---

# Project

A GCP Project is the primary container for organizing and managing Google Cloud resources. It provides an isolated environment with its own settings, permissions, billing, and quotas. Each project has a unique ID and is used to group related services, APIs, and workloads, making it easier to manage access control and track costs.

```
gcp.compute_project
```

## Fields

| Title                    | ID   | Type          | Data Type                                                                                                                                                                                                 | Description |
| ------------------------ | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string        |
| ancestors                | core | array<string> |
| cloud_armor_tier         | core | string        | Output only. [Output Only] The Cloud Armor tier for this project. It can be one of the following values: CA_STANDARD,CA_ENTERPRISE_PAYGO. If this field is not specified, it is assumed to beCA_STANDARD. |
| common_instance_metadata | core | json          | Metadata key/value pairs available to all instances contained in this project. See Custom metadata for more information.                                                                                  |
| creation_timestamp       | core | timestamp     | [Output Only] Creation timestamp inRFC3339 text format.                                                                                                                                                   |
| datadog_display_name     | core | string        |
| default_network_tier     | core | string        | This signifies the default network tier used for configuring resources of the project and can only take the following values:PREMIUM, STANDARD. Initially the default network tier is PREMIUM.            |
| default_service_account  | core | string        | [Output Only] Default service account used by VMs running in this project.                                                                                                                                |
| description              | core | string        | An optional textual description of the resource.                                                                                                                                                          |
| enabled_features         | core | array<string> | An optional list of restricted features enabled for use on this project.                                                                                                                                  |
| id                       | core | string        | [Output Only] The unique identifier for the resource. This identifier is defined by the server. This is *not* the project ID, and is just a unique ID used by Compute Engine to identify resources.       |
| kind                     | core | string        | Output only. [Output Only] Type of the resource. Always compute#project for projects.                                                                                                                     |
| labels                   | core | array<string> |
| name                     | core | string        | The project ID. For example: my-example-project. Use the project ID to make requests to Compute Engine.                                                                                                   |
| organization_id          | core | string        |
| parent                   | core | string        |
| project_id               | core | string        |
| project_number           | core | string        |
| quotas                   | core | json          | [Output Only] Quotas assigned to this project.                                                                                                                                                            |
| region_id                | core | string        |
| resource_name            | core | string        |
| self_link                | core | string        | [Output Only] Server-defined URL for the resource.                                                                                                                                                        |
| tags                     | core | hstore_csv    |
| usage_export_location    | core | json          | An optional naming prefix for daily usage reports and the Google Cloud Storage bucket where they are stored.                                                                                              |
| vm_dns_setting           | core | string        | Output only. [Output Only] Default internal DNS setting used by VMs running in this project.                                                                                                              |
| xpn_project_status       | core | string        | [Output Only] The role this project has in a shared VPC configuration. Currently, only projects with the host role, which is specified by the value HOST, are differentiated.                             |
| zone_id                  | core | string        |
