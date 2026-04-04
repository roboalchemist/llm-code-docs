# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.networkservices_tcp_route.dataset.md

---
title: TCPRoute
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > TCPRoute
---

# TCPRoute

TCPRoute is a Google Cloud resource used to define and manage routing rules for TCP traffic within the GKE Gateway API. It allows users to configure how incoming TCP connections are matched and directed to backend services based on parameters such as port numbers or destination addresses, enabling flexible and scalable traffic management for applications.

```
gcp.networkservices_tcp_route
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                  | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The timestamp when the resource was created.                                                                                                                                                                                                                  |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. A free-text description of the resource. Max length 1024 characters.                                                                                                                                                                                             |
| gateways             | core | array<string> | Optional. Gateways defines a list of gateways this TcpRoute is attached to, as one of the routing rules to route the requests served by the gateway. Each gateway reference should match the pattern: `projects/*/locations/*/gateways/`                                   |
| labels               | core | array<string> | Optional. Set of label tags associated with the TcpRoute resource.                                                                                                                                                                                                         |
| meshes               | core | array<string> | Optional. Meshes defines a list of meshes this TcpRoute is attached to, as one of the routing rules to route the requests served by the mesh. Each mesh reference should match the pattern: `projects/*/locations/*/meshes/` The attached Mesh should be of a type SIDECAR |
| name                 | core | string        | Identifier. Name of the TcpRoute resource. It matches pattern `projects/*/locations/*/tcpRoutes/tcp_route_name>`.                                                                                                                                                          |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| rules                | core | json          | Required. Rules that define how traffic is routed and handled. At least one RouteRule must be supplied. If there are multiple rules then the action taken will be the first rule to match.                                                                                 |
| self_link            | core | string        | Output only. Server-defined URL of this resource                                                                                                                                                                                                                           |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. The timestamp when the resource was updated.                                                                                                                                                                                                                  |
| zone_id              | core | string        |
