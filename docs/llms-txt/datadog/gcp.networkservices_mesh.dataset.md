# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.networkservices_mesh.dataset.md

---
title: Service Mesh
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Service Mesh
---

# Service Mesh

Service Mesh in Google Cloud is a managed service that provides consistent networking, security, and observability for microservices. It simplifies service-to-service communication by handling traffic management, authentication, and monitoring without requiring changes to application code. It is built on open-source Istio and integrates with Google Kubernetes Engine and other GCP services to provide a unified control plane for managing service interactions securely and efficiently.

```
gcp.networkservices_mesh
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                             | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The timestamp when the resource was created.                                                                                                                                                                                                                                                                                                                             |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. A free-text description of the resource. Max length 1024 characters.                                                                                                                                                                                                                                                                                                        |
| envoy_headers        | core | string        | Optional. Determines if envoy will insert internal debug headers into upstream requests. Other Envoy headers may still be injected. By default, envoy will not insert any debug headers.                                                                                                                                                                                              |
| interception_port    | core | int64         | Optional. If set to a valid TCP port (1-65535), instructs the SIDECAR proxy to listen on the specified port of localhost (127.0.0.1) address. The SIDECAR proxy will expect all traffic to be redirected to this port regardless of its actual ip:port destination. If unset, a port '15001' is used as the interception port. This is applicable only for sidecar proxy deployments. |
| labels               | core | array<string> | Optional. Set of label tags associated with the Mesh resource.                                                                                                                                                                                                                                                                                                                        |
| name                 | core | string        | Identifier. Name of the Mesh resource. It matches pattern `projects/*/locations/*/meshes/`.                                                                                                                                                                                                                                                                                           |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| self_link            | core | string        | Output only. Server-defined URL of this resource                                                                                                                                                                                                                                                                                                                                      |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. The timestamp when the resource was updated.                                                                                                                                                                                                                                                                                                                             |
| zone_id              | core | string        |
