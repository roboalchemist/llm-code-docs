# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.apigateway_gateway.dataset.md

---
title: API Gateway Gateway
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > API Gateway Gateway
---

# API Gateway Gateway

API Gateway Gateway in Google Cloud is a fully managed service that allows you to create, secure, and monitor APIs at scale. It provides a central entry point for backend services, handling authentication, authorization, traffic management, and monitoring. This resource helps developers expose services to external or internal consumers with consistent security and performance, without needing to manage infrastructure.

```
gcp.apigateway_gateway
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                        | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| api_config           | core | string        | Required. Resource name of the API Config for this Gateway. Format: projects/{project}/locations/global/apis/{api}/configs/{apiConfig}                                           |
| create_time          | core | timestamp     | Output only. Created time.                                                                                                                                                       |
| datadog_display_name | core | string        |
| default_hostname     | core | string        | Output only. The default API Gateway host name of the form `{gateway_id}-{hash}.{region_code}.gateway.dev`.                                                                      |
| gcp_display_name     | core | string        | Optional. Display name.                                                                                                                                                          |
| labels               | core | array<string> | Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |
| name                 | core | string        | Output only. Resource name of the Gateway. Format: projects/{project}/locations/{location}/gateways/{gateway}                                                                    |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | string        | Output only. The current state of the Gateway.                                                                                                                                   |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. Updated time.                                                                                                                                                       |
| zone_id              | core | string        |
