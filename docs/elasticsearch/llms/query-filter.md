# Source: https://www.elastic.co/docs/explore-analyze/query-filter

﻿---
title: Querying and filtering
description: Elasticsearch is not only great at storing and retrieving documents and their metadata, it also offers powerful querying and analytics capabilities that...
url: https://www.elastic.co/docs/explore-analyze/query-filter
products:
  - Elasticsearch
  - Kibana
applies_to:
  - Elastic Cloud Serverless: Generally available
  - Elastic Stack: Generally available
---

# Querying and filtering
Elasticsearch is not only great at storing and retrieving documents and their metadata, it also offers powerful querying and analytics capabilities that let you search, filter, and analyze your data at scale. These same capabilities are available in Kibana applications to facilitate interactive data exploration and visualization.
- **Elasticsearch makes JSON documents searchable and aggregatable.** The documents are stored in an [index](https://www.elastic.co/docs/manage-data/data-store/index-basics) or [data stream](https://www.elastic.co/docs/manage-data/data-store/data-streams), which represent one type of data.
- **Searchable means that you can find documents through multiple retrieval methods.** This includes filtering by yes/no conditions, keyword and full-text search with relevance scoring, and vector/semantic search to find content based on meaning rather than exact terms. Kibana provides many ways for you to construct these searches, from simple filters in dashboards to relevance-ranked queries in its search interfaces.
- **Aggregatable means that you can compute statistics and summaries from matching documents to reveal patterns and insights in your dataset.** The simplest aggregation is **count**, and it is frequently used in combination with the **date histogram**, to see count over time. The **terms** aggregation shows the most frequent values.


## Querying

You’ll use a combination of an API endpoint and a query language to interact with your data.
- Elasticsearch provides a number of [query languages](https://www.elastic.co/docs/explore-analyze/query-filter/languages). From Query DSL to the newest ES|QL, find the one that's most appropriate for you.
- You can call Elasticsearch's REST APIs by submitting requests directly from the command line or through the Dev Tools [Console](https://www.elastic.co/docs/explore-analyze/query-filter/tools/console) in Kibana. From your applications, you can use a [client](https://www.elastic.co/docs/reference/elasticsearch-clients) in your programming language of choice.
- A number of [tools](https://www.elastic.co/docs/explore-analyze/query-filter/tools) are available for you to save, debug, and optimize your queries.

If you're just getting started with Elasticsearch, try the hands-on [Index and search basics](https://www.elastic.co/docs/solutions/search/get-started/index-basics) to learn how to add data and run basic searches using Query DSL and the `_search` endpoint.

## Filtering

When querying your data in Kibana, additional options let you filter the results to just the subset you need. Some of these options are common to most Elastic apps. Check [Filtering in Kibana](https://www.elastic.co/docs/explore-analyze/query-filter/filtering) for more details on how to recognize and use them in the UI.