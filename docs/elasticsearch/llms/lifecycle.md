# Source: https://www.elastic.co/docs/manage-data/lifecycle

﻿---
title: Data lifecycle
description: The data you store in Elasticsearch generally falls into one of two categories: Content: a collection of items you want to search, such as a catalog of...
url: https://www.elastic.co/docs/manage-data/lifecycle
products:
  - Elasticsearch
applies_to:
  - Elastic Cloud Serverless: Generally available
  - Elastic Stack: Generally available
---

# Data lifecycle
The data you store in Elasticsearch generally falls into one of two categories:
- **Content**: a collection of items you want to search, such as a catalog of products
- **Time series data**: a stream of continuously-generated timestamped data, such as log entries

**Content** might be frequently updated, but the value of the content remains relatively constant over time. You want to be able to retrieve items quickly regardless of how old they are.
**Time series data** keeps accumulating over time, so you need strategies for balancing the value of the data against the cost of storing it. As it ages, it tends to become less important and less-frequently accessed, so you can move it to less expensive, less performant hardware. For your oldest data, what matters is that you have access to the data. It’s ok if queries take longer to complete.
To help you manage your data, Elasticsearch offers you the following options: Index lifecycle management, Data stream lifecycle, and Elastic Curator.
<note>
  [Data rollup](https://www.elastic.co/docs/manage-data/lifecycle/rollup) is a deprecated Elasticsearch feature that allows you to manage the amount of data that your cluster stores, similar to the downsampling functionality of ILM and data stream lifecycle. Do not use this feature for new deployments.
</note>


## ILM

<applies-to>
  - Elastic Cloud Serverless: Unavailable
</applies-to>

<tip>
  ILM is not available on Elasticsearch Serverless.
  <dropdown title="Why?">
    In an Elastic Cloud or self-managed environment, ILM lets you automatically transition indices through data tiers according to your performance needs and retention requirements. This allows you to balance hardware costs with performance. Elasticsearch Serverless eliminates this complexity by optimizing your cluster performance for you.[Data stream lifecycle](#data-stream-lifecycle) is an optimized lifecycle tool that lets you focus on the most common lifecycle management needs, without unnecessary hardware-centric concepts like data tiers.
  </dropdown>
</tip>

**ILM** can manage both indices and data streams. It allows you to do the following:
- Define the retention period of your data. The retention period is the minimum time Elasticsearch stores your data. Elasticsearch can delete data older than this period.
- Define [multiple tiers](https://www.elastic.co/docs/manage-data/lifecycle/data-tiers) of data nodes with different performance characteristics.
- Automatically transition indices through the data tiers according to your performance needs and retention policies.
- Leverage [searchable snapshots](https://www.elastic.co/docs/deploy-manage/tools/snapshot-and-restore/searchable-snapshots) stored in a remote repository to provide resiliency for your older indices while reducing operating costs and maintaining search performance.
- Perform [asynchronous searches](https://www.elastic.co/docs/solutions/search/async-search-api) of data stored on less-performant hardware.

**[Read more in Index lifecycle management ->](https://www.elastic.co/docs/manage-data/lifecycle/index-lifecycle-management)**

## Data stream lifecycle

**Data stream lifecycle** is less feature rich but focuses on simplicity. It allows you to do the following:
- Define the retention period of your data. The retention period is the minimum time Elasticsearch stores your data. Elasticsearch can delete data older than this period at a later time.
- Improve the performance of your data stream by performing background operations that optimize how Elasticsearch stores your data stream.

**[Read more in Data stream lifecycle ->](https://www.elastic.co/docs/manage-data/lifecycle/data-stream)**

## Elastic Curator

<applies-to>
  - Elastic Cloud Serverless: Unavailable
</applies-to>

**Elastic Curator** is a tool that allows you to manage your indices and snapshots using user-defined filters and predefined actions. If ILM provides the functionality to manage your index lifecycle, and you have at least a Basic license, consider using ILM in place of Curator. Many stack components use ILM by default.
**[Read more in Elastic Curator ->](https://www.elastic.co/docs/manage-data/lifecycle/curator)**