# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.networksecurity_gateway_security_policy.dataset.md

---
title: GatewaySecurityPolicy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > GatewaySecurityPolicy
---

# GatewaySecurityPolicy

GatewaySecurityPolicy is a Google Cloud resource used to define and manage security policies for network gateways. It allows administrators to create rules that control and filter traffic at the edge of the network, providing protection against threats and enforcing access controls. This resource is typically used with Google Cloud Armor or other gateway-based security services to ensure consistent and centralized policy enforcement across applications and services.

```
gcp.networksecurity_gateway_security_policy
```

## Fields

| Title                 | ID   | Type          | Data Type                                                                                                                                                                                                                           | Description |
| --------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string        |
| ancestors             | core | array<string> |
| create_time           | core | timestamp     | Output only. The timestamp when the resource was created.                                                                                                                                                                           |
| datadog_display_name  | core | string        |
| description           | core | string        | Optional. Free-text description of the resource.                                                                                                                                                                                    |
| labels                | core | array<string> |
| name                  | core | string        | Required. Name of the resource. Name is of the form projects/{project}/locations/{location}/gatewaySecurityPolicies/{gateway_security_policy} gateway_security_policy should match the pattern:(^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$). |
| organization_id       | core | string        |
| parent                | core | string        |
| project_id            | core | string        |
| project_number        | core | string        |
| region_id             | core | string        |
| resource_name         | core | string        |
| tags                  | core | hstore_csv    |
| tls_inspection_policy | core | string        | Optional. Name of a TLS Inspection Policy resource that defines how TLS inspection will be performed for any rule(s) which enables it.                                                                                              |
| update_time           | core | timestamp     | Output only. The timestamp when the resource was updated.                                                                                                                                                                           |
| zone_id               | core | string        |
