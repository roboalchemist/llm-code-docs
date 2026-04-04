# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.oracledatabase_cloud_vm_cluster.dataset.md

---
title: Oracle Database Cloud VM Cluster
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Oracle Database Cloud VM Cluster
---

# Oracle Database Cloud VM Cluster

This table represents the Oracle Database Cloud VM Cluster resource from Google Cloud Platform.

```
gcp.oracledatabase_cloud_vm_cluster
```

## Fields

| Title                  | ID   | Type          | Data Type                                                                                                                                                                                                                                                        | Description |
| ---------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string        |
| ancestors              | core | array<string> |
| backup_odb_subnet      | core | string        | Optional. The name of the backup OdbSubnet associated with the VM Cluster. Format: projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}                                                                                     |
| backup_subnet_cidr     | core | string        | Optional. CIDR range of the backup subnet.                                                                                                                                                                                                                       |
| cidr                   | core | string        | Optional. Network settings. CIDR to use for cluster IP allocation.                                                                                                                                                                                               |
| create_time            | core | timestamp     | Output only. The date and time that the VM cluster was created.                                                                                                                                                                                                  |
| datadog_display_name   | core | string        |
| exadata_infrastructure | core | string        | Required. The name of the Exadata Infrastructure resource on which VM cluster resource is created, in the following format: projects/{project}/locations/{region}/cloudExadataInfrastuctures/{cloud_extradata_infrastructure}                                    |
| gcp_display_name       | core | string        | Optional. User friendly name for this resource.                                                                                                                                                                                                                  |
| gcp_oracle_zone        | core | string        | Output only. The GCP Oracle zone where Oracle CloudVmCluster is hosted. This will be the same as the gcp_oracle_zone of the CloudExadataInfrastructure. Example: us-east4-b-r2.                                                                                  |
| identity_connector     | core | json          | Output only. The identity connector details which will allow OCI to securely access the resources in the customer project.                                                                                                                                       |
| labels                 | core | array<string> | Optional. Labels or tags associated with the VM Cluster.                                                                                                                                                                                                         |
| name                   | core | string        | Identifier. The name of the VM Cluster resource with the format: projects/{project}/locations/{region}/cloudVmClusters/{cloud_vm_cluster}                                                                                                                        |
| network                | core | string        | Optional. The name of the VPC network. Format: projects/{project}/global/networks/{network}                                                                                                                                                                      |
| odb_network            | core | string        | Optional. The name of the OdbNetwork associated with the VM Cluster. Format: projects/{project}/locations/{location}/odbNetworks/{odb_network} It is optional but if specified, this should match the parent ODBNetwork of the odb_subnet and backup_odb_subnet. |
| odb_subnet             | core | string        | Optional. The name of the OdbSubnet associated with the VM Cluster for IP allocation. Format: projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}                                                                          |
| organization_id        | core | string        |
| parent                 | core | string        |
| project_id             | core | string        |
| project_number         | core | string        |
| properties             | core | json          | Optional. Various properties of the VM Cluster.                                                                                                                                                                                                                  |
| region_id              | core | string        |
| resource_name          | core | string        |
| tags                   | core | hstore_csv    |
| zone_id                | core | string        |
