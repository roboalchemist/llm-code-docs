# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.k8s_validating_webhook_configuration.dataset.md

---
title: K8s Validating Webhook Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > K8s Validating Webhook Configuration
---

# K8s Validating Webhook Configuration

This table represents the k8s_validating_webhook_configuration resource from Google Cloud Platform.

```
gcp.k8s_validating_webhook_configuration
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                          | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| api_version          | core | string        | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  |
| datadog_display_name | core | string        |
| kind                 | core | string        | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| labels               | core | array<string> |
| metadata             | core | json          | Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata.                                                                                                                                                                 |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| webhooks             | core | json          | Webhooks is a list of webhooks and the affected resources and operations.                                                                                                                                                                                                                          |
| zone_id              | core | string        |
