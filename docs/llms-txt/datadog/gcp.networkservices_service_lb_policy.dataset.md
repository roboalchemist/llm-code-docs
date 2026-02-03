# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.networkservices_service_lb_policy.dataset.md

---
title: Service LB Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Service LB Policy
---

# Service LB Policy

Service LB Policy in Google Cloud defines how internal or external load balancers distribute traffic among backend services. It allows configuration of load balancing behavior, such as session affinity, connection draining, and failover settings. This policy helps optimize performance, reliability, and traffic management for services deployed across multiple regions or instances.

```
gcp.networkservices_service_lb_policy
```

## Fields

| Title                    | ID   | Type          | Data Type                                                                                                                                                  | Description |
| ------------------------ | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string        |
| ancestors                | core | array<string> |
| auto_capacity_drain      | core | json          | Optional. Configuration to automatically move traffic away for unhealthy IG/NEG for the associated Backend Service.                                        |
| create_time              | core | timestamp     | Output only. The timestamp when this resource was created.                                                                                                 |
| datadog_display_name     | core | string        |
| description              | core | string        | Optional. A free-text description of the resource. Max length 1024 characters.                                                                             |
| failover_config          | core | json          | Optional. Configuration related to health based failover.                                                                                                  |
| labels                   | core | array<string> | Optional. Set of label tags associated with the ServiceLbPolicy resource.                                                                                  |
| load_balancing_algorithm | core | string        | Optional. The type of load balancing algorithm to be used. The default behavior is WATERFALL_BY_REGION.                                                    |
| name                     | core | string        | Identifier. Name of the ServiceLbPolicy resource. It matches pattern `projects/{project}/locations/{location}/serviceLbPolicies/{service_lb_policy_name}`. |
| organization_id          | core | string        |
| parent                   | core | string        |
| project_id               | core | string        |
| project_number           | core | string        |
| region_id                | core | string        |
| resource_name            | core | string        |
| tags                     | core | hstore_csv    |
| update_time              | core | timestamp     | Output only. The timestamp when this resource was last updated.                                                                                            |
| zone_id                  | core | string        |
