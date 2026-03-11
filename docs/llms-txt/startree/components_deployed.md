# Source: https://docs.startree.ai/getstarted/deployment/components_deployed.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Architecture

> The StarTree Cloud architecture integrates a managed Apache Pinot cluster with advanced ingestion, storage, and query capabilities. It supports diverse data sources, offers tiered storage for cost-effective performance, and utilizes Kubernetes-based orchestration for scalable, cloud-native deployments.

## Managed Pinot Cluster

At the core of StarTree Cloud is Apache Pinot, an open source, distributed analytics database designed for low latency, high throughput OLAP queries. It is packaged with StarTree plugins that improve the scalability, cost efficiency and usability of the database.

<img src="https://mintcdn.com/startree/xe5mTwlEdZc68KYh/getstarted/images/startree-cloud-architecture.png?fit=max&auto=format&n=xe5mTwlEdZc68KYh&q=85&s=b2d74102a1246bf57e4cde06264ec84f" alt="Startree Cloud Architecture Pn" width="1840" height="1540" data-path="getstarted/images/startree-cloud-architecture.png" />

The StarTree Cloud cluster manages the ingestion, storage, and query functions of Apache Pinot.

### Ingestion

There's a wide range of connectors to ingest data into StarTree Cloud.

* **Streaming connectors**\
  Continuously ingest data in realtime (milliseconds latency) from various streaming sources, such as: Apache Kafka, Confluent Cloud, Amazon Kinesis, and others.
* **Batch connectors**\
  One-time or recurring ingestion from sources such as Amazon S3 and Google Cloud Storage (GCS).
* **SQL connectors**\
  Import data from SQL sources such as Snowflake and BigQuery.

The ingestion layer also provides a rich library of pre-processing functions and decorators to enhance and transform data as it's ingested into Pinot.

### Storage

StarTree Cloud offers tiered data storage (hot, warm, cold) to enable efficient table management and a balance of performance and cost. This means users benefit from millisecond query responses on actively used, recent data. For less frequent queries on historical data, while latency may be higher, the storage is more cost-effective. Complementing this, data is highly compressed using a combination of columnar layout and advanced compression and encoding strategies.

### Query

StarTree Cloud enables users to query their data in Pinot via SQL, executing both common OLAP queries and complex multi-stage queries that incorporate joins and window functions. StarTree Cloud stands out for its exceptional query performance, consistently ranked among the fastest analytical databases. Users can leverage a range of indexing options for any column, alongside the powerful StarTree Index – an intelligent materialized view. StarTree Cloud customers run tens of thousands of queries per seconds with p99 latency in the order of milliseconds.

For more information on query performance, [read this blog post](https://startree.ai/resources/what-makes-apache-pinot-fast-chapter-ii).

## Cloud Infrastructure

StarTree Cloud is a fully cloud-native platform, available on AWS, Google Cloud, and Azure Cloud. Built for modern, scalable applications, StarTree Cloud is built upon:

* **Kubernetes-Based Orchestration:** Ensures portability, scalability, and high availability.
* **Containerized Microservices:** Modular and resilient system design.
* **Flexible Networking Support:** VPC peering, private link, transit gateway,
* **Decoupled Architecture:** Agents can pull in configurations from the StarTree Control plane and act accordingly.

For more information see: [https://startree.ai/deployment-options](https://startree.ai/deployment-options)

Built with [Mintlify](https://mintlify.com).
