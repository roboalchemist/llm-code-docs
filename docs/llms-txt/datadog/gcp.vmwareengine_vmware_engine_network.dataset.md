# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.vmwareengine_vmware_engine_network.dataset.md

---
title: Vmwareengine Vmware Engine Network
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Vmwareengine Vmware Engine Network
---

# Vmwareengine Vmware Engine Network

This table represents the vmwareengine_vmware_engine_network resource from Google Cloud Platform.

```
gcp.vmwareengine_vmware_engine_network
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                           | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. Creation time of this resource.                                                                                                                                                                                                                                                                                                                                                                                        |
| datadog_display_name | core | string        |
| description          | core | string        | User-provided description for this VMware Engine network.                                                                                                                                                                                                                                                                                                                                                                           |
| etag                 | core | string        | Checksum that may be sent on update and delete requests to ensure that the user-provided value is up to date before the server processes a request. The server computes checksums based on the value of other fields in the request.                                                                                                                                                                                                |
| labels               | core | array<string> |
| name                 | core | string        | Output only. Identifier. The resource name of the VMware Engine network. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/global/vmwareEngineNetworks/my-network`                                                                                                                                                 |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | string        | Output only. State of the VMware Engine network. Possible values: ['STATE_UNSPECIFIED', 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING']. Values descriptions: ['The default value. This value is used if the state is omitted.', 'The VMware Engine network is being created.', 'The VMware Engine network is ready.', 'The VMware Engine network is being updated.', 'The VMware Engine network is being deleted.']                  |
| tags                 | core | hstore_csv    |
| type                 | core | string        | Required. VMware Engine network type. Possible values: ['TYPE_UNSPECIFIED', 'LEGACY', 'STANDARD']. Values descriptions: ['The default value. This value should never be used.', 'Network type used by private clouds created in projects without a network of type `STANDARD`. This network type is no longer used for new VMware Engine private cloud deployments.', 'Standard network type used for private cloud connectivity.'] |
| uid                  | core | string        | Output only. System-generated unique identifier for the resource.                                                                                                                                                                                                                                                                                                                                                                   |
| update_time          | core | timestamp     | Output only. Last update time of this resource.                                                                                                                                                                                                                                                                                                                                                                                     |
| vpc_networks         | core | json          | Output only. VMware Engine service VPC networks that provide connectivity from a private cloud to customer projects, the internet, and other Google Cloud services.                                                                                                                                                                                                                                                                 |
| zone_id              | core | string        |
