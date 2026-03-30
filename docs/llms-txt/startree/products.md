# Source: https://docs.startree.ai/getstarted/products.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Products

> StarTree Cloud offers applications and utilities that increase usability and reduce the time to value for users.

## StarTree Data Portal

### Overview

The StarTree Data Portal is the single, unified interface for managing and exploring Apache Pinot clusters on StarTree Cloud. It combines enterprise-grade features with Apache Pinot OSS UI capabilities into one seamless platform, eliminating the need to navigate between multiple tools. You can access the StarTree Data Portal directly at: [https://dp.your-environment.startree.cloud](https://dp.your-environment.startree.cloud)
The Data Portal makes it easy to:

* Ingest data into Pinot tables from a variety of streaming and batch sources via a guided, visual workflow.
* Transform data with minimal complexity, reducing the risk of format mismatches, quality issues, and connectivity errors.
* Explore and query real-time and offline data interactively.
* Monitor cluster health and troubleshoot operational issues.
* Secure access to data and resources with fine-grained RBAC controls.

By merging all of this into one interface, the Data Portal serves as the one-stop solution for all things Pinot.

### Key Features

#### Table Creation & Data Ingestion

* Visual, guided workflows for creating real-time and offline tables.
* Ingest from streaming sources (e.g., Confluent, Kafka, Kinesis) and batch sources (e.g., S3, GCS, ADLS).
* Apply transformations to clean or enrich data before ingestion.
* Detect and resolve issues early, such as schema mismatches, data quality problems, or connectivity errors.

#### Query Console

* Interactive query editor with syntax highlighting and auto-complete.
* Live data preview with sub-second latency for fresh data.
* Table browser to explore datasets, schemas, and metadata.
* Query templates for saving, reusing, and sharing frequently used queries.
* Performance insights with query latency and scanned record statistics.

#### Cluster Health

* Real-time views of broker, server, and controller status.

#### Observability

StarTree Cloud provides out-of-the-box support for system monitoring through Grafana dashboards.

* Users can view various system metrics such as CPU and memory usage.
* Monitor ingestion and query traffic patterns directly in Grafana.
* Export both metrics and system logs to external destinations.

#### Security Manager

* The Security Manager configures fine-grained Role-Based Access Control (RBAC) roles and policies.
* Assign roles and policies to Individual email IDs, Groups, and Service accounts
* StarTree Cloud admins can govern access control for multiple business units through a single interface.

#### Integrated Apache Pinot OSS UI Tools

* **Cluster Manager** – Inspect and manage cluster nodes, broker, server, minions, tenants, and segments. Advanced capabilities to manage Pinot Tables, like reloading and rebalancing.
* **Zookeeper Browser** – Navigate and view cluster metadata in Zookeeper.
* **Swagger API Explorer** – Test and interact with Pinot REST APIs directly from the UI.

## StarTree ThirdEye

With StarTree ThirdEye, users can create multi-dimensional real-time alerts on timeseries data stored in Pinot to detect anomalies in business events. For example, using ThirdEye you could detect if there is a sudden spike in incoming orders. ThirdEye also enables root cause analysis on the alert by identifying which dimension caused this spike. For example, the spike could originate from a certain country or demographic which will be automatically detected.

<Frame>
  **StarTree ThirdEye is not supported in the SaaS trial**
</Frame>

For more information and to request a demo see: [https://startree.ai/products/startree-thirdeye](https://startree.ai/products/startree-thirdeye)

Built with [Mintlify](https://mintlify.com).
