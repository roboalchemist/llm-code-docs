# Source: https://www.elastic.co/docs/manage-data/ingest

﻿---
title: Ingest: Bring your data to Elastic
description: Whether you call it adding, indexing, or ingesting data, you have to get the data into Elasticsearch before you can search it, visualize it, and use it...
url: https://www.elastic.co/docs/manage-data/ingest
products:
  - Elastic Cloud Hosted
  - Elastic Cloud Serverless
  - Elasticsearch
  - Kibana
applies_to:
  - Elastic Cloud Serverless: Generally available
  - Elastic Stack: Generally available
---

# Ingest: Bring your data to Elastic
Whether you call it *adding*, *indexing*, or *ingesting* data, you have to get the data into Elasticsearch before you can search it, visualize it, and use it for insights.
Our ingest tools are flexible, and support a wide range of scenarios. We can help you with everything from popular and straightforward use cases, all the way to advanced use cases that require additional processing to modify or reshape your data before it goes to Elasticsearch.
You can ingest:
- **General content** (data without timestamps), such as HTML pages, catalogs, and files
- **Time series (timestamped) data**, such as logs, metrics, and traces for Elastic Security, Observability, Search solutions, or for your own custom solutions


## Ingesting general content

Elastic offer tools designed to ingest specific types of general content. The content type determines the best ingest option.
- To index **documents** directly into Elasticsearch, use the Elasticsearch [document APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-document).
- To send **application data** directly to Elasticsearch, use an [Elasticsearch language client](https://www.elastic.co/docs/reference/elasticsearch-clients).
- To index **web page content**, use the Elastic [web crawler](https://www.elastic.co/web-crawler).
- To sync **data from third-party sources**, use [connectors](https://www.elastic.co/docs/reference/search-connectors). A connector syncs content from an original data source to an Elasticsearch index. Using connectors you can create *searchable*, read-only replicas of your data sources.
- To index **single files** for testing in a non-production environment, use the Kibana [file uploader](https://www.elastic.co/docs/manage-data/ingest/upload-data-files).

If you would like to try things out before you add your own data, try using our [sample data](https://www.elastic.co/docs/manage-data/ingest/sample-data).

## Ingesting time series data

<admonition title="What's the best approach for ingesting time series data?">
  The best approach for ingesting data is the *simplest option* that *meets your needs* and *satisfies your use case*.Usually, the *simplest option* for ingesting time series data is using Elastic Agent paired with an Elastic integration.
  - Install [Elastic Agent](https://www.elastic.co/docs/reference/fleet) on the computer(s) from which you want to collect data.
  - Add the [Elastic integration](https://docs.elastic.co/en/integrations) for the data source to your deployment.
  Integrations are available for many popular platforms and services, and are a good place to start for ingesting data into Elastic solutions—Observability, Security, and Search—or your own search application.Check out the [Integration quick reference](https://docs.elastic.co/en/integrations/all_integrations) to search for available integrations. If you don’t find an integration for your data source or if you need additional processing to extend the integration, we still have you covered. Refer to [Transform and enrich data](https://www.elastic.co/docs/manage-data/ingest/transform-enrich) to learn more.
</admonition>