# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.vmwareengine_external_address.dataset.md

---
title: External Address
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > External Address
---

# External Address

An External Address in Google Cloud is a static or ephemeral IP address that can be assigned to resources such as virtual machine instances, load balancers, or VPN gateways. It allows these resources to be accessible from the public internet. External addresses can be either IPv4 or IPv6 and are managed within a specific region or globally, depending on the resource type.

```
gcp.vmwareengine_external_address
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                     | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. Creation time of this resource.                                                                                                                                                                                                                                                                  |
| datadog_display_name | core | string        |
| description          | core | string        | User-provided description for this resource.                                                                                                                                                                                                                                                                  |
| external_ip          | core | string        | Output only. The external IP address of a workload VM.                                                                                                                                                                                                                                                        |
| internal_ip          | core | string        | The internal IP address of a workload VM.                                                                                                                                                                                                                                                                     |
| labels               | core | array<string> |
| name                 | core | string        | Output only. Identifier. The resource name of this external IP address. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/externalAddresses/my-address` |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | string        | Output only. The state of the resource.                                                                                                                                                                                                                                                                       |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. System-generated unique identifier for the resource.                                                                                                                                                                                                                                             |
| update_time          | core | timestamp     | Output only. Last update time of this resource.                                                                                                                                                                                                                                                               |
| zone_id              | core | string        |
