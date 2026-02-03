# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.networkservices_lb_traffic_extension.dataset.md

---
title: LB Traffic Extension
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > LB Traffic Extension
---

# LB Traffic Extension

LB Traffic Extension in Google Cloud Platform is a feature that enhances load balancer functionality by allowing custom traffic processing and routing logic. It enables users to extend the default behavior of Google Cloud Load Balancing with programmable extensions for traffic inspection, modification, or advanced routing decisions before requests reach backend services.

```
gcp.networkservices_lb_traffic_extension
```

## Fields

| Title                 | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                          | Description |
| --------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string        |
| ancestors             | core | array<string> |
| create_time           | core | timestamp     | Output only. The timestamp when the resource was created.                                                                                                                                                                                                                                                                                                                          |
| datadog_display_name  | core | string        |
| description           | core | string        | Optional. A human-readable description of the resource.                                                                                                                                                                                                                                                                                                                            |
| extension_chains      | core | json          | Required. A set of ordered extension chains that contain the match conditions and extensions to execute. Match conditions for each extension chain are evaluated in sequence for a given request. The first extension chain that has a condition that matches the request is executed. Any subsequent extension chains do not execute. Limited to 5 extension chains per resource. |
| forwarding_rules      | core | array<string> | Optional. A list of references to the forwarding rules to which this service extension is attached. At least one forwarding rule is required. Only one `LbTrafficExtension` resource can be associated with a forwarding rule.                                                                                                                                                     |
| labels                | core | array<string> | Optional. Set of labels associated with the `LbTrafficExtension` resource. The format must comply with [the requirements for labels](https://cloud.google.com/compute/docs/labeling-resources#requirements) for Google Cloud resources.                                                                                                                                            |
| load_balancing_scheme | core | string        | Required. All backend services and forwarding rules referenced by this extension must share the same load balancing scheme. Supported values: `INTERNAL_MANAGED` and `EXTERNAL_MANAGED`. For more information, refer to [Backend services overview](https://cloud.google.com/load-balancing/docs/backend-service).                                                                 |
| name                  | core | string        | Required. Identifier. Name of the `LbTrafficExtension` resource in the following format: `projects/{project}/locations/{location}/lbTrafficExtensions/{lb_traffic_extension}`.                                                                                                                                                                                                     |
| organization_id       | core | string        |
| parent                | core | string        |
| project_id            | core | string        |
| project_number        | core | string        |
| region_id             | core | string        |
| resource_name         | core | string        |
| tags                  | core | hstore_csv    |
| update_time           | core | timestamp     | Output only. The timestamp when the resource was updated.                                                                                                                                                                                                                                                                                                                          |
| zone_id               | core | string        |
