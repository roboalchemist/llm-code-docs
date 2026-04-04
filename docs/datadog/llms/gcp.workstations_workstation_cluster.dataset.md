# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.workstations_workstation_cluster.dataset.md

---
title: Workstation Cluster
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Workstation Cluster
---

# Workstation Cluster

A Workstation Cluster in Google Cloud is a managed environment for creating and managing multiple high-performance workstations. It provides centralized control, scalable compute resources, and secure access for developers, engineers, and data scientists. The cluster supports GPU and CPU configurations, enabling users to run demanding workloads such as software development, simulation, and machine learning in a collaborative and efficient setup.

```
gcp.workstations_workstation_cluster
```

## Fields

| Title                  | ID   | Type          | Data Type                                                                                                                                                                                                                                                    | Description |
| ---------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                   | core | string        |
| ancestors              | core | array<string> |
| annotations            | core | hstore        | Optional. Client-specified annotations.                                                                                                                                                                                                                      |
| conditions             | core | json          | Output only. Status conditions describing the workstation cluster's current state.                                                                                                                                                                           |
| control_plane_ip       | core | string        | Output only. The private IP address of the control plane for this workstation cluster. Workstation VMs need access to this IP address to work with the service, so make sure that your firewall rules allow egress from the workstation VMs to this address. |
| create_time            | core | timestamp     | Output only. Time when this workstation cluster was created.                                                                                                                                                                                                 |
| datadog_display_name   | core | string        |
| degraded               | core | bool          | Output only. Whether this workstation cluster is in degraded mode, in which case it may require user action to restore full functionality. The conditions field contains detailed information about the status of the cluster.                               |
| delete_time            | core | timestamp     | Output only. Time when this workstation cluster was soft-deleted.                                                                                                                                                                                            |
| domain_config          | core | json          | Optional. Configuration options for a custom domain.                                                                                                                                                                                                         |
| etag                   | core | string        | Optional. Checksum computed by the server. May be sent on update and delete requests to make sure that the client has an up-to-date value before proceeding.                                                                                                 |
| gateway_config         | core | json          | Optional. Configuration options for Cluster HTTP Gateway.                                                                                                                                                                                                    |
| gcp_display_name       | core | string        | Optional. Human-readable name for this workstation cluster.                                                                                                                                                                                                  |
| labels                 | core | array<string> | Optional. [Labels](https://cloud.google.com/workstations/docs/label-resources) that are applied to the workstation cluster and that are also propagated to the underlying Compute Engine resources.                                                          |
| name                   | core | string        | Identifier. Full name of this workstation cluster.                                                                                                                                                                                                           |
| network                | core | string        | Immutable. Name of the Compute Engine network in which instances associated with this workstation cluster will be created.                                                                                                                                   |
| organization_id        | core | string        |
| parent                 | core | string        |
| private_cluster_config | core | json          | Optional. Configuration for private workstation cluster.                                                                                                                                                                                                     |
| project_id             | core | string        |
| project_number         | core | string        |
| reconciling            | core | bool          | Output only. Indicates whether this workstation cluster is currently being updated to match its intended state.                                                                                                                                              |
| region_id              | core | string        |
| resource_name          | core | string        |
| subnetwork             | core | string        | Immutable. Name of the Compute Engine subnetwork in which instances associated with this workstation cluster will be created. Must be part of the subnetwork specified for this workstation cluster.                                                         |
| tags                   | core | hstore_csv    |
| uid                    | core | string        | Output only. A system-assigned unique identifier for this workstation cluster.                                                                                                                                                                               |
| update_time            | core | timestamp     | Output only. Time when this workstation cluster was most recently updated.                                                                                                                                                                                   |
| zone_id                | core | string        |
