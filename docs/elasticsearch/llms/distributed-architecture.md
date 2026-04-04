# Source: https://www.elastic.co/docs/deploy-manage/distributed-architecture

﻿---
title: Distributed architecture
description: Elasticsearch is a distributed document store. Instead of storing information as rows of columnar data, Elasticsearch stores complex data structures that...
url: https://www.elastic.co/docs/deploy-manage/distributed-architecture
products:
  - Elasticsearch
applies_to:
  - Elastic Cloud Serverless: Generally available
  - Elastic Stack: Generally available
---

# Distributed architecture
Elasticsearch is a distributed document store. Instead of storing information as rows of columnar data, Elasticsearch stores complex data structures that have been serialized as JSON documents. When you have multiple Elasticsearch nodes in a cluster, stored documents are distributed across the cluster and can be accessed immediately from any node.
The topics in this section provides information about the architecture of Elasticsearch and how it stores and retrieves data:
<note>
  Elastic Cloud Serverless scales with your workload and automates nodes, shards, and replicas for you. Some of the content in this section does not apply to you if you are using Elastic Cloud Serverless. Instead, the information in this section will provide you information about how the platform works for you.
</note>

- [Cluster, nodes, and shards](https://www.elastic.co/docs/deploy-manage/distributed-architecture/clusters-nodes-shards): Learn about the basic building blocks of an Elasticsearch cluster, including nodes, shards, primaries, and replicas.
  - [Node roles](https://www.elastic.co/docs/deploy-manage/distributed-architecture/clusters-nodes-shards/node-roles): Learn about the different roles that nodes can have in an Elasticsearch cluster.
- [Reading and writing documents](https://www.elastic.co/docs/deploy-manage/distributed-architecture/reading-and-writing-documents): Learn how Elasticsearch replicates read and write operations across shards and shard copies.
- [Shard allocation, relocation, and recovery](https://www.elastic.co/docs/deploy-manage/distributed-architecture/shard-allocation-relocation-recovery): Learn how Elasticsearch allocates and balances shards across nodes.
  - [Shard allocation awareness](https://www.elastic.co/docs/deploy-manage/distributed-architecture/shard-allocation-relocation-recovery/shard-allocation-awareness): Learn how to use custom node attributes to distribute shards across different racks or availability zones.
- [Discovery and cluster formation](https://www.elastic.co/docs/deploy-manage/distributed-architecture/discovery-cluster-formation): Learn about the cluster formation process including voting, adding nodes and publishing the cluster state.
- [Shard request cache](https://www.elastic.co/docs/deploy-manage/distributed-architecture/shard-request-cache): Learn how Elasticsearch caches search requests to improve performance.
- [Kibana task management](https://www.elastic.co/docs/deploy-manage/distributed-architecture/kibana-tasks-management): Learn how Kibana runs background tasks and distribute work across multiple Kibana instances to be persistent and scale with your deployment.