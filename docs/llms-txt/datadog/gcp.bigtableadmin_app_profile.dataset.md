# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.bigtableadmin_app_profile.dataset.md

---
title: App Profile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > App Profile
---

# App Profile

An App Profile in Google Cloud is a configuration for a Cloud Bigtable instance that defines how requests are routed to clusters. It allows you to control aspects such as multi-cluster routing, failover behavior, and application isolation. By using different app profiles, you can optimize performance, availability, and workload management for various applications accessing the same Bigtable instance.

```
gcp.bigtableadmin_app_profile
```

## Fields

| Title                          | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description |
| ------------------------------ | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                           | core | string        |
| ancestors                      | core | array<string> |
| data_boost_isolation_read_only | core | json          | Specifies that this app profile is intended for read-only usage via the Data Boost feature.                                                                                                                                                                                                                                                                                                                                                           |
| datadog_display_name           | core | string        |
| description                    | core | string        | Long form description of the use case for this AppProfile.                                                                                                                                                                                                                                                                                                                                                                                            |
| etag                           | core | string        | Strongly validated etag for optimistic concurrency control. Preserve the value returned from `GetAppProfile` when calling `UpdateAppProfile` to fail the request if there has been a modification in the mean time. The `update_mask` of the request need not include `etag` for this protection to apply. See [Wikipedia](https://en.wikipedia.org/wiki/HTTP_ETag) and [RFC 7232](https://tools.ietf.org/html/rfc7232#section-2.3) for more details. |
| labels                         | core | array<string> |
| multi_cluster_routing_use_any  | core | json          | Use a multi-cluster routing policy.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| name                           | core | string        | The unique name of the app profile, up to 50 characters long. Values are of the form `projects/{project}/instances/{instance}/appProfiles/_a-zA-Z0-9*`.                                                                                                                                                                                                                                                                                               |
| organization_id                | core | string        |
| parent                         | core | string        |
| priority                       | core | string        | This field has been deprecated in favor of `standard_isolation.priority`. If you set this field, `standard_isolation.priority` will be set instead. The priority of requests sent using this app profile.                                                                                                                                                                                                                                             |
| project_id                     | core | string        |
| project_number                 | core | string        |
| region_id                      | core | string        |
| resource_name                  | core | string        |
| single_cluster_routing         | core | json          | Use a single-cluster routing policy.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| standard_isolation             | core | json          | The standard options used for isolating this app profile's traffic from other use cases.                                                                                                                                                                                                                                                                                                                                                              |
| tags                           | core | hstore_csv    |
| zone_id                        | core | string        |
