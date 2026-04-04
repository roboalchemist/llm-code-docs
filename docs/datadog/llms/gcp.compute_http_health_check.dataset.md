# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.compute_http_health_check.dataset.md

---
title: HTTP Health Check
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > HTTP Health Check
---

# HTTP Health Check

HTTP Health Check in Google Cloud Platform is used to monitor the health of instances in a load-balanced service. It periodically sends HTTP requests to specified endpoints and checks for valid responses. If an instance fails to respond correctly, it is marked as unhealthy and removed from traffic rotation until it recovers. This ensures high availability and reliability of applications.

```
gcp.compute_http_health_check
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| check_interval_sec   | core | int64         | How often (in seconds) to send a health check. The default value is5 seconds.                                                                                                                                                                                                                                                                                                                                                                       |
| creation_timestamp   | core | timestamp     | [Output Only] Creation timestamp inRFC3339 text format.                                                                                                                                                                                                                                                                                                                                                                                             |
| datadog_display_name | core | string        |
| description          | core | string        | An optional description of this resource. Provide this property when you create the resource.                                                                                                                                                                                                                                                                                                                                                       |
| healthy_threshold    | core | int64         | A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2.                                                                                                                                                                                                                                                                                                                                   |
| host                 | core | string        | The value of the host header in the HTTP health check request. If left empty (default value), the public IP on behalf of which this health check is performed will be used.                                                                                                                                                                                                                                                                         |
| id                   | core | string        | [Output Only] The unique identifier for the resource. This identifier is defined by the server.                                                                                                                                                                                                                                                                                                                                                     |
| kind                 | core | string        | Output only. [Output Only] Type of the resource. Alwayscompute#httpHealthCheck for HTTP health checks.                                                                                                                                                                                                                                                                                                                                              |
| labels               | core | array<string> |
| name                 | core | string        | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| organization_id      | core | string        |
| parent               | core | string        |
| port                 | core | int64         | The TCP port number for the HTTP health check request. The default value is80.                                                                                                                                                                                                                                                                                                                                                                      |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| request_path         | core | string        | The request path of the HTTP health check request. The default value is/. This field does not support query parameters. Must comply withRFC3986.                                                                                                                                                                                                                                                                                                    |
| resource_name        | core | string        |
| self_link            | core | string        | [Output Only] Server-defined URL for the resource.                                                                                                                                                                                                                                                                                                                                                                                                  |
| tags                 | core | hstore_csv    |
| timeout_sec          | core | int64         | How long (in seconds) to wait before claiming failure. The default value is5 seconds. It is invalid for timeoutSec to have greater value than checkIntervalSec.                                                                                                                                                                                                                                                                                     |
| unhealthy_threshold  | core | int64         | A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2.                                                                                                                                                                                                                                                                                                                                    |
| zone_id              | core | string        |
