# Source: https://docs.datadoghq.com/cloudprem/quickstart.md

---
title: CloudPrem Quickstart
description: Get started with CloudPrem locally in less than 5 minutes
breadcrumbs: Docs > CloudPrem > CloudPrem Quickstart
source_url: https://docs.datadoghq.com/quickstart/index.html
---

# CloudPrem Quickstart

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

This quickstart covers the following:

1. Start CloudPrem locally using Docker.
1. Verify the cluster status.
1. Send a "Hello World" log.
1. View the log in the Datadog Log Explorer.

## Prerequisites{% #prerequisites %}

- Ask for the [CloudPrem Preview](https://www.datadoghq.com/product-preview/cloudprem/).
- **Datadog API Key**: [Get your API key](https://docs.datadoghq.com/account_management/api-app-keys/#add-an-api-key-or-client-token).
- **Docker**: [Install Docker](https://docs.docker.com/get-docker/).

## Step 1: Start CloudPrem{% #step-1-start-cloudprem %}

Run the following command in your terminal to start a local CloudPrem instance. Replace `<YOUR_API_KEY>` with your actual Datadog API Key.

```shell
export DD_API_KEY="<YOUR_API_KEY>"
export DD_SITE="datadoghq.com"

docker run -d \
  --name cloudprem \
  -v $(pwd)/qwdata:/quickwit/qwdata \
  -e DD_SITE=${DD_SITE} \
  -e DD_API_KEY=${DD_API_KEY} \
  -p 127.0.0.1:7280:7280 \
  datadog/cloudprem run
```

## Step 2: Verify status in the CloudPrem console{% #step-2-verify-status-in-the-cloudprem-console %}

In Datadog, go to the [CloudPrem console](https://app.datadoghq.com/cloudprem) and check that your cluster is connected. You should see the `connected` status.

In the CloudPrem console, you can edit the cluster metadata and rename your cluster to `demo`.

{% image
   source="https://datadog-docs.imgix.net/images/cloudprem/quickstart/clouprem_console.084bf6182e8049547845870f10f8d793.png?auto=format"
   alt="Screenshot of the CloudPrem console showing the cluster connected status" /%}

## Step 3: Send a log{% #step-3-send-a-log %}

In your terminal, send a "Hello World" log entry directly to your local CloudPrem instance using the API:

```shell
curl -X POST "http://localhost:7280/api/v2/logs" \
  -H "Content-Type: application/json" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -d '[
    {
      "message": "Hello world from CloudPrem",
      "level": "info",
      "service": "demo"
    }
  ]'
```

## Step 4: Explore logs{% #step-4-explore-logs %}

1. Go to the [Datadog Log Explorer](https://app.datadoghq.com/logs?query=index=cloudprem-demo&storage=hot).
1. On the left facet panel, select the checkbox for your index under **CLOUDPREM INDEXES**.
1. You should see your "Hello world from CloudPrem" log entry.

{% image
   source="https://datadog-docs.imgix.net/images/cloudprem/quickstart/cloudprem_indexes.05edf04d925974e85153733dde70a8cb.png?auto=format"
   alt="The CloudPrem index selection in the Datadog Log Explorer" /%}

## Next steps{% #next-steps %}

With CloudPrem running, you can:

- [Send logs with the Datadog Agent](https://docs.datadoghq.com/cloudprem/ingest_logs/datadog_agent) to automatically collect logs from your containers.
- [Send logs with Observability Pipelines](https://docs.datadoghq.com/cloudprem/ingest_logs/observability_pipelines/).
