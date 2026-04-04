# Source: https://www.elastic.co/docs/manage-data/data-store

﻿---
title: The Elasticsearch data store
description: Elasticsearch is a distributed search and analytics engine, scalable data store, and vector database built on Apache Lucene. The documentation in this...
url: https://www.elastic.co/docs/manage-data/data-store
products:
  - Elasticsearch
applies_to:
  - Elastic Cloud Serverless: Generally available
  - Elastic Stack: Generally available
---

# The Elasticsearch data store
[Elasticsearch](https://github.com/elastic/elasticsearch/) is a distributed search and analytics engine, scalable data store, and vector database built on Apache Lucene.
The documentation in this section details how Elasticsearch works as a _data store_ starting with the fundamental unit of storage in Elasticsearch: the index. An index is a collection of documents uniquely identified by a name or an alias. Read more in [Index basics](https://www.elastic.co/docs/manage-data/data-store/index-basics).
Then, learn how these documents and the fields they contain are stored and indexed in [Mapping](https://www.elastic.co/docs/manage-data/data-store/mapping), and how unstructured text is converted into a structured format that’s optimized for search in [Text analysis](https://www.elastic.co/docs/manage-data/data-store/text-analysis).
You can also read more about working with Elasticsearch as a data store including how to use [index templates](https://www.elastic.co/docs/manage-data/data-store/templates) to tell Elasticsearch how to configure an index when it is created, how to use [aliases](https://www.elastic.co/docs/manage-data/data-store/aliases) to point to multiple indices, and how to use the [command line to manage data](https://www.elastic.co/docs/manage-data/data-store/manage-data-from-the-command-line) stored in Elasticsearch.
If your use case involves working with continuous streams of time series data, you can consider using a [data stream](https://www.elastic.co/docs/manage-data/data-store/data-streams). These are optimally suited for storing append-only data. You can access the data through a single, named resource, while Elasticsearch stores it in a series of hidden, auto-generated backing indices.