# Source: https://docs.datadoghq.com/cloudprem/configure/datadog_account.md

---
title: Access and Search CloudPrem logs
description: Set up your Datadog account to access CloudPrem logs
breadcrumbs: Docs > CloudPrem > Configure CloudPrem > Access and Search CloudPrem logs
source_url: https://docs.datadoghq.com/configure/datadog_account/index.html
---

# Access and Search CloudPrem logs

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

After deploying your CloudPrem environment, you need to connect it to your Datadog account to search and analyze logs through the Datadog UI. This guide shows you how to enable log search for your CloudPrem cluster and start querying your self-hosted logs alongside your other Datadog workflows.

## Enabling CloudPrem log search{% #enabling-cloudprem-log-search %}

To search CloudPrem logs in the Datadog UI, contact [Datadog support](https://docs.datadoghq.com/help/) and provide the **public DNS** of your CloudPrem cluster. This links your cluster to your Datadog account.

## Searching your CloudPrem logs in the Logs Explorer{% #searching-your-cloudprem-logs-in-the-logs-explorer %}

After your Datadog account is set up, you can search for your CloudPrem cluster in the Logs Explorer by selecting it from the available facets or by entering a query in the search bar.

```
index:cloudprem-<CLUSTER_NAME>
```

## Search limitations{% #search-limitations %}

You cannot query CloudPrem clusters alongside other Datadog log indexes. Additionally, Flex Logs are not supported with CloudPrem.

## Further reading{% #further-reading %}

- [Set up log ingestion with Datadog Agent](https://docs.datadoghq.com/cloudprem/ingest_logs/datadog_agent/)
- [Configure CloudPrem Ingress](https://docs.datadoghq.com/cloudprem/configure/ingress/)
- [Manage and Monitor CloudPrem](https://docs.datadoghq.com/cloudprem/manage/)
