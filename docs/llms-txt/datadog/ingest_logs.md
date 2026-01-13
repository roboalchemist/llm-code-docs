# Source: https://docs.datadoghq.com/cloudprem/ingest_logs.md

---
title: Set up Log Ingestion
description: Configure log sources to send data to your CloudPrem deployment
breadcrumbs: Docs > CloudPrem > Set up Log Ingestion
source_url: https://docs.datadoghq.com/ingest_logs/index.html
---

# Set up Log Ingestion

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

After installing and configuring CloudPrem, you need to set up log ingestion to start sending log data from your applications and infrastructure. CloudPrem supports multiple ingestion methods to accommodate different architectures and requirements.

## Log ingestion methods{% #log-ingestion-methods %}

- [Datadog Agent](https://docs.datadoghq.com/cloudprem/ingest_logs/datadog_agent/)
- [Observability Pipelines](https://docs.datadoghq.com/cloudprem/ingest_logs/observability_pipelines/)
- [REST API Integration](https://docs.datadoghq.com/cloudprem/ingest_logs/rest_api/)
