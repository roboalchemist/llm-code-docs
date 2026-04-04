# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.servicenetworking_connection.dataset.md

---
title: Service Networking Connection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Service Networking Connection
---

# Service Networking Connection

A Service Networking Connection in Google Cloud enables private communication between a Virtual Private Cloud (VPC) network and Google services or managed service producers. It allows resources in a VPC to connect securely using internal IP addresses without traversing the public internet. This setup is commonly used for services like Cloud SQL, Memorystore, and other managed offerings that require private access.

```
gcp.servicenetworking_connection
```

## Fields

| Title                   | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description |
| ----------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string        |
| ancestors               | core | array<string> |
| datadog_display_name    | core | string        |
| labels                  | core | array<string> |
| network                 | core | string        | Required. The name of service consumer's VPC network that's connected with service producer network, in the following format: `projects/{project}/global/networks/{network}`. `{project}` is a project number, such as in `12345` that includes the VPC service consumer's VPC network. `{network}` is the name of the service consumer's VPC network.                                                                                                                              |
| organization_id         | core | string        |
| parent                  | core | string        |
| peering                 | core | string        | Output only. The name of the VPC Network Peering connection that was created by the service producer.                                                                                                                                                                                                                                                                                                                                                                               |
| project_id              | core | string        |
| project_number          | core | string        |
| region_id               | core | string        |
| reserved_peering_ranges | core | array<string> | The name of one or more allocated IP address ranges for this service producer of type `PEERING`. Note that invoking CreateConnection method with a different range when connection is already established will not modify already provisioned service producer subnetworks. If CreateConnection method is invoked repeatedly to reconnect when peering connection had been disconnected on the consumer side, leaving this field empty will restore previously allocated IP ranges. |
| resource_name           | core | string        |
| service                 | core | string        | Output only. The name of the peering service that's associated with this connection, in the following format: `services/{service name}`.                                                                                                                                                                                                                                                                                                                                            |
| tags                    | core | hstore_csv    |
| zone_id                 | core | string        |
