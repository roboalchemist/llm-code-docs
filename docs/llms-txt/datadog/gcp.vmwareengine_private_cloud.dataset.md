# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.vmwareengine_private_cloud.dataset.md

---
title: VMware Engine Private Cloud
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > VMware Engine Private Cloud
---

# VMware Engine Private Cloud

VMware Engine Private Cloud on Google Cloud is a fully managed VMware environment that allows you to run native VMware workloads in Google Cloud. It provides dedicated infrastructure with vSphere, vCenter, vSAN, and NSX-T, enabling seamless migration of on-premises VMware environments without refactoring. It integrates with Google Cloud services for hybrid and multi-cloud operations.

```
gcp.vmwareengine_private_cloud
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                       | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. Creation time of this resource.                                                                                                                                                                                                                                                                    |
| datadog_display_name | core | string        |
| delete_time          | core | timestamp     | Output only. Time when the resource was scheduled for deletion.                                                                                                                                                                                                                                                 |
| description          | core | string        | User-provided description for this private cloud.                                                                                                                                                                                                                                                               |
| expire_time          | core | timestamp     | Output only. Time when the resource will be irreversibly deleted.                                                                                                                                                                                                                                               |
| hcx                  | core | json          | Output only. HCX appliance.                                                                                                                                                                                                                                                                                     |
| labels               | core | array<string> |
| management_cluster   | core | json          | Required. Input only. The management cluster for this private cloud. This field is required during creation of the private cloud to provide details for the default cluster. The following fields can't be changed after private cloud creation: `ManagementCluster.clusterId`, `ManagementCluster.nodeTypeId`. |
| name                 | core | string        | Output only. Identifier. The resource name of this private cloud. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`                                      |
| network_config       | core | json          | Required. Network configuration of the private cloud.                                                                                                                                                                                                                                                           |
| nsx                  | core | json          | Output only. NSX appliance.                                                                                                                                                                                                                                                                                     |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | string        | Output only. State of the resource. New values may be added to this enum when appropriate.                                                                                                                                                                                                                      |
| tags                 | core | hstore_csv    |
| type                 | core | string        | Optional. Type of the private cloud. Defaults to STANDARD.                                                                                                                                                                                                                                                      |
| uid                  | core | string        | Output only. System-generated unique identifier for the resource.                                                                                                                                                                                                                                               |
| update_time          | core | timestamp     | Output only. Last update time of this resource.                                                                                                                                                                                                                                                                 |
| vcenter              | core | json          | Output only. Vcenter appliance.                                                                                                                                                                                                                                                                                 |
| zone_id              | core | string        |
