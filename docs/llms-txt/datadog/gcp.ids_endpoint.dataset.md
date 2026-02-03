# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.ids_endpoint.dataset.md

---
title: Cloud IDS Endpoint
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cloud IDS Endpoint
---

# Cloud IDS Endpoint

Cloud IDS Endpoint is a managed intrusion detection service in Google Cloud that inspects network traffic for threats and vulnerabilities. It provides deep packet inspection and threat signature matching to detect malicious activity in real time. The service integrates with Virtual Private Cloud (VPC) networks, allowing organizations to monitor traffic between workloads and the internet or between internal segments. It helps enhance network security visibility without requiring complex infrastructure management.

```
gcp.ids_endpoint
```

## Fields

| Title                    | ID   | Type          | Data Type                                                                               | Description |
| ------------------------ | ---- | ------------- | --------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string        |
| ancestors                | core | array<string> |
| create_time              | core | timestamp     | Output only. The create time timestamp.                                                 |
| datadog_display_name     | core | string        |
| description              | core | string        | User-provided description of the endpoint                                               |
| endpoint_forwarding_rule | core | string        | Output only. The fully qualified URL of the endpoint's ILB Forwarding Rule.             |
| endpoint_ip              | core | string        | Output only. The IP address of the IDS Endpoint's ILB.                                  |
| labels                   | core | array<string> | The labels of the endpoint.                                                             |
| name                     | core | string        | Output only. The name of the endpoint.                                                  |
| network                  | core | string        | Required. The fully qualified URL of the network to which the IDS Endpoint is attached. |
| organization_id          | core | string        |
| parent                   | core | string        |
| project_id               | core | string        |
| project_number           | core | string        |
| region_id                | core | string        |
| resource_name            | core | string        |
| satisfies_pzi            | core | bool          | Output only. [Output Only] Reserved for future use.                                     |
| satisfies_pzs            | core | bool          | Output only. [Output Only] Reserved for future use.                                     |
| severity                 | core | string        | Required. Lowest threat severity that this endpoint will alert on.                      |
| state                    | core | string        | Output only. Current state of the endpoint.                                             |
| tags                     | core | hstore_csv    |
| threat_exceptions        | core | array<string> | List of threat IDs to be excepted from generating alerts.                               |
| traffic_logs             | core | bool          | Whether the endpoint should report traffic logs in addition to threat logs.             |
| update_time              | core | timestamp     | Output only. The update time timestamp.                                                 |
| zone_id                  | core | string        |
