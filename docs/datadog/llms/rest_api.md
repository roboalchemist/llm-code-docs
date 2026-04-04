# Source: https://docs.datadoghq.com/cloudprem/ingest_logs/rest_api.md

---
title: Send logs to CloudPrem with REST API
description: Learn how to integrate with CloudPrem using direct API calls
breadcrumbs: Docs > CloudPrem > Set up Log Ingestion > Send logs to CloudPrem with REST API
source_url: https://docs.datadoghq.com/ingest_logs/rest_api/index.html
---

# Send logs to CloudPrem with REST API

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### CloudPrem is in Preview

Join the CloudPrem Preview to access new self-hosted log management features.

[Request Access](https://www.datadoghq.com/product-preview/cloudprem/)
{% /callout %}

## Overview{% #overview %}

You can send logs to CloudPrem using direct REST API calls. This method is useful for custom integrations or scripts that can't use a Datadog Agent or Observability Pipelines.

## Datadog Logs API{% #datadog-logs-api %}

**Endpoint**: `POST /api/v2/logs`**Content-Type**: `application/json`**Authentication**: Datadog API key

```shell
curl -X POST "http://<RELEASE_NAME>-indexer.<NAMESPACE_NAME>.svc.cluster.local:7280/api/v2/logs" \
  -H "Content-Type: application/json" \
  -H "DD-API-KEY: your-datadog-api-key" \
  -d '[
    {
      "message": "User login successful",
      "level": "info",
      "timestamp": "2024-01-15T10:30:00Z",
      "service": "auth-service",
      "host": "web-01",
      "tags": ["authentication", "success"]
    }
  ]'
```

## Further reading{% #further-reading %}

- [Datadog Agent Integration](https://docs.datadoghq.com/cloudprem/ingest_logs/datadog_agent/)
- [Observability Pipelines Integration](https://docs.datadoghq.com/cloudprem/ingest_logs/observability_pipelines/)
