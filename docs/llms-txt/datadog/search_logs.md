# Source: https://docs.datadoghq.com/cloudprem/operate/search_logs.md

---
title: Search CloudPrem Logs
description: Learn how to query and analyze your CloudPrem logs in Datadog
breadcrumbs: Docs > CloudPrem > Operate CloudPrem > Search CloudPrem Logs
---

# Search CloudPrem Logs

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

## Explore CloudPrem logs in the Logs Explorer{% #explore-cloudprem-logs-in-the-logs-explorer %}

1. Go to the Datadog Log Explorer.
1. On the left facet panel, select the checkbox for your index under CLOUDPREM INDEXES.

A CloudPrem index name is built with the following rule:

```
index:cloudprem-<CLUSTER_NAME>
```

## Search limitations{% #search-limitations %}

You cannot query CloudPrem clusters alongside other Datadog log indexes. Additionally, Flex Logs are not supported with CloudPrem.

## Further reading{% #further-reading %}

- [Ingest logs to CloudPrem](https://docs.datadoghq.com/cloudprem/ingest/)
- [Troubleshooting CloudPrem](https://docs.datadoghq.com/cloudprem/operate/troubleshooting/)
- [Log Search Syntax](https://docs.datadoghq.com/logs/explorer/search_syntax/)
