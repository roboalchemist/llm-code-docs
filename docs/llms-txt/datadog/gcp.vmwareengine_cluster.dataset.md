# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.vmwareengine_cluster.dataset.md

---
title: VMware Engine Cluster
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > VMware Engine Cluster
---

# VMware Engine Cluster

VMware Engine Cluster in Google Cloud is a managed environment that allows you to run VMware workloads natively on Google Cloud infrastructure. It provides dedicated, high-performance nodes preconfigured with VMware vSphere, vSAN, and NSX-T, enabling seamless migration of on-premises VMware environments without refactoring. It integrates with Google Cloud services for networking, storage, and management.

```
gcp.vmwareengine_cluster
```

## Fields

| Title                    | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                | Description |
| ------------------------ | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string        |
| ancestors                | core | array<string> |
| autoscaling_settings     | core | json          | Optional. Configuration of the autoscaling applied to this cluster.                                                                                                                                                                                                                      |
| create_time              | core | timestamp     | Output only. Creation time of this resource.                                                                                                                                                                                                                                             |
| datadog_display_name     | core | string        |
| labels                   | core | array<string> |
| management               | core | bool          | Output only. True if the cluster is a management cluster; false otherwise. There can only be one management cluster in a private cloud and it has to be the first one.                                                                                                                   |
| name                     | core | string        | Output only. Identifier. The resource name of this cluster. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/clusters/my-cluster` |
| organization_id          | core | string        |
| parent                   | core | string        |
| project_id               | core | string        |
| project_number           | core | string        |
| region_id                | core | string        |
| resource_name            | core | string        |
| state                    | core | string        | Output only. State of the resource.                                                                                                                                                                                                                                                      |
| stretched_cluster_config | core | json          | Optional. Configuration of a stretched cluster. Required for clusters that belong to a STRETCHED private cloud.                                                                                                                                                                          |
| tags                     | core | hstore_csv    |
| uid                      | core | string        | Output only. System-generated unique identifier for the resource.                                                                                                                                                                                                                        |
| update_time              | core | timestamp     | Output only. Last update time of this resource.                                                                                                                                                                                                                                          |
| zone_id                  | core | string        |
