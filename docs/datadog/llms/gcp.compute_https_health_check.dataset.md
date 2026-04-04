# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.compute_https_health_check.dataset.md

---
title: HTTPs Health Check
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > HTTPs Health Check
---

# HTTPs Health Check

An HTTPS Health Check in Google Cloud Platform is used to monitor the health of backend services by sending HTTPS requests to specified endpoints. It verifies that instances respond correctly and within expected time limits. If a backend fails the health check, traffic is automatically redirected to healthy instances, ensuring high availability and reliability of applications.

```
gcp.compute_https_health_check
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| check_interval_sec   | core | int64         | How often (in seconds) to send a health check. The default value is 5 seconds.                                                                                                                                                                                                                                                                                                                                                                      |
| creation_timestamp   | core | timestamp     | [Output Only] Creation timestamp inRFC3339 text format.                                                                                                                                                                                                                                                                                                                                                                                             |
| datadog_display_name | core | string        |
| description          | core | string        | An optional description of this resource. Provide this property when you create the resource.                                                                                                                                                                                                                                                                                                                                                       |
| healthy_threshold    | core | int64         | A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2.                                                                                                                                                                                                                                                                                                                                   |
| host                 | core | string        | The value of the host header in the HTTPS health check request. If left empty (default value), the public IP on behalf of which this health check is performed will be used.                                                                                                                                                                                                                                                                        |
| id                   | core | string        | [Output Only] The unique identifier for the resource. This identifier is defined by the server.                                                                                                                                                                                                                                                                                                                                                     |
| kind                 | core | string        | Output only. Type of the resource.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| labels               | core | array<string> |
| name                 | core | string        | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| organization_id      | core | string        |
| parent               | core | string        |
| port                 | core | int64         | The TCP port number for the HTTPS health check request. The default value is 443.                                                                                                                                                                                                                                                                                                                                                                   |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| request_path         | core | string        | The request path of the HTTPS health check request. The default value is "/". Must comply withRFC3986.                                                                                                                                                                                                                                                                                                                                              |
| resource_name        | core | string        |
| self_link            | core | string        | [Output Only] Server-defined URL for the resource.                                                                                                                                                                                                                                                                                                                                                                                                  |
| tags                 | core | hstore_csv    |
| timeout_sec          | core | int64         | How long (in seconds) to wait before claiming failure. The default value is 5 seconds. It is invalid for timeoutSec to have a greater value than checkIntervalSec.                                                                                                                                                                                                                                                                                  |
| unhealthy_threshold  | core | int64         | A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2.                                                                                                                                                                                                                                                                                                                                    |
| zone_id              | core | string        |
