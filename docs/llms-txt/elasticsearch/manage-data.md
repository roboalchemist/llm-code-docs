# Source: https://www.elastic.co/docs/manage-data

﻿---
title: Manage data
description: Learn how to ingest, store, and manage data in Elasticsearch. Understand indices, mappings, text analysis, data lifecycle management, and data migration between clusters.
url: https://www.elastic.co/docs/manage-data
products:
  - Elastic Cloud Serverless
  - Elasticsearch
applies_to:
  - Elastic Cloud Serverless: Generally available
  - Elastic Stack: Generally available
---

# Manage data
Whether you're looking to build a fast and relevant search solution, monitor business-critical applications and infrastructure, monitor endpoint security data, or one of the [many other use cases Elastic supports](https://www.elastic.co/docs/get-started/introduction), you need to understand how to ingest and manage data stored in Elasticsearch.

## Learn how data is stored

The fundamental unit of storage in Elasticsearch, the index, is a collection of documents uniquely identified by a name or an alias. These documents go through a process called mapping, which defines how Elasticsearch stores and indexes a document and the fields it contains, and a process called text analysis in which Elasticsearch converts unstructured text into a structured format that's optimized for search.
**Learn more in [The Elasticsearch data store](https://www.elastic.co/docs/manage-data/data-store)**.

## Get data into Elasticsearch

Before you can start searching, visualizing, and pulling actionable insights from Elastic, you have to get your data into Elasticsearch.  Elastic offers a wide range of tools and methods for getting data into Elasticsearch. The best approach depends on the kind of data you're ingesting and your specific use case.
**Learn more in [Ingestion](https://www.elastic.co/docs/manage-data/ingest).**

## Manage data over time

After you've added data to Elasticsearch, you need to manage it over time. For example, you can specify that data be deleted after a retention period or store data in multiple tiers with different performance characteristics.
Strategies for managing data depend on the type of data and how you're using it. For example, with a collection of items you want to search, like a catalog of products, the value of the content remains relatively constant over time so you want to be able to retrieve items quickly regardless of how old they are. Whereas with a stream of continuously-generated timestamped data, such as log entries, the data keeps accumulating over time, so you need strategies for balancing the value of the data against the cost of storing it.
**Learn more in [Data lifecycle](https://www.elastic.co/docs/manage-data/lifecycle).**

## Migrate data between Elasticsearch clusters

If you move to new infrastructure, there are several options for moving existing data between Elasticsearch clusters.
**Learn more in [Migrate your Elasticsearch data](https://www.elastic.co/docs/manage-data/migrate).**