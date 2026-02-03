# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.vmwareengine_network_policy.dataset.md

---
title: Network Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Network Policy
---

# Network Policy

A Network Policy in Google Cloud defines rules that control network traffic to and from Google Kubernetes Engine (GKE) pods. It allows you to specify which connections are allowed based on pod labels, namespaces, and ports. By applying network policies, you can enforce fine-grained security boundaries within your Kubernetes clusters, ensuring that only authorized communication occurs between workloads.

```
gcp.vmwareengine_network_policy
```

## Fields

| Title                           | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                | Description |
| ------------------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                            | core | string        |
| ancestors                       | core | array<string> |
| create_time                     | core | timestamp     | Output only. Creation time of this resource.                                                                                                                                                                                                                                                             |
| datadog_display_name            | core | string        |
| description                     | core | string        | Optional. User-provided description for this network policy.                                                                                                                                                                                                                                             |
| edge_services_cidr              | core | string        | Required. IP address range in CIDR notation used to create internet access and external IP access. An RFC 1918 CIDR block, with a "/26" prefix, is required. The range cannot overlap with any prefixes either in the consumer VPC network or in use by the private clouds attached to that VPC network. |
| external_ip                     | core | json          | Network service that allows External IP addresses to be assigned to VMware workloads. This service can only be enabled when `internet_access` is also enabled.                                                                                                                                           |
| internet_access                 | core | json          | Network service that allows VMware workloads to access the internet.                                                                                                                                                                                                                                     |
| labels                          | core | array<string> |
| name                            | core | string        | Output only. Identifier. The resource name of this network policy. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1/networkPolicies/my-network-policy`                     |
| organization_id                 | core | string        |
| parent                          | core | string        |
| project_id                      | core | string        |
| project_number                  | core | string        |
| region_id                       | core | string        |
| resource_name                   | core | string        |
| tags                            | core | hstore_csv    |
| uid                             | core | string        | Output only. System-generated unique identifier for the resource.                                                                                                                                                                                                                                        |
| update_time                     | core | timestamp     | Output only. Last update time of this resource.                                                                                                                                                                                                                                                          |
| vmware_engine_network           | core | string        | Optional. The relative resource name of the VMware Engine network. Specify the name in the following form: `projects/{project}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}` where `{project}` can either be a project number or a project ID.                                   |
| vmware_engine_network_canonical | core | string        | Output only. The canonical name of the VMware Engine network in the form: `projects/{project_number}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}`                                                                                                                               |
| zone_id                         | core | string        |
