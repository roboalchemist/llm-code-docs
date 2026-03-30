# Parseable Documentation

Source: https://www.parseable.com/docs/llms-full.txt

---

# Architecture (/docs/architecture)









This document outlines the overall architecture of the Parseable Observability Platform, detailing the flow of MELT data from ingestion to storage and querying.

This document is organized into specific sections for each sub-system like ingestion, query, search, and index. To understand the specific decisions and trade-offs, refer the [design choices document](/docs/design-choices).

<img alt="Parseable Architecture" src={__img0} placeholder="blur" />

## Overview

Parseable is shipped as a single unified binary (or container image if you prefer). This includes the Prism and Parseable DB. There is no additional dependency to run Parseable.

The binary can be run in different modes. You’d generally run standalone mode to test and experience Parseable on your laptop, or a small testing server.

As you move to a production setup, we recommend running the distributed mode. Here each node has a specific role, i.e. ingestion, query or search.

## Ingestion

Parseable ingestion nodes follow a shared-nothing architecture, meaning each node independently handles the entire ingestion pipeline. In production, you typically place a load balancer in front of two or more ingestion nodes, allowing ingestion requests to be distributed across nodes seamlessly.

When a node receives an ingestion request (via HTTP or Kafka), it first validates the request, then converts the payload into an Apache Arrow-based file format. During this process, it also performs auto schema detection, enabling Parseable to intelligently classify logs and generate structured schemas on the fly. This makes it easy for users to filter, search, and analyze across diverse log types with minimal upfront configuration.

The Arrow files are temporarily staged in a dedicated local disk area. Once the disk write completes, the ingestion node acknowledges the request with a success response.

To ensure data durability during staging, we recommend attaching a small, reliable disk (such as NFS, Azure Files, or EFS) to each ingestion node.

A background job then reads the staged Arrow files, converts them into highly compressed Parquet files, and uploads them to S3 or any configured object store. During this transformation, the ingestion node also generates query metadata, which significantly enhances performance during log searches and queries.

<img alt="Parseable Ingestion Architecture" src={__img1} placeholder="blur" />

## Query

<Callout type="info">
  Distributed Query nodes are Enterprise only features available in pro and enterprise versions and cannot be deployed with OSS versions.
</Callout>

Query node is primarily responsible responding to query API. The query workflow starts when someone calls the query API with (a PostgreSQL compatible) SQL query, and a start and end timestamp. The query node looks up the metadata locally first, falling back to object store only if not found.

Based on metadata, the node identifies the relevant parquet files and uses the object store API to get these files. Here again, this only happens if the files are not already present locally. If the files are to be downloaded from object storage - this adds to latency and hence the occasional cold queries.

Another node called Prism node responds to all the role, user management, dataset management API. In Parseable OSS, a query node also serves as the leader node.

<img alt="Parseable Query Architecture" src={__img2} placeholder="blur" />

## Design choices

### Low latency writes

Ingested data is staged on local disk upon successful return by Parseable API. Data is then asynchronously committed to object store like S3. This ensures low latency, high throughput ingestion. To ensure data durability, we recommend using a small, reliable storage (EFS, Azure Files, NFS or equivalent) attached to the ingesting nodes. This ensures that data is not lost in case of a node failure.

### Atomic ingestion

Each ingestion batch received via API is concurrently appended to the same file within a one-minute window. When converted from Arrow to Parquet, entries are reordered to ensure the latest data appears first.

### Efficient storage

Parseable stores heavily compressed Parquet format to one of the most cost efficient storage, i.e. object storage. This leads to significant cost savings, especially for large datasets.

### Smart caching

Frequently accessed logs are cached in memory and NVMe SSDs on query nodes for faster access. The system prioritizes recent data, manages cache eviction automatically, and minimizes object store API calls using Parseable manifest files and Parquet footers.

### Index on demand

By default data is stored in columnar Parquet files, allowing fast aggregations, filtering numerical columns and SQL queries. Parseable allows indexing specific chunks of data, on demand - to allow text search on log data as and when needed.

### Stateless high availability

High availability (HA) is ensured through a distributed mode in which multiple ingestion and query servers operate independently.

### Object storage first

There is no separate consensus layer, eliminating complex coordination and reducing operational overhead. Object storage manages all concurrency control. See [AWS S3 configuration](/docs/storage/awss3) for detailed setup instructions.

### SQL for querying

We chose SQL as the query language for Parseable because it is widely used and understood, making it easier for users to interact with the system. SQL allows users to filter, aggregate, and join data from multiple sources. SQL is also very well supported by modern LLMs to generate queries from plain text.

## Trade-offs

### Staged writes

Staging data locally on the ingestor node for at least a minute, leads to a minor lag in querying the data. We trades immediate persistence for low latency ingestion.

### Occasional Cold Queries

The query layer fetches indexes from object storage (e.g., S3) and uses intelligent caching to accelerate future access. During the initial cache warm-up, some queries may access data directly from cold storage, resulting in higher latencies.

### Timed queries

A query call requires start and end timestamp. This ensures data is queried across a fixed, definite set of files. Parseable ensures query response includes the staging and committed data on object storage as required.


# Benchmarks (/docs/benchmarks)





Performance is a core requirement for observability platforms. As telemetry data volumes grow exponentially, it is critical for observability solutions to deliver high performance, at crucial times when teams need to troubleshoot and resolve issues quickly.

Parseable's telemetry data lake architecture is designed from the ground up for high performance ingestion and querying of telemetry data at scale.

We use modern storage formats, efficient indexing techniques, and optimized query execution strategies to deliver fast performance, additionally local NVMe and memory caching further accelerates query response times.

## ClickBench

[ClickBench](https://benchmark.clickhouse.com/) is an industry-standard benchmark for analytical databases. While originally designed for clickstream data, it has been widely adopted to evaluate performance of databases for various analytical workloads, including observability data.

Parseable is a top performer on the ClickBench. [View Parseable on ClickBench](http://logg.ing/clickbench)

<img alt="Parseable Benchmark" src={__img0} placeholder="blur" />

Read more about our performance philosophy in our post: [Performance is Table Stakes](https://www.parseable.com/blog/performance-is-table-stakes).

## Real world performance

Understanding Parseable's performance with a real-world scenario of ingesting and querying 100 TB of telemetry data per day.

Test Results at a Glance

| Metric                | Result                               |
| --------------------- | ------------------------------------ |
| **Ingestion Rate**    | **2 TB/hour** (sustained)            |
| **Query Latency**     | **Millisecond-range** (even at load) |
| **Monthly Cost**      | **\~$11,810** (for a 4-node cluster) |
| **Compression Ratio** | **Up to 90%**                        |

For more details, see our blog post: [The Economics and Physics of 100 TB Telemetry Data Per Day](https://www.parseable.com/blog/the-economics-and-physics-of-100-tb-telemetry-data-per-day).


# Design Choices (/docs/design-choices)



This document outlines our key design choices, ensuring durability, scalability, and efficiency for modern observability workloads. This page also covers the technical trade offs in Parseable.

<Callout type="info">
  If you have a specific use case or need a feature tailored to your observability needs, let us know at [sales@parseable.com](mailto:sales@parseable.com). We ship fast and most of such requests can be done in a matter of days.
</Callout>

### Highlights

#### Low latency writes

Ingested data is staged on local disk upon successful return by Parseable API. Data is then asynchronously committed to object store like S3. This ensures low latency, high throughput ingestion. To ensure data durability, we recommend using a small, reliable storage (EFS, Azure Files, NFS or equivalent) attached to the ingesting nodes. This ensures that data is not lost in case of a node failure.

#### Atomic ingestion

Each ingestion batch received via API is concurrently appended to the same file within a one-minute window. When converted from Arrow to Parquet, entries are reordered to ensure the latest data appears first.

#### Efficient storage

Parseable stores heavily compressed Parquet format to one of the most cost efficient storage, i.e. object storage. This leads to significant cost savings, especially for large datasets.

#### Smart caching

Frequently accessed logs are cached in memory and NVMe SSDs on query nodes for faster access. The system prioritizes recent data, manages cache eviction automatically, and minimizes object store API calls using Parseable manifest files and Parquet footers.

#### Index on demand

By default data is stored in columnar Parquet files, allowing fast aggregations, filtering numerical columns and SQL queries. Parseable allows indexing specific chunks of data, on demand - to allow text search on log data as and when needed.

#### Stateless high availability

High availability (HA) is ensured through a distributed mode in which multiple ingestion and query servers operate independently.

#### Object storage first

There is no separate consensus layer, eliminating complex coordination and reducing operational overhead. Object storage manages all concurrency control.

#### SQL for querying

We chose SQL as the query language for Parseable because it is widely used and understood, making it easier for users to interact with the system. SQL allows users to filter, aggregate, and join data from multiple sources. SQL is also very well supported by modern LLMs to generate queries from plain text.

### Trade-offs

#### Staged writes

Staging data locally on the ingestor node for at least a minute, leads to a minor lag in querying the data. We trades immediate persistence for low latency ingestion.

#### Occasional Cold Queries

The query layer fetches indexes from object storage (e.g., S3) and uses intelligent caching to accelerate future access. During the initial cache warm-up, some queries may access data directly from cold storage, resulting in higher latencies.

#### Timed queries

A query call requires start and end timestamp. This ensures data is queried across a fixed, definite set of files. Parseable ensures query response includes the staging and committed data on object storage as required.


# Features (/docs/features)



import { IconSparkles, IconBellRinging, IconDashboard, IconCode, IconSql, IconLock, IconBrain, IconUserCircle, IconDatabase, IconRefresh, IconApi } from '@tabler/icons-react';

Explore Parseable's features designed to enhance your observability experience. From intuitive dashboards to advanced search capabilities, these features will help you get the most out of your telemetry data and streamline your observability workflow.

<Cards>
  <Card href="/docs/user-guide/ai-native" icon={<IconSparkles className="text-purple-600" />} title="AI Native">
    AI-powered observability with Keystone Q\&A, dataset summarization, and natural language to SQL conversion.
  </Card>

  <Card href="/docs/user-guide/alerting" icon={<IconBellRinging className="text-purple-600" />} title="Alerting">
    Set up real-time alerts to notify you of important events or anomalies in your telemetry data.
  </Card>

  <Card href="/docs/user-guide/dashboards" icon={<IconDashboard className="text-purple-600" />} title="Dashboards">
    Create customizable dashboards to visualize your telemetry data and gain insights at a glance.
  </Card>

  <Card href="/docs/user-guide/sql-editor" icon={<IconSql className="text-purple-600" />} title="SQL Editor">
    Write and execute SQL queries to analyze your telemetry data with a powerful query editor.
  </Card>

  <Card href="/docs/user-guide/rbac" icon={<IconLock className="text-purple-600" />} title="Role-Based Access Control">
    Secure your data with fine-grained access controls and user permissions management.
  </Card>

  <Card href="/docs/user-guide/log-iq" icon={<IconBrain className="text-purple-600" />} title="Log IQ">
    Transform unstructured logs into structured JSON data for easier querying, searching, and visualization.
  </Card>

  <Card href="/docs/user-guide/openid" icon={<IconUserCircle className="text-purple-600" />} title="OpenID Integration">
    Seamlessly integrate with OpenID providers for secure authentication and single sign-on capabilities.
  </Card>

  <Card href="/docs/user-guide/retention" icon={<IconDatabase className="text-purple-600" />} title="Retention Policies">
    Manage your data lifecycle with customizable retention policies to optimize storage costs and compliance.
  </Card>

  <Card href="/docs/user-guide/smart-cache" icon={<IconRefresh className="text-purple-600" />} title="Smart Cache">
    Optimize query performance with intelligent caching mechanisms for frequently accessed data.
  </Card>

  <Card href="/docs/api" icon={<IconApi className="text-purple-600" />} title="API Reference">
    Comprehensive API documentation for programmatic access to Parseable's features and capabilities.
  </Card>
</Cards>


# Quickstart Guide (/docs/get-started)



import { IconChartCohort, IconDirections, IconCloudDataConnection, IconBrandInertia, IconFileTypeSql, IconServerBolt,
 IconSchema, IconFileDigitFilled, IconCloudComputing, IconCloud } from '@tabler/icons-react';

## Parseable Pro

<OfferingPills pro />

The fastest way to get started is Parseable Cloud Pro tier. Sign up for Parseable Pro for a free 14 days trial. No credit card needed.

<Cards>
  <Card href="/docs/quickstart/cloud" icon={<IconCloud className="text-blue-500" />} title="Parseable Cloud" className="text-blue-500">
    Sign up for fully featured trial.
  </Card>

  <Card href="/docs/quickstart/binary" icon={<IconFileDigitFilled className="text-blue-500" />} title="Executable Binary" className="text-blue-500">
    Download and run the binary directly.
  </Card>
</Cards>

## Run locally

You can also run Parseable Open Source edition locally. To run Parseable locally, run the following command to start Parseable in local mode on your machine:

```bash
docker run -p 8000:8000 \
parseable/parseable:edge \
parseable local-store
```

Once the container is running successfully, go to [http://localhost:8000](http://localhost:8000) and login with the default credentials `admin` / `admin`.

You'll see the setup screen where you can import sample data in one click. This will also create few dashboards and queries to get you started.

## Production installation

To deploy Parseable in a production environment, refer to the self-hosted installation guide:

<Cards>
  <Card href="/docs/self-hosted/installation" icon={<IconSchema className="text-blue-500" />} title="Self-hosted installation" className="col-span-2 text-blue-500">
    Deploy Parseable in your own environment.
  </Card>
</Cards>


# Home (/docs)



import {IconEmpathize,IconHandClick,IconGeometry,IconBrandSpeedtest,IconBrandInertia,IconFileTypeSql, IconCloud,IconBrandTabler,IconBrandOpenSource } from '@tabler/icons-react';
import { Banner } from 'fumadocs-ui/components/banner';

<Banner changeLayout={false}>
  Experience the future of observability with Parseable Cloud.
  <a href="https://telemetry.new"> Get Started ↗︎ </a>
</Banner>

<p>
  Parseable is a 

  <strong>modern, unified observability platform</strong>

  . It is based on our 

  <a href="https://github.com/parseablehq/parseable">purpose built telemetry data lake</a>

  . Written in Rust, Parseable uses advanced compression and caching techniques to offer best in class performance and scalability.
</p>

<p text="bold">
  Parseable is AI native, high performance, peta scale alternative to traditional observability systems.
</p>

<p>
  This documentation site provides comprehensive guides, references, and tutorials to help you get the most out of Parseable.
</p>

## Flavors

Parseable is available in three flavors.

<Cards>
  <Card href="/docs/flavours/pro" icon={<IconCloud className="text-[#7E22CE] dark:text-[#C084FC]" />} className="text-[#7E22CE] dark:text-[#C084FC] bg-[#F3E8FF] hover:bg-[#E9D5FF] dark:bg-[#1F162A] dark:hover:bg-[#2A1E3A] col-span-2" title="Parseable Pro">
    Learn about Parseable Pro, our fully managed cloud platform.
  </Card>

  <Card href="/docs/flavours/enterprise" icon={<IconBrandTabler className="text-[#1D4ED8] dark:text-[#60A5FA]" />} className="text-[#1D4ED8] dark:text-[#60A5FA] bg-[#EAF2FF] hover:bg-[#DBEAFE] dark:bg-[#141C2A] dark:hover:bg-[#1C2A44]" title="Parseable Enterprise">
    Learn about Parseable Enterprise.
  </Card>

  <Card href="/docs/flavours/oss" icon={<IconBrandOpenSource className="text-[#047857] dark:text-[#34D399]" />} className="text-[#047857] dark:text-[#34D399] bg-[#ECFDF5] hover:bg-[#D1FAE5] dark:bg-[#14241D] dark:hover:bg-[#1C3A2D]" title="Parseable OSS">
    Learn about Parseable OSS.
  </Card>
</Cards>

## Learn more

<Cards>
  <Card href="/docs/introduction" icon={<IconEmpathize className="text-blue-500" />} className="text-blue-500" title="What is Parseable?">
    Get introduced to Parseable.
  </Card>

  <Card href="/docs/quickstart/docker" icon={<IconHandClick className="text-blue-500" />} className="text-blue-500" title="Quickstart">
    Get started with Parseable in less than a minute.
  </Card>

  <Card href="/docs/architecture" icon={<IconGeometry className="text-blue-500" />} className="text-blue-500" title="Architecture">
    Learn about the telemetry data lake architecture.
  </Card>

  <Card href="/docs/ingestion" icon={<IconBrandInertia className="text-blue-500" />} className="text-blue-500" title="Ingest data">
    Ingesting telemetry data into Parseable.
  </Card>
</Cards>


# Ingestion (/docs/ingestion)



import { IconPlug, IconCode, IconWand, IconSettings, IconDatabase, IconChartDots, IconTimeline,IconBrandAws,IconBrandAzure,IconBrandGoogle } from '@tabler/icons-react';

Ingestion is the process of sending Telemetry signals (Metrics, Events, Logs, Traces) into Parseable.

You can ingest data to Parseable in JSON format over HTTP(s). This means that any log agent, metric collector, or tracing library that can send data over HTTP in JSON format can be used to ingest data into Parseable.

For log data you can use the HTTP output plugins of all the logging agents/shippers. You can also directly integrate Parseable with your application via [REST API](/docs/api/v1/ingest).

Parseable also supports the OTel native data ingestion via the Protobuf over HTTP. This allows you to use any OpenTelemetry compatible log agent or library to send logs to Parseable.

<Callout type="info">
  Field name starting with `@` is replaced with `_`. In case of key collision, the event is rejected.
</Callout>

<Callout type="info">
  When an incoming event has a field with a data type different from the existing schema, the field is automatically renamed with a type suffix (e.g., `body_timestamp_utf8`, `span_kind_int64`). This prevents ingestion failures where field types may vary between events.
</Callout>

## Ingestion reference

Explore the different methods to ingest data into Parseable. Choose the method that best fits your infrastructure and use case.

### OpenTelemetry

<Callout type="info">
  In case of otel-metrics, there may be key collision in the attributes key, as the attributes are present in different hierarchical levels in the otel metrics event. In such scenarios, the key values are overridden by the last available attribute.
</Callout>

<Cards>
  <Card href="/docs/ingest-data/otel/traces" icon={<IconTimeline className="text-purple-600" />} title="OTel Traces">
    Ingest distributed traces using OpenTelemetry Protocol (OTLP).
  </Card>

  <Card href="/docs/ingest-data/otel/logs" icon={<IconTimeline className="text-purple-600" />} title="OTel Logs">
    Ingest structured logs using OpenTelemetry Protocol (OTLP).
  </Card>

  <Card href="/docs/ingest-data/otel/metrics" icon={<IconChartDots className="text-purple-600" />} title="OTel Metrics">
    Ingest metrics using OpenTelemetry Protocol (OTLP).
  </Card>
</Cards>

### Zero instrumentation

<Cards>
  <Card href="/docs/ingest-data/zero-instrumentation" icon={<IconWand className="text-purple-600" />} title="eBPF Agents">
    Collect logs without modifying your application code.
  </Card>
</Cards>

### LLM & AI Agents

<Cards>
  <Card href="/docs/ingest-data/ai-agents/openai" icon={<IconCode className="text-purple-600" />} title="OpenAI">
    Track and log OpenAI API calls and responses.
  </Card>

  <Card href="/docs/ingest-data/ai-agents/anthropic" icon={<IconCode className="text-purple-600" />} title="Anthropic">
    Monitor and log Anthropic Claude API interactions.
  </Card>

  <Card href="/docs/ingest-data/ai-agents/langchain" icon={<IconCode className="text-purple-600" />} title="LangChain">
    Ingest traces and logs from LangChain applications.
  </Card>

  <Card href="/docs/ingest-data/ai-agents/llamaindex" icon={<IconCode className="text-purple-600" />} title="LlamaIndex">
    Collect observability data from LlamaIndex applications.
  </Card>

  <Card href="/docs/ingest-data/ai-agents/autogen" icon={<IconCode className="text-purple-600" />} title="AutoGen">
    Track multi-agent conversations and AutoGen workflows.
  </Card>

  <Card href="/docs/ingest-data/ai-agents/crewai" icon={<IconCode className="text-purple-600" />} title="CrewAI">
    Ingest logs from CrewAI agent orchestration.
  </Card>

  <Card href="/docs/ingest-data/ai-agents/dspy" icon={<IconCode className="text-purple-600" />} title="DSPy">
    Monitor DSPy framework executions and outputs.
  </Card>

  <Card href="/docs/ingest-data/ai-agents/n8n" icon={<IconCode className="text-purple-600" />} title="n8n">
    Collect workflow execution logs from n8n automation platform.
  </Card>
</Cards>

### Log agents and shippers

<Cards>
  <Card href="/docs/ingest-data/logging-agents/fluent-bit" icon={<IconPlug className="text-blue-600" />} title="Fluent Bit">
    Lightweight and scalable logging processor. Perfect for Kubernetes and Docker environments.
  </Card>

  <Card href="/docs/ingest-data/logging-agents/vector" icon={<IconPlug className="text-blue-600" />} title="Vector">
    High-performance observability data pipeline for logs, metrics, and traces.
  </Card>

  <Card href="/docs/ingest-data/logging-agents/fluentd" icon={<IconPlug className="text-blue-600" />} title="Fluentd">
    Unified logging layer that collects data from multiple sources and routes to destinations.
  </Card>

  <Card href="/docs/ingest-data/logging-agents/otel-collector" icon={<IconPlug className="text-blue-600" />} title="OpenTelemetry Collector">
    Vendor-agnostic way to receive, process, and export telemetry data.
  </Card>

  <Card href="/docs/ingest-data/logging-agents/apache-log-4j" icon={<IconPlug className="text-blue-600" />} title="Apache Log4j">
    Send logs directly from Log4j applications to Parseable.
  </Card>

  <Card href="/docs/ingest-data/logging-agents/logstash" icon={<IconPlug className="text-blue-600" />} title="Logstash">
    Server-side data processing pipeline that ingests data from multiple sources.
  </Card>

  <Card href="/docs/ingest-data/logging-agents/syslog" icon={<IconPlug className="text-blue-600" />} title="Syslog">
    Standard protocol for message logging across network devices and servers.
  </Card>

  <Card href="/docs/ingest-data/logging-agents/filebeat" icon={<IconPlug className="text-blue-600" />} title="Filebeat">
    Lightweight shipper for forwarding and centralizing log data from files.
  </Card>

  <Card href="/docs/ingest-data/logging-agents/promtail" icon={<IconPlug className="text-blue-600" />} title="Promtail">
    Agent that ships the contents of local logs to a centralized store.
  </Card>

  <Card href="/docs/ingest-data/logging-agents/prometheus" icon={<IconChartDots className="text-blue-600" />} title="Prometheus">
    Monitoring system and time series database for metrics collection.
  </Card>
</Cards>

### Databases

<Cards>
  <Card href="/docs/ingest-data/databases/postgresql" icon={<IconDatabase className="text-gray-600" />} title="PostgreSQL">
    Ingest logs and metrics from PostgreSQL databases.
  </Card>

  <Card href="/docs/ingest-data/databases/mysql" icon={<IconDatabase className="text-gray-600" />} title="MySQL">
    Collect logs and metrics from MySQL databases.
  </Card>

  <Card href="/docs/ingest-data/databases/mongodb" icon={<IconDatabase className="text-gray-600" />} title="MongoDB">
    Ingest logs and metrics from MongoDB databases.
  </Card>

  <Card href="/docs/ingest-data/databases/redis" icon={<IconDatabase className="text-gray-600" />} title="Redis">
    Collect logs and metrics from Redis databases.
  </Card>

  <Card href="/docs/ingest-data/databases/elasticsearch" icon={<IconDatabase className="text-gray-600" />} title="Elasticsearch">
    Migrate or sync data from Elasticsearch to Parseable.
  </Card>
</Cards>

### Containers

<Cards>
  <Card href="/docs/ingest-data/containers/docker" icon={<IconDatabase className="text-orange-600" />} title="Docker">
    Collect logs from Docker containers using logging drivers.
  </Card>

  <Card href="/docs/ingest-data/containers/kubernetes" icon={<IconDatabase className="text-orange-600" />} title="Kubernetes">
    Ingest logs from Kubernetes clusters using DaemonSets and sidecars.
  </Card>

  <Card href="/docs/ingest-data/containers/amazon-ecs" icon={<IconDatabase className="text-orange-600" />} title="Amazon ECS">
    Collect logs from Amazon Elastic Container Service tasks.
  </Card>

  <Card href="/docs/ingest-data/containers/amazon-eks" icon={<IconDatabase className="text-orange-600" />} title="Amazon EKS">
    Ingest logs from Amazon Elastic Kubernetes Service clusters.
  </Card>

  <Card href="/docs/ingest-data/containers/google-gke" icon={<IconDatabase className="text-orange-600" />} title="Google GKE">
    Ingest logs from Google Kubernetes Engine clusters.
  </Card>

  <Card href="/docs/ingest-data/containers/azure-aks" icon={<IconDatabase className="text-orange-600" />} title="Azure AKS">
    Collect logs from Azure Kubernetes Service clusters.
  </Card>
</Cards>

### Streaming Platforms

<Cards>
  <Card href="/docs/ingest-data/streaming/kafka" icon={<IconTimeline className="text-purple-600" />} title="Kafka">
    Ingest real-time streaming data from Apache Kafka topics.
  </Card>

  <Card href="/docs/ingest-data/streaming/redpanda" icon={<IconTimeline className="text-purple-600" />} title="Redpanda">
    Stream data from Redpanda, a Kafka-compatible streaming platform.
  </Card>

  <Card href="/docs/ingest-data/streaming/rabbitmq" icon={<IconTimeline className="text-purple-600" />} title="RabbitMQ">
    Collect messages from RabbitMQ message broker.
  </Card>

  <Card href="/docs/ingest-data/streaming/nats" icon={<IconTimeline className="text-purple-600" />} title="NATS">
    Ingest messages from NATS messaging system.
  </Card>
</Cards>

### CI/CD Tools

<Cards>
  <Card href="/docs/ingest-data/cicd/github-actions" icon={<IconSettings className="text-green-600" />} title="GitHub Actions">
    Collect logs and metrics from GitHub Actions workflows.
  </Card>

  <Card href="/docs/ingest-data/cicd/jenkins" icon={<IconSettings className="text-green-600" />} title="Jenkins">
    Collect build and deployment logs from Jenkins.
  </Card>

  <Card href="/docs/ingest-data/cicd/gitlab-ci" icon={<IconSettings className="text-green-600" />} title="GitLab CI">
    Ingest logs from GitLab CI/CD pipelines.
  </Card>

  <Card href="/docs/ingest-data/cicd/circleci" icon={<IconSettings className="text-green-600" />} title="CircleCI">
    Ingest logs from CircleCI build pipelines.
  </Card>

  <Card href="/docs/ingest-data/cicd/argocd" icon={<IconSettings className="text-green-600" />} title="ArgoCD">
    Collect logs from ArgoCD GitOps deployments.
  </Card>

  <Card href="/docs/ingest-data/cicd/terraform" icon={<IconSettings className="text-green-600" />} title="Terraform">
    Ingest infrastructure deployment logs from Terraform.
  </Card>
</Cards>

### Cloud services

<Cards>
  <Card href="/docs/ingest-data/cloud/aws-cloudwatch" icon={<IconBrandAws className="text-blue-600" />} title="AWS CloudWatch">
    Ingest logs and metrics from AWS CloudWatch service.
  </Card>

  <Card href="/docs/ingest-data/cloud/aws-kinesis" icon={<IconBrandAws className="text-blue-600" />} title="AWS Kinesis">
    Stream data from AWS Kinesis Data Streams to Parseable.
  </Card>

  <Card href="/docs/ingest-data/cloud/azure-event-hubs" icon={<IconBrandAzure className="text-blue-600" />} title="Azure Event Hubs">
    Ingest streaming data from Azure Event Hubs.
  </Card>

  <Card href="/docs/ingest-data/cloud/gcp-pubsub" icon={<IconBrandGoogle className="text-blue-600" />} title="GCP Pub/Sub">
    Stream data from Google Cloud Pub/Sub messaging service.
  </Card>
</Cards>

### Security Tools

<Cards>
  <Card href="/docs/ingest-data/security/falco" icon={<IconSettings className="text-red-600" />} title="Falco">
    Ingest runtime security events from Falco.
  </Card>

  <Card href="/docs/ingest-data/security/trivy" icon={<IconSettings className="text-red-600" />} title="Trivy">
    Collect vulnerability scan results from Trivy.
  </Card>

  <Card href="/docs/ingest-data/security/siem-export" icon={<IconSettings className="text-red-600" />} title="SIEM Export">
    Export security events to SIEM platforms.
  </Card>
</Cards>

### Programming languages

<Cards>
  <Card href="/docs/ingest-data/programming-languages/python" icon={<IconCode className="text-green-600" />} title="Python">
    Integrate Parseable with Python applications using standard logging libraries.
  </Card>

  <Card href="/docs/ingest-data/programming-languages/javascript" icon={<IconCode className="text-green-600" />} title="JavaScript/Node.js">
    Integrate Parseable with Node.js applications and browser-based logging.
  </Card>

  <Card href="/docs/ingest-data/programming-languages/go" icon={<IconCode className="text-green-600" />} title="Go">
    Send logs from Go applications using HTTP client or OpenTelemetry SDK.
  </Card>

  <Card href="/docs/ingest-data/programming-languages/java" icon={<IconCode className="text-green-600" />} title="Java">
    Send logs from Java applications using Log4j, Logback, or OpenTelemetry.
  </Card>

  <Card href="/docs/ingest-data/programming-languages/rust" icon={<IconCode className="text-green-600" />} title="Rust">
    Send logs from Rust applications using tracing or log crates.
  </Card>

  <Card href="/docs/ingest-data/programming-languages/csharp" icon={<IconCode className="text-green-600" />} title="C#">
    Integrate Parseable with C# applications using Serilog or NLog.
  </Card>

  <Card href="/docs/ingest-data/programming-languages/dotnet" icon={<IconCode className="text-green-600" />} title=".NET">
    Integrate Parseable with .NET applications using structured logging.
  </Card>

  <Card href="/docs/ingest-data/programming-languages/php" icon={<IconCode className="text-green-600" />} title="PHP">
    Send logs from PHP applications using Monolog or custom implementations.
  </Card>

  <Card href="/docs/ingest-data/programming-languages/ruby" icon={<IconCode className="text-green-600" />} title="Ruby">
    Integrate Parseable with Ruby applications using standard logging frameworks.
  </Card>
</Cards>

## Ingestion HTTP headers

You can use HTTP headers to control how data is ingested and processed.

### Required headers

| Header          | Description                                                   | Example                  | Possible Values                           |
| --------------- | ------------------------------------------------------------- | ------------------------ | ----------------------------------------- |
| `X-P-Stream`    | Target dataset name. Creates the dataset if it doesn't exist. | `nginx-logs`             | Valid dataset name                        |
| `Authorization` | Basic auth credentials (base64 encoded `username:password`)   | `Basic YWRtaW46YWRtaW4=` | Valid credentials                         |
| `Content-Type`  | Content type of the request body                              | `application/json`       | `application/json`,`application/protobuf` |

### Optional headers

| Header            | Description                                                          | Example                           |
| ----------------- | -------------------------------------------------------------------- | --------------------------------- |
| `X-P-Tag-{field}` | Add custom tags/metadata to events. Replace `{field}` with tag name. | `X-P-Tag-environment: production` |

## Log processing

<OfferingPills pro enterprise className="mb-4" />

When agents like Fluent Bit or Vector send logs to Parseable, they typically send the entire log line in a single field (usually named `log` or `message`). With log extraction enabled, Parseable can automatically parse this raw log line and extract structured fields using regex patterns.

**The flow:**

1. Agent sends JSON log data with the raw log line in a field (e.g., `{"log": "192.168.1.1 - - [10/Jan/2026:12:00:00] ..."}`)
2. Agent sets `X-P-Extract-Log` header to the field name containing the raw log (e.g., `log`)
3. Agent sets `X-P-Log-Source` header to the log format name (e.g., `nginx_access`)
4. Parseable reads the value from the specified field, applies the matching regex pattern, and adds all extracted fields to the event

### Headers for log extraction

| Header            | Description                                                          | Example                      | Possible Values                                                   |
| ----------------- | -------------------------------------------------------------------- | ---------------------------- | ----------------------------------------------------------------- |
| `X-P-Log-Source`  | Log format name - Parseable applies regex patterns to extract fields | `nginx_access`, `syslog_log` | See [Supported log source formats](#supported-log-source-formats) |
| `X-P-Extract-Log` | Field name in the JSON payload that contains the raw log line        | `log`, `message`             | Any valid field name                                              |

### Supported log source formats

| #  | Format Name             |
| -- | ----------------------- |
| 1  | `access_log`            |
| 2  | `alb_log`               |
| 3  | `block_log`             |
| 4  | `candlepin_log`         |
| 5  | `choose_repo_log`       |
| 6  | `cloudvm_ram_log`       |
| 7  | `cups_log`              |
| 8  | `dpkg_log`              |
| 9  | `elb_log`               |
| 10 | `engine_log`            |
| 11 | `env_logger_log`        |
| 12 | `error_log`             |
| 13 | `esx_syslog_log`        |
| 14 | `haproxy_log`           |
| 15 | `java`                  |
| 16 | `katello_log`           |
| 17 | `klog`                  |
| 18 | `kubernetes_log`        |
| 19 | `lnav_debug_log`        |
| 20 | `nextflow_log`          |
| 21 | `nginx_access`          |
| 22 | `openam_log`            |
| 23 | `openamdb_log`          |
| 24 | `openstack_log`         |
| 25 | `page_log`              |
| 26 | `parseable_server_logs` |
| 27 | `postgres`              |
| 28 | `postgresql_log`        |
| 29 | `procstate_log`         |
| 30 | `proxifier_log`         |
| 31 | `rails_log`             |
| 32 | `redis_log`             |
| 33 | `s3_log`                |
| 34 | `simple_rs_log`         |
| 35 | `snaplogic_log`         |
| 36 | `sssd_log`              |
| 37 | `strace_log`            |
| 38 | `sudo_log`              |
| 39 | `syslog_log`            |
| 40 | `tcf_log`               |
| 41 | `tcsh_history`          |
| 42 | `uwsgi_log`             |
| 43 | `vmk_log`               |
| 44 | `vmw_log`               |
| 45 | `vmw_py_log`            |
| 46 | `vmw_vc_svc_log`        |
| 47 | `vpostgres_log`         |
| 48 | `web_robot_log`         |
| 49 | `xmlrpc_log`            |
| 50 | `zookeeper`             |
| 51 | `zookeeper_log`         |

## Flattening

Nested JSON objects are automatically flattened. For example, the following JSON object

```json
{
  "foo": {
    "bar": "baz"
  }
}
```

will be flattened to

```json
{
  "foo_bar": "baz"
}
```

before it gets stored. While querying, this field should be referred to as foo\_bar. For example, select `foo_bar` from `<dataset-name>`. The flattened field will be available in the schema as well.

## Batching and Compression

Wherever applicable, we recommend enabling the log agent's compression and batching features to reduce network traffic and improve ingestion performance. The maximum payload size in Parseable is 10 MiB (10485760 Bytes). The payload can contain single log event as a JSON object or multiple log events in a JSON array. There is no limit to the number of batched events in a single call.

## Timestamp

Correct time is critical to understand the proper sequence of events. Timestamps are important for debugging, analytics, and deriving transactions. We recommend that you include a timestamp in your log events formatted in RFC3339 format.

Parseable uses the event-received timestamp and adds it to the log event in the field `p_timestamp`. This ensures there is a time reference in the log event, even if the original event doesn't have a timestamp.

## Staging

Staging in Parseable refers to the process of storing log data on locally attached storage before it is pushed to a long term and persistent store like S3 or something similar. Staging acts as a buffer for incoming events and allows a stable approach to pushing events to the persistent store.

Once an HTTP call is received on the Parseable server, events are parsed and converted to Arrow format in memory. This Arrow data is then written to the staging directory (defaults to `$PWD/staging`). Every minute, the server converts the Arrow data to Parquet format and pushes it to the persistent store. We chose a minute as the default interval, so there is a clear boundary between events, and the prefix structure on S3 is predictable.

The query flow in Parseable allows transparent access to the data in the staging directory. This means that the data in the staging directory is queryable in real-time. As a user, you won't see any difference in the data fetched from the staging directory or the persistent store.

The staging directory can be configured using the `P_STAGING_DIR` environment variable, as explained in the environment vars section.

## Planning for Production

When planning for the production deployment of Parseable, the two most important considerations from a staging perspective are:

Storage size: Ensure that the staging area has sufficient capacity to handle the anticipated log volume. This prevents data loss due to disk space exhaustion. To calculate the storage size, consider the average log event size, the expected log volume for 5-10 minutes. This is done as under high loads, the conversion to Parquet and subsequent push to S3 may lag behind.

Local storage redundancy: Data in staging has not been committed to persistent store, it is important to have the staging itself reliable and redundant. This way, the staging data is protected from data loss due to simple disk failures. If using AWS, choose from services like EBS (Elastic Block Store) or EFS (Elastic File System), and mount these volumes on the Parseable server. Similarly, on Azure chose from Managed Disks or Azure Files. If you're using a private cloud, a reliable mounted volume from a NAS or SAN can be used.


# What is Parseable? (/docs/introduction)





import { IconCpu2,IconSortDescendingSmallBig,IconBolt,IconTelescope,IconCloudDataConnection,IconFileTextShield } from '@tabler/icons-react';

<p>
  Parseable is a 

  <strong>modern, unified observability platform</strong>

  . SRE and DevOps teams use Parseable to build observability pipelines to observe their production systems at scale.
</p>

<p>
  Parseable ingests, processes, stores, and queries telemetry data including logs, metrics, and traces from applications, infrastructure, and services.
</p>

<p>
  With built-in support for predictive alerting and anomaly detection, Parseable helps teams proactively identify and resolve issues before they impact end-users.
</p>

<p>
  It is based on our 

  <a href="https://github.com/parseablehq/parseable">purpose built telemetry data lake</a>

  . Written in Rust, Parseable uses advanced compression and caching techniques to offer best in class performance and scalability.
</p>

<img alt="" src={__img0} placeholder="blur" />

## Key differentiators

<Cards>
  <Card icon={<IconCpu2 />} title="Up to 70% less compute resources">
    70% less CPU than traditional Java solutions like Elasticsearch under similar workloads.
  </Card>

  <Card icon={<IconSortDescendingSmallBig />} title="Up to 90% compression">
    Built-in compression to compress observability and telemetry data by up to 90%.
  </Card>

  <Card icon={<IconBolt />} title="Fast queries">
    Fast query response with Rust based design, modern query techniques, and intelligent caching on SSDs / NVMe and memory.
  </Card>

  <Card icon={<IconCloudDataConnection />} title="Object store first">
    Excellent storage efficiency and cost with object stores like S3, GCS, Azure Blob as the primary storage layer.
  </Card>

  <Card icon={<IconTelescope />} title="OpenTelemetry native">
    Ingest, manage and query OpenTelemetry logs, metrics or traces natively. Zero configuration needed.
  </Card>

  <Card icon={<IconFileTextShield />} title="Data privacy and security">
    Deploy across public or private clouds, containers, VMs, or bare metal environments with complete data security and privacy.
  </Card>
</Cards>

## Learn more

<Cards>
  <Card href="/docs/architecture" icon={<IconTelescope className="text-blue-500" />} className="text-blue-500" title="Architecture">
    Learn about the telemetry data lake architecture.
  </Card>

  <Card href="/docs/features" icon={<IconBolt className="text-blue-500" />} className="text-blue-500" title="Features">
    Get to know the key features of Parseable.
  </Card>

  <Card href="/docs/ingestion" icon={<IconCloudDataConnection className="text-blue-500" />} className="text-blue-500" title="Ingest data">
    Ingest telemetry data into Parseable.
  </Card>

  <Card href="/docs/query" icon={<IconFileTextShield className="text-blue-500" />} className="text-blue-500" title="Query data">
    Query your telemetry data using SQL.
  </Card>

  <Card href="/docs/integrations" icon={<IconCloudDataConnection className="text-blue-500" />} className="text-blue-500" title="Integrations">
    Integrate with your existing tools and workflows.
  </Card>
</Cards>


# Query (/docs/query)



Parseable offers a PostgreSQL compatible SQL query interface to query log data. Users can choose to use the filter interface directly without having to deal with SQL at all. However for more complex queries and advanced users, Parseable offers a SQL query interface.

You can specify the query and the relevant time range for which you want this query to be run. The response is inclusive of both the start and end timestamps.

The filter interface is quite self explanatory, with options to filter by specific columns and values and also by time range. In this document, we'll cover more about the SQL API and its capabilities.

Check out the [Query API](/docs/api/v1/query).

## How does it work?

After parsing and creating the execution plan for a query, the Parseable query server uses the data manifest file to filter out the relevant Parquet files. The data manifest file is a JSON file that contains the specific column metadata for a whole day. The querier uses this file to filter the relevant Parquet files based on the query filters and the time range.

Only the relevant Parquet file paths are then added as a data source to custom table provider. Datafusion then efficiently reads the files via the GetRange S3 API, pulling only the very specific data needed for the query. This ensures that only the relevant data is read from the storage, reducing the query time and cost.

## Supported functions

Parseable supports a wide range of SQL functions - Aggregate, Window and Scalar functions. Refer the Apache Datafusion documentation for the complete list of supported functions and their usage.

* [Aggregate Functions](https://datafusion.apache.org/user-guide/sql/aggregate_functions.html)
* [Window Functions](https://datafusion.apache.org/user-guide/sql/window_functions.html)
* [Scalar Functions](https://datafusion.apache.org/user-guide/sql/scalar_functions.html)

## Query with regular expressions

This section provides examples of how to use regular expressions in Parseable queries.

* Match regular expression (Case Sensitive)

```sql
SELECT * FROM frontend where message ~ 'failing' LIMIT 9000;
```

* Match regular expression (Case Insensitive)

```sql
SELECT * FROM frontend where message ~* 'application' LIMIT 9000;
```

* Does not match regular expression (Case Sensitive)

```sql
SELECT * FROM frontend where message !~ 'started' LIMIT 9000;
```

* Does not match regular expression (Case Insensitive)

```sql
SELECT * FROM frontend where message !~* 'application' LIMIT 9000;
```

* Matches the beginning of the string (Case Insensitive)

```sql
SELECT * FROM frontend where message ~* '^a' LIMIT 9000;
```

* Matches the end of the string

```sql
SELECT * FROM frontend where message ~ 'failing$' LIMIT 9000;
```

* Matches numeric type data

```sql
SELECT * FROM frontend where uuid ~ '[0-9]' LIMIT 9000;
```

* Matches numeric type data (two digits)

```sql
SELECT * FROM frontend where uuid ~ '[0-9][0-9]' LIMIT 9000;
```

* Matches numeric type data (two digits)

```sql
SELECT * FROM frontend where uuid ~ '[0-9][0-9]' LIMIT 9000;
```

* Replace every instance of the numeric type data with the symbol \*

```sql
SELECT REGEXP_REPLACE(uuid,'[0-9]','*','g') FROM frontend LIMIT 9000;
```

* When a Regex is run against a string, the REGEXP\_MATCHES() function compares the two and returns the string that matches the pattern as a set.

```sql
SELECT REGEXP_MATCH(email,'@(.*)$')  FROM frontend where email is not null LIMIT 10;
```

* Postgres regex numbers only: Use the REGEXP\_REPLACE() function to extract only the numbers from a string in PostgreSQL.

```sql
SELECT REGEXP_REPLACE(email,'\\D','','g') FROM frontend where email is not null LIMIT 10;
```

* Postgres regex split: SPLIT\_PART() function can split a string into many parts. To divide a string into several pieces, we must pass the String, the Delimiter, and the Field Number.

```sql
SELECT SPLIT_PART(email,'@',1) FROM frontend where email is not null LIMIT 10 -- return before @ from email;
SELECT SPLIT_PART(email,'@',2) FROM frontend where email is not null LIMIT 10 -- return after @ from email;
```

* Postgres Regex Remove Special Characters: Using the REGEXP\_REPLACE() function, all Special Characters from a supplied text can be eliminated.

```sql
SELECT REGEXP_REPLACE(email, '[^\\w]+','','g') FROM frontend where email is not null LIMIT 10;
```

* Functions and Operators in pattern matching: Like and other POSIX regular expressions are supported.

```sql
SELECT * FROM frontend where email LIKE '%test%' LIMIT 10;
SELECT * FROM frontend where email ~ '^test' LIMIT 10;
```

## Case sensitivity

Dataset column names are case sensitive. For example, if you send a log event like

```json
{
  "foo": "bar",
  "Foo": "bar"
}
```

Parseable will create two columns, `foo` and `Foo` in the schema. So, while querying, please refer to the fields as `foo` and `Foo` respectively. While querying, unquoted identifiers are converted to lowercase. To query column names with uppercase letters, they must be passed in double quotes. For example, when sending a query via the REST API, the following JSON payload will apply the `WHERE` condition to the column `Foo`:

```json
{
    "query":"select * from dataset where \"Foo\"=bar",
    "startTime":"2023-02-14T00:00:00+00:00",
    "endTime":"2023-02-15T23:59:00+00:00"
}
```

If you're querying Parseable via Grafana UI (via the [data source plugin](https://github.com/parseablehq/parseable-datasource)), you can use the following query to query the column `Foo`:

```sql
SELECT * FROM dataset WHERE "Foo" = 'bar'
```

## Query analysis

In some cases, you may want to understand the query performance. To view the detailed query execution plan, use the `EXPLAIN ANALYZE` keyword in the query. For example, the following query will return the query execution plan and time taken per step.

```json
{
	"query": "EXPLAIN ANALYZE SELECT * FROM frontend LIMIT 100",
	"startTime": "2023-03-07T05:28:10.428Z",
	"endTime": "2023-03-08T05:28:10.428Z"
}
```

## Response fields information with query results

To get the query result fields as a part of query API response, add the query parameter `fields=true` to the API call, e.g. `http://localhost:8000/api/v1/query?fields=true`.

For example, for a query like `select count(*) as count from app1`, with the query parameter added will respond like this:

```json
{
    "fields": [
        "count"
    ],
    "records": [
        {
            "count": 2
        }
    ]
}
```


# Release notes (/docs/release-notes)





















































## v2.5 (December 8, 2025)

**Parseable v2.5.0** is here! This major update significantly expands our platform capabilities, introducing a dedicated **Trace View**, a **Metrics View**, and powerful AI-native integrations connecting Keystone with the alerting ecosystem.

### 1. Trace View Implementation

We have unlocked a new dimension of observability with the introduction of the **Trace View**. This feature is designed to help you visualize the complete lifecycle of requests as they traverse your distributed systems, making it easier than ever to diagnose latency issues and bottlenecks.

* **Full Trace Visualization:** Users can now view comprehensive waterfall charts of traces, providing deep visibility into service interactions.
* **Enhanced Navigation:** We added intuitive breadcrumbs to the Traces Span detail sheet, allowing for seamless navigation through complex span hierarchies.
* **OpenTelemetry Standardization:** Trace field names for events and links have been updated to align strictly with OpenTelemetry standards, ensuring consistent data ingestion and better interoperability.

<img alt="" src={__img0} placeholder="blur" />
<img alt="" src={__img1} placeholder="blur" />

### 2. Metrics View

The Metrics experience has been overhauled to provide deeper insights and a more fluid user experience.

* **Data Consistency:** Attribute field names have been standardized across all metric types, simplifying queries and ensuring consistency across your data.

<img alt="" src={__img2} placeholder="blur" />
<img alt="" src={__img3} placeholder="blur" />

### 3. Keystone Integration with Alerts

We are bringing AI-native capabilities closer to your incident response workflow. Keystone is now tightly integrated with the alerting system.

* **Automated Investigation:** You can now initiate a Keystone analysis session directly from a triggered alert. This seamless handoff reduces the time between detecting an anomaly and understanding its root cause.

<img alt="" src={__img4} />

### 4. SQL Editor & Visualization

We have enhanced the SQL Editor to support more complex data exploration and reporting needs.

* **Table Chart Support:** We introduced the **'Table' chart type**, allowing you to visualize raw data rows directly within your dashboards for detailed reporting.
* **Multi-Dataset Expansion:** The SQL editor now supports up to **3 distinct datasets** simultaneously, enabling more complex joins and comparative analysis.
* **UX Enhancements:**
  * Added a **"Clear All"** button to instantly reset GroupBy selections, speeding up exploratory data analysis.
  * Improved state management for SQL editor tabs to prevent data loss when switching contexts.
  * Refined the `dbName` logic to better handle complex subqueries.

### 5. Alerting Improvements

The alerting engine has been optimized for performance and better context.

* **State History:** Parseable now saves the history of alert states, providing a valuable audit trail of when alerts fired, resolved, or changed status.
* **Contextual Alerts:** You can now include the `metric_name` context when creating alerts, making notifications more informative at a glance.
* **Performance & Clarity:** We optimized the underlying queries used for alert creation to reduce load and removed redundant text from notification messages for cleaner, easier-to-read alerts.

### 6. Bug Fixes

* **SQL Editor:** Fixed an issue where error messages were not being displayed when a query failed, ensuring users now see the correct feedback.
* **Visualization Logic:** Refined query data checks in the `GaugeStyleSection` to correctly respect `rangeTo` values for accurate gauge rendering.
* **Recents Management:** The "Recents" list now automatically cleans itself by removing entries that are no longer valid.
* **Timezones:** Fixed an issue with URL parameter handling to ensure selected timezones persist correctly during navigation.

## v2.4.3 (September 22, 2025)

We're excited to announce Parseable v2.4.3. This release was focussed on improving the user experience of using SQL via our SQL editor.

### New SQL editor

The SQL editor has a new sidebar to showcase all the columns and their types for fast lookups. After the query is run and results are available, you can now use the chart view customization options and add these charts to dashboards directly.

AI assistant, saved queries are now rearranged to the right side of the screen for better visibility and access.

<img alt="Dashboard SQL Chart Builder" src={__img5} placeholder="blur" />

<iframe width="560" height="315" src="https://www.youtube.com/embed/VjwFONGGqaE?si=hMkSWfwGWmfb4HfY" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />

<iframe width="560" height="315" src="https://www.youtube.com/embed/O_lyg-0wBFY?si=FdfyUFnVs1zkHiql" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />

### Create alerts from Dashboard

Visualization gives you a good idea of patterns forming, and many times you want to be alerted when these patterns cross a certain threshold. You can now create alerts directly from the dashboard.

Click on the "three dots" button in a dashboard tile and select "Create Alert" from the dropdown menu. You will be redirected to the Alert Builder page, where your current filters and group-by options are automatically applied. Once satisfied with the configuration, click "Create" to activate your alert.

<img alt="Create Alert from Dashboard" src={__img6} placeholder="blur" />

### Investigation flows

As you analyze the data in your dashboard, you may identify specific trends or anomalies that require further exploration. Our new investigation flows make it easy to dive deeper into the data. You can now drill down into the data from the Dashboard or a triggered Alert.

In a dashboard tile:

* Select the "Investigate" option under the "three dots" button in chart.
* You'll be redirected to the Explore Page of the dataset with the same filters and group by options as the chart.

<img alt="Investigate from Dashboard" src={__img7} placeholder="blur" />

From a triggered Alert:

* Select the "Investigate" option from the Triggered Alert page.
* You'll be redirected to the Explore Page of the dataset with the same filters and group by options as the chart along with the timeline of the alert.

<img alt="Investigate from Alert" src={__img8} placeholder="blur" />

## v2.4.1 (August 18, 2025)

We're thrilled to announce Parseable v2.4.1, packed with powerful new features that enhance monitoring, visualization, and data ingestion capabilities. This release introduces advanced alerting mechanisms, expanded dashboard visualization options, and native Protocol Buffer support.

### 1. Advanced Alert Types

Building on our alerting capabilities, v2.4.1 introduces three sophisticated alert types to help you proactively monitor your systems. [Learn more about Alerts](/docs/user-guide/alerting)

**Threshold Alerts**

* Set precise boundaries for your metrics.
* Trigger alerts when values exceed defined limits.
* Example: Alert when response time > 500ms.
* Configure multiple conditions with "Filter" and "Group by".

**Anomaly Detection**

<OfferingPills pro enterprise className="mb-4" />

* Leverage machine learning to automatically identify unusual patterns.
* No manual threshold configuration required.
* Detects deviations from normal behavior patterns.
* Reduces alert fatigue by focusing on genuine anomalies.

**Forecasting Alerts**

<OfferingPills pro enterprise className="mb-4" />

* Predict future metric values based on historical trends.
* Alert on expected limit violations before they occur.
* Enable proactive capacity planning.
* Example: Alert when disk space is predicted to run out in 24 hours.

### 2. New Dashboard Visualization Types

Expand your data visualization capabilities with four new chart types. [Learn more about Dashboards](/docs/user-guide/dashboards)

**Pie Charts**

* Visualize proportional data at a glance.
* Perfect for showing distribution across categories.
* Interactive legends with click-to-filter functionality

**Donut Charts**

* Modern alternative to pie charts with hollow center
* Display key metrics in the center space
* Ideal for showing completion percentages

**Gauge Charts**

* Real-time performance indicators
* Configurable color-coded segments for thresholds
* Support for custom ranges and units
* Perfect for KPI monitoring (CPU usage, memory utilization)

**Query Value**

* Display single, prominent metric values
* Ideal for highlighting critical KPIs
* Support for auto-formatting and precision control
* Color coding based on thresholds

**Enhanced Styling Options:**

* Custom color palettes for all chart types
* Configurable units and number formatting
* Threshold-based color coding
* Responsive design for all screen sizes

### 3. Protocol Buffer (Protobuf) Support

<OfferingPills pro enterprise className="mb-4" />

Native support for Protocol Buffer format significantly improves data ingestion efficiency:

**Key Benefits:**

* **Prometheus Compatibility Path**: Protobuf support is a crucial step towards enabling full Prometheus compatibility.
* **Reduced Bandwidth**: Up to 50% smaller payload sizes compared to JSON
* **Faster Processing**: Binary format enables quicker parsing
* **Type Safety**: Strong typing prevents data corruption

**Implementation:**

```bash
# Send protobuf encoded logs
curl -X POST https://parseable.example.com/api/v1/ingest \
  -H "Content-Type: application/x-protobuf" \
  -H "X-P-Stream: my-dataset" \
  --data-binary @logs.pb
```

### 4. Enhanced Column Support

Parseable now supports up to **1000 columns** per dataset, a significant increase from previous limits:

* **Maximum Columns**: Support for up to 1000 columns per dataset.
* **Recommended Threshold**: Beyond 800 columns, consider splitting the dataset into multiple datasets based on schema similarity or query patterns for optimal performance.
* **Hard Limit**: The server will reject ingestion requests with more than 1000 columns.

### Upgrade Instructions

```bash
# Docker
docker pull parseable/parseable:v2.4.1

# Kubernetes
kubectl set image deployment/parseable parseable=parseable/parseable:v2.4.1
```

## v2.4.0 (July 22, 2025)

It’s that time again, a new Parseable release, and this one’s big. We’re moving up from v2.3.x to v2.4.0. Read on for all the highlights, new features, and tips to get the most out of v2.4.0

### 1. AI Powered Summarization

<OfferingPills pro enterprise className="mb-4" />

We're excited to introduce AI-powered summarization, a powerful new feature designed to simplify data analysis and debugging in Parseable.

**How It Works:**

* Select any dataset within Parseable.

* Click on `Summarize my data` to automatically generate a concise overview of your data.

<img alt="" src={__img9} placeholder="blur" />

* The AI identifies key patterns, anomalies, and potential faults in your dataset.

* Receive actionable recommendations and SQL queries to drill deeper into specific issues directly from the summary.

<iframe width="560" height="315" src="https://www.youtube.com/embed/mKjn_uNLZV0?si=J2A1SmWiQERsalMs" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />

**Benefits:**

* Quickly gain insights without manually combing through extensive datasets.

* Reduce troubleshooting time by pinpointing anomalies and root causes effortlessly.

* Simplify collaboration by sharing clear, concise summaries across your team.

* Leverage AI-driven recommendations to proactively address issues before they escalate.

**Example:**

Imagine you’re troubleshooting elevated error rates in your logs. With AI-powered summarization, Parseable instantly highlights:

* An unusual spike in errors between specific timestamps.

* Affected services and hosts.

* Suggested SQL queries to drill down further, such as:

```sql
SELECT host, COUNT(*) as error_count
FROM logs
WHERE status='error' AND timestamp BETWEEN '2025-07-20T00:00:00' AND '2025-07-20T06:00:00'
GROUP BY host
ORDER BY error_count DESC;
```

### 2. User Groups

<OfferingPills pro enterprise className="mb-4" />

We’ve added **User Groups** to Parseable’s RBAC system to make access management enterprise ready.

<img alt="User Groups" src={__img10} placeholder="blur" />

**How It Works:**

* Create groups for teams, projects, or any logical set of users.

* Assign roles (Admin, Editor, Writer, Reader, Ingestor) to the entire group in one go.

* Users in a group instantly inherit all permissions assigned to that group.

**All previous RBAC rules remain unchanged:**

* Admin/Editor: Roles apply platform-wide (Editor is owner of all datasets but can’t manage users/groups or see cluster details).

* Writer/Reader: Assignable at the resource level—fine-grained access for specific datasets or resources.

* Ingestor: Can only be assigned at the dataset level (for managing ingest operations).

<img alt="" src={__img11} placeholder="blur" />

**Benefits:**

* No more repetitive, user-by-user role assignments.

* Simplifies audits and permission reviews.

**Example:**

Say your SRE team needs full write access to all logs, while support staff should only view error logs:

* Create an “SRE” group and give it Writer on all datasets.

* Create a “Support” group with Reader on the errors dataset.

* Onboard a new SRE? Just add them to the group—done.

### 3. Introducing Dashboards in Parseable

Dashboards are here! Now you can visualize your data in Parseable, your way.

<img alt="" src={__img12} placeholder="blur" />

**How It Works:**

* **Start from the Side Nav:** Head over to Dashboards in the sidebar and hit Create New.

* **Name & Tag:** Give your dashboard a name and a tag (for easy organizing), then click Create Dashboard.

* **Build Your Canvas:** Select your new dashboard to land on the dashboard canvas. Click Add Tiles to start building charts.

* **Chart Builder Flow:** Choose your chart type: Timeseries, Line, Bar, or Area.

<img alt="" src={__img13} placeholder="blur" />

* Select the dataset you want to visualize.

* See a live preview as you build.

* Pick the plot fields from your dataset, aggregate/group/sort on the x-axis, and set your y-axis (typically count, time, or number).

* Want a quick table instead? Just click Table in the top right, skip the chart setup!

* Style your chart as you like, then hit Create.

* **Save and Favorite:** Add as many tiles as you need, then save your dashboard. You can also mark dashboards as favorites for quick access later.

**Benefits:**

* Instantly visualize logs and metrics, no need to export or use external tools.

* Flexible charting with live previews and quick customization.

* Organize dashboards by tags, share them with your team, and pin your favorites.

**Example:**

* Want to monitor API error rates over time?

* Create a dashboard called “API Health,” tag it “ops.”

* Add a Timeseries chart for error counts from your logs.

* Save it, mark as favorite—and you’ve got a live, auto-updating view for your team.

### 4. All-New Onboarding Wizard

Getting started with Parseable just got a whole lot easier. With this release, we’ve overhauled the first-time user experience:
<img alt="" src={__img14} placeholder="blur" />
<img alt="" src={__img15} placeholder="blur" />

**How It Works:**

* Right after installation, you’re greeted by an onboarding wizard.

* In just 3 minutes, the wizard sets up everything you need to explore Parseable:

  * **Demo Data:** A ready-made dataset of 5,000 events.

  * **Pre-configured Alerts:** See how to catch spikes and anomalies out of the box.

  * **Interactive Dashboards:** Instantly visualize and play with your sample data.

  * **Practical Saved Filters:** Jump straight into real-world troubleshooting examples.

  * **Example SQL Queries:** Learn how to slice and dice your data with practical queries.

### 5. Native GCP Object Store Support

Parseable now supports Google Cloud Storage (GCS) as a native object store backend.

**How It Works:**

* Set the following environment variables when starting Parseable:

```bash
GOOGLE_APPLICATION_CREDENTIALS=/parseable/svc/${GCS_CREDENTIALS_FILE:-key.json}
P_GCS_BUCKET=<your-bucket-name>
```

* Parseable will use your specified GCS bucket for all data storage.

## v2.3.5 (June 26, 2025)

We’re excited to roll out Parseable **v2.3.5**, a release packed with features that make exploring, debugging, and managing your observability data simpler and more powerful than ever. Here’s everything new:

### 1. **Filters & Group By: Slice, Dice, and Save Your Logs**

**What’s new?**
You can now filter and group logs directly from the log explorer using a flexible, built-in filter panel. Not only can you **filter logs by any field** (e.g., `service=payments`, `env=prod`), you can also **group them by any field** to spot patterns and outliers fast.

<img alt="" src={__img16} placeholder="blur" />

**How it works:**

* **Build a filter:** Type in the filter panel just like a search box—e.g., `status=error AND region=us-west-2`.
* **Add a group by:** Instantly group results by `error_code` or `user_id` to see which issues are most frequent or which users are affected.
  <img alt="" src={__img17} placeholder="blur" />
* **Save filter views:** Liked what you built? Click “Save to Library” and name the view (e.g., `Payments Errors Last Week`). Next time, just apply it from the Library to debug similar issues—no more rebuilding filters from scratch.
  <img alt="" src={__img18} placeholder="blur" />

**Example:**
Troubleshooting an incident in the `payments` service?

* Filter: `service=payments AND status=error`
* Group by: `error_code`
* Result: A quick tally of error types, so you can spot if a particular error is spiking.

**Benefits:**

* Saved filters help you build a library of ready-to-use “debug recipes.”
* The panel is as easy as typing, no complex query syntax required.
* Perfect for SREs and devs who want fast, repeatable root cause analysis.

### 2. **AI-Powered Forecasts—Now Available for Filters**

<OfferingPills pro enterprise className="mb-4" />

We’ve extended our **AI-based ingestion forecasting** to work with *any* filter you apply. This means you can select a filtered view (e.g., just logs for a specific team or region) and get **automatic predictions** for future log volumes based on your selection.

**Benefits:**

* Filter logs to `env=prod AND region=eu-central-1`
* Instantly see a chart forecasting ingestion volume for just those logs
* Plan ahead for traffic spikes, storage needs, or incident response
* No more guessing how much your filtered logs will grow over time!

### 3. **Field Stats: Occurrence Counts & Drill Down Made Easy**

You can now see detailed stats for any field in your telemetry, right in the UI. For every field (like `status`, `endpoint`, `customer_id`), Parseable shows:

* **Count of unique values** (e.g., how many different status codes?)
* **Frequency/occurrence** of each value (e.g., how many times did `status=error` appear?)
* **Order and drill down**: Click any value to instantly filter logs to just that slice.

<img alt="" src={__img19} placeholder="blur" />

**Example:**
Investigating API failures?

* Click `status` → see all possible values (e.g., `200`, `404`, `500`) and how often each occurred
* Click on `500` → now you’re only seeing server errors, ready to debug further
* Combine with group by `endpoint` to see which routes are most affected

Here's a demo video showcasing the filters feature:

<YouTubeEmbed videoId="btme5j9kzKY" />

### 4. **Multi-Role Support for OIDC Users**

Teams often need flexible, fine-grained access control—now Parseable’s OIDC integration supports **assigning multiple roles to a single user**.

**Benefits:**

* Give a DevOps engineer both `admin` and `reader` roles for different datasets
* Grant a user `editor` + `reader` permissions, so they can review logs across datasets without manual role shuffling
* All roles are respected in UI and API, just assign them in your OIDC provider and Parseable does the rest

## v2.3.3 (June 17, 2025)

### Performance Improvements

* **Optimized Conversion Task Assignment**: Improved the conversion task system to assign a definite set of arrow files for each conversion task, preventing multiple tasks from processing the same files during heavy loads.

* **Parallel Object Store Sync**: Enhanced object store synchronization to run in parallel for each dataset, significantly improving performance under heavy loads compared to the previous sequential approach.

* **Full Core Utilization**: Increased thread allocation for conversion and sync task handlers from 2 threads to utilizing all available server cores, resulting in better overall performance of conversion and sync workflows.

* **Startup Recovery Process**: Added a conversion and sync task that runs at server startup to process any pending files that weren't processed due to unplanned server shutdowns, improving system resilience.

### Bug Fixes

* **Fixed Poison Errors**: Resolved issues with poison errors that occurred when write locks acquired by ingestion threads panicked.

## v2.3.2 (June 3, 2025)

### New Features

Today is a big milestone for us at Parseable. With the release of Parseable v2.3.2, we're not just adding new features, we're officially welcoming AI to the heart of your observability workflows. This release marks our very first step into AI-powered developer tools, making it even easier to explore, query, and anticipate your data. Whether you're a SQL pro or a newcomer, or simply want to stay ahead of your growing telemetry, v2.3.2 brings smarter, more intuitive capabilities straight into your workflow.

### AI Assistant for SQL Editor

If you've ever stared at a blinking cursor in the SQL editor, wondering how to build the right query for your latest troubleshooting adventure, you're not alone. With Parseable v2.3.2, you now have an AI-powered sidekick right inside your SQL editor.

Here's what's new:

* **Query in Plain English**: Simply tell the assistant what you want, "show me all error logs for the last hour grouped by host," and it'll generate the SQL for you.

* **Multiple LLM Providers**: We know teams have preferences and constraints, so you can pick your favorite large language model (LLM) from the settings page. Out of the box, we support:
  * OpenAI GPT
  * Anthropic Claude

* **Plug-and-Play Configuration**: No extra setup headaches. Add your provider key, set your preferences, and you're ready to start querying.

This feature isn't just about convenience, it's about making data exploration accessible to everyone on your team, from SREs to product managers. The AI Assistant means faster queries, less context-switching, and more time for actual problem-solving.

### Chat with AI

At the bottom of your SQL editor, you'll now see a "Generate with AI" button. Use this to ask anything from:

* "Show me the number of 5xx errors grouped by host for the last hour"
* "Fix this query, it's giving a syntax error"
* "Summarize response statuses per environment tag"

The assistant understands context from your current datasets and query history, giving you results tailored to what you're working on. It also comes in handy when onboarding new team members. Junior engineers or analysts often need help crafting their first few queries. With the AI assistant, they can describe what they're looking for in plain language, like "Find the top 5 most common user agents in the backend table and how many times each appears?" and get an immediate, working query they can tweak and learn from.

Even seasoned users benefit when dealing with complex joins, window functions, or new datasets they haven't touched before. You can prompt the assistant with "Can you help me write a query that shows trends in status codes over time, grouped by host and tag-environment, and highlights spikes in error responses?" and get a scaffolded SQL with placeholders or editable sections you can refine.

In high-pressure situations, like an ongoing incident, the AI assistant acts as a query co-pilot. It reduces cognitive load, speeds up iteration, and lowers the risk of human error when time is critical. And because you can configure your preferred LLM in the settings, teams can balance performance, compliance, and cost based on their stack.

<img alt="" src={__img20} placeholder="blur" />

### Chat History

Every prompt and response is automatically saved. Click the "History" tab in the assistant panel to revisit, rerun, or refine past prompts. To make your workflow even smoother, Parseable also stores the full history of your AI interactions. Every prompt you've sent to the assistant, whether it's fixing a query, generating one from scratch, or just exploring a new dataset is saved alongside the responses. This means you can revisit past queries, reuse them in future investigations, or track how a particular issue evolved over time.

This is especially useful during incident retrospectives or recurring analytics, you'll never lose a good query again.

<img alt="" src={__img21} placeholder="blur" />

### The Library (Saved SQL, Now Smarter)

With Parseable 2.3.0, saved SQL queries live in the new Library. You can now:

* Save queries you want to reuse
* Edit queries with the help of AI
* Run them directly from the library pane
* Explain what a query does using the assistant

The library is your personal or team-wide knowledge base for telemetry insights.

<img alt="" src={__img22} placeholder="blur" />

### Failed Query? Let AI Fix It

Let's say you're investigating a sudden spike in latency reported by your alerting system. You jump into Parseable, type a rough query to check average response times, but something's off, either the field doesn't exist or the aggregation logic is incorrect. Instead of trial-and-error debugging, you can now ask the AI assistant:

"Fix with AI"

<img alt="" src={__img23} placeholder="blur" />

The assistant returns a corrected version using the correct percentile function and known schema fields, saving minutes or even hours of digging through docs and schema dumps.

This turns errors into learning moments and lets you recover faster in the middle of a high-pressure incident.

### Forecasting for Log Ingestion

Ever wish you could see into the future of your observability pipeline? Along with AI assisted SQL queries, now you can forecast the future ingestion load, with Parseable's new forecasting for log ingestion.

<img alt="" src={__img24} placeholder="blur" />

What this means for you:

* **Data-Driven Forecasts**: Our forecasting engine uses your recent log ingestion patterns to predict what's coming next. Enable it, and you'll see projected ingestion volumes right in your dashboards.

* **Smarter Planning**: Spot upcoming spikes before they happen. Plan capacity, staffing, and alerting based on real forecasts, not just yesterday's numbers.

* **Visualized Right Where You Need It**: Forecasts appear directly in the Parseable Explore UI, so you can compare historical and predicted loads at a glance.

Whether you're scaling infrastructure or just want to avoid surprises, forecasting helps you move from reactive to proactive.

## v2.3.1

### Highlights

* Global search datasets, saved filters, SQL snippets… anything Parseable tracks.
* 𝗣\_𝗠𝗔𝗫\_𝗙𝗟𝗔𝗧𝗧𝗘𝗡\_𝗟𝗘𝗩𝗘𝗟 env var to configure nested lists; default depth is 10, but you call configure as per your use-case.

## v2.3.0

### Enhancements

* SQL editor visualisation - SQL editor page allows slicing and dicing data exactly as you wish. We now added visualisation capabilities to the SQL editor. After running a query, you can either inspect the raw rows or quickly switch to a visual chart for better pattern recognition.

* Home chart improvements - Landing page shows a high level overview of your Parseable instance. We have now enhanced the overview section with deeper insights into total ingestion, compression and storage details.

* We’ve also improved the search API response in the sidebar, so you can quickly look up saved filters, alerts, datasets among others.

* Streaming response - We have now added support for streaming response for query. This improves responsiveness for queries that involve downloading larger data chunks. This is available as a flag for the query API. Refer to the Parseable docs on how to use this API.

### Enterprise updates

* Schema detection improvements: Parseable Enterprise edition supports automatic schema detection. The server identifies formats sent by a client when a header is set. Server also validates if the format is actually the same as set by header. This allows a consistent experience on the server side - so users can reliably build dashboards, alerts and other visualisations without being concerned about an offending client.

* In some cases where the format doesn’t match the header specified, we now added support for a column that marks this result. You can now decide to use the mismatched data or not based on the value of p\_format\_verified.

* LLM configuration across roles - As we proceed our journey of adding native Large Language Model (LLM) support to improve MTTR and leverage user’s time better. We have now added user specific actions to add LLM config.

* This means every user can have a separate LLM key and related config and use their config for their tasks with complete isolation from other user’s actions, history etc.

### Bug Fixes

* Timezone handling explore page - Fix timezone management on log explore page ensuring accurate log display aligned to user-selected timezones.

* Settings page access - Ensured the Settings page is consistently accessible to all users, addressing previous visibility inconsistencies.

* Loaders & error states - Added loading indicators and improved error messaging on user and dataset pages, resulting in a clearer user experience during data fetching and error scenarios.

* Distinct SQL query in Datasets API - Corrected SQL queries to accurately fetch distinct values, improving dataset API responses.

* Date stats deletion fix - Fixed deletion issues in date-level statistics, enhancing data consistency.

* Date level stats fix - Addressed inaccuracies in date-level statistics calculation, ensuring reliable data insights.

* Reject events when the dataset has too many fields - Implemented validation to reject events with more than 250 fields, improving platform stability.

* Allow invalid certificates - Allowed intra-cluster communication using invalid certificates, easing integration scenarios.

### Enterprise fixes

* ALB Log Regex Fix - Resolved regex parsing issues for ALB logs, ensuring accurate log ingestion.

* Create Index Form Validation - Fixed validation logic in the Create Index form, resolving form submission issues and improving user feedback during index creation.
  b


# API Reference (/docs/api)



import { Card, Cards } from 'fumadocs-ui/components/card';

This section provides detailed information about the available API endpoints for interacting with Parseable.

## Getting Started

Before you begin, make sure you have:

* A running instance of Parseable
* The base URL of your Parseable server
* Required authentication credentials (if authentication is enabled)

## API Endpoints

<Cards>
  <Card href="/docs/api/v1/logstream/stream_name/put" title="Create log dataset">
    Create a new log dataset with the specified name and configuration.
  </Card>

  <Card href="/docs/api/v1/logstream/stream_name/post" title="Send logs to a dataset">
    Send logs to an existing log dataset.
  </Card>

  <Card href="/docs/api/v1/logstream/stream_name/delete" title="Delete log dataset">
    Delete an existing log dataset and all its associated data.
  </Card>

  <Card href="/docs/api/v1/ingest" title="Ingest logs with headers">
    Send log data to a specific log dataset using HTTP headers.
  </Card>

  <Card href="/docs/api/v1/query" title="Query API">
    Query data from log streams using SQL.
  </Card>
</Cards>

## Authentication

All API requests require authentication. Include your API key in the `Authorization` header:

```bash
Authorization: Bearer YOUR_API_KEY
```

## Rate Limiting

API requests are subject to rate limiting. The default rate limit is 100 requests per minute per IP address.

## Error Handling

All error responses follow a standard format:

```json
{
  "error": {
    "code": "error_code",
    "message": "Human-readable error message"
  }
}
```

## Need Help?

If you have any questions or run into issues, please refer to our [GitHub repository](https://github.com/parseablehq/parseable) or [join our community](https://discord.gg/parseable).


# Alertmanager (/docs/alerting/alert-manager)



### Overview

[Alertmanager](https://github.com/prometheus/alertmanager) handles alerts sent by client applications such as the Parseable server. Alertmanager takes care of deduplicating, grouping, and routing them to the correct receiver integration such as email, PagerDuty, or OpsGenie.

Parseable alerts can be sent to Alertmanager to allow advanced alert management and notification routing.

### Prerequisites

* Parseable server installed and running. See [installation guide](/docs/self-hosted/installation) for more details.
* Alertmanager installed and running. See [installation and setup guide](https://github.com/prometheus/alertmanager) for more details.

### Configuration

To configure Parseable alerts to be sent to Alertmanager, use the alertmanager [target type](/docs/user-guide/alerting#alertmanager) in Parseable alert configuration.

This is a snippet of Parseable alert configuration, to demonstrate the fields required to send alerts to Alertmanager.

```json
{
    "name":"AlertManagerTarget",
    "type": "alertManager",
    "endpoint": "https://some.webhook.com",
    "username": "username",
    "password":"password",
    "skipTlsCheck": true,
    "notificationConfig": {
        "interval": 3,
        "times": 7
    }
}
```

The `endpoint` field is the URL of the Alertmanager API endpoint. The `username` and `password` fields are the credentials for basic authentication. The `skipTlsCheck` field is a boolean to skip TLS certificate verification. The `notificationConfig` field is used to repeat the alert notification. If it is not set, Parseable will send the notification just once.

Once Parseable alerts are configured to be sent to Alertmanager, you can use Alertmanager to manage the alerts. For example, you can use Alertmanager to route alerts to different receivers, such as email, PagerDuty, or OpsGenie. You can also use Alertmanager to silence alerts.


# Agentic Observability (/docs/cookbook/agentic-observability)



## Agentic Observability

Learn how to monitor AI agents and LLM-powered applications with Parseable.

### Overview

As AI agents become more prevalent, observability becomes critical for understanding their behavior, debugging issues, and ensuring reliability.

### Key Metrics to Track

* **Token Usage** - Monitor input/output tokens per request
* **Latency** - Track response times for LLM calls
* **Error Rates** - Monitor failed requests and retries
* **Cost** - Track API costs across different models

### Best Practices

1. Log all LLM interactions with full context
2. Track tool calls and their outcomes
3. Monitor agent decision paths
4. Set up alerts for anomalous behavior


# Instrumentation (/docs/cookbook/instrumentation)



## Instrumentation Guide

Learn how to properly instrument your applications for effective observability with Parseable.

### Structured Logging

Always use structured logging formats like JSON:

```json
{
  "timestamp": "2024-01-15T10:30:00Z",
  "level": "info",
  "message": "User logged in",
  "user_id": "user-123",
  "ip_address": "192.168.1.1",
  "duration_ms": 45
}
```

### Key Fields to Include

* **timestamp** - When the event occurred
* **level** - Log level (debug, info, warn, error)
* **message** - Human-readable description
* **correlation\_id** - For tracing requests across services
* **service** - Name of the service generating the log

### Best Practices

1. Use consistent field names across services
2. Include context with every log entry
3. Avoid logging sensitive data
4. Use appropriate log levels
5. Include timing information for performance analysis

### Integration Examples

See the [Logging Agents](/docs/ingest-data/logging-agents) and [OpenTelemetry](/docs/ingest-data/otel) sections for integration guides.


# Tool Calls (/docs/cookbook/tool-calls)



## Tool Calls Observability

Track and analyze tool calls made by AI agents to understand their behavior and debug issues.

### What are Tool Calls?

Tool calls are function invocations made by AI agents to interact with external systems, APIs, or perform specific actions.

### Logging Tool Calls

```json
{
  "timestamp": "2024-01-15T10:30:00Z",
  "agent_id": "agent-123",
  "tool_name": "search_database",
  "input": {"query": "user data"},
  "output": {"results": 42},
  "duration_ms": 150,
  "status": "success"
}
```

### Key Metrics

* **Call Frequency** - How often each tool is called
* **Success Rate** - Percentage of successful tool calls
* **Latency** - Time taken for tool execution
* **Error Types** - Common failure modes

### Best Practices

1. Log both input and output of tool calls
2. Include timing information
3. Track the agent context for each call
4. Set up alerts for high failure rates


# Parseable Enterprise (/docs/enterprise)



## Core infrastructure for mission-critical deployments

Core infrastructure projects, especially those that deal with data and need to guarantee data protection and reliability of the highest order, take time to build. Over the last 3 years while building ParseableDB, we've seen a wide range of edge cases, bug reports, weird behavior, and more.

The time is right to create an enterprise-grade offering, built on the solid foundation of AGPLv3 ParseableDB. With a dedicated, well-defined Enterprise offering, we'll be able to serve serious, mission-critical users much better, while improving the sustainability of the OSS product. It helps us derive some value from our work without pulling the rug from under the community.

**Sustainable open source. No drama. No bait-and-switch. Just fast, efficient, observability.**

## Parseable OSS vs. Enterprise Edition

### Parseable OSS

* High performance
* Single binary with built-in Prism
* RBAC and OIDC integrations
* Regular updates and feature releases based on community feedback
* Perfect for individuals, smaller teams, and non-mission-critical deployments

### Enterprise Edition

**Everything in OSS, plus:**

* Hardened, stable builds
* Searching on demand
* Distributed query support
* Built-in schema detection for log formats
* AI Native summarization, alerts, and correlation (coming soon, talk to us for a preview)
* High touch onboarding, O11Y data modeling, and 24/7 support
* Predictable pricing model

## How to access Parseable Enterprise

Drop us a note at [sales@parseable.com](mailto:sales@parseable.com) to set up a quick discovery call and discuss your needs.

Want to try before you buy? You can check out the enterprise features at [demo.parseable.com](https://demo.parseable.com).

Whether you're an indie developer building the next big thing or an enterprise scaling observability across a global infrastructure, we've got you covered. Let's build something awesome together!


# Enterprise Features (/docs/flavours/enterprise)



<OfferingPills enterprise className="mb-4" />

Parseable Enterprise is for mission-critical workloads requiring advanced observability. Available as Parseable Cloud, BYOC (Bring Your Own Cloud), or On-Premises deployment. Custom pricing with minimum $999/month.

## Data Infrastructure

| Feature                                 | Description                                  | Availability                                            |
| --------------------------------------- | -------------------------------------------- | ------------------------------------------------------- |
| Max Recommended Ingestion               | Total ingestion across logs, metrics, traces | Unlimited                                               |
| Query Volume                            | Volume of data scanned for queries           | 20x of ingested volume included, additional at $0.02/GB |
| [Retention](/docs/user-guide/retention) | Retention of ingested data                   | Customizable                                            |
| Infrastructure                          | Cloud provider and region                    | Dedicated infrastructure with data residency options    |
| Deployment Options                      | Where Parseable runs                         | Parseable Cloud, BYOC, or On-Premises                   |

## Native Intelligence

| Feature                                                     | Description                                  | Availability |
| ----------------------------------------------------------- | -------------------------------------------- | ------------ |
| [Keystone](/docs/user-guide/ai-native/keystone)             | Natural language Q\&A for observability data | ✅            |
| [Anomaly Detection](/docs/user-guide/alerting/anomaly)      | ML-based unusual pattern detection           | ✅            |
| [Summarization](/docs/user-guide/ai-native/summary)         | One-click data insights                      | ✅            |
| [Forecasting Alerts](/docs/user-guide/alerting/forecasting) | Alerts based on predicted patterns           | ✅            |
| [AI SQL Generation](/docs/user-guide/ai-native/text-to-sql) | Generate SQL from natural language           | ✅            |

## Enterprise Features

| Feature                                                | Description                                         | Availability |
| ------------------------------------------------------ | --------------------------------------------------- | ------------ |
| [Role Based Access Control](/docs/user-guide/rbac)     | Granular access controls for users and teams        | ✅            |
| Bring Your Own \[Cloud, LLM, OAuth]                    | Use your own cloud, LLM, or OAuth system            | ✅            |
| Team Quotas                                            | Configure ingestion, scanning, and retention quotas | ✅            |
| SLA/SLO Configuration                                  | Native SLA/SLO setup                                | ✅            |
| MTTD/MTTR Metrics                                      | Track Mean Time to Detect and Resolve               | ✅            |
| Audit Logging                                          | Complete audit trail                                | ✅            |
| Live Tailing                                           | Real-time log streaming                             | ✅            |
| [Smart Cache](/docs/user-guide/smart-cache)            | Sub-second queries with configurable caching        | ✅            |
| [Custom Partitioning](/docs/key-concepts/partitioning) | Optimize query performance                          | ✅            |

## Support

| Feature                    | Description                          | Availability |
| -------------------------- | ------------------------------------ | ------------ |
| Architectural Support      | Engineering guidance and consulting  | ✅            |
| Product Support            | 24x7 access to support teams         | ✅            |
| Ingestion Agent Management | Setup and management assistance      | ✅            |
| Dedicated SLA              | Guaranteed uptime and response times | ✅            |

## Getting Started

<Cards>
  <Card href="mailto:sales@parseable.com" title="Contact Sales">
    Set up a discovery call to discuss your needs
  </Card>

  <Card href="https://logg.ing/quick-chat" title="Quick Chat">
    Schedule a quick conversation with our team
  </Card>
</Cards>


# OSS Features (/docs/flavours/oss)



Parseable OSS is the open-source edition of Parseable, licensed under AGPLv3. It provides a high-performance, cost-effective solution for log analytics. **Free forever**.

## Data Infrastructure

| Feature                                 | Description                                  | Availability               |
| --------------------------------------- | -------------------------------------------- | -------------------------- |
| Ingestion                               | Total ingestion across logs, metrics, traces | Unlimited                  |
| Query Volume                            | Volume of data scanned for queries           | Unlimited                  |
| [Retention](/docs/user-guide/retention) | Retention of ingested data                   | Configurable               |
| [Storage](/docs/key-concepts/storage)   | Object storage backend                       | S3, GCS, Azure Blob, MinIO |

## Core Features

| Feature                                                          | Description                         | Availability |
| ---------------------------------------------------------------- | ----------------------------------- | ------------ |
| [Role Based Access Control](/docs/user-guide/rbac)               | User and role management            | ✅            |
| [Threshold Alerts](/docs/user-guide/alerting/standard-threshold) | Alert when metrics cross thresholds | ✅            |
| [Dashboards](/docs/user-guide/dashboards)                        | Custom visualization dashboards     | ✅            |
| [SQL Query](/docs/key-concepts/query)                            | PostgreSQL-compatible SQL queries   | ✅            |
| [Datasets](/docs/key-concepts/data-model)                        | Logical grouping of telemetry data  | ✅            |
| [OpenID Connect](/docs/user-guide/openid)                        | SSO authentication                  | ✅            |

## Not Available in OSS

| Feature                                                           | Available In    |
| ----------------------------------------------------------------- | --------------- |
| [Keystone](/docs/user-guide/ai-native/keystone)                   | Pro, Enterprise |
| [Anomaly Detection](/docs/user-guide/alerting/anomaly)            | Pro, Enterprise |
| [Forecasting Alerts](/docs/user-guide/alerting/forecasting)       | Pro, Enterprise |
| [AI SQL Generation](/docs/user-guide/ai-native/text-to-sql)       | Pro, Enterprise |
| [Summarization](/docs/user-guide/ai-native/summary)               | Pro, Enterprise |
| [Smart Cache](/docs/user-guide/smart-cache)                       | Pro, Enterprise |
| [Custom Partitioning](/docs/key-concepts/partitioning)            | Enterprise      |
| [High Availability Cluster](/docs/key-concepts/high-availability) | Pro, Enterprise |
| Team Quotas                                                       | Enterprise      |
| 24x7 Support                                                      | Enterprise      |

## Getting Started

```bash
curl -fsSL https://logg.ing/install | bash
```

Or run with Docker:

```bash
docker run -p 8000:8000 \
  -v /tmp/parseable/data:/parseable/data \
  -v /tmp/parseable/staging:/parseable/staging \
  -e P_FS_DIR=/parseable/data \
  -e P_STAGING_DIR=/parseable/staging \
  parseable/parseable:latest \
  parseable local-store
```

## Community & Support

<Cards>
  <Card href="https://logg.ing/community" title="Join Slack Community">
    Get help, share feedback, and connect with other users
  </Card>

  <Card href="https://github.com/parseablehq/parseable" title="GitHub Repository">
    View source code, report issues, contribute
  </Card>
</Cards>


# Pro Features (/docs/flavours/pro)



<OfferingPills pro className="mb-4" />

Parseable Pro is our fully managed cloud offering at **$0.37 per GB ingested** (minimum $29/month). It provides enterprise-grade features with managed infrastructure so you can focus on your applications.

## Data Infrastructure

| Feature                                 | Description                                  | Availability                                            |
| --------------------------------------- | -------------------------------------------- | ------------------------------------------------------- |
| Max Recommended Ingestion               | Total ingestion across logs, metrics, traces | Up to 30 TB/month                                       |
| Query Volume                            | Volume of data scanned for queries           | 10x of ingested volume included, additional at $0.02/GB |
| [Retention](/docs/user-guide/retention) | Retention of ingested data                   | 21 days                                                 |
| Infrastructure                          | Cloud provider and region                    | Shared infrastructure                                   |

## Native Intelligence

| Feature                                                     | Description                                  | Availability |
| ----------------------------------------------------------- | -------------------------------------------- | ------------ |
| [Keystone](/docs/user-guide/ai-native/keystone)             | Natural language Q\&A for observability data | ✅            |
| [Anomaly Detection](/docs/user-guide/alerting/anomaly)      | ML-based unusual pattern detection           | ✅            |
| [Summarization](/docs/user-guide/ai-native/summary)         | One-click data insights                      | ✅            |
| [Forecasting Alerts](/docs/user-guide/alerting/forecasting) | Alerts based on predicted patterns           | ✅            |
| [AI SQL Generation](/docs/user-guide/ai-native/text-to-sql) | Generate SQL from natural language           | ✅            |

## Core Features

| Feature                                            | Description                                | Availability |
| -------------------------------------------------- | ------------------------------------------ | ------------ |
| [Role Based Access Control](/docs/user-guide/rbac) | User and role management                   | ✅            |
| [Alerting](/docs/user-guide/alerting)              | Threshold, Anomaly, and Forecasting alerts | ✅            |
| [Dashboards](/docs/user-guide/dashboards)          | Custom visualization dashboards            | ✅            |
| Unlimited Users                                    | No limit on team members                   | ✅            |
| Unlimited Hosts                                    | No limit on monitored hosts                | ✅            |

## Not Available in Pro

| Feature                                                   | Available In |
| --------------------------------------------------------- | ------------ |
| [Custom Partitioning](/docs/key-concepts/partitioning)    | Enterprise   |
| Custom Retention                                          | Enterprise   |
| [Smart Cache Configuration](/docs/user-guide/smart-cache) | Enterprise   |
| Dedicated Infrastructure                                  | Enterprise   |
| Data Residency Options                                    | Enterprise   |
| Team Quotas                                               | Enterprise   |
| SLA/SLO Configuration                                     | Enterprise   |
| Architectural Support                                     | Enterprise   |
| 24x7 Product Support                                      | Enterprise   |

## Getting Started

<Cards>
  <Card href="https://app.parseable.com" title="Start Free Trial">
    14-day free trial, no credit card required
  </Card>
</Cards>


# eBPF (/docs/ingest-data/zero-instrumentation)





[Tetragon](https://github.com/cilium/tetragon) is an open-source project from Cilium that provides runtime security, deep observability, and kernel-level transparency using eBPF. Tetragon monitors processes, syscalls, file and network activity in the kernel, correlating threats with network data to identify responsible binaries. It shares insights via JSON logs and a gRPC endpoint.

This Document will walk you through how to set up Tetragon Connector to extract eBPF logs on Parseable using Vector. It is used to build observability pipelines that collect, transform, and route logs, metrics, and traces.

<img alt="Tetragon" src={__img0} placeholder="blur" />

## Prerequisites

* A Kubernetes with admin accesss.
* Kubectl installed on your machine.

## Deploy Tetragon

You can deploy Tetragon using Helm on your Kubernetes cluster using the commands:

```bash
helm repo add cilium https://helm.cilium.io
helm repo update
helm install tetragon cilium/tetragon -n kube-system
```

## Deploy Vector

You can deploy Vector using Helm on your Kubernetes cluster. We have created a vector-tetragon-values.yaml file to configure Vector to collect logs from Tetragon and send them to Parseable.

```bash
helm repo add vector https://helm.vector.dev
wget https://www.parseable.com/blog/vector/vector-tetragon-values.yaml
helm install vector vector/vector --namespace vector --create-namespace --values vector-tetragon-values.yaml
```

It will take some time to deploy Vector. You can check the status using the command:

```bash
kubectl get pods -n vector
```

Now Vector is ready to send the events stored in `/var/run/cilium/tetragon/tetragon.log` file to the Parseable tetrademo dataset. Once this is done, you can verify the log events inPrism.

We have a blog post which guides you through the process of tracking sensitive file access using Tetragon and Parseable. You can read it here.


# Integrations (/docs/integrations)



import { IconChartBar, IconBell, IconCloud, IconLock, IconFileText, IconActivity, IconServer, IconBox, IconCode, IconDatabase, IconGitBranch, IconShield, IconRobot, IconApi } from '@tabler/icons-react';

Parseable integrates with 50+ tools and platforms across visualization, alerting, cloud providers, authentication, and more. Browse integrations by category below.

***

## Visualization

<Cards>
  <Card href="/docs/integrations/visualization/grafana" title="Grafana">
    Create dashboards and alerts with Parseable as a data source
  </Card>

  <Card href="/docs/integrations/visualization/metabase" title="Metabase">
    Self-service BI and analytics on your log data
  </Card>

  <Card href="/docs/integrations/visualization/apache-superset" title="Apache Superset">
    Open-source data exploration and visualization
  </Card>

  <Card href="/docs/integrations/visualization/tableau" title="Tableau">
    Enterprise analytics and visualization
  </Card>

  <Card href="/docs/integrations/visualization/redash" title="Redash">
    Connect and query your data sources
  </Card>

  <Card href="/docs/integrations/visualization/looker" title="Looker">
    Business intelligence and analytics
  </Card>
</Cards>

***

## Incident management

<Cards>
  <Card href="/docs/integrations/alerting/slack" title="Slack">
    Send alerts and notifications to Slack channels
  </Card>

  <Card href="/docs/integrations/alerting/pagerduty" title="PagerDuty">
    Incident management and on-call scheduling
  </Card>

  <Card href="/docs/integrations/alerting/opsgenie" title="Opsgenie">
    Alert and incident management
  </Card>

  <Card href="/docs/integrations/alerting/microsoft-teams" title="Microsoft Teams">
    Alert notifications to Teams channels
  </Card>

  <Card href="/docs/integrations/alerting/discord" title="Discord">
    Send alerts to Discord servers
  </Card>

  <Card href="/docs/integrations/alerting/email" title="Email">
    Email notifications for alerts
  </Card>

  <Card href="/docs/integrations/alerting/webhook" title="Webhook">
    Generic webhook for custom integrations
  </Card>
</Cards>

***

## Cloud providers

<Cards>
  <Card href="/docs/cloud-provider/aws/intro" title="AWS Overview">
    Getting started with AWS integrations
  </Card>

  <Card href="/docs/ingest-data/cloud/aws-cloudwatch" title="AWS CloudWatch">
    Ingest logs from CloudWatch
  </Card>

  <Card href="/docs/self-hosted/storage-targets/aws-s3" title="AWS S3">
    Store and query logs from S3
  </Card>

  <Card href="/docs/ingest-data/cloud/aws-kinesis" title="AWS Kinesis">
    Stream logs via Kinesis Data Firehose
  </Card>

  <Card href="/docs/cloud-provider/aws/aws-data-firehose" title="AWS Data Firehose">
    Direct integration with Data Firehose
  </Card>

  <Card href="/docs/cloud-provider/aws/lambda" title="AWS Lambda">
    Ingest Lambda function logs
  </Card>

  <Card href="/docs/ingest-data/cloud/azure-event-hubs" title="Azure Event Hubs">
    Ingest logs from Azure Event Hubs
  </Card>

  <Card href="/docs/cloud-provider/azure/api-service" title="Azure API Service">
    Azure API Management logs via Event Hub and Logic Apps
  </Card>

  <Card href="/docs/cloud-provider/azure/service-bus" title="Azure Service Bus">
    Ingest from Azure Service Bus
  </Card>

  <Card href="/docs/self-hosted/storage-targets/azure-blob-storage" title="Azure Blob Storage">
    Store logs in Azure Blob Storage
  </Card>

  <Card href="/docs/ingest-data/cloud/gcp-pubsub" title="Google Cloud Pub/Sub">
    Stream logs from GCP Pub/Sub
  </Card>

  <Card href="/docs/self-hosted/storage-targets/gcp-storage" title="Google Cloud Storage">
    Store logs in GCS
  </Card>

  <Card href="/docs/self-hosted/storage-targets/digitalocean-spaces" title="DigitalOcean Spaces">
    Object storage for logs
  </Card>
</Cards>

***

## Authentication

<Cards>
  <Card href="/docs/user-guide/openid" title="OAuth / OIDC">
    OpenID Connect authentication
  </Card>

  <Card href="/docs/integrations/auth/authentik" title="Authentik">
    Open-source identity provider
  </Card>

  <Card href="/docs/integrations/auth/keycloak" title="Keycloak">
    Open-source identity and access management
  </Card>

  <Card href="/docs/integrations/auth/okta" title="Okta">
    Enterprise identity management
  </Card>

  <Card href="/docs/integrations/auth/auth0" title="Auth0">
    Flexible authentication platform
  </Card>

  <Card href="/docs/integrations/auth/azure-ad" title="Azure AD">
    Microsoft Azure Active Directory
  </Card>

  <Card href="/docs/integrations/auth/google-workspace" title="Google Workspace">
    Google identity provider
  </Card>

  <Card href="/docs/integrations/auth/ldap" title="LDAP">
    Lightweight Directory Access Protocol
  </Card>
</Cards>

***

## Telemetry agents

<Cards>
  <Card href="/docs/ingest-data/logging-agents" title="Fluent Bit">
    Lightweight log processor and forwarder
  </Card>

  <Card href="/docs/ingest-data/logging-agents" title="Fluentd">
    Unified logging layer
  </Card>

  <Card href="/docs/ingest-data/logging-agents" title="Vector">
    High-performance observability data pipeline
  </Card>

  <Card href="/docs/ingest-data/logging-agents" title="Logstash">
    Server-side data processing pipeline
  </Card>

  <Card href="/docs/ingest-data/logging-agents/filebeat" title="Filebeat">
    Lightweight shipper for logs
  </Card>

  <Card href="/docs/ingest-data/logging-agents/promtail" title="Promtail">
    Log collector for Loki
  </Card>
</Cards>

***

## OpenTelemetry

<Cards>
  <Card href="/docs/ingest-data/otel" title="OTLP (HTTP)">
    OpenTelemetry Protocol over HTTP
  </Card>

  <Card href="/docs/ingest-data/otel" title="OTLP (gRPC)">
    OpenTelemetry Protocol over gRPC
  </Card>

  <Card href="/docs/ingest-data/otel" title="OTel Collector">
    OpenTelemetry Collector integration
  </Card>
</Cards>

***

## Streaming platforms

<Cards>
  <Card href="/docs/ingest-data/streaming/kafka" title="Apache Kafka">
    Distributed event streaming platform
  </Card>

  <Card href="/docs/ingest-data/streaming/redpanda" title="Redpanda">
    Kafka-compatible streaming platform
  </Card>

  <Card href="/docs/ingest-data/streaming/rabbitmq" title="RabbitMQ">
    Message broker
  </Card>

  <Card href="/docs/ingest-data/streaming/nats" title="NATS">
    Cloud-native messaging system
  </Card>

  <Card href="/docs/ingest-data/streaming/cribl" title="Cribl">
    Observability pipeline
  </Card>
</Cards>

***

## Container orchestration

<Cards>
  <Card href="/docs/ingest-data/containers/kubernetes" title="Kubernetes">
    Container orchestration platform
  </Card>

  <Card href="/docs/ingest-data/containers/docker" title="Docker">
    Container runtime logs
  </Card>

  <Card href="/docs/ingest-data/containers/amazon-ecs" title="Amazon ECS">
    Elastic Container Service
  </Card>

  <Card href="/docs/ingest-data/containers/amazon-eks" title="Amazon EKS">
    Elastic Kubernetes Service
  </Card>

  <Card href="/docs/ingest-data/containers/google-gke" title="Google GKE">
    Google Kubernetes Engine
  </Card>

  <Card href="/docs/ingest-data/containers/azure-aks" title="Azure AKS">
    Azure Kubernetes Service
  </Card>
</Cards>

***

## Programming languages

<Cards>
  <Card href="/docs/ingest-data/programming-languages" title="Python">
    Python logging integration
  </Card>

  <Card href="/docs/ingest-data/programming-languages" title="JavaScript">
    Node.js logging integration
  </Card>

  <Card href="/docs/ingest-data/programming-languages" title="Go">
    Go logging integration
  </Card>

  <Card href="/docs/ingest-data/programming-languages" title="Java">
    Java logging integration
  </Card>

  <Card href="/docs/ingest-data/programming-languages" title="Rust">
    Rust logging integration
  </Card>

  <Card href="/docs/ingest-data/programming-languages/ruby" title="Ruby">
    Ruby logging integration
  </Card>

  <Card href="/docs/ingest-data/programming-languages/php" title="PHP">
    PHP logging integration
  </Card>

  <Card href="/docs/ingest-data/programming-languages/dotnet" title=".NET">
    .NET logging integration
  </Card>
</Cards>

***

## Data systems

<Cards>
  <Card href="/docs/ingest-data/databases/postgresql" title="PostgreSQL">
    PostgreSQL metrics and logs
  </Card>

  <Card href="/docs/ingest-data/databases/mysql" title="MySQL">
    MySQL metrics and logs
  </Card>

  <Card href="/docs/ingest-data/databases/mongodb" title="MongoDB">
    MongoDB metrics and logs
  </Card>

  <Card href="/docs/ingest-data/databases/redis" title="Redis">
    Redis metrics and logs
  </Card>

  <Card href="/docs/ingest-data/databases/elasticsearch" title="Elasticsearch">
    Migrate from Elasticsearch
  </Card>
</Cards>

***

## DevOps

<Cards>
  <Card href="/docs/ingest-data/cicd/github-actions" title="GitHub Actions">
    CI/CD pipeline logs
  </Card>

  <Card href="/docs/ingest-data/cicd/gitlab-ci" title="GitLab CI">
    GitLab pipeline logs
  </Card>

  <Card href="/docs/ingest-data/cicd/jenkins" title="Jenkins">
    Jenkins build logs
  </Card>

  <Card href="/docs/ingest-data/cicd/circleci" title="CircleCI">
    CircleCI pipeline logs
  </Card>

  <Card href="/docs/ingest-data/cicd/argocd" title="ArgoCD">
    GitOps continuous delivery
  </Card>

  <Card href="/docs/ingest-data/cicd/terraform" title="Terraform">
    Infrastructure as code logs
  </Card>
</Cards>

***

## Security & compliance

<Cards>
  <Card href="/docs/ingest-data/security/falco" title="Falco">
    Cloud-native runtime security
  </Card>

  <Card href="/docs/ingest-data/security/trivy" title="Trivy">
    Vulnerability scanner
  </Card>

  <Card href="/docs/ingest-data/security/siem-export" title="SIEM Export">
    Export to SIEM platforms
  </Card>
</Cards>

***

## LLMs & AI agents

<Cards>
  <Card href="/docs/ingest-data/ai-agents/openai" title="OpenAI">
    Log OpenAI API calls and token usage
  </Card>

  <Card href="/docs/ingest-data/ai-agents/anthropic" title="Anthropic">
    Log Claude API calls and responses
  </Card>

  <Card href="/docs/ingest-data/ai-agents/langchain" title="LangChain">
    Trace chains, agents, and tools
  </Card>

  <Card href="/docs/ingest-data/ai-agents/llamaindex" title="LlamaIndex">
    Trace RAG queries and retrievals
  </Card>

  <Card href="/docs/ingest-data/ai-agents/autogen" title="AutoGen">
    Log multi-agent conversations
  </Card>

  <Card href="/docs/ingest-data/ai-agents/crewai" title="CrewAI">
    Monitor crew and task executions
  </Card>

  <Card href="/docs/ingest-data/ai-agents/dspy" title="DSPy">
    Track program optimizations
  </Card>

  <Card href="/docs/ingest-data/ai-agents/n8n" title="n8n">
    Workflow automation observability
  </Card>
</Cards>

***

## Can't find what you're looking for?

We're constantly adding new integrations. If you need an integration that's not listed:

1. **Check our GitHub** - Browse [open issues](https://github.com/parseablehq/parseable/issues) for integration requests
2. **Request an integration** - [Open a new issue](https://github.com/parseablehq/parseable/issues/new) describing your use case
3. **Join the community** - Ask in our [Slack community](https://logg.ing/community) for help


# Data modelling (/docs/key-concepts/data-model)



import { Accordion, Accordions } from 'fumadocs-ui/components/accordion';

Datasets are the primary unit of storage in Parseable. Any MELT (Metrics, Events, Logs, Traces) data is ingested into one or other dataset.

Think of a dataset as a logical grouping of similar telemetry data. Proper datasets planning ensures fast query and optimal storage compression.

Every dataset is identified by a unique name. A dataset has a assigned schema (can be dynamic i.e. inferred from incoming data or static i.e. explicitly defined). Role based access control, alerts, retention and notifications are supported at the dataset level.

## Mapping sources to datasets

As SREs and DevOps engineers, you often deal with multiple data sources generating telemetry data. These sources can include applications, infrastructure components, and third-party services. Each of these sources can produce different types of data with varying schemas.

When debugging or investigating issues, it's common to correlate data from multiple sources. For example, you might want to correlate application logs with infrastructure metrics to identify performance bottlenecks.

Hence it is crucial to thoughtfully map data sources to datasets in Parseable. This mapping ensures that related data is stored together, making it easier to query and analyze.

A data source is anything that generates data, i.e. agents like FluentBit, FluentD, Vector, LogStash, agents from the OTel ecosystem, or the application itself. While ingesting data, you'll need to specify the dataset name to which the data should be sent. This allows mapping sources to datasets. Technically it is possible to map any number of data sources any number of data sources. Parseable allows this to ensure flexibility for varying use cases.

But, it is important to critically think about mapping data sources to datasets. Too many unrelated columns in a dataset can lead to poor compression and slower query performance. On the other hand, too many datasets can lead to increased complexity in managing the data.

When deciding how to map sources to datasets, consider the following:

* **Schema similarity**: If the sources have similar schema, it is better to map them to a single dataset. This allows for better compression and faster query performance. Similar here means fields are matching for 80 percent or more of the events. If the schema is too different, it is better to create separate datasets for each source.

* **Query patterns**: If you frequently query across multiple sources, it is better to map them to a single dataset. This allows you to query the data easily without having to join multiple datasets.

* **Data retention**: If the sources have different data retention requirements, it is better to create separate datasets for each source. This allows you to set different retention policies for each dataset.

* **Data ownership**: If different teams own different sources, it is better to create separate datasets for each source. This allows you to set different access controls for each dataset and manage the data better.

Let's understand this with some examples:

* **Kubernetes infrastructure logs**: Kubernetes infrastructure logs (e.g. kubelet, kube-proxy, etc.) can be mapped to a single dataset. This allows you to query the logs across all the Kubernetes components easily. Since these logs have similar schema, they fit well into a single dataset.

* **Application logs with similar schema**: If you have logs from multiple applications that log in a common format for example [go-log](https://pkg.go.dev/log), you can create a single dataset for all of them. This allows you to query the logs across applications easily.

* **Application logs with different schemas**: If you have logs from multiple applications that have completely different schemas, you can create a separate dataset for each application. This allows you to enforce a specific schema for each dataset and query them independently.

* **Aggregated data**: If you have aggregated data (e.g. metrics, traces) that you want to store, you can create a separate dataset for that. This allows you to query the aggregated data separately from the raw logs.

<Callout type="warn">
  Beyond 800 columns in a dataset, consider splitting the dataset into multiple datasets based on schema similarity or query patterns. Beyond 1000 columns, the server will reject the ingestion request with an error.
</Callout>

## Adding data to Parseable

### Identify the data source

Refer the ingestion guides for various data sources in the [Ingestion](/docs/ingestion) section.

### Create or use an existing dataset

You can create a dataset using the "Create Dataset" button on Datasets page. You'll be prompted to enter the dataset name, schema type, and partition column.

You can set the schema type to be [static](#static) (schema has to be explicitly provided at the time of creation of dataset) or [dynamic](#dynamic) (let server infer the schema from the incoming data). Once set, the schema type cannot be changed. Read more about schema types in the [Dataset Schema](#dataset-schema) section.

Partition column is an optional field. If you want to partition the dataset based on a specific field, you can specify that field here. If you don't specify a partition field, Parseable will use the internal `p_timestamp` field as the partition field. Read more about partitioning in the [Partitioning](/docs/key-concepts/partitioning) section.

## Dataset vs index

Traditional indices in systems like Elasticsearch are build to ingest textual data, index each field and allow for fast search and retrieval. This works well for pure search use cases, where you want to search for specific keywords or phrases in the data.

But applying this concept to huge volumes of observability data (logs, metrics, traces) is not practical. Observability data is often structured, semi-structured or unstructured, and indexing every field can lead to excessive storage costs for little to no performance gain.

Parseable datasets are designed to handle large volumes of observability data efficiently. They focus on optimal storage compression and fast retrieval via query, rather than indexing every field. This allows Parseable to handle high cardinality data, such as logs with many unique fields, without the performance and storage overhead of traditional indices.

## Dataset schema

Schema defines the fields in an event and their types. Parseable supports two types of schema - dynamic and static. You can choose the schema type while creating the dataset. Additionally, if you want to enforce a specific schema, you'll need to send that schema at the time of creating the dataset.

### Dynamic

Datasets by default have dynamic schema. This means you don't need to define a schema for a dataset. The Parseable server detects the schema from first event. If there are subsequent events (with new schema), it updates internal schema accordingly.

Log data formats evolve over time, and users prefer a dynamic schema approach, where they don't have to worry about schema changes, and they are still able to ingest events to a given dataset.

<Callout type="info">
  For dynamic schema, Parseable doesn't allow changing the type of an existing column whose type is already set. For example, if a column is detected as string in the first event, it can't be changed to int or timestamp in a later event. If you'd like to enforce a specific schema, please use static schema.
</Callout>

### Static

In some cases, you may want to enforce a specific schema for a dataset. You can do this by setting the static schema type while creating the dataset. This schema will be enforced for all the events ingested to the dataset. You'll need to provide the schema in the form of a JSON object with field names and their types, with the create dataset API call. The following types are supported in the schema: `string`, `int`, `float`, `datetime`,`date`, `boolean`.

## FAQ

Some of common questions related to datasets are answered below. If you have any other questions, please reach out to us on [Slack](http://logg.ing/community) or [GitHub Discussions](http://github.com/parseablehq/parseable/discussions).

<Accordions>
  <Accordion id="dataset-vs-index" title="Is a dataset equivalent to an index in Elasticsearch?">
    A dataset is not equivalent to an index in Elasticsearch. While both are used to store and retrieve data, datasets in Parseable are designed specifically for observability data (logs, metrics, traces) and focus on optimal storage compression and fast retrieval via query. Datasets can handle high cardinality data without the performance and storage overhead of traditional indices. Refer to the [Dataset vs index](#dataset-vs-index) section for more details.
  </Accordion>

  <Accordion id="new-vs-old-dataset" title="How do I decide between creating a new dataset or using an existing one?">
    General principle is to create a new dataset if the data has a different schema or if you want to enforce a specific schema. If the data has similar schema and you want to query it together, you can use an existing dataset. Refer to the [Mapping sources to datasets](#mapping-sources-to-datasets) section for more details.
  </Accordion>

  <Accordion id="static-vs-dynamic-schema" title="How do I decide static vs dynamic schema?">
    If in doubt, use static schema. Static schema allows you to enforce a specific schema for the dataset, which can help in better compression and faster query performance. Dynamic schema is useful when you don't want to worry about schema changes and want to ingest events without specifying the schema. Refer to the [Dataset Schema](#dataset-schema) section for more details.
  </Accordion>

  <Accordion id="when-to-use-partitions" title="When should I use partitioning?">
    Partitioning is useful when you want to optimize query performance for specific fields. If you frequently query on a specific field, you can partition the dataset based on that field. This allows Parseable to store the data in a way that makes it faster to retrieve the data for that field. Refer to the [Partitioning](/docs/key-concepts/partitioning) section for more details.
  </Accordion>

  <Accordion id="how-many-columns" title="How many columns are too many in datasets?">
    We recommend keeping the number of columns in a dataset to a reasonable limit, ideally less than 800. Too many columns can lead to poor compression and slower query performance. If you have more than 800 columns, consider splitting the dataset into multiple datasets based on schema similarity or query patterns. Beyond 1000 columns, the server will reject the ingestion request with an error.
  </Accordion>
</Accordions>


# High Availability (/docs/key-concepts/high-availability)



<OfferingPills pro enterprise className="mb-4" />

Parseable supports a distributed, high-availability mode for production use cases where downtime is not an option. The distributed setup is designed to ensure fault tolerance and high availability for log ingestion.

The distributed setup consists of multiple ingestion and query server and a S3 (or other object store) bucket.

The Query servers use metadata stored in the object store to query the data. The query server uses the Parseable manifest file and the Parquet footers in tandem to ensure that the data is read in fewest possible object store API calls.

## Node Functions

* **Prism Node**: Handles the Parseable UI and all user requests except for query and search operations. The Prism node is designed to be as compute efficient as the querier node.

* **Querier Node**: Processes data queries and analytics. Queriers use metadata stored in the object store to efficiently read data with minimal API calls.

* **Ingestor Node**: Processes incoming log events. Each ingestor creates its own set of metadata and data files in the object storage system, allowing for simple scaling as workloads change.

* **Indexer Node**: Manages indexing and search functionality.

## High Availability

Parseable Enterprise builds upon the distributed architecture of Parseable OSS, enhancing it with an even more robust high availability framework. This feature allows you to independently scale the query nodes along with the independently scalable ingest nodes.

The high availability architecture in Parseable Enterprise consists of four specialized node types, each serving a distinct function within the cluster:

### Node specific Environment variables

| Node Type      | Role                                        | Scalability                      | Node specific Env var |
| -------------- | ------------------------------------------- | -------------------------------- | --------------------- |
| Prism (Leader) | Manages UI, dataset configuration, and RBAC | Single Node                      | -                     |
| Query          | Handles data querying and analytics         | Independently scalable           | P\_QUERIER\_ENDPOINT  |
| Ingest         | Processes incoming log event                | Independently scalable           | P\_INGESTOR\_ENDPOINT |
| Index          | Manages indexing and search                 | Single Node (multi node planned) | P\_INDEXER\_ENDPOINT  |

Details of the environment variables are available in the [Environment Variables](/docs/self-hosted/configuration).

Each node in the cluster generates and maintains its own NodeMetadata file containing domain name information, authentication tokens, and node-specific configuration. These metadata files are stored in the configured S3 bucket and serve as the foundation for inter-node communication.

For optimal performance, we recommend the following specifications for each node type:

| Node Type      | vCPU | Memory |
| -------------- | ---- | ------ |
| Prism (leader) | 16   | 32 GiB |
| Query          | 16   | 32 GiB |
| Ingest         | 8    | 16 GiB |
| Index          | 16   | 32 GiB |

The Prism node requires similar compute and storage resources as the querier node because it handles all user interface operations and administrative requests.


# Key Concepts (/docs/key-concepts)



import { IconChartCohort,IconDirections,IconCloudDataConnection,IconBrandInertia,IconFileTypeSql,IconServerBolt
 } from '@tabler/icons-react';

Dive deeper into the key concepts of Parseable to understand how to best leverage Parseable for your specific observability needs. Whether you're new to Parseable or looking to deepen your understanding, these concepts will provide a solid foundation for using Parseable effectively.

<Cards>
  <Card href="/docs/key-concepts/data-model" icon={<IconChartCohort className="text-purple-600" />} title="Data modelling">
    Learn when to create datasets, how to aggregate observability data, use schemas, and manage your data effectively.
  </Card>

  <Card href="/docs/key-concepts/partitioning" icon={<IconDirections className="text-purple-600" />} title="Partitioning">
    Optimize query performance by partitioning datasets based on frequently filtered columns.
  </Card>

  <Card href="/docs/key-concepts/query" icon={<IconFileTypeSql className="text-purple-600" />} title="Query">
    Use PostgreSQL-compatible SQL to query your telemetry data with powerful filtering and aggregation.
  </Card>

  <Card href="/docs/key-concepts/storage" icon={<IconCloudDataConnection className="text-purple-600" />} title="Storage">
    Achieve storage efficiency and cost with object stores like S3, GCS, Azure Blob as the primary storage layer.
  </Card>

  <Card href="/docs/key-concepts/high-availability" icon={<IconServerBolt className="text-purple-600" />} title="High availability" className="col-span-2">
    Ensure your Parseable deployment is resilient and always available with built-in high availability features.
    Deploy across public or private clouds, containers, VMs, or bare metal environments with complete data security and privacy.
  </Card>
</Cards>


# Partitioning (/docs/key-concepts/partitioning)



<OfferingPills pro enterprise className="mb-4" />

Partitioning allows splitting of telemetry based on specific columns and value pairs to improve query performance. The decision to choose specific columns for partitioning is based on the access patterns of the data. By partitioning log data, you can optimize query performance, reduce the amount of data scanned during queries, and improve storage efficiency.

## When to use partitioning?

Partitioning is useful when you have a clear understanding of the most common data access patterns for a given log dataset. More specifically, when the columns where users are most likely to `filter` or `group by` are well known.

Also, a relatively larger dataset (at least few TBs or more) is better suited for partitioning. For tiny datasets, the overhead of managing partitions might outweigh the benefits.

## Select a column for partitioning

The first step is to find which column users are most likely to `filter` or `group by`. Once you have this information, it is important to know the variance in the column values (i.e. the number of unique values in the column). For example, if you have a column `log_level` with only a few unique values like `ERR`, `WARN`, and `INFO`, it would be a good candidate for partitioning. But if there is a column called `log_message` where each log event has a unique message, partitioning on this column will in fact make things worse.

**Important**: In Parseable, you can select only one column per dataset for partitioning.

## How to set up partitioning?

You can specify a single column for partitioning while creating a dataset on the Parseable Console (Create Dataset >> Custom Partition Field). Once the dataset is created, Parseable will automatically create physical partitions based on the values in this column.

You can also edit the partition column for an existing dataset (Dataset >> Manage >> Info >> Custom Partition Field). Note that this will have effect on all the new data that is ingested into the dataset, and not the existing data.

## How does partitioning work?

When a dataset is created with partitioning enabled, Parseable will create physical partitions based on the values in the specified column. For example, if you have a column `log_level` with the values `ERR`, `WARN`, and `INFO`, Parseable will create three physical partitions, one for each value.

When a query is run with a filter on `log_level`, Parseable will only scan the relevant partition(s) and not the entire dataset. This significantly reduces the amount of data scanned during queries and improves query performance.

Let's understand this better with an example. Let's say you have log events with columns `timestamp`, `log_level`, `service_name`, `log_message` and `os`. If one of the most common data query patterns is to filter events by `log_level` (i.e., most queries are of the form `select * from logs where log_level = '...'`), then you should consider partitioning by the `log_level` column.

Physically on the storage (S3 bucket or disk), you'll see the data organized by the partition column values. For example, if you have partitioning on `log_level`, you'll see the data organized like this:

```sql
  log_level=ERR
  log_level=WARN
  log_level=INFO
```

If you frequently filter by both `log_level` and another column like `os`, you'll need to decide which one provides the most query benefit as your partition column, since only one column can be used for partitioning.

## Best practices

* **Choose the right column:** Choose the column that is most frequently used in query filters.

* **Understand the data distribution:** Ensure that the column you choose has a good distribution of values with relatively low cardinality (few unique values).

* **Avoid high cardinality columns:** Partitioning on a column with high cardinality (i.e., many unique values) can lead to too many small partitions, which is inefficient.

* **Consider query patterns:** Select a partition column that aligns with your most common query filters.

* **Monitor and adjust:** Monitor the query performance and adjust the partition column as needed if query patterns change.


# Query (/docs/key-concepts/query)



Parseable offers a SQL compatible query interface to query telemetry data. Users can choose to use the filter interface directly without having to deal with SQL at all. However for more complex queries and advanced users, Parseable offers a SQL query interface.

You can specify the query and the relevant time range for which you want this query to be run. The response is inclusive of both the start and end timestamps.

The filter interface is quite self explanatory, with options to filter by specific columns and values and also by time range. In this document, we'll cover more about the SQL API and its capabilities.

Check out the [Query API](/docs/api/v1/query).

## How does it work?

After parsing and creating the execution plan for a query, the Parseable query server uses the data manifest file to filter out the relevant Parquet files. The data manifest file is a JSON file that contains the specific column metadata for a whole day. The querier uses this file to filter the relevant Parquet files based on the query filters and the time range.

Only the relevant Parquet file paths are then added as a data source to custom table provider. Datafusion then efficiently reads the files via the GetRange S3 API, pulling only the very specific data needed for the query. This ensures that only the relevant data is read from the storage, reducing the query time and cost.

## Supported functions

Parseable supports a wide range of SQL functions - Aggregate, Window and Scalar functions. Refer the Apache Datafusion documentation for the complete list of supported functions and their usage.

* [Aggregate Functions](https://datafusion.apache.org/user-guide/sql/aggregate_functions.html)
* [Window Functions](https://datafusion.apache.org/user-guide/sql/window_functions.html)
* [Scalar Functions](https://datafusion.apache.org/user-guide/sql/scalar_functions.html)

## Query with regular expressions

This section provides examples of how to use regular expressions in Parseable queries.

* Match regular expression (Case Sensitive)

```sql
SELECT * FROM frontend where message ~ 'failing' LIMIT 9000;
```

* Match regular expression (Case Insensitive)

```sql
SELECT * FROM frontend where message ~* 'application' LIMIT 9000;
```

* Does not match regular expression (Case Sensitive)

```sql
SELECT * FROM frontend where message !~ 'started' LIMIT 9000;
```

* Does not match regular expression (Case Insensitive)

```sql
SELECT * FROM frontend where message !~* 'application' LIMIT 9000;
```

* Matches the beginning of the string (Case Insensitive)

```sql
SELECT * FROM frontend where message ~* '^a' LIMIT 9000;
```

* Matches the end of the string

```sql
SELECT * FROM frontend where message ~ 'failing$' LIMIT 9000;
```

* Matches numeric type data

```sql
SELECT * FROM frontend where uuid ~ '[0-9]' LIMIT 9000;
```

* Matches numeric type data (two digits)

```sql
SELECT * FROM frontend where uuid ~ '[0-9][0-9]' LIMIT 9000;
```

* Matches numeric type data (two digits)

```sql
SELECT * FROM frontend where uuid ~ '[0-9][0-9]' LIMIT 9000;
```

* Replace every instance of the numeric type data with the symbol \*

```sql
SELECT REGEXP_REPLACE(uuid,'[0-9]','*','g') FROM frontend LIMIT 9000;
```

* When a Regex is run against a string, the REGEXP\_MATCHES() function compares the two and returns the string that matches the pattern as a set.

```sql
SELECT REGEXP_MATCH(email,'@(.*)$')  FROM frontend where email is not null LIMIT 10;
```

* Postgres regex numbers only: Use the REGEXP\_REPLACE() function to extract only the numbers from a string in PostgreSQL.

```sql
SELECT REGEXP_REPLACE(email,'\\D','','g') FROM frontend where email is not null LIMIT 10;
```

* Postgres regex split: SPLIT\_PART() function can split a string into many parts. To divide a string into several pieces, we must pass the String, the Delimiter, and the Field Number.

```sql
SELECT SPLIT_PART(email,'@',1) FROM frontend where email is not null LIMIT 10 -- return before @ from email;
SELECT SPLIT_PART(email,'@',2) FROM frontend where email is not null LIMIT 10 -- return after @ from email;
```

* Postgres Regex Remove Special Characters: Using the REGEXP\_REPLACE() function, all Special Characters from a supplied text can be eliminated.

```sql
SELECT REGEXP_REPLACE(email, '[^\\w]+','','g') FROM frontend where email is not null LIMIT 10;
```

* Functions and Operators in pattern matching: Like and other POSIX regular expressions are supported.

```sql
SELECT * FROM frontend where email LIKE '%test%' LIMIT 10;
SELECT * FROM frontend where email ~ '^test' LIMIT 10;
```

## Case sensitivity

Dataset column names are case sensitive. For example, if you send a log event like

```json
{
  "foo": "bar",
  "Foo": "bar"
}
```

Parseable will create two columns, `foo` and `Foo` in the schema. So, while querying, please refer to the fields as `foo` and `Foo` respectively. While querying, unquoted identifiers are converted to lowercase. To query column names with uppercase letters, they must be passed in double quotes. For example, when sending a query via the REST API, the following JSON payload will apply the `WHERE` condition to the column `Foo`:

```json
{
    "query":"select * from dataset where \"Foo\"=bar",
    "startTime":"2023-02-14T00:00:00+00:00",
    "endTime":"2023-02-15T23:59:00+00:00"
}
```

If you're querying Parseable via Grafana UI (via the [data source plugin](https://github.com/parseablehq/parseable-datasource)), you can use the following query to query the column `Foo`:

```sql
SELECT * FROM dataset WHERE "Foo" = 'bar'
```

## Query analysis

In some cases, you may want to understand the query performance. To view the detailed query execution plan, use the `EXPLAIN ANALYZE` keyword in the query. For example, the following query will return the query execution plan and time taken per step.

```json
{
	"query": "EXPLAIN ANALYZE SELECT * FROM frontend LIMIT 100",
	"startTime": "2023-03-07T05:28:10.428Z",
	"endTime": "2023-03-08T05:28:10.428Z"
}
```

## Response fields information with query results

To get the query result fields as a part of query API response, add the query parameter `fields=true` to the API call, e.g. `http://localhost:8000/api/v1/query?fields=true`.

For example, for a query like `select count(*) as count from app1`, with the query parameter added will respond like this:

```json
{
    "fields": [
        "count"
    ],
    "records": [
        {
            "count": 2
        }
    ]
}
```


# Storage (/docs/key-concepts/storage)



Parseable is a purpose built telemetry datalake. This means telemetry data is persisted in inexpensive, infinitely scalable commodity storage such as Amazon S3, Google Cloud Storage, Azure Blob, or other S3‑compatible service (Tigris, MinIO, Wasabi, DigitalOcean Spaces, etc.).

## Architecture

Parseable uses Apache Arrow and Parquet as its underlying data structures, optimized for analytical workloads. This columnar format provides:

* **Compression efficiency**: Significantly reduced storage costs
* **Query performance**: Fast analytical queries over compressed data
* **Schema evolution**: Flexible data structure changes over time
* **Cross-platform compatibility**: Standard format readable by many tools

(SSE)

* **Customer-Managed Keys**: SSE-C for custom encryption keys
* **TLS in Transit**: Secure data transmission
* **Access Control**: Fine-grained permissions through cloud IAM

## Supported providers

Parseable supports multiple cloud storage providers and S3-compatible services:

### Cloud Providers

* **AWS S3**: Native integration with all AWS regions
* **Azure Blob Storage**: Full support for Azure storage accounts
* **Google Cloud Storage**: Compatible through S3 API

### S3-Compatible Services

* **MinIO**: Self-hosted object storage
* **Wasabi**: Cost-optimized cloud storage
* **DigitalOcean Spaces**: Developer-friendly object storage
* **Backblaze B2**: Affordable cloud storage

## Authentication Models

Parseable supports multiple authentication mechanisms to fit different deployment scenarios:

### Static Credentials

* Access keys and secret keys for direct authentication
* Suitable for development and simple deployments
* Requires careful credential management

### Dynamic Credentials

* **IAM Roles**: For AWS EC2/ECS deployments
* **Instance Metadata Service (IMDS)**: Automatic credential rotation
* **Container Credentials**: For containerized environments
* **Azure AD Integration**: Service principal authentication

### Security Features

* **Encryption at Rest**: Support for server-side encryption (SSE)
* **Customer-Managed Keys**: SSE-C for custom encryption keys
* **TLS in Transit**: Secure data transmission
* **Access Control**: Fine-grained permissions through cloud IAM

## Data Organization

Parseable organizes data in object storage using a hierarchical structure:

```
bucket/
├── streams/
│   ├── app-logs/
│   │   ├── year=2024/
│   │   │   ├── month=01/
│   │   │   │   ├── day=15/
│   │   │   │   │   └── data.parquet
│   └── system-logs/
└── metadata/
    └── schemas/
```


# Parseable AI Assistant (/docs/llm/text-to-sql)



<OfferingPills pro enterprise className="mb-4" />


# Executable Binary (/docs/quickstart/binary)





## Start Parseable

Download the relevant binary and start Parseable in local-store mode with the following commands:

```sh
curl -fsSL https://logg.ing/install | bash
parseable local-store
```

This will start Parseable on port 8000. You can access the Parseable Console at [http://localhost:8000](http://localhost:8000).

## Ingest data

Send your first log event to the demo dataset using below command.

```bash
curl --location --request POST \
'http://localhost:8000/api/v1/ingest' \
--header 'X-P-Stream: demo' \
--header 'Authorization: Basic YWRtaW46YWRtaW4=' \
--header 'Content-Type: application/json' \
--data-raw '[
    {
        "id": "434a5f5e-2f5f-11ed-a261-0242ac120002",
        "datetime": "2023-01-05T07:20:50.52Z",
        "host": "153.10.110.81",
        "user-identifier": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) Firefox/64.0",
        "method": "PUT",
        "status": 500,
        "referrer": "http://www.google.com/"
    }
]'
```

Parseable uses datasets to organize log data. Here we posted a sample log data to the demo dataset, by adding the header `X-P-Stream: demo` in the request.

## Query data

To query the data via Console, login at [http://localhost:8000](http://localhost:8000). Default username and password is `admin:admin`. Then select the demo dataset under the log explorer page.

<img alt="Query data" src={__img0} placeholder="blur" />


# Parseable Cloud (/docs/quickstart/cloud)



Get started with Parseable Cloud in minutes — no infrastructure to manage.

## Sign Up

1. Go to [app.parseable.com](https://app.parseable.com) and create an account
2. Verify your email address

## Create a Workspace

1. Click **Create Workspace**
2. Choose your preferred **region** (select the region closest to your data sources for best performance)
3. Wait a few minutes for your Parseable workspace to be provisioned

Once ready, you'll receive your unique **ingestion endpoint**.

## Start Ingesting Data

Use the endpoint provided to start sending logs. Here's an example using curl:

```bash
curl --location --request POST \
'https://<your-workspace>.parseable.com/api/v1/ingest' \
--header 'X-P-Stream: demo' \
--header 'Authorization: Basic <your-credentials>' \
--header 'Content-Type: application/json' \
--data-raw '[
    {
        "id": "434a5f5e-2f5f-11ed-a261-0242ac120002",
        "datetime": "2023-01-05T07:20:50.52Z",
        "host": "153.10.110.81",
        "message": "Hello from Parseable Cloud!"
    }
]'
```

Replace `<your-workspace>` and `<your-credentials>` with the values from your workspace dashboard.

## Query Your Data

Once data is ingested, you can query it directly from the Parseable Cloud console at [app.parseable.com](https://app.parseable.com).

## Benefits of Parseable Cloud

* **No infrastructure management** — We handle scaling, updates, and maintenance
* **Pay-as-you-go pricing** — Only pay for what you use
* **Global regions** — Deploy close to your data sources
* **Instant setup** — Start ingesting in minutes
* **Enterprise-grade security** — SOC 2 compliant, encrypted at rest and in transit


# Docker Image (/docs/quickstart/docker)





Ensure Docker is installed on your machine. Refer to [this doc](https://www.docker.com/products/docker-desktop/) to install Docker.

## Start Parseable

```sh
docker run -p 8000:8000 \
-p 8001:8001 \
-p 8002:8002 \
-v /tmp/parseable/data:/parseable/data \
-v /tmp/parseable/staging:/parseable/staging \
-e P_FS_DIR=/parseable/data \
-e P_STAGING_DIR=/parseable/staging \
parseable/parseable:latest \
parseable local-store
```

This will start Parseable on port 8000. You can access the Parseable Console at [http://localhost:8000](http://localhost:8000).

## Ingest data

You can post log data to the demo dataset using a POST call to the dataset endpoint.

```bash
curl --location --request POST \
'http://localhost:8000/api/v1/ingest' \
--header 'X-P-Stream: demo' \
--header 'Authorization: Basic YWRtaW46YWRtaW4=' \
--header 'Content-Type: application/json' \
--data-raw '[
    {
        "id": "434a5f5e-2f5f-11ed-a261-0242ac120002",
        "datetime": "2023-01-05T07:20:50.52Z",
        "host": "153.10.110.81",
        "user-identifier": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) Firefox/64.0",
        "method": "PUT",
        "status": 500,
        "referrer": "http://www.google.com/"
    }
]'
```

Parseable uses datasets to organize log data. Here we posted a sample log data to the demo dataset, by adding the header `X-P-Stream: demo` in the request.

## Query data

To query the data via Console, login at [http://localhost:8000](http://localhost:8000). Default username and password is `admin:admin`. Then select the demo dataset under the log explorer page.

<img alt="Query data" src={__img0} placeholder="blur" />


# Configuration (/docs/self-hosted/configuration)



This document lists all the environment variables and HTTP headers supported by Parseable server.

### Common environment variables

| Variable Name                 | Required | Description                                                                                                                                          | Default          | Example                        |
| ----------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------------------ |
| `P_USERNAME`                  | `Yes`    | Username for the admin user. Will be used to access API and UI.                                                                                      | admin            | `AKIAIOSFODNN7`                |
| `P_PASSWORD`                  | `Yes`    | Password for the admin user. Will be used to access API and UI.                                                                                      | admin            | `wJalrXUtnaYrOq7phc6l`         |
| `RUST_LOG`                    | `No`     | Control the log level of Parseable server. By default, all logging is disabled, except for the error level. Refer the docs here for possible values. | error            | `info`                         |
| `P_ADDR`                      | `No`     | Address (IP Address and Port without the scheme) on which the Parseable server would listen for new connections.                                     | `127.0.0.1:8000` | `127.0.0.1:7000`               |
| `P_GRPC_PORT`                 | `No`     | Port to be used for gRPC response.                                                                                                                   | `8001`           | `5001`                         |
| `P_FLIGHT_PORT`               | `No`     | Port to be used for Arrow Flight response.                                                                                                           | `8002`           | `5002`                         |
| `P_TLS_CERT_PATH`             | `No`     | Location of the TLS Cert file on the server. Use this and P\_TLS\_KEY\_PATH variable together to enable TLS on your Parseable server.                | -                | `/home/user/fullchain.pem`     |
| `P_TLS_KEY_PATH`              | `No`     | Location of TLS Private key file on the server. Use this and P\_TLS\_CERT\_PATH variable together to enable TLS on your Parseable server.            | -                | `/home/user/privkey.pem`       |
| `P_STAGING_DIR`               | `No`     | Path on the local machine, where the Parseable server would stage data before pushing it to storage.                                                 | `$PWD/staging`   | `/home/user/parseable/staging` |
| `P_CHECK_UPDATE`              | `No`     | Specify whether server should check for new updates from Parseable download server.                                                                  | `true`           | `false`                        |
| `P_SEND_ANONYMOUS_USAGE_DATA` | `No`     | Specify whether the server should send anonymous usage data to Parseable analytics.                                                                  | `true`           | `false`                        |
| `P_PARQUET_COMPRESSION_ALGO`  | `No`     | Specify the compression algorithm to use for Parquet files. Support values are `UNCOMPRESSED`, `SNAPPY`, `GZIP`, `LZO`, `BROTLI`, `LZ4`, `ZSTD`.     | `LZ4`            | `GZIP`                         |
| `P_OPENAI_API_KEY`            | `No`     | Specify your OpenAI API key to generate SQL automatically from plain text.                                                                           | -                | `sk-open-ai-api-key`           |
| `P_CORS`                      | `No`     | Specify whether the server should enable/disable CORS. Supported values are `true` to disable, `false` to enable CORS                                | `true`           | `false`                        |
| `P_MEMORY_THRESHOLD`          | `No`     | Specify the memory threshold to use for Parseable server.                                                                                            | `100`            | `80`                           |
| `P_CPU_THRESHOLD`             | `No`     | Specify the CPU threshold to use for Parseable server.                                                                                               | `100`            | `80`                           |

### Applicable to distributed mode

| Variable Name              | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Default        | Example                                 |
| -------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | --------------------------------------- |
| `P_MODE`                   | `Yes`    | Mode for this Parseable instance. Can be INGEST or QUERY or ALL. If set to ALL, instance will behave as a standalone deployment.                                                                                                                                                                                                                                                                                                                                                                                                                         | `ALL`          | `INGEST`                                |
| `P_HOT_TIER_DIR`           | `No`     | Path on the query node (or standalone node), where the Parseable server would store recent data. Refer [Hot Tier documentation](/docs/user-guide/smart-cache) for details.                                                                                                                                                                                                                                                                                                                                                                               | `-`            | `/home/user/hot-tier`                   |
| `P_MAX_DISK_USAGE_PERCENT` | `No`     | Maximum percentage of total disk that should be used for hot tier. Refer [Hot Tier documentation](/docs/user-guide/smart-cache) for details.                                                                                                                                                                                                                                                                                                                                                                                                             | `80`           | `70`                                    |
| `P_INGESTOR_ENDPOINT`      | `No`     | Endpoint (IP, DNS or URL and Port, without the scheme) of the ingestor. If set, the query node will use this address to access this Ingestor. If not set, the query node will use the P\_ADDR value if set. If `P_ADDR` is also not set, then defaults to `0.0.0.0:8000`. You can also set this variable to point to another environment variable. For example, if `P_INGESTOR_ENDPOINT` is set to `$HOSTNAME:$PORT`, Parseable process will look for environment variables `HOSTNAME` and `PORT` and replace their values in the `P_INGESTOR_ENDPOINT`. | `0.0.0.0:8000` | `ingestor1.parseable.svc.cluster.local` |

### Applicable to the S3 storage mode

This section lists all the environment variables applicable to the S3 storage mode. This is applicable to AWS S3 or any other S3 compatible object storage platform.

| Variable Name              | Required | Description                                                                                                                                                      | Default | Example                                                     |
| -------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ----------------------------------------------------------- |
| `P_S3_URL`                 | `Yes`    | URL for S3 or compatible object storage server.                                                                                                                  | `-`     | `https://s3.us-east-1.amazonaws.com`                        |
| `P_S3_ACCESS_KEY`          | `Yes`    | Access key for S3 or compatible object storage server.                                                                                                           | `-`     | `AKIAIOSFODNN7EXAMPLE`                                      |
| `P_S3_SECRET_KEY`          | `Yes`    | Secret key for S3 or compatible object storage server.                                                                                                           | `-`     | `wJalrXUtnaEXAMPLEKEY`                                      |
| `P_S3_BUCKET`              | `Yes`    | Bucket to use for Parseable data storage.                                                                                                                        | `-`     | `parseable`                                                 |
| `P_S3_REGION`              | `Yes`    | Region for the object storage platform.                                                                                                                          | `-`     | `us-east-1`                                                 |
| `P_S3_PATH_STYLE`          | `No`     | Force Parseable to use [Path style access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-bucket-intro.html#path-style-url-ex) to S3 store.        | `true`  | `false`                                                     |
| `P_S3_TLS_SKIP_VERIFY`     | `No`     | Skip checking for S3 store's TLS certificate validity.                                                                                                           | `false` | `true`                                                      |
| `P_S3_CHECKSUM`            | `No`     | Set SHA256 checksum in requests to allow S3 buckets with [WORM enabled](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html).                     | `false` | `true`                                                      |
| `P_S3_SSEC_ENCRYPTION_KEY` | `No`     | Set server side encryption key with [customer provided key for S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html). | `-`     | `SSE-C:AES256:lgYvIsNHaYFh45knxlpxCdLFJaLnmXiibQcDrUYZt9Q=` |

### Applicable to the Azure storage account

This section lists all the environment variables applicable to the Azure blobstore storage mode. These environment are mandatory, if you're staring Parseable server in Azure storage mode i.e. `parseable server blob-store`.

| Variable Name         | Required | Description                                                                                                                         | Default | Example                                   |
| --------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------- | ----------------------------------------- |
| `P_AZR_URL`           | `Yes`    | URL to communicate with blob storage.                                                                                               | `-`     | `https://parseable.blob.core.windows.net` |
| `P_AZR_ACCOUNT`       | `Yes`    | Azure storage account name. [Refer the docs here](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview). | `-`     | `parseable`                               |
| `P_AZR_CONTAINER`     | `Yes`    | Container name created in the storage storage account.                                                                              | `-`     | `parseable`                               |
| `P_AZR_ACCESS_KEY`    | `No`     | Access key to authenticate azure storage account.                                                                                   | `-`     | `AKIAIOSFODNN7EXAMPLE`                    |
| `P_AZR_CLIENT_ID`     | `No`     | Client ID of app registered in Azure AD to authenticate azure storage account.                                                      | `-`     | `AKIAIOSFODNN7EXAMPLE`                    |
| `P_AZR_CLIENT_SECRET` | `No`     | Client secret of app registered in Azure AD to authenticate azure storage account.                                                  | `-`     | `wJalrXUtnaEXAMPLEKEY`                    |
| `P_AZR_TENANT_ID`     | `No`     | Tenant ID associated with your Azure AD                                                                                             | `-`     | `AKIAIOSFODNN7EXAMPLE`                    |

### Applicable to AWS

This section lists all the environment variables applicable to the AWS blobstore storage mode. These environment are mandatory, if you're staring Parseable server in AWS storage mode i.e. `parseable server blob-store`.

| Variable Name             | Required | Description                                                      | Default                  | Example                |
| ------------------------- | -------- | ---------------------------------------------------------------- | ------------------------ | ---------------------- |
| `P_AWS_PROFILE_NAME`      | `No`     | Set AWS profile name which will be used for fetching credentials | `-`                      | `default`              |
| `P_AWS_IMDSV1_FALLBACK`   | `No`     | Sets if object store client should fallback to imdsv1.           | `false`                  | `true`                 |
| `P_AWS_METADATA_ENDPOINT` | `No`     | Sets AWS instance metadata endpoint to use.                      | `http://169.254.169.254` | `http://fd00:ec2::254` |

### Applicable to local drive mode

This section lists all the environment variables applicable to the local drive storage mode. These environment are mandatory, if you're staring Parseable server in local drive storage mode i.e. `parseable server blob-store`.

| Variable Name | Required | Description                                                        | Default     | Example                     |
| ------------- | -------- | ------------------------------------------------------------------ | ----------- | --------------------------- |
| `P_FS_DIR`    | `No`     | Path on the local machine where Parseable server would store data. | `$PWD/data` | `/home/user/parseable/data` |

### Applicable to OIDC

This section lists all the environment variables applicable to the OIDC mode. These environment are mandatory, if you're staring Parseable server in OIDC mode i.e. `parseable server oidc`.

| Variable Name          | Required | Description                                                                                                                                       | Default | Example                       |
| ---------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ----------------------------- |
| `P_OIDC_CLIENT_ID`     | `Yes`    | Your OIDC client identifier, provided by your identity provider.                                                                                  | `-`     | `client-id`                   |
| `P_OIDC_CLIENT_SECRET` | `Yes`    | Your OIDC client secret, provided by your identity provider.                                                                                      | `-`     | `client-secret`               |
| `P_OIDC_ISSUER`        | `Yes`    | The OIDC issuer URL, typically provided by your identity provider. It points to the OIDC authorization server. Should support discovery protocol. | `-`     | `https://accounts.google.com` |
| `P_ORIGIN_URI`         | `Yes`    | The URI where Parseable is hosted or accessible. This should be the base URL of your Parseable instance.                                          | `-`     | `https://demo.parseable.com/` |

Refer to [OIDC](/docs/user-guide/openid) section for more details.


# Parseable Metrics (/docs/self-hosted/metrics)



### Export Parseable to Prometheus

Prometheus offers a multi-dimensional data model with time series data identified by metric name and key/value pairs. The data collection happens via a pull model over HTTP/HTTPS.

Parseable server exposes Prometheus metrics at `/api/v1/metrics` endpoint (unauthorized). The metrics are exposed in Prometheus exposition format.

### Prerequisites

Parseable server installed and running. See installation guide for more details.

Prometheus installed and running. See installation guide for more details.

### Configuration

Prometheus configuration is done via a YAML file. Locate your Prometheus configuration file `prometheus.yml` and add the following section to scrape Parseable server metrics.

```yaml
scrape_configs:
- job_name: parseable-job
  metrics_path: /api/v1/metrics
  scheme: http
  static_configs:
  - targets: ['localhost:8000']
  basic_auth:
    username: "admin"
    password: "admin"
```

Make sure to replace localhost:8000 with the actual host and port where Parseable server is running.

### List of metrics exposed by Parseable

Parseable server exposes the following metrics on `/api/v1/metrics` endpoint. All of these can be accessed via Prometheus dashboard. A sample list of exposed metrics along with their definition is available in the demo server at `https://demo.parseable.com/api/v1/metrics`.

```bash
curl https://demo.parseable.com/api/v1/metrics
```


# Telemetry (/docs/self-hosted/telemetry)



### Overview

Parseable collects anonymized usage statistics from users in order to improve the server. You can deactivate at any time by setting `P_SEND_ANONYMOUS_USAGE_DATA=false`.

Any data that has already been collected can be deleted on request.

### Why is data collected?

Parseable is a young project and we want to make it fast, reliable and resource efficient. While we perform several benchmarks internally, it is impossible to capture all the scenarios, hardware and software combinations that Parseable is used in.

In order to identify performance characteristics and improve Parseable, we need to collect information about how it is used.

### What data is collected?

Broadly, there are two types of data collected:

* System information - general information about the system, such as CPU, RAM, and disk type. As well as the configuration of the Parseable instance.
* Usage - information about data stored and compressed.

We do not collect any data that can be used to identify the user or the user’s organization. This includes:

* Any data that can be used to identify the user or the user’s organization
* Any data stored in the dataset
* Any names of the dataset
* Any URLs

### Sample JSON data

This is a sample data received by our servers, when a Parseable installation reports anonymous telemetry.

```json
{
	"commit_hash": "f053d2f",
	"cpu_count": 8,
	"deployment_id": "01GTB8PGHM5AK9XQXPMTTCBQ0S",
	"memory_total_bytes": 16287862784,
	"metrics": {
		"cpu_cpu0_usage_percent": 1.5296164751052856,
		"cpu_cpu1_usage_percent": 1.6184406280517578,
		"cpu_cpu2_usage_percent": 2.738511800765991,
		"cpu_cpu3_usage_percent": 2.094792366027832,
		"cpu_cpu4_usage_percent": 2.183173179626465,
		"cpu_cpu5_usage_percent": 1.5540571212768557,
		"cpu_cpu6_usage_percent": 1.4056124687194824,
		"cpu_cpu7_usage_percent": 1.449198842048645,
		"memory_free_bytes": 349634560,
		"memory_in_use_bytes": 6138183680,
		"stream_count": 7,
		"total_events_count": 864611,
		"total_json_bytes": 396726688,
		"total_parquet_bytes": 311480071
	},
	"mode": "S3 bucket",
	"os_name": "Debian GNU/Linux",
	"os_version": "11",
	"platform": "Docker",
	"report_created_at": "2023-04-25T10:00:10.000638350Z",
	"uptime_secs": 12469729,
	"version": "0.4.0"
}
```

### Request data deletion

To request data deletion, send an email to [hi@parseable.com](mailto:hi@parseable.com) containing the unique `Deployment UID` generated for your Parseable installation.

You can find this identifier in the server startup banner under the field `Deployment UID`.


# AWS S3 (/docs/storage/awss3)



This document is a deep dive into Parseable and AWS S3 setup

## Prerequisites

* New Parseable cluster requires a fully empty S3 bucket.
* For optimum performance, please ensure the S3 bucket is in the same region as the compute (EC2, EKS, ECS, Lightsail or others) instances.

## Authentication

Parseable supports authentication to S3 via

* Access Key and Secret Key: The AWS access key and the secret key can be used to authenticate to AWS S3 bucket. To use this method, set the environment variables `P_S3_ACCESS_KEY` and `P_S3_SECRET_KEY` before starting the Parseable server(s).

* Instance Metadata Service (IMDS): For Parseable instances running on EC2, AWS credentials can be sourced from the Instance Metadata Service (IMDS), avoiding the need for explicit `P_S3_ACCESS_KEY` and `P_S3_SECRET_KEY`. To use this method,

  * Ensure that `Instance Metadata Service (IMDS)` is enabled when creating the EC2 instance (under Advanced details section). Select the Metadata version to `V1` and `V2` (token optional). Please refer to the [metadata service docs](https://docs.aws.amazon.com/sdkref/latest/guide/feature-imds-credentials.html) for more. You set `P_AWS_IMDSV1_FALLBACK` to true if you want to use the V1 method.

  * By default, Parseable uses the standard AWS metadata endpoint. If you’re using a custom metadata endpoint, add the optional environment variable `P_AWS_METADATA_ENDPOINT` to specify a [custom endpoint URL](https://docs.aws.amazon.com/sdkref/latest/guide/feature-imds-credentials.html) for retrieving instance metadata.

* IAM Roles for Service Accounts (IRSA): This is useful for EKS deployments. With IRSA you can associate an IAM role with a Kubernetes service account and configure Parseable to use the service account. To use this method, refer to [Parseable EKS documentation](https://www.parseable.com/docs/self-hosted/installation/standalone/aws-eks).

## SSE-C Support

Parseable supports server side encryption for [AWS S3 with customer provided encryption keys (SSE-C)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html). With SSE-C, you can store your data encrypted with your own encryption keys. Amazon S3 or a compatible service like MinIO manages data encryption and decryption transparently.

Note that SSE-C requires HTTPS and Amazon S3 or compatible service might reject any requests made over HTTP when using SSE-C.

## Setting up

The encryption key must be a 256-bit key for AES-256 encryption. To add SSE-C encryption key, add the environment variable `P_S3_SSEC_ENCRYPTION_KEY` before starting the server. The value should be in the format `- SSE-C:AES256:<base64_encryption_key>`. Here is example of adding the SSE-C encryption key to Parseable

Generate a 256-bit AES key and `Base64` encode it

```bash
ENCRYPTION_KEY=$(openssl rand -base64 32)
echo "Encryption Key: $ENCRYPTION_KEY"
```

Add the `Base64` encoded encryption key to the environment variable

```bash
P_S3_SSEC_ENCRYPTION_KEY=SSE-C:AES256:$ENCRYPTION_KEY
```

For distributed deployments, the environment variable `P_S3_SSEC_ENCRYPTION_KEY` needs to be set for Query as well as Ingestor nodes.

<Callout type="warn">
  If you lose the encryption key, you’ll lose access to the log data. Hence, we recommend secure storage for the encryption key such as [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) or similar.
</Callout>


# Dashboards (/docs/user-guide/dashboards)















Parseable Dashboards are customizable and support querying multiple data streams for comprehensive insights. You can also leverage text to SQL conversion for quick query creation.

<img alt="" src={__img0} placeholder="blur" />

<iframe width="560" height="315" src="https://www.youtube.com/embed/mXO2WtV0vBU?si=t1aW3PQUdN0oc9VC" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />

## Creating a Dashboard

1. **Start from the Side Nav:** Head over to Dashboards in the sidebar and hit Create New
2. **Name & Tag:** Give your dashboard a name and a tag (for easy organizing), then click Create Dashboard
3. **Build Your Canvas:** Select your new dashboard to land on the dashboard canvas. Click Add Tiles to start building charts
4. **Save and Favorite:** Add as many tiles as you need, then save your dashboard. You can also mark dashboards as favorites for quick access later

## Adding Charts to Dashboards

Charts can be added to dashboards from multiple sources:

* **SQL Editor**: Run queries in the SQL editor, visualize results, and add charts directly to dashboards
* **Keystone**: AI-generated insights can be added as dashboard tiles
* **Chart Builder**: Build visualizations using the built-in chart builder

## Chart Builder Types

There are two ways to build charts:

### 1. SQL Editor

Write custom SQL queries, visualize the results, and add them to your dashboard. The SQL editor supports up to 3 datasets simultaneously for complex joins and comparative analysis.

After running a query, you can use the chart view customization options and add these charts to dashboards directly.

<img alt="" src={__img1} placeholder="blur" />

<iframe width="560" height="315" src="https://www.youtube.com/embed/VjwFONGGqaE?si=hMkSWfwGWmfb4HfY" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />

### 2. Visual Chart Builder

<img alt="" src={__img2} placeholder="blur" />

The chart builder follows a 3-step process to create powerful visualizations:

### Step 1: Initialize

**Chart Type Selection:**

* **Timeseries**: For time-based data visualization
* **Line**: For trend analysis and continuous data
* **Bar**: For categorical comparisons
* **Area**: For cumulative values over time
* **Pie**: For showing proportions of a whole
* **Donut**: Similar to pie with a hollow center
* **Query Value**: For displaying single metric values
* **Gauge**: For showing progress or thresholds

**Dataset Selection:**
Choose your data source from the dropdown menu (e.g., vLLMmetrics or your custom log streams).

### Step 2: Plot Configuration

The configuration options vary based on your selected chart type:

#### For Timeseries, Line, Bar, and Area Charts:

* **Y-Axis**: Select the plot field (e.g., `aggregation_temporality_desc`)
* **Aggregate**: Choose aggregation method (COUNT)
* **Filters**: Add conditions to filter your data
* **Group by**: Group data by specific fields for segmentation
* **Sort by**: Order your results (ascending or descending)
* **X-Axis**: Select the dimension field (e.g., `aggregation_temporality`)

<img alt="" src={__img3} placeholder="blur" />

#### For Pie and Donut Charts:

* **Plot**: Select the field to visualize
* **Aggregate**: Choose how to aggregate values (COUNT)
* **Filters**: Apply data filters as needed
* **Note**: Grouping and sorting options are not available for these chart types

<img alt="" src={__img4} placeholder="blur" />

#### For Query Value and Gauge:

* **Plot**: Select the metric field
* **Aggregate**: Define the aggregation method
* **Filters**: Filter data to focus on specific values
* **Note**: These visualizations display single values, no grouping or sorting needed

<img alt="" src={__img5} placeholder="blur" />

### Step 3: Style Your Visualization

**Customization Options:**

* **X-axis Label**: Custom label for the X-axis
* **Y-axis Label**: Custom label for the Y-axis
* **Colour Scheme**: Choose from predefined color palettes (Forest, Ocean, Sunset, etc.)
* **Legend Position**: Place legend where it best fits your layout
* **Grid Lines**: Toggle grid visibility for better readability
* **Data Labels**: Show/hide values on the chart

**Chart-Specific Styling:**

* **Line/Area**: Smooth curves, fill opacity, stroke width
* **Bar**: Orientation (vertical/horizontal), bar spacing
* **Pie/Donut**: Inner radius (for donut), label display

**Gauge and Query Value Specific Styling:**

* **Units**: Add unit labels (e.g., %, ms, GB)
* **Auto-formatting**: Enable automatic number formatting
* **Precision**: Set decimal places for displayed values
* **Range**: Define min and max values (from 0 to 100 for percentages)
* **Segments**: Configure color-coded thresholds
  * Set breakpoints (e.g., 10, 90 for three segments)
  * Assign colors to each segment (green, yellow, red)
  * Use visual indicators for performance levels

**Quick Table View:**
Want to see raw data? Click the **Table** button in the top right corner to skip chart setup and view your query results in a tabular format.

## How it works

Dashboards in Parseable are a collection of tiles, each representing a visualization of a query result. You can create multiple tiles on a dashboard, each with its own query and chart type. Further, a tile's chart can be configured for different colors, units and formatting. Each tile can be based on a query targeting different dataset. The tiles can be resized, repositioned, and exported in various formats for easy sharing and collaboration.

Dashboard tiles can be dragged and repositioned anywhere on the dashboard. You can also adjust the tile size to fit your layout preferences, selecting from small, medium, large, or full screen widths (1/4, 2/4, 3/4, and full screen).

## Visualization Types

Parseable offers eight distinct visualization types, each optimized for different data patterns:

### Time-Series Charts

* **Timeseries**: Specialized for temporal data with automatic time formatting
* **Line**: Connect data points for trend visualization
* **Area**: Show cumulative values with filled areas

These charts support full configuration: Y-axis plotting, filtering, grouping, and sorting.

### Comparison Charts

* **Bar**: Compare categories with vertical or horizontal bars
  * Supports: Y-axis plot, filters, grouping, sorting
  * Best for: Categorical comparisons, distributions

### Proportion Charts

* **Pie**: Display parts of a whole in circular format
* **Donut**: Similar to pie with hollow center for modern aesthetics
  * Supports: Plot selection, aggregation, filtering
  * Best for: Showing percentages and proportions

### Metric Displays

* **Query Value**: Single metric display for KPIs
* **Gauge**: Visual progress indicator with thresholds
  * Supports: Plot selection, aggregation, filtering
  * Best for: Performance indicators, threshold monitoring

### Data Table

* **Simple Table**: Raw data view with sorting and filtering
  * Access via the Table button in any chart builder
  * Export capabilities for further analysis

Each visualization includes customizable styling options for colors, labels, and formatting to match your dashboard aesthetic.

## Time Range

Set a fixed time range for your dashboard to ensure all tiles load data consistently. You can save this time range with the dashboard, allowing for synchronized data views across all visualizations.


# Log IQ (/docs/user-guide/log-iq)



<OfferingPills pro enterprise className="mb-4" />

Log IQ allows identifying the format of unstructured log data, transforming it into structured columns within ingested events in JSON format. This helps in easy and optimized query, search, debug and visualize the data.

## How Log IQ works

Log IQ requires specific HTTP headers when ingesting data to properly identify and parse log formats:

### Required Headers

* `X-P-Log-Source` - **Mandatory** - Identifies the log format name (e.g., `syslog`, `nginx_access`, `zookeeper`)
* `X-P-Extract-Log` - **Required for unstructured data** - Specifies which field in the incoming JSON contains the raw log text (typically `log`)

### Processing Logic

**For structured data:**

* Only `X-P-Log-Source` is required
* Parseable assumes the data is already in a structured format
* The specified format is used for validation and additional processing

**For unstructured data:**

* Both `X-P-Log-Source` and `X-P-Extract-Log` are required
* Parseable extracts the raw log text from the field specified in `X-P-Extract-Log`
* The system applies regex patterns based on the format specified in `X-P-Log-Source`
* If the content matches the format, it's parsed into structured fields
* If the content doesn't match the format, the original value is retained in the specified field

### Outcome

* After successful format detection, a `p_format` field is added to the log event containing the log source name
* The dataset info is updated with an array of detected log sources
* Parseable UI (Prism) automatically displays filters on the `p_format` field
* If the log format is not detected, `p_format_verified=false` is added to the event
* Data is always ingested, regardless of format detection success

> **Note:** Even if your unstructured data doesn't match any of the supported formats listed below, you must still specify both headers. Choose the format that most closely aligns with your log structure.

### Example: Processing a Syslog Entry

Let's walk through a practical example of how Log IQ processes a syslog entry:

**1. Original log sent by an agent (e.g., FluentBit):**

```json
{
    "log": "2025-07-11T14:57:33.000111+05:30 node01 exporter[9012]: [2025/07/11 14:57:33] [error] [output:http:http.8] Failed to push metrics to endpoint /metrics"
}
```

**2. HTTP headers used when sending to Parseable:**

```
X-P-Log-Source: syslog_log
X-P-Extract-Log: log
```

**3. Parseable's processed output:**

```json
{
  "body": "[2025/07/11 14:57:33] [error] [output:http:http.8] Failed to push metrics to endpoint /metrics",
  "log": "2025-07-11T14:57:33.000111+05:30 node01 exporter[9012]: [2025/07/11 14:57:33] [error] [output:http:http.8] Failed to push metrics to endpoint /metrics",
  "log_hostname": "node01",
  "log_pid": "9012",
  "log_procname": "exporter",
  "log_syslog_tag": "exporter[9012]",
  "p_format": "syslog_log",
  "p_format_verified": "true",
  "p_src_ip": "127.0.0.1",
  "p_timestamp": "2025-07-11T09:20:23.019",
  "p_user_agent": "PostmanRuntime/7.44.1",
  "timestamp": "2025-07-11T09:27:33"
}
```

In this example:

1. The agent (like FluentBit) collects the log and places it in the `log` field
2. Parseable receives this with the appropriate headers
3. The system identifies it as a syslog format and extracts structured fields:
   * `log_hostname`: The host that generated the log ("node01")
   * `log_pid`: The process ID ("9012")
   * `log_procname`: The process name ("exporter")
   * `log_syslog_tag`: The syslog tag ("exporter\[9012]")
   * `body`: The actual message content
4. Parseable adds its metadata fields:
   * `p_format`: The detected format ("syslog\_log")
   * `p_format_verified`: Confirmation that the format was successfully detected
   * Other `p_` prefixed fields with request metadata

This structured data is now ready for efficient querying and analysis.

## Supported Formats

Parseable Log IQ supports a wide range of log formats. You can specify these formats using the `X-P-Log-Source` header when ingesting logs. The currently supported formats include:

| Format            | Description                                         |
| ----------------- | --------------------------------------------------- |
| `access_log`      | Common web server access logs (Apache, Nginx, etc.) |
| `alb_log`         | AWS Application Load Balancer logs                  |
| `block_log`       | Generic block-style logs                            |
| `candlepin_log`   | Candlepin service logs                              |
| `choose_repo_log` | Repository selection logs                           |
| `cloudvm_ram_log` | Cloud VM RAM usage logs                             |
| `cups_log`        | Common UNIX Printing System logs                    |
| `dpkg_log`        | Debian package manager logs                         |
| `elb_log`         | AWS Elastic Load Balancer logs                      |
| `engine_log`      | Generic engine logs                                 |
| `env_logger_log`  | Environment logger format                           |
| `error_log`       | Common error log format                             |
| `esx_syslog_log`  | VMware ESX syslog format                            |
| `haproxy_log`     | HAProxy load balancer logs                          |
| `katello_log`     | Katello service logs                                |
| `lnav_debug_log`  | LNAV debug logs                                     |
| `nextflow_log`    | Nextflow workflow logs                              |
| `openam_log`      | OpenAM authentication logs                          |
| `openamdb_log`    | OpenAM database logs                                |
| `openstack_log`   | OpenStack service logs                              |
| `page_log`        | Printer page logs                                   |
| `procstate_log`   | Process state logs                                  |
| `proxifier_log`   | Proxifier logs                                      |
| `rails_log`       | Ruby on Rails application logs                      |
| `redis_log`       | Redis database logs                                 |
| `s3_log`          | AWS S3 access logs                                  |
| `simple_rs_log`   | Simple Rust logs                                    |
| `snaplogic_log`   | SnapLogic integration logs                          |
| `sssd_log`        | System Security Services Daemon logs                |
| `strace_log`      | System call trace logs                              |
| `sudo_log`        | Sudo command logs                                   |
| `syslog_log`      | Standard system logs                                |
| `tcf_log`         | Target Communication Framework logs                 |
| `tcsh_history`    | TCSH shell history                                  |
| `uwsgi_log`       | uWSGI server logs                                   |
| `vmk_log`         | VMware kernel logs                                  |
| `vmw_log`         | VMware general logs                                 |
| `vmw_py_log`      | VMware Python logs                                  |
| `vmw_vc_svc_log`  | VMware vCenter service logs                         |
| `vpostgres_log`   | VMware Postgres database logs                       |
| `web_robot_log`   | Web crawler/robot logs                              |
| `xmlrpc_log`      | XML-RPC logs                                        |

Each format has specific patterns and fields that are extracted. When a log matches one of these formats, Parseable automatically extracts the structured fields and makes them available for querying and analysis.

### Extracted Fields by Format

Below are the fields extracted for each supported log format:

<details>
  <summary>
    <b>access_log</b>

     \- Web server access logs
  </summary>

  * `timestamp` - Time when the request was received
  * `c_ip` - Client IP address
  * `cs_username` - Username if authentication was used
  * `cs_method` - HTTP method (GET, POST, etc.)
  * `cs_uri_stem` - Requested URI path
  * `cs_uri_query` - Query string parameters
  * `cs_version` - HTTP protocol version
  * `sc_status` - HTTP status code
  * `sc_bytes` - Response size in bytes
  * `cs_referer` - Referer URL
  * `cs_user_agent` - User agent string
  * `cs_host` - Host header value
  * `body` - Any additional content
</details>

<details>
  <summary>
    <b>alb_log</b>

     \- AWS Application Load Balancer logs
  </summary>

  * `type` - Connection type (HTTP, HTTPS, etc.)
  * `timestamp` - Request timestamp
  * `elb` - Load balancer name
  * `client_ip` - Client IP address
  * `client_port` - Client port
  * `target_ip` - Target IP address
  * `target_port` - Target port
  * `request_processing_time` - Time from connection to routing decision
  * `target_processing_time` - Time from request to response from target
  * `response_processing_time` - Time from response from target to client
  * `elb_status_code` - Response code from load balancer
  * `target_status_code` - Response code from target
  * `received_bytes` - Bytes received from client
  * `sent_bytes` - Bytes sent to client
  * `cs_method` - HTTP method
  * `cs_uri_whole` - Request URL
  * `cs_version` - HTTP version
  * `user_agent` - User agent string
  * `ssl_cipher` - SSL cipher
  * `ssl_protocol` - SSL/TLS protocol
</details>

<details>
  <summary>
    <b>syslog_log</b>

     \- Standard system logs
  </summary>

  * `timestamp` - Log timestamp
  * `log_hostname` - Host name
  * `log_syslog_tag` - Syslog tag
  * `log_procname` - Process name
  * `log_pid` - Process ID
  * `body` - Log message content
  * `log_pri` - Priority value
  * `syslog_version` - Syslog version
  * `log_msgid` - Message ID
  * `log_struct` - Structured data
</details>

<details>
  <summary>
    <b>redis_log</b>

     \- Redis database logs
  </summary>

  * `pid` - Process ID
  * `timestamp` - Log timestamp
  * `level` - Log level
  * `role` - Redis role (master, slave, etc.)
  * `body` - Log message content
</details>

This is not an exhaustive list of all fields for all formats. Each format has specific patterns and may extract additional fields based on the log content. When using Log IQ, you can explore the extracted fields in the Parseable UI or through SQL queries.

<Callout type="info">
  In case of p\_format\_verified = false, for a known format listed above, raise a Git issue to add the format.
</Callout>


# Logs (/docs/user-guide/logs)





Logs explorer is the primary interface for searching, filtering and analyzing log data in Parseable. It supports field level filtering, SQL querying, time-series visualization with forecasting, and exporting results.

<img alt="Logs Explore page overview" src={__img0} placeholder="blur" />

## Page Layout

The Logs Explore page is organized into four main areas:

* **Top Toolbar** - Dataset selector, time range picker, refresh controls, saved views, and the AI summarization button
* **Left Sidebar (Fields Panel)** - System-detected field categories, table fields currently displayed, and all available fields in the selected dataset
* **Histogram Chart** - A time-series bar chart that visualizes log volume over the selected time range, with an optional forecast overlay
* **Log Table** - Individual log records in a paginated, sortable table with configurable columns and inline expansion

## Dataset Selector

The dataset selector dropdown is at the top-left of the content area. Click it to search for and switch between available log datasets. The dropdown includes a search box that filters the list as you type. Selecting a different dataset reloads the page with that dataset's data and fields.

## Time Range Picker

Click the time range button (e.g., "Last 1 hour") to open the time range configuration panel:

* **Quick presets** - Select common durations: 10 min, 1 hr, 5 hrs, 1 day, and 3 days
* **Custom range** - Use the calendar and time inputs to set precise "From" and "To" dates and times
* **Timezone** - Choose the timezone for the displayed times (e.g., "UTC (UTC) +0:00")

Click **Apply** to execute the query or **Cancel** to discard changes.

<Callout type="info">
  Parseable requires a time range for every query. By scoping queries to a specific time window, the engine only reads the relevant Parquet files from storage, keeping response times fast even over large datasets.
</Callout>

## Refresh and Auto-Refresh

* **Manual refresh** - The circular arrow icon triggers an immediate re-query of the data within the current time range
* **Auto-refresh** - The button labeled "Off" (by default) opens a dropdown with interval options: 10s, 30s, 1m, 5m, 10m, and 20m. Selecting an interval causes the query to re-execute automatically at that cadence

## Save View

Click **Save view** to persist the current query configuration (filters, selected fields, and optionally the time range) for future reuse. The dialog includes a required Title field, an optional Description field, and an **Include time range** toggle.

## View Library

Click **Library** to open a slide-out panel with three tabs:

* **Recent** - Views you have recently accessed
* **My views** - Views you have created
* **All views** - All saved views across the team

A search bar at the top lets you filter saved views by name. Click a saved view to load its stored configuration.

## Summarize My Data

Click the **Summarize my data** button (purple with a sparkle icon) to trigger an AI-powered summary of the current log data. This analyzes the queried logs and generates insights about patterns, anomalies, and key observations. See [AI Native](/docs/user-guide/ai-native) for more details.

## Fields Panel

The fields panel on the left side organizes the dataset's schema into three sections.

### System Fields

The **System** section surfaces automatically detected field categories:

* **Log formats** - Detected log format patterns with occurrence counts. Each entry has include (funnel with plus) and exclude (funnel with minus) filter icons for one-click filtering
* **User agents** - Detected user agent strings with include/exclude filter options
* **Source IPs** - Detected source IP addresses with include/exclude filter options

### Table Fields

Shows columns currently displayed in the log table. By default, these are "Ingestion Time" and "Data." Click a table field to expand it and see its **Top 5 Values** with occurrence counts. Each value has include/exclude filter icons.

Each table field shows action icons on hover: a pin icon, a filter icon, a minus icon (to remove the column), and a collapse arrow. Fields can be reordered by drag-and-drop.

### Available Fields

Lists all fields in the dataset not currently shown as table columns. The count in the header (e.g., "Available fields (39)") indicates how many fields exist. Click the plus icon on any field to add it as a table column.

### Search Field Names

A search box at the top of the fields panel ("Search field names") filters the field list by partial name match.

## Add Filter

Click **Add filter** to open a comprehensive filter panel. This panel organizes filterable fields into semantic categories: Service, Kubernetes, Container, Cloud, HTTP, Telemetry, and All fields.

For each field, you see available values along with occurrence counts. Click a value to add it as a filter condition. A search box at the top ("Search and add filters") locates specific fields or values quickly. Some fields show a "Show more values" link when there are more values than initially displayed.

## Edit with SQL

Click **Edit with SQL** to open the [SQL Editor](/docs/user-guide/sql-editor) in a new tab with a pre-populated query (`select * from "dataset-name"`) targeting the current dataset.

## Group By

Click **Group by** and select a field from the dropdown (body, cloud.provider, cloud.region, http.method, http.status\_code, etc.). This groups the log data by that field's values, restructuring the histogram and table to show aggregated results.

## Histogram Chart

The histogram chart visualizes the volume of log records over time. The Y-axis shows the record count and the X-axis shows time intervals. The chart automatically adjusts its time granularity based on the selected range.

### Forecast

A **Forecast** toggle in the upper-right of the chart enables predictive analytics. When enabled, the chart extends beyond the current time to show projected log volume. The legend differentiates between "Historical" data (solid line) and "Forecast" data (dashed line), with the forecast region shown as a shaded area.

## Log Table

The log table displays individual log records.

### Sorting

Click any column header to toggle between ascending and descending sort order.

### Row Display

Each row shows values for the configured table columns. By default, "Ingestion Time" shows the timestamp and "Data" shows a formatted view of the log record's key-value pairs. Field names appear in a muted color while values appear in an accent color for easy scanning.

### Row Expansion

Click a log row to reveal an expand icon and a copy icon. Click the expand icon to display all fields of the log record in a formatted key-value layout, including body, cloud metadata, HTTP details, Kubernetes labels, telemetry information, trace and span IDs, and all other attributes.

### Pagination

Pagination controls include previous/next page arrows, a page size selector (10, 50, 100), and a status indicator showing total records found and query execution time (e.g., "Found 3K records in 163.73 ms").

### Find in Data

A search box labeled "Find in data" provides client-side text search within the currently displayed log records.

## Table Toolbar

The table toolbar includes four icon buttons to the right of the "Find in data" box:

* **Share** - Generates a shareable link to the current view
* **Maximize** - Expands the table to a larger view
* **Wrap Text** - Toggles text wrapping in the Data column
* **Export** - Opens a dropdown with two options: **Export CSV** and **Export JSON**

## Toggle Fields Panel

A small icon button to the left of the "Add filter" button toggles the visibility of the left fields panel. Collapsing it gives the histogram and log table the full width of the page.

## Keyboard Shortcuts

| Shortcut          | Action                                                         |
| ----------------- | -------------------------------------------------------------- |
| `⌘ K`             | Open the global search dialog from anywhere in the application |
| `⌘ ↵` (Cmd+Enter) | Execute a query in the SQL Editor                              |


# Metrics (/docs/user-guide/metrics)











Metrics explorer is the central interface for browsing, analyzing, and acting on metrics data in Parseable. It provides a visual overview of all metrics in a dataset, tools for filtering and drilling down into individual metrics, and pathways to create alerts, dashboards, and SQL queries directly from your metric data.

<img alt="Metrics explorer page overview" src={__img0} placeholder="blur" />

## Page Layout

The Metrics explorer page is organized into three main areas:

* **Left Sidebar (Field Browser)** - A categorized and searchable list of all fields (labels) present in the selected metrics dataset
* **Central Content Area** - A summary chart of total metric volume over time, and a table listing all discovered metrics with their descriptions, data point counts, and types
* **Right Detail Panel** - Appears when you click on a specific metric, showing an expanded overview, timeseries chart, alert configuration, and field details

## Selecting a Dataset

A dataset selector dropdown at the top-left lets you choose which metrics dataset to explore. Click the dropdown to search for and switch between available datasets.

## Main Tabs

Three tabs at the top of the content area provide different ways to interact with your metric data.

### All Metrics Tab

This is the default view. It displays a summary timeseries chart at the top showing total metric data point volume, followed by a metrics table listing all metrics in the dataset. Each row shows the metric name, a data point count badge (e.g., 338.3K), a description, and a type badge (such as `sum` or `gauge`). Metrics are sorted by data point count in descending order.

Click any metric row to open the metric detail panel on the right.

### Insights Tab

The Insights tab provides a tile-based analysis view for deeper exploration.

<img alt="Insights tab with metric tile and bar chart" src={__img1} placeholder="blur" />

The configuration panel at the top includes:

* **Metric selector** - The metric to analyze
* **Type badge** - The metric type (e.g., `sum`) with a dropdown
* **Units** - Optional unit label
* **Precision** - Decimal precision selector
* **Add filter** - Filter the metric by label values
* **Group & sort** - Expand to reveal Group by and Sort by fields for slicing data by any label dimension

Each tile displays a bar chart with aggregation toggles: count, sum, avg, min, and max. A **Time grain** dropdown (defaulting to Minute) controls the temporal resolution.

A three-dot menu on each tile offers:

* **Add to dashboard** - Adds the chart to a dashboard
* **Set alert** - Opens the alert creation form pre-filled with the metric
* **Download as PNG** - Exports the chart image

Click **+ Add new tile** to compare different metrics side by side.

### Table Tab

The Table tab shows raw metric data in a tabular format.

The left sidebar adapts to show:

* **System fields** - Built-in fields like Log formats, User agents, and Source IPs
* **Table fields** - Currently displayed columns (by default, Ingestion Time and Data)
* **Available fields** - All 48+ fields available in the dataset that can be added as table columns

The data table shows an Ingestion Time column and a Data column containing the full key-value pairs for each data point. Above the table, pagination controls, a record count indicator (e.g., "Found 2.2M records in 292.88 ms"), and a **Find in data** search box are available. A **Group by** button lets you group raw records by specific field values.

## Field Browser

The left sidebar provides a categorized view of all fields in the metrics dataset. Fields are organized under semantic categories such as System, Service, Kubernetes, Container, Error, Metric, Cloud, Database, Network, Telemetry, and All fields.

A **Search field names** text box at the top lets you quickly find specific fields. Expanding an individual field shows its distinct values along with occurrence counts. Next to each field value, two filter icons appear:

* **Include filter** (funnel with +) - Adds a positive filter for that value
* **Exclude filter** (funnel with −) - Filters out records with that value

The sidebar can be collapsed using the toggle button to give the main content area more space.

## Filtering

Click **Add filter** to open the filter panel. Fields are organized by category (Service, Kubernetes, Container, Error, Metric, Cloud, Database, Telemetry, All fields). Each field displays its distinct values as clickable chips with occurrence counts.

<img alt="Filter panel with field categories and values" src={__img2} placeholder="blur" />

Use the **Search and add filters** text box to locate specific fields or values. Click any value chip to add it as an active filter. Filters can also be added directly from the field browser sidebar by clicking the include/exclude icons next to field values.

## Time Range

Click the time range button (e.g., "Last 1 hour") to configure the query window:

* **Quick presets** - 10 min, 1 hr, 5 hrs, 1 day, 3 days
* **Custom range** - Calendar-based date/time selection with From and To fields
* **Timezone** - Timezone selector (defaults to UTC)

Click **Apply** to confirm or **Cancel** to discard.

## Auto-Refresh

* **Manual refresh** - The circular arrow icon triggers an immediate data refresh
* **Auto-refresh** - Dropdown with interval options: 10s, 30s, 1m, 5m, 10m, or 20m

## Forecast

A **Forecast** toggle in the upper-right area of the summary chart enables predictive visualization. When enabled, the chart extends beyond the current time to show forecasted values. The legend distinguishes between "Historical" data (solid line) and "Forecast" data (dashed line).

## Metric Detail Panel

Click any metric in the metrics table to open the detail panel on the right. The panel header shows the metric name (with a copy icon), type badge, description, latest timestamp, and current value.

<img alt="Metric detail panel with timeseries chart" src={__img3} placeholder="blur" />

### Overview Sub-tab

Displays a timeseries bar chart showing the metric's behavior over the selected time range. Controls include:

* A dedicated time range selector and refresh controls
* **Set alert** button to create an alert directly from the metric
* **Add to dashboard** button to add the chart to a dashboard
* **Time grain** dropdown (defaults to Minute) for temporal resolution
* **Aggregation buttons** - count, sum, avg, min, max

### Alerts Sub-tab

Shows all alerts configured for the selected metric. If no alerts exist, a **Set alert** button is available to create one. See [Alerting](/docs/user-guide/alerting) for details.

### Fields Sub-tab

Displays all fields associated with the selected metric organized by category (Service, Kubernetes, Container, Metric, Cloud, Telemetry, All fields). Each row shows a field name and its value for the most recent data point. A **Search field name** text box filters the field list.

## Creating Alerts from Metrics

Click **Set alert** from either the metric detail panel or the Insights tile menu. This navigates to the **Alerts > Create** page with the metric context pre-filled. The alert creation form has four steps:

1. **Set rule** - Configure the dataset, metric, aggregation function (e.g., AVG), optional units, filters, and optional Group by fields
2. **Set Evaluation** - Choose the alert type: Threshold, Anomaly Detection, or Forecast. Configure the evaluation window, repetition interval, and trigger condition
3. **Targets** - Specify notification delivery targets and repeat interval
4. **Title and severity** - Enter the alert title, select severity, and optionally add tags

A live chart/table preview at the top shows the metric data alongside the configured threshold. For more details, see [Alerting](/docs/user-guide/alerting).

## Adding Metrics to Dashboards

Click **Add to dashboard** to open a dialog where you can search existing dashboards, select one, or click **+ Create new** to create a new dashboard. The metric chart is added as a tile on the chosen dashboard. For more on dashboards, see [Dashboards](/docs/user-guide/dashboards).

## Edit with SQL

Click **Edit with SQL** to open the [SQL Editor](/docs/user-guide/sql-editor) in a new tab with a pre-populated query (e.g., `select * from "otel-demo-metrics"`).

## Save View

Click **Save view** to persist the current filters, time range, and configuration as a reusable view. Provide a Title (required), optional Description, and toggle **Include time range** to save the time window as part of the view.

## View Library

Click **Library** to open the view library with three tabs:

* **Recent** - Recently accessed views
* **My views** - Views you created
* **All views** - All views across the team

A search field lets you find views by name.

## Summarize My Data

Click the **Summarize my data** button (sparkle icon) for an AI-powered summary of your metrics dataset. This provides automated insights and observations about the data. See [AI Native](/docs/user-guide/ai-native) for more details.


# OpenID Connect (/docs/user-guide/openid)



Parseable supports OpenID Connect (OIDC) authentication for secure access to all its functionality. An OpenID server publishes its metadata at a well-known URL, typically `https://server.com/.well-known/openid-configuration`. Parseable uses OpenID connect discovery mechanism to connect to Identity providers.

## Prerequisites

Before you begin, make sure you have the following prerequisites:

* A configured OIDC provider which provides group claims for each user. Parseable will map the group name for a user with role created in the instance.
* Knowledge of your OIDC identity provider and its configuration details.
* A Parseable instance with admin access and the endpoint to access Parseable should have TLS certification (`https://parseable-endpoint`)
* You need to set the redirect uri in the OIDC identity provider to `<parseable-instance-url>/api/v1/o/code`. For example, if Parseable instance is hosted at `https://demo.parseable.com/` then the redirect uri should be `https://demo.parseable.com/api/v1/o/code`.
* You need to add the encryption key on your OIDC provider used to encrypt the keys.
* Default OIDC role created on Parseable instance.

## Environment Variables

To use OIDC authentication with Parseable, you need to set the following environment variables:

| Variable Name           | Required | Description                                                                                                                                      | Default | Example                                                      |
| ----------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | ------------------------------------------------------------ |
| P\_OIDC\_CLIENT\_ID     | Yes      | Your OIDC client identifier provided by your identity provider.                                                                                  | ""      | "client-id from the OIDC identity provider"                  |
| P\_OIDC\_CLIENT\_SECRET | Yes      | Your OIDC client secret provided by your identity provider.                                                                                      | ""      | "client-secret from the OIDC identity provider"              |
| P\_OIDC\_ISSUER         | Yes      | The OIDC issuer URL, typically provided by your identity provider. It points to the OIDC authorization server. Should support discovery protocol | ""      | "[https://accounts.google.com](https://accounts.google.com)" |
| P\_ORIGIN\_URI          | Yes      | The URI where Parseable is hosted or accessible. This should be the base URL of your Parseable instance.                                         | ""      | "[https://demo.parseable.com/](https://demo.parseable.com/)" |

## Privilege Management with OIDC

You can either setup a default OIDC role on Parseable instance or map a user group from your identity provider to a role on Parseable instance.

### Assign default role to any new OIDC user

Users that are not a part of group(s) or are part of group(s) where corresponding role is not created on Parseable, will be assigned a default role.

Follow below steps to set default OIDC role on Parseable instance:

1. Login to Parseable with admin access
2. Click on "Users" from the left pane
3. Click on "Create Role", provide the name of the role and the privilege to assign

Once created, Click on "Set Default OIDC Role", select the role just created from the dropdown and click on "Set Default OIDC Role".

### Multi-Role Support

Parseable's OIDC integration supports **assigning multiple roles to a single user**, providing flexible, fine-grained access control for your team.

**Benefits:**

* Give a DevOps engineer both `writer` and `reader` roles for different datasets
* Grant a user `reader` permissions, so they can review logs across datasets without manual role shuffling
* All roles are respected in UI and API, just assign them in your OIDC provider and Parseable does the rest

### Map user groups to roles on Parseable

To map your user group to a role on Parseable you must first create that role on Parseable instance with the same name as the user group from your identity provider. To create roles in Parseable, you can use the Create a role API. This allows you to define custom roles for users, granting them specific privileges and permissions within the application.

Once we have roles setup now your users can login with SSO and all the permissions will be immediately granted. Please note that per user customization is not an option for OIDC users. It is recommended you create a new role if such case arises.


# Role Based Access Control (/docs/user-guide/rbac)



There are five entities in Parseable Access Control model - **Action**, **Privilege**, **Resource**, **Role** and **User**. Below section explains each of these entities in detail.

* **Actions**: Each API corresponds to an Action on the Parseable server.
* **Privilege**: It is a group of allowed actions. Actions and Privileges are predefined within a Parseable server instance. Current Privileges are Admin, Editor, Writer, Reader and Ingester.
* **Resources**: Log datasets are Resources. Each Resource has a unique name. For example, a log dataset with name my\_dataset is a Resource.
* **Roles**: Roles are dynamic, named entities on a Parseable server instance. Each role has a set of privileges and resources associated with it. A role can be assigned to several users. A user can have multiple roles assigned to it.
* **Users**: Users refer to human or machine entities that can perform actions on a Parseable server instance. Each user has a unique username and password. A user can be assigned one or more roles.

<Callout type="info">
  User passwords are hashed and stored in Parseable metadata file. Parseable does not store the password in plain text.
</Callout>

## Overview of Roles & Access

Each role—Admin, Editor, Writer, Reader, and Ingestor—has varying access to different endpoints, categorized into six sections: General, Access Management, Resource Based, Stream Related, and Query & Ingest Logs Related. Access permissions are denoted with either `✓` (allowed) or `x` (denied).

### General

This section covers general system and informational endpoints, which are accessible to most roles for actions such as viewing the system's status or metrics.

| Action             | Endpoint                    | Admin | Editor | Writer | Reader | Ingester |
| ------------------ | --------------------------- | ----- | ------ | ------ | ------ | -------- |
| GetAbout           | GET /about                  | ✓     | ✓      | ✓      | ✓      | x        |
| GetAnalytics       | GET /analytics              | ✓     | x      | x      | x      | x        |
| GetLiveness        | HEAD /liveness              | ✓     | ✓      | ✓      | ✓      | x        |
| GetReadiness       | HEAD /readiness             | ✓     | ✓      | ✓      | ✓      | x        |
| ListCluster        | GET /cluster/info           | ✓     | x      | x      | x      | x        |
| ListClusterMetrics | GET /cluster/metrics        | ✓     | x      | x      | x      | x        |
| DeleteIngestor     | DELETE /cluster/\{ingestor} | ✓     | x      | x      | x      | x        |
| Metrics            | GET /metrics                | ✓     | ✓      | x      | x      | x        |

### Access Management

This section deals with endpoints for managing roles and users. Only Admins have access to critical actions like creating, updating, and deleting roles or users, ensuring proper control over access management in the system.

| Action       | Endpoint                                     | Admin | Editor | Writer | Reader | Ingester |
| ------------ | -------------------------------------------- | ----- | ------ | ------ | ------ | -------- |
| PutRole      | PUT /role/default                            | ✓     | x      | x      | x      | x        |
| PutRole      | PUT /role/\{name}                            | ✓     | x      | x      | x      | x        |
| GetRole      | GET /role/default                            | ✓     | x      | x      | x      | x        |
| GetRole      | GET /role/\{name}                            | ✓     | x      | x      | x      | x        |
| DeleteRole   | DELETE /role/\{name}                         | ✓     | x      | x      | x      | x        |
| ListRole     | GET /role                                    | ✓     | x      | x      | x      | x        |
| PutUser      | POST /user/\{username}                       | ✓     | x      | x      | x      | x        |
| PutUser      | POST /user/\{username}/generate-new-password | ✓     | x      | x      | x      | x        |
| ListUser     | GET /user                                    | ✓     | x      | x      | x      | x        |
| DeleteUser   | DELETE /user/\{username}                     | ✓     | x      | x      | x      | x        |
| PutUserRoles | PUT /user/\{username}/role                   | ✓     | x      | x      | x      | x        |
| GetUserRoles | GET /user/\{username}/role                   | ✓     | ✓      | ✓      | ✓      | x        |

### Resource Management

This section defines access to resources such as dashboards and filters. While most roles can view and create resources, only Admins and Editors have permission to modify or delete them.

| Action          | Endpoint                            | Admin | Editor | Writer | Reader | Ingester |
| --------------- | ----------------------------------- | ----- | ------ | ------ | ------ | -------- |
| ListDashboard   | GET /dashboards                     | ✓     | ✓      | ✓      | ✓      | x        |
| GetDashboard    | GET /dashboards/\{dashboard\_id}    | ✓     | ✓      | ✓      | ✓      | x        |
| CreateDashboard | POST /dashboards                    | ✓     | ✓      | ✓      | ✓      | x        |
| CreateDashboard | PUT /dashboards/\{dashboard\_id}    | ✓     | ✓      | ✓      | ✓      | x        |
| DeleteDashboard | DELETE /dashboards/\{dashboard\_id} | ✓     | ✓      | ✓      | ✓      | x        |
| ListFilter      | GET /filters                        | ✓     | ✓      | ✓      | ✓      | x        |
| GetFilter       | GET /filters/\{filter\_id}          | ✓     | ✓      | ✓      | ✓      | x        |
| CreateFilter    | POST /filters                       | ✓     | ✓      | ✓      | ✓      | x        |
| CreateFilter    | PUT /filters/\{filter\_id}          | ✓     | ✓      | ✓      | ✓      | x        |
| DeleteFilter    | DELETE /filters/\{filter\_id}       | ✓     | ✓      | ✓      | ✓      | x        |

### Stream Related

This section deals with endpoints for managing datasets. Admins and Editors have full access to these endpoints, while other roles have limited or no access to dataset management functionalities.

| Action               | Endpoint                               | Admin | Editor | Writer | Reader | Ingester |
| -------------------- | -------------------------------------- | ----- | ------ | ------ | ------ | -------- |
| CreateStream         | PUT /logstream/\{logstream}            | ✓     | ✓      | x      | x      | x        |
| DeleteStream         | DELETE /logstream/\{logstream}         | ✓     | ✓      | x      | x      | x        |
| GetSchema            | GET /logstream/\{logstream}/schema     | ✓     | ✓      | ✓      | ✓      | x        |
| GetStats             | GET /logstream/\{logstream}/stats      | ✓     | ✓      | ✓      | ✓      | x        |
| GetStreamInfo        | GET /logstream/\{logstream}/info       | ✓     | ✓      | ✓      | ✓      | x        |
| ListStream           | GET /logstream                         | ✓     | ✓      | ✓      | ✓      | x        |
| PutAlert             | PUT /logstream/\{logstream}/alert      | ✓     | ✓      | ✓      | x      | x        |
| GetAlert             | GET /logstream/\{logstream}/alert      | ✓     | ✓      | ✓      | x      | x        |
| PutHotTierEnabled    | PUT /logstream/\{logstream}/hottier    | ✓     | ✓      | ✓      | x      | x        |
| GetHotTierEnabled    | GET /logstream/\{logstream}/hottier    | ✓     | ✓      | ✓      | x      | x        |
| DeleteHotTierEnabled | DELETE /logstream/\{logstream}/hottier | ✓     | ✓      | ✓      | x      | x        |
| GetRetention         | GET /logstream/\{logstream}/retention  | ✓     | ✓      | ✓      | x      | x        |
| PutRetention         | PUT /logstream/\{logstream}/retention  | ✓     | ✓      | ✓      | x      | x        |

### Query & Ingest Logs Related

This section highlights endpoints related to querying and ingesting logs. Admins and Editors have full access to these functionalities, while other roles, like Readers and Ingestors, may have restricted access depending on their responsibilities.

| Action   | Endpoint                     | Admin | Editor | Writer | Reader | Ingester |
| -------- | ---------------------------- | ----- | ------ | ------ | ------ | -------- |
| Ingest   | POST /logstream/\{logstream} | ✓     | ✓      | ✓      | x      | ✓        |
| Ingest   | POST /ingest                 | ✓     | ✓      | ✓      | x      | ✓        |
| Query    | POST /query                  | ✓     | ✓      | ✓      | ✓      | x        |
| QueryLLM | POST /llm                    | ✓     | ✓      | ✓      | ✓      | x        |

### Get started

#### Creating a Role

This is the first step in setting up Role Based Access Control (RBAC) for Parseable. Use the Create Role API to create a role. The Create Role API request body requires the role definition in JSON format. Below examples demonstrate sample JSON for different types of role and privileges.

Role JSON with Admin Privilege

```json
[
    {
        "privilege": "admin"
    }
]
```

Role JSON with Editor Privilege

```json
[
    {
        "privilege": "editor"
    }
]
```

Role JSON with Writer Privilege: The Writer privilege is resource specific. A user with above role json, will be able to call the Writer specific API only on the specified resource. In the above example, the user will be able to call Writer specific API on backend and frontend datasets only.

```json
[
    {
        "privilege": "writer",
        "resource": {
            "dataset": "backend"
        }
    },
    {
        "privilege": "writer",
        "resource": {
            "dataset": "frontend"
        }
    }
]
```

Role JSON with Ingester Privilege: The Ingester privilege is resource specific. A user with above role json, will be able to call the Ingester specific API only on the specified resource. In the above example, the user will be able to call Ingester specific API on backend and frontend datasets only. This privilege is useful to be set in log agents, forwarders, and other log ingestion tools.

```json
[
    {
        "privilege": "ingester",
        "resource": {
            "dataset": "backend"
        }
    },
    {
        "privilege": "ingester",
        "resource": {
            "dataset": "frontend"
        }
    }
]
```

Role JSON with Reader Privilege: The Reader privilege is resource specific. A user with above role json, will be able to call the Reader specific API only on the specified resources. In the above example, the user will be able to call Reader specific API on frontend dataset, and only on events with tag source=web.

```json
[
    {
        "privilege": "reader",
        "resource": {
            "dataset": "frontend",
            "tag": "source=web"   // optional field
        }
    }
]
```

### Creating User

To create a User, use the Create User API. Here you can optionally pass a request body that has appropriate role name (as explained in the role section) to assign a role to the user.

After successful Create User API call, you'll get the user's password in the response. Keep it in a safe place as this is the only time server will return the password in plain text.

### Assign a role

To assign a role to a user after creating a user, use the Assign Role API. This API takes the username and role name as input. After a successful API call, the user will be able to perform actions allowed by the assigned role.

### Reset password

In any case if you need to reset password for a user. This can be done through Reset Password API.

### Delete user

To delete a user, use the Delete User API. This API will delete the user and all the roles assigned to it.

### OpenID Connect

For managing roles for your OAuth2 users, refer to OIDC section. Roles are automatically assigned by matching the role name with group name that is obtained to groups claim in the id token.


# Retention (/docs/user-guide/retention)



<OfferingPills pro enterprise className="mb-4" />

Parseable allows setting the retention, or the amount of time that log data is kept in the system, for each dataset. The time can be set to a multiple of 1 day. Note that retention works at a dataset level, and each dataset can have a different retention period. Also, you can only set a single dataset per retention period.

## Setting up

You can set Retention via the Dataset Management page (Dataset >> Manage >> Retention). If you're using external applications to interact with Parseable, you can also use the retention API calls. Refer to the [API documentation](/docs/api) for details.

## Configuration

Here is sample retention configuration, with all the available options.

```json
[
    {
        "duration": "20d",
        "action": "delete",
        "description": "delete logs after 20 days"
    }
]
```

This table explains the configuration options.

| Variable Name | Required | Description                                                                                    |
| ------------- | -------- | ---------------------------------------------------------------------------------------------- |
| duration      | Yes      | Total duration for which logs should be retained. Can be multiple of 1 day, e.g. 20d.          |
| action        | Yes      | Action to be taken when log data passes retention duration. Currently only delete is supported |
| description   | No       | Human friendly description of the log retention rule                                           |


# Smart Cache (/docs/user-guide/smart-cache)



<OfferingPills pro enterprise className="mb-4" />

<Callout type="info">
  Smart cache is only available to be set-up through API and not natively supported in the UI from Release `v2.0.0` onwards. We are working on adding this feature to Prism and it will be available soon.
</Callout>

## How it works

Tiering in Parseable allows keeping a copy of log data on the query node (in addition to the object store). You can create storage tiers on query node disks, allowing hot/recent data on SSD and older data backed by S3/object storage. This architecture allows for much faster query response, while keeping costs very low because data is always backed on object store.

The tiered storage capacity works at the log dataset level. You can specify the size on disk available to a specific dataset for its hot tier data. This is useful for situations where different datasets have different query patterns, i.e. some dataset need to be queried for predominantly recent data, while others not so much.

## Setup hot tier

To enable hot tier for a query node, add the environment variable `P_HOT_TIER_DIR` to the query node (or the standalone node) before starting the server. The value of environment variable should be set to the path of directory that you want to use for the data store. For example, `P_HOT_TIER_DIR=/path/to/hot/tier/directory`.

Setting the environment variable enables the global hot tier mechanism. You'll now need to set hot tier size for specific datasets based on your requirements. The setting is available in the Manage page of each dataset, under the Hot Tier Storage Size section.

## Under the hood

When the global hot tier mechanism is enabled, the server identifies the drive (where the hot tier directory is created) and calculates the total size and the free size of the drive. The upper threshold for hot tier size is set to 80% of the total drive capacity. So if the drive is of 10 TiB, then 8 TiB is automatically considered the maximum size of hot tier (subject to disk availability).

## Size allocation

Now when a specific dataset requests a hot tier capacity of let's say `2 TiB`, server checks if it is possible to allocate. The maths is : max size possible (8 TiB) - total used size of the disk (assume `1.3 TiB`) = `6.7 TiB`. The server then allocates the `2 TiB` to this dataset.

Once the hot tier is set up, a scheduler is configured to run every minute. This scheduler verifies if new files are available in remote object store and downloads them to the hot tier, ensuring that your most recent and frequently accessed data is always readily available.

## Populating hot tier

Based on the size allocated for the hot tier (for a dataset), the server starts downloading Parquet files from object store, beginning with the most recent data and moving backward in time. This approach ensures that the latest data, which is more likely to be queried, is prioritized.

As each file is downloaded, it’s recorded in a `hottier.manifest.json` file. This manifest file is crucial for tracking which Parquet files are stored locally in the hot tier. Along with this, the system also updates the available and used sizes in the hot tier's JSON file, providing a clear view of the hot tier’s current state.

The server deletes the oldest files when necessary. This happens under two conditions:

* Size exhaustion: When the total size of the files in the hot tier reaches the allocated limit.

* Disk usage threshold: When the combined disk usage, including the hot tier, exceeds the configured disk usage threshold (e.g., 80%).

The `hottier.manifest.json` is updated to reflect the removal of old files, ensuring that the hot tier remains within its defined constraints while continuing to serve the most relevant data efficiently.

## Query flow for hot tier

On receiving a query, the server fetches the dataset.json and related manifest.json files based on the query time range. It then identifies the list of Parquet file paths from the manifest. The server checks if these files are available in the hot tier. If any of the Parquet files are present in the hot tier path, server utilizes those file, avoiding S3 GET calls. For files not in the hot tier, the system fetches the necessary data from S3.

## Adjusting the hot tier Size

If you need to adjust the size of the hot tier for an existing dataset, you can do so with via the dataset Management page. Here’s how it works:

* Increasing the hot tier Size: When you increase the size of an existing hot tier, the system updates the meta file to reflect the new size. This allows for additional data to be stored locally without any interruption in service.
* Decreasing the hot tier Size: Reducing the size of the hot tier is not allowed. If you attempt to do so, the server will respond with an error, maintaining the integrity of your current data storage setup.


# SQL Editor (/docs/user-guide/sql-editor)













Parseable provides a powerful SQL editor that allows you to query your telemetry data (logs, metrics, and traces) using PostgreSQL compatible SQL syntax.

<img alt="SQL Editor" src={__img0} placeholder="blur" />

## Getting Started

1. Navigate to the SQL Editor in the Parseable UI
2. Select your dataset from the dropdown
3. Write your SQL query
4. Click "Run" to execute

## Features

* **Full SQL Support** - Use standard SQL queries to analyze your data
* **Auto-completion** - Intelligent suggestions as you type
* **Query History** - Access your previous queries
* **Export Results** - Download query results in various formats

## Example Queries

```sql
-- Get recent data
SELECT * FROM mystream LIMIT 100

-- Count by level
SELECT level, COUNT(*) as count 
FROM mystream 
GROUP BY level

-- Filter by time range
SELECT * FROM mystream 
WHERE p_timestamp > NOW() - INTERVAL '1 hour'
```

## Query with Regular Expressions

Examples of how to use regular expressions in Parseable queries:

### Match regular expression (Case Sensitive)

```sql
SELECT * FROM frontend where message ~ 'failing' LIMIT 9000;
```

### Match regular expression (Case Insensitive)

```sql
SELECT * FROM frontend where message ~* 'application' LIMIT 9000;
```

### Does not match regular expression

```sql
SELECT * FROM frontend where message !~ 'started' LIMIT 9000;
```

### Matches the beginning/end of the string

```sql
SELECT * FROM frontend where message ~* '^a' LIMIT 9000;
SELECT * FROM frontend where message ~ 'failing$' LIMIT 9000;
```

### Replace with REGEXP\_REPLACE

```sql
SELECT REGEXP_REPLACE(uuid,'[0-9]','*','g') FROM frontend LIMIT 9000;
```

### Split a string with SPLIT\_PART

```sql
SELECT SPLIT_PART(email,'@',1) FROM frontend where email is not null LIMIT 10;
```

### Pattern matching with LIKE

```sql
SELECT * FROM frontend where email LIKE '%test%' LIMIT 10;
```

## Case Sensitivity

Dataset column names are case sensitive. To query column names with uppercase letters, use double quotes:

```sql
SELECT * FROM dataset WHERE "Foo" = 'bar'
```

## Query Analysis

To view the detailed query execution plan, use the `EXPLAIN ANALYZE` keyword:

```sql
EXPLAIN ANALYZE SELECT * FROM frontend LIMIT 100
```

## Response Fields Information

To get the query result fields as a part of query API response, add the query parameter `fields=true`:

```
http://localhost:8000/api/v1/query?fields=true
```

## Add Charts to Dashboard

After running a query, you can visualize the results and add them directly to a dashboard.

<img alt="Add to Dashboard" src={__img1} placeholder="blur" />

## Filters and Group By

Use the filter panel to slice and dice your data, and group results by any field.

<img alt="Filters" src={__img2} placeholder="blur" />

<img alt="Group By" src={__img3} placeholder="blur" />

## Query Library

Save queries you want to reuse in the Library for quick access.

<img alt="Query Library" src={__img4} placeholder="blur" />

## Tips

* Use `p_timestamp` for time-based filtering
* Use `LIMIT` to prevent large result sets
* Use `GROUP BY` for aggregations
* For AI-powered query generation, see [Text to SQL](/docs/user-guide/ai-native/text-to-sql)


# Traces (/docs/user-guide/traces)







Traces explorer is the primary interface for searching, filtering, and analyzing distributed traces in Parseable. It provides a scatter-plot of trace durations over time, a paginated trace list, powerful filtering capabilities, and detailed span-level inspection with a waterfall view.

<img alt="Traces explorer page overview" src={__img0} placeholder="blur" />

## Page Layout

The Traces explorer page is composed of four main areas:

* **Top Toolbar** - Dataset selector, Traces/Table tabs, time range picker, refresh controls, saved views, and AI summarization
* **Left Sidebar (Field Browser)** - A categorized and searchable list of all trace attributes and span fields
* **Central Content Area** - A scatter-plot of trace durations and a paginated trace list (Traces view), or a line chart and raw span table (Table view)
* **Detail Panels** - Contextual panels that appear when you click on a trace or span

## Dataset Selector

A dropdown at the top-left shows the currently selected trace dataset (e.g., "k8s-traces"). Click it to open a searchable dropdown listing all available trace datasets. Selecting a different dataset reloads the page with that dataset's traces and field schema.

## Traces / Table Tabs

Two tabs toggle between the **Traces** view and the **Table** view:

* **Traces** - The default view, optimized for trace-level exploration with a scatter chart and trace list
* **Table** - Displays individual span records in a flat tabular format, useful for raw data inspection and bulk analysis

## Time Range Picker

Click the time range button (e.g., "Last 1 hour") to configure the query window:

* **Quick presets** - 10 min, 1 hr, 5 hrs, 1 day, 3 days
* **Custom range** - Calendar-based date/time selection with From and To fields
* **Timezone** - Timezone selector for the displayed times

Click **Apply** to update the query or **Cancel** to dismiss.

## Refresh and Auto-Refresh

* **Refresh** - The circular arrow icon immediately re-queries the data
* **Auto-refresh** - Labeled "Off" by default. Click to select an interval: 10s, 30s, 1m, 5m, 10m, or 20m

## Save View

Click **Save view** to persist the current query configuration (filters, time range, sort order) as a named view. The dialog includes a required Title, optional Description, and an **Include time range** toggle.

## View Library

Click **Library** to open a side panel with three tabs:

* **Recent** - Views you recently accessed
* **My views** - Views you created
* **All views** - All views across the team

A search bar lets you find saved views by name. Click a view to restore its configuration.

## Summarize My Data

Click **Summarize my data** to trigger an AI-powered summary of the trace data within the current time window. You can select the AI model (e.g., gpt-4.1-mini) from a dropdown. The summary runs in the background through several stages: running the query, filtering irrelevant entries, and clustering similar patterns.

The resulting Summary Report includes:

* A narrative summary of the trace data
* Error/warning metric cards
* Detailed observations about patterns and anomalies
* Actionable recommendations
* A **Drilldown** section with pre-built SQL queries you can run directly in a new tab

See [AI Native](/docs/user-guide/ai-native) for more details.

## Field Browser

The left sidebar provides a hierarchical field browser for navigating and filtering on trace attributes. A **Search field names** text box at the top lets you quickly locate fields.

Fields are organized into collapsible semantic categories:

* **System** - Log formats, user agents, and source IPs
* **Error** - Fields related to error states
* **Service** - `service.name`, `service.namespace`, `service.version`, `service.instance.id`
* **Span** - Core span attributes: `span_name`, `span_kind`, `span_kind_description`, `span_status_code`, `span_status_description`, `span_duration_ns`, `span_trace_id`, `span_span_id`, `span_parent_span_id`, and timing fields
* **Kubernetes** - `k8s.namespace.name`, `k8s.node.name`, `k8s.pod.name`, `k8s.deployment.name`, `k8s.replicaset.name`
* **Container** - Container-level fields like `k8s.container.name`
* **HTTP** - `http.request.method`, `http.response.status_code`
* **Server** - Server address and port fields
* **Network** - `network.peer.address`, `network.peer.port`, `network.protocol.version`
* **Process** - `process.runtime.name`, `process.runtime.version`
* **Telemetry** - `telemetry.distro.name`, `telemetry.distro.version`, `telemetry.sdk.language`
* **URL** - `url.full`, `url.path`
* **All fields** - A flat listing of every field with data type indicators

Expanding a field reveals its top values with occurrence counts. Next to each value, include (funnel with +) and exclude (funnel with −) filter icons let you apply filters with one click. The sidebar can be collapsed using the toggle button.

## Traces View

The Traces view is the default exploration mode, consisting of a scatter chart and a trace list.

### Span Filter

A dropdown (default: "All spans") controls which spans are included:

* **All spans** - Shows all spans regardless of type
* **All root spans** - Shows only root spans (the top-level entry point of each trace)
* **Only error spans** - Filters to show only spans with an error status

### Sort Order

A dropdown (default: "Most recent") controls trace ordering:

* **Most recent** - Newest traces first
* **Longest first** - Highest duration traces at the top
* **Shortest first** - Lowest duration traces at the top
* **Most spans** - Traces with the highest span count first
* **Least spans** - Traces with the fewest spans first

### Lookup by Trace ID

A text input where you can paste a specific Trace ID to jump directly to that trace. This is useful when you have a trace ID from logs or another system and want to find it quickly.

### Add Filter

Click **Add filter** to open a searchable filter panel listing all available fields organized by category (Service, Span, Kubernetes, Container, HTTP, Network, Process, Telemetry, URL, All fields). Each field displays its top values with occurrence counts. Click a value to add it as a filter. A **Show more values** link appears when a field has additional values beyond those initially displayed.

### Edit with SQL

Click **Edit with SQL** to open the [SQL Editor](/docs/user-guide/sql-editor) in a new tab with a pre-populated query (e.g., `select * from "k8s-traces"`) based on the current dataset.

### Scatter Chart

The scatter chart visualizes traces as bubbles plotted with Time on the X-axis and Duration on the Y-axis. The size of each bubble corresponds to the number of spans in the trace. Bubble color indicates different services or error states (blue for normal, red/pink for errors).

Hovering over a bubble displays a tooltip showing the service name and operation, trace duration, and total span count.

### Trace List

Below the chart is a paginated list of traces. Each trace entry displays:

* **Service : Operation** - The service name and span operation (e.g., "inventory-manager : DB")
* **Trace ID** - The unique identifier, with a copy-to-clipboard button
* **Timestamp** - When the trace was recorded
* **Duration** - Total trace duration (e.g., "1.55 ms")
* **Span count** - Number of spans in the trace (e.g., "7 spans")

Click any trace to navigate to its detailed view.

### Pagination Controls

Below the trace list: previous/next page arrows, an entries-per-page selector (default: 10), and a record count (e.g., "Found 19K records"). Additional toolbar icons include **Share** (generates a shareable link) and **Maximize** (expands the trace list to full screen).

## Table View

Switching to the **Table** tab shows a flat, record-level view of individual spans.

* **Line Chart** - A time-series line chart showing span event counts over time. A **Forecast** toggle can be enabled to project future trends
* **Group By** - A dropdown that aggregates the chart data by any available field (e.g., `service.name`, `k8s.pod.name`, `http.response.status_code`), segmenting the line chart into multiple series
* **Data Table** - Columns include Ingestion Time (with timezone) and Data (a key-value display of all span fields). The sidebar shows Table fields (currently displayed columns) and Available fields (columns that can be added)
* **Toolbar** - Includes a **Find in data** search box and icons for Share, Maximize, Wrap Rows (toggles text wrapping), and a layout toggle

## Trace Detail View

Clicking a trace from the trace list navigates to the Trace Detail page. The breadcrumb updates to show: **Home > dataset name > trace ID > View**.

<img alt="Trace detail view with waterfall and span detail" src={__img1} placeholder="blur" />

### Header

Displays the **Start time**, **Duration**, and **Spans count** for the entire trace.

### Timeline Overview

A horizontal bar at the top provides a minimap of the full trace timeline, showing the overall duration span.

### Waterfall View

The main area is a waterfall (Gantt-chart) visualization showing all spans as horizontal bars:

* **Left column** - Span name with service name, organized in a hierarchical tree reflecting parent-child relationships
* **Horizontal bars** - Each bar's position and length represent the span's start time and duration relative to the trace start. The X-axis shows time markers
* **Colors** - Different colors distinguish different services or span types
* **Duration labels** - Appear on each bar

Spans can be expanded or collapsed using arrow icons, and a global **Expand all / Collapse all** toggle is available at the top of the span list.

### Span Detail Panel

Click any span in the waterfall to open a detail side panel showing:

* **Span name and ID** (with copy button)
* **Start time**, **Duration**, and **Span ID**
* A **Fields** tab with a searchable list of all span attributes organized by category (Service, Span, Kubernetes, Process, Telemetry, All fields)

Each field row has a three-dot action menu with three options:

* **Include in filter** - Adds this field value as an inclusion filter back on the explorer page
* **Exclude from filter** - Adds this field value as an exclusion filter
* **Copy key value pair** - Copies the field name and value to the clipboard

## Common Workflows

**Finding slow traces:** Set the sort order to "Longest first" to surface traces with the highest latency. Use the scatter chart to visually identify outlier bubbles at the top of the Y-axis.

**Investigating errors:** Use the span filter dropdown to select "Only error spans," then inspect the trace detail for spans with non-zero status codes.

**Filtering by service:** Click "Add filter," find the `service.name` field under the Service category, and click the desired service name to filter the trace list.

**Lookup by Trace ID:** Paste a known trace ID into the "Lookup by Trace ID" field to jump directly to a specific trace.

**Querying with SQL:** Click "Edit with SQL" to open the SQL editor with a pre-built query based on the current dataset. Modify the query to perform advanced aggregations or custom filtering.

**Generating an AI summary:** Click "Summarize my data" to generate an AI-powered analysis of the current trace data. The report provides an overview, highlights errors and anomalies, and includes drilldown queries you can execute directly.


# Ingest logs with headers (/docs/api/v1/ingest)



{/* This file was generated by Fumadocs. Do not edit this file directly. Any changes should be made by running the generation command again. */}

**Log Ingestion API via Custom Headers**\
This approach allows you to send logs to Parseable using custom headers to specify the target dataset.

Required headers:

* **X-P-Stream**: The name of the dataset to ingest logs into

The API accepts logs in JSON format. You can send single log entries or arrays of log entries.

Example:

```json
{
  "level": "info",
  "message": "User logged in",
  "timestamp": "2023-01-01T12:00:00Z",
  "user_id": "user123"
}
```

Or as an array:

```json
[
  {
    "level": "info",
    "message": "User logged in",
    "timestamp": "2023-01-01T12:00:00Z",
    "user_id": "user123"
  },
  {
    "level": "error",
    "message": "Failed to process request",
    "timestamp": "2023-01-01T12:01:00Z",
    "error_code": "ERR-1001"
  }
]
```

<APIPage document={"public/parseable-api-schema-cleaned.yaml"} operations={[{"path":"/api/v1/ingest","method":"post"}]} webhooks={[]} hasHead={false} />


# Query a log dataset (/docs/api/v1/query)



{/* This file was generated by Fumadocs. Do not edit this file directly. Any changes should be made by running the generation command again. */}

**Parseable Log Query API**\
This endpoint allows you to query logs using PostgreSQL syntax.

The query API accepts the following parameters:

* **query**: The SQL query to execute (required)
* **startTime**: The start time for the query range (optional)
* **endTime**: The end time for the query range (optional)
* **streamName**: The name of the log dataset to query (required)

Example request body:

```json
{
  "query": "SELECT * FROM log WHERE log ILIKE '%error%';",
  "startTime": "2023-01-01 00:00:00.000000",
  "endTime": "2023-01-01 23:59:59.999999",
  "streamName": "example-dataset"
}
```

<APIPage document={"public/parseable-api-schema-cleaned.yaml"} operations={[{"path":"/api/v1/query","method":"post"}]} webhooks={[]} hasHead={false} />


# AWS Data Firehose (/docs/cloud-provider/aws/aws-data-firehose)



### Introduction

Amazon Data Firehose is a fully managed service for delivering real-time streaming data to various destination.

* Firehose dataset: The underlying entity of Amazon Data Firehose. You use Amazon Data Firehose by creating a Firehose dataset and then sending data to it.
* Record: The data of interest that your data producer sends to a Firehose dataset. A record can be as large as 1,000 KB.
* Data producer: Producers send records to Firehose streams. For example, a web server that sends log data to a Firehose dataset is a data producer. You can also configure your Firehose dataset to automatically read data from an existing Kinesis data dataset, and load it into destinations.
* Buffer size and buffer interval: Amazon Data Firehose buffers incoming streaming data to a certain size or for a certain period of time before delivering it to destinations. Buffer Size is in MBs and Buffer Interval is in seconds.

### Overview

You can send data to Parseable using Amazon Data Firehose dataset, and Parseable will automatically ingest the data and make it available for you to query and analyze.

Once logs are unified in Parseable, you can easily monitor and analyze the logs in real-time, and get insights into the performance and usage of your APIs.

### Pre-requisites

* Parseable deployed and running in your environment. Refer the [installation guide](/docs/self-hosted/installation) for more information.
* AWS account with access to Amazon Data Firehose service.

### Create a Firehose dataset

First step is to create a Firehose dataset to ingest data from various sources and send it to Parseable. In the AWS Management Console, navigate to the Amazon Data Firehose service and click on `Create Firehose dataset`.

In the next screen, you can choose from various sources like Kinesis data dataset, Amazon MSK (Kafka), and Direct PUT (i.e. send data directly to Firehose dataset from an application).

### Destination settings

In the next step, you can configure the destination settings. Choose HTTP Endpoint as the destination. After that we'll need to provide the endpoint URL, Basic Auth token, and the Parseable dataset where you want to send the data.

For example to send events to the demo Parseable instance at `https://demo.parseable.com`:

* Endpoint URL will be `https://demo.parseable.com/api/v1/ingest`.

* Under Parameters, add the following:

  * Authorization header with the value `Basic YWRtaW46YWRtaW4=`.

  * Content-Type header with the value `application/json`.

  * X-P-Stream header with the value `kinesisdata`.

### Backup settings

To ensure that no data is lost, you can configure the backup settings. You can choose to deliver the data to an S3 bucket in case the data can't be delivered to Parseable.

That's it. You have successfully created a Firehose dataset to ingest data from various sources and send it to Parseable. Now you can start sending data to the Firehose dataset and you'll see the data in Parseable available for query and analysis.


# AWS (/docs/cloud-provider/aws/intro)



Amazon Web Services (AWS) is the leading cloud services provider, offering a wide range of services including compute, storage, databases, analytics, machine learning, and more. Parseable integrates with AWS to provide a seamless experience for our customers.

This document provides an overview of the AWS services that Parseable integrates with, and how to set up the integration.

### Authentication and access control

Parseable uses AWS IAM roles to authenticate and authorize access to AWS services. You can create an IAM role with the necessary permissions and attach it to the Parseable instance to enable access to AWS services.

### Deployment and configuration

Parseable can be deployed in AWS using the following methods:

* AWS EKS: Install Parseable in your EKS cluster using [this guide here](/docs/self-hosted/installation/standalone/aws-eks).
* AWS ECS: Install Parseable in your ECS cluster using [this guide here](/docs/self-hosted/installation/standalone/aws-ecs).
* AWS EC2: You can install Parseable on an EC2 (with an Ubuntu 22.04 LTS AMI) using the [standard Linux installation guide](/docs/self-hosted/installation/standalone/linux).

### Ingest logs and events from AWS services

Parseable can ingest logs and events from various AWS services, including:

* AWS Lambda: Parseable can ingest logs from AWS Lambda functions. You can use the Lambda function log ingestion guide to set up the integration.
* AWS Kinesis Firehose: Parseable can ingest logs from Kinesis Firehose. You can use the Kinesis Firehose log ingestion guide to set up the integration.
* AWS S3: Parseable can ingest logs from S3. You can use any log agent's S3 source to ingest logs from S3. For example Vector, FileBeat, etc.

[Request an integration](https://github.com/parseablehq/parseable/issues/new)


# AWS Lambda (/docs/cloud-provider/aws/lambda)



Parseable AWS Lambda extension is a Lambda extension that allows you to send logs from your Lambda functions to your Parseable instance.

## Usage

To use the parseable-lambda-extension with a lambda function, it must be configured as a layer. There are two variants of the extension available: one for x86\_64 architecture and one for arm64 architecture.

You can add the extension as a layer with the AWS CLI tool:

```bash
$ aws lambda update-code-configuration \
  --function-name MyAwesomeFunction
  --layers "<layer version ARN>"
```

The extension's layer version ARN follows the pattern below.

```bash
# Layer Version ARN Pattern
arn:aws:lambda:<AWS_REGION>:724973952305:layer:parseable-lambda-extension-<ARCH>-<VERSION>:1
```

* AWS\_REGION - This must match the region of the Lambda function to which you are adding the extension.

* ARCH - `x86_64` or `arm64`.

* VERSION - The version of the extension you want to use. Current version is v1.0. For current latest release `v1.0`, use the value `v1-0`.

## Configuration

The extension is configurable via environment variables set for your lambda function.

* `PARSEABLE_LOG_URL` - Parseable endpoint URL. It should be set to `https://<parseable-url>/api/v1/ingest`. Change `<parseable-url>` to your Parseable instance URL. (required)

* `PARSEABLE_USERNAME` - Username set for your Parseable instance. (required)

* `PARSEABLE_PASSWORD` - Password set for your Parseable instance. (required)

* `PARSEABLE_LOG_STREAM` - Parseable dataset name where you want to ingest logs. (default: `Lambda Function Name`).

Refer [Parseable installation documentation](/docs/self-hosted/installation/) for more details.

## Container image lambda

In case if you deploy your lambda as container image, to inject extension as part of your function just copy it to your image:

```bash
FROM parseable/aws-lambda-extension:latest AS parseable-extension
FROM public.ecr.aws/lambda/python:3.8
# Layer code
WORKDIR /opt
COPY --from=parseable-extension /opt/ .
# Function code
WORKDIR /var/task
COPY app.py .
CMD app.lambda_handler 
```


# Azure API Service (/docs/cloud-provider/azure/api-service)



## API Management Service Logs

Azure API Management (APIM) is a hybrid, multi cloud management platform for APIs across all environments. It provides a scalable, multi-cloud API management platform for securing, publishing, and analyzing APIs.

Azure API Management helps customers:

* Abstract backend architecture diversity and complexity from API consumers

* Securely expose services hosted on and outside of Azure as APIs

* Protect, accelerate, and observe APIs

* Enable API discovery and consumption by internal and external users

Azure API Management is made up of an API gateway, a management plane, and a developer portal. These components are Azure-hosted and fully managed by default.

## Overview

You can send Azure API Management Service logs to Parseable via Azure Event Hub & Azure Logic Apps. Once logs are unified in Parseable, you can easily monitor and analyze the logs in real-time, and get insights into the performance and usage of your APIs.

Most importantly, you have full ownership and control over this data, so you can use it to improve your API management and security, without cost or privacy concerns.

## Pre-requisites

Before you begin, you will need the following:

* Parseable deployed and running in your environment. Refer the [installation guide](/docs/self-hosted/installation/) for more information.

* Active Azure subscription with APIM service created. Refer the [Azure API Management documentation](https://learn.microsoft.com/en-us/azure/api-management/authentication-authorization-overview) for more information.

* Azure Event Hub created. Refer the [Create an event hub using Azure portal documentation](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-capture-enable-through-portal) for more information.

## Send Azure APIM Service Logs to Event Hub

* Navigate to the Azure API Management Service in the Azure portal.
* Click on the `Diagnostics settings` under the `Monitoring` section.
* Configure the APIM service to send logs to the Event Hub. Refer the image below for more information.

## Use Azure Logic Apps to send events to Parseable

* Navigate to the Azure Logic Apps in the Azure portal.
* Click on the `+ Add` button to create a new Logic App.
* Configure the Logic App to trigger when an event is received in the Event Hub. Refer the image below for more information. We have used the `When events are available in Event Hub` trigger to start the Logic App.

With this, you should now be able to see the APIM service logs in Parseable. You can now monitor and analyze the logs in real-time, and get insights into the performance and usage of your APIs. You have a detailed view of the API management and security, without cost or privacy concerns.


# Azure Service Bus (/docs/cloud-provider/azure/service-bus)



### Service Bus Messages

Azure Service Bus is a fully managed enterprise integration message broker. Service Bus is most commonly used to decouple applications and services from each other, and is a reliable and secure platform for asynchronous data and state transfer.

Service Bus is used to decouple applications and services from each other, providing the following benefits:

* Load-balancing work across competing workers

* Safely routing and transferring data and control across service and application boundaries

* Coordinating transactional work that requires a high-degree of reliability

### Overview

You can send messages published to Azure Service Bus Queue to Parseable [Azure Logic Apps](https://docs.microsoft.com/en-us/azure/logic-apps/logic-apps-overview) service.

We'll use the Azure Logic Apps trigger "When a message is received in a queue" to send message to Parseable.

### Prerequisites

Before you begin, you will need the following:

* Parseable deployed and running in your environment. Refer the [installation guide](/docs/self-hosted/installation/) for more information.

* Active Azure subscription with Service Bus namespace and queue created. Refer the [Azure Service Bus documentation](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview) for more information.

### Use Azure Logic Apps to send Service Bus messages to Parseable

* Navigate to the Azure Logic Apps in the Azure portal.

* Click on the `+ Add` button to create a new Logic App.

* Configure the Logic App to trigger when an message is available in the Message queue. Refer the image below for more information. We have used the `When a message is received in a queue` trigger to start the Logic App.


# Anthropic (/docs/ingest-data/ai-agents/anthropic)



Log Anthropic Claude API calls, responses, and token usage to Parseable for LLM observability.

## Overview

Integrate Anthropic with Parseable to:

* **API Logging** - Track all Claude API calls
* **Token Usage** - Monitor input/output tokens
* **Latency Tracking** - Measure response times
* **Error Analysis** - Debug failed requests
* **Model Comparison** - Compare Claude model performance

## Prerequisites

* Anthropic API key
* Parseable instance accessible
* Python application

## Python Integration

### Basic Logger

```python
import anthropic
import requests
import time
from datetime import datetime
from typing import Dict, Any, List

class AnthropicLogger:
    def __init__(self, parseable_url: str, dataset: str, username: str, password: str):
        self.parseable_url = parseable_url
        self.dataset = dataset
        self.auth = (username, password)
        self.client = anthropic.Anthropic()
    
    def _log(self, entry: Dict[str, Any]):
        try:
            requests.post(
                f"{self.parseable_url}/api/v1/ingest",
                json=[entry],
                auth=self.auth,
                headers={"X-P-Stream": self.dataset},
                timeout=5
            )
        except Exception as e:
            print(f"Logging failed: {e}")
    
    def message(
        self,
        messages: List[Dict],
        model: str = "claude-3-opus-20240229",
        max_tokens: int = 1024,
        system: str = None,
        **kwargs
    ) -> Any:
        start_time = datetime.utcnow()
        
        log_entry = {
            "timestamp": start_time.isoformat() + "Z",
            "provider": "anthropic",
            "type": "message",
            "model": model,
            "max_tokens": max_tokens,
            "message_count": len(messages),
            "has_system": system is not None,
            "user_prompt_preview": messages[-1]["content"][:200] if messages else None
        }
        
        try:
            response = self.client.messages.create(
                model=model,
                max_tokens=max_tokens,
                system=system,
                messages=messages,
                **kwargs
            )
            
            end_time = datetime.utcnow()
            log_entry.update({
                "success": True,
                "duration_ms": (end_time - start_time).total_seconds() * 1000,
                "input_tokens": response.usage.input_tokens,
                "output_tokens": response.usage.output_tokens,
                "total_tokens": response.usage.input_tokens + response.usage.output_tokens,
                "stop_reason": response.stop_reason,
                "response_preview": response.content[0].text[:200] if response.content else None
            })
            
            self._log(log_entry)
            return response
            
        except Exception as e:
            log_entry.update({
                "success": False,
                "error": str(e),
                "error_type": type(e).__name__
            })
            self._log(log_entry)
            raise

# Usage
logger = AnthropicLogger(
    parseable_url="http://parseable:8000",
    dataset="anthropic-logs",
    username="admin",
    password="admin"
)

response = logger.message(
    messages=[{"role": "user", "content": "Explain quantum computing in simple terms."}],
    model="claude-3-sonnet-20240229",
    system="You are a helpful science teacher."
)
```

### Streaming Support

```python
def message_stream(
    self,
    messages: List[Dict],
    model: str = "claude-3-opus-20240229",
    max_tokens: int = 1024,
    **kwargs
):
    start_time = datetime.utcnow()
    
    log_entry = {
        "timestamp": start_time.isoformat() + "Z",
        "provider": "anthropic",
        "type": "message_stream",
        "model": model,
        "max_tokens": max_tokens
    }
    
    try:
        with self.client.messages.dataset(
            model=model,
            max_tokens=max_tokens,
            messages=messages,
            **kwargs
        ) as dataset:
            full_response = ""
            for text in dataset.text_stream:
                full_response += text
                yield text
            
            # Get final message for usage stats
            final_message = dataset.get_final_message()
            
            log_entry.update({
                "success": True,
                "duration_ms": (datetime.utcnow() - start_time).total_seconds() * 1000,
                "input_tokens": final_message.usage.input_tokens,
                "output_tokens": final_message.usage.output_tokens,
                "response_length": len(full_response)
            })
            
    except Exception as e:
        log_entry.update({
            "success": False,
            "error": str(e)
        })
        raise
    finally:
        self._log(log_entry)
```

## Node.js Integration

```javascript
const Anthropic = require('@anthropic-ai/sdk');
const axios = require('axios');

class AnthropicLogger {
  constructor(parseableUrl, dataset, auth) {
    this.parseableUrl = parseableUrl;
    this.dataset = dataset;
    this.auth = auth;
    this.client = new Anthropic();
  }

  async log(entry) {
    try {
      await axios.post(`${this.parseableUrl}/api/v1/ingest`, [entry], {
        headers: {
          'Authorization': `Basic ${this.auth}`,
          'X-P-Stream': this.dataset
        }
      });
    } catch (error) {
      console.error('Logging failed:', error.message);
    }
  }

  async message(messages, options = {}) {
    const startTime = Date.now();
    const model = options.model || 'claude-3-sonnet-20240229';
    
    const logEntry = {
      timestamp: new Date().toISOString(),
      provider: 'anthropic',
      type: 'message',
      model,
      message_count: messages.length
    };

    try {
      const response = await this.client.messages.create({
        model,
        max_tokens: options.max_tokens || 1024,
        messages,
        ...options
      });

      logEntry.success = true;
      logEntry.duration_ms = Date.now() - startTime;
      logEntry.input_tokens = response.usage?.input_tokens;
      logEntry.output_tokens = response.usage?.output_tokens;
      logEntry.stop_reason = response.stop_reason;

      await this.log(logEntry);
      return response;

    } catch (error) {
      logEntry.success = false;
      logEntry.error = error.message;
      await this.log(logEntry);
      throw error;
    }
  }
}
```

## Querying Anthropic Logs

```sql
-- Token usage by model
SELECT 
  model,
  SUM(input_tokens) as total_input,
  SUM(output_tokens) as total_output,
  COUNT(*) as requests
FROM "anthropic-logs"
WHERE timestamp > NOW() - INTERVAL '7 days'
GROUP BY model
ORDER BY total_input + total_output DESC

-- Latency percentiles
SELECT 
  model,
  AVG(duration_ms) as avg_latency,
  PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY duration_ms) as p50,
  PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY duration_ms) as p95,
  PERCENTILE_CONT(0.99) WITHIN GROUP (ORDER BY duration_ms) as p99
FROM "anthropic-logs"
WHERE success = true
GROUP BY model

-- Error analysis
SELECT 
  error_type,
  error,
  COUNT(*) as count
FROM "anthropic-logs"
WHERE success = false
GROUP BY error_type, error
ORDER BY count DESC
```

## Best Practices

1. **Log Both Providers** - Compare OpenAI vs Anthropic
2. **Track Stop Reasons** - Monitor truncations
3. **Monitor Streaming** - Track streaming vs non-streaming
4. **Cost Tracking** - Calculate costs per model

## Next Steps

* Configure [OpenAI](/docs/ingest-data/ai-agents/openai) logging
* Set up [LangChain](/docs/ingest-data/ai-agents/langchain) tracing
* Create [dashboards](/docs/user-guide/dashboards) for LLM metrics


# AutoGen (/docs/ingest-data/ai-agents/autogen)



Log AutoGen multi-agent conversations, tool calls, and LLM interactions to Parseable.

## Overview

Integrate AutoGen with Parseable to:

* **Conversation Logging** - Track multi-agent conversations
* **Agent Monitoring** - Monitor individual agent behavior
* **Tool Usage** - Track function/tool calls
* **Token Tracking** - Aggregate token usage
* **Debug Workflows** - Trace complex agent interactions

## Prerequisites

* AutoGen installed (`pip install pyautogen`)
* Parseable instance accessible
* Python application

## Custom Logger

```python
import autogen
import requests
from datetime import datetime
from typing import Dict, Any, List, Optional
import uuid
import json

class ParseableAutogenLogger:
    def __init__(self, parseable_url: str, dataset: str, username: str, password: str):
        self.parseable_url = parseable_url
        self.dataset = dataset
        self.auth = (username, password)
        self.conversation_id = str(uuid.uuid4())
        self.message_count = 0
    
    def _log(self, entry: Dict[str, Any]):
        entry["timestamp"] = datetime.utcnow().isoformat() + "Z"
        entry["conversation_id"] = self.conversation_id
        try:
            requests.post(
                f"{self.parseable_url}/api/v1/ingest",
                json=[entry],
                auth=self.auth,
                headers={"X-P-Stream": self.dataset},
                timeout=5
            )
        except Exception as e:
            print(f"Logging failed: {e}")
    
    def log_message(self, sender: str, recipient: str, message: Dict[str, Any]):
        self.message_count += 1
        
        content = message.get("content", "")
        if isinstance(content, list):
            content = json.dumps(content)
        
        log_entry = {
            "event": "message",
            "message_number": self.message_count,
            "sender": sender,
            "recipient": recipient,
            "content_preview": str(content)[:500],
            "content_length": len(str(content)),
            "role": message.get("role", "unknown"),
            "has_function_call": "function_call" in message or "tool_calls" in message
        }
        
        # Log function calls
        if "function_call" in message:
            log_entry["function_name"] = message["function_call"].get("name")
            log_entry["function_args"] = message["function_call"].get("arguments", "")[:200]
        
        if "tool_calls" in message:
            log_entry["tool_calls"] = [
                {"name": tc.get("function", {}).get("name")}
                for tc in message.get("tool_calls", [])
            ]
        
        self._log(log_entry)
    
    def log_llm_call(self, agent_name: str, model: str, messages: List[Dict], response: Any):
        log_entry = {
            "event": "llm_call",
            "agent": agent_name,
            "model": model,
            "input_messages": len(messages)
        }
        
        if hasattr(response, "usage"):
            log_entry["prompt_tokens"] = response.usage.prompt_tokens
            log_entry["completion_tokens"] = response.usage.completion_tokens
            log_entry["total_tokens"] = response.usage.total_tokens
        
        self._log(log_entry)
    
    def log_function_execution(self, function_name: str, args: Dict, result: Any, duration_ms: float):
        self._log({
            "event": "function_execution",
            "function_name": function_name,
            "args": str(args)[:200],
            "result_preview": str(result)[:200],
            "duration_ms": duration_ms
        })
    
    def log_conversation_start(self, agents: List[str], task: str):
        self._log({
            "event": "conversation_start",
            "agents": agents,
            "task_preview": task[:500]
        })
    
    def log_conversation_end(self, summary: str, total_messages: int):
        self._log({
            "event": "conversation_end",
            "summary": summary[:500],
            "total_messages": total_messages
        })
    
    def new_conversation(self):
        self.conversation_id = str(uuid.uuid4())
        self.message_count = 0
```

### Wrapped Agent

```python
from autogen import AssistantAgent, UserProxyAgent
import time

class LoggedAssistantAgent(AssistantAgent):
    def __init__(self, logger: ParseableAutogenLogger, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logger
    
    def send(self, message, recipient, request_reply=None, silent=False):
        self.logger.log_message(self.name, recipient.name, message)
        return super().send(message, recipient, request_reply, silent)

class LoggedUserProxyAgent(UserProxyAgent):
    def __init__(self, logger: ParseableAutogenLogger, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logger
        self._original_execute = self.execute_function
    
    def send(self, message, recipient, request_reply=None, silent=False):
        self.logger.log_message(self.name, recipient.name, message)
        return super().send(message, recipient, request_reply, silent)
    
    def execute_function(self, func_call):
        start_time = time.time()
        result = self._original_execute(func_call)
        duration_ms = (time.time() - start_time) * 1000
        
        self.logger.log_function_execution(
            func_call.get("name", "unknown"),
            func_call.get("arguments", {}),
            result,
            duration_ms
        )
        return result
```

### Usage

```python
# Create logger
logger = ParseableAutogenLogger(
    parseable_url="http://parseable:8000",
    dataset="autogen-logs",
    username="admin",
    password="admin"
)

# Create logged agents
assistant = LoggedAssistantAgent(
    logger=logger,
    name="assistant",
    llm_config={"model": "gpt-4"}
)

user_proxy = LoggedUserProxyAgent(
    logger=logger,
    name="user_proxy",
    human_input_mode="NEVER",
    code_execution_config={"work_dir": "coding"}
)

# Log conversation start
logger.log_conversation_start(
    agents=["assistant", "user_proxy"],
    task="Write a Python function to calculate fibonacci numbers"
)

# Start conversation
user_proxy.initiate_chat(
    assistant,
    message="Write a Python function to calculate fibonacci numbers"
)

# Log conversation end
logger.log_conversation_end(
    summary="Completed fibonacci function",
    total_messages=logger.message_count
)
```

## Querying AutoGen Logs

```sql
-- Conversation overview
SELECT 
  conversation_id,
  MIN(timestamp) as started,
  MAX(timestamp) as ended,
  COUNT(*) as total_events,
  SUM(CASE WHEN event = 'message' THEN 1 ELSE 0 END) as messages
FROM "autogen-logs"
GROUP BY conversation_id
ORDER BY started DESC

-- Agent activity
SELECT 
  sender,
  COUNT(*) as messages_sent,
  AVG(content_length) as avg_content_length
FROM "autogen-logs"
WHERE event = 'message'
GROUP BY sender

-- Function usage
SELECT 
  function_name,
  COUNT(*) as calls,
  AVG(duration_ms) as avg_duration
FROM "autogen-logs"
WHERE event = 'function_execution'
GROUP BY function_name
ORDER BY calls DESC

-- Token usage per conversation
SELECT 
  conversation_id,
  SUM(total_tokens) as total_tokens,
  COUNT(CASE WHEN event = 'llm_call' THEN 1 END) as llm_calls
FROM "autogen-logs"
GROUP BY conversation_id
ORDER BY total_tokens DESC
```

## Best Practices

1. **Track Conversation IDs** - Correlate all events
2. **Log All Agents** - Monitor each agent's behavior
3. **Track Function Calls** - Monitor tool usage
4. **Truncate Content** - Don't log full messages

## Next Steps

* Configure [CrewAI](/docs/ingest-data/ai-agents/crewai) logging
* Set up [LangChain](/docs/ingest-data/ai-agents/langchain) tracing
* Create [dashboards](/docs/user-guide/dashboards) for agent metrics


# CrewAI (/docs/ingest-data/ai-agents/crewai)



Log CrewAI crews, agents, tasks, and tool usage to Parseable for multi-agent observability.

## Overview

Integrate CrewAI with Parseable to:

* **Crew Monitoring** - Track crew executions
* **Agent Logging** - Monitor individual agent work
* **Task Tracking** - Log task assignments and completions
* **Tool Usage** - Track tool calls and results
* **Performance Analysis** - Measure crew efficiency

## Prerequisites

* CrewAI installed (`pip install crewai`)
* Parseable instance accessible
* Python application

## Custom Logger

```python
from crewai import Agent, Task, Crew, Process
import requests
from datetime import datetime
from typing import Dict, Any, List, Optional
import uuid
import time
from functools import wraps

class ParseableCrewLogger:
    def __init__(self, parseable_url: str, dataset: str, username: str, password: str):
        self.parseable_url = parseable_url
        self.dataset = dataset
        self.auth = (username, password)
        self.crew_id = str(uuid.uuid4())
    
    def _log(self, entry: Dict[str, Any]):
        entry["timestamp"] = datetime.utcnow().isoformat() + "Z"
        entry["crew_id"] = self.crew_id
        try:
            requests.post(
                f"{self.parseable_url}/api/v1/ingest",
                json=[entry],
                auth=self.auth,
                headers={"X-P-Stream": self.dataset},
                timeout=5
            )
        except Exception as e:
            print(f"Logging failed: {e}")
    
    def log_crew_start(self, crew_name: str, agents: List[str], tasks: List[str]):
        self._log({
            "event": "crew_start",
            "crew_name": crew_name,
            "agents": agents,
            "tasks": tasks,
            "agent_count": len(agents),
            "task_count": len(tasks)
        })
    
    def log_crew_end(self, crew_name: str, result: str, duration_ms: float):
        self._log({
            "event": "crew_end",
            "crew_name": crew_name,
            "result_preview": str(result)[:500],
            "duration_ms": duration_ms
        })
    
    def log_task_start(self, task_description: str, agent_name: str):
        self._log({
            "event": "task_start",
            "task_description": task_description[:200],
            "assigned_agent": agent_name
        })
    
    def log_task_end(self, task_description: str, agent_name: str, output: str, duration_ms: float):
        self._log({
            "event": "task_end",
            "task_description": task_description[:200],
            "agent": agent_name,
            "output_preview": str(output)[:500],
            "duration_ms": duration_ms
        })
    
    def log_agent_action(self, agent_name: str, action: str, thought: str = None):
        self._log({
            "event": "agent_action",
            "agent": agent_name,
            "action": action[:200],
            "thought": thought[:200] if thought else None
        })
    
    def log_tool_use(self, agent_name: str, tool_name: str, input_data: str, output: str, duration_ms: float):
        self._log({
            "event": "tool_use",
            "agent": agent_name,
            "tool": tool_name,
            "input": str(input_data)[:200],
            "output": str(output)[:200],
            "duration_ms": duration_ms
        })
    
    def log_llm_call(self, agent_name: str, model: str, tokens: Dict[str, int] = None):
        entry = {
            "event": "llm_call",
            "agent": agent_name,
            "model": model
        }
        if tokens:
            entry.update(tokens)
        self._log(entry)
    
    def new_crew(self):
        self.crew_id = str(uuid.uuid4())
```

### Wrapped Crew

```python
class LoggedCrew:
    def __init__(self, crew: Crew, logger: ParseableCrewLogger):
        self.crew = crew
        self.logger = logger
    
    def kickoff(self, inputs: Dict = None):
        self.logger.new_crew()
        
        # Log crew start
        agent_names = [a.role for a in self.crew.agents]
        task_descriptions = [t.description[:100] for t in self.crew.tasks]
        
        self.logger.log_crew_start(
            crew_name=getattr(self.crew, 'name', 'unnamed_crew'),
            agents=agent_names,
            tasks=task_descriptions
        )
        
        start_time = time.time()
        
        try:
            result = self.crew.kickoff(inputs=inputs)
            
            duration_ms = (time.time() - start_time) * 1000
            self.logger.log_crew_end(
                crew_name=getattr(self.crew, 'name', 'unnamed_crew'),
                result=str(result),
                duration_ms=duration_ms
            )
            
            return result
            
        except Exception as e:
            self.logger._log({
                "event": "crew_error",
                "error": str(e),
                "error_type": type(e).__name__
            })
            raise
```

### Usage

```python
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

# Create logger
logger = ParseableCrewLogger(
    parseable_url="http://parseable:8000",
    dataset="crewai-logs",
    username="admin",
    password="admin"
)

# Define agents
researcher = Agent(
    role='Senior Research Analyst',
    goal='Uncover cutting-edge developments in AI',
    backstory='You are an expert researcher...',
    tools=[SerperDevTool()],
    verbose=True
)

writer = Agent(
    role='Tech Content Strategist',
    goal='Craft compelling content on tech advancements',
    backstory='You are a renowned content strategist...',
    verbose=True
)

# Define tasks
research_task = Task(
    description='Research the latest AI trends',
    expected_output='A comprehensive report on AI trends',
    agent=researcher
)

write_task = Task(
    description='Write a blog post about AI trends',
    expected_output='A 500-word blog post',
    agent=writer
)

# Create crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential
)

# Wrap with logger
logged_crew = LoggedCrew(crew, logger)

# Execute
result = logged_crew.kickoff(inputs={'topic': 'AI in 2024'})
```

## Callback-Based Logging

```python
from crewai.utilities.callbacks import CrewCallbackHandler

class ParseableCrewCallback(CrewCallbackHandler):
    def __init__(self, logger: ParseableCrewLogger):
        self.logger = logger
    
    def on_task_start(self, task):
        self.logger.log_task_start(
            task_description=task.description,
            agent_name=task.agent.role
        )
    
    def on_task_end(self, task, output):
        self.logger.log_task_end(
            task_description=task.description,
            agent_name=task.agent.role,
            output=str(output),
            duration_ms=0  # Calculate if needed
        )
    
    def on_tool_use(self, agent, tool, input_data, output):
        self.logger.log_tool_use(
            agent_name=agent.role,
            tool_name=tool.name,
            input_data=str(input_data),
            output=str(output),
            duration_ms=0
        )
```

## Querying CrewAI Logs

```sql
-- Crew execution summary
SELECT 
  crew_id,
  crew_name,
  agent_count,
  task_count,
  duration_ms / 1000 as duration_seconds
FROM "crewai-logs"
WHERE event = 'crew_end'
ORDER BY timestamp DESC

-- Task performance by agent
SELECT 
  agent,
  COUNT(*) as tasks_completed,
  AVG(duration_ms) as avg_duration_ms
FROM "crewai-logs"
WHERE event = 'task_end'
GROUP BY agent
ORDER BY tasks_completed DESC

-- Tool usage analysis
SELECT 
  tool,
  agent,
  COUNT(*) as usage_count,
  AVG(duration_ms) as avg_duration
FROM "crewai-logs"
WHERE event = 'tool_use'
GROUP BY tool, agent
ORDER BY usage_count DESC

-- Error tracking
SELECT 
  timestamp,
  crew_id,
  error_type,
  error
FROM "crewai-logs"
WHERE event = 'crew_error'
ORDER BY timestamp DESC
```

## Best Practices

1. **Track Crew IDs** - Correlate all events in a crew run
2. **Log All Tasks** - Monitor task assignments and completions
3. **Monitor Tools** - Track tool usage and performance
4. **Measure Duration** - Track time spent on each task

## Next Steps

* Configure [AutoGen](/docs/ingest-data/ai-agents/autogen) logging
* Set up [LangChain](/docs/ingest-data/ai-agents/langchain) tracing
* Create [dashboards](/docs/user-guide/dashboards) for crew metrics


# DSPy (/docs/ingest-data/ai-agents/dspy)



Log DSPy programs, module executions, and optimization runs to Parseable.

## Overview

Integrate DSPy with Parseable to:

* **Program Tracing** - Track DSPy program executions
* **Module Monitoring** - Log individual module calls
* **Optimization Tracking** - Monitor optimization progress
* **Token Usage** - Track LLM token consumption

## Prerequisites

* DSPy installed (`pip install dspy-ai`)
* Parseable instance accessible
* Python application

## Custom Logger

```python
import dspy
import requests
from datetime import datetime
from typing import Dict, Any
import uuid
import time

class ParseableDSPyLogger:
    def __init__(self, parseable_url: str, dataset: str, username: str, password: str):
        self.parseable_url = parseable_url
        self.dataset = dataset
        self.auth = (username, password)
        self.program_id = str(uuid.uuid4())
    
    def _log(self, entry: Dict[str, Any]):
        entry["timestamp"] = datetime.utcnow().isoformat() + "Z"
        entry["program_id"] = self.program_id
        try:
            requests.post(
                f"{self.parseable_url}/api/v1/ingest",
                json=[entry],
                auth=self.auth,
                headers={"X-P-Stream": self.dataset},
                timeout=5
            )
        except Exception as e:
            print(f"Logging failed: {e}")
    
    def log_module_call(self, module_name: str, inputs: Dict, outputs: Dict, duration_ms: float):
        self._log({
            "event": "module_call",
            "module_name": module_name,
            "inputs": {k: str(v)[:100] for k, v in inputs.items()},
            "outputs": {k: str(v)[:200] for k, v in outputs.items()},
            "duration_ms": duration_ms
        })
    
    def log_optimization_trial(self, trial_num: int, score: float):
        self._log({
            "event": "optimization_trial",
            "trial_num": trial_num,
            "score": score
        })
```

## Querying DSPy Logs

```sql
-- Module performance
SELECT module_name, AVG(duration_ms) as avg_duration, COUNT(*) as calls
FROM "dspy-logs"
WHERE event = 'module_call'
GROUP BY module_name

-- Optimization progress
SELECT trial_num, score
FROM "dspy-logs"
WHERE event = 'optimization_trial'
ORDER BY trial_num
```

## Next Steps

* Configure [LangChain](/docs/ingest-data/ai-agents/langchain) tracing
* Set up [OpenAI](/docs/ingest-data/ai-agents/openai) direct logging


# LLM Observability (/docs/ingest-data/ai-agents)



import { IconBrandOpenai, IconRobot, IconLink, IconBook, IconUsers, IconBrain, IconCode, IconSettingsAutomation, IconServer, IconApi, IconRoute } from '@tabler/icons-react';

Monitor, debug, and optimize your LLM applications with Parseable. Track API calls, token usage, latency, and errors across all major LLM providers and frameworks.

## Why LLM Observability?

LLM applications present unique observability challenges:

* **Non-deterministic outputs** - Same input can produce different results
* **High costs** - Token usage directly impacts costs
* **Latency sensitivity** - Response times affect user experience
* **Complex chains** - Multi-step workflows are hard to debug
* **Prompt engineering** - Need visibility into prompt effectiveness

## Supported Integrations

<Cards>
  <Card title="OpenAI" href="/docs/ingest-data/ai-agents/openai" icon={<IconBrandOpenai />}>
    GPT-4, GPT-3.5, and other OpenAI models
  </Card>

  <Card title="Anthropic" href="/docs/ingest-data/ai-agents/anthropic" icon={<IconRobot />}>
    Claude and Claude Instant models
  </Card>

  <Card title="LiteLLM" href="/docs/ingest-data/ai-agents/litellm" icon={<IconApi />}>
    Unified API gateway for 100+ LLM providers
  </Card>

  <Card title="OpenRouter" href="/docs/ingest-data/ai-agents/openrouter" icon={<IconRoute />}>
    Zero-code LLM observability via Broadcast
  </Card>

  <Card title="vLLM" href="/docs/ingest-data/ai-agents/vllm" icon={<IconServer />}>
    High-performance LLM inference serving
  </Card>

  <Card title="LangChain" href="/docs/ingest-data/ai-agents/langchain" icon={<IconLink />}>
    LangChain framework integration
  </Card>

  <Card title="LlamaIndex" href="/docs/ingest-data/ai-agents/llamaindex" icon={<IconBook />}>
    LlamaIndex RAG applications
  </Card>

  <Card title="AutoGen" href="/docs/ingest-data/ai-agents/autogen" icon={<IconUsers />}>
    Microsoft AutoGen multi-agent systems
  </Card>

  <Card title="CrewAI" href="/docs/ingest-data/ai-agents/crewai" icon={<IconBrain />}>
    CrewAI agent orchestration
  </Card>

  <Card title="DSPy" href="/docs/ingest-data/ai-agents/dspy" icon={<IconCode />}>
    DSPy programmatic prompting
  </Card>

  <Card title="n8n" href="/docs/ingest-data/ai-agents/n8n" icon={<IconSettingsAutomation />}>
    n8n workflow automation
  </Card>
</Cards>

## What to Monitor

### API Calls & Responses

Track every interaction with LLM providers:

* Request parameters (model, temperature, max\_tokens)
* Full prompts and completions
* Response metadata and finish reasons

### Token Usage & Costs

Monitor consumption to control costs:

* Input and output tokens per request
* Cost calculations by model
* Usage trends over time

### Latency & Performance

Measure response times:

* Time to first token (TTFT)
* Total response time
* Streaming vs non-streaming performance

### Errors & Failures

Debug issues quickly:

* Rate limit errors
* API failures and retries
* Timeout tracking

## Guides & Cookbooks

<Cards>
  <Card title="Agentic Observability" href="/docs/cookbook/agentic-observability" icon={<IconRobot />}>
    End-to-end guide for monitoring AI agents
  </Card>

  <Card title="Tool Calls Monitoring" href="/docs/cookbook/tool-calls" icon={<IconCode />}>
    Track and debug LLM tool/function calls
  </Card>

  <Card title="Instrumentation Guide" href="/docs/cookbook/instrumentation" icon={<IconSettingsAutomation />}>
    Add observability to your LLM applications
  </Card>
</Cards>


# LangChain (/docs/ingest-data/ai-agents/langchain)



Trace LangChain chains, agents, and tool calls with Parseable for comprehensive LLM observability.

## Overview

Integrate LangChain with Parseable to:

* **Chain Tracing** - Track entire chain executions
* **Agent Monitoring** - Monitor agent decisions and tool usage
* **Token Tracking** - Aggregate token usage across chains
* **Latency Analysis** - Identify slow components
* **Error Debugging** - Trace failures through chains

## Prerequisites

* LangChain installed
* Parseable instance accessible
* Python application

## Custom Callback Handler

### Basic Handler

```python
from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import LLMResult
import requests
from datetime import datetime
from typing import Dict, Any, List, Optional
import uuid

class ParseableCallbackHandler(BaseCallbackHandler):
    def __init__(self, parseable_url: str, dataset: str, username: str, password: str):
        self.parseable_url = parseable_url
        self.dataset = dataset
        self.auth = (username, password)
        self.run_id = str(uuid.uuid4())
        self.chain_stack = []
    
    def _log(self, entry: Dict[str, Any]):
        entry["run_id"] = self.run_id
        entry["timestamp"] = datetime.utcnow().isoformat() + "Z"
        try:
            requests.post(
                f"{self.parseable_url}/api/v1/ingest",
                json=[entry],
                auth=self.auth,
                headers={"X-P-Stream": self.dataset},
                timeout=5
            )
        except Exception as e:
            print(f"Logging failed: {e}")
    
    def on_chain_start(self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs):
        chain_id = str(uuid.uuid4())
        self.chain_stack.append({
            "chain_id": chain_id,
            "start_time": datetime.utcnow(),
            "name": serialized.get("name", "unknown")
        })
        
        self._log({
            "event": "chain_start",
            "chain_id": chain_id,
            "chain_name": serialized.get("name"),
            "inputs": str(inputs)[:500]
        })
    
    def on_chain_end(self, outputs: Dict[str, Any], **kwargs):
        if self.chain_stack:
            chain = self.chain_stack.pop()
            duration = (datetime.utcnow() - chain["start_time"]).total_seconds() * 1000
            
            self._log({
                "event": "chain_end",
                "chain_id": chain["chain_id"],
                "chain_name": chain["name"],
                "duration_ms": duration,
                "outputs": str(outputs)[:500]
            })
    
    def on_chain_error(self, error: Exception, **kwargs):
        if self.chain_stack:
            chain = self.chain_stack.pop()
            
            self._log({
                "event": "chain_error",
                "chain_id": chain["chain_id"],
                "chain_name": chain["name"],
                "error": str(error),
                "error_type": type(error).__name__
            })
    
    def on_llm_start(self, serialized: Dict[str, Any], prompts: List[str], **kwargs):
        self._log({
            "event": "llm_start",
            "model": serialized.get("name", "unknown"),
            "prompt_count": len(prompts),
            "prompt_preview": prompts[0][:200] if prompts else None
        })
    
    def on_llm_end(self, response: LLMResult, **kwargs):
        usage = {}
        if response.llm_output:
            token_usage = response.llm_output.get("token_usage", {})
            usage = {
                "prompt_tokens": token_usage.get("prompt_tokens"),
                "completion_tokens": token_usage.get("completion_tokens"),
                "total_tokens": token_usage.get("total_tokens")
            }
        
        self._log({
            "event": "llm_end",
            "generations": len(response.generations),
            **usage
        })
    
    def on_llm_error(self, error: Exception, **kwargs):
        self._log({
            "event": "llm_error",
            "error": str(error),
            "error_type": type(error).__name__
        })
    
    def on_tool_start(self, serialized: Dict[str, Any], input_str: str, **kwargs):
        self._log({
            "event": "tool_start",
            "tool_name": serialized.get("name", "unknown"),
            "input": input_str[:500]
        })
    
    def on_tool_end(self, output: str, **kwargs):
        self._log({
            "event": "tool_end",
            "output": output[:500]
        })
    
    def on_tool_error(self, error: Exception, **kwargs):
        self._log({
            "event": "tool_error",
            "error": str(error),
            "error_type": type(error).__name__
        })
    
    def on_agent_action(self, action, **kwargs):
        self._log({
            "event": "agent_action",
            "tool": action.tool,
            "tool_input": str(action.tool_input)[:500],
            "log": action.log[:500]
        })
    
    def on_agent_finish(self, finish, **kwargs):
        self._log({
            "event": "agent_finish",
            "output": str(finish.return_values)[:500]
        })
```

### Usage with Chains

```python
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Create handler
handler = ParseableCallbackHandler(
    parseable_url="http://parseable:8000",
    dataset="langchain-traces",
    username="admin",
    password="admin"
)

# Create chain with callback
llm = ChatOpenAI(model="gpt-4", callbacks=[handler])
prompt = PromptTemplate.from_template("Tell me about {topic}")
chain = LLMChain(llm=llm, prompt=prompt, callbacks=[handler])

# Run chain
result = chain.run(topic="machine learning")
```

### Usage with Agents

```python
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.chat_models import ChatOpenAI

# Define tools
tools = [
    Tool(
        name="Calculator",
        func=lambda x: eval(x),
        description="Useful for math calculations"
    )
]

# Create agent with callback
llm = ChatOpenAI(model="gpt-4")
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    callbacks=[handler],
    verbose=True
)

# Run agent
result = agent.run("What is 25 * 4 + 10?")
```

## LCEL Integration

```python
from langchain_core.runnables import RunnableConfig

# Create config with callbacks
config = RunnableConfig(callbacks=[handler])

# Use with LCEL chains
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_template("Tell me about {topic}")
model = ChatOpenAI()
chain = prompt | model

# Invoke with config
result = chain.invoke({"topic": "AI"}, config=config)
```

## Querying LangChain Traces

```sql
-- Chain execution times
SELECT 
  chain_name,
  AVG(duration_ms) as avg_duration,
  COUNT(*) as executions
FROM "langchain-traces"
WHERE event = 'chain_end'
GROUP BY chain_name
ORDER BY avg_duration DESC

-- Token usage by run
SELECT 
  run_id,
  SUM(total_tokens) as total_tokens,
  COUNT(CASE WHEN event = 'tool_start' THEN 1 END) as tool_calls
FROM "langchain-traces"
GROUP BY run_id
ORDER BY total_tokens DESC

-- Agent tool usage
SELECT 
  tool,
  COUNT(*) as usage_count
FROM "langchain-traces"
WHERE event = 'agent_action'
GROUP BY tool
ORDER BY usage_count DESC

-- Error analysis
SELECT 
  event,
  error_type,
  error,
  COUNT(*) as count
FROM "langchain-traces"
WHERE event LIKE '%error%'
GROUP BY event, error_type, error
ORDER BY count DESC
```

## Best Practices

1. **Use Run IDs** - Correlate events in a single execution
2. **Truncate Content** - Don't log full prompts/responses
3. **Track All Events** - Log starts, ends, and errors
4. **Monitor Agents** - Pay attention to tool usage patterns

## Next Steps

* Configure [LlamaIndex](/docs/ingest-data/ai-agents/llamaindex) tracing
* Set up [OpenAI](/docs/ingest-data/ai-agents/openai) direct logging
* Create [dashboards](/docs/user-guide/dashboards) for chain metrics


# LiteLLM (/docs/ingest-data/ai-agents/litellm)



Send LiteLLM traces to Parseable through OpenTelemetry for complete LLM observability with SQL-queryable analytics.

## Overview

[LiteLLM](https://litellm.ai) is an open-source LLM gateway that provides a unified API for 100+ LLM providers. It acts as a proxy between your application and LLM APIs like OpenAI, Anthropic, Azure, Bedrock, and self-hosted models.

Integrate LiteLLM with Parseable to:

* **Track All LLM Calls** - Monitor requests across multiple providers
* **Analyze Latency** - Identify slow models and optimize routing
* **Monitor Token Usage** - Track consumption and estimate costs
* **Debug Errors** - Investigate failed requests with full context

## Architecture

```
LiteLLM → OpenTelemetry Collector → Parseable
                /v1/traces
```

## Prerequisites

* Python 3.8+
* LiteLLM installed
* OpenTelemetry Collector
* Parseable instance

## Step 1: Install Dependencies

```bash
pip install litellm opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp
```

## Step 2: Configure OpenTelemetry Collector

Create `otel-collector-config.yaml`:

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

processors:
  batch:
    timeout: 5s
    send_batch_size: 100

exporters:
  otlphttp:
    endpoint: http://localhost:8000
    headers:
      Authorization: Basic YWRtaW46YWRtaW4=
      X-P-Stream: litellm-traces
      X-P-Log-Source: otel-traces
    tls:
      insecure: true

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlphttp]
```

| Setting                       | Description                                      |
| ----------------------------- | ------------------------------------------------ |
| `receivers.otlp`              | Accepts OTLP data on gRPC (4317) and HTTP (4318) |
| `processors.batch`            | Batches spans before export for efficiency       |
| `exporters.otlphttp.endpoint` | Parseable server URL                             |
| `X-P-Stream`                  | Target dataset in Parseable                      |
| `X-P-Log-Source`              | Must be `otel-traces` for trace data             |

Start the collector:

```bash
./otelcol --config ./otel-collector-config.yaml
```

## Step 3: Configure LiteLLM

Set environment variables:

```bash
export OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:4318"
export OTEL_EXPORTER_OTLP_PROTOCOL="http/json"
```

Enable the OTEL callback in your Python code:

```python
import litellm
from litellm import completion

# Enable OpenTelemetry tracing
litellm.callbacks = ["otel"]

# Make an LLM call
response = completion(
    model="gpt-4",
    messages=[{"role": "user", "content": "What is observability?"}]
)

print(response.choices[0].message.content)
```

Every LLM call now emits a trace to Parseable.

## Step 4: LiteLLM Proxy (Optional)

If running LiteLLM as a proxy server, configure `litellm_config.yaml`:

```yaml
model_list:
  - model_name: gpt-4
    litellm_params:
      model: openai/gpt-4
      api_key: sk-...

litellm_settings:
  callbacks: ["otel"]

environment_variables:
  OTEL_EXPORTER_OTLP_ENDPOINT: "http://localhost:4318"
  OTEL_EXPORTER_OTLP_PROTOCOL: "http/json"
```

Start the proxy:

```bash
litellm --config litellm_config.yaml
```

## Trace Schema

LiteLLM traces include rich metadata:

| Field                | Description                                 |
| -------------------- | ------------------------------------------- |
| `trace_id`           | Unique trace identifier                     |
| `span_id`            | Unique span identifier                      |
| `span_name`          | Operation name (e.g., `litellm.completion`) |
| `span_duration_ms`   | Span duration in milliseconds               |
| `span_model`         | Model used (e.g., `gpt-4`, `claude-3-opus`) |
| `span_input_tokens`  | Input token count                           |
| `span_output_tokens` | Output token count                          |
| `span_total_tokens`  | Total tokens used                           |
| `span_status_code`   | HTTP status or error code                   |

## Example Queries

### Average Latency by Model

```sql
SELECT 
  "span_model" AS model,
  AVG("span_duration_ms") AS avg_latency_ms,
  COUNT(*) AS call_count
FROM "litellm-traces"
WHERE "span_name" LIKE '%completion%'
GROUP BY model
ORDER BY avg_latency_ms DESC;
```

### Token Usage Over Time

```sql
SELECT 
  DATE_TRUNC('hour', p_timestamp) AS hour,
  SUM("span_input_tokens") AS input_tokens,
  SUM("span_output_tokens") AS output_tokens,
  SUM("span_total_tokens") AS total_tokens
FROM "litellm-traces"
GROUP BY hour
ORDER BY hour;
```

### Slowest Requests

```sql
SELECT 
  trace_id,
  "span_model",
  "span_duration_ms",
  "span_total_tokens",
  p_timestamp
FROM "litellm-traces"
ORDER BY "span_duration_ms" DESC
LIMIT 20;
```

### Error Rate by Model

```sql
SELECT 
  "span_model" AS model,
  COUNT(*) AS total_calls,
  SUM(CASE WHEN "span_status_code" >= 400 THEN 1 ELSE 0 END) AS errors,
  ROUND(100.0 * SUM(CASE WHEN "span_status_code" >= 400 THEN 1 ELSE 0 END) / COUNT(*), 2) AS error_rate
FROM "litellm-traces"
GROUP BY model
ORDER BY error_rate DESC;
```

## Cost Tracking

Calculate costs with token counts:

```sql
SELECT 
  "span_model" AS model,
  SUM("span_input_tokens") AS input_tokens,
  SUM("span_output_tokens") AS output_tokens,
  -- GPT-4 pricing: $0.03/1K input, $0.06/1K output
  ROUND(SUM("span_input_tokens") * 0.00003 + SUM("span_output_tokens") * 0.00006, 2) AS estimated_cost_usd
FROM "litellm-traces"
WHERE "span_model" = 'gpt-4'
  AND p_timestamp >= NOW() - INTERVAL '24 hours'
GROUP BY model;
```

## Alerting

### High Latency Alert

Create an alert in Parseable:

* **Stream**: `litellm-traces`
* **Column**: `span_duration_ms`
* **Aggregation**: `AVG`
* **Threshold**: `> 5000`

### Token Spike Detection

Use anomaly detection on:

* **Stream**: `litellm-traces`
* **Column**: `span_total_tokens`
* **Aggregation**: `SUM`

## Privacy: Redacting Prompts

LiteLLM can redact sensitive content from traces:

**Redact all messages globally:**

```python
litellm.turn_off_message_logging = True
```

**Redact per-request:**

```python
response = completion(
    model="gpt-4",
    messages=[{"role": "user", "content": "Sensitive prompt"}],
    metadata={
        "mask_input": True,
        "mask_output": True
    }
)
```

This keeps request metadata (model, tokens, latency) while hiding the actual content.

## Resources

* [LiteLLM Documentation](https://docs.litellm.ai/)
* [Blog Post](/blog/litellm-trace-analysis-parseable)


# LlamaIndex (/docs/ingest-data/ai-agents/llamaindex)



Trace LlamaIndex queries, retrievals, and LLM calls with Parseable for RAG observability.

## Overview

Integrate LlamaIndex with Parseable to:

* **Query Tracing** - Track query engine executions
* **Retrieval Monitoring** - Monitor document retrieval
* **LLM Tracking** - Log LLM calls and token usage
* **Index Operations** - Track indexing and embedding
* **RAG Debugging** - Debug retrieval-augmented generation

## Prerequisites

* LlamaIndex installed
* Parseable instance accessible
* Python application

## Custom Callback Handler

```python
from llama_index.core.callbacks import CallbackManager, CBEventType
from llama_index.core.callbacks.base_handler import BaseCallbackHandler
import requests
from datetime import datetime
from typing import Dict, Any, List, Optional
import uuid

class ParseableCallbackHandler(BaseCallbackHandler):
    def __init__(self, parseable_url: str, dataset: str, username: str, password: str):
        self.parseable_url = parseable_url
        self.dataset = dataset
        self.auth = (username, password)
        self.event_starts = {}
        super().__init__(
            event_starts_to_ignore=[],
            event_ends_to_ignore=[]
        )
    
    def _log(self, entry: Dict[str, Any]):
        entry["timestamp"] = datetime.utcnow().isoformat() + "Z"
        try:
            requests.post(
                f"{self.parseable_url}/api/v1/ingest",
                json=[entry],
                auth=self.auth,
                headers={"X-P-Stream": self.dataset},
                timeout=5
            )
        except Exception as e:
            print(f"Logging failed: {e}")
    
    def on_event_start(
        self,
        event_type: CBEventType,
        payload: Optional[Dict[str, Any]] = None,
        event_id: str = "",
        parent_id: str = "",
        **kwargs
    ) -> str:
        self.event_starts[event_id] = datetime.utcnow()
        
        log_entry = {
            "event": "start",
            "event_type": event_type.value,
            "event_id": event_id,
            "parent_id": parent_id
        }
        
        if payload:
            if event_type == CBEventType.QUERY:
                log_entry["query"] = str(payload.get("query_str", ""))[:500]
            elif event_type == CBEventType.RETRIEVE:
                log_entry["query"] = str(payload.get("query_str", ""))[:500]
            elif event_type == CBEventType.LLM:
                messages = payload.get("messages", [])
                log_entry["message_count"] = len(messages)
                log_entry["model"] = payload.get("model_name", "unknown")
            elif event_type == CBEventType.EMBEDDING:
                log_entry["chunk_count"] = len(payload.get("chunks", []))
        
        self._log(log_entry)
        return event_id
    
    def on_event_end(
        self,
        event_type: CBEventType,
        payload: Optional[Dict[str, Any]] = None,
        event_id: str = "",
        **kwargs
    ) -> None:
        start_time = self.event_starts.pop(event_id, None)
        duration_ms = None
        if start_time:
            duration_ms = (datetime.utcnow() - start_time).total_seconds() * 1000
        
        log_entry = {
            "event": "end",
            "event_type": event_type.value,
            "event_id": event_id,
            "duration_ms": duration_ms
        }
        
        if payload:
            if event_type == CBEventType.QUERY:
                response = payload.get("response")
                if response:
                    log_entry["response_preview"] = str(response)[:500]
            elif event_type == CBEventType.RETRIEVE:
                nodes = payload.get("nodes", [])
                log_entry["nodes_retrieved"] = len(nodes)
                log_entry["scores"] = [n.score for n in nodes[:5]] if nodes else []
            elif event_type == CBEventType.LLM:
                response = payload.get("response")
                if response:
                    log_entry["response_preview"] = str(response)[:200]
                    # Token usage if available
                    if hasattr(response, "raw"):
                        usage = getattr(response.raw, "usage", None)
                        if usage:
                            log_entry["prompt_tokens"] = usage.prompt_tokens
                            log_entry["completion_tokens"] = usage.completion_tokens
            elif event_type == CBEventType.EMBEDDING:
                log_entry["embeddings_created"] = len(payload.get("embeddings", []))
        
        self._log(log_entry)
    
    def start_trace(self, trace_id: Optional[str] = None) -> None:
        self.trace_id = trace_id or str(uuid.uuid4())
    
    def end_trace(
        self,
        trace_id: Optional[str] = None,
        trace_map: Optional[Dict[str, List[str]]] = None
    ) -> None:
        pass
```

### Usage

```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.callbacks import CallbackManager

# Create handler
handler = ParseableCallbackHandler(
    parseable_url="http://parseable:8000",
    dataset="llamaindex-traces",
    username="admin",
    password="admin"
)

# Create callback manager
callback_manager = CallbackManager([handler])

# Load documents
documents = SimpleDirectoryReader("data").load_data()

# Create index with callbacks
index = VectorStoreIndex.from_documents(
    documents,
    callback_manager=callback_manager
)

# Query with callbacks
query_engine = index.as_query_engine(callback_manager=callback_manager)
response = query_engine.query("What is the main topic?")
```

## Global Handler Setup

```python
from llama_index.core import Settings

# Set global callback manager
Settings.callback_manager = CallbackManager([handler])

# All LlamaIndex operations will now be traced
```

## Querying LlamaIndex Traces

```sql
-- Query performance
SELECT 
  event_id,
  duration_ms,
  nodes_retrieved,
  response_preview
FROM "llamaindex-traces"
WHERE event_type = 'query' AND event = 'end'
ORDER BY timestamp DESC
LIMIT 50

-- Retrieval quality
SELECT 
  AVG(nodes_retrieved) as avg_nodes,
  AVG(scores[1]) as avg_top_score
FROM "llamaindex-traces"
WHERE event_type = 'retrieve' AND event = 'end'

-- LLM token usage
SELECT 
  model,
  SUM(prompt_tokens) as total_prompt,
  SUM(completion_tokens) as total_completion,
  COUNT(*) as calls
FROM "llamaindex-traces"
WHERE event_type = 'llm' AND event = 'end'
GROUP BY model

-- Embedding operations
SELECT 
  DATE_TRUNC('hour', timestamp) as hour,
  SUM(embeddings_created) as embeddings,
  COUNT(*) as operations
FROM "llamaindex-traces"
WHERE event_type = 'embedding' AND event = 'end'
GROUP BY hour
ORDER BY hour DESC
```

## Best Practices

1. **Track All Events** - Monitor queries, retrievals, and LLM calls
2. **Log Retrieval Scores** - Analyze retrieval quality
3. **Monitor Token Usage** - Track costs across operations
4. **Use Parent IDs** - Correlate nested events

## Next Steps

* Configure [LangChain](/docs/ingest-data/ai-agents/langchain) tracing
* Set up [OpenAI](/docs/ingest-data/ai-agents/openai) direct logging
* Create [dashboards](/docs/user-guide/dashboards) for RAG metrics


# n8n (/docs/ingest-data/ai-agents/n8n)



Set up end-to-end observability for n8n workflow automation with Parseable using OpenTelemetry.

## Overview

Integrate n8n with Parseable to:

* **Workflow Tracing** - Track every workflow and node execution
* **Performance Metrics** - Monitor durations, error rates, and token usage
* **Structured Logging** - Capture logs with Winston + OpenTelemetry
* **AI Agent Debugging** - Debug non-deterministic agentic workflows
* **Unified Observability** - Single OTLP pipeline for logs, traces, and metrics

## Architecture

```
┌───────────┐    ┌───────────────────────┐    ┌──────────────────────┐
│   n8n     │───▶│ OpenTelemetry (OTLP)  │───▶│ Parseable (Datasets) │
│           │    │ - Traces              │    │ - otel-traces        │
│ Workflows │    │ - Metrics             │    │ - otel-metrics       │
│ Nodes     │    │ - Logs (Winston)      │    │ - otel-logs          │
└───────────┘    └───────────────────────┘    └──────────────────────┘
```

## Prerequisites

* Docker and Docker Compose
* n8n instance
* Parseable instance

## Quick Start

Clone the observability repository and start the stack:

```bash
git clone https://github.com/parseablehq/n8n-observability.git
cd n8n-observability
cp .env.example .env
# Edit .env with your passwords
docker-compose up -d
```

Access the applications:

* **n8n**: `http://localhost:5678` (admin/admin)
* **Parseable**: `http://localhost:8000` (admin/admin)

## Docker Compose Setup

### Environment Variables

Create a `.env` file:

```bash
# Parseable credentials
PARSEABLE_USERNAME=admin
PARSEABLE_PASSWORD=admin

# n8n authentication
N8N_BASIC_AUTH_PASSWORD=admin

# Database password
POSTGRES_PASSWORD=admin

# Optional: Custom domain/protocol
N8N_HOST=localhost
N8N_PROTOCOL=http
WEBHOOK_URL=http://localhost:5678/
```

### Docker Compose Configuration

```yaml
version: '3.8'
services:
  parseable:
    image: parseable/parseable:latest
    ports:
      - "8000:8000"
    environment:
      - P_USERNAME=${PARSEABLE_USERNAME}
      - P_PASSWORD=${PARSEABLE_PASSWORD}

  n8n:
    build:
      dockerfile: Dockerfile.working
    environment:
      - PARSEABLE_URL=http://parseable:8000
      - OTEL_SERVICE_NAME=n8n-comprehensive
      - N8N_WINSTON_LOGGING=true
    ports:
      - "5678:5678"
    depends_on:
      - parseable
      - postgres

  postgres:
    image: postgres:15-alpine
    environment:
      - POSTGRES_DB=n8n
      - POSTGRES_USER=n8n
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
```

## Verification

Check that telemetry is flowing:

```bash
# Check service status
docker-compose ps

# View n8n logs for OpenTelemetry initialization
docker logs n8n-comprehensive | grep "OpenTelemetry"

# Verify Parseable streams exist
curl -s http://localhost:8000/api/v1/logstream \
  -H "Authorization: Basic $(echo -n 'admin:admin' | base64)"
```

You should see two streams: `otel-traces` and `otel-metrics`.

## Querying n8n Data

### Workflow Execution Metrics

```sql
SELECT 
  metric_name,
  workflow_name,
  workflow_id,
  data_point_value,
  time_unix_nano
FROM "otel-metrics"
WHERE metric_name LIKE '%workflow%'
ORDER BY time_unix_nano DESC
LIMIT 20
```

### Node Performance Metrics

```sql
SELECT 
  metric_name,
  node_type,
  node_name,
  workflow_name,
  data_point_value,
  time_unix_nano
FROM "otel-metrics"
WHERE metric_name LIKE '%node%'
  AND node_type IS NOT NULL
ORDER BY time_unix_nano DESC
LIMIT 15
```

### HTTP Request Success Rate

```sql
SELECT 
  "http.response.status_code",
  COUNT(*) as request_count,
  COUNT(*) * 100.0 / SUM(COUNT(*)) OVER() as percentage
FROM "otel-metrics"
WHERE metric_name LIKE '%http%'
  AND "http.response.status_code" IS NOT NULL
  AND p_timestamp > NOW() - INTERVAL '24 hours'
GROUP BY "http.response.status_code"
ORDER BY request_count DESC
```

### Slowest HTTP Requests

```sql
SELECT 
  span_name,
  "http.method",
  "http.route",
  EXTRACT(EPOCH FROM (span_end_time_unix_nano - span_start_time_unix_nano)) * 1000 as duration_ms,
  "http.response.status_code",
  span_status_description
FROM "otel-traces"
WHERE span_name LIKE 'GET %' OR span_name LIKE 'POST %'
ORDER BY duration_ms DESC
LIMIT 10
```

## Setting Up Alerts

### HTTP Error Rate Alert

Monitor when n8n experiences high error rates:

1. **Dataset**: `otel-metrics`
2. **Monitor**: `http.status_code` by COUNT
3. **Filter**: `http.response.status_code >= 400`
4. **Threshold**: Trigger when error count > 900 in 5 minutes
5. **Evaluation**: Every 5 minutes

### High Response Time Alert

Get notified when API response times exceed thresholds:

1. **Dataset**: `otel-metrics`
2. **Monitor**: `data_point_value` (for duration metrics)
3. **Filter**: `metric_name LIKE '%http%duration%'`
4. **Threshold**: Trigger when average response time > 2000ms
5. **Group by**: `http.route` to identify specific endpoints

## Alert Delivery Options

Parseable supports multiple notification channels:

* **Webhook** - Send alerts to Slack, Discord, or custom endpoints
* **Email** - Direct email notifications
* **PagerDuty** - Integration for critical production alerts

## Best Practices

1. **Layered Alerting** - Set up multiple severity levels (warning, critical)
2. **Context-Rich Notifications** - Include workflow IDs and execution details
3. **Alert Fatigue Prevention** - Use appropriate thresholds to avoid noise
4. **Escalation Policies** - Define clear escalation paths
5. **Regular Review** - Periodically adjust alert thresholds based on patterns

## What You Get

* **Structured, correlated logs** from n8n using Winston + OpenTelemetry
* **Distributed traces** for every workflow and node to pinpoint slow or failing steps
* **Metrics** for durations, error rates, and token usage
* **Single OTLP pipeline** into Parseable for unified storage and analysis
* **Ready-to-use SQL queries**, dashboards, and alerts

## Resources

* [GitHub Repository](https://github.com/parseablehq/n8n-observability)
* [Full Blog Post](https://www.parseable.com/blog/n8n-observability-with-parseable-a-complete-observability-setup)

## Next Steps

* Set up [alerts](/docs/user-guide/alerting) for workflow failures
* Create [dashboards](/docs/user-guide/dashboards) for n8n monitoring
* Configure [OpenTelemetry](/docs/ingest-data/otel) for other services


# OpenAI (/docs/ingest-data/ai-agents/openai)



Log OpenAI API calls, responses, and token usage to Parseable for LLM observability.

## Overview

Integrate OpenAI with Parseable to:

* **API Logging** - Track all API calls and responses
* **Token Usage** - Monitor token consumption and costs
* **Latency Tracking** - Measure response times
* **Error Analysis** - Debug failed requests
* **Prompt Engineering** - Analyze prompt effectiveness

## Prerequisites

* OpenAI API key
* Parseable instance accessible
* Python or Node.js application

## Python Integration

### Basic Wrapper

```python
import openai
import requests
import time
from datetime import datetime
from functools import wraps

PARSEABLE_URL = "http://parseable:8000"
PARSEABLE_AUTH = ("admin", "admin")
STREAM = "openai-logs"

def log_to_parseable(log_entry):
    try:
        requests.post(
            f"{PARSEABLE_URL}/api/v1/ingest",
            json=[log_entry],
            auth=PARSEABLE_AUTH,
            headers={"X-P-Stream": STREAM}
        )
    except Exception as e:
        print(f"Failed to log: {e}")

def log_openai_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        error = None
        response = None
        
        try:
            response = func(*args, **kwargs)
            return response
        except Exception as e:
            error = str(e)
            raise
        finally:
            duration = time.time() - start_time
            
            log_entry = {
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "model": kwargs.get("model", "unknown"),
                "endpoint": func.__name__,
                "duration_ms": round(duration * 1000, 2),
                "success": error is None,
                "error": error
            }
            
            if response:
                usage = getattr(response, "usage", None)
                if usage:
                    log_entry["prompt_tokens"] = usage.prompt_tokens
                    log_entry["completion_tokens"] = usage.completion_tokens
                    log_entry["total_tokens"] = usage.total_tokens
            
            log_to_parseable(log_entry)
    
    return wrapper

# Wrap OpenAI client
client = openai.OpenAI()

@log_openai_call
def chat_completion(**kwargs):
    return client.chat.completions.create(**kwargs)

# Usage
response = chat_completion(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Comprehensive Logger

```python
import openai
import requests
import json
import hashlib
from datetime import datetime
from typing import Optional, Dict, Any

class OpenAILogger:
    def __init__(self, parseable_url: str, dataset: str, username: str, password: str):
        self.parseable_url = parseable_url
        self.dataset = dataset
        self.auth = (username, password)
        self.client = openai.OpenAI()
    
    def _log(self, entry: Dict[str, Any]):
        try:
            requests.post(
                f"{self.parseable_url}/api/v1/ingest",
                json=[entry],
                auth=self.auth,
                headers={"X-P-Stream": self.dataset},
                timeout=5
            )
        except Exception as e:
            print(f"Logging failed: {e}")
    
    def _hash_content(self, content: str) -> str:
        return hashlib.sha256(content.encode()).hexdigest()[:16]
    
    def chat(self, messages: list, model: str = "gpt-4", **kwargs) -> Any:
        start_time = datetime.utcnow()
        request_id = self._hash_content(json.dumps(messages) + str(start_time))
        
        log_entry = {
            "timestamp": start_time.isoformat() + "Z",
            "request_id": request_id,
            "type": "chat_completion",
            "model": model,
            "message_count": len(messages),
            "system_prompt": next((m["content"][:200] for m in messages if m["role"] == "system"), None),
            "user_prompt": next((m["content"][:500] for m in messages if m["role"] == "user"), None),
            **{k: v for k, v in kwargs.items() if k in ["temperature", "max_tokens", "top_p"]}
        }
        
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                **kwargs
            )
            
            end_time = datetime.utcnow()
            log_entry.update({
                "success": True,
                "duration_ms": (end_time - start_time).total_seconds() * 1000,
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
                "total_tokens": response.usage.total_tokens,
                "finish_reason": response.choices[0].finish_reason,
                "response_preview": response.choices[0].message.content[:200] if response.choices else None
            })
            
            self._log(log_entry)
            return response
            
        except Exception as e:
            log_entry.update({
                "success": False,
                "error": str(e),
                "error_type": type(e).__name__
            })
            self._log(log_entry)
            raise

# Usage
logger = OpenAILogger(
    parseable_url="http://parseable:8000",
    dataset="openai-logs",
    username="admin",
    password="admin"
)

response = logger.chat(
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ],
    model="gpt-4",
    temperature=0.7
)
```

## Node.js Integration

```javascript
const OpenAI = require('openai');
const axios = require('axios');

const PARSEABLE_URL = process.env.PARSEABLE_URL || 'http://parseable:8000';
const PARSEABLE_AUTH = Buffer.from('admin:admin').toString('base64');

class OpenAILogger {
  constructor() {
    this.client = new OpenAI();
  }

  async log(entry) {
    try {
      await axios.post(`${PARSEABLE_URL}/api/v1/ingest`, [entry], {
        headers: {
          'Authorization': `Basic ${PARSEABLE_AUTH}`,
          'X-P-Stream': 'openai-logs',
          'Content-Type': 'application/json'
        }
      });
    } catch (error) {
      console.error('Logging failed:', error.message);
    }
  }

  async chat(messages, options = {}) {
    const startTime = Date.now();
    const model = options.model || 'gpt-4';
    
    const logEntry = {
      timestamp: new Date().toISOString(),
      type: 'chat_completion',
      model,
      message_count: messages.length
    };

    try {
      const response = await this.client.chat.completions.create({
        model,
        messages,
        ...options
      });

      logEntry.success = true;
      logEntry.duration_ms = Date.now() - startTime;
      logEntry.prompt_tokens = response.usage?.prompt_tokens;
      logEntry.completion_tokens = response.usage?.completion_tokens;
      logEntry.total_tokens = response.usage?.total_tokens;
      logEntry.finish_reason = response.choices[0]?.finish_reason;

      await this.log(logEntry);
      return response;

    } catch (error) {
      logEntry.success = false;
      logEntry.error = error.message;
      logEntry.error_type = error.constructor.name;
      await this.log(logEntry);
      throw error;
    }
  }
}

// Usage
const logger = new OpenAILogger();
const response = await logger.chat([
  { role: 'user', content: 'Hello!' }
], { model: 'gpt-4' });
```

## Querying OpenAI Logs

```sql
-- Token usage over time
SELECT 
  DATE_TRUNC('hour', timestamp) as hour,
  SUM(total_tokens) as total_tokens,
  SUM(prompt_tokens) as prompt_tokens,
  SUM(completion_tokens) as completion_tokens,
  COUNT(*) as request_count
FROM "openai-logs"
WHERE timestamp > NOW() - INTERVAL '24 hours'
GROUP BY hour
ORDER BY hour DESC

-- Average latency by model
SELECT 
  model,
  AVG(duration_ms) as avg_latency,
  PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY duration_ms) as p95_latency,
  COUNT(*) as requests
FROM "openai-logs"
WHERE success = true
GROUP BY model

-- Error rate
SELECT 
  DATE_TRUNC('hour', timestamp) as hour,
  COUNT(*) as total,
  SUM(CASE WHEN success = false THEN 1 ELSE 0 END) as errors,
  ROUND(SUM(CASE WHEN success = false THEN 1 ELSE 0 END)::float / COUNT(*) * 100, 2) as error_rate
FROM "openai-logs"
GROUP BY hour
ORDER BY hour DESC

-- Cost estimation (approximate)
SELECT 
  model,
  SUM(prompt_tokens) / 1000.0 * 0.03 as prompt_cost,
  SUM(completion_tokens) / 1000.0 * 0.06 as completion_cost,
  SUM(prompt_tokens) / 1000.0 * 0.03 + SUM(completion_tokens) / 1000.0 * 0.06 as total_cost
FROM "openai-logs"
WHERE timestamp > NOW() - INTERVAL '30 days'
GROUP BY model
```

## Best Practices

1. **Hash Sensitive Data** - Don't log full prompts if sensitive
2. **Track Request IDs** - Correlate requests across systems
3. **Monitor Costs** - Set up alerts for token usage
4. **Log Errors** - Capture error details for debugging
5. **Sample High Volume** - Consider sampling for high-traffic apps

## Next Steps

* Configure [Anthropic](/docs/ingest-data/ai-agents/anthropic) logging
* Set up [LangChain](/docs/ingest-data/ai-agents/langchain) tracing
* Create [dashboards](/docs/user-guide/dashboards) for LLM metrics
* Set up [alerts](/docs/user-guide/alerting) for cost thresholds


# OpenRouter (/docs/ingest-data/ai-agents/openrouter)



Send LLM traces to Parseable using OpenRouter's Broadcast feature — no code changes required.

## Overview

[OpenRouter](https://openrouter.ai) is a unified API for accessing 100+ LLM models. Its Broadcast feature automatically sends OpenTelemetry traces for every LLM request to your configured destinations.

Integrate OpenRouter with Parseable to:

* **Zero-Code Observability** - No application instrumentation needed
* **Track All Requests** - Monitor every LLM call automatically
* **Analyze Costs** - Built-in cost tracking per request
* **Debug Issues** - Full trace context for troubleshooting

## How It Works

OpenRouter Broadcast automatically sends OpenTelemetry-formatted traces to your configured endpoints. Combined with Parseable's native OTLP ingestion, you get full LLM observability in minutes.

```
Your App → OpenRouter → LLM Provider
              ↓
         Broadcast
              ↓
          Parseable
```

## Setup

### Step 1: Get Your Parseable Endpoint

Your Parseable OTLP endpoint:

```
https://your-parseable-host:8000/v1/traces
```

### Step 2: Prepare Authentication Headers

Encode your Parseable credentials:

```bash
echo -n "username:password" | base64
```

Required headers:

```json
{
  "Authorization": "Basic <base64-encoded-credentials>",
  "X-P-Stream": "openrouter-traces",
  "X-P-Log-Source": "otel-traces"
}
```

| Header           | Purpose                               |
| ---------------- | ------------------------------------- |
| `Authorization`  | Basic auth with Parseable credentials |
| `X-P-Stream`     | Target dataset name in Parseable      |
| `X-P-Log-Source` | Must be `otel-traces` for trace data  |

### Step 3: Configure OpenRouter Broadcast

In OpenRouter dashboard, add a new Broadcast destination:

* **Name**: Parseable Production
* **Endpoint**: `https://<your-instance>.parseable.com/v1/traces`
* **Headers**:

```json
{
  "Authorization": "Basic <your-base64-credentials>",
  "X-P-Stream": "openrouter-traces",
  "X-P-Log-Source": "otel-traces"
}
```

### Step 4: Configure Sampling (Optional)

For high-volume applications, sample traces to control costs:

| Sampling Rate | Use Case                           |
| ------------- | ---------------------------------- |
| 1.0 (100%)    | Development, debugging, low-volume |
| 0.1 (10%)     | Medium-volume production           |
| 0.01 (1%)     | High-volume production             |

## Enriching Traces

Add context to your API requests for better observability.

### User Identification

```python
import openai

client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="your-openrouter-key"
)

response = client.chat.completions.create(
    model="anthropic/claude-3.5-sonnet",
    messages=[{"role": "user", "content": "Hello!"}],
    extra_body={
        "user": "user_12345"  # Links traces to specific users
    }
)
```

### Session Tracking

```python
response = client.chat.completions.create(
    model="anthropic/claude-3.5-sonnet",
    messages=[{"role": "user", "content": "Hello!"}],
    extra_body={
        "user": "user_12345",
        "session_id": "session_abc123"  # Groups related requests
    }
)
```

Or via header:

```python
response = client.chat.completions.create(
    model="anthropic/claude-3.5-sonnet",
    messages=[{"role": "user", "content": "Hello!"}],
    extra_headers={
        "x-session-id": "session_abc123"
    }
)
```

## Trace Schema

OpenRouter traces include these fields:

| Field                        | Description                      |
| ---------------------------- | -------------------------------- |
| `trace_id`                   | Unique trace identifier          |
| `span_id`                    | Unique span identifier           |
| `span_name`                  | Operation name                   |
| `span_duration_ns`           | Duration in nanoseconds          |
| `gen_ai.request.model`       | Requested model                  |
| `gen_ai.response.model`      | Actual model used                |
| `gen_ai.usage.input_tokens`  | Input token count                |
| `gen_ai.usage.output_tokens` | Output token count               |
| `gen_ai.usage.cost`          | Estimated cost                   |
| `user.id`                    | User identifier (if provided)    |
| `session.id`                 | Session identifier (if provided) |

## Example Queries

### Token Usage by Model

```sql
SELECT 
  "gen_ai.request.model" AS model,
  COUNT(*) AS requests,
  SUM(CAST("gen_ai.usage.input_tokens" AS BIGINT)) AS input_tokens,
  SUM(CAST("gen_ai.usage.output_tokens" AS BIGINT)) AS output_tokens,
  SUM(CAST("gen_ai.usage.input_tokens" AS BIGINT) + 
      CAST("gen_ai.usage.output_tokens" AS BIGINT)) AS total_tokens
FROM "openrouter-traces"
WHERE p_timestamp > NOW() - INTERVAL '24 hours'
GROUP BY model
ORDER BY total_tokens DESC;
```

### Average Latency by Model

```sql
SELECT 
  "gen_ai.request.model" AS model,
  COUNT(*) AS requests,
  AVG(span_duration_ns / 1e6) AS avg_latency_ms,
  PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY span_duration_ns / 1e6) AS p95_latency_ms
FROM "openrouter-traces"
WHERE p_timestamp > NOW() - INTERVAL '24 hours'
GROUP BY model
ORDER BY avg_latency_ms DESC;
```

### Cost Breakdown by User

```sql
SELECT 
  "user.id" AS user_id,
  COUNT(*) AS requests,
  SUM(CAST("gen_ai.usage.cost" AS DOUBLE)) AS total_cost_usd
FROM "openrouter-traces"
WHERE p_timestamp > NOW() - INTERVAL '7 days'
  AND "user.id" IS NOT NULL
GROUP BY user_id
ORDER BY total_cost_usd DESC
LIMIT 20;
```

### Requests per Session

```sql
SELECT 
  "session.id" AS session_id,
  COUNT(*) AS request_count,
  SUM(CAST("gen_ai.usage.input_tokens" AS BIGINT)) AS total_input_tokens,
  MIN(p_timestamp) AS session_start,
  MAX(p_timestamp) AS session_end
FROM "openrouter-traces"
WHERE "session.id" IS NOT NULL
  AND p_timestamp > NOW() - INTERVAL '24 hours'
GROUP BY session_id
ORDER BY request_count DESC
LIMIT 20;
```

### Error Rate by Model

```sql
SELECT 
  "gen_ai.request.model" AS model,
  COUNT(*) AS total_requests,
  SUM(CASE WHEN span_status_code = 2 THEN 1 ELSE 0 END) AS errors,
  ROUND(100.0 * SUM(CASE WHEN span_status_code = 2 THEN 1 ELSE 0 END) / COUNT(*), 2) AS error_rate
FROM "openrouter-traces"
WHERE p_timestamp > NOW() - INTERVAL '24 hours'
GROUP BY model
ORDER BY error_rate DESC;
```

## Alerting

### High Cost Alert

Monitor when daily LLM spend exceeds budget:

* **Stream**: `openrouter-traces`
* **Column**: `gen_ai.usage.cost`
* **Aggregation**: `SUM`
* **Threshold**: `> 100`

### Latency Spike Alert

Detect when response times degrade:

* **Stream**: `openrouter-traces`
* **Column**: `span_duration_ns`
* **Aggregation**: `AVG`
* **Type**: Anomaly detection

### Error Rate Alert

Get notified when error rates increase:

* **Stream**: `openrouter-traces`
* **Condition**: `span_status_code = 2`

## Dashboard Queries

### Hourly Request Volume

```sql
SELECT 
  DATE_TRUNC('hour', p_timestamp) AS hour,
  COUNT(*) AS requests
FROM "openrouter-traces"
WHERE p_timestamp > NOW() - INTERVAL '7 days'
GROUP BY hour
ORDER BY hour;
```

### Daily Cost Trend

```sql
SELECT 
  DATE_TRUNC('day', p_timestamp) AS day,
  SUM(CAST("gen_ai.usage.cost" AS DOUBLE)) AS daily_cost
FROM "openrouter-traces"
WHERE p_timestamp > NOW() - INTERVAL '30 days'
GROUP BY day
ORDER BY day;
```

## Multiple Destinations

OpenRouter supports up to 5 destinations. Use this for:

| Destination | Stream             | Sampling | API Keys      |
| ----------- | ------------------ | -------- | ------------- |
| Production  | `openrouter-prod`  | 10%      | `prod-*` keys |
| Development | `openrouter-dev`   | 100%     | `dev-*` keys  |
| Debugging   | `openrouter-debug` | 100%     | Specific key  |

## Resources

* [OpenRouter Documentation](https://openrouter.ai/docs)
* [Blog Post](/blog/openrouter-broadcast-parseable-llm-observability)


# vLLM (/docs/ingest-data/ai-agents/vllm)



Monitor vLLM inference workloads with OpenTelemetry and Parseable. Collect metrics, build dashboards, and analyze GPU costs for production LLM serving.

## Overview

[vLLM](https://github.com/vllm-project/vllm) is a fast and easy-to-use library for LLM inference and serving. Originally developed at UC Berkeley, vLLM has evolved into a community-driven project for high-performance model serving.

Integrate vLLM with Parseable to:

* **Monitor Inference Performance** - Track latency, throughput, and GPU utilization
* **Analyze Token Usage** - Measure input/output tokens and costs
* **Debug Issues** - Identify slow requests and errors
* **Optimize Resources** - Right-size GPU infrastructure based on metrics

## Architecture

```
┌─────────────┐    ┌──────────────┐    ┌────────────┐    ┌────────────┐
│    vLLM     │───▶│   Metrics    │───▶│    OTel    │───▶│  Parseable │
│   Service   │    │    Proxy     │    │  Collector │    │            │
└─────────────┘    └──────────────┘    └────────────┘    └────────────┘
       ↓                  ↓                  ↓                  ↓
    Metrics         Sanitization       Collection        Observability
```

## Prerequisites

* vLLM deployment with metrics endpoint accessible
* Docker or Podman with Compose
* Parseable instance (local or cloud)

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/opensourceops/vllm-inference-metrics.git
cd vllm-inference-metrics
```

### 2. Configure vLLM Endpoint

Edit `compose.yml` to point to your vLLM deployment:

```yaml
services:
  proxy:
    environment:
      - VLLM_METRICS_URL=https://your-vllm-endpoint/metrics
```

For local vLLM deployments:

```yaml
environment:
  - VLLM_METRICS_URL=http://localhost:8000/metrics
```

### 3. Start the Stack

Using Docker:

```bash
docker compose -f compose-otel.yml up -d
```

Using Podman:

```bash
podman compose -f compose-otel.yml up -d
```

### 4. Access Services

| Service          | URL                      | Credentials |
| ---------------- | ------------------------ | ----------- |
| Parseable UI     | `localhost:8080`         | admin/admin |
| Metrics endpoint | `localhost:9090/metrics` | -           |
| Health check     | `localhost:9090/health`  | -           |

### 5. Verify Metrics Collection

```bash
# View proxy metrics
curl http://localhost:9090/metrics

# Check OTel Collector logs
docker compose logs -f otel-collector

# Query metrics in Parseable
curl -X POST http://localhost:8080/api/v1/query \
  -H "Authorization: Basic YWRtaW46YWRtaW4=" \
  -d '{"query": "SELECT * FROM vLLMmetrics LIMIT 10"}'
```

## Docker Compose Configuration

Complete `compose-otel.yml` example:

```yaml
services:
  parseable:
    image: parseable/parseable:edge
    command: ["parseable", "local-store"]
    env_file: ./parseable.env
    volumes:
      - parseable-staging:/staging
    ports: ["8080:8000"]
    restart: unless-stopped

  proxy:
    image: python:3.11-alpine
    volumes: ["./proxy.py:/app/proxy.py:ro"]
    environment:
      - VLLM_METRICS_URL=<your-vllm-metrics-url>
    command: >
      sh -c "pip install --no-cache-dir flask requests && python /app/proxy.py"
    ports: ["9090:9090"]
    restart: unless-stopped
    depends_on: [parseable]

  otel-collector:
    image: otel/opentelemetry-collector:latest
    command: ["--config=/etc/otel-config.yaml"]
    volumes:
      - ./otel-config.yaml:/etc/otel-config.yaml:ro
    ports:
      - "4317:4317"  # OTLP/gRPC
      - "4318:4318"  # OTLP/HTTP
    restart: unless-stopped
    depends_on:
      proxy:
        condition: service_healthy
      parseable:
        condition: service_started

volumes:
  parseable-staging:
```

## Environment Variables

| Variable           | Description                 | Default  |
| ------------------ | --------------------------- | -------- |
| `VLLM_METRICS_URL` | vLLM metrics endpoint URL   | Required |
| `P_USERNAME`       | Parseable username          | admin    |
| `P_PASSWORD`       | Parseable password          | admin    |
| `SCRAPE_INTERVAL`  | Metrics collection interval | 2s       |

## Key Metrics

| Metric Name                          | Type      | Description                   |
| ------------------------------------ | --------- | ----------------------------- |
| `vllm_num_requests_running`          | Gauge     | Active inference requests     |
| `vllm_num_requests_waiting`          | Gauge     | Queued requests               |
| `vllm_gpu_cache_usage_perc`          | Gauge     | GPU KV-cache utilization      |
| `vllm_num_preemptions_total`         | Counter   | Request preemptions           |
| `vllm_prompt_tokens_total`           | Counter   | Total prompt tokens processed |
| `vllm_generation_tokens_total`       | Counter   | Total tokens generated        |
| `vllm_request_latency_seconds`       | Histogram | End-to-end request latency    |
| `vllm_time_to_first_token_seconds`   | Histogram | TTFT latency                  |
| `vllm_time_per_output_token_seconds` | Histogram | Inter-token latency           |

## Example Queries

### Request Latency Analysis

```sql
SELECT 
  DATE_TRUNC('minute', p_timestamp) AS minute,
  AVG(vllm_request_latency_seconds) AS avg_latency,
  MAX(vllm_request_latency_seconds) AS max_latency
FROM vLLMmetrics
WHERE p_timestamp > NOW() - INTERVAL '1 hour'
GROUP BY minute
ORDER BY minute;
```

### GPU Cache Utilization

```sql
SELECT 
  p_timestamp,
  vllm_gpu_cache_usage_perc
FROM vLLMmetrics
WHERE p_timestamp > NOW() - INTERVAL '30 minutes'
ORDER BY p_timestamp;
```

### Token Throughput

```sql
SELECT 
  DATE_TRUNC('hour', p_timestamp) AS hour,
  SUM(vllm_prompt_tokens_total) AS input_tokens,
  SUM(vllm_generation_tokens_total) AS output_tokens
FROM vLLMmetrics
GROUP BY hour
ORDER BY hour DESC
LIMIT 24;
```

## Cost Analysis

Track GPU costs with token metrics:

```sql
SELECT 
  DATE_TRUNC('day', p_timestamp) AS day,
  COUNT(*) AS total_requests,
  SUM(vllm_prompt_tokens_total + vllm_generation_tokens_total) AS total_tokens,
  -- A100 PCIe at $1.64/hour example
  ROUND(COUNT(*) * 0.001, 2) AS estimated_cost_usd
FROM vLLMmetrics
GROUP BY day
ORDER BY day DESC;
```

## Alerting

Set up alerts in Parseable for:

* **High Latency**: Alert when `vllm_request_latency_seconds` exceeds threshold
* **Queue Buildup**: Alert when `vllm_num_requests_waiting` grows
* **GPU Memory**: Alert when `vllm_gpu_cache_usage_perc` approaches 100%

## Resources

* [GitHub Repository](https://github.com/opensourceops/vllm-inference-metrics)
* [vLLM Documentation](https://docs.vllm.ai/)
* [Blog Post](/blog/vllm-inference-metrics-otel)


# ArgoCD (/docs/ingest-data/cicd/argocd)



Collect ArgoCD GitOps events and application logs in Parseable.

## Overview

Integrate ArgoCD with Parseable to:

* **Deployment Events** - Track application sync events
* **GitOps Audit** - Monitor configuration changes
* **Health Status** - Track application health over time
* **Troubleshooting** - Debug deployment issues

## Prerequisites

* ArgoCD installed in Kubernetes
* Parseable instance accessible from cluster
* ArgoCD notifications configured

## Method 1: ArgoCD Notifications

Use ArgoCD Notifications to send events to Parseable.

### Install Notifications Controller

```bash
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj-labs/argocd-notifications/release-1.0/manifests/install.yaml
```

### Configure Webhook Service

Create notification configuration:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: argocd-notifications-cm
  namespace: argocd
data:
  service.webhook.parseable: |
    url: http://parseable:8000/api/v1/ingest
    headers:
      - name: Authorization
        value: Basic YWRtaW46YWRtaW4=
      - name: X-P-Stream
        value: argocd-events
      - name: Content-Type
        value: application/json

  template.app-sync-status: |
    webhook:
      parseable:
        method: POST
        body: |
          [{
            "timestamp": "{{.app.status.operationState.finishedAt}}",
            "event": "sync",
            "app_name": "{{.app.metadata.name}}",
            "project": "{{.app.spec.project}}",
            "repo": "{{.app.spec.source.repoURL}}",
            "revision": "{{.app.status.sync.revision}}",
            "sync_status": "{{.app.status.sync.status}}",
            "health_status": "{{.app.status.health.status}}",
            "message": "{{.app.status.operationState.message}}"
          }]

  template.app-health-degraded: |
    webhook:
      parseable:
        method: POST
        body: |
          [{
            "timestamp": "{{now | date \"2006-01-02T15:04:05Z\"}}",
            "event": "health_degraded",
            "app_name": "{{.app.metadata.name}}",
            "project": "{{.app.spec.project}}",
            "health_status": "{{.app.status.health.status}}",
            "sync_status": "{{.app.status.sync.status}}"
          }]

  trigger.on-sync-succeeded: |
    - when: app.status.operationState.phase in ['Succeeded']
      send: [app-sync-status]

  trigger.on-sync-failed: |
    - when: app.status.operationState.phase in ['Failed', 'Error']
      send: [app-sync-status]

  trigger.on-health-degraded: |
    - when: app.status.health.status == 'Degraded'
      send: [app-health-degraded]
```

### Subscribe Applications

Add annotation to applications:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app
  annotations:
    notifications.argoproj.io/subscribe.on-sync-succeeded.parseable: ""
    notifications.argoproj.io/subscribe.on-sync-failed.parseable: ""
    notifications.argoproj.io/subscribe.on-health-degraded.parseable: ""
```

## Method 2: Event Collector

Deploy a collector to watch ArgoCD events.

### Collector Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: argocd-event-collector
  namespace: argocd
spec:
  replicas: 1
  selector:
    matchLabels:
      app: argocd-event-collector
  template:
    spec:
      serviceAccountName: argocd-event-collector
      containers:
        - name: collector
          image: bitnami/kubectl:latest
          command:
            - /bin/bash
            - -c
            - |
              while true; do
                kubectl get events -n argocd --watch -o json | while read event; do
                  curl -s -X POST "${PARSEABLE_URL}/api/v1/ingest" \
                    -H "Authorization: Basic ${PARSEABLE_AUTH}" \
                    -H "X-P-Stream: argocd-events" \
                    -H "Content-Type: application/json" \
                    -d "[${event}]"
                done
              done
          env:
            - name: PARSEABLE_URL
              value: "http://parseable:8000"
            - name: PARSEABLE_AUTH
              valueFrom:
                secretKeyRef:
                  name: parseable-credentials
                  key: auth
```

## Method 3: ArgoCD Logs

Collect ArgoCD component logs using Fluent Bit.

### Fluent Bit Configuration

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: fluent-bit-config
  namespace: argocd
data:
  fluent-bit.conf: |
    [SERVICE]
        Flush         5
        Log_Level     info

    [INPUT]
        Name              tail
        Path              /var/log/containers/argocd-*.log
        Parser            cri
        Tag               argocd.*
        Refresh_Interval  5

    [FILTER]
        Name                kubernetes
        Match               argocd.*
        Kube_URL            https://kubernetes.default.svc:443
        Merge_Log           On

    [OUTPUT]
        Name            http
        Match           *
        Host            parseable
        Port            8000
        URI             /api/v1/ingest
        Format          json
        Header          Authorization Basic YWRtaW46YWRtaW4=
        Header          X-P-Stream argocd-logs
```

## Querying ArgoCD Events

```sql
-- Recent sync events
SELECT timestamp, app_name, sync_status, health_status, revision
FROM "argocd-events"
WHERE event = 'sync'
ORDER BY timestamp DESC
LIMIT 100

-- Failed syncs
SELECT timestamp, app_name, project, message
FROM "argocd-events"
WHERE sync_status = 'Failed' OR sync_status = 'Error'
ORDER BY timestamp DESC

-- Application health history
SELECT 
  app_name,
  health_status,
  COUNT(*) as count
FROM "argocd-events"
WHERE timestamp > NOW() - INTERVAL '24 hours'
GROUP BY app_name, health_status
ORDER BY app_name, count DESC

-- Deployment frequency
SELECT 
  DATE_TRUNC('day', timestamp) as day,
  app_name,
  COUNT(*) as deployments
FROM "argocd-events"
WHERE event = 'sync' AND sync_status = 'Succeeded'
GROUP BY day, app_name
ORDER BY day DESC
```

## Best Practices

1. **Track All Events** - Sync, health, and errors
2. **Include Revision** - Track which commits deployed
3. **Monitor Health** - Alert on degraded applications
4. **Audit Changes** - Log who triggered syncs

## Troubleshooting

### Notifications Not Sending

1. Check notification controller logs
2. Verify webhook URL is accessible
3. Check ConfigMap syntax
4. Verify application annotations

### Missing Events

1. Check trigger conditions
2. Verify template syntax
3. Check ArgoCD logs

## Next Steps

* Set up [alerts](/docs/user-guide/alerting) for failed deployments
* Create [dashboards](/docs/user-guide/dashboards) for GitOps metrics
* Configure [GitHub Actions](/docs/ingest-data/cicd/github-actions) for CI


# CircleCI (/docs/ingest-data/cicd/circleci)



Collect and analyze CircleCI pipeline logs in Parseable for CI/CD observability.

## Overview

Integrate CircleCI with Parseable to:

* **Pipeline Logs** - Collect all job and workflow logs
* **Debug Failures** - Quickly find and analyze failed builds
* **Track Performance** - Monitor build times and trends
* **Audit Pipelines** - Maintain compliance with log retention

## Prerequisites

* CircleCI project
* Parseable instance accessible from CircleCI
* CircleCI environment variables configured

## Direct Log Shipping

Send logs directly from your CircleCI config.

### Config.yml

```yaml
version: 2.1

executors:
  default:
    docker:
      - image: cimg/base:stable

commands:
  send_to_parseable:
    parameters:
      status:
        type: string
      message:
        type: string
        default: ""
    steps:
      - run:
          name: Send to Parseable
          command: |
            curl -X POST "${PARSEABLE_URL}/api/v1/ingest" \
              -H "Authorization: Basic ${PARSEABLE_AUTH}" \
              -H "X-P-Stream: circleci-pipelines" \
              -H "Content-Type: application/json" \
              -d "[{
                \"timestamp\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\",
                \"project\": \"${CIRCLE_PROJECT_REPONAME}\",
                \"workflow\": \"${CIRCLE_WORKFLOW_ID}\",
                \"job\": \"${CIRCLE_JOB}\",
                \"build_num\": ${CIRCLE_BUILD_NUM},
                \"branch\": \"${CIRCLE_BRANCH}\",
                \"sha\": \"${CIRCLE_SHA1}\",
                \"username\": \"${CIRCLE_USERNAME}\",
                \"status\": \"<< parameters.status >>\",
                \"message\": \"<< parameters.message >>\"
              }]"
          when: always

jobs:
  build:
    executor: default
    steps:
      - checkout
      - send_to_parseable:
          status: "started"
          message: "Build started"
      - run:
          name: Build
          command: |
            echo "Building..."
            npm ci
            npm run build
      - send_to_parseable:
          status: "completed"
          message: "Build completed"

  test:
    executor: default
    steps:
      - checkout
      - run:
          name: Test
          command: npm test
      - send_to_parseable:
          status: "completed"
          message: "Tests passed"

workflows:
  build-and-test:
    jobs:
      - build
      - test:
          requires:
            - build
```

### With Status Detection

```yaml
commands:
  send_to_parseable_with_status:
    steps:
      - run:
          name: Send to Parseable
          command: |
            if [ "${CIRCLE_JOB_STATUS}" = "success" ]; then
              STATUS="success"
            else
              STATUS="failure"
            fi
            
            curl -X POST "${PARSEABLE_URL}/api/v1/ingest" \
              -H "Authorization: Basic ${PARSEABLE_AUTH}" \
              -H "X-P-Stream: circleci-pipelines" \
              -H "Content-Type: application/json" \
              -d "[{
                \"timestamp\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\",
                \"project\": \"${CIRCLE_PROJECT_REPONAME}\",
                \"job\": \"${CIRCLE_JOB}\",
                \"build_num\": ${CIRCLE_BUILD_NUM},
                \"status\": \"${STATUS}\"
              }]"
          when: always
```

## Orb Integration

Create a reusable orb for Parseable logging.

### Orb Definition

```yaml
# .circleci/orbs/parseable.yml
version: 2.1

description: Send logs to Parseable

commands:
  log:
    parameters:
      status:
        type: string
      message:
        type: string
        default: ""
      dataset:
        type: string
        default: "circleci-pipelines"
    steps:
      - run:
          name: Log to Parseable
          command: |
            curl -s -X POST "${PARSEABLE_URL}/api/v1/ingest" \
              -H "Authorization: Basic ${PARSEABLE_AUTH}" \
              -H "X-P-Stream: << parameters.dataset >>" \
              -H "Content-Type: application/json" \
              -d "[{
                \"timestamp\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\",
                \"project\": \"${CIRCLE_PROJECT_REPONAME}\",
                \"workflow_id\": \"${CIRCLE_WORKFLOW_ID}\",
                \"job\": \"${CIRCLE_JOB}\",
                \"build_num\": ${CIRCLE_BUILD_NUM},
                \"branch\": \"${CIRCLE_BRANCH}\",
                \"sha\": \"${CIRCLE_SHA1}\",
                \"status\": \"<< parameters.status >>\",
                \"message\": \"<< parameters.message >>\"
              }]" || true
          when: always
```

### Using the Orb

```yaml
version: 2.1

orbs:
  parseable: your-org/parseable@1.0.0

jobs:
  build:
    docker:
      - image: cimg/node:18.0
    steps:
      - checkout
      - parseable/log:
          status: "started"
      - run: npm ci && npm run build
      - parseable/log:
          status: "completed"
```

## Webhook Integration

Use CircleCI webhooks for workflow events.

### Webhook Receiver

```javascript
const express = require('express');
const axios = require('axios');
const crypto = require('crypto');

const app = express();
app.use(express.json());

const CIRCLECI_SECRET = process.env.CIRCLECI_WEBHOOK_SECRET;
const PARSEABLE_URL = process.env.PARSEABLE_URL;
const PARSEABLE_AUTH = process.env.PARSEABLE_AUTH;

app.post('/webhook', async (req, res) => {
  // Verify signature
  const signature = req.headers['circleci-signature'];
  // Verification logic here
  
  const event = req.body;
  
  const logEntry = {
    timestamp: new Date().toISOString(),
    event_type: event.type,
    project: event.project?.name,
    workflow_id: event.workflow?.id,
    workflow_name: event.workflow?.name,
    job_name: event.job?.name,
    status: event.job?.status || event.workflow?.status,
    branch: event.pipeline?.vcs?.branch,
    commit: event.pipeline?.vcs?.revision
  };
  
  try {
    await axios.post(`${PARSEABLE_URL}/api/v1/ingest`, [logEntry], {
      headers: {
        'Authorization': `Basic ${PARSEABLE_AUTH}`,
        'X-P-Stream': 'circleci-webhooks',
        'Content-Type': 'application/json'
      }
    });
  } catch (error) {
    console.error('Error:', error);
  }
  
  res.status(200).json({ status: 'received' });
});

app.listen(3000);
```

## Environment Variables

Configure in CircleCI project settings:

| Variable         | Description                        |
| ---------------- | ---------------------------------- |
| `PARSEABLE_URL`  | Parseable instance URL             |
| `PARSEABLE_AUTH` | Base64 encoded `username:password` |

## Querying CircleCI Logs

```sql
-- Recent builds
SELECT timestamp, project, job, status, branch
FROM "circleci-pipelines"
ORDER BY timestamp DESC
LIMIT 100

-- Failed builds
SELECT timestamp, project, job, branch, message
FROM "circleci-pipelines"
WHERE status = 'failure'
ORDER BY timestamp DESC

-- Build success rate
SELECT 
  project,
  COUNT(*) as total,
  SUM(CASE WHEN status = 'success' THEN 1 ELSE 0 END) as successful,
  ROUND(SUM(CASE WHEN status = 'success' THEN 1 ELSE 0 END)::float / COUNT(*) * 100, 2) as success_rate
FROM "circleci-pipelines"
WHERE timestamp > NOW() - INTERVAL '7 days'
GROUP BY project
```

## Best Practices

1. **Use Orbs** - Centralize logging logic
2. **Log All Jobs** - Track every job in workflow
3. **Include Context** - Add branch, commit, and user info
4. **Handle Failures** - Use `when: always` for logging steps

## Next Steps

* Set up [alerts](/docs/user-guide/alerting) for failed builds
* Create [dashboards](/docs/user-guide/dashboards) for CI/CD metrics
* Configure [GitHub Actions](/docs/ingest-data/cicd/github-actions) for comparison


# GitHub Actions (/docs/ingest-data/cicd/github-actions)



Collect and analyze GitHub Actions workflow logs in Parseable for CI/CD observability.

## Overview

Integrate GitHub Actions with Parseable to:

* **Centralize CI/CD Logs** - Collect all workflow logs in one place
* **Debug Failures** - Quickly find and analyze failed jobs
* **Track Performance** - Monitor build times and trends
* **Audit Pipelines** - Maintain compliance with log retention

## Prerequisites

* GitHub repository with Actions enabled
* Parseable instance accessible from GitHub Actions runners
* GitHub Personal Access Token (for API access)

## Method 1: Direct Log Shipping

Send logs directly from your workflow to Parseable.

### Workflow Configuration

Add a step to send logs to Parseable:

```yaml
name: CI Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Build
        id: build
        run: |
          echo "Starting build..."
          # Your build commands here
          npm ci
          npm run build
          echo "Build completed successfully"
      
      - name: Send logs to Parseable
        if: always()
        run: |
          curl -X POST "${{ secrets.PARSEABLE_URL }}/api/v1/ingest" \
            -H "Authorization: Basic ${{ secrets.PARSEABLE_AUTH }}" \
            -H "X-P-Stream: github-actions" \
            -H "Content-Type: application/json" \
            -d '[{
              "timestamp": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'",
              "repository": "${{ github.repository }}",
              "workflow": "${{ github.workflow }}",
              "job": "${{ github.job }}",
              "run_id": "${{ github.run_id }}",
              "run_number": "${{ github.run_number }}",
              "actor": "${{ github.actor }}",
              "event": "${{ github.event_name }}",
              "ref": "${{ github.ref }}",
              "sha": "${{ github.sha }}",
              "status": "${{ job.status }}",
              "conclusion": "${{ steps.build.conclusion }}"
            }]'
```

### Reusable Action

Create a reusable action for consistent logging:

```yaml
# .github/actions/log-to-parseable/action.yml
name: Log to Parseable
description: Send workflow logs to Parseable

inputs:
  parseable_url:
    description: Parseable instance URL
    required: true
  parseable_auth:
    description: Base64 encoded credentials
    required: true
  dataset:
    description: Parseable dataset name
    default: github-actions
  status:
    description: Job status
    required: true
  message:
    description: Log message
    default: ''

runs:
  using: composite
  steps:
    - name: Send to Parseable
      shell: bash
      run: |
        curl -X POST "${{ inputs.parseable_url }}/api/v1/ingest" \
          -H "Authorization: Basic ${{ inputs.parseable_auth }}" \
          -H "X-P-Stream: ${{ inputs.dataset }}" \
          -H "Content-Type: application/json" \
          -d '[{
            "timestamp": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'",
            "repository": "${{ github.repository }}",
            "workflow": "${{ github.workflow }}",
            "job": "${{ github.job }}",
            "run_id": "${{ github.run_id }}",
            "run_number": "${{ github.run_number }}",
            "actor": "${{ github.actor }}",
            "event": "${{ github.event_name }}",
            "ref": "${{ github.ref }}",
            "sha": "${{ github.sha }}",
            "status": "${{ inputs.status }}",
            "message": "${{ inputs.message }}"
          }]'
```

Use the action in your workflow:

```yaml
- name: Log success
  if: success()
  uses: ./.github/actions/log-to-parseable
  with:
    parseable_url: ${{ secrets.PARSEABLE_URL }}
    parseable_auth: ${{ secrets.PARSEABLE_AUTH }}
    status: success
    message: Build completed successfully

- name: Log failure
  if: failure()
  uses: ./.github/actions/log-to-parseable
  with:
    parseable_url: ${{ secrets.PARSEABLE_URL }}
    parseable_auth: ${{ secrets.PARSEABLE_AUTH }}
    status: failure
    message: Build failed
```

## Method 2: OpenTelemetry Tracing

Use OpenTelemetry to trace your CI/CD pipelines.

### Workflow with OTEL

```yaml
name: CI Pipeline with Tracing

on:
  push:
    branches: [main]

env:
  OTEL_EXPORTER_OTLP_ENDPOINT: ${{ secrets.PARSEABLE_OTEL_ENDPOINT }}
  OTEL_EXPORTER_OTLP_HEADERS: "Authorization=Basic ${{ secrets.PARSEABLE_AUTH }},X-P-Stream=github-actions-traces"

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup OTEL CLI
        run: |
          curl -L https://github.com/equinix-labs/otel-cli/releases/latest/download/otel-cli-linux-amd64 -o otel-cli
          chmod +x otel-cli
          sudo mv otel-cli /usr/local/bin/
      
      - name: Build with tracing
        run: |
          otel-cli exec \
            --name "build" \
            --service "github-actions" \
            --attrs "repository=${{ github.repository }},workflow=${{ github.workflow }}" \
            -- npm run build
```

## Method 3: Webhook Integration

Use GitHub webhooks to capture workflow events.

### Webhook Receiver

Create a webhook receiver that forwards events to Parseable:

```javascript
// github-webhook-to-parseable.js
const express = require('express');
const crypto = require('crypto');
const axios = require('axios');

const app = express();
app.use(express.json());

const WEBHOOK_SECRET = process.env.GITHUB_WEBHOOK_SECRET;
const PARSEABLE_URL = process.env.PARSEABLE_URL;
const PARSEABLE_AUTH = process.env.PARSEABLE_AUTH;

function verifySignature(payload, signature) {
  const hmac = crypto.createHmac('sha256', WEBHOOK_SECRET);
  const digest = 'sha256=' + hmac.update(JSON.stringify(payload)).digest('hex');
  return crypto.timingSafeEqual(Buffer.from(signature), Buffer.from(digest));
}

app.post('/webhook', async (req, res) => {
  const signature = req.headers['x-hub-signature-256'];
  
  if (!verifySignature(req.body, signature)) {
    return res.status(401).json({ error: 'Invalid signature' });
  }
  
  const event = req.headers['x-github-event'];
  const payload = req.body;
  
  // Only process workflow events
  if (event === 'workflow_run' || event === 'workflow_job') {
    const logEntry = {
      timestamp: new Date().toISOString(),
      event_type: event,
      action: payload.action,
      repository: payload.repository?.full_name,
      workflow: payload.workflow?.name || payload.workflow_run?.name,
      run_id: payload.workflow_run?.id || payload.workflow_job?.run_id,
      conclusion: payload.workflow_run?.conclusion || payload.workflow_job?.conclusion,
      actor: payload.sender?.login,
      url: payload.workflow_run?.html_url || payload.workflow_job?.html_url
    };
    
    try {
      await axios.post(`${PARSEABLE_URL}/api/v1/ingest`, [logEntry], {
        headers: {
          'Authorization': `Basic ${PARSEABLE_AUTH}`,
          'X-P-Stream': 'github-webhooks',
          'Content-Type': 'application/json'
        }
      });
    } catch (error) {
      console.error('Error sending to Parseable:', error);
    }
  }
  
  res.status(200).json({ status: 'received' });
});

app.listen(3000, () => {
  console.log('GitHub webhook receiver listening on port 3000');
});
```

### Configure GitHub Webhook

1. Go to your repository **Settings** → **Webhooks**
2. Click **Add webhook**
3. Set Payload URL to your webhook receiver
4. Set Content type to `application/json`
5. Set Secret to your webhook secret
6. Select events: **Workflow runs** and **Workflow jobs**

## Querying GitHub Actions Logs

Query your CI/CD logs in Parseable:

```sql
-- Get recent workflow runs
SELECT timestamp, repository, workflow, status, actor
FROM "github-actions"
ORDER BY timestamp DESC
LIMIT 100

-- Find failed builds
SELECT timestamp, repository, workflow, run_id, message
FROM "github-actions"
WHERE status = 'failure'
ORDER BY timestamp DESC

-- Build success rate by repository
SELECT 
  repository,
  COUNT(*) as total_runs,
  SUM(CASE WHEN status = 'success' THEN 1 ELSE 0 END) as successful,
  ROUND(SUM(CASE WHEN status = 'success' THEN 1 ELSE 0 END)::float / COUNT(*) * 100, 2) as success_rate
FROM "github-actions"
WHERE timestamp > NOW() - INTERVAL '7 days'
GROUP BY repository
ORDER BY success_rate ASC
```

## GitHub Secrets Configuration

Add these secrets to your repository:

| Secret                    | Description                        |
| ------------------------- | ---------------------------------- |
| `PARSEABLE_URL`           | Your Parseable instance URL        |
| `PARSEABLE_AUTH`          | Base64 encoded `username:password` |
| `PARSEABLE_OTEL_ENDPOINT` | OTEL endpoint (for tracing)        |

## Best Practices

1. **Use Secrets** - Never hardcode credentials in workflows
2. **Log on Failure** - Always capture failure information
3. **Include Context** - Add repository, workflow, and run details
4. **Use Consistent Streams** - Organize logs by dataset
5. **Set Retention** - Configure appropriate log retention

## Troubleshooting

### Logs Not Appearing

1. Verify Parseable URL is accessible from GitHub runners
2. Check authentication credentials are correct
3. Verify the dataset exists or auto-creation is enabled
4. Check workflow logs for curl errors

### Authentication Failures

1. Verify Base64 encoding of credentials
2. Check the Parseable user has ingest permissions
3. Verify secrets are properly configured

## Next Steps

* Set up [alerts](/docs/user-guide/alerting) for failed builds
* Create [dashboards](/docs/user-guide/dashboards) for CI/CD metrics
* Configure [Jenkins](/docs/ingest-data/cicd/jenkins) for additional pipelines


# GitLab CI (/docs/ingest-data/cicd/gitlab-ci)



Collect and analyze GitLab CI/CD pipeline logs in Parseable for comprehensive observability.

## Overview

Integrate GitLab CI with Parseable to:

* **Centralize Pipeline Logs** - Collect all CI/CD logs in one place
* **Debug Failures** - Quickly find and analyze failed jobs
* **Track Performance** - Monitor pipeline times and trends
* **Audit Pipelines** - Maintain compliance with log retention

## Prerequisites

* GitLab repository with CI/CD enabled
* Parseable instance accessible from GitLab runners
* GitLab CI/CD variables configured

## Method 1: Direct Log Shipping

Send logs directly from your `.gitlab-ci.yml`.

### Basic Configuration

```yaml
variables:
  PARSEABLE_URL: ${PARSEABLE_URL}
  PARSEABLE_AUTH: ${PARSEABLE_AUTH}

stages:
  - build
  - test
  - deploy

.send_to_parseable: &send_to_parseable
  - |
    curl -X POST "${PARSEABLE_URL}/api/v1/ingest" \
      -H "Authorization: Basic ${PARSEABLE_AUTH}" \
      -H "X-P-Stream: gitlab-pipelines" \
      -H "Content-Type: application/json" \
      -d "[{
        \"timestamp\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\",
        \"project\": \"${CI_PROJECT_PATH}\",
        \"pipeline_id\": ${CI_PIPELINE_ID},
        \"job_id\": ${CI_JOB_ID},
        \"job_name\": \"${CI_JOB_NAME}\",
        \"stage\": \"${CI_JOB_STAGE}\",
        \"ref\": \"${CI_COMMIT_REF_NAME}\",
        \"sha\": \"${CI_COMMIT_SHA}\",
        \"author\": \"${GITLAB_USER_LOGIN}\",
        \"status\": \"${1}\",
        \"message\": \"${2}\"
      }]"

build:
  stage: build
  script:
    - echo "Building..."
    - npm ci
    - npm run build
  after_script:
    - |
      if [ "$CI_JOB_STATUS" == "success" ]; then
        STATUS="success"
        MESSAGE="Build completed successfully"
      else
        STATUS="failure"
        MESSAGE="Build failed"
      fi
      curl -X POST "${PARSEABLE_URL}/api/v1/ingest" \
        -H "Authorization: Basic ${PARSEABLE_AUTH}" \
        -H "X-P-Stream: gitlab-pipelines" \
        -H "Content-Type: application/json" \
        -d "[{
          \"timestamp\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\",
          \"project\": \"${CI_PROJECT_PATH}\",
          \"pipeline_id\": ${CI_PIPELINE_ID},
          \"job_id\": ${CI_JOB_ID},
          \"job_name\": \"${CI_JOB_NAME}\",
          \"stage\": \"${CI_JOB_STAGE}\",
          \"ref\": \"${CI_COMMIT_REF_NAME}\",
          \"sha\": \"${CI_COMMIT_SHA}\",
          \"author\": \"${GITLAB_USER_LOGIN}\",
          \"status\": \"${STATUS}\",
          \"message\": \"${MESSAGE}\"
        }]"

test:
  stage: test
  script:
    - npm test
  after_script:
    - |
      STATUS="${CI_JOB_STATUS}"
      curl -X POST "${PARSEABLE_URL}/api/v1/ingest" \
        -H "Authorization: Basic ${PARSEABLE_AUTH}" \
        -H "X-P-Stream: gitlab-pipelines" \
        -H "Content-Type: application/json" \
        -d "[{
          \"timestamp\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\",
          \"project\": \"${CI_PROJECT_PATH}\",
          \"pipeline_id\": ${CI_PIPELINE_ID},
          \"job_id\": ${CI_JOB_ID},
          \"job_name\": \"${CI_JOB_NAME}\",
          \"stage\": \"${CI_JOB_STAGE}\",
          \"status\": \"${STATUS}\"
        }]"
```

### Reusable Template

Create a reusable template for consistent logging:

```yaml
# templates/parseable.yml
.parseable_logging:
  after_script:
    - |
      STATUS="${CI_JOB_STATUS:-unknown}"
      DURATION="${CI_JOB_DURATION:-0}"
      
      curl -s -X POST "${PARSEABLE_URL}/api/v1/ingest" \
        -H "Authorization: Basic ${PARSEABLE_AUTH}" \
        -H "X-P-Stream: gitlab-pipelines" \
        -H "Content-Type: application/json" \
        -d "[{
          \"timestamp\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\",
          \"project\": \"${CI_PROJECT_PATH}\",
          \"project_id\": ${CI_PROJECT_ID},
          \"pipeline_id\": ${CI_PIPELINE_ID},
          \"pipeline_url\": \"${CI_PIPELINE_URL}\",
          \"job_id\": ${CI_JOB_ID},
          \"job_name\": \"${CI_JOB_NAME}\",
          \"job_url\": \"${CI_JOB_URL}\",
          \"stage\": \"${CI_JOB_STAGE}\",
          \"ref\": \"${CI_COMMIT_REF_NAME}\",
          \"sha\": \"${CI_COMMIT_SHA}\",
          \"short_sha\": \"${CI_COMMIT_SHORT_SHA}\",
          \"author\": \"${GITLAB_USER_LOGIN}\",
          \"author_email\": \"${GITLAB_USER_EMAIL}\",
          \"status\": \"${STATUS}\",
          \"duration_seconds\": ${DURATION},
          \"runner\": \"${CI_RUNNER_DESCRIPTION}\",
          \"environment\": \"${CI_ENVIRONMENT_NAME:-none}\"
        }]" || true
```

Use the template:

```yaml
include:
  - local: templates/parseable.yml

build:
  extends: .parseable_logging
  stage: build
  script:
    - npm ci
    - npm run build

test:
  extends: .parseable_logging
  stage: test
  script:
    - npm test
```

## Method 2: GitLab Webhooks

Use GitLab webhooks to capture pipeline events.

### Webhook Receiver

```javascript
// gitlab-webhook-to-parseable.js
const express = require('express');
const axios = require('axios');

const app = express();
app.use(express.json());

const GITLAB_TOKEN = process.env.GITLAB_WEBHOOK_TOKEN;
const PARSEABLE_URL = process.env.PARSEABLE_URL;
const PARSEABLE_AUTH = process.env.PARSEABLE_AUTH;

app.post('/webhook', async (req, res) => {
  // Verify token
  if (req.headers['x-gitlab-token'] !== GITLAB_TOKEN) {
    return res.status(401).json({ error: 'Invalid token' });
  }
  
  const event = req.headers['x-gitlab-event'];
  const payload = req.body;
  
  let logEntry = null;
  
  if (event === 'Pipeline Hook') {
    logEntry = {
      timestamp: new Date().toISOString(),
      event_type: 'pipeline',
      project: payload.project?.path_with_namespace,
      pipeline_id: payload.object_attributes?.id,
      ref: payload.object_attributes?.ref,
      sha: payload.object_attributes?.sha,
      status: payload.object_attributes?.status,
      duration: payload.object_attributes?.duration,
      created_at: payload.object_attributes?.created_at,
      finished_at: payload.object_attributes?.finished_at,
      user: payload.user?.username
    };
  } else if (event === 'Job Hook') {
    logEntry = {
      timestamp: new Date().toISOString(),
      event_type: 'job',
      project: payload.project?.path_with_namespace,
      pipeline_id: payload.pipeline_id,
      job_id: payload.build_id,
      job_name: payload.build_name,
      stage: payload.build_stage,
      status: payload.build_status,
      duration: payload.build_duration,
      runner: payload.runner?.description,
      user: payload.user?.username
    };
  }
  
  if (logEntry) {
    try {
      await axios.post(`${PARSEABLE_URL}/api/v1/ingest`, [logEntry], {
        headers: {
          'Authorization': `Basic ${PARSEABLE_AUTH}`,
          'X-P-Stream': 'gitlab-webhooks',
          'Content-Type': 'application/json'
        }
      });
    } catch (error) {
      console.error('Error sending to Parseable:', error);
    }
  }
  
  res.status(200).json({ status: 'received' });
});

app.listen(3000);
```

### Configure GitLab Webhook

1. Go to your project **Settings** → **Webhooks**
2. Enter your webhook URL
3. Enter a Secret Token
4. Select events: **Pipeline events** and **Job events**
5. Click **Add webhook**

## Method 3: OpenTelemetry Tracing

Use OpenTelemetry for distributed tracing of pipelines.

```yaml
variables:
  OTEL_EXPORTER_OTLP_ENDPOINT: ${PARSEABLE_OTEL_ENDPOINT}
  OTEL_EXPORTER_OTLP_HEADERS: "Authorization=Basic ${PARSEABLE_AUTH},X-P-Stream=gitlab-traces"
  OTEL_SERVICE_NAME: gitlab-ci

build:
  stage: build
  image: node:18
  before_script:
    - npm install -g @opentelemetry/auto-instrumentations-node
  script:
    - node --require @opentelemetry/auto-instrumentations-node npm run build
```

## GitLab CI/CD Variables

Configure these variables in GitLab:

| Variable                  | Type              | Description                        |
| ------------------------- | ----------------- | ---------------------------------- |
| `PARSEABLE_URL`           | Variable          | Parseable instance URL             |
| `PARSEABLE_AUTH`          | Variable (masked) | Base64 encoded `username:password` |
| `PARSEABLE_OTEL_ENDPOINT` | Variable          | OTEL endpoint (for tracing)        |

## Querying GitLab Logs

Query your GitLab CI/CD logs in Parseable:

```sql
-- Get recent pipeline runs
SELECT timestamp, project, pipeline_id, status, duration_seconds
FROM "gitlab-pipelines"
ORDER BY timestamp DESC
LIMIT 100

-- Find failed jobs
SELECT timestamp, project, job_name, stage, status, job_url
FROM "gitlab-pipelines"
WHERE status = 'failed'
ORDER BY timestamp DESC

-- Pipeline success rate by project
SELECT 
  project,
  COUNT(*) as total_pipelines,
  SUM(CASE WHEN status = 'success' THEN 1 ELSE 0 END) as successful,
  ROUND(SUM(CASE WHEN status = 'success' THEN 1 ELSE 0 END)::float / COUNT(*) * 100, 2) as success_rate
FROM "gitlab-pipelines"
WHERE timestamp > NOW() - INTERVAL '7 days'
  AND job_name IS NULL  -- Pipeline-level events only
GROUP BY project
ORDER BY success_rate ASC

-- Average job duration by stage
SELECT 
  stage,
  AVG(duration_seconds) as avg_duration,
  MAX(duration_seconds) as max_duration,
  COUNT(*) as job_count
FROM "gitlab-pipelines"
WHERE timestamp > NOW() - INTERVAL '7 days'
  AND duration_seconds IS NOT NULL
GROUP BY stage
ORDER BY avg_duration DESC
```

## Best Practices

1. **Use Templates** - Centralize logging configuration
2. **Include Context** - Add project, pipeline, and job details
3. **Log All Stages** - Track each stage separately
4. **Handle Failures** - Use `|| true` to prevent logging failures from breaking builds
5. **Mask Secrets** - Always mask sensitive variables

## Troubleshooting

### Logs Not Appearing

1. Verify Parseable URL is accessible from GitLab runners
2. Check CI/CD variables are properly configured
3. Verify the dataset exists or auto-creation is enabled
4. Check job logs for curl errors

### Authentication Failures

1. Verify Base64 encoding of credentials
2. Check the Parseable user has ingest permissions
3. Ensure variables are not protected when running on unprotected branches

## Next Steps

* Set up [alerts](/docs/user-guide/alerting) for failed pipelines
* Create [dashboards](/docs/user-guide/dashboards) for CI/CD metrics
* Configure [GitHub Actions](/docs/ingest-data/cicd/github-actions) for multi-platform CI


# Jenkins (/docs/ingest-data/cicd/jenkins)



Collect and analyze Jenkins build logs in Parseable for comprehensive CI/CD observability.

## Overview

Integrate Jenkins with Parseable to:

* **Centralize Build Logs** - Collect all Jenkins logs in one place
* **Debug Failures** - Quickly find and analyze failed builds
* **Track Performance** - Monitor build times and trends
* **Audit Pipelines** - Maintain compliance with log retention

## Prerequisites

* Jenkins instance with Pipeline support
* Parseable instance accessible from Jenkins
* Jenkins HTTP Request plugin (optional)

## Method 1: Pipeline Script

Send logs directly from your Jenkinsfile.

### Declarative Pipeline

```groovy
pipeline {
    agent any
    
    environment {
        PARSEABLE_URL = credentials('parseable-url')
        PARSEABLE_AUTH = credentials('parseable-auth')
    }
    
    stages {
        stage('Build') {
            steps {
                script {
                    sendToParseable('started', 'Build started')
                }
                sh 'npm ci'
                sh 'npm run build'
            }
        }
        
        stage('Test') {
            steps {
                sh 'npm test'
            }
        }
    }
    
    post {
        success {
            script {
                sendToParseable('success', 'Build completed successfully')
            }
        }
        failure {
            script {
                sendToParseable('failure', 'Build failed')
            }
        }
        always {
            script {
                sendToParseable(currentBuild.result ?: 'unknown', 'Build finished')
            }
        }
    }
}

def sendToParseable(String status, String message) {
    def payload = """[{
        "timestamp": "${new Date().format("yyyy-MM-dd'T'HH:mm:ss'Z'", TimeZone.getTimeZone('UTC'))}",
        "job_name": "${env.JOB_NAME}",
        "build_number": ${env.BUILD_NUMBER},
        "build_url": "${env.BUILD_URL}",
        "node": "${env.NODE_NAME}",
        "status": "${status}",
        "message": "${message}",
        "duration": ${currentBuild.duration},
        "user": "${currentBuild.getBuildCauses()[0]?.userId ?: 'system'}"
    }]"""
    
    httpRequest(
        url: "${PARSEABLE_URL}/api/v1/ingest",
        httpMode: 'POST',
        contentType: 'APPLICATION_JSON',
        customHeaders: [
            [name: 'Authorization', value: "Basic ${PARSEABLE_AUTH}"],
            [name: 'X-P-Stream', value: 'jenkins-builds']
        ],
        requestBody: payload,
        validResponseCodes: '200:299'
    )
}
```

### Scripted Pipeline

```groovy
node {
    def parseableUrl = env.PARSEABLE_URL
    def parseableAuth = env.PARSEABLE_AUTH
    
    try {
        stage('Build') {
            sendLog('started', 'Build started')
            sh 'npm ci && npm run build'
        }
        
        stage('Test') {
            sh 'npm test'
        }
        
        sendLog('success', 'Build completed successfully')
        
    } catch (Exception e) {
        sendLog('failure', "Build failed: ${e.message}")
        throw e
    }
}

def sendLog(String status, String message) {
    def payload = [
        [
            timestamp: new Date().format("yyyy-MM-dd'T'HH:mm:ss'Z'"),
            job_name: env.JOB_NAME,
            build_number: env.BUILD_NUMBER as Integer,
            build_url: env.BUILD_URL,
            status: status,
            message: message
        ]
    ]
    
    httpRequest(
        url: "${env.PARSEABLE_URL}/api/v1/ingest",
        httpMode: 'POST',
        contentType: 'APPLICATION_JSON',
        customHeaders: [
            [name: 'Authorization', value: "Basic ${env.PARSEABLE_AUTH}"],
            [name: 'X-P-Stream', value: 'jenkins-builds']
        ],
        requestBody: groovy.json.JsonOutput.toJson(payload)
    )
}
```

## Method 2: Fluent Bit Sidecar

Collect Jenkins logs using Fluent Bit.

### Fluent Bit Configuration

```yaml
service:
  flush: 5
  log_level: info

pipeline:
  inputs:
    - name: tail
      path: /var/jenkins_home/jobs/*/builds/*/log
      tag: jenkins.build
      parser: jenkins
      refresh_interval: 5

  parsers:
    - name: jenkins
      format: regex
      regex: ^(?<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d+Z)\s+(?<message>.*)$
      time_key: timestamp
      time_format: "%Y-%m-%dT%H:%M:%S.%LZ"

  outputs:
    - name: http
      match: jenkins.*
      host: parseable
      port: 8000
      uri: /api/v1/ingest
      format: json
      header: Authorization Basic YWRtaW46YWRtaW4=
      header: X-P-Stream jenkins-logs
```

### Docker Compose

```yaml
version: '3.8'
services:
  jenkins:
    image: jenkins/jenkins:lts
    volumes:
      - jenkins_home:/var/jenkins_home
    ports:
      - "8080:8080"
  
  fluent-bit:
    image: fluent/fluent-bit:latest
    volumes:
      - jenkins_home:/var/jenkins_home:ro
      - ./fluent-bit.yaml:/fluent-bit/etc/fluent-bit.yaml
    depends_on:
      - jenkins
      - parseable

volumes:
  jenkins_home:
```

## Method 3: Logstash Integration

Use Logstash to collect and forward Jenkins logs.

### Logstash Configuration

```ruby
input {
  file {
    path => "/var/jenkins_home/jobs/*/builds/*/log"
    start_position => "beginning"
    sincedb_path => "/var/logstash/sincedb"
    codec => multiline {
      pattern => "^\d{4}-\d{2}-\d{2}"
      negate => true
      what => "previous"
    }
  }
}

filter {
  grok {
    match => { 
      "path" => "/var/jenkins_home/jobs/(?<job_name>[^/]+)/builds/(?<build_number>\d+)/log" 
    }
  }
  
  mutate {
    add_field => {
      "source" => "jenkins"
    }
  }
}

output {
  http {
    url => "http://parseable:8000/api/v1/ingest"
    http_method => "post"
    format => "json"
    headers => {
      "Authorization" => "Basic YWRtaW46YWRtaW4="
      "X-P-Stream" => "jenkins-logs"
    }
  }
}
```

## Method 4: Jenkins Webhook

Use Jenkins webhooks to send build notifications.

### Shared Library

Create a shared library for consistent logging:

```groovy
// vars/parseableNotify.groovy
def call(Map config = [:]) {
    def status = config.status ?: currentBuild.result ?: 'UNKNOWN'
    def message = config.message ?: "Build ${status}"
    
    def payload = [
        [
            timestamp: new Date().format("yyyy-MM-dd'T'HH:mm:ss'Z'", TimeZone.getTimeZone('UTC')),
            job_name: env.JOB_NAME,
            build_number: env.BUILD_NUMBER as Integer,
            build_url: env.BUILD_URL,
            git_commit: env.GIT_COMMIT,
            git_branch: env.GIT_BRANCH,
            node: env.NODE_NAME,
            status: status,
            message: message,
            duration_ms: currentBuild.duration,
            executor: currentBuild.getBuildCauses()[0]?.userId ?: 'system'
        ]
    ]
    
    httpRequest(
        url: "${env.PARSEABLE_URL}/api/v1/ingest",
        httpMode: 'POST',
        contentType: 'APPLICATION_JSON',
        customHeaders: [
            [name: 'Authorization', value: "Basic ${env.PARSEABLE_AUTH}"],
            [name: 'X-P-Stream', value: config.dataset ?: 'jenkins-builds']
        ],
        requestBody: groovy.json.JsonOutput.toJson(payload),
        validResponseCodes: '200:299',
        quiet: true
    )
}
```

Use in your pipeline:

```groovy
@Library('my-shared-library') _

pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                parseableNotify(status: 'STARTED', message: 'Build started')
                sh 'make build'
            }
        }
    }
    
    post {
        success {
            parseableNotify(status: 'SUCCESS')
        }
        failure {
            parseableNotify(status: 'FAILURE')
        }
    }
}
```

## Jenkins Credentials

Add these credentials in Jenkins:

| Credential ID    | Type        | Description                        |
| ---------------- | ----------- | ---------------------------------- |
| `parseable-url`  | Secret text | Parseable instance URL             |
| `parseable-auth` | Secret text | Base64 encoded `username:password` |

## Querying Jenkins Logs

Query your Jenkins logs in Parseable:

```sql
-- Get recent builds
SELECT timestamp, job_name, build_number, status, duration
FROM "jenkins-builds"
ORDER BY timestamp DESC
LIMIT 100

-- Find failed builds
SELECT timestamp, job_name, build_number, message, build_url
FROM "jenkins-builds"
WHERE status = 'FAILURE'
ORDER BY timestamp DESC

-- Average build duration by job
SELECT 
  job_name,
  COUNT(*) as total_builds,
  AVG(duration_ms) / 1000 as avg_duration_seconds,
  MAX(duration_ms) / 1000 as max_duration_seconds
FROM "jenkins-builds"
WHERE timestamp > NOW() - INTERVAL '7 days'
GROUP BY job_name
ORDER BY avg_duration_seconds DESC

-- Build success rate
SELECT 
  job_name,
  COUNT(*) as total,
  SUM(CASE WHEN status = 'SUCCESS' THEN 1 ELSE 0 END) as successful,
  ROUND(SUM(CASE WHEN status = 'SUCCESS' THEN 1 ELSE 0 END)::float / COUNT(*) * 100, 2) as success_rate
FROM "jenkins-builds"
WHERE timestamp > NOW() - INTERVAL '30 days'
GROUP BY job_name
ORDER BY success_rate ASC
```

## Best Practices

1. **Use Shared Libraries** - Centralize logging logic
2. **Include Git Context** - Add commit, branch, and author info
3. **Log Stage Transitions** - Track each stage separately
4. **Capture Build Causes** - Know who/what triggered builds
5. **Set Up Alerts** - Notify on repeated failures

## Troubleshooting

### HTTP Request Plugin Errors

1. Install the HTTP Request plugin
2. Verify Parseable URL is accessible from Jenkins
3. Check credentials are properly configured
4. Review Jenkins console output for errors

### Missing Logs

1. Verify the log file paths are correct
2. Check Fluent Bit/Logstash has read permissions
3. Verify the Parseable dataset exists

## Next Steps

* Set up [alerts](/docs/user-guide/alerting) for failed builds
* Create [dashboards](/docs/user-guide/dashboards) for CI/CD metrics
* Configure [GitHub Actions](/docs/ingest-data/cicd/github-actions) for additional pipelines


# Terraform (/docs/ingest-data/cicd/terraform)



Collect Terraform execution logs and state changes in Parseable.

## Overview

Integrate Terraform with Parseable to:

* **Execution Logs** - Track plan and apply operations
* **State Changes** - Monitor infrastructure changes
* **Audit Trail** - Compliance and change history
* **Cost Tracking** - Monitor resource changes

## Prerequisites

* Terraform CLI or Terraform Cloud
* Parseable instance accessible
* CI/CD pipeline (recommended)

## Method 1: CI/CD Integration

Send Terraform logs from your CI/CD pipeline.

### GitHub Actions

```yaml
name: Terraform

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  terraform:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_wrapper: false
      
      - name: Terraform Init
        id: init
        run: terraform init
      
      - name: Terraform Plan
        id: plan
        run: terraform plan -out=tfplan -json > plan.json 2>&1
        continue-on-error: true
      
      - name: Send Plan to Parseable
        run: |
          # Parse plan output
          ADDS=$(jq '[.resource_changes[]? | select(.change.actions | contains(["create"]))] | length' plan.json 2>/dev/null || echo 0)
          CHANGES=$(jq '[.resource_changes[]? | select(.change.actions | contains(["update"]))] | length' plan.json 2>/dev/null || echo 0)
          DESTROYS=$(jq '[.resource_changes[]? | select(.change.actions | contains(["delete"]))] | length' plan.json 2>/dev/null || echo 0)
          
          curl -X POST "${{ secrets.PARSEABLE_URL }}/api/v1/ingest" \
            -H "Authorization: Basic ${{ secrets.PARSEABLE_AUTH }}" \
            -H "X-P-Stream: terraform-logs" \
            -H "Content-Type: application/json" \
            -d "[{
              \"timestamp\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\",
              \"event\": \"plan\",
              \"repository\": \"${{ github.repository }}\",
              \"ref\": \"${{ github.ref }}\",
              \"sha\": \"${{ github.sha }}\",
              \"actor\": \"${{ github.actor }}\",
              \"status\": \"${{ steps.plan.outcome }}\",
              \"resources_to_add\": ${ADDS},
              \"resources_to_change\": ${CHANGES},
              \"resources_to_destroy\": ${DESTROYS}
            }]"
      
      - name: Terraform Apply
        if: github.ref == 'refs/heads/main' && github.event_name == 'push'
        id: apply
        run: terraform apply -auto-approve tfplan
      
      - name: Send Apply to Parseable
        if: github.ref == 'refs/heads/main' && github.event_name == 'push'
        run: |
          curl -X POST "${{ secrets.PARSEABLE_URL }}/api/v1/ingest" \
            -H "Authorization: Basic ${{ secrets.PARSEABLE_AUTH }}" \
            -H "X-P-Stream: terraform-logs" \
            -H "Content-Type: application/json" \
            -d "[{
              \"timestamp\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\",
              \"event\": \"apply\",
              \"repository\": \"${{ github.repository }}\",
              \"sha\": \"${{ github.sha }}\",
              \"actor\": \"${{ github.actor }}\",
              \"status\": \"${{ steps.apply.outcome }}\"
            }]"
```

### GitLab CI

```yaml
stages:
  - plan
  - apply

variables:
  TF_ROOT: ${CI_PROJECT_DIR}

plan:
  stage: plan
  image: hashicorp/terraform:latest
  script:
    - terraform init
    - terraform plan -out=tfplan -json > plan.json
    - |
      ADDS=$(jq '[.resource_changes[]? | select(.change.actions | contains(["create"]))] | length' plan.json)
      CHANGES=$(jq '[.resource_changes[]? | select(.change.actions | contains(["update"]))] | length' plan.json)
      DESTROYS=$(jq '[.resource_changes[]? | select(.change.actions | contains(["delete"]))] | length' plan.json)
      
      curl -X POST "${PARSEABLE_URL}/api/v1/ingest" \
        -H "Authorization: Basic ${PARSEABLE_AUTH}" \
        -H "X-P-Stream: terraform-logs" \
        -H "Content-Type: application/json" \
        -d "[{
          \"timestamp\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\",
          \"event\": \"plan\",
          \"project\": \"${CI_PROJECT_PATH}\",
          \"ref\": \"${CI_COMMIT_REF_NAME}\",
          \"sha\": \"${CI_COMMIT_SHA}\",
          \"actor\": \"${GITLAB_USER_LOGIN}\",
          \"resources_to_add\": ${ADDS},
          \"resources_to_change\": ${CHANGES},
          \"resources_to_destroy\": ${DESTROYS}
        }]"
  artifacts:
    paths:
      - tfplan

apply:
  stage: apply
  image: hashicorp/terraform:latest
  script:
    - terraform init
    - terraform apply -auto-approve tfplan
    - |
      curl -X POST "${PARSEABLE_URL}/api/v1/ingest" \
        -H "Authorization: Basic ${PARSEABLE_AUTH}" \
        -H "X-P-Stream: terraform-logs" \
        -H "Content-Type: application/json" \
        -d "[{
          \"timestamp\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\",
          \"event\": \"apply\",
          \"project\": \"${CI_PROJECT_PATH}\",
          \"sha\": \"${CI_COMMIT_SHA}\",
          \"status\": \"success\"
        }]"
  only:
    - main
```

## Method 2: Terraform Cloud Webhooks

Use Terraform Cloud run notifications.

### Webhook Receiver

```javascript
const express = require('express');
const axios = require('axios');

const app = express();
app.use(express.json());

const PARSEABLE_URL = process.env.PARSEABLE_URL;
const PARSEABLE_AUTH = process.env.PARSEABLE_AUTH;

app.post('/webhook', async (req, res) => {
  const notification = req.body;
  
  const logEntry = {
    timestamp: new Date().toISOString(),
    event: 'terraform_cloud',
    run_id: notification.run_id,
    run_status: notification.run_status,
    workspace: notification.workspace_name,
    organization: notification.organization_name,
    message: notification.run_message,
    created_by: notification.run_created_by,
    is_destroy: notification.run_is_destroy,
    plan_resource_additions: notification.plan_resource_additions,
    plan_resource_changes: notification.plan_resource_changes,
    plan_resource_destructions: notification.plan_resource_destructions
  };
  
  try {
    await axios.post(`${PARSEABLE_URL}/api/v1/ingest`, [logEntry], {
      headers: {
        'Authorization': `Basic ${PARSEABLE_AUTH}`,
        'X-P-Stream': 'terraform-cloud',
        'Content-Type': 'application/json'
      }
    });
  } catch (error) {
    console.error('Error:', error);
  }
  
  res.status(200).json({ status: 'received' });
});

app.listen(3000);
```

### Configure in Terraform Cloud

1. Go to **Workspace Settings** → **Notifications**
2. Click **Create Notification**
3. Select **Webhook**
4. Enter your webhook URL
5. Select triggers (Run completed, needs attention, etc.)

## Querying Terraform Logs

```sql
-- Recent Terraform operations
SELECT timestamp, event, repository, actor, status,
       resources_to_add, resources_to_change, resources_to_destroy
FROM "terraform-logs"
ORDER BY timestamp DESC
LIMIT 100

-- Failed applies
SELECT timestamp, repository, actor, status
FROM "terraform-logs"
WHERE event = 'apply' AND status != 'success'
ORDER BY timestamp DESC

-- Resource change summary
SELECT 
  DATE_TRUNC('day', timestamp) as day,
  SUM(resources_to_add) as total_added,
  SUM(resources_to_change) as total_changed,
  SUM(resources_to_destroy) as total_destroyed
FROM "terraform-logs"
WHERE event = 'plan'
GROUP BY day
ORDER BY day DESC

-- Most active repositories
SELECT 
  repository,
  COUNT(*) as operations,
  SUM(resources_to_add + resources_to_change + resources_to_destroy) as total_changes
FROM "terraform-logs"
WHERE timestamp > NOW() - INTERVAL '30 days'
GROUP BY repository
ORDER BY operations DESC
```

## Best Practices

1. **Log Plans and Applies** - Track both operations
2. **Include Resource Counts** - Monitor change volume
3. **Track Actors** - Know who made changes
4. **Alert on Destroys** - Notify on resource deletions
5. **Store Plan Files** - Keep for audit purposes

## Troubleshooting

### Missing Logs

1. Check CI/CD pipeline logs
2. Verify Parseable endpoint
3. Check authentication

### Incorrect Counts

1. Verify JSON parsing
2. Check plan output format
3. Handle empty plans

## Next Steps

* Set up [alerts](/docs/user-guide/alerting) for infrastructure changes
* Create [dashboards](/docs/user-guide/dashboards) for IaC metrics
* Configure [ArgoCD](/docs/ingest-data/cicd/argocd) for GitOps


# AWS CloudWatch (/docs/ingest-data/cloud/aws-cloudwatch)



Collect and forward logs from AWS CloudWatch Log Groups to Parseable using the OpenTelemetry Collector.

## Overview

Integrate AWS CloudWatch with Parseable to:

* **Centralize AWS Logs** - Collect logs from Lambda, ECS, EC2, and other AWS services
* **Unified Observability** - Combine AWS logs with application logs
* **Cost Optimization** - Reduce CloudWatch costs by forwarding to Parseable
* **Advanced Analytics** - Use Parseable's SQL queries on AWS logs

## Prerequisites

* AWS account with CloudWatch Logs
* AWS credentials with CloudWatch read permissions
* OpenTelemetry Collector with `awscloudwatch` receiver
* Parseable instance running and accessible

### IAM Permissions

Create an IAM policy with the required permissions:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:DescribeLogGroups",
        "logs:DescribeLogStreams",
        "logs:GetLogEvents",
        "logs:FilterLogEvents"
      ],
      "Resource": "*"
    }
  ]
}
```

## OpenTelemetry Collector Configuration

### Basic Configuration

Create an `otel-collector-config.yaml` file:

```yaml
receivers:
  awscloudwatch:
    region: us-east-1
    logs:
      poll_interval: 1m
      groups:
        autodiscover:
          limit: 100

exporters:
  otlphttp/parseable:
    endpoint: "http://parseable:8000"
    headers:
      Authorization: "Basic YWRtaW46YWRtaW4="
      X-P-Stream: "cloudwatch-logs"
      X-P-Log-Source: "otel-logs"
    tls:
      insecure: true

service:
  pipelines:
    logs:
      receivers: [awscloudwatch]
      exporters: [otlphttp/parseable]
```

### Filter Specific Log Groups

Collect logs from specific log groups only:

```yaml
receivers:
  awscloudwatch:
    region: us-east-1
    logs:
      poll_interval: 1m
      groups:
        named:
          /aws/lambda/my-function:
          /aws/ecs/my-cluster:
          /aws/apigateway/my-api:

exporters:
  otlphttp/parseable:
    endpoint: "http://parseable:8000"
    headers:
      Authorization: "Basic YWRtaW46YWRtaW4="
      X-P-Stream: "cloudwatch-logs"
      X-P-Log-Source: "otel-logs"
    tls:
      insecure: true

service:
  pipelines:
    logs:
      receivers: [awscloudwatch]
      exporters: [otlphttp/parseable]
```

### Autodiscover with Prefix Filter

Discover log groups matching a prefix:

```yaml
receivers:
  awscloudwatch:
    region: us-east-1
    logs:
      poll_interval: 1m
      groups:
        autodiscover:
          limit: 50
          prefix: /aws/lambda/

exporters:
  otlphttp/parseable:
    endpoint: "http://parseable:8000"
    headers:
      Authorization: "Basic YWRtaW46YWRtaW4="
      X-P-Stream: "lambda-logs"
      X-P-Log-Source: "otel-logs"
    tls:
      insecure: true

service:
  pipelines:
    logs:
      receivers: [awscloudwatch]
      exporters: [otlphttp/parseable]
```

### Filter Log Streams

Filter specific log streams within log groups:

```yaml
receivers:
  awscloudwatch:
    region: us-east-1
    logs:
      poll_interval: 1m
      groups:
        named:
          /aws/lambda/my-function:
            names:
              - "2024/01/15/[$LATEST]abc123"
            prefixes:
              - "2024/01/"

exporters:
  otlphttp/parseable:
    endpoint: "http://parseable:8000"
    headers:
      Authorization: "Basic YWRtaW46YWRtaW4="
      X-P-Stream: "lambda-logs"
      X-P-Log-Source: "otel-logs"
    tls:
      insecure: true

service:
  pipelines:
    logs:
      receivers: [awscloudwatch]
      exporters: [otlphttp/parseable]
```

## Configuration Options

### Top Level Parameters

| Parameter       | Required | Description                    |
| --------------- | -------- | ------------------------------ |
| `region`        | Yes      | AWS region (e.g., `us-east-1`) |
| `profile`       | No       | AWS profile name               |
| `imds_endpoint` | No       | Custom IMDS endpoint for EC2   |
| `logs`          | No       | Logs collection configuration  |

### Logs Parameters

| Parameter                | Default | Description                       |
| ------------------------ | ------- | --------------------------------- |
| `poll_interval`          | `1m`    | Time between log requests         |
| `max_events_per_request` | `1000`  | Max events per CloudWatch request |
| `groups`                 | All     | Log group configuration           |

### Group Parameters

| Parameter             | Description                    |
| --------------------- | ------------------------------ |
| `autodiscover.limit`  | Max log groups to discover     |
| `autodiscover.prefix` | Log group name prefix filter   |
| `named`               | Specific log groups to collect |

## Running the Collector

### Docker with AWS Credentials

```bash
docker run -d \
  --name otel-collector \
  -v $(pwd)/otel-collector-config.yaml:/etc/otelcol/config.yaml \
  -v ~/.aws:/root/.aws:ro \
  -e AWS_REGION=us-east-1 \
  otel/opentelemetry-collector-contrib:latest
```

### Docker with Environment Variables

```bash
docker run -d \
  --name otel-collector \
  -v $(pwd)/otel-collector-config.yaml:/etc/otelcol/config.yaml \
  -e AWS_ACCESS_KEY_ID=your-access-key \
  -e AWS_SECRET_ACCESS_KEY=your-secret-key \
  -e AWS_REGION=us-east-1 \
  otel/opentelemetry-collector-contrib:latest
```

### Kubernetes with IAM Roles for Service Accounts (IRSA)

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: otel-collector
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::123456789012:role/OtelCollectorRole
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: otel-collector
spec:
  template:
    spec:
      serviceAccountName: otel-collector
      containers:
        - name: otel-collector
          image: otel/opentelemetry-collector-contrib:latest
          volumeMounts:
            - name: config
              mountPath: /etc/otelcol/config.yaml
              subPath: config.yaml
      volumes:
        - name: config
          configMap:
            name: otel-collector-config
```

## Querying CloudWatch Logs in Parseable

Once data is flowing, query your CloudWatch logs:

```sql
-- Get recent Lambda logs
SELECT p_timestamp, log_group, log_stream, message 
FROM "cloudwatch-logs" 
WHERE log_group LIKE '/aws/lambda/%'
ORDER BY p_timestamp DESC 
LIMIT 100

-- Find Lambda errors
SELECT p_timestamp, log_group, message
FROM "cloudwatch-logs"
WHERE log_group LIKE '/aws/lambda/%'
  AND (message LIKE '%ERROR%' OR message LIKE '%Exception%')
ORDER BY p_timestamp DESC

-- Count logs by log group
SELECT log_group, COUNT(*) as log_count
FROM "cloudwatch-logs"
WHERE p_timestamp > NOW() - INTERVAL '1 hour'
GROUP BY log_group
ORDER BY log_count DESC
```

## Troubleshooting

### Authentication Issues

1. Verify AWS credentials are configured correctly
2. Check IAM permissions include required CloudWatch actions
3. Verify the region matches your log groups
4. Check for credential expiration (if using temporary credentials)

### Missing Logs

1. Verify log groups exist and have recent logs
2. Check `poll_interval` is appropriate for your log volume
3. Verify autodiscover prefix matches your log group names
4. Check CloudWatch Logs retention settings

### High Latency

1. Reduce `poll_interval` for more frequent collection
2. Increase `max_events_per_request` for higher throughput
3. Filter to specific log groups to reduce API calls

## Next Steps

* Set up [alerts](/docs/user-guide/alerting) for AWS log patterns
* Create [dashboards](/docs/user-guide/dashboards) for AWS monitoring
* Configure [AWS S3](/docs/self-hosted/storage-targets/aws-s3) for log storage


# AWS Kinesis (/docs/ingest-data/cloud/aws-kinesis)



Stream logs from AWS Kinesis Data Streams and Kinesis Data Firehose to Parseable.

## Overview

Integrate AWS Kinesis with Parseable to:

* **Real-time Streaming** - Ingest logs as they arrive
* **High Throughput** - Handle massive log volumes
* **AWS Integration** - Collect logs from AWS services
* **Buffering** - Use Firehose for batched delivery

## Prerequisites

* AWS account with Kinesis access
* Parseable instance accessible from AWS
* IAM permissions for Kinesis

## Method 1: Kinesis Data Firehose

Use Firehose for managed delivery to Parseable's HTTP endpoint.

### Create Delivery Stream

1. Go to **Kinesis** → **Data Firehose**
2. Click **Create delivery dataset**
3. Configure source (Direct PUT or Kinesis Data Stream)
4. Select **HTTP Endpoint** as destination
5. Configure endpoint:

| Field             | Value                                  |
| ----------------- | -------------------------------------- |
| HTTP endpoint URL | `https://your-parseable/api/v1/ingest` |
| Content encoding  | GZIP (recommended)                     |
| Access key        | Your Parseable credentials             |

### Configure Buffering

```
Buffer size: 5 MB
Buffer interval: 60 seconds
```

### IAM Role

Firehose needs permissions to deliver to HTTP endpoint:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "firehose:PutRecord",
        "firehose:PutRecordBatch"
      ],
      "Resource": "arn:aws:firehose:*:*:deliverystream/parseable-*"
    }
  ]
}
```

## Method 2: Lambda Consumer

Use Lambda to consume from Kinesis and forward to Parseable.

### Lambda Function

```javascript
// index.js
const https = require('https');

const PARSEABLE_URL = process.env.PARSEABLE_URL;
const PARSEABLE_AUTH = process.env.PARSEABLE_AUTH;
const STREAM_NAME = process.env.STREAM_NAME || 'kinesis-logs';

exports.handler = async (event) => {
  const logs = event.Records.map(record => {
    const payload = Buffer.from(record.kinesis.data, 'base64').toString('utf-8');
    try {
      return JSON.parse(payload);
    } catch {
      return { message: payload, timestamp: new Date().toISOString() };
    }
  });

  const url = new URL(PARSEABLE_URL);
  const options = {
    hostname: url.hostname,
    port: url.port || 443,
    path: '/api/v1/ingest',
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Basic ${PARSEABLE_AUTH}`,
      'X-P-Stream': STREAM_NAME
    }
  };

  return new Promise((resolve, reject) => {
    const req = https.request(options, (res) => {
      if (res.statusCode >= 200 && res.statusCode < 300) {
        resolve({ statusCode: 200, body: 'Success' });
      } else {
        reject(new Error(`HTTP ${res.statusCode}`));
      }
    });
    req.on('error', reject);
    req.write(JSON.stringify(logs));
    req.end();
  });
};
```

### Lambda Configuration

```yaml
# serverless.yml
functions:
  kinesisConsumer:
    handler: index.handler
    events:
      - dataset:
          type: kinesis
          arn: arn:aws:kinesis:region:account:dataset/your-dataset
          batchSize: 100
          startingPosition: LATEST
    environment:
      PARSEABLE_URL: https://your-parseable.com
      PARSEABLE_AUTH: ${ssm:/parseable/auth}
      STREAM_NAME: kinesis-logs
```

## Method 3: OpenTelemetry Collector

Use OTel Collector with Kinesis receiver.

### Configuration

```yaml
receivers:
  awskinesis:
    stream_name: your-kinesis-dataset
    region: us-east-1
    encoding: json

exporters:
  otlphttp/parseable:
    endpoint: "http://parseable:8000"
    headers:
      Authorization: "Basic YWRtaW46YWRtaW4="
      X-P-Stream: "kinesis-logs"
      X-P-Log-Source: "otel-logs"

service:
  pipelines:
    logs:
      receivers: [awskinesis]
      exporters: [otlphttp/parseable]
```

## Best Practices

1. **Use Firehose** - For managed, reliable delivery
2. **Enable Compression** - Reduce data transfer costs
3. **Configure Retries** - Handle transient failures
4. **Monitor Metrics** - Track delivery success rates
5. **Set Buffer Sizes** - Balance latency vs efficiency

## Troubleshooting

### Delivery Failures

1. Check Parseable endpoint is accessible
2. Verify authentication credentials
3. Check CloudWatch logs for errors
4. Verify IAM permissions

### Data Loss

1. Enable S3 backup in Firehose
2. Configure dead letter queue
3. Monitor iterator age

## Next Steps

* Set up [AWS CloudWatch](/docs/ingest-data/cloud/aws-cloudwatch) for CloudWatch logs
* Configure [alerts](/docs/user-guide/alerting) for streaming metrics
* Create [dashboards](/docs/user-guide/dashboards) for monitoring


# Azure Event Hubs (/docs/ingest-data/cloud/azure-event-hubs)



Stream logs from Azure Event Hubs to Parseable for centralized observability.

## Overview

Integrate Azure Event Hubs with Parseable to:

* **Stream Azure Logs** - Collect logs from Azure services
* **High Throughput** - Handle millions of events per second
* **Real-time Processing** - Process logs as they arrive
* **Azure Integration** - Native Azure ecosystem support

## Prerequisites

* Azure subscription with Event Hubs
* Event Hubs namespace and hub created
* Parseable instance accessible from Azure
* Connection string or managed identity

## Method 1: Azure Functions

Use Azure Functions to consume events and forward to Parseable.

### Function Code

```javascript
// index.js
const axios = require('axios');

module.exports = async function (context, eventHubMessages) {
  const PARSEABLE_URL = process.env.PARSEABLE_URL;
  const PARSEABLE_AUTH = process.env.PARSEABLE_AUTH;
  
  const logs = eventHubMessages.map(msg => {
    if (typeof msg === 'string') {
      try {
        return JSON.parse(msg);
      } catch {
        return { message: msg, timestamp: new Date().toISOString() };
      }
    }
    return msg;
  });

  try {
    await axios.post(`${PARSEABLE_URL}/api/v1/ingest`, logs, {
      headers: {
        'Authorization': `Basic ${PARSEABLE_AUTH}`,
        'X-P-Stream': 'azure-events',
        'Content-Type': 'application/json'
      }
    });
    context.log(`Sent ${logs.length} events to Parseable`);
  } catch (error) {
    context.log.error('Error sending to Parseable:', error);
    throw error;
  }
};
```

### Function Configuration

```json
// function.json
{
  "bindings": [
    {
      "type": "eventHubTrigger",
      "name": "eventHubMessages",
      "direction": "in",
      "eventHubName": "your-event-hub",
      "connection": "EventHubConnection",
      "cardinality": "many",
      "consumerGroup": "$Default"
    }
  ]
}
```

### Application Settings

```
PARSEABLE_URL=https://your-parseable.com
PARSEABLE_AUTH=base64-encoded-credentials
EventHubConnection=Endpoint=sb://...
```

## Method 2: OpenTelemetry Collector

Use OTel Collector with Azure Event Hubs receiver.

### Configuration

```yaml
receivers:
  azureeventhub:
    connection: ${EVENTHUB_CONNECTION}
    format: json

exporters:
  otlphttp/parseable:
    endpoint: "http://parseable:8000"
    headers:
      Authorization: "Basic YWRtaW46YWRtaW4="
      X-P-Stream: "azure-events"
      X-P-Log-Source: "otel-logs"

service:
  pipelines:
    logs:
      receivers: [azureeventhub]
      exporters: [otlphttp/parseable]
```

## Method 3: Fluent Bit

Use Fluent Bit with Azure Event Hubs input.

### Configuration

```yaml
service:
  flush: 5
  log_level: info

pipeline:
  inputs:
    - name: azure_event_hub
      connection_string: ${EVENTHUB_CONNECTION}
      hub_name: your-event-hub
      consumer_group: $Default

  outputs:
    - name: http
      match: '*'
      host: parseable
      port: 8000
      uri: /api/v1/ingest
      format: json
      header: Authorization Basic YWRtaW46YWRtaW4=
      header: X-P-Stream azure-events
```

## Diagnostic Settings

Export Azure resource logs to Event Hubs:

1. Go to your Azure resource
2. **Monitoring** → **Diagnostic settings**
3. Click **Add diagnostic setting**
4. Select log categories
5. Choose **Stream to an event hub**
6. Select your Event Hubs namespace and hub

## Best Practices

1. **Use Consumer Groups** - Separate consumers for different purposes
2. **Configure Partitions** - Scale throughput with partitions
3. **Enable Checkpointing** - Track processing progress
4. **Monitor Lag** - Watch for processing delays
5. **Handle Retries** - Implement retry logic

## Troubleshooting

### Connection Issues

1. Verify connection string is correct
2. Check network connectivity
3. Verify firewall rules allow access
4. Check managed identity permissions

### Missing Events

1. Verify consumer group configuration
2. Check checkpoint storage
3. Monitor Event Hubs metrics

## Next Steps

* Set up [Azure Blob Storage](/docs/self-hosted/storage-targets/azure-blob-storage) for log storage
* Configure [alerts](/docs/user-guide/alerting) for Azure metrics
* Create [dashboards](/docs/user-guide/dashboards) for monitoring


# Google Cloud Pub/Sub (/docs/ingest-data/cloud/gcp-pubsub)



Stream logs from Google Cloud Pub/Sub to Parseable using the OpenTelemetry Collector.

## Overview

Integrate Google Cloud Pub/Sub with Parseable to:

* **Stream GCP Logs** - Collect logs from Cloud Logging via Pub/Sub
* **Real-time Ingestion** - Process logs as they arrive
* **Unified Observability** - Combine GCP logs with other sources
* **Scalable Collection** - Handle high-volume log streams

## Prerequisites

* Google Cloud project with Pub/Sub enabled
* Pub/Sub subscription for log messages
* Service account with Pub/Sub permissions
* OpenTelemetry Collector with `googlecloudpubsub` receiver
* Parseable instance running and accessible

### IAM Permissions

Create a service account with the required permissions:

```bash
# Create service account
gcloud iam service-accounts create otel-collector \
  --display-name="OpenTelemetry Collector"

# Grant Pub/Sub Subscriber role
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
  --member="serviceAccount:otel-collector@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/pubsub.subscriber"

# Create and download key
gcloud iam service-accounts keys create key.json \
  --iam-account=otel-collector@YOUR_PROJECT_ID.iam.gserviceaccount.com
```

## Setting Up Cloud Logging Export

### Create a Pub/Sub Topic

```bash
gcloud pubsub topics create parseable-logs
```

### Create a Subscription

```bash
gcloud pubsub subscriptions create parseable-logs-sub \
  --topic=parseable-logs \
  --ack-deadline=60
```

### Create a Log Sink

Export Cloud Logging logs to Pub/Sub:

```bash
gcloud logging sinks create parseable-sink \
  pubsub.googleapis.com/projects/YOUR_PROJECT_ID/topics/parseable-logs \
  --log-filter='resource.type="gce_instance" OR resource.type="cloud_function"'
```

### Grant Sink Permissions

```bash
# Get the sink's writer identity
SINK_IDENTITY=$(gcloud logging sinks describe parseable-sink --format='value(writerIdentity)')

# Grant publish permission
gcloud pubsub topics add-iam-policy-binding parseable-logs \
  --member="$SINK_IDENTITY" \
  --role="roles/pubsub.publisher"
```

## OpenTelemetry Collector Configuration

### Basic Configuration

Create an `otel-collector-config.yaml` file:

```yaml
receivers:
  googlecloudpubsub:
    project: your-gcp-project-id
    subscription: projects/your-gcp-project-id/subscriptions/parseable-logs-sub
    encoding: cloud_logging

exporters:
  otlphttp/parseable:
    endpoint: "http://parseable:8000"
    headers:
      Authorization: "Basic YWRtaW46YWRtaW4="
      X-P-Stream: "gcp-logs"
      X-P-Log-Source: "otel-logs"
    tls:
      insecure: true

service:
  pipelines:
    logs:
      receivers: [googlecloudpubsub]
      exporters: [otlphttp/parseable]
```

### With Processing

Add processors to transform logs:

```yaml
receivers:
  googlecloudpubsub:
    project: your-gcp-project-id
    subscription: projects/your-gcp-project-id/subscriptions/parseable-logs-sub
    encoding: cloud_logging

processors:
  batch:
    timeout: 10s
    send_batch_size: 1000
  
  attributes:
    actions:
      - key: cloud.provider
        value: gcp
        action: insert

exporters:
  otlphttp/parseable:
    endpoint: "http://parseable:8000"
    headers:
      Authorization: "Basic YWRtaW46YWRtaW4="
      X-P-Stream: "gcp-logs"
      X-P-Log-Source: "otel-logs"
    tls:
      insecure: true

service:
  pipelines:
    logs:
      receivers: [googlecloudpubsub]
      processors: [batch, attributes]
      exporters: [otlphttp/parseable]
```

## Configuration Options

| Parameter      | Description                                                |
| -------------- | ---------------------------------------------------------- |
| `project`      | GCP project ID                                             |
| `subscription` | Full subscription path                                     |
| `encoding`     | Message encoding (`cloud_logging`, `raw_text`, `raw_json`) |

## Running the Collector

### Docker with Service Account Key

```bash
docker run -d \
  --name otel-collector \
  -v $(pwd)/otel-collector-config.yaml:/etc/otelcol/config.yaml \
  -v $(pwd)/key.json:/etc/gcp/key.json \
  -e GOOGLE_APPLICATION_CREDENTIALS=/etc/gcp/key.json \
  otel/opentelemetry-collector-contrib:latest
```

### Kubernetes with Workload Identity

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: otel-collector
  annotations:
    iam.gke.io/gcp-service-account: otel-collector@YOUR_PROJECT_ID.iam.gserviceaccount.com
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: otel-collector
spec:
  template:
    spec:
      serviceAccountName: otel-collector
      containers:
        - name: otel-collector
          image: otel/opentelemetry-collector-contrib:latest
          volumeMounts:
            - name: config
              mountPath: /etc/otelcol/config.yaml
              subPath: config.yaml
      volumes:
        - name: config
          configMap:
            name: otel-collector-config
```

## Querying GCP Logs in Parseable

Once data is flowing, query your GCP logs:

```sql
-- Get recent GCP logs
SELECT p_timestamp, resource_type, severity, text_payload 
FROM "gcp-logs" 
ORDER BY p_timestamp DESC 
LIMIT 100

-- Find Cloud Function errors
SELECT p_timestamp, resource_labels, text_payload
FROM "gcp-logs"
WHERE resource_type = 'cloud_function'
  AND severity IN ('ERROR', 'CRITICAL')
ORDER BY p_timestamp DESC

-- Count logs by resource type
SELECT resource_type, COUNT(*) as log_count
FROM "gcp-logs"
WHERE p_timestamp > NOW() - INTERVAL '1 hour'
GROUP BY resource_type
ORDER BY log_count DESC
```

## Troubleshooting

### Authentication Issues

1. Verify service account key is valid
2. Check IAM permissions include Pub/Sub Subscriber role
3. Verify GOOGLE\_APPLICATION\_CREDENTIALS is set
4. Check Workload Identity binding if using GKE

### Missing Messages

1. Verify the subscription exists and is active
2. Check the log sink filter matches your logs
3. Verify the sink has publish permission on the topic
4. Check for message acknowledgment issues

### High Latency

1. Increase batch size for higher throughput
2. Reduce ack deadline if messages are timing out
3. Scale the collector horizontally

## Next Steps

* Set up [alerts](/docs/user-guide/alerting) for GCP log patterns
* Create [dashboards](/docs/user-guide/dashboards) for GCP monitoring
* Configure [AWS CloudWatch](/docs/ingest-data/cloud/aws-cloudwatch) for multi-cloud


# Amazon ECS (/docs/ingest-data/containers/amazon-ecs)



Collect and forward logs from Amazon ECS (Elastic Container Service) to Parseable.

## Overview

Integrate Amazon ECS with Parseable to:

* **Container Logs** - Collect logs from ECS tasks
* **Centralized Observability** - Unified view of container logs
* **AWS Integration** - Native AWS log routing
* **Fargate Support** - Works with both EC2 and Fargate

## Prerequisites

* AWS account with ECS
* ECS cluster running
* Parseable instance accessible from AWS
* IAM permissions for log routing

## Method 1: FireLens (Fluent Bit)

Use AWS FireLens with Fluent Bit sidecar for log routing.

### Task Definition

```json
{
  "family": "my-app",
  "containerDefinitions": [
    {
      "name": "log-router",
      "image": "amazon/aws-for-fluent-bit:latest",
      "essential": true,
      "firelensConfiguration": {
        "type": "fluentbit",
        "options": {
          "config-file-type": "file",
          "config-file-value": "/fluent-bit/configs/parse-json.conf"
        }
      },
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/firelens",
          "awslogs-region": "us-east-1",
          "awslogs-dataset-prefix": "firelens"
        }
      },
      "memoryReservation": 50
    },
    {
      "name": "app",
      "image": "my-app:latest",
      "essential": true,
      "logConfiguration": {
        "logDriver": "awsfirelens",
        "options": {
          "Name": "http",
          "Host": "parseable.example.com",
          "Port": "8000",
          "URI": "/api/v1/ingest",
          "Format": "json",
          "Header": "Authorization Basic YWRtaW46YWRtaW4=",
          "Header": "X-P-Stream ecs-logs"
        }
      }
    }
  ]
}
```

### Custom Fluent Bit Config

Store in S3 or include in custom image:

```ini
[OUTPUT]
    Name http
    Match *
    Host parseable.example.com
    Port 8000
    URI /api/v1/ingest
    Format json
    Header Authorization Basic YWRtaW46YWRtaW4=
    Header X-P-Stream ecs-logs
    tls On
    tls.verify Off
```

## Method 2: CloudWatch to Parseable

Route logs through CloudWatch, then forward to Parseable.

### Task Definition with awslogs

```json
{
  "containerDefinitions": [
    {
      "name": "app",
      "image": "my-app:latest",
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/my-app",
          "awslogs-region": "us-east-1",
          "awslogs-dataset-prefix": "app"
        }
      }
    }
  ]
}
```

Then use [AWS CloudWatch integration](/docs/ingest-data/cloud/aws-cloudwatch) to forward to Parseable.

## Method 3: Sidecar Container

Deploy a log collector sidecar alongside your application.

### Task Definition with Sidecar

```json
{
  "family": "my-app-with-collector",
  "containerDefinitions": [
    {
      "name": "app",
      "image": "my-app:latest",
      "essential": true,
      "mountPoints": [
        {
          "sourceVolume": "logs",
          "containerPath": "/var/log/app"
        }
      ]
    },
    {
      "name": "log-collector",
      "image": "fluent/fluent-bit:latest",
      "essential": false,
      "mountPoints": [
        {
          "sourceVolume": "logs",
          "containerPath": "/var/log/app",
          "readOnly": true
        }
      ],
      "environment": [
        {"name": "PARSEABLE_URL", "value": "http://parseable:8000"},
        {"name": "PARSEABLE_AUTH", "value": "YWRtaW46YWRtaW4="}
      ]
    }
  ],
  "volumes": [
    {
      "name": "logs",
      "host": {}
    }
  ]
}
```

## IAM Permissions

Required IAM permissions for FireLens:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogStream",
        "logs:CreateLogGroup",
        "logs:PutLogEvents"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject"
      ],
      "Resource": "arn:aws:s3:::your-config-bucket/*"
    }
  ]
}
```

## Best Practices

1. **Use FireLens** - AWS-native log routing
2. **Add Metadata** - Include task ID, cluster name
3. **Configure Retries** - Handle transient failures
4. **Monitor Log Router** - Watch sidecar health
5. **Use Secrets** - Store credentials in Secrets Manager

## Troubleshooting

### Logs Not Appearing

1. Check FireLens container logs
2. Verify Parseable endpoint is accessible
3. Check IAM permissions
4. Verify log configuration syntax

### High Memory Usage

1. Configure buffer limits
2. Reduce batch sizes
3. Check for log volume spikes

## Next Steps

* Configure [Amazon EKS](/docs/ingest-data/containers/amazon-eks) for Kubernetes
* Set up [alerts](/docs/user-guide/alerting) for container metrics
* Create [dashboards](/docs/user-guide/dashboards) for monitoring


# Amazon EKS (/docs/ingest-data/containers/amazon-eks)



Collect and forward logs from Amazon EKS (Elastic Kubernetes Service) to Parseable.

## Overview

Integrate Amazon EKS with Parseable to:

* **Kubernetes Logs** - Collect pod and container logs
* **AWS Integration** - Native AWS ecosystem support
* **Scalable Collection** - Handle large cluster deployments
* **Rich Metadata** - Include Kubernetes context

## Prerequisites

* Amazon EKS cluster
* kubectl configured
* Helm (recommended)
* Parseable instance accessible from EKS

## Method 1: Fluent Bit DaemonSet

Deploy Fluent Bit as a DaemonSet for log collection.

### Install with Helm

```bash
helm repo add fluent https://fluent.github.io/helm-charts
helm repo update

helm install fluent-bit fluent/fluent-bit \
  --namespace logging \
  --create-namespace \
  --set config.outputs="[OUTPUT]\n    Name http\n    Match *\n    Host parseable.example.com\n    Port 8000\n    URI /api/v1/ingest\n    Format json\n    Header Authorization Basic YWRtaW46YWRtaW4=\n    Header X-P-Stream eks-logs"
```

### Custom Values

Create `fluent-bit-values.yaml`:

```yaml
config:
  inputs: |
    [INPUT]
        Name tail
        Path /var/log/containers/*.log
        Parser cri
        Tag kube.*
        Mem_Buf_Limit 5MB
        Skip_Long_Lines On

  filters: |
    [FILTER]
        Name kubernetes
        Match kube.*
        Merge_Log On
        Keep_Log Off
        K8S-Logging.Parser On
        K8S-Logging.Exclude On

  outputs: |
    [OUTPUT]
        Name http
        Match *
        Host parseable.example.com
        Port 8000
        URI /api/v1/ingest
        Format json
        Header Authorization Basic YWRtaW46YWRtaW4=
        Header X-P-Stream eks-logs
        tls On
        tls.verify Off

tolerations:
  - operator: Exists
    effect: NoSchedule
```

Install with custom values:

```bash
helm install fluent-bit fluent/fluent-bit \
  --namespace logging \
  --create-namespace \
  -f fluent-bit-values.yaml
```

## Method 2: AWS for Fluent Bit

Use AWS's optimized Fluent Bit distribution.

### DaemonSet Manifest

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluent-bit
  namespace: logging
spec:
  selector:
    matchLabels:
      app: fluent-bit
  template:
    metadata:
      labels:
        app: fluent-bit
    spec:
      serviceAccountName: fluent-bit
      containers:
        - name: fluent-bit
          image: amazon/aws-for-fluent-bit:latest
          volumeMounts:
            - name: varlog
              mountPath: /var/log
            - name: varlibdockercontainers
              mountPath: /var/lib/docker/containers
              readOnly: true
            - name: config
              mountPath: /fluent-bit/etc/
          env:
            - name: PARSEABLE_HOST
              value: "parseable.example.com"
            - name: PARSEABLE_AUTH
              valueFrom:
                secretKeyRef:
                  name: parseable-credentials
                  key: auth
      volumes:
        - name: varlog
          hostPath:
            path: /var/log
        - name: varlibdockercontainers
          hostPath:
            path: /var/lib/docker/containers
        - name: config
          configMap:
            name: fluent-bit-config
      tolerations:
        - operator: Exists
          effect: NoSchedule
```

### ConfigMap

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: fluent-bit-config
  namespace: logging
data:
  fluent-bit.conf: |
    [SERVICE]
        Flush         5
        Log_Level     info
        Parsers_File  parsers.conf

    [INPUT]
        Name              tail
        Path              /var/log/containers/*.log
        Parser            cri
        Tag               kube.*
        Refresh_Interval  5
        Mem_Buf_Limit     50MB
        Skip_Long_Lines   On

    [FILTER]
        Name                kubernetes
        Match               kube.*
        Kube_URL            https://kubernetes.default.svc:443
        Kube_CA_File        /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
        Kube_Token_File     /var/run/secrets/kubernetes.io/serviceaccount/token
        Merge_Log           On
        K8S-Logging.Parser  On

    [OUTPUT]
        Name            http
        Match           *
        Host            ${PARSEABLE_HOST}
        Port            8000
        URI             /api/v1/ingest
        Format          json
        Header          Authorization Basic ${PARSEABLE_AUTH}
        Header          X-P-Stream eks-logs
        tls             On

  parsers.conf: |
    [PARSER]
        Name        cri
        Format      regex
        Regex       ^(?<time>[^ ]+) (?<dataset>stdout|stderr) (?<logtag>[^ ]*) (?<log>.*)$
        Time_Key    time
        Time_Format %Y-%m-%dT%H:%M:%S.%L%z
```

## Method 3: OpenTelemetry Collector

Deploy OTel Collector for comprehensive telemetry.

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: otel-collector
  namespace: logging
spec:
  selector:
    matchLabels:
      app: otel-collector
  template:
    spec:
      containers:
        - name: collector
          image: otel/opentelemetry-collector-contrib:latest
          volumeMounts:
            - name: config
              mountPath: /etc/otelcol
            - name: varlog
              mountPath: /var/log
              readOnly: true
      volumes:
        - name: config
          configMap:
            name: otel-collector-config
        - name: varlog
          hostPath:
            path: /var/log
```

## IRSA Configuration

Use IAM Roles for Service Accounts:

```bash
eksctl create iamserviceaccount \
  --name fluent-bit \
  --namespace logging \
  --cluster my-cluster \
  --attach-policy-arn arn:aws:iam::aws:policy/CloudWatchLogsFullAccess \
  --approve
```

## Best Practices

1. **Use DaemonSet** - Ensure logs from all nodes
2. **Add K8s Metadata** - Include pod, namespace, labels
3. **Configure Tolerations** - Run on all nodes
4. **Use IRSA** - Secure credential management
5. **Monitor Collector** - Watch for backpressure

## Troubleshooting

### Missing Logs

1. Check Fluent Bit pod logs
2. Verify log paths are correct
3. Check RBAC permissions
4. Verify Parseable connectivity

### High Resource Usage

1. Adjust buffer limits
2. Filter unnecessary logs
3. Increase flush interval

## Next Steps

* Configure [Google GKE](/docs/ingest-data/containers/google-gke) for multi-cloud
* Set up [alerts](/docs/user-guide/alerting) for Kubernetes events
* Create [dashboards](/docs/user-guide/dashboards) for cluster monitoring


# Azure AKS (/docs/ingest-data/containers/azure-aks)



Collect and forward logs from Azure AKS to Parseable.

## Overview

Integrate Azure AKS with Parseable to:

* **Kubernetes Logs** - Collect pod and container logs
* **Azure Integration** - Native Azure ecosystem support
* **Managed Identity** - Secure credential management
* **Rich Metadata** - Include Azure and K8s context

## Prerequisites

* AKS cluster running
* kubectl configured
* Helm (recommended)
* Parseable instance accessible from AKS

## Method 1: Fluent Bit DaemonSet

Deploy Fluent Bit for log collection.

### Install with Helm

```bash
helm repo add fluent https://fluent.github.io/helm-charts
helm repo update

helm install fluent-bit fluent/fluent-bit \
  --namespace logging \
  --create-namespace \
  -f fluent-bit-values.yaml
```

### Values File

```yaml
config:
  inputs: |
    [INPUT]
        Name tail
        Path /var/log/containers/*.log
        Parser cri
        Tag kube.*
        Mem_Buf_Limit 5MB

  filters: |
    [FILTER]
        Name kubernetes
        Match kube.*
        Merge_Log On
        Keep_Log Off
        K8S-Logging.Parser On

    [FILTER]
        Name modify
        Match *
        Add cloud.provider azure
        Add cluster.name ${CLUSTER_NAME}

  outputs: |
    [OUTPUT]
        Name http
        Match *
        Host parseable.example.com
        Port 8000
        URI /api/v1/ingest
        Format json
        Header Authorization Basic YWRtaW46YWRtaW4=
        Header X-P-Stream aks-logs
        tls On

env:
  - name: CLUSTER_NAME
    value: "my-aks-cluster"

tolerations:
  - operator: Exists
    effect: NoSchedule
```

## Method 2: Azure Monitor Export

Export from Azure Monitor to Event Hubs, then to Parseable.

### Enable Diagnostic Settings

```bash
az monitor diagnostic-settings create \
  --name aks-to-eventhub \
  --resource /subscriptions/.../resourceGroups/.../providers/Microsoft.ContainerService/managedClusters/my-cluster \
  --event-hub-rule /subscriptions/.../resourceGroups/.../providers/Microsoft.EventHub/namespaces/.../authorizationRules/RootManageSharedAccessKey \
  --logs '[{"category": "kube-apiserver", "enabled": true}, {"category": "kube-controller-manager", "enabled": true}]'
```

Then use [Azure Event Hubs integration](/docs/ingest-data/cloud/azure-event-hubs) to forward to Parseable.

## Method 3: OpenTelemetry Collector

### Collector DaemonSet

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: otel-collector
  namespace: logging
spec:
  selector:
    matchLabels:
      app: otel-collector
  template:
    metadata:
      labels:
        app: otel-collector
    spec:
      containers:
        - name: collector
          image: otel/opentelemetry-collector-contrib:latest
          volumeMounts:
            - name: config
              mountPath: /etc/otelcol
            - name: varlog
              mountPath: /var/log
              readOnly: true
          env:
            - name: PARSEABLE_AUTH
              valueFrom:
                secretKeyRef:
                  name: parseable-credentials
                  key: auth
      volumes:
        - name: config
          configMap:
            name: otel-collector-config
        - name: varlog
          hostPath:
            path: /var/log
      tolerations:
        - operator: Exists
          effect: NoSchedule
```

## Azure Workload Identity

Use Workload Identity for secure authentication:

### Enable Workload Identity

```bash
az aks update \
  --resource-group myResourceGroup \
  --name myAKSCluster \
  --enable-oidc-issuer \
  --enable-workload-identity
```

### Create Managed Identity

```bash
az identity create \
  --name fluent-bit-identity \
  --resource-group myResourceGroup

# Get client ID
CLIENT_ID=$(az identity show --name fluent-bit-identity --resource-group myResourceGroup --query clientId -o tsv)
```

### Kubernetes Service Account

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: fluent-bit
  namespace: logging
  annotations:
    azure.workload.identity/client-id: ${CLIENT_ID}
  labels:
    azure.workload.identity/use: "true"
```

## Best Practices

1. **Use Workload Identity** - Secure credential management
2. **Add Azure Metadata** - Include subscription, resource group
3. **Filter System Logs** - Exclude kube-system if needed
4. **Monitor Resources** - Watch collector resource usage
5. **Use Labels** - Leverage AKS labels for filtering

## Troubleshooting

### Permission Denied

1. Verify Workload Identity configuration
2. Check managed identity permissions
3. Verify RBAC configuration

### Missing Logs

1. Check collector pod logs
2. Verify log paths
3. Check network policies
4. Verify AKS node pools

## Next Steps

* Configure [Amazon EKS](/docs/ingest-data/containers/amazon-eks) for multi-cloud
* Set up [alerts](/docs/user-guide/alerting) for AKS events
* Create [dashboards](/docs/user-guide/dashboards) for cluster monitoring


# Docker (/docs/ingest-data/containers/docker)



Collect and forward logs from Docker containers to Parseable.

## Overview

Integrate Docker with Parseable to:

* **Container Logs** - Collect stdout/stderr from containers
* **Centralized Logging** - Aggregate logs from all containers
* **Real-time Streaming** - Stream logs as they're generated
* **Rich Metadata** - Include container and image information

## Prerequisites

* Docker installed
* Parseable instance accessible
* Fluent Bit or logging driver configured

## Method 1: Fluent Bit Sidecar

Deploy Fluent Bit alongside your containers.

### Docker Compose

```yaml
version: '3.8'
services:
  app:
    image: your-app:latest
    logging:
      driver: fluentd
      options:
        fluentd-address: localhost:24224
        tag: app.logs

  fluent-bit:
    image: fluent/fluent-bit:latest
    ports:
      - "24224:24224"
    volumes:
      - ./fluent-bit.yaml:/fluent-bit/etc/fluent-bit.yaml
    command: ["/fluent-bit/bin/fluent-bit", "-c", "/fluent-bit/etc/fluent-bit.yaml"]
```

### Fluent Bit Configuration

```yaml
service:
  flush: 5
  log_level: info

pipeline:
  inputs:
    - name: forward
      listen: 0.0.0.0
      port: 24224

  outputs:
    - name: http
      match: '*'
      host: parseable
      port: 8000
      uri: /api/v1/ingest
      format: json
      header: Authorization Basic YWRtaW46YWRtaW4=
      header: X-P-Stream docker-logs
```

## Method 2: Docker Log Driver

Use Docker's built-in logging drivers.

### Fluentd Driver

```yaml
version: '3.8'
services:
  app:
    image: your-app:latest
    logging:
      driver: fluentd
      options:
        fluentd-address: "fluent-bit:24224"
        fluentd-async: "true"
        tag: "docker.{{.Name}}"
```

### JSON File Driver with Tail

Collect logs from Docker's default JSON file driver:

```yaml
# fluent-bit.yaml
service:
  flush: 5
  log_level: info

pipeline:
  inputs:
    - name: tail
      path: /var/lib/docker/containers/*/*.log
      parser: docker
      tag: docker.*
      refresh_interval: 5
      mem_buf_limit: 5MB
      skip_long_lines: on

  parsers:
    - name: docker
      format: json
      time_key: time
      time_format: "%Y-%m-%dT%H:%M:%S.%L"

  filters:
    - name: modify
      match: docker.*
      add: source docker

  outputs:
    - name: http
      match: '*'
      host: parseable
      port: 8000
      uri: /api/v1/ingest
      format: json
      header: Authorization Basic YWRtaW46YWRtaW4=
      header: X-P-Stream docker-logs
```

### Docker Compose with Log Collection

```yaml
version: '3.8'
services:
  fluent-bit:
    image: fluent/fluent-bit:latest
    volumes:
      - /var/lib/docker/containers:/var/lib/docker/containers:ro
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - ./fluent-bit.yaml:/fluent-bit/etc/fluent-bit.yaml
    command: ["/fluent-bit/bin/fluent-bit", "-c", "/fluent-bit/etc/fluent-bit.yaml"]

  parseable:
    image: parseable/parseable:latest
    ports:
      - "8000:8000"
    environment:
      - P_USERNAME=admin
      - P_PASSWORD=admin
```

## Method 3: Direct HTTP Logging

Send logs directly from your application.

### Python Example

```python
import logging
import requests
import json
from datetime import datetime

class ParseableHandler(logging.Handler):
    def __init__(self, url, dataset, username, password):
        super().__init__()
        self.url = f"{url}/api/v1/ingest"
        self.dataset = dataset
        self.auth = (username, password)
        self.buffer = []
        self.batch_size = 100

    def emit(self, record):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname.lower(),
            "message": self.format(record),
            "logger": record.name,
            "container": os.environ.get("HOSTNAME", "unknown")
        }
        self.buffer.append(log_entry)
        
        if len(self.buffer) >= self.batch_size:
            self.flush()

    def flush(self):
        if not self.buffer:
            return
        try:
            requests.post(
                self.url,
                json=self.buffer,
                auth=self.auth,
                headers={"X-P-Stream": self.dataset}
            )
        except Exception as e:
            print(f"Failed to send logs: {e}")
        finally:
            self.buffer = []

# Usage
handler = ParseableHandler(
    url="http://parseable:8000",
    dataset="app-logs",
    username="admin",
    password="admin"
)
logging.getLogger().addHandler(handler)
```

## Method 4: Docker Events

Collect Docker daemon events.

### Event Collector Script

```python
#!/usr/bin/env python3
import docker
import requests
import json
from datetime import datetime

PARSEABLE_URL = "http://parseable:8000"
PARSEABLE_AUTH = ("admin", "admin")
STREAM = "docker-events"

client = docker.from_env()

for event in client.events(decode=True):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "event_type": event.get("Type"),
        "action": event.get("Action"),
        "actor_id": event.get("Actor", {}).get("ID"),
        "actor_attributes": event.get("Actor", {}).get("Attributes"),
        "status": event.get("status"),
        "from": event.get("from")
    }
    
    try:
        requests.post(
            f"{PARSEABLE_URL}/api/v1/ingest",
            json=[log_entry],
            auth=PARSEABLE_AUTH,
            headers={"X-P-Stream": STREAM}
        )
    except Exception as e:
        print(f"Error: {e}")
```

## Container Labels

Add metadata using Docker labels:

```yaml
version: '3.8'
services:
  app:
    image: your-app:latest
    labels:
      - "logging.parseable.dataset=app-logs"
      - "logging.parseable.service=my-app"
      - "logging.parseable.environment=production"
```

### Use Labels in Fluent Bit

```yaml
filters:
  - name: modify
    match: docker.*
    add: service ${LABEL_logging.parseable.service}
    add: environment ${LABEL_logging.parseable.environment}
```

## Querying Docker Logs

```sql
-- Recent container logs
SELECT timestamp, container_name, message, level
FROM "docker-logs"
ORDER BY timestamp DESC
LIMIT 100

-- Error logs by container
SELECT container_name, COUNT(*) as error_count
FROM "docker-logs"
WHERE level = 'error'
  AND timestamp > NOW() - INTERVAL '1 hour'
GROUP BY container_name
ORDER BY error_count DESC

-- Container events
SELECT timestamp, event_type, action, actor_id
FROM "docker-events"
ORDER BY timestamp DESC
LIMIT 50
```

## Best Practices

1. **Use Labels** - Add metadata for filtering
2. **Buffer Logs** - Batch logs for efficiency
3. **Handle Backpressure** - Configure memory limits
4. **Monitor Collector** - Watch Fluent Bit health
5. **Rotate Logs** - Configure Docker log rotation

## Troubleshooting

### Missing Logs

1. Verify logging driver is configured
2. Check Fluent Bit is running
3. Verify Parseable endpoint is accessible
4. Check container permissions

### High Memory Usage

1. Configure `mem_buf_limit` in Fluent Bit
2. Enable Docker log rotation
3. Reduce batch sizes

## Next Steps

* Configure [Kubernetes](/docs/ingest-data/containers/kubernetes) for orchestration
* Set up [alerts](/docs/user-guide/alerting) for container events
* Create [dashboards](/docs/user-guide/dashboards) for monitoring


# Google GKE (/docs/ingest-data/containers/google-gke)



Collect and forward logs from Google GKE to Parseable.

## Overview

Integrate Google GKE with Parseable to:

* **Kubernetes Logs** - Collect pod and container logs
* **GCP Integration** - Native Google Cloud support
* **Autopilot Support** - Works with GKE Autopilot
* **Rich Metadata** - Include GCP and K8s context

## Prerequisites

* GKE cluster running
* kubectl configured
* Helm (recommended)
* Parseable instance accessible from GKE

## Method 1: Fluent Bit DaemonSet

Deploy Fluent Bit for log collection.

### Install with Helm

```bash
helm repo add fluent https://fluent.github.io/helm-charts
helm repo update

helm install fluent-bit fluent/fluent-bit \
  --namespace logging \
  --create-namespace \
  -f fluent-bit-values.yaml
```

### Values File

```yaml
config:
  inputs: |
    [INPUT]
        Name tail
        Path /var/log/containers/*.log
        Parser cri
        Tag kube.*
        Mem_Buf_Limit 5MB

  filters: |
    [FILTER]
        Name kubernetes
        Match kube.*
        Merge_Log On
        Keep_Log Off
        K8S-Logging.Parser On

    [FILTER]
        Name modify
        Match *
        Add cloud.provider gcp
        Add cluster.name ${CLUSTER_NAME}

  outputs: |
    [OUTPUT]
        Name http
        Match *
        Host parseable.example.com
        Port 8000
        URI /api/v1/ingest
        Format json
        Header Authorization Basic YWRtaW46YWRtaW4=
        Header X-P-Stream gke-logs
        tls On

env:
  - name: CLUSTER_NAME
    value: "my-gke-cluster"

tolerations:
  - operator: Exists
    effect: NoSchedule
```

## Method 2: Google Cloud Logging Export

Export from Cloud Logging to Pub/Sub, then to Parseable.

### Create Log Sink

```bash
gcloud logging sinks create gke-to-pubsub \
  pubsub.googleapis.com/projects/PROJECT_ID/topics/gke-logs \
  --log-filter='resource.type="k8s_container"'
```

Then use [GCP Pub/Sub integration](/docs/ingest-data/cloud/gcp-pubsub) to forward to Parseable.

## Method 3: OpenTelemetry Collector

### Collector Configuration

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: otel-collector-config
data:
  config.yaml: |
    receivers:
      filelog:
        include: [/var/log/containers/*.log]
        operators:
          - type: regex_parser
            regex: '^(?P<time>[^ ]+) (?P<dataset>stdout|stderr) (?P<logtag>[^ ]*) (?P<log>.*)$'
            timestamp:
              parse_from: attributes.time
              layout: '%Y-%m-%dT%H:%M:%S.%LZ'

    processors:
      k8sattributes:
        extract:
          metadata:
            - k8s.pod.name
            - k8s.namespace.name
            - k8s.deployment.name
      batch:
        timeout: 10s

    exporters:
      otlphttp:
        endpoint: "http://parseable:8000"
        headers:
          Authorization: "Basic YWRtaW46YWRtaW4="
          X-P-Stream: "gke-logs"

    service:
      pipelines:
        logs:
          receivers: [filelog]
          processors: [k8sattributes, batch]
          exporters: [otlphttp]
```

## Workload Identity

Use Workload Identity for secure authentication:

```bash
# Create GCP service account
gcloud iam service-accounts create fluent-bit-sa

# Grant permissions
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:fluent-bit-sa@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/logging.viewer"

# Bind to Kubernetes service account
gcloud iam service-accounts add-iam-policy-binding \
  fluent-bit-sa@PROJECT_ID.iam.gserviceaccount.com \
  --role="roles/iam.workloadIdentityUser" \
  --member="serviceAccount:PROJECT_ID.svc.id.goog[logging/fluent-bit]"
```

### Kubernetes Service Account

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: fluent-bit
  namespace: logging
  annotations:
    iam.gke.io/gcp-service-account: fluent-bit-sa@PROJECT_ID.iam.gserviceaccount.com
```

## GKE Autopilot

For Autopilot clusters, use Cloud Logging export method as DaemonSets are not supported.

## Best Practices

1. **Use Workload Identity** - Secure credential management
2. **Add GCP Metadata** - Include project, cluster info
3. **Filter Logs** - Exclude system namespaces if needed
4. **Monitor Resources** - Watch collector resource usage
5. **Use Labels** - Leverage GKE labels for filtering

## Troubleshooting

### Permission Denied

1. Verify Workload Identity binding
2. Check service account permissions
3. Verify RBAC configuration

### Missing Logs

1. Check collector pod logs
2. Verify log paths
3. Check network policies

## Next Steps

* Configure [Azure AKS](/docs/ingest-data/containers/azure-aks) for multi-cloud
* Set up [alerts](/docs/user-guide/alerting) for GKE events
* Create [dashboards](/docs/user-guide/dashboards) for cluster monitoring


# Kubernetes (/docs/ingest-data/containers/kubernetes)



Collect and forward logs from Kubernetes clusters to Parseable.

## Overview

Integrate Kubernetes with Parseable to:

* **Pod Logs** - Collect logs from all pods
* **Cluster Events** - Monitor Kubernetes events
* **Rich Metadata** - Include pod, namespace, and label information
* **Centralized Observability** - Unified view of cluster logs

## Prerequisites

* Kubernetes cluster
* kubectl configured
* Helm (recommended)
* Parseable instance accessible from cluster

## Method 1: Fluent Bit DaemonSet

Deploy Fluent Bit as a DaemonSet for cluster-wide log collection.

### Install with Helm

```bash
helm repo add fluent https://fluent.github.io/helm-charts
helm repo update

helm install fluent-bit fluent/fluent-bit \
  --namespace logging \
  --create-namespace \
  -f fluent-bit-values.yaml
```

### Fluent Bit Values

```yaml
# fluent-bit-values.yaml
config:
  service: |
    [SERVICE]
        Flush         5
        Log_Level     info
        Daemon        off
        Parsers_File  /fluent-bit/etc/parsers.conf
        HTTP_Server   On
        HTTP_Listen   0.0.0.0
        HTTP_Port     2020

  inputs: |
    [INPUT]
        Name              tail
        Path              /var/log/containers/*.log
        Parser            cri
        Tag               kube.*
        Mem_Buf_Limit     50MB
        Skip_Long_Lines   On
        Refresh_Interval  10

  filters: |
    [FILTER]
        Name                kubernetes
        Match               kube.*
        Kube_URL            https://kubernetes.default.svc:443
        Kube_CA_File        /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
        Kube_Token_File     /var/run/secrets/kubernetes.io/serviceaccount/token
        Kube_Tag_Prefix     kube.var.log.containers.
        Merge_Log           On
        Merge_Log_Key       log_processed
        K8S-Logging.Parser  On
        K8S-Logging.Exclude Off
        Labels              On
        Annotations         Off

    [FILTER]
        Name          nest
        Match         kube.*
        Operation     lift
        Nested_under  kubernetes
        Add_prefix    k8s_

  outputs: |
    [OUTPUT]
        Name            http
        Match           kube.*
        Host            parseable.parseable.svc.cluster.local
        Port            8000
        URI             /api/v1/ingest
        Format          json
        Header          Authorization Basic YWRtaW46YWRtaW4=
        Header          X-P-Stream k8s-logs
        tls             Off
        Retry_Limit     5

  customParsers: |
    [PARSER]
        Name        cri
        Format      regex
        Regex       ^(?<time>[^ ]+) (?<dataset>stdout|stderr) (?<logtag>[^ ]*) (?<log>.*)$
        Time_Key    time
        Time_Format %Y-%m-%dT%H:%M:%S.%L%z

tolerations:
  - key: node-role.kubernetes.io/master
    operator: Exists
    effect: NoSchedule
  - key: node-role.kubernetes.io/control-plane
    operator: Exists
    effect: NoSchedule

resources:
  limits:
    cpu: 100m
    memory: 128Mi
  requests:
    cpu: 50m
    memory: 64Mi
```

## Method 2: OpenTelemetry Collector

Deploy OTel Collector for comprehensive telemetry.

### Collector DaemonSet

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: otel-collector
  namespace: logging
spec:
  selector:
    matchLabels:
      app: otel-collector
  template:
    metadata:
      labels:
        app: otel-collector
    spec:
      serviceAccountName: otel-collector
      containers:
        - name: collector
          image: otel/opentelemetry-collector-contrib:latest
          args:
            - --config=/etc/otelcol/config.yaml
          volumeMounts:
            - name: config
              mountPath: /etc/otelcol
            - name: varlog
              mountPath: /var/log
              readOnly: true
            - name: varlibdockercontainers
              mountPath: /var/lib/docker/containers
              readOnly: true
          resources:
            limits:
              cpu: 200m
              memory: 256Mi
      volumes:
        - name: config
          configMap:
            name: otel-collector-config
        - name: varlog
          hostPath:
            path: /var/log
        - name: varlibdockercontainers
          hostPath:
            path: /var/lib/docker/containers
      tolerations:
        - operator: Exists
          effect: NoSchedule
```

### OTel Collector ConfigMap

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: otel-collector-config
  namespace: logging
data:
  config.yaml: |
    receivers:
      filelog:
        include:
          - /var/log/containers/*.log
        exclude:
          - /var/log/containers/otel-collector*.log
        operators:
          - type: router
            id: get-format
            routes:
              - output: parser-cri
                expr: 'body matches "^[^ Z]+ "'
          - type: regex_parser
            id: parser-cri
            regex: '^(?P<time>[^ Z]+) (?P<dataset>stdout|stderr) (?P<logtag>[^ ]*) ?(?P<log>.*)$'
            timestamp:
              parse_from: attributes.time
              layout: '%Y-%m-%dT%H:%M:%S.%LZ'

    processors:
      k8sattributes:
        extract:
          metadata:
            - k8s.pod.name
            - k8s.pod.uid
            - k8s.namespace.name
            - k8s.node.name
            - k8s.deployment.name
            - k8s.container.name
        pod_association:
          - sources:
              - from: resource_attribute
                name: k8s.pod.uid
      batch:
        timeout: 10s
        send_batch_size: 1000

    exporters:
      otlphttp:
        endpoint: "http://parseable.parseable.svc.cluster.local:8000"
        headers:
          Authorization: "Basic YWRtaW46YWRtaW4="
          X-P-Stream: "k8s-logs"
          X-P-Log-Source: "otel-logs"

    service:
      pipelines:
        logs:
          receivers: [filelog]
          processors: [k8sattributes, batch]
          exporters: [otlphttp]
```

### RBAC Configuration

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: otel-collector
  namespace: logging
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: otel-collector
rules:
  - apiGroups: [""]
    resources: ["pods", "namespaces", "nodes"]
    verbs: ["get", "watch", "list"]
  - apiGroups: ["apps"]
    resources: ["replicasets", "deployments"]
    verbs: ["get", "watch", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: otel-collector
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: otel-collector
subjects:
  - kind: ServiceAccount
    name: otel-collector
    namespace: logging
```

## Method 3: Kubernetes Events

Collect Kubernetes events for cluster monitoring.

### Event Exporter

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: k8s-event-exporter
  namespace: logging
spec:
  replicas: 1
  selector:
    matchLabels:
      app: k8s-event-exporter
  template:
    metadata:
      labels:
        app: k8s-event-exporter
    spec:
      serviceAccountName: event-exporter
      containers:
        - name: exporter
          image: bitnami/kubectl:latest
          command:
            - /bin/bash
            - -c
            - |
              while true; do
                kubectl get events -A --watch -o json | while read event; do
                  curl -s -X POST "http://parseable.parseable.svc.cluster.local:8000/api/v1/ingest" \
                    -H "Authorization: Basic YWRtaW46YWRtaW4=" \
                    -H "X-P-Stream: k8s-events" \
                    -H "Content-Type: application/json" \
                    -d "[${event}]" || true
                done
                sleep 5
              done
```

### Event Exporter RBAC

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: event-exporter
  namespace: logging
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: event-exporter
rules:
  - apiGroups: [""]
    resources: ["events"]
    verbs: ["get", "watch", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: event-exporter
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: event-exporter
subjects:
  - kind: ServiceAccount
    name: event-exporter
    namespace: logging
```

## Deploy Parseable on Kubernetes

### Helm Installation

```bash
helm repo add parseable https://charts.parseable.com
helm repo update

helm install parseable parseable/parseable \
  --namespace parseable \
  --create-namespace \
  --set parseable.username=admin \
  --set parseable.password=admin
```

### Basic Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: parseable
  namespace: parseable
spec:
  replicas: 1
  selector:
    matchLabels:
      app: parseable
  template:
    metadata:
      labels:
        app: parseable
    spec:
      containers:
        - name: parseable
          image: parseable/parseable:latest
          ports:
            - containerPort: 8000
          env:
            - name: P_USERNAME
              value: "admin"
            - name: P_PASSWORD
              value: "admin"
          resources:
            limits:
              cpu: "1"
              memory: 2Gi
            requests:
              cpu: 500m
              memory: 1Gi
---
apiVersion: v1
kind: Service
metadata:
  name: parseable
  namespace: parseable
spec:
  selector:
    app: parseable
  ports:
    - port: 8000
      targetPort: 8000
```

## Namespace Filtering

Filter logs by namespace:

```yaml
# In Fluent Bit config
filters: |
  [FILTER]
      Name    grep
      Match   kube.*
      Exclude $kubernetes['namespace_name'] kube-system

  [FILTER]
      Name    grep
      Match   kube.*
      Exclude $kubernetes['namespace_name'] logging
```

## Querying Kubernetes Logs

```sql
-- Recent pod logs
SELECT timestamp, k8s_namespace_name, k8s_pod_name, log
FROM "k8s-logs"
ORDER BY timestamp DESC
LIMIT 100

-- Errors by namespace
SELECT 
  k8s_namespace_name,
  COUNT(*) as error_count
FROM "k8s-logs"
WHERE log LIKE '%error%' OR log LIKE '%ERROR%'
  AND timestamp > NOW() - INTERVAL '1 hour'
GROUP BY k8s_namespace_name
ORDER BY error_count DESC

-- Pod restarts (from events)
SELECT timestamp, involvedObject_name, reason, message
FROM "k8s-events"
WHERE reason = 'Restarted' OR reason = 'BackOff'
ORDER BY timestamp DESC

-- Logs from specific deployment
SELECT timestamp, k8s_pod_name, log
FROM "k8s-logs"
WHERE k8s_deployment_name = 'my-app'
ORDER BY timestamp DESC
LIMIT 100
```

## Best Practices

1. **Use DaemonSet** - Ensure logs from all nodes
2. **Add Tolerations** - Run on master/control-plane nodes
3. **Filter System Logs** - Exclude kube-system if noisy
4. **Resource Limits** - Set appropriate limits for collectors
5. **Use Labels** - Leverage Kubernetes labels for filtering
6. **Monitor Collectors** - Watch for backpressure and errors

## Troubleshooting

### Missing Logs

1. Check DaemonSet pods are running on all nodes
2. Verify RBAC permissions
3. Check log file paths are correct
4. Verify Parseable service is accessible

### High Resource Usage

1. Increase `Mem_Buf_Limit`
2. Add namespace exclusions
3. Reduce `Refresh_Interval`
4. Enable log sampling

### Permission Denied

1. Verify ServiceAccount exists
2. Check ClusterRole and ClusterRoleBinding
3. Verify pod security policies

## Next Steps

* Configure [Amazon EKS](/docs/ingest-data/containers/amazon-eks) for AWS
* Configure [Google GKE](/docs/ingest-data/containers/google-gke) for GCP
* Configure [Azure AKS](/docs/ingest-data/containers/azure-aks) for Azure
* Set up [alerts](/docs/user-guide/alerting) for cluster events
* Create [dashboards](/docs/user-guide/dashboards) for monitoring


# Elasticsearch (/docs/ingest-data/databases/elasticsearch)



Migrate your log data and workflows from Elasticsearch to Parseable.

## Overview

Migrate from Elasticsearch to Parseable to:

* **Reduce Costs** - Lower storage and operational costs
* **Simplify Operations** - No cluster management
* **Faster Queries** - Optimized for log analytics
* **Native SQL** - Use familiar SQL syntax

## Migration Strategies

### Strategy 1: Parallel Ingestion

Run both systems in parallel during migration.

```
Log Sources → [Fluent Bit] → Elasticsearch
                          → Parseable
```

### Strategy 2: Historical Export

Export historical data from Elasticsearch to Parseable.

### Strategy 3: Cut-over

Switch log ingestion from Elasticsearch to Parseable.

## Parallel Ingestion Setup

### Fluent Bit Configuration

```yaml
service:
  flush: 5
  log_level: info

pipeline:
  inputs:
    - name: tail
      path: /var/log/*.log
      tag: logs

  outputs:
    # Continue sending to Elasticsearch
    - name: es
      match: '*'
      host: elasticsearch
      port: 9200
      index: logs
      type: _doc

    # Also send to Parseable
    - name: http
      match: '*'
      host: parseable
      port: 8000
      uri: /api/v1/ingest
      format: json
      header: Authorization Basic YWRtaW46YWRtaW4=
      header: X-P-Stream application-logs
```

## Historical Data Export

### Using Elasticdump

Export data from Elasticsearch:

```bash
# Install elasticdump
npm install -g elasticdump

# Export to JSON
elasticdump \
  --input=http://elasticsearch:9200/logs \
  --output=/tmp/logs.json \
  --type=data \
  --limit=10000
```

### Import to Parseable

```python
import json
import requests
from datetime import datetime

PARSEABLE_URL = "http://parseable:8000"
PARSEABLE_AUTH = ("admin", "admin")
STREAM = "elasticsearch-import"

def import_to_parseable(file_path):
    batch = []
    batch_size = 1000
    
    with open(file_path, 'r') as f:
        for line in f:
            doc = json.loads(line)
            source = doc.get('_source', doc)
            
            # Transform Elasticsearch document
            log_entry = {
                'timestamp': source.get('@timestamp', datetime.utcnow().isoformat() + 'Z'),
                'message': source.get('message', ''),
                'level': source.get('level', source.get('log.level', 'info')),
                **{k: v for k, v in source.items() if k not in ['@timestamp', 'message', 'level']}
            }
            
            batch.append(log_entry)
            
            if len(batch) >= batch_size:
                send_batch(batch)
                batch = []
        
        if batch:
            send_batch(batch)

def send_batch(batch):
    response = requests.post(
        f"{PARSEABLE_URL}/api/v1/ingest",
        json=batch,
        auth=PARSEABLE_AUTH,
        headers={'X-P-Stream': STREAM}
    )
    response.raise_for_status()
    print(f"Imported {len(batch)} documents")

import_to_parseable('/tmp/logs.json')
```

## Query Migration

### Elasticsearch to SQL

| Elasticsearch                                    | Parseable SQL                                   |
| ------------------------------------------------ | ----------------------------------------------- |
| `match: { message: "error" }`                    | `WHERE message LIKE '%error%'`                  |
| `term: { level: "error" }`                       | `WHERE level = 'error'`                         |
| `range: { @timestamp: { gte: "now-1h" } }`       | `WHERE p_timestamp > NOW() - INTERVAL '1 hour'` |
| `aggs: { count: { terms: { field: "level" } } }` | `SELECT level, COUNT(*) GROUP BY level`         |

### Example Queries

**Elasticsearch:**

```json
{
  "query": {
    "bool": {
      "must": [
        { "match": { "level": "error" } },
        { "range": { "@timestamp": { "gte": "now-24h" } } }
      ]
    }
  },
  "aggs": {
    "by_service": {
      "terms": { "field": "service.keyword" }
    }
  }
}
```

**Parseable SQL:**

```sql
SELECT service, COUNT(*) as error_count
FROM "application-logs"
WHERE level = 'error'
  AND p_timestamp > NOW() - INTERVAL '24 hours'
GROUP BY service
ORDER BY error_count DESC
```

## Index Pattern to Stream Mapping

| Elasticsearch Index | Parseable Stream   |
| ------------------- | ------------------ |
| `logs-*`            | `application-logs` |
| `nginx-*`           | `nginx-logs`       |
| `kubernetes-*`      | `k8s-logs`         |

## Kibana to Parseable Dashboard

### Visualization Mapping

| Kibana   | Parseable  |
| -------- | ---------- |
| Discover | SQL Editor |
| Lens     | Dashboards |
| Canvas   | Dashboards |
| Alerts   | Alerts     |

### Recreate Dashboards

1. Export Kibana dashboard JSON
2. Map visualizations to Parseable queries
3. Create equivalent dashboards in Parseable or Grafana

## Logstash to Fluent Bit

### Logstash Config

```ruby
input {
  beats { port => 5044 }
}
filter {
  grok { match => { "message" => "%{COMBINEDAPACHELOG}" } }
}
output {
  elasticsearch { hosts => ["elasticsearch:9200"] }
}
```

### Equivalent Fluent Bit

```yaml
pipeline:
  inputs:
    - name: tcp
      listen: 0.0.0.0
      port: 5044
      format: json

  filters:
    - name: parser
      match: '*'
      key_name: message
      parser: apache

  outputs:
    - name: http
      match: '*'
      host: parseable
      port: 8000
      uri: /api/v1/ingest
      format: json
      header: Authorization Basic YWRtaW46YWRtaW4=
      header: X-P-Stream apache-logs
```

## Best Practices

1. **Run Parallel First** - Validate data before switching
2. **Map Fields** - Document field mappings
3. **Test Queries** - Verify query results match
4. **Migrate Gradually** - Start with non-critical logs
5. **Update Dashboards** - Recreate visualizations

## Troubleshooting

### Data Mismatch

1. Compare document counts
2. Verify field mappings
3. Check timestamp formats

### Query Differences

1. Elasticsearch full-text vs SQL LIKE
2. Aggregation syntax differences
3. Time zone handling

## Next Steps

* Set up [alerts](/docs/user-guide/alerting) in Parseable
* Create [dashboards](/docs/user-guide/dashboards) for monitoring
* Configure [Grafana](/docs/integrations/visualization/grafana) for visualization


# MongoDB (/docs/ingest-data/databases/mongodb)



Monitor your MongoDB databases by collecting metrics using the OpenTelemetry Collector and sending them to Parseable.

## Overview

The OpenTelemetry Collector's MongoDB receiver collects metrics from standalone MongoDB clusters including:

* **Server Statistics** - Connections, operations, network traffic
* **Database Metrics** - Document counts, storage sizes
* **Collection Metrics** - Index usage, document operations
* **Replication Metrics** - Replica set status and lag

## Prerequisites

* MongoDB 4.0+ (supports 4.0, 5.0, 6.0, 7.0)
* OpenTelemetry Collector with `mongodb` receiver
* Parseable instance running and accessible

### Database User Setup

Create a monitoring user with the `clusterMonitor` role:

```javascript
// Connect to admin database
use admin

// Create monitoring user
db.createUser({
  user: "otel",
  pwd: "your-secure-password",
  roles: [
    { role: "clusterMonitor", db: "admin" },
    { role: "read", db: "local" }
  ]
})
```

## OpenTelemetry Collector Configuration

### Basic Configuration

Create an `otel-collector-config.yaml` file:

```yaml
receivers:
  mongodb:
    hosts:
      - endpoint: localhost:27017
    username: otel
    password: ${env:MONGODB_PASSWORD}
    collection_interval: 60s
    initial_delay: 1s
    tls:
      insecure: true

exporters:
  otlphttp/parseable:
    endpoint: "http://parseable:8000"
    headers:
      Authorization: "Basic YWRtaW46YWRtaW4="
      X-P-Stream: "mongodb-metrics"
      X-P-Log-Source: "otel-metrics"
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      receivers: [mongodb]
      exporters: [otlphttp/parseable]
```

### Replica Set Configuration

For monitoring MongoDB replica sets:

```yaml
receivers:
  mongodb:
    hosts:
      - endpoint: mongo1:27017
      - endpoint: mongo2:27017
      - endpoint: mongo3:27017
    username: otel
    password: ${env:MONGODB_PASSWORD}
    replica_set: rs0
    collection_interval: 60s
    timeout: 1m
    tls:
      insecure: false
      insecure_skip_verify: false
      ca_file: /path/to/ca.crt

exporters:
  otlphttp/parseable:
    endpoint: "http://parseable:8000"
    headers:
      Authorization: "Basic YWRtaW46YWRtaW4="
      X-P-Stream: "mongodb-metrics"
      X-P-Log-Source: "otel-metrics"
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      receivers: [mongodb]
      exporters: [otlphttp/parseable]
```

## Configuration Options

| Parameter             | Default           | Description                        |
| --------------------- | ----------------- | ---------------------------------- |
| `hosts`               | `localhost:27017` | List of MongoDB endpoints          |
| `username`            | -                 | Database username                  |
| `password`            | -                 | Database password                  |
| `replica_set`         | -                 | Replica set name for autodiscovery |
| `collection_interval` | `1m`              | Metrics collection interval        |
| `timeout`             | `1m`              | Command timeout                    |
| `direct_connection`   | `false`           | Disable autodiscovery              |
| `tls.insecure`        | -                 | Disable TLS                        |

## Collected Metrics

The MongoDB receiver collects the following metrics:

| Metric                             | Description               |
| ---------------------------------- | ------------------------- |
| `mongodb.cache.operations`         | Cache operations count    |
| `mongodb.collection.count`         | Number of collections     |
| `mongodb.connection.count`         | Active connections        |
| `mongodb.cursor.count`             | Open cursors              |
| `mongodb.cursor.timeout.count`     | Timed out cursors         |
| `mongodb.database.count`           | Number of databases       |
| `mongodb.document.operation.count` | Document operations       |
| `mongodb.global_lock.time`         | Global lock time          |
| `mongodb.index.count`              | Number of indexes         |
| `mongodb.index.size`               | Index size in bytes       |
| `mongodb.memory.usage`             | Memory usage              |
| `mongodb.network.io.receive`       | Network bytes received    |
| `mongodb.network.io.transmit`      | Network bytes transmitted |
| `mongodb.operation.count`          | Operation counts by type  |
| `mongodb.storage.size`             | Storage size in bytes     |

## Running the Collector

### Docker

```bash
docker run -d \
  --name otel-collector \
  -v $(pwd)/otel-collector-config.yaml:/etc/otelcol/config.yaml \
  -e MONGODB_PASSWORD=your-password \
  otel/opentelemetry-collector-contrib:latest
```

### Docker Compose

```yaml
version: '3.8'
services:
  otel-collector:
    image: otel/opentelemetry-collector-contrib:latest
    volumes:
      - ./otel-collector-config.yaml:/etc/otelcol/config.yaml
    environment:
      - MONGODB_PASSWORD=${MONGODB_PASSWORD}
    depends_on:
      - mongodb
      - parseable
```

## Querying MongoDB Metrics in Parseable

Once data is flowing, query your MongoDB metrics:

```sql
-- Get connection counts over time
SELECT p_timestamp, connection_count 
FROM "mongodb-metrics" 
ORDER BY p_timestamp DESC 
LIMIT 100

-- Find databases with high storage usage
SELECT database_name, storage_size, index_size
FROM "mongodb-metrics"
WHERE p_timestamp > NOW() - INTERVAL '1 hour'
ORDER BY storage_size DESC
```

## Troubleshooting

### Connection Issues

If the collector can't connect to MongoDB:

1. Verify MongoDB is accepting connections on the configured port
2. Check the user has `clusterMonitor` role
3. Verify authentication database is correct (usually `admin`)
4. Check firewall rules allow the connection

### Missing Metrics

If some metrics are not appearing:

1. Ensure the monitoring user has proper roles
2. Verify the replica set name is correct (if using replica sets)
3. Check timeout settings if MongoDB is slow to respond

## Next Steps

* Set up [alerts](/docs/user-guide/alerting) for database performance thresholds
* Create [dashboards](/docs/user-guide/dashboards) for MongoDB monitoring
* Explore [SQL queries](/docs/user-guide/sql-editor) for custom analysis


# MySQL (/docs/ingest-data/databases/mysql)



Monitor your MySQL databases by collecting metrics and logs using the OpenTelemetry Collector and sending them to Parseable.

## Overview

The OpenTelemetry Collector's MySQL receiver collects metrics from MySQL and MariaDB databases including:

* **Server Statistics** - Connections, queries, threads
* **InnoDB Metrics** - Buffer pool, row operations, locks
* **Query Performance** - Statement events, query samples
* **Replication Status** - Slave lag and replication metrics

## Prerequisites

* MySQL 8.0+ or MariaDB 10.11+
* OpenTelemetry Collector with `mysql` receiver
* Parseable instance running and accessible

### Database User Setup

Create a monitoring user with the required permissions:

```sql
-- Create monitoring user
CREATE USER 'otel'@'%' IDENTIFIED BY 'your-secure-password';

-- Grant required permissions
GRANT PROCESS, REPLICATION CLIENT ON *.* TO 'otel'@'%';
GRANT SELECT ON performance_schema.* TO 'otel'@'%';

-- Flush privileges
FLUSH PRIVILEGES;
```

## OpenTelemetry Collector Configuration

### Basic Configuration

Create an `otel-collector-config.yaml` file:

```yaml
receivers:
  mysql:
    endpoint: localhost:3306
    username: otel
    password: ${env:MYSQL_PASSWORD}
    database: mydb
    collection_interval: 10s

exporters:
  otlphttp/parseable:
    endpoint: "http://parseable:8000"
    headers:
      Authorization: "Basic YWRtaW46YWRtaW4="
      X-P-Stream: "mysql-metrics"
      X-P-Log-Source: "otel-metrics"
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      receivers: [mysql]
      exporters: [otlphttp/parseable]
```

### Advanced Configuration with Statement Events

For detailed query performance monitoring:

```yaml
receivers:
  mysql:
    endpoint: localhost:3306
    username: otel
    password: ${env:MYSQL_PASSWORD}
    database: mydb
    collection_interval: 10s
    initial_delay: 1s
    statement_events:
      digest_text_limit: 120
      time_limit: 24h
      limit: 250
    tls:
      insecure: false
      insecure_skip_verify: false

exporters:
  otlphttp/parseable:
    endpoint: "http://parseable:8000"
    headers:
      Authorization: "Basic YWRtaW46YWRtaW4="
      X-P-Stream: "mysql-metrics"
      X-P-Log-Source: "otel-metrics"
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      receivers: [mysql]
      exporters: [otlphttp/parseable]
```

## Configuration Options

| Parameter                | Default          | Description                           |
| ------------------------ | ---------------- | ------------------------------------- |
| `endpoint`               | `localhost:3306` | MySQL server endpoint                 |
| `username`               | `root`           | Database username                     |
| `password`               | -                | Database password                     |
| `database`               | -                | Database name (empty = all databases) |
| `collection_interval`    | `10s`            | Metrics collection interval           |
| `allow_native_passwords` | `true`           | Allow native password authentication  |
| `tls.insecure`           | `false`          | Disable TLS                           |
| `statement_events.limit` | `250`            | Max statement events to collect       |

## Collected Metrics

The MySQL receiver collects the following metrics:

| Metric                             | Description              |
| ---------------------------------- | ------------------------ |
| `mysql.buffer_pool.pages`          | Buffer pool page counts  |
| `mysql.buffer_pool.data_pages`     | Buffer pool data pages   |
| `mysql.buffer_pool.operations`     | Buffer pool operations   |
| `mysql.commands`                   | Command execution counts |
| `mysql.handlers`                   | Handler operation counts |
| `mysql.locks`                      | Lock wait counts         |
| `mysql.sorts`                      | Sort operation counts    |
| `mysql.threads`                    | Thread counts by state   |
| `mysql.connections`                | Connection counts        |
| `mysql.queries`                    | Query execution counts   |
| `mysql.statement_events.count`     | Statement event counts   |
| `mysql.statement_events.wait.time` | Statement wait times     |

## Running the Collector

### Docker

```bash
docker run -d \
  --name otel-collector \
  -v $(pwd)/otel-collector-config.yaml:/etc/otelcol/config.yaml \
  -e MYSQL_PASSWORD=your-password \
  otel/opentelemetry-collector-contrib:latest
```

### Docker Compose

```yaml
version: '3.8'
services:
  otel-collector:
    image: otel/opentelemetry-collector-contrib:latest
    volumes:
      - ./otel-collector-config.yaml:/etc/otelcol/config.yaml
    environment:
      - MYSQL_PASSWORD=${MYSQL_PASSWORD}
    depends_on:
      - mysql
      - parseable
```

## Querying MySQL Metrics in Parseable

Once data is flowing, query your MySQL metrics:

```sql
-- Get thread counts over time
SELECT p_timestamp, threads_running, threads_connected 
FROM "mysql-metrics" 
ORDER BY p_timestamp DESC 
LIMIT 100

-- Find slow queries
SELECT digest_text, total_latency, exec_count
FROM "mysql-metrics"
WHERE p_timestamp > NOW() - INTERVAL '1 hour'
ORDER BY total_latency DESC
LIMIT 10
```

## Troubleshooting

### Connection Issues

If the collector can't connect to MySQL:

1. Verify MySQL is accepting connections on the configured port
2. Check the user has proper permissions
3. Verify `skip-networking` is not enabled in MySQL config
4. Check firewall rules allow the connection

### Missing Metrics

If some metrics are not appearing:

1. Ensure `performance_schema` is enabled
2. Verify the monitoring user has SELECT on `performance_schema`
3. Check InnoDB is the storage engine for InnoDB-specific metrics

## Next Steps

* Set up [alerts](/docs/user-guide/alerting) for database performance thresholds
* Create [dashboards](/docs/user-guide/dashboards) for MySQL monitoring
* Explore [SQL queries](/docs/user-guide/sql-editor) for custom analysis


# PostgreSQL (/docs/ingest-data/databases/postgresql)



Monitor your PostgreSQL databases by collecting metrics and logs using the OpenTelemetry Collector and sending them to Parseable.

## Overview

The OpenTelemetry Collector's PostgreSQL receiver collects metrics from PostgreSQL databases including:

* **Database Statistics** - Connections, transactions, queries
* **Table Metrics** - Row counts, dead tuples, table sizes
* **Index Metrics** - Index usage and efficiency
* **Query Performance** - Query samples and execution times
* **Replication Metrics** - Lag and replication status

## Prerequisites

* PostgreSQL 12+ (see [supported versions](https://www.postgresql.org/support/versioning))
* OpenTelemetry Collector with `postgresql` receiver
* Parseable instance running and accessible

### Database User Setup

Create a monitoring user with the required permissions:

```sql
-- Create monitoring user
CREATE USER otel WITH PASSWORD 'your-secure-password';

-- Grant required permissions
GRANT SELECT ON pg_stat_database TO otel;
GRANT pg_monitor TO otel;

-- For query sample collection (optional)
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
```

## OpenTelemetry Collector Configuration

### Basic Configuration

Create an `otel-collector-config.yaml` file:

```yaml
receivers:
  postgresql:
    endpoint: localhost:5432
    transport: tcp
    username: otel
    password: ${env:POSTGRESQL_PASSWORD}
    databases:
      - mydb
    collection_interval: 10s
    tls:
      insecure: true

exporters:
  otlphttp/parseable:
    endpoint: "http://parseable:8000"
    headers:
      Authorization: "Basic YWRtaW46YWRtaW4="
      X-P-Stream: "postgresql-metrics"
      X-P-Log-Source: "otel-metrics"
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      receivers: [postgresql]
      exporters: [otlphttp/parseable]
```

### Advanced Configuration with Query Samples

For detailed query performance monitoring:

```yaml
receivers:
  postgresql:
    endpoint: localhost:5432
    transport: tcp
    username: otel
    password: ${env:POSTGRESQL_PASSWORD}
    databases:
      - mydb
    collection_interval: 10s
    tls:
      insecure: false
      insecure_skip_verify: false
      ca_file: /path/to/ca.crt
      cert_file: /path/to/client.crt
      key_file: /path/to/client.key
    events:
      db.server.query_sample:
        enabled: true
      db.server.top_query:
        enabled: true
    query_sample_collection:
      max_rows_per_query: 100
    top_query_collection:
      max_rows_per_query: 100
      top_n_query: 100

exporters:
  otlphttp/parseable:
    endpoint: "http://parseable:8000"
    headers:
      Authorization: "Basic YWRtaW46YWRtaW4="
      X-P-Stream: "postgresql-metrics"
      X-P-Log-Source: "otel-metrics"
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      receivers: [postgresql]
      exporters: [otlphttp/parseable]
```

## Configuration Options

| Parameter                  | Default          | Description                                |
| -------------------------- | ---------------- | ------------------------------------------ |
| `endpoint`                 | `localhost:5432` | PostgreSQL server endpoint                 |
| `transport`                | `tcp`            | Transport protocol (`tcp` or `unix`)       |
| `username`                 | -                | Database username                          |
| `password`                 | -                | Database password                          |
| `databases`                | `[]`             | List of databases to monitor (empty = all) |
| `collection_interval`      | `10s`            | Metrics collection interval                |
| `tls.insecure`             | `false`          | Disable TLS                                |
| `tls.insecure_skip_verify` | `true`           | Skip certificate verification              |

## Collected Metrics

The PostgreSQL receiver collects the following metrics:

| Metric                     | Description                        |
| -------------------------- | ---------------------------------- |
| `postgresql.backends`      | Number of active connections       |
| `postgresql.commits`       | Number of committed transactions   |
| `postgresql.rollbacks`     | Number of rolled back transactions |
| `postgresql.database.size` | Database size in bytes             |
| `postgresql.rows`          | Number of rows by operation type   |
| `postgresql.blocks_read`   | Number of disk blocks read         |
| `postgresql.blocks_hit`    | Number of buffer hits              |
| `postgresql.deadlocks`     | Number of deadlocks detected       |
| `postgresql.temp_files`    | Number of temporary files created  |

## Running the Collector

### Docker

```bash
docker run -d \
  --name otel-collector \
  -v $(pwd)/otel-collector-config.yaml:/etc/otelcol/config.yaml \
  -e POSTGRESQL_PASSWORD=your-password \
  otel/opentelemetry-collector-contrib:latest
```

### Docker Compose

```yaml
version: '3.8'
services:
  otel-collector:
    image: otel/opentelemetry-collector-contrib:latest
    volumes:
      - ./otel-collector-config.yaml:/etc/otelcol/config.yaml
    environment:
      - POSTGRESQL_PASSWORD=${POSTGRESQL_PASSWORD}
    depends_on:
      - postgres
      - parseable
```

## Querying PostgreSQL Metrics in Parseable

Once data is flowing, query your PostgreSQL metrics:

```sql
-- Get connection count over time
SELECT p_timestamp, backends 
FROM "postgresql-metrics" 
ORDER BY p_timestamp DESC 
LIMIT 100

-- Find databases with high rollback rates
SELECT database_name, commits, rollbacks,
       (rollbacks::float / NULLIF(commits + rollbacks, 0)) * 100 as rollback_pct
FROM "postgresql-metrics"
WHERE p_timestamp > NOW() - INTERVAL '1 hour'
```

## Troubleshooting

### Connection Issues

If the collector can't connect to PostgreSQL:

1. Verify PostgreSQL is accepting connections on the configured port
2. Check firewall rules allow the connection
3. Verify the username and password are correct
4. Check TLS settings match your PostgreSQL configuration

### Missing Metrics

If some metrics are not appearing:

1. Ensure the monitoring user has `pg_monitor` role
2. Verify `pg_stat_statements` extension is installed for query metrics
3. Check the `databases` list includes your target databases

## Next Steps

* Set up [alerts](/docs/user-guide/alerting) for database performance thresholds
* Create [dashboards](/docs/user-guide/dashboards) for PostgreSQL monitoring
* Explore [SQL queries](/docs/user-guide/sql-editor) for custom analysis


# Redis (/docs/ingest-data/databases/redis)



Monitor your Redis instances by collecting metrics using the OpenTelemetry Collector and sending them to Parseable.

## Overview

The OpenTelemetry Collector's Redis receiver collects metrics from Redis instances using the `INFO` command including:

* **Server Statistics** - Uptime, connected clients, memory usage
* **Memory Metrics** - Used memory, peak memory, fragmentation
* **Persistence Metrics** - RDB and AOF status
* **Replication Metrics** - Master/replica status and lag
* **Command Statistics** - Commands processed, keyspace hits/misses

## Prerequisites

* Redis 4.0+
* OpenTelemetry Collector with `redis` receiver
* Parseable instance running and accessible

### Redis Authentication (Optional)

If your Redis instance requires authentication:

```bash
# Redis 6.0+ with ACL
redis-cli ACL SETUSER otel on >your-password +info +client +slowlog +latency allkeys

# Redis < 6.0 with requirepass
# Set password in redis.conf: requirepass your-password
```

## OpenTelemetry Collector Configuration

### Basic Configuration

Create an `otel-collector-config.yaml` file:

```yaml
receivers:
  redis:
    endpoint: "localhost:6379"
    collection_interval: 10s
    password: ${env:REDIS_PASSWORD}

exporters:
  otlphttp/parseable:
    endpoint: "http://parseable:8000"
    headers:
      Authorization: "Basic YWRtaW46YWRtaW4="
      X-P-Stream: "redis-metrics"
      X-P-Log-Source: "otel-metrics"
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      receivers: [redis]
      exporters: [otlphttp/parseable]
```

### TLS Configuration

For Redis instances with TLS enabled:

```yaml
receivers:
  redis:
    endpoint: "localhost:6379"
    collection_interval: 10s
    username: otel
    password: ${env:REDIS_PASSWORD}
    tls:
      insecure: false
      ca_file: /path/to/ca.crt
      cert_file: /path/to/client.crt
      key_file: /path/to/client.key

exporters:
  otlphttp/parseable:
    endpoint: "http://parseable:8000"
    headers:
      Authorization: "Basic YWRtaW46YWRtaW4="
      X-P-Stream: "redis-metrics"
      X-P-Log-Source: "otel-metrics"
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      receivers: [redis]
      exporters: [otlphttp/parseable]
```

### Unix Socket Configuration

For Redis instances using Unix sockets:

```yaml
receivers:
  redis:
    endpoint: "/var/run/redis/redis.sock"
    transport: unix
    collection_interval: 10s
    password: ${env:REDIS_PASSWORD}

exporters:
  otlphttp/parseable:
    endpoint: "http://parseable:8000"
    headers:
      Authorization: "Basic YWRtaW46YWRtaW4="
      X-P-Stream: "redis-metrics"
      X-P-Log-Source: "otel-metrics"
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      receivers: [redis]
      exporters: [otlphttp/parseable]
```

## Configuration Options

| Parameter             | Default | Description                          |
| --------------------- | ------- | ------------------------------------ |
| `endpoint`            | -       | Redis server endpoint (required)     |
| `transport`           | `tcp`   | Transport protocol (`tcp` or `unix`) |
| `username`            | -       | Username for Redis 6.0+ ACL          |
| `password`            | -       | Redis password                       |
| `collection_interval` | `10s`   | Metrics collection interval          |
| `tls.insecure`        | `true`  | Disable TLS                          |
| `tls.ca_file`         | -       | CA certificate path                  |
| `tls.cert_file`       | -       | Client certificate path              |
| `tls.key_file`        | -       | Client key path                      |

## Collected Metrics

The Redis receiver collects the following metrics:

| Metric                                        | Description                   |
| --------------------------------------------- | ----------------------------- |
| `redis.clients.connected`                     | Number of connected clients   |
| `redis.clients.blocked`                       | Number of blocked clients     |
| `redis.clients.max_input_buffer`              | Biggest input buffer          |
| `redis.clients.max_output_buffer`             | Biggest output buffer         |
| `redis.commands`                              | Total commands processed      |
| `redis.commands.processed`                    | Commands processed per second |
| `redis.connections.received`                  | Total connections received    |
| `redis.connections.rejected`                  | Rejected connections          |
| `redis.cpu.time`                              | CPU time consumed             |
| `redis.db.avg_ttl`                            | Average TTL of keys           |
| `redis.db.expires`                            | Keys with expiration          |
| `redis.db.keys`                               | Total keys in database        |
| `redis.keys.evicted`                          | Evicted keys                  |
| `redis.keys.expired`                          | Expired keys                  |
| `redis.keyspace.hits`                         | Keyspace hits                 |
| `redis.keyspace.misses`                       | Keyspace misses               |
| `redis.memory.fragmentation_ratio`            | Memory fragmentation ratio    |
| `redis.memory.lua`                            | Lua memory usage              |
| `redis.memory.peak`                           | Peak memory usage             |
| `redis.memory.rss`                            | Resident set size             |
| `redis.memory.used`                           | Used memory                   |
| `redis.net.input`                             | Network input bytes           |
| `redis.net.output`                            | Network output bytes          |
| `redis.rdb.changes_since_last_save`           | Changes since last RDB save   |
| `redis.replication.backlog_first_byte_offset` | Replication backlog offset    |
| `redis.replication.offset`                    | Replication offset            |
| `redis.slaves.connected`                      | Connected replicas            |
| `redis.uptime`                                | Server uptime in seconds      |

## Running the Collector

### Docker

```bash
docker run -d \
  --name otel-collector \
  -v $(pwd)/otel-collector-config.yaml:/etc/otelcol/config.yaml \
  -e REDIS_PASSWORD=your-password \
  otel/opentelemetry-collector-contrib:latest
```

### Docker Compose

```yaml
version: '3.8'
services:
  otel-collector:
    image: otel/opentelemetry-collector-contrib:latest
    volumes:
      - ./otel-collector-config.yaml:/etc/otelcol/config.yaml
    environment:
      - REDIS_PASSWORD=${REDIS_PASSWORD}
    depends_on:
      - redis
      - parseable
```

## Querying Redis Metrics in Parseable

Once data is flowing, query your Redis metrics:

```sql
-- Get memory usage over time
SELECT p_timestamp, memory_used, memory_peak 
FROM "redis-metrics" 
ORDER BY p_timestamp DESC 
LIMIT 100

-- Calculate cache hit ratio
SELECT 
  p_timestamp,
  keyspace_hits,
  keyspace_misses,
  (keyspace_hits::float / NULLIF(keyspace_hits + keyspace_misses, 0)) * 100 as hit_ratio
FROM "redis-metrics"
WHERE p_timestamp > NOW() - INTERVAL '1 hour'
ORDER BY p_timestamp DESC
```

## Troubleshooting

### Connection Issues

If the collector can't connect to Redis:

1. Verify Redis is accepting connections on the configured port
2. Check the password is correct
3. Verify `protected-mode` settings in Redis
4. Check firewall rules allow the connection

### Missing Metrics

If some metrics are not appearing:

1. Ensure the Redis user has permission to run `INFO` command
2. Check if specific features (like replication) are enabled
3. Verify the Redis version supports the metrics

## Next Steps

* Set up [alerts](/docs/user-guide/alerting) for cache performance thresholds
* Create [dashboards](/docs/user-guide/dashboards) for Redis monitoring
* Explore [SQL queries](/docs/user-guide/sql-editor) for custom analysis


# Apache Log4j 2 (/docs/ingest-data/logging-agents/apache-log-4j)



Apache Log4j 2 is a Java-based logging framework. It is one of most popular logging frameworks in Java. This document explains how to use the [Log4j 2 HTTP appender](https://logging.apache.org/log4j/2.x/manual/appenders.html#HTTP) to send logs to Parseable.

### Prerequisites

* Parseable server installed and running. See [installation](/docs/self-hosted/installation/) for more details.
* A Java project with Log4j dependency.

### Setup

Edit the log4j2.xml file to add the following configuration. Please ensure to update the url, Authorization, and X-P-Stream properties with the correct values.

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<Configuration status="TRACE">
    <Appenders>
        <Http name="Parseable" url="<parseable-server-url>/api/v1/ingest" method="POST">
            <Property name="Authorization" value="Basic <basic-auth-hash>" />
            <Property name="X-P-Stream" value="<dataset-name>" />
            <Property name="Accept" value="application/json" />
            <JsonLayout properties="true"/>
        </Http>
    </Appenders>
    <Loggers>
        <Root level="info">
            <AppenderRef ref="Parseable"/>
        </Root>
    </Loggers>
</Configuration>
```

Once the configuration is updated, restart the application. You should start seeing logs in Parseable.


# Filebeat (/docs/ingest-data/logging-agents/filebeat)



Ship logs from Filebeat to Parseable using the HTTP output.

## Overview

Integrate Filebeat with Parseable to:

* **Lightweight Collection** - Minimal resource footprint
* **Rich Inputs** - Collect from files, containers, cloud services
* **Modules** - Pre-built configurations for common applications
* **Reliable Delivery** - At-least-once delivery guarantee

## Prerequisites

* Filebeat installed
* Parseable instance accessible
* Log files or inputs configured

## Filebeat Configuration

### Basic Configuration

Create `filebeat.yml`:

```yaml
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /var/log/*.log
    fields:
      source: filebeat
    fields_under_root: true

output.http:
  hosts: ["http://parseable:8000/api/v1/ingest"]
  method: "POST"
  headers:
    Authorization: "Basic YWRtaW46YWRtaW4="
    X-P-Stream: "filebeat-logs"
    Content-Type: "application/json"
  codec.format:
    string: '[%{[message]}]'
```

### JSON Log Collection

For JSON-formatted logs:

```yaml
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /var/log/app/*.json
    json.keys_under_root: true
    json.add_error_key: true

processors:
  - timestamp:
      field: timestamp
      layouts:
        - '2006-01-02T15:04:05.000Z'
      test:
        - '2024-01-15T10:30:00.000Z'

output.http:
  hosts: ["http://parseable:8000/api/v1/ingest"]
  method: "POST"
  headers:
    Authorization: "Basic YWRtaW46YWRtaW4="
    X-P-Stream: "app-logs"
  batch.size: 100
  batch.timeout: 5s
```

### Container Logs

Collect Docker container logs:

```yaml
filebeat.inputs:
  - type: container
    paths:
      - '/var/lib/docker/containers/*/*.log'
    processors:
      - add_docker_metadata:
          host: "unix:///var/run/docker.sock"

output.http:
  hosts: ["http://parseable:8000/api/v1/ingest"]
  method: "POST"
  headers:
    Authorization: "Basic YWRtaW46YWRtaW4="
    X-P-Stream: "container-logs"
```

### Kubernetes Logs

For Kubernetes deployments:

```yaml
filebeat.inputs:
  - type: container
    paths:
      - /var/log/containers/*.log
    processors:
      - add_kubernetes_metadata:
          host: ${NODE_NAME}
          matchers:
            - logs_path:
                logs_path: "/var/log/containers/"

output.http:
  hosts: ["http://parseable:8000/api/v1/ingest"]
  method: "POST"
  headers:
    Authorization: "Basic YWRtaW46YWRtaW4="
    X-P-Stream: "k8s-logs"
```

## Filebeat Modules

Use built-in modules for common applications:

### Enable Module

```bash
filebeat modules enable nginx
filebeat modules enable mysql
```

### Module Configuration

```yaml
# modules.d/nginx.yml
- module: nginx
  access:
    enabled: true
    var.paths: ["/var/log/nginx/access.log*"]
  error:
    enabled: true
    var.paths: ["/var/log/nginx/error.log*"]
```

## Running Filebeat

### Docker

```bash
docker run -d \
  --name filebeat \
  -v $(pwd)/filebeat.yml:/usr/share/filebeat/filebeat.yml:ro \
  -v /var/log:/var/log:ro \
  docker.elastic.co/beats/filebeat:8.11.0
```

### Docker Compose

```yaml
version: '3.8'
services:
  filebeat:
    image: docker.elastic.co/beats/filebeat:8.11.0
    user: root
    volumes:
      - ./filebeat.yml:/usr/share/filebeat/filebeat.yml:ro
      - /var/log:/var/log:ro
      - /var/lib/docker/containers:/var/lib/docker/containers:ro
      - /var/run/docker.sock:/var/run/docker.sock:ro
```

### Kubernetes DaemonSet

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: filebeat
spec:
  selector:
    matchLabels:
      app: filebeat
  template:
    spec:
      containers:
        - name: filebeat
          image: docker.elastic.co/beats/filebeat:8.11.0
          volumeMounts:
            - name: config
              mountPath: /usr/share/filebeat/filebeat.yml
              subPath: filebeat.yml
            - name: varlog
              mountPath: /var/log
              readOnly: true
      volumes:
        - name: config
          configMap:
            name: filebeat-config
        - name: varlog
          hostPath:
            path: /var/log
```

## Configuration Options

| Parameter                   | Description                 |
| --------------------------- | --------------------------- |
| `output.http.hosts`         | Parseable endpoint URL      |
| `output.http.headers`       | HTTP headers including auth |
| `output.http.batch.size`    | Events per batch            |
| `output.http.batch.timeout` | Max wait time for batch     |

## Best Practices

1. **Use Batching** - Configure appropriate batch sizes
2. **Add Metadata** - Include host, container, or k8s metadata
3. **Parse JSON** - Use JSON parsing for structured logs
4. **Monitor Filebeat** - Enable monitoring endpoints
5. **Handle Backpressure** - Configure queue settings

## Troubleshooting

### Events Not Sending

1. Test Filebeat configuration: `filebeat test config`
2. Test output: `filebeat test output`
3. Check Filebeat logs
4. Verify Parseable endpoint is accessible

### Duplicate Events

1. Check registry file location
2. Verify clean\_removed setting
3. Check for multiple Filebeat instances

## Next Steps

* Configure [Fluent Bit](/docs/ingest-data/logging-agents) as alternative
* Set up [alerts](/docs/user-guide/alerting) for log patterns
* Create [dashboards](/docs/user-guide/dashboards) for monitoring


# Fluent Bit (/docs/ingest-data/logging-agents/fluent-bit)



[Fluent Bit](https://fluentbit.io) is a lightweight and scalable logging and metrics processor and forwarder. Fluent Bit can be configured to send logs to Parseable with [HTTP output plugin](https://docs.fluentbit.io/v/1.12.0/output/http) and [JSON output format](https://docs.fluentbit.io/v/1.12.0/output/json).

This document explains how to set up Fluent Bit to ship logs to Parseable Docker Compose and Kubernetes. This should give you an idea on how to configure the output plugin for other scenarios.

For demo purpose, we used Fluent Bit's [Memory Metrics Input plugin](https://docs.fluentbit.io/v/1.12.0/input/metrics-memory) as the source of logs.

## Docker Compose

Please ensure Docker Compose installed on your machine. Then run the following commands to set up Parseable and Fluent Bit.

```bash
mkdir parseable
cd parseable
wget https://www.parseable.com/fluentbit/fluent-bit.conf
wget https://www.parseable.com/fluentbit/docker-compose.yaml
docker-compose up -d
```

You can now access the Parseable dashboard on `http://localhost:8000`. You should see a dataset called `fluentbitdemo` populated with log data generated by the Memory Metrics Input plugin.

## Kubernetes

How does Fluent Bit runs in a K8s cluster

* Fluent Bit runs as a DaemonSet → Deploys on every node to collect logs.
* Watches `/var/log/containers/*.log` → Reads container logs from the node’s filesystem.
* Filters and enriches logs → Extracts Kubernetes metadata, merges multi-line logs.
* Compresses & sends logs → Pushes logs to Parseable over HTTP with Gzip compression.

### Pre-Requisites

* Please ensure `kubectl` and `helm` installed and configured to access your Kubernetes cluster.
* Parseable installed on your Kubernetes cluster. Refer the [Parseable Kubernetes documentation](https://www.parseable.com/docs/self-hosted/installation/distributed/k8s-helm).

### Install Fluent Bit

We use the official [Fluent Bit Helm chart](https://github.com/fluent/helm-charts) to install Fluent Bit. But, we'll use a modified values.yaml file, that contains the configuration for Fluent Bit to send logs to Parseable.

```bash
wget https://www.parseable.com/fluentbit/values.yaml
helm repo add fluent https://fluent.github.io/helm-charts
helm install fluent-bit fluent/fluent-bit --values values.yaml -n fluentbit --create-namespace
```

Let's take a deeper look at the Fluent Bit configuration in `values.yaml`. Here we use the kubernetes filter to enrich the logs with Kubernetes metadata. We then use the http output plugin to send logs to Parseable. Notice the Match section in the http output plugin. We use `kube.*` to match all logs from Kubernetes filter. With the header `X-P-Stream fluentbitdemo`, we tell Parseable to send the logs to the `fluentbitdemo` dataset.

```ini
  filters: |
    [FILTER]
        Name                 kubernetes
        Match                kube.*
        Merge_Log            On
        Keep_Log             Off
        K8S-Logging.Parser   On
        K8S-Logging.Exclude  On

  outputs: |
    [OUTPUT]
        Name                 http
        Match                kube.*
        host                 parseable.parseable.svc.cluster.local
        uri                  /api/v1/ingest
        port                 80
        http_User            admin
        http_Passwd          admin
        format               json
        compress             gzip
        header               Content-Type application/json
        header               X-P-Stream fluentbitdemo
        json_date_key        timestamp
        json_date_format     iso8601
```

### \[FILTER] Section - Enriching Logs with Kubernetes Metadata

```ini
[FILTER]
    Name                 kubernetes
    Match                kube.*
    Merge_Log            On
    Keep_Log             Off
    K8S-Logging.Parser   On
    K8S-Logging.Exclude  On
```

This section processes logs before sending them out.

* `Name kubernetes` → Enables the Kubernetes filter, which fetches metadata (like Pod name, Namespace, Container ID).

* `Match kube.*` → Applies the filter to logs tagged as "kube.\*" (which typically means logs from Kubernetes containers).

* `Merge_Log On` → Merges multi-line logs into a single structured log (e.g., stack traces).

* `Keep_Log Off` → Removes the original unstructured log after enrichment (saves space).

* `K8S-Logging.Parser On` → Uses parsers to extract structured log fields (if JSON or logfmt is detected).

* `K8S-Logging.Exclude On` → Removes Kubernetes annotations that aren’t useful for logs.

### \[OUTPUT] Section - Forwarding to Parseable

```ini
[OUTPUT]
    Name                 http
    Match                kube.*
    host                 parseable.parseable.svc.cluster.local
    uri                  /api/v1/ingest
    port                 80
    http_User            admin
    http_Passwd          admin
    format               json
    compress             gzip
    header               Content-Type application/json
    header               X-P-Stream fluentbitdemo
    json_date_key        timestamp
    json_date_format     iso8601
```

This section defines where Fluent Bit sends logs.

* `Name http` → Sends logs using the HTTP output plugin.

* `Match kube.*` → Only sends logs tagged as "kube.\*" (i.e., Kubernetes logs).

* `host parseable.parseable.svc.cluster.local` → Uses Kubernetes DNS resolution to reach Parseable's service inside the cluster.

  * `uri /api/v1/ingest` → Sends logs to Parseable’s ingestion API.

  * `port 80` → Connects via port 80 (default HTTP port).

* `http_User admin & http_Passwd admin` → Uses Basic Authentication.

* `format json` → Sends logs in JSON format.

* `compress gzip` → Compresses logs before sending → reduces bandwidth & storage costs.

* `header Content-Type application/json` → Ensures correct content type for the API.

* `header X-P-Stream fluentbitdemo` → Assigns logs to the "fluentbitdemo" dataset in Parseable.

* `json_date_key timestamp` → Sets the timestamp field in logs as "timestamp".

* `json_date_format iso8601` → Uses the ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ).

### Check logs in Parseable

Port forward Parseable service to access the dashboard with:

```bash
kubectl port-forward svc/parseable 8000:80 -n parseable
```

You can now check the Parseable server `fluentbitdemo` dataset to see the logs from this setup.

### Batching and Compression

Parseable supports batching and compressing the log data before sending it via HTTP POST. Fluent Bit supports this feature via the compress and buffer\_max\_size option. We recommend enabling both of these options to reduce the number of HTTP requests and to reduce the size of the HTTP payload.

### Adding custom columns

In several cases you may want to add additional metadata to a log event. For example, you may want to append hostname to each log event, so filtering becomes easy at the time of debugging. This is done using lua scripts. Here is an example:

```lua
Use a Lua function to create some additional entries in the log record
function append_columns(tag, timestamp, record)
    new_record = record
    -- Add a static new field to the record
    new_record["environment"] = "production"
    -- Add a dynamic field to the record
    -- We get the env variable HOSTNAME from the Docker container
    -- Then we add it to the record
    hostname = os.getenv("HOSTNAME")
    new_record["hostname"] = hostname
    -- Return the new record
    -- "1" means that the record is modified
    -- "timestamp" is updated timestamp
    -- "new_record" is the new record (after modification)
    return 1, timestamp, new_record
end
```

Lua scripts are added to Fluent Bit as filters. To add this script as a filter, save the above script as `filters.lua` file. Place the `filters.lua` file in the same directory as rest of the Fluent Bit configuration files. Then add a filters section in the Fluent Bit config. For example:

```ini
[FILTER]
    Name                 lua
    Match                *
    Script               filters.lua
    Call                 append_columns

[OUTPUT]
    Name                 http
    Match                *
    host                 parseable
    uri                  /api/v1/ingest
    port                 8000
    http_User            admin
    http_Passwd          admin
    format               json
    compress             gzip
    header               Content-Type application/json
    header               X-P-Stream fluentbitdemo
    json_date_key        timestamp
    json_date_format     iso8601
```

Note that the `[Input]` section needs to be added.

### Database Monitoring

#### PostgreSQL

Here we assume that the PostgreSQL is installed on a pod in the same k8s cluster as of Fluentbit. Read More on how to install PostgreSQl on K8s.

Update the volume mount once installed.

```yaml
volumeMounts:
  - name: pg-logs
    mountPath: /var/lib/postgresql/data/pg_log
```

Edit PostgreSQL Config (postgresql.conf)

```bash
sudo nano /etc/postgresql/15/main/postgresql.conf
```

Modify the following settings:

```ini
logging_collector = on
log_directory = 'pg_log'
log_filename = 'postgresql.log'
log_statement = 'all'
log_connections = on
log_disconnections = on
log_min_duration_statement = 0
```

Restart PostgreSQL

```bash
sudo systemctl restart postgresql
```

Connect to fluent bit using the config map

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: fluent-bit-config
  namespace: logging
data:
  fluent-bit.conf: |
    [SERVICE]
        Flush        1
        Daemon       Off
        Log_Level    info
        Parsers_File parsers.conf

    [INPUT]
        Name        tail
        Path        /var/log/postgresql/postgresql.log
        Tag         postgres.*
        Parser      postgres_parser
        DB         /var/log/postgresql/flb.db
        Mem_Buf_Limit 5MB
        Skip_Long_Lines On
        Refresh_Interval 10

    [FILTER]
        Name        modify
        Match       postgres.*
        Add         service postgresql

    [OUTPUT]
        Name        http
        Match       *
        Host        parseable.parseable.svc.cluster.local
        Port        80
        URI         /api/v1/ingest/postgres-logs
        Format      json
        Header      Content-Type application/json
```

Apply the config map

```bash
kubectl apply -f fluent-bit-config.yaml
```

Check if Fluent Bit is Sending Logs

```bash
kubectl logs -l name=fluent-bit -n logging
```

Check if logs are reaching Parseable:

```bash
kubectl logs -l app=fluent-bit -n logging | grep postgres
```

View Logs inPrism
Log in to Parseable and Navigate to "Streams" and click on `postgres-logs` (created automatically by Fluent Bit)

Search and filter logs based on timestamps, queries, errors, etc.

DeepDive into FluentBit configuration Use Case: Collecting Kubernetes Container Logs & Sending to Parseable
This Fluent Bit configuration reads Kubernetes container logs, extracts structured fields using parsers, and sends them to Parseable.

Configuration

```ini
[SERVICE]
    Flush        5
    Daemon       Off
    Log_Level    info

[INPUT]
    Name         tail
    Path         /var/log/containers/*.log
    Tag          kube.*
    Parser       docker
    Refresh_Interval 5
    Mem_Buf_Limit 10MB
    Skip_Long_Lines On
    DB           /var/log/flb_kube.db

[FILTER]
    Name         kubernetes
    Match        kube.*
    Kube_URL     https://kubernetes.default.svc:443
    Merge_Log    On
    Keep_Log     On
    K8S-Logging.Parser On
    K8S-Logging.Exclude On

[OUTPUT]
    Name         http
    Match        kube.*
    Host         parseable
    Port         8000
    URI          /api/v1/ingest
    format       json
    http_User    admin
    http_Passwd  admin
    Header       X-P-Stream kubernetes_logs
    Json_date_key timestamp
    Json_date_format iso8601
```

### Explanation

1. \[SERVICE] (Global Settings)

   * `Flush 5` → Sends logs every 5 seconds.

   * `Daemon Off` → Runs in foreground mode.

   * `Log_Level info` → Only logs important messages.

2. \[INPUT] (Reading Container Logs)

   * `Name tail` → Uses the tail plugin to read log files.

   * `Path /var/log/containers/*.log` → Reads all container logs in /var/log/containers/.

   * `Tag kube.*` → Tags logs with a Kubernetes-specific prefix for filtering.

   * `Parser docker` → Uses the Docker parser to properly structure logs.

   * `Refresh_Interval 5` → Scans the file for new logs every 5 seconds.

   * `Mem_Buf_Limit 10MB` → Buffers logs up to 10MB in memory before flushing.

   * `Skip_Long_Lines On` → Prevents log truncation issues.

   * `DB /var/log/flb_kube.db` → Maintains a checkpoint database to track log processing.

3. \[FILTER] (Processing Kubernetes Metadata)

   * `Name kubernetes` → Enables the Kubernetes filter to enrich logs.

   * `Match kube.*` → Applies the filter to all Kubernetes logs.

   * `Kube_URL https://kubernetes.default.svc:443` → Connects to the Kubernetes API to fetch metadata.

   * `Merge_Log On` → Merges multi-line logs into a single structured log.

   * `Keep_Log On` → Retains the original log structure.

   * `K8S-Logging.Parser On` → Enables automatic parsing of Kubernetes logs.

   * `K8S-Logging.Exclude On` → Removes redundant log metadata after parsing.

4. \[OUTPUT] (Sending to Parseable)

   * `Name http` → Uses the HTTP output plugin.

   * `Match kube.*` → Sends only Kubernetes logs.

   * `Host parseable` → Sends logs to a Parseable instance.

   * `Port 8000` → Connects via port 8000.

   * `URI /api/v1/ingest` → Sends logs to the Parseable API endpoint.

   * `format json` → Logs are formatted as JSON.

   * `http_User admin` / `http_Passwd admin` → Uses authentication.

   * `Header X-P-Stream kubernetes_logs` → Adds a dataset name (kubernetes\_logs).

   * `Json_date_key timestamp` → Uses "timestamp" as the JSON key.

   * `Json_date_format iso8601` → Ensures ISO 8601 timestamp format.

### Understanding Parsers in Fluent Bit

Parsers convert raw logs into structured formats. In this config, we use the Docker parser:

```ini
[PARSER]
    Name         docker
    Format       json
    Time_Key     time
    Time_Format  %Y-%m-%dT%H:%M:%S.%L
```

Why use a parser?

* Extracts structured fields from JSON logs.
* Converts timestamps into a standard format.

## Using OpenTelemetry Output Plugin

Fluent Bit supports sending telemetry data to Parseable using the OpenTelemetry output plugin. This plugin enables Fluent Bit to act as an OpenTelemetry collector, receiving and forwarding logs, metrics, and traces in the Protocol Buffers format.

<OfferingPills pro enterprise className="mb-4" />

### Configuration Overview

This configuration sets up Fluent Bit to:

1. **Receive** OpenTelemetry data on port 4318 (OTLP/HTTP standard port)
2. **Route** different telemetry types (logs, metrics, traces) to appropriate Parseable endpoints
3. **Authenticate** using basic authentication
4. **Tag** data with dataset names and sources for organization in Parseable

```ini
[SERVICE]
    Flush         1                # Flush data every second
    Log_Level     debug            # Enable debug logging for troubleshooting
    Daemon        off              # Run in foreground
    Parsers_File  parsers.conf     # Load custom parsers
    HTTP_Server   On               # Enable HTTP monitoring server
    HTTP_Listen   0.0.0.0         
    HTTP_Port     2020            # Monitoring dashboard on port 2020

# OpenTelemetry input to receive OTLP data
[INPUT]
    name opentelemetry
    listen 0.0.0.0                # Accept connections from any IP
    port   4318                   # Standard OTLP/HTTP port
    tag    otel                   # Base tag for routing
    tag_from_uri true             # Extract tag from URI path (e.g., /v1/logs → v1_logs)

# Output for OpenTelemetry Logs
[OUTPUT]
    Name          opentelemetry
    Match         v1_logs         # Match logs from /v1/logs endpoint
    Host          parseable       # Parseable server hostname
    Port          8000           # Parseable port
    Logs_uri      /v1/logs       # Parseable logs endpoint
    Log_response_payload True    # Log server responses for debugging
    Tls           Off            # Disable TLS (use 'On' for production)
    Http_User     admin          # Basic auth username
    Http_Passwd   admin          # Basic auth password
    Header        X-P-Stream otellogs      # Stream name in Parseable
    Header        X-P-Log-Source otel-logs # Source identifier
    Add_label     app fluent-bit          # Add metadata label

# Output for OpenTelemetry Metrics
[OUTPUT]
    Name          opentelemetry
    Match         v1_metrics     # Match metrics from /v1/metrics endpoint
    Host          parseable
    Port          8000
    Metrics_uri   /v1/metrics    # Parseable metrics endpoint
    Log_response_payload True
    Tls           Off
    Http_User     admin
    Http_Passwd   admin
    Header        X-P-Stream otelmetrics     # Stream name for metrics
    Header        X-P-Log-Source otel-metrics
    Add_label     app fluent-bit

# Output for OpenTelemetry Traces
[OUTPUT]
    Name          opentelemetry
    Match         v1_traces      # Match traces from /v1/traces endpoint
    Host          parseable
    Port          8000
    Traces_uri    /v1/traces     # Parseable traces endpoint
    Log_response_payload True
    Tls           Off
    Http_User     admin
    Http_Passwd   admin
    Header        X-P-Stream oteltraces      # Stream name for traces
    Header        X-P-Log-Source otel-traces
    Add_label     app fluent-bit
```

### Key Configuration Parameters

| Parameter              | Description                                                                  |
| ---------------------- | ---------------------------------------------------------------------------- |
| `tag_from_uri`         | Automatically creates tags based on the URI path, enabling automatic routing |
| `X-P-Stream`           | Required header that specifies the target dataset in Parseable               |
| `X-P-Log-Source`       | Identifies the type of the data for filtering and analysis                   |
| `Add_label`            | Adds metadata to help identify the data pipeline                             |
| `Log_response_payload` | Useful for debugging; disable in production for better performance           |

### Usage Example

Once configured, Fluent Bit will:

1. Accept OpenTelemetry data from applications or other collectors at `http://fluent-bit:4318`
2. Automatically route logs to the `otellogs` dataset, metrics to `otelmetrics`, and traces to `oteltraces`
3. Preserve the OpenTelemetry semantic conventions and structure
4. Forward all data to Parseable with proper authentication and metadata

## Scraping Prometheus Metrics

Fluent Bit can scrape Prometheus metrics from any application exposing a `/metrics` endpoint and forward them to Parseable. This capability effectively makes Parseable compatible with the entire Prometheus ecosystem, allowing you to collect metrics from thousands of applications that already expose Prometheus metrics.

### How It Makes Parseable Prometheus-Compatible

<OfferingPills pro enterprise className="mb-4" />

This configuration creates a bridge between Prometheus and Parseable:

1. **Prometheus Scraping**: Fluent Bit acts as a Prometheus scraper, pulling metrics from any Prometheus-compatible endpoint
2. **Format Conversion**: Automatically converts Prometheus exposition format to OpenTelemetry format
3. **Unified Storage**: Stores metrics alongside logs and traces in Parseable for unified observability

### Configuration Example

```ini
[SERVICE]
    Flush              5          # Flush metrics every 5 seconds
    Log_Level          info       # Standard logging level

[INPUT]
    Name               prometheus_scrape
    Host               proxy      # Target host exposing Prometheus metrics
    Port               9090       # Prometheus metrics port
    Metrics_Path       /metrics   # Standard Prometheus metrics endpoint
    Scrape_Interval    2s         # Scrape metrics every 2 seconds

[OUTPUT]
    Name                  opentelemetry
    Match                 *        # Match all scraped metrics
    Host                  parseable
    Port                  8000
    Metrics_uri           /v1/metrics      # Send to Parseable metrics endpoint
    Log_response_payload  True             # Enable response logging
    Tls                   Off
    Http_User             admin
    Http_Passwd           admin
    Header                X-P-Stream vLLMmetrics    # Dataset name in Parseable
    Header                X-P-Log-Source otel-metrics
    Add_label             app fluent-bit
```

### Common Use Cases

1. **Application Metrics**: Scrape metrics from web servers, databases, and custom applications
2. **Infrastructure Monitoring**: Collect system metrics from node exporters
3. **Kubernetes Metrics**: Gather metrics from Kubernetes components and workloads
4. **Service Mesh Metrics**: Collect metrics from Istio, Linkerd, or other service meshes

### Example Targets

You can scrape metrics from various sources by adjusting the `Host` and `Port`:

```ini
# Scrape Node Exporter
Host: node-exporter
Port: 9100

# Scrape Kubernetes API Server
Host: kube-apiserver
Port: 6443

# Scrape Custom Application
Host: my-app
Port: 8080
```

This approach allows you to leverage Parseable as a complete observability backend while maintaining compatibility with your existing Prometheus-based monitoring setup.


# Fluentd (/docs/ingest-data/logging-agents/fluentd)



[Fluentd](https://www.fluentd.org) is a data collector for your applications and services. Fluentd can be configured to send logs to Parseable with [HTTP output plugin](https://docs.fluentd.org/output/http) and [JSON output format](https://docs.fluentd.org/output/json).

This document explains how to set up Fluentd to ship logs to Parseable Docker Compose and Kubernetes. This should give you an idea on how to configure the output plugin for other scenarios.

For demo purpose, we used Fluentd's [Memory Metrics Input plugin](https://docs.fluentd.org/input/metrics-memory) as the source of logs.

## Docker Compose

Please ensure Docker Compose installed on your machine. Then run the following commands to set up Parseable and Fluentd.

```bash
mkdir parseable
cd parseable
wget https://www.parseable.com/fluentd/fluentd.conf
wget https://www.parseable.com/fluentd/docker-compose.yaml
docker-compose up -d
```

You can now access the Parseable dashboard on `http://localhost:8000`. You should see a dataset called `fluentbitdemo` populated with log data generated by the Memory Metrics Input plugin.

## Kubernetes

* Please ensure kubectl and helm installed and configured to access your Kubernetes cluster.
* Parseable installed on your Kubernetes cluster. Refer the [Parseable Kubernetes documentation](https://www.parseable.com/docs/self-hosted/installation/distributed/k8s-helm).

### Install Fluentd

We use the official [Fluentd Helm chart](https://github.com/fluent/fluentd-helm). But, we'll use a modified values.yaml file, that contains the configuration for Fluentd to send logs to Parseable.

```bash
wget https://www.parseable.com/fluentd/values.yaml
helm repo add fluent https://fluent.github.io/helm-charts
helm install fluentd fluent/fluentd --values values.yaml -n f
```

### Fluentd Configuration

Let's take a deeper look at the Fluentd configuration in `values.yaml`. Here we use the `kubernetes` filter to enrich the logs with Kubernetes metadata. We then use the http output plugin to send logs to Parseable. Notice the Match section in the http output plugin. We use `kube.*` to match all logs from Kubernetes filter. With the header `X-P-Stream fluentbitdemo`, we tell Parseable to send the logs to the `fluentbitdemo` dataset.

```ini
# Fluentd configuration
config:
  system: |
    <system>
      log_level debug
    </system>

  ## Input configuration
  inputs: |
    <source>
      @type monitor_agent
      tag memory
      emit_interval 5
    </source>

  ## Output configuration
  outputs: |
    <match *>
      @type http
      host parseable.parseable.svc.cluster.local    
      uri /api/v1/ingest
      port 80
      
      <headers>
        X-P-META-meta1 value1
        X-P-TAG-tag1 value1
        X-P-Stream fluentbitdemo
      </headers>
      
      <format>
        @type json
        time_key timestamp
        time_format iso8601
      </format>
      
      <buffer>
        @type memory
        flush_interval 5s
      </buffer>
      
      <auth>
        method basic
        username admin
        password admin
      </auth>
    </match>
```

## Check logs in Parseable

Port forward Parseable service to access the dashboard with:

```bash
kubectl port-forward svc/parseable 8000:80 -n parseable
```

You can now check the Parseable server `fluentbitdemo` dataset to see the logs from this setup.

Navigate to the Parseable dashboard and verify that logs are being ingested correctly.


# Logging Agents (/docs/ingest-data/logging-agents)



Parseable supports ingestion from various logging agents. Choose the agent that best fits your infrastructure:

* [Fluent Bit](/docs/ingest-data/logging-agents/fluent-bit) - Lightweight and high-performance log processor
* [Vector](/docs/ingest-data/logging-agents/vector) - High-performance observability data pipeline
* [Fluentd](/docs/ingest-data/logging-agents/fluentd) - Unified logging layer
* [Logstash](/docs/ingest-data/logging-agents/logstash) - Server-side data processing pipeline
* [Filebeat](/docs/ingest-data/logging-agents/filebeat) - Lightweight shipper for logs
* [Promtail](/docs/ingest-data/logging-agents/promtail) - Agent for Loki, works with Parseable
* [OpenTelemetry Collector](/docs/ingest-data/logging-agents/otel-collector) - Vendor-agnostic telemetry collection
* [Syslog](/docs/ingest-data/logging-agents/syslog) - Standard logging protocol
* [Apache Log4j](/docs/ingest-data/logging-agents/apache-log-4j) - Java logging framework
* [Prometheus](/docs/ingest-data/logging-agents/prometheus) - Metrics collection and forwarding


# Logstash (/docs/ingest-data/logging-agents/logstash)



Logstash is a server-side data processing pipeline that ingests data from a multitude of sources, transforms it, and then sends it to variety of targets. Logstash can be configured to send logs to Parseable with [HTTP output plugin](https://www.elastic.co/guide/en/logstash/current/output-plugins.html#output-http) and [JSON output format](https://www.elastic.co/guide/en/logstash/current/output-plugins.html#output-json).

This document explains how to set up Logstash to ship logs to Parseable in Docker Compose. We use Logstash's [generator](https://www.elastic.co/guide/en/logstash/current/input-plugins.html#input-generator) input plugin to generate sample log data. Then we use the [http](https://www.elastic.co/guide/en/logstash/current/output-plugins.html#output-http) output plugin to send these logs to Parseable.

## Docker Compose

Please ensure Docker Compose installed on your machine.

```bash
mkdir parseable
cd parseable
wget https://www.parseable.com/logstash/logstash.conf
wget https://www.parseable.com/logstash/docker-compose.yaml
docker-compose up -d
```

You can now access the Parseable dashboard on `http://localhost:8000`. You should see a dataset called `logstashlogs` populated with log data generated by the [generator](https://www.elastic.co/guide/en/logstash/current/input-plugins.html#input-generator) input plugin.


# OpenTelemetry Collector (/docs/ingest-data/logging-agents/otel-collector)



## Pre-requisites

* OTEL Collector installed on your target infrastructure. Refer the [OpenTelemetry Collector installation documentation](https://opentelemetry.io/docs/collector/installation/) for installation instructions.
* Parseable installed on infrastructure of your choice. Refer the [Parseable installation documentation](/docs/self-hosted/installation/).

## Configuration

We'll use the OTLP receiver and the OTEL HTTP exporter to send logs to Parseable.

```yaml
receivers:
  otlp:
    protocols:
      grpc: null
      http: null
exporters:
  otlphttp:
    endpoint: '[PARSEABLE_URL]'
    headers:
      Authorization: '[BASIC_AUTH_TOKEN]'
      X-P-Log-Source: otel
      X-P-Stream: '[NAME_OF THE_STREAM_TO_SEND_LOGS_TO]'
      Content-Type: application/json
    encoding: json
    tls:
      insecure: true
processors:
  batch: null
service:
  pipelines:
    logs:
      receivers:
        - otlp
      processors:
        - batch
      exporters:
        - otlphttp
```

The configuration above sets up the OTLP receiver to receive logs and the OTEL HTTP exporter to send logs to Parseable. The exporter configuration includes the Parseable endpoint, authorization headers, and the log source and dataset names.

Please ensure to change the `[PARSEABLE_URL]`, `[BASIC_AUTH_TOKEN]`, and `[NAME_OF THE_STREAM_TO_SEND_LOGS_TO]` placeholders with the actual values. The `[PARSEABLE_URL]` is the Parseable ingestor's endpoint to send logs to, like `http://ingestor.demo.parseable.com`. The `[BASIC_AUTH_TOKEN]` is the basic auth token to authenticate with Parseable. The `[NAME_OF THE_STREAM_TO_SEND_LOGS_TO]` is the name of the dataset in Parseable to send logs to.

### Start the OpenTelemetry Collector

After you have update the configuration file successfully (replaced the placeholders), start the OpenTelemetry Collector with the updated configuration file. For example, for a configuration file named `config.yaml` with OTEL Collector binary named `otel`, you can start the collector with the following command:

```bash
./otelcol --config ./config.yaml
```

Now the collector is running on HTTP port `4317` and gRPC port `4318`. By default, Parseable's `/v1/logs` endpoint is active, so it will ingest the logs directly.


# Prometheus (/docs/ingest-data/logging-agents/prometheus)



Parseable supports ingesting metrics from Prometheus and Prometheus-compatible sources. You can use native remote write, or collect metrics via Fluent Bit or OpenTelemetry Collector.

## Remote Write

To configure Prometheus to send metrics directly to Parseable using remote write, add the following to your Prometheus configuration file:

```yaml
remote_write:
  - url: "http://<parseable-endpoint>:8000/api/v1/ingest"
    basic_auth:
      username: <username>
      password: <password>
    headers:
      X-P-Stream: prometheus-metrics
```

## Fluent Bit with OpenTelemetry Output

Fluent Bit can scrape Prometheus metrics from any application exposing a `/metrics` endpoint and forward them to Parseable using the OpenTelemetry output plugin.

```ini
[SERVICE]
    Flush              5
    Log_Level          info

[INPUT]
    Name               prometheus_scrape
    Host               my-app           # Target host exposing Prometheus metrics
    Port               9090             # Prometheus metrics port
    Metrics_Path       /metrics         # Standard Prometheus metrics endpoint
    Scrape_Interval    2s               # Scrape metrics every 2 seconds

[OUTPUT]
    Name                  opentelemetry
    Match                 *
    Host                  parseable
    Port                  8000
    Metrics_uri           /v1/metrics
    Log_response_payload  True
    Tls                   Off
    Http_User             admin
    Http_Passwd           admin
    Header                X-P-Stream prometheus-metrics
    Header                X-P-Log-Source otel-metrics
    Add_label             app fluent-bit
```

### Example Targets

Adjust `Host` and `Port` to scrape different sources:

| Target         | Host             | Port   |
| -------------- | ---------------- | ------ |
| Node Exporter  | `node-exporter`  | `9100` |
| Kubernetes API | `kube-apiserver` | `6443` |
| Custom App     | `my-app`         | `8080` |

## OpenTelemetry Collector with Prometheus Receiver

Use the OpenTelemetry Collector to scrape Prometheus metrics and export to Parseable:

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: 'my-app'
          scrape_interval: 15s
          static_configs:
            - targets: ['my-app:9090']

exporters:
  otlphttp/parseable:
    endpoint: "http://parseable:8000"
    headers:
      Authorization: "Basic <base64 encoded username:password>"
      X-P-Stream: prometheus-metrics
      X-P-Log-Source: otel-metrics
      Content-Type: application/json
    encoding: json
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      receivers: [prometheus]
      exporters: [otlphttp/parseable]
```

## Features

* **Long-term Storage**: Store your Prometheus metrics in Parseable for long-term retention and analysis.
* **SQL Queries**: Query your metrics using standard SQL syntax.
* **Cost Effective**: Leverage Parseable's efficient storage to reduce costs compared to traditional time-series databases.
* **Unified Observability**: Store metrics alongside logs and traces for correlated analysis.

## Best Practices

1. **Stream Naming**: Use descriptive dataset names to organize your metrics by application or environment.
2. **Retention Policies**: Configure appropriate retention policies based on your compliance and analysis needs.
3. **Query Optimization**: Use appropriate time ranges and filters when querying large metric datasets.


# Promtail (/docs/ingest-data/logging-agents/promtail)



Ship logs from Promtail to Parseable using the HTTP client.

## Overview

Integrate Promtail with Parseable to:

* **Kubernetes Native** - Designed for Kubernetes log collection
* **Service Discovery** - Automatic target discovery
* **Label Extraction** - Rich labeling capabilities
* **Pipeline Stages** - Powerful log processing

## Prerequisites

* Promtail installed
* Parseable instance accessible
* Kubernetes cluster (for k8s deployments)

## Promtail Configuration

### Basic Configuration

Create `promtail-config.yaml`:

```yaml
server:
  http_listen_port: 9080
  grpc_listen_port: 0

positions:
  filename: /tmp/positions.yaml

clients:
  - url: http://parseable:8000/api/v1/ingest
    headers:
      Authorization: Basic YWRtaW46YWRtaW4=
      X-P-Stream: promtail-logs
    batchwait: 1s
    batchsize: 1048576

scrape_configs:
  - job_name: system
    static_configs:
      - targets:
          - localhost
        labels:
          job: varlogs
          __path__: /var/log/*log
```

### Kubernetes Pod Logs

```yaml
server:
  http_listen_port: 9080

positions:
  filename: /run/promtail/positions.yaml

clients:
  - url: http://parseable:8000/api/v1/ingest
    headers:
      Authorization: Basic YWRtaW46YWRtaW4=
      X-P-Stream: k8s-logs

scrape_configs:
  - job_name: kubernetes-pods
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_label_app]
        target_label: app
      - source_labels: [__meta_kubernetes_namespace]
        target_label: namespace
      - source_labels: [__meta_kubernetes_pod_name]
        target_label: pod
    pipeline_stages:
      - cri: {}
```

### JSON Log Parsing

```yaml
scrape_configs:
  - job_name: json-logs
    static_configs:
      - targets:
          - localhost
        labels:
          job: app
          __path__: /var/log/app/*.json
    pipeline_stages:
      - json:
          expressions:
            level: level
            message: message
            timestamp: timestamp
      - labels:
          level:
      - timestamp:
          source: timestamp
          format: RFC3339
```

### Multi-line Logs

```yaml
scrape_configs:
  - job_name: multiline
    static_configs:
      - targets:
          - localhost
        labels:
          job: java-app
          __path__: /var/log/java/*.log
    pipeline_stages:
      - multiline:
          firstline: '^\d{4}-\d{2}-\d{2}'
          max_wait_time: 3s
      - regex:
          expression: '^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (?P<level>\w+) (?P<message>.*)'
      - labels:
          level:
```

## Running Promtail

### Docker

```bash
docker run -d \
  --name promtail \
  -v $(pwd)/promtail-config.yaml:/etc/promtail/config.yaml \
  -v /var/log:/var/log:ro \
  grafana/promtail:latest \
  -config.file=/etc/promtail/config.yaml
```

### Docker Compose

```yaml
version: '3.8'
services:
  promtail:
    image: grafana/promtail:latest
    volumes:
      - ./promtail-config.yaml:/etc/promtail/config.yaml
      - /var/log:/var/log:ro
    command: -config.file=/etc/promtail/config.yaml
```

### Kubernetes DaemonSet

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: promtail
spec:
  selector:
    matchLabels:
      app: promtail
  template:
    metadata:
      labels:
        app: promtail
    spec:
      serviceAccountName: promtail
      containers:
        - name: promtail
          image: grafana/promtail:latest
          args:
            - -config.file=/etc/promtail/config.yaml
          volumeMounts:
            - name: config
              mountPath: /etc/promtail
            - name: varlog
              mountPath: /var/log
              readOnly: true
            - name: varlibdockercontainers
              mountPath: /var/lib/docker/containers
              readOnly: true
      volumes:
        - name: config
          configMap:
            name: promtail-config
        - name: varlog
          hostPath:
            path: /var/log
        - name: varlibdockercontainers
          hostPath:
            path: /var/lib/docker/containers
```

## Pipeline Stages

### Common Stages

| Stage       | Description            |
| ----------- | ---------------------- |
| `json`      | Parse JSON logs        |
| `regex`     | Extract with regex     |
| `labels`    | Add labels             |
| `timestamp` | Parse timestamps       |
| `multiline` | Handle multi-line logs |
| `drop`      | Drop matching logs     |
| `output`    | Set log content        |

### Example Pipeline

```yaml
pipeline_stages:
  - json:
      expressions:
        level: level
        msg: message
        ts: timestamp
  - labels:
      level:
  - timestamp:
      source: ts
      format: RFC3339Nano
  - output:
      source: msg
```

## Configuration Options

| Parameter             | Description             |
| --------------------- | ----------------------- |
| `clients[].url`       | Parseable endpoint      |
| `clients[].headers`   | HTTP headers            |
| `clients[].batchwait` | Max wait before sending |
| `clients[].batchsize` | Max batch size in bytes |

## Best Practices

1. **Use Service Discovery** - Leverage Kubernetes SD
2. **Add Labels** - Include relevant metadata
3. **Parse Structured Logs** - Extract fields from JSON
4. **Handle Multi-line** - Configure for stack traces
5. **Monitor Promtail** - Check metrics endpoint

## Troubleshooting

### Logs Not Appearing

1. Check Promtail logs for errors
2. Verify file paths are correct
3. Check permissions on log files
4. Verify Parseable endpoint is accessible

### Label Issues

1. Check relabel\_configs syntax
2. Verify source\_labels exist
3. Test with promtool

## Next Steps

* Configure [Fluent Bit](/docs/ingest-data/logging-agents) as alternative
* Set up [alerts](/docs/user-guide/alerting) for log patterns
* Create [dashboards](/docs/user-guide/dashboards) for monitoring


# Syslog-ng (/docs/ingest-data/logging-agents/syslog)



syslog-ng allows you to collect, parse, classify, rewrite and correlate logs from across your infrastructure and store or route them to log analysis tools. syslog-ng implements syslog protocol for Unix and Unix-like systems. syslog-ng can be configured to send logs to Parseable with [HTTP forward](https://www.syslog-ng.com/technical-documents/doc/syslog-ng-open-source-edition/3.37/administration-guide/40#TOPIC-1829058) and JSON output format.

This document explains how to set up syslog-ng to ship logs to Parseable. We use a demo application [Flog](https://github.com/mingrammer/flog) running in Docker Compose to generate logs.

## Docker Compose

Please ensure Docker Compose [installed on your machine](https://docs.docker.com/compose/install/).

```bash
mkdir parseable
cd parseable
wget https://www.parseable.com/syslog-ng/syslog-ng.conf
wget https://www.parseable.com/syslog-ng/docker-compose.yaml
docker-compose up -d
```

You can now access the Parseable dashboard on `http://localhost:8000`. You should see a dataset called `demo` populated with log data generated by the [flog container](https://github.com/mingrammer/flog).


# Vector (/docs/ingest-data/logging-agents/vector)



This document explains how to set up [Vector](https://vector.dev) to ship logs to Parseable on a Kubernetes cluster. We use Vector's kubernetes\_logs source to collect logs from Kubernetes pods. Then we use the http sink to send logs to Parseable.

## Kubernetes

Please ensure kubectl and helm installed and configured to access your Kubernetes cluster.

Parseable installed on your Kubernetes cluster. Refer the [Parseable Kubernetes documentation](https://www.parseable.com/docs/self-hosted/installation/distributed/k8s-helm).

### Install Vector

We use the official [Vector Helm chart](https://github.com/vectordotdev/helm-charts). But, we'll use a modified values.yaml file, that contains the configuration for Vector to send logs to Parseable.

```bash
wget https://www.parseable.com/vector/values.yaml
helm repo add vector https://helm.vector.dev

helm install vector vector/vector \
  --namespace vector \
  --create-namespace \
  --values values.yaml
```

Let's take a deeper look at the Vector sink configuration in `values.yaml`. Important to notice here is that we use the sink type http. Source can be any of the supported sources by Vector.

```yaml
  sources:
    kubernetes_logs:
      type: kubernetes_logs
  sinks:
    parseable:
      type: http
      method: post
      batch:
        max_bytes: 10485760
        max_events: 1000
        timeout_secs: 10
      compression: gzip
      inputs: 
        - kubernetes_logs
      encoding:
        codec: json
      uri: 'http://parseable.parseable.svc.cluster.local/api/v1/ingest'
      auth:
        strategy: basic
        user: admin
        password: admin
      request:
        headers:
          X-P-Stream: vectordemo  ## dataset/dataset name
      healthcheck:
        enabled: true
        path: 'http://parseable.parseable.svc.cluster.local/api/v1/liveness'
        port: 80
```

## Batching and Compression

Parseable supports batching and compressing the log data before sending it via HTTP POST. Vector supports this feature via the batch and compression options. We recommend enabling both of these options to reduce the number of HTTP requests and to reduce the size of the HTTP payload.

## Check logs in Parseable

If you've not already done so, port-forward Parseable service to access the dashboard with `kubectl`:

```bash
kubectl port-forward svc/parseable 8000:80 -n parseable
```

You can now check the Parseable server `vectordemo` dataset to see the logs from this setup.


# OpenTelemetry (/docs/ingest-data/otel)



import { IconFileText, IconChartBar, IconRoute } from '@tabler/icons-react';

Parseable provides native support for OpenTelemetry, the open-source observability framework that helps you collect, process, and export telemetry data. Learn how to integrate Parseable with OpenTelemetry to ingest and analyze your logs, metrics, and traces with zero configuration.

<Cards>
  <Card href="/docs/ingest-data/otel/logs" icon={<IconFileText className="text-purple-600" />} title="Logs">
    Ingest and analyze OpenTelemetry logs with Parseable's native support. Collect structured log data from your applications and infrastructure.
  </Card>

  <Card href="/docs/ingest-data/otel/metrics" icon={<IconChartBar className="text-purple-600" />} title="Metrics">
    Capture and visualize OpenTelemetry metrics to monitor the performance and health of your systems in real-time.
  </Card>

  <Card href="/docs/ingest-data/otel/traces" icon={<IconRoute className="text-purple-600" />} title="Traces">
    Track request flows across distributed systems with OpenTelemetry traces to identify bottlenecks and troubleshoot issues.
  </Card>
</Cards>


# Logs (/docs/ingest-data/otel/logs)



Parseable enables ingesting the OpenTelemetry logs sent from the OTEL collectors in the JSON format. In order to do so, Parseable exposes default endpoint /v1/logs at which the OTEL collector sends the log data.

Below is the sample configuration of the OTEL collector to send the logs to Parseable

```yaml
exporters:
  otlphttp/parseablelogs:
    endpoint: "<parseable-endpoint> eg. http://localhost:8000"
    headers:
      Authorization: "Basic <base64 encoded string of username:password>"
      X-P-Stream: otel-logs     # dataset/dataset name
      X-P-Log-Source: otel-logs
      Content-Type: application/json
    encoding: json
    tls:
      insecure: true

service:
  pipelines:
    logs:
      exporters: [otlphttp/parseablelogs]
```

## Support for Protocol Buffers

<OfferingPills pro enterprise className="mb-4" />

Parseable also supports ingesting the OpenTelemetry logs sent from the OTEL collectors in the Protocol Buffers format. Below is an example configuration of the OTEL collector to send the logs to Parseable in the Protocol Buffers format.

```yaml
exporters:
  otlphttp/parseablelogs:
    endpoint: "http://parseable:8000"
    headers:
      Authorization: "Basic YWRtaW46YWRtaW4="  # admin:admin in base64
      X-P-Stream: otel-logs      # dataset/dataset name
      X-P-Log-Source: otel-logs
      Content-Type: application/x-protobuf
    encoding: proto
    tls:
      insecure: true
service:
  pipelines:
    logs:
      exporters: [otlphttp/parseablelogs]
```

## Data flattening

The OpenTelemetry logs that are in the form of a nested JSON. When the log event is received at `/v1/logs` endpoint, Parseable will flatten the nested JSON to a flat JSON object. This is done to make the data more queryable and filterable. Here's a quick comparison of the nested JSON and the flattened JSON:

### OTEL JSON format sample:

```json
{
  "resourceLogs": [
    {
      "resource": {
        "attributes": [
          {
            "key": "container.id",
            "value": {
              "stringValue": "61625241a33e64c6c34de99b1827a713b630f5548e715a87c6f8d052f1e3a2ab"
            }
          },
          {
            "key": "docker.cli.cobra.command_path",
            "value": {
              "stringValue": "docker compose"
            }
          },
          {
            "key": "host.arch",
            "value": {
              "stringValue": "amd64"
            }
          },
          {
            "key": "host.name",
            "value": {
              "stringValue": "61625241a33e"
            }
          },
          {
            "key": "os.description",
            "value": {
              "stringValue": "Linux 5.15.167.4-microsoft-standard-WSL2"
            }
          },
          {
            "key": "os.type",
            "value": {
              "stringValue": "linux"
            }
          },
          {
            "key": "process.command_line",
            "value": {
              "stringValue": "/opt/java/openjdk/bin/java -Xmx400m -Xms400m -XX:SharedArchiveFile=/opt/kafka/kafka.jsa -Xlog:gc*:file=/opt/kafka/bin/../logs/kafkaServer-gc.log:time,tags:filecount=10,filesize=100M -Dcom.sun.management.jmxremote=true -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Dkafka.logs.dir=/opt/kafka/bin/../logs -Dlog4j.configuration=file:/opt/kafka/bin/../config/log4j.properties -javaagent:/tmp/opentelemetry-javaagent.jar -Dotel.jmx.target.system=kafka-broker kafka.Kafka /opt/kafka/config/server.properties"
            }
          },
          {
            "key": "process.executable.path",
            "value": {
              "stringValue": "/opt/java/openjdk/bin/java"
            }
          },
          {
            "key": "process.pid",
            "value": {
              "intValue": "1"
            }
          },
          {
            "key": "process.runtime.description",
            "value": {
              "stringValue": "Eclipse Adoptium OpenJDK 64-Bit Server VM 21.0.2+13-LTS"
            }
          },
          {
            "key": "process.runtime.name",
            "value": {
              "stringValue": "OpenJDK Runtime Environment"
            }
          },
          {
            "key": "process.runtime.version",
            "value": {
              "stringValue": "21.0.2+13-LTS"
            }
          },
          {
            "key": "service.instance.id",
            "value": {
              "stringValue": "eff8a3d7-15f2-4718-94e5-6b984a9c18d7"
            }
          },
          {
            "key": "service.name",
            "value": {
              "stringValue": "kafka"
            }
          },
          {
            "key": "telemetry.distro.name",
            "value": {
              "stringValue": "opentelemetry-java-instrumentation"
            }
          },
          {
            "key": "telemetry.distro.version",
            "value": {
              "stringValue": "2.9.0"
            }
          },
          {
            "key": "telemetry.sdk.language",
            "value": {
              "stringValue": "java"
            }
          },
          {
            "key": "telemetry.sdk.name",
            "value": {
              "stringValue": "opentelemetry"
            }
          },
          {
            "key": "telemetry.sdk.version",
            "value": {
              "stringValue": "1.43.0"
            }
          }
        ]
      },
      "scopeLogs": [
        {
          "scope": {
            "name": "kafka.server.BrokerServer"
          },
          "logRecords": [
            {
              "timeUnixNano": "1735735228333091540",
              "observedTimeUnixNano": "1735735228333101306",
              "severityNumber": 9,
              "severityText": "INFO",
              "body": {
                "stringValue": "[BrokerServer id=1] Transition from STARTED to SHUTTING_DOWN"
              },
              "traceId": "",
              "spanId": ""
            }
          ]
        }
      ]
    }
  ]
}
```

### Flattened JSON

```json
{
  "body": "[BrokerServer id=1] Transition from STARTED to SHUTTING_DOWN",
  "container.id": "61625241a33e64c6c34de99b1827a713b630f5548e715a87c6f8d052f1e3a2ab",
  "docker.cli.cobra.command_path": "docker compose",
  "flags": 0,
  "host.arch": "amd64",
  "host.name": "61625241a33e",
  "log_record_dropped_attributes_count": 0,
  "observable_time_unix_nano": 1735735228333101300,
  "os.description": "Linux 5.15.167.4-microsoft-standard-WSL2",
  "os.type": "linux",
  "p_metadata": "",
  "p_tags": "",
  "p_timestamp": "2025-01-01T23:15:01.661+05:30",
  "process.command_line": "/opt/java/openjdk/bin/java -Xmx400m -Xms400m -XX:SharedArchiveFile=/opt/kafka/kafka.jsa -Xlog:gc*:file=/opt/kafka/bin/../logs/kafkaServer-gc.log:time,tags:filecount=10,filesize=100M -Dcom.sun.management.jmxremote=true -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Dkafka.logs.dir=/opt/kafka/bin/../logs -Dlog4j.configuration=file:/opt/kafka/bin/../config/log4j.properties -javaagent:/tmp/opentelemetry-javaagent.jar -Dotel.jmx.target.system=kafka-broker kafka.Kafka /opt/kafka/config/server.properties",
  "process.executable.path": "/opt/java/openjdk/bin/java",
  "process.pid": "1",
  "process.runtime.description": "Eclipse Adoptium OpenJDK 64-Bit Server VM 21.0.2+13-LTS",
  "process.runtime.name": "OpenJDK Runtime Environment",
  "process.runtime.version": "21.0.2+13-LTS",
  "resource_dropped_attributes_count": 0,
  "schema_url": "",
  "scope_dropped_attributes_count": 0,
  "scope_log_schema_url": "",
  "scope_name": "kafka.server.BrokerServer",
  "scope_version": "",
  "service.instance.id": "eff8a3d7-15f2-4718-94e5-6b984a9c18d7",
  "service.name": "kafka",
  "severity_number": 9,
  "p_log_category": "INFO",
  "severity_text": "SEVERITY_NUMBER_INFO",
  "span_id": "",
  "telemetry.distro.name": "opentelemetry-java-instrumentation",
  "telemetry.distro.version": "2.9.0",
  "telemetry.sdk.language": "java",
  "telemetry.sdk.name": "opentelemetry",
  "telemetry.sdk.version": "1.43.0",
  "time_unix_nano": 1735735228333091600,
  "trace_id": ""
}
```

All the resource attributes are stored as key-value pair where each attribute key becomes the field and the value, which may be of one of `stringValue/intValue/doubleValue etc`, becomes the value for that particular field.

Each log record in the incoming log event is stored as individual record in Parseable and all resource attributes, scope name, version etc which are at the scope level (parent of logRecords) are copied in each ingested record.

### Flattening of body field

In addition to top level flattening, if the `body` field is a valid JSON string, Parseable automatically flattens its key-value pairs into separate fields in the ingested record. Each key is prefixed with `body_`. The original `body` field is also preserved as-is.

For example, if a log body is:

```json
"body": "{\"request_id\": \"abc-123\", \"status\": \"ok\"}",
```

The ingested record will contain:

```json
{
  "body": "{\"request_id\": \"abc-123\", \"status\": \"ok\"}",
  "body_request_id": "abc-123",
  "body_status": "ok"
}
```

This makes individual fields within the log body directly queryable and filterable without needing to parse JSON at query time.

## Log categorization

Parseable automatically adds a `p_log_category` field to every ingested OTel log record. This field contains one of the following values: `FATAL`, `ERROR`, `WARN`, `INFO`, `DEBUG`, `TRACE`, or `UNSPECIFIED`.

The category is derived using the following logic:

1. **Severity number mapping** — If the log record has a `severity_number` set (non-zero), it is mapped directly to a category:
   * 1–4 → `TRACE`
   * 5–8 → `DEBUG`
   * 9–12 → `INFO`
   * 13–16 → `WARN`
   * 17–20 → `ERROR`
   * 21–24 → `FATAL`

2. **Body text fallback** — If `severity_number` is unset (0 / UNSPECIFIED), Parseable scans the log body for a case-insensitive substring match against the category names (`FATAL`, `ERROR`, `WARN`, `INFO`, `DEBUG`, `TRACE`).

3. **Default** — If neither method yields a result, the category is set to `UNSPECIFIED`.

This categorization allows users to easily filter and analyze logs based on severity, even if the original log records do not have structured severity information.


# Metrics (/docs/ingest-data/otel/metrics)



Parseable enables ingesting the OpenTelemetry metrics sent from the OTEL collectors in the JSON format. In order to do so, Parseable exposes default endpoint `/v1/metrics` at which the OTEL collector sends the metric data.

Below is the sample configuration of the OTEL collector to send the metrics to Parseable

```yaml
exporters:
  otlphttp/parseablemetrics:
    endpoint: "<parseable-endpoint> eg. http://localhost:8000"
    headers:
      Authorization: "Basic <base64 encoded string of username:password>"
      X-P-Stream: otel-metrics     # dataset/dataset name
      X-P-Log-Source: otel-metrics
      Content-Type: application/json
    encoding: json
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      exporters: [otlphttp/parseablemetrics]
```

## Support for Protocol Buffers

<OfferingPills pro enterprise className="mb-4" />

Parseable also supports ingesting the OpenTelemetry Metrics sent from the OTEL collectors in the Protocol Buffers format. Below is an example configuration of the OTEL collector to send the metrics to Parseable in the Protocol Buffers format.

```yaml
exporters:
  otlphttp/parseablemetrics:
    endpoint: "http://parseable:8000"
    headers:
      Authorization: "Basic YWRtaW46YWRtaW4="  # admin:admin in base64
      X-P-Stream: otel-metrics       # dataset/dataset name
      X-P-Log-Source: otel-metrics
      Content-Type: application/x-protobuf
    encoding: proto
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      exporters: [otlphttp/parseablemetrics]
```

## Data Flattening

The OpenTelemetry metrics that are in the form of a nested JSON. When the metric event is received at `/v1/metrics` endpoint, Parseable will flatten the nested JSON to a flat JSON object. This is done to make the data more queryable and filterable. Here's a quick comparison of the nested JSON and the flattened JSON:

OTEL JSON format sample:

```json
{
  "resourceMetrics": [
    {
      "resource": {
        "attributes": [
          {
            "key": "service.name",
            "value": {
              "stringValue": "otelcol"
            }
          },
          {
            "key": "service.instance.id",
            "value": {
              "stringValue": "0.0.0.0:8888"
            }
          },
          {
            "key": "net.host.port",
            "value": {
              "stringValue": "8888"
            }
          },
          {
            "key": "http.scheme",
            "value": {
              "stringValue": "http"
            }
          },
          {
            "key": "server.port",
            "value": {
              "stringValue": "8888"
            }
          },
          {
            "key": "url.scheme",
            "value": {
              "stringValue": "http"
            }
          },
          {
            "key": "service_instance_id",
            "value": {
              "stringValue": "45df285f-1c8a-4fcf-8a7c-8e8ebc6ee068"
            }
          },
          {
            "key": "service_name",
            "value": {
              "stringValue": "otelcol-contrib"
            }
          },
          {
            "key": "service_version",
            "value": {
              "stringValue": "0.113.0"
            }
          }
        ]
      },
      "scopeMetrics": [
        {
          "scope": {
            "name": "github.com/open-telemetry/opentelemetry-collector-contrib/receiver/prometheusreceiver",
            "version": "0.113.0"
          },
          "metrics": [
            {
              "name": "otelcol_receiver_accepted_log_records",
              "description": "Number of log records successfully pushed into the pipeline.",
              "sum": {
                "dataPoints": [
                  {
                    "attributes": [
                      {
                        "key": "receiver",
                        "value": {
                          "stringValue": "otlp"
                        }
                      },
                      {
                        "key": "service_instance_id",
                        "value": {
                          "stringValue": "45df285f-1c8a-4fcf-8a7c-8e8ebc6ee068"
                        }
                      },
                      {
                        "key": "service_name",
                        "value": {
                          "stringValue": "otelcol-contrib"
                        }
                      },
                      {
                        "key": "service_version",
                        "value": {
                          "stringValue": "0.113.0"
                        }
                      },
                      {
                        "key": "transport",
                        "value": {
                          "stringValue": "grpc"
                        }
                      }
                    ],
                    "startTimeUnixNano": "1734185431888000000",
                    "timeUnixNano": "1734185431888000000",
                    "asDouble": 11
                  },
                  {
                    "attributes": [
                      {
                        "key": "receiver",
                        "value": {
                          "stringValue": "otlp"
                        }
                      },
                      {
                        "key": "service_instance_id",
                        "value": {
                          "stringValue": "45df285f-1c8a-4fcf-8a7c-8e8ebc6ee068"
                        }
                      },
                      {
                        "key": "service_name",
                        "value": {
                          "stringValue": "otelcol-contrib"
                        }
                      },
                      {
                        "key": "service_version",
                        "value": {
                          "stringValue": "0.113.0"
                        }
                      },
                      {
                        "key": "transport",
                        "value": {
                          "stringValue": "http"
                        }
                      }
                    ],
                    "startTimeUnixNano": "1734185431888000000",
                    "timeUnixNano": "1734185431888000000",
                    "asDouble": 4
                  }
                ],
                "aggregationTemporality": 2,
                "isMonotonic": true
              },
              "metadata": [
                {
                  "key": "prometheus.type",
                  "value": {
                    "stringValue": "counter"
                  }
                }
              ]
            }
          ]
        }
      ]
    }
  ] 
}
```

#### Flattened JSON:

```json
[
  {
    "aggregation_temporality": 2,
    "aggregation_temporality_description": "AGGREGATION_TEMPORALITY_CUMULATIVE",
    "http.scheme": "http",
    "metric_description": "Number of log records successfully pushed into the pipeline.",
    "metric_name": "otelcol_receiver_accepted_log_records",
    "metric_unit": "",
    "net.host.port": "8888",
    "p_metadata": "",
    "p_tags": "",
    "p_timestamp": "2025-01-02T00:00:08.290+05:30",
    "prometheus.type": "counter",
    "resource_dropped_attributes_count": 0,
    "resource_metrics_schema_url": "",
    "scope_dropped_attributes_count": 0,
    "scope_metrics_schema_url": "",
    "scope_name": "github.com/open-telemetry/opentelemetry-collector-contrib/receiver/prometheusreceiver",
    "scope_version": "0.113.0",
    "server.port": "8888",
    "service.instance.id": "0.0.0.0:8888",
    "service.name": "otelcol",
    "service_instance_id": "45df285f-1c8a-4fcf-8a7c-8e8ebc6ee068",
    "service_name": "otelcol-contrib",
    "service_version": "0.113.0",
    "sum_data_point_flags": 0,
    "sum_data_point_flags_description": "DATA_POINT_FLAGS_DO_NOT_USE",
    "sum_data_point_value_as_double": 11,
    "sum_is_monotonic": true,
    "sum_receiver": "otlp",
    "sum_service_instance_id": "45df285f-1c8a-4fcf-8a7c-8e8ebc6ee068",
    "sum_service_name": "otelcol-contrib",
    "sum_service_version": "0.113.0",
    "sum_start_time_unix_nano": 1734185431888000000,
    "sum_time_unix_nano": 1734185431888000000,
    "sum_transport": "grpc",
    "url.scheme": "http"
  },
  {
    "aggregation_temporality": 2,
    "aggregation_temporality_description": "AGGREGATION_TEMPORALITY_CUMULATIVE",
    "http.scheme": "http",
    "metric_description": "Number of log records successfully pushed into the pipeline.",
    "metric_name": "otelcol_receiver_accepted_log_records",
    "metric_unit": "",
    "net.host.port": "8888",
    "p_metadata": "",
    "p_tags": "",
    "p_timestamp": "2025-01-02T00:00:08.292+05:30",
    "prometheus.type": "counter",
    "resource_dropped_attributes_count": 0,
    "resource_metrics_schema_url": "",
    "scope_dropped_attributes_count": 0,
    "scope_metrics_schema_url": "",
    "scope_name": "github.com/open-telemetry/opentelemetry-collector-contrib/receiver/prometheusreceiver",
    "scope_version": "0.113.0",
    "server.port": "8888",
    "service.instance.id": "0.0.0.0:8888",
    "service.name": "otelcol",
    "service_instance_id": "45df285f-1c8a-4fcf-8a7c-8e8ebc6ee068",
    "service_name": "otelcol-contrib",
    "service_version": "0.113.0",
    "sum_data_point_flags": 0,
    "sum_data_point_flags_description": "DATA_POINT_FLAGS_DO_NOT_USE",
    "sum_data_point_value_as_double": 4,
    "sum_is_monotonic": true,
    "sum_receiver": "otlp",
    "sum_service_instance_id": "45df285f-1c8a-4fcf-8a7c-8e8ebc6ee068",
    "sum_service_name": "otelcol-contrib",
    "sum_service_version": "0.113.0",
    "sum_start_time_unix_nano": 1734185431888000000,
    "sum_time_unix_nano": 1734185431888000000,
    "sum_transport": "http",
    "url.scheme": "http"
  }
]
```

All the resource attributes are stored as key-value pair where each attribute key becomes the field and the value, which may be of one of `stringValue/intValue/doubleValue etc`, becomes the value for that particular field.

Each metric record has data which is one of `sum` `gauge` `histogram` `exponentialHistogram` `summary` type.

Each data has one or more data points. Each data point is stored as individual record in Parseable and all resource attributes, scope name, version, other metric elements such as metric name, description, metadata etc are copied in each ingested record. In the above example, there are 2 dataPoints under `sum` record, thus, Parseable stores the incoming event as 2 records making it simpler to query and analyse.


# Traces (/docs/ingest-data/otel/traces)



Parseable enables ingesting the OpenTelemetry traces sent from the OTEL collectors in the JSON format. In order to do so, Parseable exposes default endpoint /v1/traces at which the OTEL collector sends the span data.

Below is the sample configuration of the OTEL collector to send the traces to Parseable

```yaml
exporters:
  otlphttp/parseabletraces:
    endpoint: "<parseable-endpoint> eg. http://localhost:8000"
    headers:
      Authorization: "Basic <base64 encoded string of username:password>"
      X-P-Stream: otel-traces       # dataset/dataset name
      X-P-Log-Source: otel-traces
      Content-Type: application/json
    encoding: json
    tls:
      insecure: true

service:
  pipelines:
    traces:
      exporters: [otlphttp/parseabletraces]
```

## Support for Protocol Buffers

<OfferingPills pro enterprise className="mb-4" />

Parseable also supports ingesting the OpenTelemetry Traces sent from the OTEL collectors in the Protocol Buffers format. Below is an example configuration of the OTEL collector to send the traces to Parseable in the Protocol Buffers format.

```yaml
exporters:
  otlphttp/parseabletraces:
    endpoint: "http://parseable:8000"
    headers:
      Authorization: "Basic YWRtaW46YWRtaW4="  # admin:admin in base64
      X-P-Stream: otel-traces        # dataset/dataset name
      X-P-Log-Source: otel-traces
      Content-Type: application/x-protobuf
    encoding: proto
    tls:
      insecure: true

service:
  pipelines:
    traces:
      exporters: [otlphttp/parseabletraces]
```

## Data Flattening

The OpenTelemetry traces that are in the form of a nested JSON. When the log event is received at `/v1/traces` endpoint, Parseable will flatten the nested JSON to a flat JSON object. This is done to make the data more queryable and filterable. Here's a quick comparison of the nested JSON and the flattened JSON:

OTEL JSON format sample:

```json
{
  "resourceSpans": [
    {
      "resource": {
        "attributes": [
          {
            "key": "service.name",
            "value": {
              "stringValue": "frontend-web"
            }
          },
          {
            "key": "telemetry.sdk.language",
            "value": {
              "stringValue": "webjs"
            }
          },
          {
            "key": "telemetry.sdk.name",
            "value": {
              "stringValue": "opentelemetry"
            }
          },
          {
            "key": "telemetry.sdk.version",
            "value": {
              "stringValue": "1.25.1"
            }
          },
          {
            "key": "process.runtime.name",
            "value": {
              "stringValue": "browser"
            }
          },
          {
            "key": "process.runtime.description",
            "value": {
              "stringValue": "Web Browser"
            }
          },
          {
            "key": "process.runtime.version",
            "value": {
              "stringValue": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/120.0.6099.28 Safari/537.36"
            }
          }
        ]
      },
      "scopeSpans": [
        {
          "scope": {
            "name": "@opentelemetry/instrumentation-fetch",
            "version": "0.52.1"
          },
          "spans": [
            {
              "traceId": "d43eb15c7303ad1951047e10bd22b5c3",
              "spanId": "c1250f476d1acff9",
              "parentSpanId": "",
              "name": "HTTP GET",
              "kind": 3,
              "startTimeUnixNano": "1734185431811000000",
              "endTimeUnixNano": "1734185431956000000",
              "attributes": [
                {
                  "key": "component",
                  "value": {
                    "stringValue": "fetch"
                  }
                },
                {
                  "key": "http.method",
                  "value": {
                    "stringValue": "GET"
                  }
                },
                {
                  "key": "http.url",
                  "value": {
                    "stringValue": "http://frontend-proxy:8080/api/recommendations?productIds=\\u0026sessionId=8b1a837b-17a5-40a4-abed-c7bc419eb91e\\u0026currencyCode=USD"
                  }
                },
                {
                  "key": "session.id",
                  "value": {
                    "stringValue": "8b1a837b-17a5-40a4-abed-c7bc419eb91e"
                  }
                },
                {
                  "key": "app.synthetic_request",
                  "value": {
                    "stringValue": "true"
                  }
                },
                {
                  "key": "http.status_code",
                  "value": {
                    "intValue": "200"
                  }
                },
                {
                  "key": "http.status_text",
                  "value": {
                    "stringValue": "OK"
                  }
                },
                {
                  "key": "http.host",
                  "value": {
                    "stringValue": "frontend-proxy:8080"
                  }
                },
                {
                  "key": "http.scheme",
                  "value": {
                    "stringValue": "http"
                  }
                },
                {
                  "key": "http.user_agent",
                  "value": {
                    "stringValue": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/120.0.6099.28 Safari/537.36"
                  }
                },
                {
                  "key": "http.response_content_length",
                  "value": {
                    "intValue": "1165"
                  }
                },
                {
                  "key": "http.response_content_length_uncompressed",
                  "value": {
                    "intValue": "2547"
                  }
                }
              ],
              "events": [
                {
                  "timeUnixNano": "1734185431811799902",
                  "name": "fetchStart"
                },
                {
                  "timeUnixNano": "1734185431811799902",
                  "name": "domainLookupStart"
                }
              ],
              "status": {}
            }
          ]
        }
      ]
    }
  ]
}   
```

## Flattened JSON

```json
[
    {
      "app.synthetic_request": "true",
      "component": "fetch",
      "event_dropped_attributes_count": 0,
      "event_name": "fetchStart",
      "event_time_unix_nano": 1734185431811799800,
      "http.host": "frontend-proxy:8080",
      "http.method": "GET",
      "http.response_content_length": "1165",
      "http.response_content_length_uncompressed": "2547",
      "http.scheme": "http",
      "http.status_code": "200",
      "http.status_text": "OK",
      "http.url": "http://frontend-proxy:8080/api/recommendations?productIds=\\u0026sessionId=8b1a837b-17a5-40a4-abed-c7bc419eb91e\\u0026currencyCode=USD",
      "http.user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/120.0.6099.28 Safari/537.36",
      "p_metadata": "",
      "p_tags": "",
      "p_timestamp": "2025-01-01T23:47:50.691+05:30",
      "process.runtime.description": "Web Browser",
      "process.runtime.name": "browser",
      "process.runtime.version": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/120.0.6099.28 Safari/537.36",
      "resource_dropped_attributes_count": 0,
      "schema_url": "",
      "scope_dropped_attributes_count": 0,
      "scope_name": "@opentelemetry/instrumentation-fetch",
      "scope_version": "0.52.1",
      "service.name": "frontend-web",
      "session.id": "8b1a837b-17a5-40a4-abed-c7bc419eb91e",
      "span_dropped_attributes_count": 0,
      "span_dropped_events_count": 0,
      "span_dropped_links_count": 0,
      "span_end_time_unix_nano": 1734185431956000000,
      "span_flags": 0,
      "span_flags_description": "SPAN_FLAGS_DO_NOT_USE",
      "span_kind": 3,
      "span_kind_description": "SPAN_KIND_CLIENT",
      "span_name": "HTTP GET",
      "span_parent_span_id": "",
      "span_span_id": "d43eb15c7303ad1951047e10bd22b5c3",
      "span_start_time_unix_nano": 1734185431811000000,
      "span_status_code": 0,
      "span_status_description": "STATUS_CODE_UNSET",
      "span_status_message": "",
      "span_trace_id": "c1250f476d1acff9",
      "span_trace_state": "",
      "telemetry.sdk.language": "webjs",
      "telemetry.sdk.name": "opentelemetry",
      "telemetry.sdk.version": "1.25.1"
    },
    {
      "app.synthetic_request": "true",
      "component": "fetch",
      "event_dropped_attributes_count": 0,
      "event_name": "domainLookupStart",
      "event_time_unix_nano": 1734185431811799800,
      "http.host": "frontend-proxy:8080",
      "http.method": "GET",
      "http.response_content_length": "1165",
      "http.response_content_length_uncompressed": "2547",
      "http.scheme": "http",
      "http.status_code": "200",
      "http.status_text": "OK",
      "http.url": "http://frontend-proxy:8080/api/recommendations?productIds=\\u0026sessionId=8b1a837b-17a5-40a4-abed-c7bc419eb91e\\u0026currencyCode=USD",
      "http.user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/120.0.6099.28 Safari/537.36",
      "p_metadata": "",
      "p_tags": "",
      "p_timestamp": "2025-01-01T23:47:50.695+05:30",
      "process.runtime.description": "Web Browser",
      "process.runtime.name": "browser",
      "process.runtime.version": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/120.0.6099.28 Safari/537.36",
      "resource_dropped_attributes_count": 0,
      "schema_url": "",
      "scope_dropped_attributes_count": 0,
      "scope_name": "@opentelemetry/instrumentation-fetch",
      "scope_version": "0.52.1",
      "service.name": "frontend-web",
      "session.id": "8b1a837b-17a5-40a4-abed-c7bc419eb91e",
      "span_dropped_attributes_count": 0,
      "span_dropped_events_count": 0,
      "span_dropped_links_count": 0,
      "span_end_time_unix_nano": 1734185431956000000,
      "span_flags": 0,
      "span_flags_description": "SPAN_FLAGS_DO_NOT_USE",
      "span_kind": 3,
      "span_kind_description": "SPAN_KIND_CLIENT",
      "span_name": "HTTP GET",
      "span_parent_span_id": "",
      "span_span_id": "d43eb15c7303ad1951047e10bd22b5c3",
      "span_start_time_unix_nano": 1734185431811000000,
      "span_status_code": 0,
      "span_status_description": "STATUS_CODE_UNSET",
      "span_status_message": "",
      "span_trace_id": "c1250f476d1acff9",
      "span_trace_state": "",
      "telemetry.sdk.language": "webjs",
      "telemetry.sdk.name": "opentelemetry",
      "telemetry.sdk.version": "1.25.1"
    }
]
```

All the resource attributes are stored as key-value pair where each attribute key becomes the field and the value, which may be of one of `stringValue/intValue/doubleValue etc`, becomes the value for that particular field.

Each event under span record in the incoming log event is stored as individual record in Parseable and all resource or span attributes, scope name, version, span elements such as traceId, spanId, name, kind etc which are at the parent level of event are copied in each ingested record. In the above example, there are 2 events `fetchStart` and `domainLookupStart` under the span record, thus, Parseable stores the incoming event as 2 records making it simpler to query and analyse.


# C# (/docs/ingest-data/programming-languages/csharp)



### Create a dataset

First, we'll need to create a dataset. This is a one time operation, and we recommend storing log entries with same schema in a single dataset. So, for example, you can use one dataset per application (given that all logs from that application have the same schema).

```csharp
Console.WriteLine("Create dataset!");
var client = new HttpClient();
var logstream_name = "teststream";
var request = new HttpRequestMessage(HttpMethod.Put, String.Concat("http://localhost:8000/api/v1/logstream/", logstream_name));
request.Headers.Add("Authorization", "Basic YWRtaW46YWRtaW4=");
var response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();
Console.WriteLine(await response.Content.ReadAsStringAsync());
```

### Send logs to the dataset

After dataset is created, you can start sending logs to the dataset using HTTP POST requests.

```csharp
Console.WriteLine("Ingest a log event to the created dataset!");
request = new HttpRequestMessage(HttpMethod.Post, "http://localhost:8000/api/v1/ingest");
request.Headers.Add("Authorization", "Basic YWRtaW46YWRtaW4=");
request.Headers.Add("X-P-Stream", logstream_name);
var content = new StringContent("{\"source_time\":\"2024-03-27T10:29:00.434Z\",\"level\":\"info\",\"message\":\"Application is failing\",\"version\":\"1.2.0\",\"user_id\":13912,\"device_id\":4138,\"session_id\":\"abc\",\"os\":\"Windows\",\"host\":\"112.168.1.110\",\"location\":\"ngeuprqhynuvpxgp\",\"request_body\":\"rnkmffyawtdcindtrdqruyxbndbjpfsptzpwtujbmkwcqastmxwbvjwphmyvpnhordwljnodxhtvpjesjldtifswqbpyuhlcytmm\",\"status_code\":300,\"app_meta\":\"ckgpibhmlusqqfunnpxbfxbc\", \"new_field_added_by\":\"ingester 8020\"}", null, "application/json");
request.Content = content;
response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();
Console.WriteLine(await response.Content.ReadAsStringAsync());
Console.WriteLine("Log event ingested successfully!");
```

### Querying a dataset

Once you have started sending logs to a dataset, you can query the logs using standard SQL.

```csharp
Console.WriteLine("Query the dataset!");
request = new HttpRequestMessage(HttpMethod.Post, "http://localhost:8000/api/v1/query");
request.Headers.Add("Authorization", "Basic YWRtaW46YWRtaW4=");
content = new StringContent("{\n    \"query\": \"SELECT * from teststream\",\n    \"startTime\": \"2024-03-27T00:00:00.000Z\",\n    \"endTime\": \"2024-03-28T23:59:00.000Z\"\n}\n", null, "application/json");
request.Content = content;
response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();
Console.WriteLine(await response.Content.ReadAsStringAsync());
```


# .NET (/docs/ingest-data/programming-languages/dotnet)



Send logs from .NET applications to Parseable using HTTP or logging libraries.

## Overview

Integrate .NET with Parseable to:

* **Application Logs** - Send structured logs from .NET apps
* **ASP.NET Core** - Native integration with Microsoft.Extensions.Logging
* **Serilog Support** - Use with Serilog sink
* **Structured Logging** - JSON-formatted log entries

## Prerequisites

* .NET 6.0+
* Parseable instance accessible
* HttpClient or Serilog

## Basic HTTP Integration

### Using HttpClient

```csharp
using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;

public class ParseableLogger : IDisposable
{
    private readonly HttpClient _client;
    private readonly string _stream;
    private readonly List<object> _buffer = new();
    private readonly object _lock = new();
    private readonly int _batchSize;
    private readonly Timer _flushTimer;

    public ParseableLogger(string url, string dataset, string username, string password, int batchSize = 100)
    {
        _stream = dataset;
        _batchSize = batchSize;
        
        _client = new HttpClient { BaseAddress = new Uri(url) };
        var auth = Convert.ToBase64String(Encoding.UTF8.GetBytes($"{username}:{password}"));
        _client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Basic", auth);
        
        _flushTimer = new Timer(_ => Flush(), null, TimeSpan.FromSeconds(5), TimeSpan.FromSeconds(5));
    }

    public void Log(string level, string message, object? data = null)
    {
        var entry = new
        {
            timestamp = DateTime.UtcNow.ToString("yyyy-MM-ddTHH:mm:ss.fffZ"),
            level,
            message,
            data
        };

        lock (_lock)
        {
            _buffer.Add(entry);
            if (_buffer.Count >= _batchSize)
            {
                FlushInternal();
            }
        }
    }

    public void Info(string message, object? data = null) => Log("info", message, data);
    public void Error(string message, object? data = null) => Log("error", message, data);
    public void Warning(string message, object? data = null) => Log("warning", message, data);

    public void Flush()
    {
        lock (_lock)
        {
            FlushInternal();
        }
    }

    private void FlushInternal()
    {
        if (_buffer.Count == 0) return;

        var entries = _buffer.ToList();
        _buffer.Clear();

        Task.Run(async () =>
        {
            try
            {
                var json = JsonSerializer.Serialize(entries);
                var content = new StringContent(json, Encoding.UTF8, "application/json");
                content.Headers.Add("X-P-Stream", _stream);
                
                await _client.PostAsync("/api/v1/ingest", content);
            }
            catch (Exception ex)
            {
                Console.Error.WriteLine($"Failed to send logs: {ex.Message}");
            }
        });
    }

    public void Dispose()
    {
        _flushTimer.Dispose();
        Flush();
        _client.Dispose();
    }
}

// Usage
using var logger = new ParseableLogger(
    "http://parseable:8000",
    "dotnet-app",
    "admin",
    "admin"
);

logger.Info("Application started", new { Version = "1.0.0" });
logger.Error("Database error", new { Error = "Connection refused" });
```

## Serilog Integration

### Install Package

```bash
dotnet add package Serilog
dotnet add package Serilog.Sinks.Http
```

### Custom Sink

```csharp
using Serilog;
using Serilog.Core;
using Serilog.Events;
using System.Text;
using System.Text.Json;

public class ParseableSink : ILogEventSink, IDisposable
{
    private readonly HttpClient _client;
    private readonly string _stream;
    private readonly List<object> _buffer = new();
    private readonly object _lock = new();
    private readonly Timer _flushTimer;

    public ParseableSink(string url, string dataset, string username, string password)
    {
        _stream = dataset;
        _client = new HttpClient { BaseAddress = new Uri(url) };
        var auth = Convert.ToBase64String(Encoding.UTF8.GetBytes($"{username}:{password}"));
        _client.DefaultRequestHeaders.Authorization = 
            new System.Net.Http.Headers.AuthenticationHeaderValue("Basic", auth);
        
        _flushTimer = new Timer(_ => Flush(), null, 
            TimeSpan.FromSeconds(5), TimeSpan.FromSeconds(5));
    }

    public void Emit(LogEvent logEvent)
    {
        var entry = new
        {
            timestamp = logEvent.Timestamp.UtcDateTime.ToString("yyyy-MM-ddTHH:mm:ss.fffZ"),
            level = logEvent.Level.ToString().ToLower(),
            message = logEvent.RenderMessage(),
            exception = logEvent.Exception?.ToString(),
            properties = logEvent.Properties.ToDictionary(
                p => p.Key, 
                p => p.Value.ToString().Trim('"'))
        };

        lock (_lock)
        {
            _buffer.Add(entry);
            if (_buffer.Count >= 100)
            {
                FlushInternal();
            }
        }
    }

    public void Flush()
    {
        lock (_lock) { FlushInternal(); }
    }

    private void FlushInternal()
    {
        if (_buffer.Count == 0) return;

        var entries = _buffer.ToList();
        _buffer.Clear();

        Task.Run(async () =>
        {
            var json = JsonSerializer.Serialize(entries);
            var content = new StringContent(json, Encoding.UTF8, "application/json");
            content.Headers.Add("X-P-Stream", _stream);
            await _client.PostAsync("/api/v1/ingest", content);
        });
    }

    public void Dispose()
    {
        _flushTimer.Dispose();
        Flush();
        _client.Dispose();
    }
}

// Extension method
public static class ParseableSinkExtensions
{
    public static LoggerConfiguration Parseable(
        this LoggerSinkConfiguration config,
        string url,
        string dataset,
        string username,
        string password)
    {
        return config.Sink(new ParseableSink(url, dataset, username, password));
    }
}
```

### Usage

```csharp
Log.Logger = new LoggerConfiguration()
    .WriteTo.Parseable(
        url: "http://parseable:8000",
        dataset: "dotnet-app",
        username: "admin",
        password: "admin")
    .CreateLogger();

Log.Information("Application started");
Log.Error("Something went wrong", new { ErrorCode = 500 });
```

## ASP.NET Core Integration

### Configure in Program.cs

```csharp
var builder = WebApplication.CreateBuilder(args);

// Add Serilog with Parseable
builder.Host.UseSerilog((context, config) =>
{
    config
        .ReadFrom.Configuration(context.Configuration)
        .WriteTo.Parseable(
            url: context.Configuration["Parseable:Url"]!,
            dataset: context.Configuration["Parseable:Stream"]!,
            username: context.Configuration["Parseable:Username"]!,
            password: context.Configuration["Parseable:Password"]!);
});

var app = builder.Build();
app.UseSerilogRequestLogging();
app.Run();
```

### Configuration

```json
{
  "Parseable": {
    "Url": "http://parseable:8000",
    "Stream": "aspnet-app",
    "Username": "admin",
    "Password": "admin"
  }
}
```

## OpenTelemetry Integration

```csharp
using OpenTelemetry.Logs;

builder.Logging.AddOpenTelemetry(options =>
{
    options.AddOtlpExporter(otlp =>
    {
        otlp.Endpoint = new Uri("http://parseable:8000/v1/logs");
        otlp.Headers = "Authorization=Basic YWRtaW46YWRtaW4=,X-P-Stream=dotnet-otel";
    });
});
```

## Best Practices

1. **Use Batching** - Buffer logs and send in batches
2. **Async Sending** - Don't block application threads
3. **Handle Failures** - Log locally on send failures
4. **Add Context** - Include correlation ID, user ID
5. **Dispose Properly** - Flush on application shutdown

## Troubleshooting

### Connection Errors

1. Verify Parseable URL is accessible
2. Check SSL certificate if using HTTPS
3. Verify credentials

### Missing Logs

1. Ensure Flush is called on shutdown
2. Check for exceptions in background tasks
3. Verify dataset name

## Next Steps

* Configure [alerts](/docs/user-guide/alerting) for error patterns
* Create [dashboards](/docs/user-guide/dashboards) for .NET metrics
* Explore [OpenTelemetry](/docs/ingest-data/otel) for tracing


# Go (/docs/ingest-data/programming-languages/go)



### Create a dataset

First, we'll need to create a dataset. This is a one time operation, and we recommend storing log entries with same schema in a single dataset. So, for example, you can use one dataset per application (given that all logs from that application have the same schema).

```go
package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
	// highlight-start
	// TODO: Replace the url with your Parseable URL and dataset name
	url := "https://<parseable-url>/api/v1/logstream/<dataset-name>"
	// highlight-end
	method := "PUT"

	client := &http.Client{}
	req, err := http.NewRequest(method, url, nil)

	if err != nil {
		fmt.Println(err)
		return
	}

	// highlight-start
	// TODO: Replace the basic auth credentials with your Parseable credentials
	req.Header.Add("Authorization", "Basic YWRtaW46YWRtaW4=")
	// highlight-end

	res, err := client.Do(req)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer res.Body.Close()

	body, err := ioutil.ReadAll(res.Body)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(string(body))
}
```

### Send logs to the dataset

After dataset is created, you can start sending logs to the dataset using HTTP POST requests.

```go
package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"
)

func main() {

	// highlight-start
	// TODO: Replace the url with your Parseable URL and dataset name
	url := "https://<parseable-url>/api/v1/logstream/<dataset-name>"
	// highlight-end
	method := "POST"

	payload := strings.NewReader(`[{
        "id": "434a5f5e-2f5f-11ed-a261-asdasdafgdfd",
        "datetime": "24/Jun/2022:14:12:15 +0000",
        "host": "153.10.110.81", 
        "user-identifier": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0", 
        "method": "PUT", 
        "status": 500, 
        "referrer": "http://www.google.com/"
  }]`)

	client := &http.Client{}
	req, err := http.NewRequest(method, url, payload)

	if err != nil {
		fmt.Println(err)
		return
	}
	// highlight-start
	// INFO: Use X-P-META-<key>:<value> to add custom metadata to the log event
	req.Header.Add("X-P-META-Host", "192.168.1.3")
	// INFO: Use X-P-TAG-<key>:<value> to add tags to the log event
	req.Header.Add("X-P-TAG-Language", "golang")
	// TODO: Replace the basic auth credentials with your Parseable credentials
	req.Header.Add("Authorization", "Basic YWRtaW46YWRtaW4=")
	// highlight-end
	req.Header.Add("Content-Type", "application/json")

	res, err := client.Do(req)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer res.Body.Close()

	body, err := ioutil.ReadAll(res.Body)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(string(body))
}
```

### Querying a dataset

Once you have started sending logs to a dataset, you can query the logs using standard SQL.

```go
package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"
)

func main() {
	// highlight-start
	// TODO: Replace the url with your Parseable URL
	url := "https://<parseable-url>/api/v1/query"
	// highlight-end
	method := "POST"

	payload := strings.NewReader(`{
    // highlight-start
    // TODO: Replace the dataset name with your dataset name
    "query": "select * from <dataset-name>",
    // TODO: Replace the time range with your desired time range
    "startTime": "2022-09-10T08:20:00+00:00",
    "endTime": "2022-09-10T08:20:31+00:00"
    // highlight-end
}
`)

	client := &http.Client{}
	req, err := http.NewRequest(method, url, payload)

	if err != nil {
		fmt.Println(err)
		return
	}

	// highlight-start
	// TODO: Replace the basic auth credentials with your Parseable credentials
	req.Header.Add("Authorization", "Basic YWRtaW46YWRtaW4=")
	// highlight-end
	req.Header.Add("Content-Type", "application/json")

	res, err := client.Do(req)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer res.Body.Close()

	body, err := ioutil.ReadAll(res.Body)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(string(body))
}
```


# Programming Languages (/docs/ingest-data/programming-languages)



Parseable supports direct log ingestion from various programming languages using HTTP clients or dedicated SDKs:

* [Go](/docs/ingest-data/programming-languages/go) - Native Go HTTP client integration
* [Python](/docs/ingest-data/programming-languages/python) - Python logging with HTTP transport
* [Java](/docs/ingest-data/programming-languages/java) - Java logging frameworks integration
* [JavaScript](/docs/ingest-data/programming-languages/javascript) - Node.js and browser logging
* [Rust](/docs/ingest-data/programming-languages/rust) - Rust HTTP client integration
* [C#](/docs/ingest-data/programming-languages/csharp) - .NET logging integration
* [.NET](/docs/ingest-data/programming-languages/dotnet) - .NET Core and Framework support
* [PHP](/docs/ingest-data/programming-languages/php) - PHP logging integration
* [Ruby](/docs/ingest-data/programming-languages/ruby) - Ruby logging integration


# Java (/docs/ingest-data/programming-languages/java)



### Create a dataset

First, we'll need to create a dataset. This is a one time operation, and we recommend storing log entries with same schema in a single dataset. So, for example, you can use one dataset per application (given that all logs from that application have the same schema).

```java
OkHttpClient client = new OkHttpClient().newBuilder().build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
    // highlight-start 
    // TODO: Replace the url with your Parseable URL and dataset name
    .url("https://<parseable-url>/api/v1/logstream/<dataset-name>")
    // highlight-end
    .method("PUT", body)
    // highlight-start 
    // TODO: Replace the basic auth credentials with your Parseable credentials
    .addHeader("Authorization", "Basic YWRtaW46YWRtaW4=")
    // highlight-end
    .build();

Response response = client.newCall(request).execute();
```

### Send logs to the dataset

After dataset is created, you can start sending logs to the dataset using HTTP POST requests.

```java
OkHttpClient client = new OkHttpClient().newBuilder()
    .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "[\n    {\n        \"id\": \"434a5f5e-2f5f-11ed-a261-asdasdafgdfd\",\n        \"datetime\": \"24/Jun/2022:14:12:15 +0000\",\n        \"host\": \"153.10.110.81\", \n        \"user-identifier\": \"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0\", \n        \"method\": \"PUT\", \n        \"status\": 500, \n        \"referrer\": \"http://www.google.com/\"\n    }\n]");
Request request = new Request.Builder()
    // highlight-start
    // TODO: Replace the url with your Parseable URL and dataset name
    .url("https://<parseable-url>/api/v1/logstream/<dataset-name>")
    // highlight-end
    .method("POST", body)
    // highlight-start
    // INFO: Use X-P-META-<key>:<value> to add custom metadata to the log event
    .addHeader("X-P-META-Host", "192.168.1.3")
    // INFO: Use X-P-TAG-<key>:<value> to add tags to the log event
    .addHeader("X-P-TAG-Language", "java")
    // TODO: Replace the basic auth credentials with your Parseable credentials
    .addHeader("Authorization", "Basic YWRtaW46YWRtaW4=")
    // highlight-end
    .addHeader("Content-Type", "application/json")
    .build();
Response response = client.newCall(request).execute();
```

### Querying a dataset

Once you have started sending logs to a dataset, you can query the logs using standard SQL.

```java
OkHttpClient client = new OkHttpClient().newBuilder()
    .build();
MediaType mediaType = MediaType.parse("application/json");
// highlight-start
// TODO: Replace the dataset name with your dataset name
RequestBody body = RequestBody.create(mediaType, "{\n    \"query\": \"select * from <dataset-name>\",\n    \"startTime\": \"2022-09-10T08:20:00+00:00\",\n    \"endTime\": \"2022-09-10T08:20:31+00:00\"\n}\n");
// highlight-end
Request request = new Request.Builder()
    // highlight-start
    // TODO: Replace the url with your Parseable URL
    .url("https://<parseable-url>/api/v1/query")
    // highlight-end
    .method("POST", body)
    // highlight-start
    // TODO: Replace the basic auth credentials with your Parseable credentials
    .addHeader("Authorization", "Basic YWRtaW46YWRtaW4=")
    // highlight-end
    .addHeader("Content-Type", "application/json")
    .build();
Response response = client.newCall(request).execute();
```


# JavaScript (/docs/ingest-data/programming-languages/javascript)



## Parseable Bunyan Plugin

The Parseable Bunyan plugin is developed by our community champion Jacques-Yves Bleau. Refer to the plugin here:

NPM page: [https://www.npmjs.com/package/parseable-bunyan](https://www.npmjs.com/package/parseable-bunyan)
Repo page: [https://github.com/jybleau/parseable-node-loggers/tree/main/packages/bunyan#parseable-bunyan](https://github.com/jybleau/parseable-node-loggers/tree/main/packages/bunyan#parseable-bunyan)
Installation

```bash
npm install parseable-bunyan
yarn add parseable-bunyan
```

### Using the Plugin

```javascript
const { ParseableBunyan } = require('parseable-bunyan')
const bunyan = require('bunyan')

const parseableStream = new ParseableBunyan({
    // highlight-start 
    url: process.env.PARSEABLE_URL, // Ex: 'https://parsable.myserver.local/api/v1/logstream'
    username: process.env.PARSEABLE_USERNAME,
    password: process.env.PARSEABLE_PASSWORD,
    logstream: process.env.PARSEABLE_LOGSTREAM, // The logstream name
    // highlight-end
    tags: { tag1: 'tagValue' } // optional tags to be added with each ingestion
    disableTLSCerts: true, // Optional: Default to false. Set to true to ignore invalid certificate
    http2: true, // Optional: Default to true. Set to false to use HTTP/1.1 instead of HTTP/2.0
    buffer: { maxEntries: 100, flushInterval: 5000 }, // Optional: Tune the default buffering options
    onError: error => console.error(error), // Optional: handle an error by yourself
    onRecord: record => { // optional onRecord event
        // Examples of what could be done here: exclude routes, methods, IPs and UAs
        const excludeMethods = 'HEAD,OPTIONS'
        const excludeRoutes = '/check,/test1'
        const excludeIPs = '192.168.1.1,192.168.1.2'
        const excludeUAs = 'UptimeRobot,AnnoyingUA'

        if (record.req) {
        if (excludeRoutes.includes(record.req.path)) {
            return false
        }
        if (excludeMethods.includes(record.req.method)) {
            return false
        }
        if (record.remoteAddress) {
            if (excludeIPs.some(ip => record.remoteAddress.includes(ip))) {
            return false
            }
        }            
        if (record.req.headers['user-agent']) {
            const _ua = record.req.headers['user-agent'].toLowerCase()
            if (excludeUAs.some(ua => _ua.includes(ua.toLowerCase()))) {
            return false
            }
        }
        }
    // You can also apply custom serialization here and return the serialized record.
  }
})

const bunyanLogger = bunyan.createLogger({
    name: 'logger',
    serializers, // optionally set your own serializers
    streams: [parseableStream]
  })
```

## Parseable Winston Plugin

This is a community plugin, refer to the plugin here:

NPM page: [https://www.npmjs.com/package/parseable-winston](https://www.npmjs.com/package/parseable-winston)
Repo page: [https://github.com/jybleau/parseable-node-loggers/tree/main/packages/winston#parseable-winston](https://github.com/jybleau/parseable-node-loggers/tree/main/packages/winston#parseable-winston)

### Installation

```bash
npm install parseable-winston
yarn add parseable-winston
```

### Using the Plugin

```javascript
// Using cjs
const { ParseableTransport } = require('parseable-winston')
const winston = require('winston')
// highlight-start 
const parseable = new ParseableTransport({
  url: process.env.PARSEABLE_LOGS_URL, // Ex: 'https://parsable.myserver.local/api/v1/logstream'
  username: process.env.PARSEABLE_LOGS_USERNAME,
  password: process.env.PARSEABLE_LOGS_PASSWORD,
  logstream: process.env.PARSEABLE_LOGS_LOGSTREAM, // The logstream name
  tags: { tag1: 'tagValue' } // optional tags to be added with each ingestion
})
// highlight-end

const logger = winston.createLogger({
  levels: winston.config.syslog.levels,
  transports: [parseable],
  defaultMeta: { instance: 'app', hostname: 'app1' }
})

logger.info('User took the goggles', { userid: 1, user: { name: 'Rainier Wolfcastle' } })
logger.warning('The goggles do nothing', { userid: 1 })
```

### To turn off default buffering option:

```javascript
const parseable = new ParseableTransport({
  url: process.env.PARSEABLE_LOGS_URL,
  username: process.env.PARSEABLE_LOGS_USERNAME,
  password: process.env.PARSEABLE_LOGS_PASSWORD,
  logstream: process.env.PARSEABLE_LOGS_LOGSTREAM,
  buffer: { maxEntries: 100, flushInterval: 5000 }
})
```

## Using plain JavaScript

### Create a dataset

First, we'll need to create a dataset. This is a one time operation, and we recommend storing log entries with same schema in a single dataset. So, for example, you can use one dataset per application (given that all logs from that application have the same schema).

```javascript
var myHeaders = new Headers();
// highlight-start 
// TODO: Replace the basic auth credentials with your Parseable credentials
myHeaders.append("Authorization", "Basic YWRtaW46YWRtaW4=");
// highlight-end

var requestOptions = {
    method: 'PUT',
    headers: myHeaders,
    redirect: 'follow'
};
// highlight-start 
// TODO: Replace the url with your Parseable URL and dataset name
fetch("https://<parseable-url>/api/v1/logstream/<dataset-name>", requestOptions)
    // highlight-end
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));
```

### Send logs to the dataset

After dataset is created, you can start sending logs to the dataset using HTTP POST requests.

```javascript
var myHeaders = new Headers();
// highlight-start
// INFO: Use X-P-META-<key>:<value> to add custom metadata to the log event
myHeaders.append("X-P-META-Host", "192.168.1.3");
// INFO: Use X-P-TAG-<key>:<value> to add tags to the log event
myHeaders.append("X-P-TAG-Language", "javascript");
// TODO: Replace the basic auth credentials with your Parseable credentials
myHeaders.append("Authorization", "Basic YWRtaW46YWRtaW4=");
// highlight-end
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify([{
    "id": "434a5f5e-2f5f-11ed-a261-asdasdafgdfd",
    "datetime": "24/Jun/2022:14:12:15 +0000",
    "host": "153.10.110.81",
    "user-identifier": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0",
    "method": "PUT",
    "status": 500,
    "referrer": "http://www.google.com/"
}]);

var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
};

// highlight-start
// TODO: Replace the url with your Parseable URL and dataset name
fetch("https://<parseable-url>/api/v1/logstream/<dataset-name>", requestOptions)
    // highlight-end
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));
```

### Querying a dataset

Once you have started sending logs to a dataset, you can query the logs using standard SQL.

```javascript
var myHeaders = new Headers();
// highlight-start
// TODO: Replace the basic auth credentials with your Parseable credentials
myHeaders.append("Authorization", "Basic YWRtaW46YWRtaW4=");
// highlight-end
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
    // highlight-start
    // TODO: Replace the dataset name with your dataset name
    "query": "select * from <dataset-name>",
    // TODO: Replace the time range with your desired time range
    "startTime": "2022-09-10T08:20:00+00:00",
    "endTime": "2022-09-10T08:20:31+00:00"
    // highlight-end
});

var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
};

// highlight-start
// TODO: Replace the url with your Parseable URL
fetch("https://<parseable-url>/api/v1/query", requestOptions)
    // highlight-end
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));
```


# PHP (/docs/ingest-data/programming-languages/php)



Send logs from PHP applications to Parseable using HTTP or logging libraries.

## Overview

Integrate PHP with Parseable to:

* **Application Logs** - Send structured logs from PHP apps
* **Laravel/Symfony** - Works with popular frameworks
* **Monolog Integration** - Use with Monolog handler
* **Structured Logging** - JSON-formatted log entries

## Prerequisites

* PHP 7.4+
* Parseable instance accessible
* cURL extension or Guzzle HTTP client

## Basic HTTP Integration

### Using cURL

```php
<?php

class ParseableLogger
{
    private string $url;
    private string $dataset;
    private string $auth;

    public function __construct(string $url, string $dataset, string $username, string $password)
    {
        $this->url = rtrim($url, '/') . '/api/v1/ingest';
        $this->dataset = $dataset;
        $this->auth = base64_encode("$username:$password");
    }

    public function log(string $level, string $message, array $context = []): void
    {
        $entry = [
            'timestamp' => gmdate('Y-m-d\TH:i:s.v\Z'),
            'level' => $level,
            'message' => $message,
            ...$context
        ];

        $this->send([$entry]);
    }

    public function info(string $message, array $context = []): void
    {
        $this->log('info', $message, $context);
    }

    public function error(string $message, array $context = []): void
    {
        $this->log('error', $message, $context);
    }

    public function warning(string $message, array $context = []): void
    {
        $this->log('warning', $message, $context);
    }

    private function send(array $entries): void
    {
        $ch = curl_init($this->url);
        
        curl_setopt_array($ch, [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => json_encode($entries),
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => [
                'Content-Type: application/json',
                "Authorization: Basic {$this->auth}",
                "X-P-Stream: {$this->dataset}"
            ],
            CURLOPT_TIMEOUT => 5
        ]);

        $response = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);

        if ($httpCode >= 400) {
            error_log("Failed to send log to Parseable: HTTP $httpCode");
        }
    }
}

// Usage
$logger = new ParseableLogger(
    'http://parseable:8000',
    'php-app',
    'admin',
    'admin'
);

$logger->info('Application started', ['version' => '1.0.0']);
$logger->error('Database error', ['error' => 'Connection refused']);
```

### Using Guzzle

```php
<?php

use GuzzleHttp\Client;

class ParseableLogger
{
    private Client $client;
    private string $dataset;

    public function __construct(string $url, string $dataset, string $username, string $password)
    {
        $this->dataset = $dataset;
        $this->client = new Client([
            'base_uri' => $url,
            'auth' => [$username, $password],
            'timeout' => 5.0,
        ]);
    }

    public function log(string $level, string $message, array $context = []): void
    {
        $entry = [
            'timestamp' => gmdate('Y-m-d\TH:i:s.v\Z'),
            'level' => $level,
            'message' => $message,
            ...$context
        ];

        try {
            $this->client->post('/api/v1/ingest', [
                'json' => [$entry],
                'headers' => [
                    'X-P-Stream' => $this->dataset
                ]
            ]);
        } catch (\Exception $e) {
            error_log("Failed to send log: " . $e->getMessage());
        }
    }
}
```

## Monolog Handler

Create a custom Monolog handler:

```php
<?php

namespace App\Logging;

use Monolog\Handler\AbstractProcessingHandler;
use Monolog\LogRecord;

class ParseableHandler extends AbstractProcessingHandler
{
    private string $url;
    private string $dataset;
    private string $auth;
    private array $buffer = [];
    private int $batchSize;

    public function __construct(
        string $url,
        string $dataset,
        string $username,
        string $password,
        int $batchSize = 100,
        $level = Logger::DEBUG,
        bool $bubble = true
    ) {
        parent::__construct($level, $bubble);
        $this->url = rtrim($url, '/') . '/api/v1/ingest';
        $this->dataset = $dataset;
        $this->auth = base64_encode("$username:$password");
        $this->batchSize = $batchSize;
    }

    protected function write(LogRecord $record): void
    {
        $this->buffer[] = [
            'timestamp' => $record->datetime->format('Y-m-d\TH:i:s.v\Z'),
            'level' => strtolower($record->level->name),
            'message' => $record->message,
            'channel' => $record->channel,
            'context' => $record->context,
            'extra' => $record->extra
        ];

        if (count($this->buffer) >= $this->batchSize) {
            $this->flush();
        }
    }

    public function flush(): void
    {
        if (empty($this->buffer)) {
            return;
        }

        $entries = $this->buffer;
        $this->buffer = [];

        $ch = curl_init($this->url);
        curl_setopt_array($ch, [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => json_encode($entries),
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => [
                'Content-Type: application/json',
                "Authorization: Basic {$this->auth}",
                "X-P-Stream: {$this->dataset}"
            ]
        ]);
        curl_exec($ch);
        curl_close($ch);
    }

    public function close(): void
    {
        $this->flush();
        parent::close();
    }
}
```

## Laravel Integration

### Custom Log Channel

In `config/logging.php`:

```php
'channels' => [
    'parseable' => [
        'driver' => 'custom',
        'via' => App\Logging\CreateParseableLogger::class,
        'url' => env('PARSEABLE_URL'),
        'dataset' => env('PARSEABLE_STREAM', 'laravel-app'),
        'username' => env('PARSEABLE_USERNAME'),
        'password' => env('PARSEABLE_PASSWORD'),
    ],
],
```

Create `app/Logging/CreateParseableLogger.php`:

```php
<?php

namespace App\Logging;

use Monolog\Logger;

class CreateParseableLogger
{
    public function __invoke(array $config): Logger
    {
        $logger = new Logger('parseable');
        
        $logger->pushHandler(new ParseableHandler(
            $config['url'],
            $config['dataset'],
            $config['username'],
            $config['password']
        ));

        return $logger;
    }
}
```

### Usage

```php
Log::channel('parseable')->info('User logged in', ['user_id' => 123]);
```

## Symfony Integration

### Service Configuration

```yaml
# config/services.yaml
services:
    App\Logging\ParseableHandler:
        arguments:
            $url: '%env(PARSEABLE_URL)%'
            $dataset: '%env(PARSEABLE_STREAM)%'
            $username: '%env(PARSEABLE_USERNAME)%'
            $password: '%env(PARSEABLE_PASSWORD)%'
```

### Monolog Configuration

```yaml
# config/packages/monolog.yaml
monolog:
    handlers:
        parseable:
            type: service
            id: App\Logging\ParseableHandler
```

## Best Practices

1. **Use Batching** - Buffer logs and send in batches
2. **Async Sending** - Use queues for non-blocking sends
3. **Handle Failures** - Log locally on send failures
4. **Add Context** - Include request ID, user ID
5. **Flush on Shutdown** - Register shutdown handler

## Troubleshooting

### Connection Errors

1. Verify cURL extension is installed
2. Check Parseable URL is accessible
3. Verify SSL certificates

### Missing Logs

1. Check buffer is being flushed
2. Verify dataset name
3. Check for cURL errors

## Next Steps

* Configure [alerts](/docs/user-guide/alerting) for error patterns
* Create [dashboards](/docs/user-guide/dashboards) for PHP metrics
* Explore [OpenTelemetry](/docs/ingest-data/otel) for tracing


# Python (/docs/ingest-data/programming-languages/python)



## Create a dataset

First, we'll need to create a dataset. This is a one time operation, and we recommend storing log entries with same schema in a single dataset. So, for example, you can use one dataset per application (given that all logs from that application have the same schema).

```python
import requests

# highlight-start
# TODO: Replace the url with your Parseable URL and dataset name
url = "https://<parseable-url>/api/v1/logstream/<dataset-name>"
# highlight-end
payload = {}

headers = {
    # highlight-start
    # TODO: Replace the basic auth credentials with your Parseable credentials
    "Authorization": "Basic YWRtaW46YWRtaW4="
    # highlight-end
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
```

## Send logs to the dataset

After dataset is created, you can start sending logs to the dataset using HTTP POST requests.

```python
import requests
import json

# highlight-start
# TODO: Replace the url with your Parseable URL and dataset name
url = "https://<parseable-url>/api/v1/logstream/<dataset-name>"
# highlight-end

payload = json.dumps(
    [
        {
            "id": "434a5f5e-2f5f-11ed-a261-asdasdafgdfd",
            "datetime": "24/Jun/2022:14:12:15  0000",
            "host": "153.10.110.81",
            "user-identifier": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0",
            "method": "PUT",
            "status": 500,
            "referrer": "http://www.google.com/",
        }
    ]
)

headers = {
    # highlight-start
    # INFO: Use X-P-META-<key>:<value> to add custom metadata to the log event
    "X-P-META-Host": "192.168.1.3",
    # INFO: Use X-P-TAG-<key>:<value> to add tags to the log event
    "X-P-TAG-Language": "python",
    # TODO: Replace the basic auth credentials with your Parseable credentials
    "Authorization": "Basic YWRtaW46YWRtaW4=",
    # highlight-end
    "Content-Type": "application/json",
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
```

### Querying a dataset

Once you have started sending logs to a dataset, you can query the logs using standard SQL.

```python
import requests
import json

# highlight-start
# TODO: Replace the url with your Parseable URL
url = "https://<parseable-url>/api/v1/query"
# highlight-end

payload = json.dumps(
    {
        # highlight-start
        # TODO: Replace the dataset name with your dataset name
        "query": "select * from <dataset-name>",
        # TODO: Replace the time range with your desired time range
        "startTime": "2022-09-10T08:20:00+00:00",
        "endTime": "2022-09-10T08:20:31+00:00"
        # highlight-end
    }
)
headers = {
    # highlight-start
    # TODO: Replace the basic auth credentials with your Parseable credentials
    "Authorization": "Basic YWRtaW46YWRtaW4=",
    # highlight-end
    "Content-Type": "application/json",
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```


# Ruby (/docs/ingest-data/programming-languages/ruby)



Send logs from Ruby applications to Parseable using HTTP or logging libraries.

## Overview

Integrate Ruby with Parseable to:

* **Application Logs** - Send structured logs from Ruby apps
* **Rails Integration** - Works with Ruby on Rails
* **Multiple Frameworks** - Sinatra, Hanami, and more
* **Structured Logging** - JSON-formatted log entries

## Prerequisites

* Ruby 2.7+
* Parseable instance accessible
* HTTP client gem (net/http, faraday, or httparty)

## Basic HTTP Integration

### Using Net::HTTP

```ruby
require 'net/http'
require 'json'
require 'uri'

class ParseableLogger
  def initialize(url:, dataset:, username:, password:)
    @uri = URI.parse("#{url}/api/v1/ingest")
    @dataset = dataset
    @auth = Base64.strict_encode64("#{username}:#{password}")
  end

  def log(level:, message:, **metadata)
    entry = {
      timestamp: Time.now.utc.iso8601(3),
      level: level.to_s,
      message: message,
      **metadata
    }

    send_log([entry])
  end

  def info(message, **metadata)
    log(level: :info, message: message, **metadata)
  end

  def error(message, **metadata)
    log(level: :error, message: message, **metadata)
  end

  def warn(message, **metadata)
    log(level: :warn, message: message, **metadata)
  end

  private

  def send_log(entries)
    http = Net::HTTP.new(@uri.host, @uri.port)
    http.use_ssl = @uri.scheme == 'https'

    request = Net::HTTP::Post.new(@uri.path)
    request['Content-Type'] = 'application/json'
    request['Authorization'] = "Basic #{@auth}"
    request['X-P-Stream'] = @dataset
    request.body = entries.to_json

    response = http.request(request)
    raise "Failed to send log: #{response.code}" unless response.is_a?(Net::HTTPSuccess)
  end
end

# Usage
logger = ParseableLogger.new(
  url: 'http://parseable:8000',
  dataset: 'ruby-app',
  username: 'admin',
  password: 'admin'
)

logger.info('Application started', service: 'my-app', version: '1.0.0')
logger.error('Database connection failed', error: 'Connection refused')
```

### Using Faraday

```ruby
require 'faraday'
require 'json'

class ParseableLogger
  def initialize(url:, dataset:, username:, password:)
    @dataset = dataset
    @conn = Faraday.new(url: url) do |f|
      f.request :json
      f.request :authorization, :basic, username, password
      f.adapter Faraday.default_adapter
    end
  end

  def log(level:, message:, **metadata)
    entry = {
      timestamp: Time.now.utc.iso8601(3),
      level: level.to_s,
      message: message,
      **metadata
    }

    @conn.post('/api/v1/ingest') do |req|
      req.headers['X-P-Stream'] = @dataset
      req.body = [entry].to_json
    end
  end
end
```

## Rails Integration

### Custom Logger

Create `lib/parseable_logger.rb`:

```ruby
require 'net/http'
require 'json'

class ParseableLogger < Logger
  def initialize(url:, dataset:, username:, password:)
    super(nil)
    @uri = URI.parse("#{url}/api/v1/ingest")
    @dataset = dataset
    @auth = Base64.strict_encode64("#{username}:#{password}")
    @buffer = []
    @mutex = Mutex.new
    @batch_size = 100
    @flush_interval = 5

    start_flush_thread
  end

  def add(severity, message = nil, progname = nil)
    message = yield if block_given?
    
    entry = {
      timestamp: Time.now.utc.iso8601(3),
      level: severity_name(severity),
      message: message.to_s,
      progname: progname
    }

    @mutex.synchronize do
      @buffer << entry
      flush_buffer if @buffer.size >= @batch_size
    end
  end

  private

  def severity_name(severity)
    %w[DEBUG INFO WARN ERROR FATAL UNKNOWN][severity] || 'UNKNOWN'
  end

  def start_flush_thread
    Thread.new do
      loop do
        sleep @flush_interval
        @mutex.synchronize { flush_buffer }
      end
    end
  end

  def flush_buffer
    return if @buffer.empty?

    entries = @buffer.dup
    @buffer.clear

    Thread.new { send_logs(entries) }
  end

  def send_logs(entries)
    http = Net::HTTP.new(@uri.host, @uri.port)
    http.use_ssl = @uri.scheme == 'https'

    request = Net::HTTP::Post.new(@uri.path)
    request['Content-Type'] = 'application/json'
    request['Authorization'] = "Basic #{@auth}"
    request['X-P-Stream'] = @dataset
    request.body = entries.to_json

    http.request(request)
  rescue => e
    STDERR.puts "Failed to send logs to Parseable: #{e.message}"
  end
end
```

### Configure in Rails

In `config/environments/production.rb`:

```ruby
config.logger = ParseableLogger.new(
  url: ENV['PARSEABLE_URL'],
  dataset: 'rails-app',
  username: ENV['PARSEABLE_USERNAME'],
  password: ENV['PARSEABLE_PASSWORD']
)
```

## Semantic Logger Integration

Use Semantic Logger for structured logging:

```ruby
# Gemfile
gem 'semantic_logger'

# config/initializers/semantic_logger.rb
require 'semantic_logger'

class ParseableAppender < SemanticLogger::Subscriber
  def initialize(url:, dataset:, username:, password:)
    super()
    @uri = URI.parse("#{url}/api/v1/ingest")
    @dataset = dataset
    @auth = Base64.strict_encode64("#{username}:#{password}")
  end

  def log(log)
    entry = {
      timestamp: log.time.utc.iso8601(3),
      level: log.level.to_s,
      message: log.message,
      name: log.name,
      duration: log.duration,
      payload: log.payload,
      exception: log.exception&.message,
      backtrace: log.exception&.backtrace&.first(10)
    }.compact

    send_log([entry])
  end

  private

  def send_log(entries)
    # Same as above
  end
end

SemanticLogger.add_appender(appender: ParseableAppender.new(
  url: ENV['PARSEABLE_URL'],
  dataset: 'rails-app',
  username: ENV['PARSEABLE_USERNAME'],
  password: ENV['PARSEABLE_PASSWORD']
))
```

## Best Practices

1. **Use Batching** - Buffer logs and send in batches
2. **Async Sending** - Don't block application threads
3. **Handle Failures** - Implement retry logic
4. **Add Context** - Include request ID, user ID
5. **Use Structured Logs** - Send JSON-formatted entries

## Troubleshooting

### Connection Errors

1. Verify Parseable URL is accessible
2. Check SSL certificate if using HTTPS
3. Verify credentials

### Missing Logs

1. Check buffer is being flushed
2. Verify dataset name is correct
3. Check for exceptions in send thread

## Next Steps

* Configure [alerts](/docs/user-guide/alerting) for error patterns
* Create [dashboards](/docs/user-guide/dashboards) for Ruby metrics
* Explore [OpenTelemetry](/docs/ingest-data/otel) for tracing


# Rust (/docs/ingest-data/programming-languages/rust)



## Create a dataset

First, we'll need to create a dataset. This is a one time operation, and we recommend storing log entries with same schema in a single dataset. So, for example, you can use one dataset per application (given that all logs from that application have the same schema).

```rust
use reqwest::{Client};

#[tokio::main]
async fn main() {
    // TODO: Replace the url with your Parseable URL and dataset name    
    let url = "https://<parseable-url>/api/v1/logstream/<dataset-name>";

    let client = Client::new();
    client
        .put(url)
        // TODO: Replace the basic auth credentials with your Parseable credentials
        .header("Authorization", "Basic YWRtaW46YWRtaW4=")
        .send()
        .await
        .unwrap();
}
```

## Send logs to the dataset

After dataset is created, you can start sending logs to the dataset using HTTP POST requests.

```rust
use std::collections::HashMap;
use reqwest::{Client};

#[tokio::main]
async fn main() {
    // TODO: Replace the url with your Parseable URL and dataset name    
    let url = "https://<parseable-url>/api/v1/logstream/<dataset-name>";

    let mut map = HashMap::new();
    map.insert("id", "434a5f5e-2f5f-11ed-a261-0242ac120002");
    map.insert("datetime", "24/Jun/2022:14:12:15 +0000");
    map.insert("host", "153.10.110.81",);
    map.insert("user-identifier", "Mozilla/5.0 Gecko/20100101 Firefox/64.0",);
    map.insert("method", "PUT",);
    map.insert("status", "500");
    map.insert("referrer", "http://www.google.com/");

    let client = Client::new();
    client
        .post(url)
        // INFO: Use X-P-META-<key>:<value> to add custom metadata to the log event
        .header("X-P-META-meta1", "value1")
        // INFO: Use X-P-TAG-<key>:<value> to add tags to the log event
        .header("X-P-TAG-tag1", "value1")
        // TODO: Replace the basic auth credentials with your Parseable credentials
        .header("Authorization", "Basic YWRtaW46YWRtaW4=")
        .header("Content-Type", "application/json")
        .json(&map)
        .send()
        .await
        .unwrap();
}
```

## Querying a dataset

Once you have started sending logs to a dataset, you can query the logs using standard SQL.

```rust
use reqwest::{Client};
use std::collections::HashMap;

#[tokio::main]
async fn main() {
    // TODO: Replace the url with your Parseable URL
    let url = "https://<parseable-url>/api/v1/query";

    let mut map = HashMap::new();
    // TODO: Replace the dataset name with your dataset name
    map.insert("query", "select * from <dataset-name>");
    // TODO: Replace the time range with your desired time range
    map.insert("startTime", "2022-11-20T08:20:00+00:00");
    map.insert("endTime", "2022-11-20T22:20:31+00:00");

    let client = Client::new();
    let res = client
        .post(url)
        // TODO: Replace the basic auth credentials with your Parseable credentials
        .header("Authorization", "Basic YWRtaW46YWRtaW4=")
        .header("Content-Type", "application/json")
        .json(&map)
        .send()
        .await
        .unwrap();

    if res.status() != 200 {
        panic!("Error: {}", res.status());
    }
    println!("{}", res.text().await.unwrap());
}
```


# Falco (/docs/ingest-data/security/falco)



Collect and analyze Falco security events in Parseable for comprehensive runtime security monitoring.

## Overview

Integrate Falco with Parseable to:

* **Runtime Security** - Detect suspicious behavior in containers and hosts
* **Threat Detection** - Identify security threats in real-time
* **Compliance Monitoring** - Track security policy violations
* **Incident Response** - Investigate security incidents with full context

## Prerequisites

* Kubernetes cluster or Linux host
* Falco installed and running
* Parseable instance accessible from Falco
* Falco Sidekick (recommended) or direct HTTP output

## What is Falco?

Falco is a cloud-native runtime security tool that detects unexpected application behavior and alerts on threats at runtime. It uses system calls to monitor:

* Container activity
* File system access
* Network connections
* Process execution
* Privilege escalation

## Method 1: Falco Sidekick

Falco Sidekick is the recommended way to forward Falco events to multiple destinations.

### Install Falco with Sidekick

Using Helm:

```bash
helm repo add falcosecurity https://falcosecurity.github.io/charts
helm repo update

helm install falco falcosecurity/falco \
  --namespace falco \
  --create-namespace \
  --set falcosidekick.enabled=true \
  --set falcosidekick.config.webhook.address="http://parseable:8000/api/v1/ingest" \
  --set falcosidekick.config.webhook.customHeaders="Authorization:Basic <YOUR_BASE64_AUTH>,X-P-Stream:falco-events"

# Note: Replace <YOUR_BASE64_AUTH> with your base64-encoded credentials
# Generate with: echo -n 'username:password' | base64
```

### Sidekick Configuration

Create a custom values file for more control:

```yaml
# falco-values.yaml
falcosidekick:
  enabled: true
  config:
    webhook:
      address: "http://parseable:8000/api/v1/ingest"
      customHeaders:
        Authorization: "Basic YWRtaW46YWRtaW4="
        X-P-Stream: "falco-events"
      minimumpriority: "warning"
```

Install with custom values:

```bash
helm install falco falcosecurity/falco \
  --namespace falco \
  --create-namespace \
  -f falco-values.yaml
```

## Method 2: Direct HTTP Output

Configure Falco to send events directly to Parseable.

### Falco Configuration

Edit `/etc/falco/falco.yaml`:

```yaml
json_output: true
json_include_output_property: true
json_include_tags_property: true

http_output:
  enabled: true
  url: "http://parseable:8000/api/v1/ingest"
  user_agent: "falco/0.35.0"
  insecure: true
  ca_cert: ""
  ca_bundle: ""
  client_cert: ""
  client_key: ""
  echo: false
  headers:
    Authorization: "Basic YWRtaW46YWRtaW4="
    X-P-Stream: "falco-events"
    Content-Type: "application/json"
```

### Kubernetes ConfigMap

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: falco-config
  namespace: falco
data:
  falco.yaml: |
    json_output: true
    json_include_output_property: true
    
    http_output:
      enabled: true
      url: "http://parseable.parseable.svc.cluster.local:8000/api/v1/ingest"
      headers:
        Authorization: "Basic YWRtaW46YWRtaW4="
        X-P-Stream: "falco-events"
```

## Method 3: Fluent Bit Collection

Collect Falco logs using Fluent Bit.

### Fluent Bit Configuration

```yaml
service:
  flush: 5
  log_level: info

pipeline:
  inputs:
    - name: tail
      path: /var/log/falco/events.json
      tag: falco
      parser: json
      refresh_interval: 5

  outputs:
    - name: http
      match: falco
      host: parseable
      port: 8000
      uri: /api/v1/ingest
      format: json
      header: Authorization Basic YWRtaW46YWRtaW4=
      header: X-P-Stream falco-events
```

### Docker Compose

```yaml
version: '3.8'
services:
  falco:
    image: falcosecurity/falco:latest
    privileged: true
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - /dev:/host/dev
      - /proc:/host/proc:ro
      - /boot:/host/boot:ro
      - /lib/modules:/host/lib/modules:ro
      - /usr:/host/usr:ro
      - /etc:/host/etc:ro
      - falco_logs:/var/log/falco
    command: ["/usr/bin/falco", "-o", "json_output=true", "-o", "file_output.enabled=true", "-o", "file_output.filename=/var/log/falco/events.json"]
  
  fluent-bit:
    image: fluent/fluent-bit:latest
    volumes:
      - falco_logs:/var/log/falco:ro
      - ./fluent-bit.yaml:/fluent-bit/etc/fluent-bit.yaml
    depends_on:
      - falco
      - parseable

volumes:
  falco_logs:
```

## Falco Event Format

Falco events sent to Parseable include:

```json
{
  "uuid": "12345678-1234-1234-1234-123456789012",
  "output": "19:23:45.123456789: Warning Shell spawned in container (user=root container_id=abc123)",
  "priority": "Warning",
  "rule": "Terminal shell in container",
  "time": "2024-01-15T19:23:45.123456789Z",
  "output_fields": {
    "container.id": "abc123",
    "container.name": "my-app",
    "user.name": "root",
    "proc.name": "bash",
    "proc.cmdline": "bash"
  },
  "source": "syscall",
  "tags": ["container", "shell", "mitre_execution"]
}
```

## Custom Falco Rules

Create custom rules for your environment:

```yaml
# custom-rules.yaml
- rule: Detect Cryptocurrency Mining
  desc: Detect cryptocurrency mining processes
  condition: >
    spawned_process and 
    (proc.name in (xmrig, minerd, cpuminer) or
     proc.cmdline contains "stratum+tcp")
  output: >
    Cryptocurrency miner detected 
    (user=%user.name command=%proc.cmdline container=%container.name)
  priority: CRITICAL
  tags: [cryptomining, mitre_resource_hijacking]

- rule: Sensitive File Access
  desc: Detect access to sensitive files
  condition: >
    open_read and 
    fd.name in (/etc/shadow, /etc/passwd, /etc/sudoers)
  output: >
    Sensitive file accessed 
    (user=%user.name file=%fd.name container=%container.name)
  priority: WARNING
  tags: [filesystem, sensitive_files]
```

## Querying Falco Events

Query your Falco security events in Parseable:

```sql
-- Get recent security events
SELECT time, priority, rule, output
FROM "falco-events"
ORDER BY time DESC
LIMIT 100

-- Find critical security events
SELECT time, rule, output, output_fields
FROM "falco-events"
WHERE priority IN ('Critical', 'Emergency')
ORDER BY time DESC

-- Count events by rule
SELECT 
  rule,
  priority,
  COUNT(*) as event_count
FROM "falco-events"
WHERE time > NOW() - INTERVAL '24 hours'
GROUP BY rule, priority
ORDER BY event_count DESC

-- Find container shell access
SELECT 
  time,
  output_fields->>'container.name' as container,
  output_fields->>'user.name' as user,
  output_fields->>'proc.cmdline' as command
FROM "falco-events"
WHERE rule = 'Terminal shell in container'
ORDER BY time DESC

-- Security events by container
SELECT 
  output_fields->>'container.name' as container,
  COUNT(*) as event_count,
  COUNT(DISTINCT rule) as unique_rules
FROM "falco-events"
WHERE time > NOW() - INTERVAL '1 hour'
GROUP BY container
ORDER BY event_count DESC
```

## Setting Up Alerts

Create Parseable alerts for critical security events:

```json
{
  "name": "Critical Security Event",
  "dataset": "falco-events",
  "alertType": "threshold",
  "condition": {
    "field": "priority",
    "operator": "in",
    "value": ["Critical", "Emergency"]
  },
  "threshold": 1,
  "duration": "1m",
  "webhook": {
    "url": "https://your-pagerduty-webhook",
    "method": "POST"
  }
}
```

## Best Practices

1. **Tune Rules** - Reduce false positives by tuning rules for your environment
2. **Set Priorities** - Use appropriate priority levels for different events
3. **Add Context** - Include container, pod, and namespace information
4. **Create Alerts** - Set up alerts for critical security events
5. **Regular Review** - Regularly review and investigate security events

## Troubleshooting

### Events Not Appearing

1. Verify Falco is running and generating events
2. Check Falco Sidekick logs for errors
3. Verify Parseable URL is accessible
4. Check authentication credentials

### High Volume

1. Increase `minimumpriority` to reduce noise
2. Add filters for specific rules
3. Use sampling for high-volume events

## Next Steps

* Set up [alerts](/docs/user-guide/alerting) for security events
* Create [dashboards](/docs/user-guide/dashboards) for security monitoring
* Configure [Trivy](/docs/ingest-data/security/trivy) for vulnerability scanning


# SIEM Export (/docs/ingest-data/security/siem-export)



Export logs from Parseable to Security Information and Event Management (SIEM) platforms.

## Overview

Export Parseable logs to SIEM platforms for:

* **Security Analysis** - Correlate with other security data
* **Compliance** - Meet regulatory requirements
* **Threat Detection** - Leverage SIEM detection rules
* **Incident Response** - Unified security view

## Supported SIEM Platforms

* Splunk
* IBM QRadar
* Microsoft Sentinel
* Elastic Security
* Sumo Logic
* LogRhythm

## Method 1: Scheduled Export

Export logs on a schedule using scripts or automation.

### Export Script

```python
#!/usr/bin/env python3
import requests
import json
from datetime import datetime, timedelta
import os

PARSEABLE_URL = os.getenv('PARSEABLE_URL')
PARSEABLE_AUTH = (os.getenv('PARSEABLE_USER'), os.getenv('PARSEABLE_PASS'))
SIEM_URL = os.getenv('SIEM_URL')
SIEM_TOKEN = os.getenv('SIEM_TOKEN')

def export_to_siem(dataset, start_time, end_time):
    # Query Parseable using the Query API
    response = requests.post(
        f"{PARSEABLE_URL}/api/v1/query",
        auth=PARSEABLE_AUTH,
        json={
            "query": f"SELECT * FROM {dataset}",
            "startTime": start_time,
            "endTime": end_time,
            "streamName": dataset
        }
    )
    
    logs = response.json()
    
    if not logs:
        return 0
    
    # Transform for SIEM
    siem_events = []
    for log in logs:
        event = {
            "timestamp": log.get('p_timestamp'),
            "source": "parseable",
            "dataset": dataset,
            "event": log
        }
        siem_events.append(event)
    
    # Send to SIEM (Splunk HEC example)
    siem_response = requests.post(
        f"{SIEM_URL}/services/collector/event",
        headers={
            "Authorization": f"Splunk {SIEM_TOKEN}",
            "Content-Type": "application/json"
        },
        json={"event": siem_events}
    )
    
    return len(siem_events)

# Export last hour
end_time = datetime.utcnow()
start_time = end_time - timedelta(hours=1)

datasets = ['security-logs', 'audit-logs', 'access-logs']
for dataset in datasets:
    count = export_to_siem(
        dataset,
        start_time.strftime('%Y-%m-%d %H:%M:%S.%f'),
        end_time.strftime('%Y-%m-%d %H:%M:%S.%f')
    )
    print(f"Exported {count} events from {dataset}")
```

### Kubernetes CronJob

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: siem-export
spec:
  schedule: "0 * * * *"  # Every hour
  jobTemplate:
    spec:
      template:
        spec:
          containers:
            - name: exporter
              image: python:3.11-slim
              command: ["python", "/scripts/export.py"]
              env:
                - name: PARSEABLE_URL
                  value: "http://parseable:8000"
                - name: PARSEABLE_USER
                  valueFrom:
                    secretKeyRef:
                      name: parseable-creds
                      key: username
                - name: PARSEABLE_PASS
                  valueFrom:
                    secretKeyRef:
                      name: parseable-creds
                      key: password
                - name: SIEM_URL
                  value: "https://siem.example.com"
                - name: SIEM_TOKEN
                  valueFrom:
                    secretKeyRef:
                      name: siem-creds
                      key: token
              volumeMounts:
                - name: scripts
                  mountPath: /scripts
          volumes:
            - name: scripts
              configMap:
                name: siem-export-script
          restartPolicy: OnFailure
```

## Method 2: Real-time Streaming

Stream logs in real-time using Fluent Bit.

### Fluent Bit Configuration

```yaml
service:
  flush: 5
  log_level: info

pipeline:
  inputs:
    - name: http
      listen: 0.0.0.0
      port: 8888
      tag: parseable

  outputs:
    # Splunk HEC
    - name: splunk
      match: '*'
      host: splunk.example.com
      port: 8088
      splunk_token: ${SPLUNK_TOKEN}
      tls: On
      tls.verify: Off

    # Elastic
    - name: es
      match: '*'
      host: elastic.example.com
      port: 9200
      index: security-logs
      http_user: ${ES_USER}
      http_passwd: ${ES_PASS}
```

### Configure Parseable Webhook

Set up Parseable alerts to forward to Fluent Bit:

```json
{
  "name": "SIEM Forward",
  "dataset": "security-logs",
  "alertType": "threshold",
  "condition": {
    "field": "level",
    "operator": "in",
    "value": ["error", "critical", "security"]
  },
  "threshold": 1,
  "duration": "1m",
  "webhook": {
    "url": "http://fluent-bit:8888",
    "method": "POST"
  }
}
```

## SIEM-Specific Configurations

### Splunk

```python
def send_to_splunk(events):
    # Splunk HEC expects individual events or batch format
    for event in events:
        payload = {
            "time": event.get('timestamp'),
            "host": "parseable",
            "source": "parseable",
            "sourcetype": "_json",
            "event": event
        }
        
        requests.post(
            f"{SPLUNK_URL}/services/collector/event",
            headers={"Authorization": f"Splunk {SPLUNK_TOKEN}"},
            json=payload
        )

# For batch sending (more efficient for high volume)
def send_to_splunk_batch(events):
    # Splunk HEC batch format: newline-delimited JSON
    batch_payload = "\n".join([
        json.dumps({
            "time": event.get('timestamp'),
            "host": "parseable",
            "source": "parseable",
            "sourcetype": "_json",
            "event": event
        }) for event in events
    ])
    
    requests.post(
        f"{SPLUNK_URL}/services/collector/event",
        headers={"Authorization": f"Splunk {SPLUNK_TOKEN}"},
        data=batch_payload
    )
```

### Microsoft Sentinel

```python
import hashlib
import hmac
import base64

def send_to_sentinel(events):
    workspace_id = os.getenv('SENTINEL_WORKSPACE_ID')
    shared_key = os.getenv('SENTINEL_SHARED_KEY')
    log_type = 'ParseableLogs'
    
    body = json.dumps(events)
    
    # Build signature
    date = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
    content_length = len(body)
    string_to_hash = f"POST\n{content_length}\napplication/json\nx-ms-date:{date}\n/api/logs"
    
    decoded_key = base64.b64decode(shared_key)
    encoded_hash = base64.b64encode(
        hmac.new(decoded_key, string_to_hash.encode('utf-8'), hashlib.sha256).digest()
    ).decode()
    
    signature = f"SharedKey {workspace_id}:{encoded_hash}"
    
    requests.post(
        f"https://{workspace_id}.ods.opinsights.azure.com/api/logs?api-version=2016-04-01",
        headers={
            "Authorization": signature,
            "Content-Type": "application/json",
            "Log-Type": log_type,
            "x-ms-date": date
        },
        data=body
    )
```

### IBM QRadar

```python
def send_to_qradar(events):
    for event in events:
        # Format as syslog
        syslog_msg = f"<14>{event.get('timestamp')} parseable {json.dumps(event)}"
        
        # Send via syslog
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(syslog_msg.encode(), (QRADAR_HOST, 514))
```

## Data Mapping

Map Parseable fields to SIEM fields:

| Parseable     | Splunk     | Sentinel        | QRadar        |
| ------------- | ---------- | --------------- | ------------- |
| `p_timestamp` | `_time`    | `TimeGenerated` | `deviceTime`  |
| `level`       | `severity` | `SeverityLevel` | `severity`    |
| `message`     | `_raw`     | `Message`       | `payload`     |
| `source`      | `source`   | `SourceSystem`  | `logSourceId` |

## Best Practices

1. **Filter First** - Only export security-relevant logs
2. **Normalize Data** - Map to SIEM schema
3. **Handle Failures** - Implement retry logic
4. **Monitor Lag** - Track export latency
5. **Deduplicate** - Prevent duplicate events

## Troubleshooting

### Export Failures

1. Check SIEM connectivity
2. Verify authentication tokens
3. Check rate limits
4. Verify data format

### Missing Events

1. Check time range queries
2. Verify dataset names
3. Check export schedule

## Next Steps

* Set up [alerts](/docs/user-guide/alerting) for security events
* Configure [Falco](/docs/ingest-data/security/falco) for runtime security
* Create [dashboards](/docs/user-guide/dashboards) for security monitoring


# Trivy (/docs/ingest-data/security/trivy)



Collect and analyze Trivy vulnerability scan results in Parseable for comprehensive security monitoring.

## Overview

Integrate Trivy with Parseable to:

* **Vulnerability Tracking** - Track vulnerabilities across your infrastructure
* **Container Security** - Scan container images for known vulnerabilities
* **IaC Security** - Detect misconfigurations in infrastructure code
* **Compliance** - Monitor security compliance over time

## Prerequisites

* Trivy installed (CLI or Operator)
* Parseable instance accessible
* CI/CD pipeline or scheduled scanning

## What is Trivy?

Trivy is a comprehensive security scanner that detects:

* **Vulnerabilities** - CVEs in OS packages and application dependencies
* **Misconfigurations** - Security issues in IaC (Terraform, Kubernetes, etc.)
* **Secrets** - Hardcoded secrets and credentials
* **Licenses** - License compliance issues

## Method 1: CI/CD Integration

Send scan results from your CI/CD pipeline.

### GitHub Actions

```yaml
name: Security Scan

on:
  push:
    branches: [main]
  schedule:
    - cron: '0 0 * * *'  # Daily scan

jobs:
  trivy-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          scan-ref: '.'
          format: 'json'
          output: 'trivy-results.json'
      
      - name: Send results to Parseable
        run: |
          # Transform Trivy output to Parseable format
          jq -c '[.Results[] | .Vulnerabilities[]? | {
            timestamp: now | strftime("%Y-%m-%dT%H:%M:%SZ"),
            scan_type: "filesystem",
            repository: "${{ github.repository }}",
            ref: "${{ github.ref }}",
            sha: "${{ github.sha }}",
            vulnerability_id: .VulnerabilityID,
            pkg_name: .PkgName,
            installed_version: .InstalledVersion,
            fixed_version: .FixedVersion,
            severity: .Severity,
            title: .Title,
            description: .Description,
            cvss_score: .CVSS.nvd.V3Score
          }]' trivy-results.json > parseable-payload.json
          
          curl -X POST "${{ secrets.PARSEABLE_URL }}/api/v1/ingest" \
            -H "Authorization: Basic ${{ secrets.PARSEABLE_AUTH }}" \
            -H "X-P-Stream: trivy-vulnerabilities" \
            -H "Content-Type: application/json" \
            -d @parseable-payload.json
```

### Container Image Scanning

```yaml
name: Container Security Scan

on:
  push:
    branches: [main]

jobs:
  scan-image:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Build image
        run: docker build -t myapp:${{ github.sha }} .
      
      - name: Run Trivy scanner
        run: |
          trivy image --format json --output trivy-results.json myapp:${{ github.sha }}
      
      - name: Send to Parseable
        run: |
          jq -c '[.Results[] | .Vulnerabilities[]? | {
            timestamp: now | strftime("%Y-%m-%dT%H:%M:%SZ"),
            scan_type: "container",
            image: "myapp:${{ github.sha }}",
            repository: "${{ github.repository }}",
            target: .Target,
            vulnerability_id: .VulnerabilityID,
            pkg_name: .PkgName,
            installed_version: .InstalledVersion,
            fixed_version: .FixedVersion,
            severity: .Severity,
            title: .Title
          }]' trivy-results.json > payload.json
          
          curl -X POST "${{ secrets.PARSEABLE_URL }}/api/v1/ingest" \
            -H "Authorization: Basic ${{ secrets.PARSEABLE_AUTH }}" \
            -H "X-P-Stream: trivy-vulnerabilities" \
            -H "Content-Type: application/json" \
            -d @payload.json
```

### GitLab CI

```yaml
trivy-scan:
  stage: security
  image: aquasec/trivy:latest
  script:
    - trivy image --format json --output trivy-results.json $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
    - |
      apk add --no-cache jq curl
      jq -c '[.Results[] | .Vulnerabilities[]? | {
        timestamp: now | strftime("%Y-%m-%dT%H:%M:%SZ"),
        scan_type: "container",
        image: "'$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA'",
        project: "'$CI_PROJECT_PATH'",
        vulnerability_id: .VulnerabilityID,
        pkg_name: .PkgName,
        severity: .Severity,
        title: .Title
      }]' trivy-results.json > payload.json
      
      curl -X POST "${PARSEABLE_URL}/api/v1/ingest" \
        -H "Authorization: Basic ${PARSEABLE_AUTH}" \
        -H "X-P-Stream: trivy-vulnerabilities" \
        -H "Content-Type: application/json" \
        -d @payload.json
```

## Method 2: Trivy Operator

Use the Trivy Operator for continuous Kubernetes scanning.

### Install Trivy Operator

```bash
helm repo add aqua https://aquasecurity.github.io/helm-charts/
helm repo update

helm install trivy-operator aqua/trivy-operator \
  --namespace trivy-system \
  --create-namespace
```

### Collect Reports with Fluent Bit

```yaml
# fluent-bit-config.yaml
service:
  flush: 30
  log_level: info

pipeline:
  inputs:
    - name: kubernetes_events
      tag: k8s_events
      kube_url: https://kubernetes.default.svc
      
  filters:
    - name: grep
      match: k8s_events
      regex: involvedObject.kind VulnerabilityReport

  outputs:
    - name: http
      match: k8s_events
      host: parseable
      port: 8000
      uri: /api/v1/ingest
      format: json
      header: Authorization Basic YWRtaW46YWRtaW4=
      header: X-P-Stream trivy-operator
```

### Export Reports Script

Create a script to export Trivy Operator reports:

```bash
#!/bin/bash
# export-trivy-reports.sh

PARSEABLE_URL="${PARSEABLE_URL:-http://parseable:8000}"
PARSEABLE_AUTH="${PARSEABLE_AUTH:-YWRtaW46YWRtaW4=}"

# Get all VulnerabilityReports
kubectl get vulnerabilityreports -A -o json | jq -c '
  [.items[] | {
    timestamp: .metadata.creationTimestamp,
    namespace: .metadata.namespace,
    name: .metadata.name,
    image: .report.artifact.repository,
    tag: .report.artifact.tag,
    critical: .report.summary.criticalCount,
    high: .report.summary.highCount,
    medium: .report.summary.mediumCount,
    low: .report.summary.lowCount,
    vulnerabilities: [.report.vulnerabilities[] | {
      id: .vulnerabilityID,
      severity: .severity,
      pkg: .resource,
      version: .installedVersion,
      fixed: .fixedVersion,
      title: .title
    }]
  }]
' > /tmp/vuln-reports.json

curl -X POST "${PARSEABLE_URL}/api/v1/ingest" \
  -H "Authorization: Basic ${PARSEABLE_AUTH}" \
  -H "X-P-Stream: trivy-operator" \
  -H "Content-Type: application/json" \
  -d @/tmp/vuln-reports.json
```

### Kubernetes CronJob

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: trivy-report-exporter
spec:
  schedule: "0 * * * *"  # Every hour
  jobTemplate:
    spec:
      template:
        spec:
          serviceAccountName: trivy-exporter
          containers:
            - name: exporter
              image: bitnami/kubectl:latest
              command: ["/bin/bash", "/scripts/export-trivy-reports.sh"]
              env:
                - name: PARSEABLE_URL
                  value: "http://parseable:8000"
                - name: PARSEABLE_AUTH
                  valueFrom:
                    secretKeyRef:
                      name: parseable-auth
                      key: auth
              volumeMounts:
                - name: scripts
                  mountPath: /scripts
          volumes:
            - name: scripts
              configMap:
                name: trivy-exporter-scripts
          restartPolicy: OnFailure
```

## Method 3: Direct CLI Integration

Send scan results directly from Trivy CLI.

### Wrapper Script

```bash
#!/bin/bash
# trivy-to-parseable.sh

PARSEABLE_URL="${PARSEABLE_URL:-http://localhost:8000}"
PARSEABLE_AUTH="${PARSEABLE_AUTH:-YWRtaW46YWRtaW4=}"
STREAM="${STREAM:-trivy-scans}"

# Run Trivy scan
trivy "$@" --format json --output /tmp/trivy-results.json

# Transform and send to Parseable
jq -c '[{
  timestamp: now | strftime("%Y-%m-%dT%H:%M:%SZ"),
  scan_target: .ArtifactName,
  scan_type: .ArtifactType,
  results: [.Results[] | {
    target: .Target,
    class: .Class,
    type: .Type,
    vulnerabilities: (.Vulnerabilities // []) | length,
    critical: [(.Vulnerabilities // [])[] | select(.Severity == "CRITICAL")] | length,
    high: [(.Vulnerabilities // [])[] | select(.Severity == "HIGH")] | length,
    medium: [(.Vulnerabilities // [])[] | select(.Severity == "MEDIUM")] | length,
    low: [(.Vulnerabilities // [])[] | select(.Severity == "LOW")] | length
  }]
}]' /tmp/trivy-results.json > /tmp/parseable-payload.json

curl -s -X POST "${PARSEABLE_URL}/api/v1/ingest" \
  -H "Authorization: Basic ${PARSEABLE_AUTH}" \
  -H "X-P-Stream: ${STREAM}" \
  -H "Content-Type: application/json" \
  -d @/tmp/parseable-payload.json

echo "Scan results sent to Parseable"
```

Usage:

```bash
./trivy-to-parseable.sh image nginx:latest
./trivy-to-parseable.sh fs /path/to/project
./trivy-to-parseable.sh config /path/to/terraform
```

## Querying Trivy Results

Query your vulnerability data in Parseable:

```sql
-- Get recent vulnerability scans
SELECT timestamp, scan_target, scan_type, 
       results[0].critical as critical,
       results[0].high as high
FROM "trivy-scans"
ORDER BY timestamp DESC
LIMIT 100

-- Find critical vulnerabilities
SELECT timestamp, image, vulnerability_id, pkg_name, title
FROM "trivy-vulnerabilities"
WHERE severity = 'CRITICAL'
ORDER BY timestamp DESC

-- Vulnerability count by severity
SELECT 
  severity,
  COUNT(*) as count
FROM "trivy-vulnerabilities"
WHERE timestamp > NOW() - INTERVAL '7 days'
GROUP BY severity
ORDER BY 
  CASE severity 
    WHEN 'CRITICAL' THEN 1 
    WHEN 'HIGH' THEN 2 
    WHEN 'MEDIUM' THEN 3 
    WHEN 'LOW' THEN 4 
  END

-- Most vulnerable images
SELECT 
  image,
  COUNT(*) as total_vulns,
  SUM(CASE WHEN severity = 'CRITICAL' THEN 1 ELSE 0 END) as critical,
  SUM(CASE WHEN severity = 'HIGH' THEN 1 ELSE 0 END) as high
FROM "trivy-vulnerabilities"
WHERE timestamp > NOW() - INTERVAL '24 hours'
GROUP BY image
ORDER BY critical DESC, high DESC
LIMIT 20

-- Vulnerabilities with available fixes
SELECT vulnerability_id, pkg_name, installed_version, fixed_version, severity
FROM "trivy-vulnerabilities"
WHERE fixed_version IS NOT NULL AND fixed_version != ''
ORDER BY 
  CASE severity 
    WHEN 'CRITICAL' THEN 1 
    WHEN 'HIGH' THEN 2 
  END
LIMIT 50
```

## Setting Up Alerts

Create alerts for critical vulnerabilities:

```json
{
  "name": "Critical Vulnerability Detected",
  "dataset": "trivy-vulnerabilities",
  "alertType": "threshold",
  "condition": {
    "field": "severity",
    "operator": "equals",
    "value": "CRITICAL"
  },
  "threshold": 1,
  "duration": "5m",
  "webhook": {
    "url": "https://your-slack-webhook",
    "method": "POST"
  }
}
```

## Best Practices

1. **Scan Regularly** - Run scans on every build and on a schedule
2. **Track Trends** - Monitor vulnerability counts over time
3. **Prioritize Fixes** - Focus on critical and high severity first
4. **Include Context** - Add repository, image, and commit information
5. **Set SLAs** - Define remediation timelines by severity

## Troubleshooting

### Empty Results

1. Verify Trivy is finding vulnerabilities (check raw output)
2. Check jq transformation is correct
3. Verify Parseable dataset accepts the payload format

### Large Payloads

1. Split large scans into smaller batches
2. Send summary data instead of full vulnerability details
3. Use compression if supported

## Next Steps

* Set up [alerts](/docs/user-guide/alerting) for vulnerability thresholds
* Create [dashboards](/docs/user-guide/dashboards) for security posture
* Configure [Falco](/docs/ingest-data/security/falco) for runtime security


# Cribl (/docs/ingest-data/streaming/cribl)















This guide explains how to add Parseable as a destination in Cribl Stream to forward your telemetry data.

## Prerequisites

* A running Cribl Stream instance
* [Parseable Cloud account](https://app.parseable.com)
* Your Parseable ingestor endpoint URL (obtain this from your Parseable Cloud dashboard)

## Adding Parseable as a Destination

To add a destination, you can use either QuickConnect or Routes. Here's how to use QuickConnect:

### Using QuickConnect

1. If on a Distributed deployment, select **Worker Groups** in the sidebar and choose a Worker Group.
2. Navigate to **Routing > QuickConnect**.
3. Select **Add Destination** and choose **OpenTelemetry** from the list.

<img alt="Set up new QuickConnect Destination" src={__img0} placeholder="blur" />

### Configure General Settings

<img alt="Select OpenTelemetry destination" src={__img1} placeholder="blur" />

After selecting OpenTelemetry as your destination, configure the following settings:

<img alt="Cribl OpenTelemetry General Settings" src={__img2} placeholder="blur" />

| Setting          | Value                                                                                                                                                                                                         |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Output ID**    | A unique identifier for this destination (e.g., `Cribl-telemetry`)                                                                                                                                            |
| **Description**  | A description for this destination (e.g., `telemetry from cribl to parseable`)                                                                                                                                |
| **OTLP version** | `0.10.0`                                                                                                                                                                                                      |
| **Protocol**     | `HTTP`                                                                                                                                                                                                        |
| **Endpoint**     | Your Parseable ingestor URL (e.g., `https://<your-instance>-ingestor.workspace-staging.parseable.com`) - make sure to use the correct ingestor URL for your environment without any trailing slash in the end |

### Configure Advanced Settings

Navigate to **Advanced Settings** to configure additional options:

<img alt="Cribl Advanced Settings" src={__img3} placeholder="blur" />

| Setting                   | Recommended Value |
| ------------------------- | ----------------- |
| **Validate server certs** | Enabled           |
| **Keep alive**            | Enabled           |
| **Compression**           | `Gzip`            |
| **Request timeout**       | `30`              |
| **Request concurrency**   | `5`               |
| **Body size limit (KB)**  | `4096`            |
| **Flush period (sec)**    | `1`               |

### Configure Extra HTTP Headers

Add the following HTTP headers to route data to the correct Parseable stream:

| Field Name       | Field Value                                                               |
| ---------------- | ------------------------------------------------------------------------- |
| `X-P-Log-Source` | `otel-metrics`, `otel-logs`, `otel-traces` (or your preferred log source) |
| `X-P-Stream`     | Your target stream name (e.g., `cribl-telemetry-new`)                     |

## Authentication

Parseable instance requires authentication, navigate to the **Authentication** tab and configure your credentials:

* For Parseable Cloud, use your Login credentials

<img alt="Cribl Authentication" src={__img4} placeholder="blur" />

## Save and Test

1. Click **Save** to save your destination configuration.
2. Use the **Test** tab to verify connectivity to your Parseable instance.
   <img alt="Test Connection" src={__img5} placeholder="blur" />
3. Check the **Live Data** tab to monitor incoming data.


# Kafka (/docs/ingest-data/streaming/kafka)



The Parseable Kafka Connector enables log ingestion from Apache Kafka into Parseable, providing a high-performance, scalable, and efficient logging pipeline.

## Features

* Consumer & Producer Support: Supports both consuming and producing messages (ready to use for DLT).
* Configurable Buffering & Performance Settings: Optimized for high-throughput data processing.
* Security Integration: Supports SSL/TLS and SASL authentication.
* Fault Tolerance & Partitioning: Handles partition balancing, offsets, and error handling.

## Configuration Options

### General Kafka Configuration

| Parameter                          | Environment Variable                     | Default Value       | Description                                               | Usage                                                                                                                                  |
| ---------------------------------- | ---------------------------------------- | ------------------- | --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `--bootstrap-servers`              | `P_KAFKA_BOOTSTRAP_SERVERS`              | `localhost:9092`    | Comma-separated list of Kafka bootstrap servers.          | Specifies the Kafka brokers the client should connect to.                                                                              |
| `--client-id`                      | `P_KAFKA_CLIENT_ID`                      | `parseable-connect` | Client ID for Kafka connection.                           | Identifies the client instance in Kafka logs.                                                                                          |
| `--partition-listener-concurrency` | `P_KAFKA_PARTITION_LISTENER_CONCURRENCY` | `2`                 | Number of parallel threads for Kafka partition listeners. | Determines the number of threads used to process Kafka partitions.                                                                     |
| `--bad-data-policy`                | `P_CONNECTOR_BAD_DATA_POLICY`            | `fail`              | Policy for handling bad data.                             | Determines how the client should handle corrupt or invalid messages. Options: fail, drop (not yet supported), dlt (not yet supported). |

* All parameters can be set using command-line arguments or environment variables.
* Environment variables take precedence over default values.
* When configuring both producer and consumer, make sure to specify relevant options in their respective sections.

For more details, refer to [Kafka's official documentation](https://kafka.apache.org/documentation).

### Consumer Configuration

| Parameter                               | Environment Variable                          | Default Value                      | Description                                            | Usage                                                                                |
| --------------------------------------- | --------------------------------------------- | ---------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `--consumer-topics`                     | `P_KAFKA_CONSUMER_TOPICS`                     | `None`                             | Comma-separated list of topics to consume from.        | Specify the Kafka topics the consumer should subscribe to.                           |
| `--consumer-group-id`                   | `P_KAFKA_CONSUMER_GROUP_ID`                   | `parseable-connect-cg`             | The consumer group ID.                                 | Used to group consumers for load balancing and fault tolerance.                      |
| `--buffer-size`                         | `P_KAFKA_CONSUMER_BUFFER_SIZE`                | `10000`                            | Size of the buffer for batching records per partition. | Controls the number of messages buffered before processing.                          |
| `--buffer-timeout`                      | `P_KAFKA_CONSUMER_BUFFER_TIMEOUT`             | `10000ms`                          | Timeout for buffer flush in milliseconds.              | Defines the time to wait before flushing buffered messages.                          |
| `--consumer-group-instance-id`          | `P_KAFKA_CONSUMER_GROUP_INSTANCE_ID`          | `parseable-connect-cg-ii-{random}` | Group instance ID for static membership.               | Useful for maintaining static assignments in consumer groups.                        |
| `--consumer-partition-strategy`         | `P_KAFKA_CONSUMER_PARTITION_STRATEGY`         | `roundrobin,range`                 | Partition assignment strategy.                         | Determines how partitions are assigned among consumers.                              |
| `--consumer-session-timeout`            | `P_KAFKA_CONSUMER_SESSION_TIMEOUT`            | `60000`                            | Session timeout in milliseconds.                       | Time before a consumer is considered inactive.                                       |
| `--consumer-heartbeat-interval`         | `P_KAFKA_CONSUMER_HEARTBEAT_INTERVAL`         | `3000`                             | Heartbeat interval in milliseconds.                    | Frequency at which consumers send heartbeats.                                        |
| `--consumer-max-poll-interval`          | `P_KAFKA_CONSUMER_MAX_POLL_INTERVAL`          | `300000`                           | Maximum poll interval in milliseconds.                 | Maximum time between poll calls before the consumer is considered dead.              |
| `--consumer-enable-auto-offset-store`   | `P_KAFKA_CONSUMER_ENABLE_AUTO_OFFSET_STORE`   | `true`                             | Enable auto offset store.                              | Determines whether offsets are automatically stored after processing messages.       |
| `--consumer-auto-offset-reset`          | `P_KAFKA_CONSUMER_AUTO_OFFSET_RESET`          | `earliest`                         | Auto offset reset behavior.                            | Determines whether to start from the beginning (earliest) or latest (latest) offset. |
| `--consumer-fetch-min-bytes`            | `P_KAFKA_CONSUMER_FETCH_MIN_BYTES`            | `1`                                | Minimum bytes to fetch.                                | The smallest amount of data the broker should send.                                  |
| `--consumer-fetch-max-bytes`            | `P_KAFKA_CONSUMER_FETCH_MAX_BYTES`            | `52428800`                         | Maximum bytes to fetch.                                | The maximum amount of data fetched in a single request.                              |
| `--consumer-fetch-max-wait`             | `P_KAFKA_CONSUMER_FETCH_MAX_WAIT`             | `500`                              | Maximum wait time for fetch in milliseconds.           | Maximum time the broker should wait before sending data.                             |
| `--consumer-max-partition-fetch-bytes`  | `P_KAFKA_CONSUMER_MAX_PARTITION_FETCH_BYTES`  | `1048576`                          | Maximum bytes to fetch per partition.                  | Limits the maximum data fetched per partition.                                       |
| `--consumer-queued-min-messages`        | `P_KAFKA_CONSUMER_QUEUED_MIN_MESSAGES`        | `100000`                           | Minimum messages to queue.                             | Controls the minimum number of messages buffered in the consumer.                    |
| `--consumer-queued-max-messages-kbytes` | `P_KAFKA_CONSUMER_QUEUED_MAX_MESSAGES_KBYTES` | `65536`                            | Maximum message queue size in KBytes.                  | Determines the maximum queue size in kilobytes.                                      |
| `--consumer-enable-partition-eof`       | `P_KAFKA_CONSUMER_ENABLE_PARTITION_EOF`       | `false`                            | Enable partition EOF.                                  | Signals when the end of a partition is reached.                                      |
| `--consumer-check-crcs`                 | `P_KAFKA_CONSUMER_CHECK_CRCS`                 | `false`                            | Check CRCs on messages.                                | Ensures message integrity by verifying CRCs.                                         |
| `--consumer-isolation-level`            | `P_KAFKA_CONSUMER_ISOLATION_LEVEL`            | `read_committed`                   | Transaction isolation level.                           | Controls whether uncommitted transactions should be visible to the consumer.         |
| `--consumer-fetch-message-max-bytes`    | `P_KAFKA_CONSUMER_FETCH_MESSAGE_MAX_BYTES`    | `1048576`                          | Maximum bytes per message.                             | Defines the largest individual message the consumer can fetch.                       |
| `--consumer-stats-interval`             | `P_KAFKA_CONSUMER_STATS_INTERVAL`             | `10000`                            | Statistics interval in milliseconds.                   | Defines the frequency at which consumer statistics are collected.                    |

* All parameters can be set using command-line arguments or environment variables.
* Environment variables take precedence over default values.
* Some values, such as `group_instance_id`, are dynamically generated if not explicitly provided.

For more details, refer to [Kafka's official documentation on consumer configurations](https://kafka.apache.org/documentation#consumerconfigs).

### Producer Configuration

<Callout type="info">
  Producer configuration is not necessary at this moment. When DLT is implemented, these settings will be required.
</Callout>

| Parameter                                 | Environment Variable                            | Default Value | Description                                                   | Usage                                                                   |
| ----------------------------------------- | ----------------------------------------------- | ------------- | ------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `--producer-acks`                         | `P_KAFKA_PRODUCER_ACKS`                         | `all`         | Number of acknowledgments the producer requires.              | Determines when a message is considered successfully sent (0, 1, all).  |
| `--producer-compression-type`             | `P_KAFKA_PRODUCER_COMPRESSION_TYPE`             | `lz4`         | Compression type for messages.                                | Determines how messages are compressed (none, gzip, snappy, lz4, zstd). |
| `--producer-batch-size`                   | `P_KAFKA_PRODUCER_BATCH_SIZE`                   | `16384`       | Maximum size of a request in bytes.                           | Defines the size of batches sent to Kafka.                              |
| `--producer-linger-ms`                    | `P_KAFKA_PRODUCER_LINGER_MS`                    | `5`           | Delay to wait for more messages in the same batch.            | Controls latency vs. throughput trade-off.                              |
| `--producer-message-timeout-ms`           | `P_KAFKA_PRODUCER_MESSAGE_TIMEOUT_MS`           | `120000`      | Local message timeout.                                        | Time before an unacknowledged message is dropped.                       |
| `--producer-max-inflight`                 | `P_KAFKA_PRODUCER_MAX_INFLIGHT`                 | `5`           | Maximum number of in-flight requests per connection.          | Controls how many messages can be sent without acknowledgment.          |
| `--producer-message-max-bytes`            | `P_KAFKA_PRODUCER_MESSAGE_MAX_BYTES`            | `1048576`     | Maximum size of a message in bytes.                           | Restricts the maximum message size that can be sent.                    |
| `--producer-enable-idempotence`           | `P_KAFKA_PRODUCER_ENABLE_IDEMPOTENCE`           | `true`        | Enable idempotent producer.                                   | Ensures exactly-once delivery guarantees.                               |
| `--producer-transaction-timeout-ms`       | `P_KAFKA_PRODUCER_TRANSACTION_TIMEOUT_MS`       | `60000`       | Transaction timeout.                                          | Maximum time for a transaction before it times out.                     |
| `--producer-buffer-memory`                | `P_KAFKA_PRODUCER_BUFFER_MEMORY`                | `33554432`    | Total bytes of memory the producer can use.                   | Limits the memory available for buffering messages.                     |
| `--producer-retry-backoff-ms`             | `P_KAFKA_PRODUCER_RETRY_BACKOFF_MS`             | `100`         | Time to wait before retrying a failed request.                | Defines back-off time for retries.                                      |
| `--producer-request-timeout-ms`           | `P_KAFKA_PRODUCER_REQUEST_TIMEOUT_MS`           | `30000`       | Time to wait for a response from brokers.                     | Limits how long the producer waits for broker acknowledgment.           |
| `--producer-queue-buffering-max-messages` | `P_KAFKA_PRODUCER_QUEUE_BUFFERING_MAX_MESSAGES` | `100000`      | Maximum number of messages allowed on the producer queue.     | Prevents excessive message buffering.                                   |
| `--producer-queue-buffering-max-kbytes`   | `P_KAFKA_PRODUCER_QUEUE_BUFFERING_MAX_KBYTES`   | `1048576`     | Maximum total message size sum allowed on the producer queue. | Restricts the producer queue's total size.                              |
| `--producer-delivery-timeout-ms`          | `P_KAFKA_PRODUCER_DELIVERY_TIMEOUT_MS`          | `120000`      | Maximum time to report success or failure after send.         | Defines the upper bound on message delivery time.                       |
| `--producer-max-retries`                  | `P_KAFKA_PRODUCER_MAX_RETRIES`                  | `2147483647`  | Maximum number of retries per message.                        | Controls how many times a message is retried before failing.            |
| `--producer-retry-backoff-max-ms`         | `P_KAFKA_PRODUCER_RETRY_BACKOFF_MAX_MS`         | `1000`        | Maximum back-off time between retries.                        | Ensures retries are not too frequent.                                   |

* All parameters can be set using command-line arguments or environment variables.
* Environment variables take precedence over default values.
* Certain parameters, such as `--producer-acks` and `--producer-enable-idempotence`, affect message durability and reliability.

For more details, refer to [Kafka's official documentation on producer configurations](https://kafka.apache.org/documentation#producerconfigs).

### Security Configuration

| Parameter                    | Environment Variable               | Default Value | Description                               | Usage                                                                                                        |
| ---------------------------- | ---------------------------------- | ------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `--security-protocol`        | `P_KAFKA_SECURITY_PROTOCOL`        | `PLAINTEXT`   | Security protocol used for communication. | Determines whether SSL, SASL, or plaintext is used.                                                          |
| `--ssl-ca-location`          | `P_KAFKA_SSL_CA_LOCATION`          | `None`        | CA certificate file path.                 | Required when using SSL or SASL\_SSL.                                                                        |
| `--ssl-certificate-location` | `P_KAFKA_SSL_CERTIFICATE_LOCATION` | `None`        | Client certificate file path.             | Required when using SSL or SASL\_SSL.                                                                        |
| `--ssl-key-location`         | `P_KAFKA_SSL_KEY_LOCATION`         | `None`        | Client key file path.                     | Required when using SSL or SASL\_SSL.                                                                        |
| `--ssl-key-password`         | `P_KAFKA_SSL_KEY_PASSWORD`         | `None`        | SSL key password.                         | Used if the SSL key is password protected.                                                                   |
| `--sasl-mechanism`           | `P_KAFKA_SASL_MECHANISM`           | `None`        | SASL authentication mechanism.            | Required when using SASL\_SSL or SASL\_PLAINTEXT (PLAIN, SCRAM-SHA-256, SCRAM-SHA-512, GSSAPI, OAUTHBEARER). |
| `--sasl-username`            | `P_KAFKA_SASL_USERNAME`            | `None`        | SASL username.                            | Required for PLAIN or SCRAM SASL mechanisms.                                                                 |
| `--sasl-password`            | `P_KAFKA_SASL_PASSWORD`            | `None`        | SASL password.                            | Required for PLAIN or SCRAM SASL mechanisms.                                                                 |
| `--kerberos-service-name`    | `P_KAFKA_KERBEROS_SERVICE_NAME`    | `None`        | Kerberos service name.                    | Required when using GSSAPI SASL mechanism.                                                                   |
| `--kerberos-principal`       | `P_KAFKA_KERBEROS_PRINCIPAL`       | `None`        | Kerberos principal.                       | Used for Kerberos authentication.                                                                            |
| `--kerberos-keytab`          | `P_KAFKA_KERBEROS_KEYTAB`          | `None`        | Path to Kerberos keytab file.             | Required when using Kerberos authentication.                                                                 |
| `--oauth-token-endpoint`     | `P_KAFKA_OAUTH_TOKEN_ENDPOINT`     | `None`        | OAuth Bearer token endpoint.              | Required when using OAUTHBEARER SASL mechanism.                                                              |
| `--oauth-client-id`          | `P_KAFKA_OAUTH_CLIENT_ID`          | `None`        | OAuth client ID.                          | Used for authentication with an OAuth provider.                                                              |
| `--oauth-client-secret`      | `P_KAFKA_OAUTH_CLIENT_SECRET`      | `None`        | OAuth client secret.                      | Used to authenticate the OAuth client.                                                                       |
| `--oauth-scope`              | `P_KAFKA_OAUTH_SCOPE`              | `None`        | OAuth scope.                              | Defines the permissions requested from the OAuth provider.                                                   |

### Security Configuration Combinations

#### Plaintext Communication (No Security)

* `--security-protocol=PLAINTEXT`
* No additional parameters required.

#### SSL Encryption

* `--security-protocol=SSL`

Required parameters:

* `--ssl-ca-location`
* `--ssl-certificate-location`
* `--ssl-key-location`
* `--ssl-key-password` (if the key is password-protected)

#### SASL Authentication with SSL

* `--security-protocol=SASL_SSL`

Required parameters:

* `--sasl-mechanism`
* `--sasl-username` and `--sasl-password` (for PLAIN or SCRAM mechanisms)
* `--kerberos-service-name` and `--kerberos-principal` (for GSSAPI mechanism)
* `--kerberos-keytab` (if using Kerberos authentication)

SSL parameters (if required by the security policy)

#### SASL Authentication without SSL

* `--security-protocol=SASL_PLAINTEXT`

Required parameters:

* `--sasl-mechanism`
* `--sasl-username` and `--sasl-password` (for PLAIN or SCRAM mechanisms)
* `--kerberos-service-name` and `--kerberos-principal` (for GSSAPI mechanism)
* `--kerberos-keytab` (if using Kerberos authentication)

#### OAuth Bearer Token Authentication (Not supported yet)

* `--security-protocol=SASL_SSL or SASL_PLAINTEXT`
* `--sasl-mechanism=OAUTHBEARER`

Required parameters:

* `--oauth-token-endpoint`
* `--oauth-client-id`
* `--oauth-client-secret`
* `--oauth-scope` (if required by the OAuth provider)

#### Examples

##### SSL Configuration

```bash
export P_KAFKA_SECURITY_PROTOCOL="SSL"
export P_KAFKA_SSL_CA_LOCATION="/path/to/ca.pem"
export P_KAFKA_SSL_CERTIFICATE_LOCATION="/path/to/client-cert.pem"
export P_KAFKA_SSL_KEY_LOCATION="/path/to/client-key.pem"
export P_KAFKA_SSL_KEY_PASSWORD="my-secure-password"
```

##### SASL Configuration

```bash
export P_KAFKA_SECURITY_PROTOCOL="SASL_SSL"
export P_KAFKA_SASL_MECHANISM="SCRAM-SHA-512"
export P_KAFKA_SASL_USERNAME="my-user"
export P_KAFKA_SASL_PASSWORD="my-password"
```

For more details, refer to [Kafka's official security documentation](https://kafka.apache.org/documentation#security_sasl).

#### Concurrency and Multi-Instance Processing

The connector uses a dedicated thread per partition with configurable concurrency:

```bash
export P_KAFKA_PARTITION_LISTENER_CONCURRENCY="2"
```

Thread Assignment Formula:

```bash
Threads per ingestor = min(Partitions per ingestor, Configured threads)
```

##### Example Scenarios:

Balanced Configuration:

* 6 partitions
* 2 ingest nodes
* 3 threads per node

Result: Each thread handles one partition

Over-threaded Configuration:

* 4 partitions
* 2 ingest nodes
* 4 threads per node

Result: 2 threads per node will be idle

##### Consumer Group Rebalancing

Rebalance triggers:

* New consumer joins
* Existing consumer leaves
* Network issues
* Partition reassignment

Available strategies:

* Range: Assigns consecutive partitions
* RoundRobin: Distributes evenly
* Sticky: Minimizes reassignments (Not recommended for Parseable since rdKafka issues)
* CooperativeSticky: Controlled rebalance (Not recommended for Parseable since rdKafka support is lacking)

Recommended configuration(by default):

```bash
export P_KAFKA_CONSUMER_PARTITION_STRATEGY="roundrobin,range"
export P_KAFKA_CONSUMER_SESSION_TIMEOUT="60000"
export P_KAFKA_CONSUMER_HEARTBEAT_INTERVAL="3000"
```

#### Metrics

All metrics listed in [librdkafka's statistics documentation](https://github.com/edenhill/librdkafka/blob/master/STATISTICS.mdx) are available at the /metrics endpoint.

#### Architecture and Design

##### Core Components

* KafkaStreams: Manages consumers and partitions.
* StreamWorker: Processes records per partition.
* ParseableSinkProcessor: Transforms messages and sinks them to Parseable.
* RebalanceListener: Handles partition rebalancing.
* Metrics Collector: Provides Prometheus metrics.

#### Security Layer: Configurable authentication.

##### Error Handling

| Error Type        | Handling Strategy      |
| ----------------- | ---------------------- |
| Connection Errors | Retries every 1 second |
| Fatal Errors      | Stops the pipeline     |
| Auth Errors       | Stops the pipeline     |

### Best Practices

Performance Tuning:

* More partitions = Better parallelism
* Use RoundRobin partition assignment
* Increase partition count for high lag

Security:

* Prefer SSL over SASL\_PLAINTEXT
* Rotate certificates regularly
* Monitor authentication failures


# NATS (/docs/ingest-data/streaming/nats)



Stream logs from NATS messaging system to Parseable.

## Overview

Integrate NATS with Parseable to:

* **Cloud Native Messaging** - Lightweight, high-performance messaging
* **Pub/Sub Logs** - Subscribe to log topics
* **JetStream** - Persistent message streaming
* **Low Latency** - Sub-millisecond message delivery

## Prerequisites

* NATS server running
* Parseable instance accessible
* NATS client library

## Method 1: Custom Subscriber

Build a subscriber to forward messages to Parseable.

### Node.js Subscriber

```javascript
const { connect, StringCodec } = require('nats');
const axios = require('axios');

const NATS_URL = process.env.NATS_URL || 'localhost:4222';
const SUBJECT = process.env.NATS_SUBJECT || 'logs.>';
const PARSEABLE_URL = process.env.PARSEABLE_URL;
const PARSEABLE_AUTH = process.env.PARSEABLE_AUTH;

const sc = StringCodec();

async function subscribe() {
  const nc = await connect({ servers: NATS_URL });
  console.log(`Connected to NATS at ${NATS_URL}`);
  
  const batch = [];
  const BATCH_SIZE = 100;
  const BATCH_TIMEOUT = 5000;
  
  let timeout = null;
  
  const sendBatch = async () => {
    if (batch.length === 0) return;
    
    const logs = batch.splice(0, batch.length);
    
    try {
      await axios.post(`${PARSEABLE_URL}/api/v1/ingest`, logs, {
        headers: {
          'Authorization': `Basic ${PARSEABLE_AUTH}`,
          'X-P-Stream': 'nats-logs',
          'Content-Type': 'application/json'
        }
      });
      console.log(`Sent ${logs.length} logs to Parseable`);
    } catch (error) {
      console.error('Error sending to Parseable:', error.message);
    }
  };
  
  const sub = nc.subscribe(SUBJECT);
  console.log(`Subscribed to: ${SUBJECT}`);
  
  for await (const msg of sub) {
    try {
      const data = sc.decode(msg.data);
      const log = JSON.parse(data);
      log.timestamp = log.timestamp || new Date().toISOString();
      log.subject = msg.subject;
      batch.push(log);
      
      if (batch.length >= BATCH_SIZE) {
        clearTimeout(timeout);
        await sendBatch();
      } else if (!timeout) {
        timeout = setTimeout(async () => {
          await sendBatch();
          timeout = null;
        }, BATCH_TIMEOUT);
      }
    } catch (error) {
      console.error('Error processing message:', error);
    }
  }
}

subscribe().catch(console.error);
```

### Go Subscriber

```go
package main

import (
    "bytes"
    "encoding/json"
    "log"
    "net/http"
    "os"
    "time"

    "github.com/nats-io/nats.go"
)

type LogEntry struct {
    Timestamp string                 `json:"timestamp"`
    Subject   string                 `json:"subject"`
    Data      map[string]interface{} `json:"data,inline"`
}

func main() {
    natsURL := os.Getenv("NATS_URL")
    if natsURL == "" {
        natsURL = "nats://localhost:4222"
    }
    
    parseableURL := os.Getenv("PARSEABLE_URL")
    parseableAuth := os.Getenv("PARSEABLE_AUTH")
    
    nc, err := nats.Connect(natsURL)
    if err != nil {
        log.Fatal(err)
    }
    defer nc.Close()
    
    log.Printf("Connected to NATS at %s", natsURL)
    
    _, err = nc.Subscribe("logs.>", func(msg *nats.Msg) {
        var data map[string]interface{}
        if err := json.Unmarshal(msg.Data, &data); err != nil {
            data = map[string]interface{}{"message": string(msg.Data)}
        }
        
        entry := LogEntry{
            Timestamp: time.Now().UTC().Format(time.RFC3339),
            Subject:   msg.Subject,
            Data:      data,
        }
        
        payload, _ := json.Marshal([]LogEntry{entry})
        
        req, _ := http.NewRequest("POST", parseableURL+"/api/v1/ingest", bytes.NewBuffer(payload))
        req.Header.Set("Authorization", "Basic "+parseableAuth)
        req.Header.Set("X-P-Stream", "nats-logs")
        req.Header.Set("Content-Type", "application/json")
        
        client := &http.Client{Timeout: 10 * time.Second}
        resp, err := client.Do(req)
        if err != nil {
            log.Printf("Error sending to Parseable: %v", err)
            return
        }
        defer resp.Body.Close()
    })
    
    if err != nil {
        log.Fatal(err)
    }
    
    log.Println("Subscribed to logs.>")
    select {}
}
```

## Method 2: JetStream Consumer

For persistent message streaming with JetStream:

```javascript
const { connect, StringCodec, AckPolicy, DeliverPolicy } = require('nats');
const axios = require('axios');

async function consumeJetStream() {
  const nc = await connect({ servers: process.env.NATS_URL });
  const js = nc.jetstream();
  const sc = StringCodec();
  
  // Create or get consumer
  const consumer = await js.consumers.get('LOGS', 'parseable-consumer');
  
  const messages = await consumer.consume();
  
  for await (const msg of messages) {
    try {
      const log = JSON.parse(sc.decode(msg.data));
      log.timestamp = log.timestamp || new Date().toISOString();
      
      await axios.post(`${process.env.PARSEABLE_URL}/api/v1/ingest`, [log], {
        headers: {
          'Authorization': `Basic ${process.env.PARSEABLE_AUTH}`,
          'X-P-Stream': 'nats-logs',
          'Content-Type': 'application/json'
        }
      });
      
      msg.ack();
    } catch (error) {
      console.error('Error:', error);
      msg.nak();
    }
  }
}

consumeJetStream().catch(console.error);
```

## Docker Compose

```yaml
version: '3.8'
services:
  nats:
    image: nats:latest
    ports:
      - "4222:4222"
      - "8222:8222"
    command: ["--jetstream"]
  
  subscriber:
    build: .
    environment:
      - NATS_URL=nats://nats:4222
      - NATS_SUBJECT=logs.>
      - PARSEABLE_URL=http://parseable:8000
      - PARSEABLE_AUTH=YWRtaW46YWRtaW4=
    depends_on:
      - nats
      - parseable
```

## Configuration Options

| Parameter        | Description                  |
| ---------------- | ---------------------------- |
| `NATS_URL`       | NATS server URL              |
| `NATS_SUBJECT`   | Subject pattern to subscribe |
| `PARSEABLE_URL`  | Parseable endpoint           |
| `PARSEABLE_AUTH` | Base64 encoded credentials   |

## Best Practices

1. **Use JetStream** - For persistent, reliable delivery
2. **Batch Messages** - Reduce HTTP overhead
3. **Handle Backpressure** - Implement flow control
4. **Monitor Consumers** - Track consumer lag
5. **Use Wildcards** - Subscribe to subject hierarchies

## Troubleshooting

### Connection Issues

1. Verify NATS server is running
2. Check network connectivity
3. Verify authentication if enabled

### Message Loss

1. Use JetStream for persistence
2. Implement acknowledgments
3. Configure appropriate retention

## Next Steps

* Configure [Kafka](/docs/ingest-data/streaming/kafka) for high-throughput
* Set up [alerts](/docs/user-guide/alerting) for streaming metrics
* Create [dashboards](/docs/user-guide/dashboards) for monitoring


# RabbitMQ (/docs/ingest-data/streaming/rabbitmq)



Stream logs from RabbitMQ message queues to Parseable.

## Overview

Integrate RabbitMQ with Parseable to:

* **Message Queue Logs** - Collect logs from RabbitMQ queues
* **Application Events** - Stream application events via RabbitMQ
* **Decoupled Architecture** - Buffer logs through message queues
* **Reliable Delivery** - Leverage RabbitMQ's delivery guarantees

## Prerequisites

* RabbitMQ server running
* Parseable instance accessible
* Consumer application or Fluent Bit

## Method 1: Fluent Bit Consumer

Use Fluent Bit to consume messages from RabbitMQ.

### Fluent Bit Configuration

```yaml
service:
  flush: 5
  log_level: info

pipeline:
  inputs:
    - name: rabbitmq
      host: rabbitmq
      port: 5672
      user: guest
      password: guest
      queue: logs
      vhost: /

  outputs:
    - name: http
      match: '*'
      host: parseable
      port: 8000
      uri: /api/v1/ingest
      format: json
      header: Authorization Basic YWRtaW46YWRtaW4=
      header: X-P-Stream rabbitmq-logs
```

## Method 2: Custom Consumer

Build a consumer application to forward messages to Parseable.

### Node.js Consumer

```javascript
const amqp = require('amqplib');
const axios = require('axios');

const RABBITMQ_URL = process.env.RABBITMQ_URL || 'amqp://localhost';
const QUEUE_NAME = process.env.QUEUE_NAME || 'logs';
const PARSEABLE_URL = process.env.PARSEABLE_URL;
const PARSEABLE_AUTH = process.env.PARSEABLE_AUTH;

async function consume() {
  const connection = await amqp.connect(RABBITMQ_URL);
  const channel = await connection.createChannel();
  
  await channel.assertQueue(QUEUE_NAME, { durable: true });
  
  const batch = [];
  const BATCH_SIZE = 100;
  const BATCH_TIMEOUT = 5000;
  
  let timeout = null;
  
  const sendBatch = async () => {
    if (batch.length === 0) return;
    
    const logs = batch.splice(0, batch.length);
    
    try {
      await axios.post(`${PARSEABLE_URL}/api/v1/ingest`, logs, {
        headers: {
          'Authorization': `Basic ${PARSEABLE_AUTH}`,
          'X-P-Stream': 'rabbitmq-logs',
          'Content-Type': 'application/json'
        }
      });
      console.log(`Sent ${logs.length} logs to Parseable`);
    } catch (error) {
      console.error('Error sending to Parseable:', error.message);
      // Re-queue failed messages
      logs.forEach(log => batch.push(log));
    }
  };
  
  channel.consume(QUEUE_NAME, async (msg) => {
    if (msg) {
      try {
        const log = JSON.parse(msg.content.toString());
        log.timestamp = log.timestamp || new Date().toISOString();
        batch.push(log);
        channel.ack(msg);
        
        if (batch.length >= BATCH_SIZE) {
          clearTimeout(timeout);
          await sendBatch();
        } else if (!timeout) {
          timeout = setTimeout(async () => {
            await sendBatch();
            timeout = null;
          }, BATCH_TIMEOUT);
        }
      } catch (error) {
        console.error('Error processing message:', error);
        channel.nack(msg, false, false);
      }
    }
  });
  
  console.log(`Consuming from queue: ${QUEUE_NAME}`);
}

consume().catch(console.error);
```

### Python Consumer

```python
import pika
import requests
import json
import os
from datetime import datetime

RABBITMQ_URL = os.getenv('RABBITMQ_URL', 'localhost')
QUEUE_NAME = os.getenv('QUEUE_NAME', 'logs')
PARSEABLE_URL = os.getenv('PARSEABLE_URL')
PARSEABLE_AUTH = os.getenv('PARSEABLE_AUTH')

def send_to_parseable(logs):
    headers = {
        'Authorization': f'Basic {PARSEABLE_AUTH}',
        'X-P-Stream': 'rabbitmq-logs',
        'Content-Type': 'application/json'
    }
    response = requests.post(
        f'{PARSEABLE_URL}/api/v1/ingest',
        json=logs,
        headers=headers
    )
    response.raise_for_status()

def callback(ch, method, properties, body):
    try:
        log = json.loads(body)
        log['timestamp'] = log.get('timestamp', datetime.utcnow().isoformat() + 'Z')
        send_to_parseable([log])
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f'Error: {e}')
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_URL))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME, durable=True)
channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)
print(f'Consuming from queue: {QUEUE_NAME}')
channel.start_consuming()
```

## Docker Compose

```yaml
version: '3.8'
services:
  rabbitmq:
    image: rabbitmq:3-management
    ports:
      - "5672:5672"
      - "15672:15672"
  
  consumer:
    build: .
    environment:
      - RABBITMQ_URL=amqp://rabbitmq
      - QUEUE_NAME=logs
      - PARSEABLE_URL=http://parseable:8000
      - PARSEABLE_AUTH=YWRtaW46YWRtaW4=
    depends_on:
      - rabbitmq
      - parseable
```

## Best Practices

1. **Use Batching** - Batch messages for efficiency
2. **Handle Failures** - Implement retry logic
3. **Monitor Queues** - Watch queue depth
4. **Use Dead Letter** - Configure DLX for failed messages
5. **Acknowledge Properly** - Ack after successful send

## Troubleshooting

### Messages Not Consumed

1. Verify RabbitMQ connection
2. Check queue exists
3. Verify consumer is running
4. Check RabbitMQ management UI

### Delivery Failures

1. Check Parseable endpoint
2. Verify authentication
3. Check network connectivity

## Next Steps

* Configure [Kafka](/docs/ingest-data/streaming/kafka) for high-throughput
* Set up [alerts](/docs/user-guide/alerting) for queue metrics
* Create [dashboards](/docs/user-guide/dashboards) for monitoring


# Redpanda (/docs/ingest-data/streaming/redpanda)



[Redpanda](https://redpanda.com/) is a Kafka compatible streaming data platform. It is a drop-in replacement for Apache Kafka.

This document explains how to set up Redpanda, along with [Redpanda Connect](https://redpanda.com/docs/redpanda-connect) to send logs to Parseable using Docker Compose as the deployment platform. We assume here that you have producer applications that are sending logs/events to Redpanda.

## Prerequisites

Please ensure [Docker Compose](https://docs.docker.com/compose/) is installed on your machine.

## Docker Compose

Then run the following commands to start the Docker Compose. It will deploy Redpanda, Redpanda Console, and Parseable (standalone).

```bash
mkdir redpanda-parseable
wget https://www.parseable.com/redpanda/docker-compose.yaml
docker-compose up -d
```

### Using the Redpanda Connect

Exec into the Redpanda instance by using the command:

```bash
docker exec -u root -it redpanda-0 /bin/bash
```

Once you are logged in, download the connect file using:

```bash
curl https://www.parseable.com/redpanda/connect.yaml > connect.yaml
```

The `connect.yaml` file contains `input` and `output` configurations. Here Kafka is the input, i.e. we listen to a Kafka topic using Redpanda connect. The output is an HTTP Connector that will send data to Parseable. Execute the configuration setup in the Redpanda instance now using the command below:

```bash
rpk connect run connect.yaml
```

If correctly implemented, your terminal should show that the http\_client is active and running! Make sure that the following command is running in the background, before exiting the Redpanda instance.

### Send data to Redpanda topic

This step helps you test if everything is working as expected. In a production scenario, you'll have a log agent sending logs to the Redpanda topic.

Run the following commands to start a bash shell in the Redpanda container and post some sample data.

```bash
docker exec -it redpanda-0 /bin/bash
rpk topic produce redpandatest
```

The rpk command will open up a console, ready to accept events. Then paste the below data in the terminal.

```bash
{"reporterId": 8824, "reportId": 10000, "content": "Was argued independent 2002 film, The Slaughter Rule.", "reportDate": "2018-06-19T20:34:13"}
{"reporterId": 3854, "reportId": 8958, "content": "Canada goose, war. Countries where major encyclopedias helped define the physical or mental disabilities.", "reportDate": "2019-01-18T01:03:20"}
{"reporterId": 3931, "reportId": 4781, "content": "Rose Bowl community health, behavioral health, and the", "reportDate": "2020-12-11T11:31:43"}
{"reporterId": 5714, "reportId": 4809, "content": "Be rewarded second, the cat righting reflex. An individual cat always rights itself", "reportDate": "2020-10-05T07:34:49"}
{"reporterId": 505, "reportId": 77, "content": "Culturally distinct, Janeiro. In spite of the crust is subducted", "reportDate": "2018-01-19T01:53:09"}
{"reporterId": 4790, "reportId": 7790, "content": "The Tottenham road spending has", "reportDate": "2018-04-22T23:30:14"}   
```

You can now check the Parseable dashboard at `http://localhost:8000`, you should see this data in the dashboard.


# Discord (/docs/integrations/alerting/discord)



Send Parseable alerts to Discord channels for team notifications and incident awareness.

## Overview

Integrate Parseable with Discord to:

* **Server Notifications** - Alert your team in dedicated channels
* **Rich Embeds** - Send formatted messages with alert details
* **Bot Integration** - Use Discord bots for advanced features
* **Mobile Alerts** - Receive notifications on any device

## Prerequisites

* Discord server with admin access
* Discord Webhook URL
* Parseable instance with alerting configured

## Setting Up Discord Webhook

### Create a Webhook

1. Open Discord and go to your server
2. Navigate to the channel for alerts
3. Click **Edit Channel** (gear icon)
4. Go to **Integrations** → **Webhooks**
5. Click **New Webhook**
6. Name your webhook (e.g., "Parseable Alerts")
7. Copy the **Webhook URL**

## Webhook Integration

Create a webhook service to transform Parseable alerts to Discord format:

```javascript
// webhook-to-discord.js
const express = require('express');
const axios = require('axios');

const app = express();
app.use(express.json());

const DISCORD_WEBHOOK_URL = process.env.DISCORD_WEBHOOK_URL;

app.post('/webhook', async (req, res) => {
  const alert = req.body;
  
  const discordMessage = {
    username: "Parseable Alerts",
    avatar_url: "https://parseable.com/logo.png",
    embeds: [{
      title: `🚨 ${alert.name || 'Alert Triggered'}`,
      description: alert.message || `Alert triggered on dataset ${alert.dataset}`,
      color: getColor(alert.severity),
      fields: [
        {
          name: "Stream",
          value: alert.dataset || 'N/A',
          inline: true
        },
        {
          name: "Severity",
          value: alert.severity || 'Unknown',
          inline: true
        },
        {
          name: "Current Value",
          value: String(alert.value || 'N/A'),
          inline: true
        },
        {
          name: "Threshold",
          value: String(alert.threshold || 'N/A'),
          inline: true
        }
      ],
      timestamp: new Date().toISOString(),
      footer: {
        text: "Parseable Alert System"
      }
    }]
  };

  try {
    await axios.post(DISCORD_WEBHOOK_URL, discordMessage);
    res.status(200).json({ status: 'sent' });
  } catch (error) {
    console.error('Error sending to Discord:', error);
    res.status(500).json({ error: 'Failed to send to Discord' });
  }
});

function getColor(severity) {
  const colors = {
    'critical': 0xFF0000,  // Red
    'high': 0xFFA500,      // Orange
    'medium': 0xFFFF00,    // Yellow
    'low': 0x00FF00,       // Green
    'info': 0x0000FF       // Blue
  };
  return colors[severity?.toLowerCase()] || 0xFFA500;
}

app.listen(3000);
```

### With Mentions

Add role or user mentions for critical alerts:

```javascript
const discordMessage = {
  content: alert.severity === 'critical' ? '<@&ROLE_ID> Critical Alert!' : '',
  embeds: [{
    // ... embed content
  }]
};
```

## Docker Compose

```yaml
version: '3.8'
services:
  webhook-to-discord:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...
```

## Configuration Options

### Embed Colors

| Severity | Color  | Hex      |
| -------- | ------ | -------- |
| critical | Red    | 0xFF0000 |
| high     | Orange | 0xFFA500 |
| medium   | Yellow | 0xFFFF00 |
| low      | Green  | 0x00FF00 |
| info     | Blue   | 0x0000FF |

## Best Practices

1. **Use Dedicated Channels** - Create separate channels for alerts
2. **Role Mentions** - Mention roles for critical alerts only
3. **Rich Embeds** - Use embeds for better formatting
4. **Rate Limiting** - Discord has rate limits, batch messages if needed

## Next Steps

* Set up [Parseable alerts](/docs/user-guide/alerting) for automated notifications
* Configure [Slack](/docs/integrations/alerting/slack) as an alternative
* Create [dashboards](/docs/user-guide/dashboards) for monitoring


# Email (/docs/integrations/alerting/email)



Send Parseable alerts via email for universal notification delivery.

## Overview

Integrate Parseable with email to:

* **Universal Delivery** - Reach anyone with an email address
* **Detailed Reports** - Send formatted HTML alert emails
* **Audit Trail** - Maintain email records for compliance
* **Escalation** - Use email as a fallback notification method

## Prerequisites

* SMTP server access (or email service API)
* Email credentials configured
* Parseable instance with alerting configured

## Webhook Integration

Create a webhook service to send email notifications:

### Using Nodemailer (SMTP)

```javascript
// webhook-to-email.js
const express = require('express');
const nodemailer = require('nodemailer');

const app = express();
app.use(express.json());

const transporter = nodemailer.createTransport({
  host: process.env.SMTP_HOST,
  port: process.env.SMTP_PORT || 587,
  secure: process.env.SMTP_SECURE === 'true',
  auth: {
    user: process.env.SMTP_USER,
    pass: process.env.SMTP_PASS
  }
});

app.post('/webhook', async (req, res) => {
  const alert = req.body;
  
  const mailOptions = {
    from: process.env.EMAIL_FROM || 'alerts@parseable.com',
    to: process.env.EMAIL_TO,
    subject: `[${alert.severity?.toUpperCase() || 'ALERT'}] ${alert.name || 'Parseable Alert'}`,
    html: generateEmailHtml(alert),
    text: generateEmailText(alert)
  };

  try {
    await transporter.sendMail(mailOptions);
    res.status(200).json({ status: 'sent' });
  } catch (error) {
    console.error('Error sending email:', error);
    res.status(500).json({ error: 'Failed to send email' });
  }
});

function generateEmailHtml(alert) {
  const severityColor = {
    'critical': '#FF0000',
    'high': '#FFA500',
    'medium': '#FFFF00',
    'low': '#00FF00',
    'info': '#0000FF'
  }[alert.severity?.toLowerCase()] || '#FFA500';

  return `
    <!DOCTYPE html>
    <html>
    <head>
      <style>
        body { font-family: Arial, sans-serif; }
        .header { background: ${severityColor}; color: white; padding: 20px; }
        .content { padding: 20px; }
        .field { margin: 10px 0; }
        .label { font-weight: bold; }
        .footer { background: #f5f5f5; padding: 10px; font-size: 12px; }
      </style>
    </head>
    <body>
      <div class="header">
        <h1>🚨 ${alert.name || 'Alert Triggered'}</h1>
      </div>
      <div class="content">
        <div class="field">
          <span class="label">Stream:</span> ${alert.dataset || 'N/A'}
        </div>
        <div class="field">
          <span class="label">Severity:</span> ${alert.severity || 'Unknown'}
        </div>
        <div class="field">
          <span class="label">Current Value:</span> ${alert.value || 'N/A'}
        </div>
        <div class="field">
          <span class="label">Threshold:</span> ${alert.threshold || 'N/A'}
        </div>
        <div class="field">
          <span class="label">Message:</span> ${alert.message || 'No message'}
        </div>
        <div class="field">
          <span class="label">Time:</span> ${new Date().toISOString()}
        </div>
        <p>
          <a href="https://your-parseable.com/streams/${alert.dataset}">View in Parseable</a>
        </p>
      </div>
      <div class="footer">
        This alert was sent by Parseable Alert System
      </div>
    </body>
    </html>
  `;
}

function generateEmailText(alert) {
  return `
Parseable Alert: ${alert.name || 'Alert Triggered'}

Stream: ${alert.dataset || 'N/A'}
Severity: ${alert.severity || 'Unknown'}
Current Value: ${alert.value || 'N/A'}
Threshold: ${alert.threshold || 'N/A'}
Message: ${alert.message || 'No message'}
Time: ${new Date().toISOString()}

View in Parseable: https://your-parseable.com/streams/${alert.dataset}
  `;
}

app.listen(3000);
```

### Using SendGrid

```javascript
const sgMail = require('@sendgrid/mail');
sgMail.setApiKey(process.env.SENDGRID_API_KEY);

app.post('/webhook', async (req, res) => {
  const alert = req.body;
  
  const msg = {
    to: process.env.EMAIL_TO,
    from: process.env.EMAIL_FROM,
    subject: `[${alert.severity?.toUpperCase()}] ${alert.name}`,
    html: generateEmailHtml(alert),
    text: generateEmailText(alert)
  };

  try {
    await sgMail.send(msg);
    res.status(200).json({ status: 'sent' });
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ error: 'Failed to send' });
  }
});
```

## Docker Compose

```yaml
version: '3.8'
services:
  webhook-to-email:
    build: .
    ports:
      - "3000:3000"
    environment:
      - SMTP_HOST=smtp.gmail.com
      - SMTP_PORT=587
      - SMTP_USER=your-email@gmail.com
      - SMTP_PASS=your-app-password
      - EMAIL_FROM=alerts@yourdomain.com
      - EMAIL_TO=team@yourdomain.com
```

## Configuration Options

| Variable     | Description                          |
| ------------ | ------------------------------------ |
| `SMTP_HOST`  | SMTP server hostname                 |
| `SMTP_PORT`  | SMTP port (587 for TLS, 465 for SSL) |
| `SMTP_USER`  | SMTP username                        |
| `SMTP_PASS`  | SMTP password                        |
| `EMAIL_FROM` | Sender email address                 |
| `EMAIL_TO`   | Recipient email address(es)          |

## Best Practices

1. **Use HTML and Text** - Include both formats for compatibility
2. **Clear Subject Lines** - Include severity and alert name
3. **Include Links** - Add direct links to Parseable
4. **Rate Limiting** - Avoid sending too many emails
5. **Distribution Lists** - Use mailing lists for team alerts

## Next Steps

* Set up [Parseable alerts](/docs/user-guide/alerting) for automated notifications
* Configure [Slack](/docs/integrations/alerting/slack) for instant notifications
* Create [dashboards](/docs/user-guide/dashboards) for monitoring


# Microsoft Teams (/docs/integrations/alerting/microsoft-teams)



Send Parseable alerts to Microsoft Teams channels for team collaboration and incident awareness.

## Overview

Integrate Parseable with Microsoft Teams to:

* **Team Notifications** - Alert your team in dedicated channels
* **Rich Messages** - Send formatted cards with alert details
* **Collaboration** - Discuss and resolve issues in context
* **Mobile Alerts** - Receive notifications on mobile devices

## Prerequisites

* Microsoft Teams workspace
* Incoming Webhook connector configured
* Parseable instance with alerting configured

## Setting Up Teams Webhook

### Create an Incoming Webhook

1. Open Microsoft Teams
2. Navigate to the channel for alerts
3. Click **...** → **Connectors**
4. Find **Incoming Webhook** and click **Configure**
5. Name your webhook (e.g., "Parseable Alerts")
6. Optionally upload an icon
7. Click **Create**
8. Copy the webhook URL

## Webhook Integration

Create a webhook service to transform Parseable alerts to Teams format:

```javascript
// webhook-to-teams.js
const express = require('express');
const axios = require('axios');

const app = express();
app.use(express.json());

const TEAMS_WEBHOOK_URL = process.env.TEAMS_WEBHOOK_URL;

app.post('/webhook', async (req, res) => {
  const alert = req.body;
  
  const teamsMessage = {
    "@type": "MessageCard",
    "@context": "http://schema.org/extensions",
    "themeColor": getThemeColor(alert.severity),
    "summary": `Parseable Alert: ${alert.name}`,
    "sections": [{
      "activityTitle": `🚨 ${alert.name || 'Alert Triggered'}`,
      "activitySubtitle": `Stream: ${alert.dataset}`,
      "activityImage": "https://parseable.com/logo.png",
      "facts": [
        { "name": "Severity", "value": alert.severity || 'Unknown' },
        { "name": "Stream", "value": alert.dataset || 'N/A' },
        { "name": "Current Value", "value": String(alert.value || 'N/A') },
        { "name": "Threshold", "value": String(alert.threshold || 'N/A') },
        { "name": "Time", "value": new Date().toISOString() }
      ],
      "markdown": true
    }],
    "potentialAction": [{
      "@type": "OpenUri",
      "name": "View in Parseable",
      "targets": [{
        "os": "default",
        "uri": `https://your-parseable.com/streams/${alert.dataset}`
      }]
    }]
  };

  try {
    await axios.post(TEAMS_WEBHOOK_URL, teamsMessage);
    res.status(200).json({ status: 'sent' });
  } catch (error) {
    console.error('Error sending to Teams:', error);
    res.status(500).json({ error: 'Failed to send to Teams' });
  }
});

function getThemeColor(severity) {
  const colors = {
    'critical': 'FF0000',
    'high': 'FFA500',
    'medium': 'FFFF00',
    'low': '00FF00',
    'info': '0000FF'
  };
  return colors[severity?.toLowerCase()] || 'FFA500';
}

app.listen(3000);
```

### Adaptive Cards (Modern Format)

For richer formatting, use Adaptive Cards:

```javascript
const adaptiveCard = {
  "type": "message",
  "attachments": [{
    "contentType": "application/vnd.microsoft.card.adaptive",
    "content": {
      "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
      "type": "AdaptiveCard",
      "version": "1.4",
      "body": [
        {
          "type": "TextBlock",
          "size": "Large",
          "weight": "Bolder",
          "text": `🚨 ${alert.name}`,
          "color": alert.severity === 'critical' ? 'Attention' : 'Warning'
        },
        {
          "type": "FactSet",
          "facts": [
            { "title": "Stream", "value": alert.dataset },
            { "title": "Severity", "value": alert.severity },
            { "title": "Value", "value": String(alert.value) }
          ]
        }
      ],
      "actions": [{
        "type": "Action.OpenUrl",
        "title": "View in Parseable",
        "url": `https://your-parseable.com/streams/${alert.dataset}`
      }]
    }
  }]
};
```

## Docker Compose

```yaml
version: '3.8'
services:
  webhook-to-teams:
    build: .
    ports:
      - "3000:3000"
    environment:
      - TEAMS_WEBHOOK_URL=https://outlook.office.com/webhook/...
```

## Best Practices

1. **Use Dedicated Channels** - Create separate channels for different alert severities
2. **Include Action Links** - Add buttons to view alerts in Parseable
3. **Format Messages** - Use cards for better readability
4. **Rate Limiting** - Implement rate limiting to avoid flooding channels

## Next Steps

* Set up [Parseable alerts](/docs/user-guide/alerting) for automated notifications
* Configure [Slack](/docs/integrations/alerting/slack) as an alternative
* Create [dashboards](/docs/user-guide/dashboards) for monitoring


# Opsgenie (/docs/integrations/alerting/opsgenie)



Integrate Parseable with Opsgenie for alert management, on-call scheduling, and incident response.

## Overview

Integrate Parseable with Opsgenie to:

* **Alert Management** - Create and manage alerts from Parseable
* **On-Call Scheduling** - Route alerts to the right team members
* **Incident Response** - Track and resolve issues efficiently
* **Escalation Policies** - Automatic escalation for unacknowledged alerts

## Prerequisites

* Opsgenie account with API access
* Opsgenie API Integration key
* Parseable instance with alerting configured

## Setting Up Opsgenie Integration

### Create an API Integration

1. Log in to your Opsgenie account
2. Go to **Settings** → **Integration List**
3. Search for **API** and click **Add**
4. Name your integration (e.g., "Parseable Alerts")
5. Copy the **API Key**
6. Configure teams and responders as needed
7. Click **Save Integration**

## Webhook Integration

Create a webhook service to transform Parseable alerts to Opsgenie format:

```javascript
// webhook-to-opsgenie.js
const express = require('express');
const axios = require('axios');

const app = express();
app.use(express.json());

const OPSGENIE_API_KEY = process.env.OPSGENIE_API_KEY;
const OPSGENIE_API_URL = 'https://api.opsgenie.com/v2/alerts';

app.post('/webhook', async (req, res) => {
  const alert = req.body;
  
  const opsgenieAlert = {
    message: `[Parseable] ${alert.name || 'Alert Triggered'}`,
    alias: `parseable-${alert.name}-${alert.dataset}`,
    description: alert.message || `Alert triggered on dataset ${alert.dataset}`,
    priority: mapPriority(alert.severity),
    source: 'Parseable',
    tags: ['parseable', alert.dataset],
    details: {
      dataset: alert.dataset,
      query: alert.query,
      threshold: alert.threshold,
      current_value: alert.value
    },
    entity: alert.dataset,
    actions: ['Acknowledge', 'View in Parseable']
  };

  try {
    await axios.post(OPSGENIE_API_URL, opsgenieAlert, {
      headers: {
        'Authorization': `GenieKey ${OPSGENIE_API_KEY}`,
        'Content-Type': 'application/json'
      }
    });
    res.status(200).json({ status: 'sent' });
  } catch (error) {
    console.error('Error sending to Opsgenie:', error.response?.data || error);
    res.status(500).json({ error: 'Failed to send to Opsgenie' });
  }
});

function mapPriority(severity) {
  const mapping = {
    'critical': 'P1',
    'high': 'P2',
    'medium': 'P3',
    'low': 'P4',
    'info': 'P5'
  };
  return mapping[severity?.toLowerCase()] || 'P3';
}

app.listen(3000);
```

### Docker Compose

```yaml
version: '3.8'
services:
  webhook-to-opsgenie:
    build: .
    ports:
      - "3000:3000"
    environment:
      - OPSGENIE_API_KEY=your-api-key
```

## Configuration Options

### Priority Mapping

| Parseable Severity | Opsgenie Priority |
| ------------------ | ----------------- |
| critical           | P1                |
| high               | P2                |
| medium             | P3                |
| low                | P4                |
| info               | P5                |

## Best Practices

1. **Use Aliases** - Prevent duplicate alerts with consistent aliases
2. **Add Tags** - Include dataset and severity tags for filtering
3. **Set Priorities** - Map severity levels appropriately
4. **Include Details** - Add context like query and threshold values

## Next Steps

* Set up [Parseable alerts](/docs/user-guide/alerting) for automated notifications
* Configure [PagerDuty](/docs/integrations/alerting/pagerduty) as an alternative
* Create [dashboards](/docs/user-guide/dashboards) for monitoring


# PagerDuty (/docs/integrations/alerting/pagerduty)



Integrate Parseable with PagerDuty for incident management, on-call scheduling, and alert escalation.

## Overview

Integrate Parseable with PagerDuty to:

* **Trigger Incidents** - Automatically create PagerDuty incidents from alerts
* **On-Call Escalation** - Route alerts to the right team members
* **Incident Management** - Track and resolve issues with full context
* **Reduce Alert Fatigue** - Use PagerDuty's intelligent grouping

## Prerequisites

* PagerDuty account with admin access
* PagerDuty Integration Key (Events API v2)
* Parseable alerts configured or Fluent Bit for log streaming

## Setting Up PagerDuty Integration

### Create a PagerDuty Service

1. Log in to your PagerDuty account
2. Go to **Services** → **Service Directory**
3. Click **+ New Service**
4. Name your service (e.g., "Parseable Alerts")
5. Select an escalation policy
6. Under **Integrations**, select **Events API V2**
7. Click **Create Service**
8. Copy the **Integration Key** (32-character string)

## Webhook Integration

Use Parseable's alerting system with a webhook to send incidents to PagerDuty.

### Create a Webhook Endpoint

Create a webhook service that transforms Parseable alerts to PagerDuty Events API format:

```javascript
// webhook-to-pagerduty.js
const express = require('express');
const axios = require('axios');

const app = express();
app.use(express.json());

const PAGERDUTY_ROUTING_KEY = process.env.PAGERDUTY_ROUTING_KEY;
const PAGERDUTY_EVENTS_URL = 'https://events.pagerduty.com/v2/enqueue';

app.post('/webhook', async (req, res) => {
  const alert = req.body;
  
  const pagerdutyEvent = {
    routing_key: PAGERDUTY_ROUTING_KEY,
    event_action: 'trigger',
    dedup_key: `parseable-${alert.name}-${alert.dataset}`,
    payload: {
      summary: `[Parseable] ${alert.name || 'Alert Triggered'}`,
      severity: mapSeverity(alert.severity),
      source: alert.dataset || 'parseable',
      timestamp: new Date().toISOString(),
      custom_details: {
        dataset: alert.dataset,
        query: alert.query,
        threshold: alert.threshold,
        current_value: alert.value,
        message: alert.message
      }
    },
    links: [
      {
        href: `https://your-parseable-instance.com/streams/${alert.dataset}`,
        text: 'View in Parseable'
      }
    ]
  };

  try {
    const response = await axios.post(PAGERDUTY_EVENTS_URL, pagerdutyEvent);
    res.status(200).json({ 
      status: 'sent',
      dedup_key: response.data.dedup_key 
    });
  } catch (error) {
    console.error('Error sending to PagerDuty:', error.response?.data || error);
    res.status(500).json({ error: 'Failed to send to PagerDuty' });
  }
});

// Map Parseable severity to PagerDuty severity
function mapSeverity(severity) {
  const mapping = {
    'critical': 'critical',
    'high': 'error',
    'medium': 'warning',
    'low': 'info',
    'error': 'error',
    'warning': 'warning',
    'info': 'info'
  };
  return mapping[severity?.toLowerCase()] || 'error';
}

// Endpoint to resolve incidents
app.post('/webhook/resolve', async (req, res) => {
  const alert = req.body;
  
  const pagerdutyEvent = {
    routing_key: PAGERDUTY_ROUTING_KEY,
    event_action: 'resolve',
    dedup_key: `parseable-${alert.name}-${alert.dataset}`
  };

  try {
    await axios.post(PAGERDUTY_EVENTS_URL, pagerdutyEvent);
    res.status(200).json({ status: 'resolved' });
  } catch (error) {
    console.error('Error resolving in PagerDuty:', error);
    res.status(500).json({ error: 'Failed to resolve in PagerDuty' });
  }
});

app.listen(3000, () => {
  console.log('PagerDuty webhook server listening on port 3000');
});
```

### Docker Compose Setup

```yaml
version: '3.8'
services:
  webhook-to-pagerduty:
    build: .
    ports:
      - "3000:3000"
    environment:
      - PAGERDUTY_ROUTING_KEY=your-32-character-integration-key
```

### Configure Parseable Alert

Configure your Parseable alert to send to the webhook endpoint:

```json
{
  "name": "Critical Error Rate",
  "dataset": "production-logs",
  "alertType": "threshold",
  "condition": {
    "field": "level",
    "operator": "equals",
    "value": "critical"
  },
  "threshold": 10,
  "duration": "5m",
  "webhook": {
    "url": "http://webhook-to-pagerduty:3000/webhook",
    "method": "POST"
  }
}
```

## PagerDuty Events API v2

### Event Actions

| Action        | Description                              |
| ------------- | ---------------------------------------- |
| `trigger`     | Create a new incident or add to existing |
| `acknowledge` | Acknowledge an existing incident         |
| `resolve`     | Resolve an existing incident             |

### Severity Levels

| Severity   | Description                              |
| ---------- | ---------------------------------------- |
| `critical` | System is unusable                       |
| `error`    | A problem that needs immediate attention |
| `warning`  | A problem that should be addressed soon  |
| `info`     | Informational message                    |

### Deduplication

Use the `dedup_key` to group related alerts into a single incident:

```javascript
dedup_key: `parseable-${alert.name}-${alert.dataset}`
```

This prevents alert storms from creating multiple incidents for the same issue.

## Advanced Configuration

### Custom Fields

Add custom details to provide more context:

```javascript
custom_details: {
  dataset: alert.dataset,
  query: alert.query,
  threshold: alert.threshold,
  current_value: alert.value,
  environment: process.env.ENVIRONMENT,
  region: process.env.REGION,
  runbook_url: 'https://wiki.example.com/runbooks/high-error-rate'
}
```

### Priority Mapping

Map Parseable alert priorities to PagerDuty priorities:

```javascript
const priorityMapping = {
  'P1': { severity: 'critical', urgency: 'high' },
  'P2': { severity: 'error', urgency: 'high' },
  'P3': { severity: 'warning', urgency: 'low' },
  'P4': { severity: 'info', urgency: 'low' }
};
```

## Best Practices

1. **Use Deduplication** - Prevent duplicate incidents with consistent dedup keys
2. **Include Runbook Links** - Add links to troubleshooting documentation
3. **Set Appropriate Severity** - Map alert severity correctly to avoid alert fatigue
4. **Add Context** - Include relevant details like dataset, query, and thresholds
5. **Test Integration** - Verify the integration works before production deployment

## Troubleshooting

### Incidents Not Creating

1. Verify the Integration Key is correct
2. Check the webhook service logs for errors
3. Ensure the PagerDuty service is not disabled
4. Verify network connectivity to PagerDuty

### Duplicate Incidents

1. Ensure `dedup_key` is consistent for related alerts
2. Check that the dedup key format matches across trigger/resolve events

### Missing Context

1. Verify `custom_details` are being populated
2. Check that the alert payload contains expected fields

## Next Steps

* Set up [Parseable alerts](/docs/user-guide/alerting) for automated incident creation
* Configure [Slack](/docs/integrations/alerting/slack) for team notifications
* Create [dashboards](/docs/user-guide/dashboards) for visual monitoring


# Slack (/docs/integrations/alerting/slack)



Send alerts and important log events to Slack channels using Fluent Bit or custom webhooks.

## Overview

Integrate Parseable with Slack to:

* **Receive Alert Notifications** - Get notified when alerts trigger
* **Stream Critical Logs** - Send error logs directly to Slack channels
* **Team Collaboration** - Share observability insights with your team

## Prerequisites

* Slack workspace with admin access
* Slack Incoming Webhook URL
* Fluent Bit (for log streaming) or Parseable alerts configured

## Setting Up Slack Webhook

### Create an Incoming Webhook

1. Go to [Slack API Apps](https://api.slack.com/apps)
2. Click **Create New App** → **From scratch**
3. Name your app (e.g., "Parseable Alerts") and select your workspace
4. Go to **Incoming Webhooks** in the sidebar
5. Toggle **Activate Incoming Webhooks** to On
6. Click **Add New Webhook to Workspace**
7. Select the channel for notifications
8. Copy the Webhook URL (format: `https://hooks.slack.com/services/T.../B.../xxx`)

## Method 1: Fluent Bit Log Streaming

Stream logs from Parseable to Slack using Fluent Bit as an intermediary.

### Architecture

```
Parseable → Fluent Bit → Slack
```

### Fluent Bit Configuration

Create a `fluent-bit.yaml` configuration:

```yaml
service:
  flush: 5
  log_level: info

pipeline:
  inputs:
    - name: http
      listen: 0.0.0.0
      port: 8888
      tag: parseable

  filters:
    # Filter for error logs only
    - name: grep
      match: parseable
      regex: level error|ERROR|critical|CRITICAL

  outputs:
    - name: slack
      match: parseable
      webhook: https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX
```

### Classic Config Format

```ini
[SERVICE]
    Flush        5
    Log_Level    info

[INPUT]
    Name         http
    Listen       0.0.0.0
    Port         8888
    Tag          parseable

[FILTER]
    Name         grep
    Match        parseable
    Regex        level error|ERROR|critical|CRITICAL

[OUTPUT]
    Name         slack
    Match        parseable
    Webhook      https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX
```

### Running Fluent Bit

```bash
docker run -d \
  --name fluent-bit-slack \
  -p 8888:8888 \
  -v $(pwd)/fluent-bit.yaml:/fluent-bit/etc/fluent-bit.yaml \
  fluent/fluent-bit:latest \
  /fluent-bit/bin/fluent-bit -c /fluent-bit/etc/fluent-bit.yaml
```

## Method 2: Webhook Integration

Use Parseable's alerting system with a custom webhook to send notifications to Slack.

### Create a Webhook Endpoint

Create a simple webhook service that transforms Parseable alerts to Slack format:

```javascript
// webhook-to-slack.js (Node.js example)
const express = require('express');
const axios = require('axios');

const app = express();
app.use(express.json());

const SLACK_WEBHOOK = process.env.SLACK_WEBHOOK_URL;

app.post('/webhook', async (req, res) => {
  const alert = req.body;
  
  const slackMessage = {
    blocks: [
      {
        type: "header",
        text: {
          type: "plain_text",
          text: `🚨 Alert: ${alert.name || 'Parseable Alert'}`,
          emoji: true
        }
      },
      {
        type: "section",
        fields: [
          {
            type: "mrkdwn",
            text: `*Severity:*\n${alert.severity || 'Unknown'}`
          },
          {
            type: "mrkdwn",
            text: `*Stream:*\n${alert.dataset || 'N/A'}`
          }
        ]
      },
      {
        type: "section",
        text: {
          type: "mrkdwn",
          text: `*Message:*\n${alert.message || JSON.stringify(alert)}`
        }
      },
      {
        type: "context",
        elements: [
          {
            type: "mrkdwn",
            text: `Triggered at: ${new Date().toISOString()}`
          }
        ]
      }
    ]
  };

  try {
    await axios.post(SLACK_WEBHOOK, slackMessage);
    res.status(200).json({ status: 'sent' });
  } catch (error) {
    console.error('Error sending to Slack:', error);
    res.status(500).json({ error: 'Failed to send to Slack' });
  }
});

app.listen(3000, () => {
  console.log('Webhook server listening on port 3000');
});
```

### Docker Compose Setup

```yaml
version: '3.8'
services:
  webhook-to-slack:
    build: .
    ports:
      - "3000:3000"
    environment:
      - SLACK_WEBHOOK_URL=https://hooks.slack.com/services/T.../B.../xxx
```

### Configure Parseable Alert

Configure your Parseable alert to send to the webhook endpoint:

```json
{
  "name": "High Error Rate",
  "dataset": "application-logs",
  "alertType": "threshold",
  "condition": {
    "field": "level",
    "operator": "equals",
    "value": "error"
  },
  "threshold": 100,
  "duration": "5m",
  "webhook": {
    "url": "http://webhook-to-slack:3000/webhook",
    "method": "POST"
  }
}
```

## Configuration Options

### Fluent Bit Slack Output

| Parameter | Default | Description                  |
| --------- | ------- | ---------------------------- |
| `webhook` | -       | Slack webhook URL (required) |
| `workers` | `0`     | Number of worker threads     |
| `match`   | -       | Tag pattern to match         |

## Message Formatting

### Custom Message Template

You can customize the Slack message format by using Fluent Bit's record modifier:

```yaml
pipeline:
  filters:
    - name: record_modifier
      match: parseable
      record: slack_message "🔴 Error in ${dataset}: ${message}"

  outputs:
    - name: slack
      match: parseable
      webhook: ${SLACK_WEBHOOK_URL}
```

## Best Practices

1. **Filter Critical Logs** - Only send important events to avoid notification fatigue
2. **Use Channels Wisely** - Create dedicated channels for different alert severities
3. **Include Context** - Add relevant metadata like dataset name, timestamp, and severity
4. **Rate Limiting** - Implement rate limiting to prevent Slack API throttling
5. **Test Webhooks** - Verify webhook connectivity before production deployment

## Troubleshooting

### Messages Not Appearing

1. Verify the webhook URL is correct
2. Check Fluent Bit logs for errors
3. Ensure the Slack app has permission to post to the channel
4. Verify network connectivity to Slack

### Rate Limiting

If you're hitting Slack's rate limits:

1. Increase the flush interval in Fluent Bit
2. Aggregate similar events before sending
3. Filter to reduce message volume

## Next Steps

* Set up [Parseable alerts](/docs/user-guide/alerting) for automated notifications
* Configure [PagerDuty](/docs/integrations/alerting/pagerduty) for on-call escalation
* Create [dashboards](/docs/user-guide/dashboards) for visual monitoring


# Webhook (/docs/integrations/alerting/webhook)



Send Parseable alerts to any HTTP endpoint using generic webhooks for custom integrations.

## Overview

Webhooks provide a flexible way to integrate Parseable with any system that accepts HTTP requests:

* **Custom Applications** - Send alerts to your internal tools
* **Third-Party Services** - Integrate with any service that has an API
* **Automation Workflows** - Trigger automated responses to alerts
* **Data Pipelines** - Forward alerts to data processing systems

## Prerequisites

* HTTP endpoint that accepts POST requests
* Parseable alerts configured
* Network connectivity between Parseable and the webhook endpoint

## Basic Webhook Configuration

### Parseable Alert with Webhook

Configure an alert in Parseable with a webhook target:

```json
{
  "name": "High Error Rate Alert",
  "dataset": "application-logs",
  "alertType": "threshold",
  "condition": {
    "field": "level",
    "operator": "equals",
    "value": "error"
  },
  "threshold": 100,
  "duration": "5m",
  "webhook": {
    "url": "https://your-endpoint.com/webhook",
    "method": "POST",
    "headers": {
      "Content-Type": "application/json",
      "Authorization": "Bearer your-api-token"
    }
  }
}
```

## Webhook Payload

When an alert triggers, Parseable sends a JSON payload to your webhook endpoint:

```json
{
  "alert_name": "High Error Rate Alert",
  "dataset": "application-logs",
  "alert_type": "threshold",
  "severity": "high",
  "triggered_at": "2024-01-15T10:30:00Z",
  "condition": {
    "field": "level",
    "operator": "equals",
    "value": "error"
  },
  "threshold": 100,
  "current_value": 150,
  "duration": "5m",
  "message": "Error count exceeded threshold: 150 > 100"
}
```

## Building a Webhook Receiver

### Node.js Example

```javascript
const express = require('express');
const app = express();

app.use(express.json());

app.post('/webhook', (req, res) => {
  const alert = req.body;
  
  console.log('Received alert:', alert);
  
  // Process the alert
  handleAlert(alert);
  
  res.status(200).json({ status: 'received' });
});

function handleAlert(alert) {
  // Your custom logic here
  // Examples:
  // - Send to a messaging queue
  // - Update a database
  // - Trigger an automation
  // - Forward to another service
  
  console.log(`Alert: ${alert.alert_name}`);
  console.log(`Stream: ${alert.dataset}`);
  console.log(`Value: ${alert.current_value} (threshold: ${alert.threshold})`);
}

app.listen(3000, () => {
  console.log('Webhook receiver listening on port 3000');
});
```

### Python Example

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/webhook', methods=['POST'])
def webhook():
    alert = request.json
    
    logging.info(f"Received alert: {alert}")
    
    # Process the alert
    handle_alert(alert)
    
    return jsonify({'status': 'received'}), 200

def handle_alert(alert):
    # Your custom logic here
    logging.info(f"Alert: {alert.get('alert_name')}")
    logging.info(f"Stream: {alert.get('dataset')}")
    logging.info(f"Value: {alert.get('current_value')} (threshold: {alert.get('threshold')})")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
```

### Go Example

```go
package main

import (
    "encoding/json"
    "fmt"
    "log"
    "net/http"
)

type Alert struct {
    AlertName    string `json:"alert_name"`
    Stream       string `json:"dataset"`
    AlertType    string `json:"alert_type"`
    Severity     string `json:"severity"`
    TriggeredAt  string `json:"triggered_at"`
    Threshold    int    `json:"threshold"`
    CurrentValue int    `json:"current_value"`
    Message      string `json:"message"`
}

func webhookHandler(w http.ResponseWriter, r *http.Request) {
    var alert Alert
    
    if err := json.NewDecoder(r.Body).Decode(&alert); err != nil {
        http.Error(w, err.Error(), http.StatusBadRequest)
        return
    }
    
    log.Printf("Received alert: %s", alert.AlertName)
    log.Printf("Stream: %s, Value: %d (threshold: %d)", 
        alert.Stream, alert.CurrentValue, alert.Threshold)
    
    // Process the alert
    handleAlert(alert)
    
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(map[string]string{"status": "received"})
}

func handleAlert(alert Alert) {
    // Your custom logic here
    fmt.Printf("Processing alert: %s\n", alert.AlertName)
}

func main() {
    http.HandleFunc("/webhook", webhookHandler)
    log.Println("Webhook receiver listening on port 3000")
    log.Fatal(http.ListenAndServe(":3000", nil))
}
```

## Authentication

### Bearer Token

```json
{
  "webhook": {
    "url": "https://your-endpoint.com/webhook",
    "headers": {
      "Authorization": "Bearer your-api-token"
    }
  }
}
```

### Basic Auth

```json
{
  "webhook": {
    "url": "https://your-endpoint.com/webhook",
    "headers": {
      "Authorization": "Basic base64-encoded-credentials"
    }
  }
}
```

### API Key

```json
{
  "webhook": {
    "url": "https://your-endpoint.com/webhook",
    "headers": {
      "X-API-Key": "your-api-key"
    }
  }
}
```

## Common Integrations

### Forward to Microsoft Teams

```javascript
app.post('/webhook', async (req, res) => {
  const alert = req.body;
  
  const teamsMessage = {
    "@type": "MessageCard",
    "@context": "http://schema.org/extensions",
    "themeColor": alert.severity === 'critical' ? "FF0000" : "FFA500",
    "summary": alert.alert_name,
    "sections": [{
      "activityTitle": `🚨 ${alert.alert_name}`,
      "facts": [
        { "name": "Stream", "value": alert.dataset },
        { "name": "Severity", "value": alert.severity },
        { "name": "Value", "value": `${alert.current_value} (threshold: ${alert.threshold})` }
      ],
      "markdown": true
    }]
  };
  
  await axios.post(process.env.TEAMS_WEBHOOK_URL, teamsMessage);
  res.status(200).json({ status: 'sent' });
});
```

### Forward to Discord

```javascript
app.post('/webhook', async (req, res) => {
  const alert = req.body;
  
  const discordMessage = {
    embeds: [{
      title: `🚨 ${alert.alert_name}`,
      color: alert.severity === 'critical' ? 0xFF0000 : 0xFFA500,
      fields: [
        { name: "Stream", value: alert.dataset, inline: true },
        { name: "Severity", value: alert.severity, inline: true },
        { name: "Value", value: `${alert.current_value}`, inline: true }
      ],
      timestamp: alert.triggered_at
    }]
  };
  
  await axios.post(process.env.DISCORD_WEBHOOK_URL, discordMessage);
  res.status(200).json({ status: 'sent' });
});
```

### Trigger AWS Lambda

```javascript
const AWS = require('aws-sdk');
const lambda = new AWS.Lambda();

app.post('/webhook', async (req, res) => {
  const alert = req.body;
  
  await lambda.invoke({
    FunctionName: 'alert-handler',
    InvocationType: 'Event',
    Payload: JSON.stringify(alert)
  }).promise();
  
  res.status(200).json({ status: 'triggered' });
});
```

## Best Practices

1. **Respond Quickly** - Return 200 status immediately, process async if needed
2. **Implement Retries** - Handle transient failures gracefully
3. **Validate Payloads** - Verify the webhook payload structure
4. **Use HTTPS** - Always use encrypted connections
5. **Authenticate Requests** - Verify requests are from Parseable
6. **Log Everything** - Keep audit logs of received webhooks
7. **Handle Duplicates** - Implement idempotency for duplicate alerts

## Troubleshooting

### Webhook Not Receiving

1. Verify the webhook URL is accessible from Parseable
2. Check firewall rules allow incoming connections
3. Verify the endpoint returns 2xx status codes
4. Check Parseable logs for webhook errors

### Authentication Failures

1. Verify credentials are correct
2. Check header names are properly formatted
3. Ensure tokens haven't expired

### Timeout Issues

1. Increase timeout settings if processing takes time
2. Process alerts asynchronously
3. Return 202 Accepted for long-running operations

## Next Steps

* Set up [Parseable alerts](/docs/user-guide/alerting) for automated notifications
* Configure [Slack](/docs/integrations/alerting/slack) for team notifications
* Configure [PagerDuty](/docs/integrations/alerting/pagerduty) for incident management


# Auth0 (/docs/integrations/auth/auth0)



Configure Auth0 as an identity provider for Parseable using OpenID Connect.

## Overview

Integrate Auth0 with Parseable to:

* **Flexible Authentication** - Multiple identity providers
* **Social Login** - Google, GitHub, and more
* **Enterprise Connections** - SAML, LDAP, AD
* **Passwordless** - Email and SMS authentication

## Prerequisites

* Auth0 account
* Auth0 tenant
* Parseable instance with OIDC support

## Auth0 Configuration

### Create Application

1. Log in to Auth0 Dashboard
2. Go to **Applications** → **Applications**
3. Click **Create Application**
4. Configure:
   * **Name**: Parseable
   * **Type**: Regular Web Applications
5. Click **Create**

### Configure Application

1. Go to **Settings** tab
2. Configure:
   * **Allowed Callback URLs**: `https://your-parseable.com/callback`
   * **Allowed Logout URLs**: `https://your-parseable.com`
   * **Allowed Web Origins**: `https://your-parseable.com`
3. Click **Save Changes**

### Get Credentials

From the **Settings** tab, copy:

* **Domain** (e.g., `your-tenant.auth0.com`)
* **Client ID**
* **Client Secret**

## Parseable Configuration

### Environment Variables

```bash
P_OIDC_CLIENT_ID=your-client-id
P_OIDC_CLIENT_SECRET=your-client-secret
P_OIDC_ISSUER=https://your-tenant.auth0.com/
P_OIDC_REDIRECT_URI=https://your-parseable.com/callback
```

### Docker Compose

```yaml
version: '3.8'
services:
  parseable:
    image: parseable/parseable:latest
    environment:
      - P_OIDC_CLIENT_ID=${AUTH0_CLIENT_ID}
      - P_OIDC_CLIENT_SECRET=${AUTH0_CLIENT_SECRET}
      - P_OIDC_ISSUER=https://your-tenant.auth0.com/
      - P_OIDC_REDIRECT_URI=https://your-parseable.com/callback
```

## OIDC Endpoints

Auth0 OIDC endpoints:

| Endpoint      | URL                                                |
| ------------- | -------------------------------------------------- |
| Issuer        | `https://{tenant}.auth0.com/`                      |
| Authorization | `https://{tenant}.auth0.com/authorize`             |
| Token         | `https://{tenant}.auth0.com/oauth/token`           |
| UserInfo      | `https://{tenant}.auth0.com/userinfo`              |
| JWKS          | `https://{tenant}.auth0.com/.well-known/jwks.json` |

## Custom Claims with Rules

Add custom claims using Auth0 Rules:

```javascript
function addRolesToToken(user, context, callback) {
  const namespace = 'https://parseable.com/';
  const assignedRoles = (context.authorization || {}).roles || [];
  
  context.idToken[namespace + 'roles'] = assignedRoles;
  context.accessToken[namespace + 'roles'] = assignedRoles;
  
  callback(null, user, context);
}
```

## Social Connections

Enable social login:

1. Go to **Authentication** → **Social**
2. Enable desired providers (Google, GitHub, etc.)
3. Configure each provider with API keys

## Best Practices

1. **Use Rules** - Add custom claims for authorization
2. **Enable MFA** - Configure multi-factor authentication
3. **Brute Force Protection** - Enable attack protection
4. **Audit Logs** - Monitor authentication events

## Troubleshooting

### Callback URL Mismatch

1. Verify callback URL matches exactly (including trailing slash)
2. Check for http vs https
3. Verify domain is correct

### Token Issues

1. Check client secret is correct
2. Verify issuer URL format
3. Check Auth0 logs for errors

## Next Steps

* Configure [OAuth](/docs/user-guide/openid) for other providers
* Set up [RBAC](/docs/user-guide/rbac) in Parseable
* Review [security best practices](/docs/user-guide/rbac)


# Authentik (/docs/integrations/auth/authentik)



Authentik is an open source, multi-tenant authentication and authorization server. It is a drop-in replacement for Okta, Keycloak, and other identity providers. This document offers step-by-step guide to set up Authentik with Parseable using OpenID Connect (OIDC)

## Pre-requisites

* Parseable server setup and receiving logs from your application. Follow the installation guide to set it up.
* Authentik installed and running. Refer their docs here.

## Configure Authentik

* Browse to your Authentik instance and sign in.
* Create an OAuth2 Provider
* Navigate to Applications → Providers.
* Start by creating an OAuth2 provider.
* Set the Redirect URI to:

```sh
[parseable-instance-url]/api/v1/o/code
```

For example, if your Parseable instance is hosted at `https://demo.parseable.com/`, then the redirect URI should be:

```sh
https://demo.parseable.com/api/v1/o/code
```

## Setting up OIDC in Parseable

Set up requires configuring the OIDC provider via environment variables. Please add these environment variables to your Parseable instance.

```sh
P_OIDC_CLIENT_ID → Client ID from Authentik OAuth2 provider.

P_OIDC_CLIENT_SECRET → Client Secret from Authentik OAuth2 provider.

P_OIDC_ISSUER → Authentik issuer URL.

P_ORIGIN_URI → Parseable host URL.
```

After setting the environment variables, restart the Parseable server instance. For more details on environment variables, refer to [Parseable OIDC documentation](/docs/user-guide/openid#environment-variables).

<Callout type="info">
  If you’re running a distributed Parseable set up, please ensure to set these environment variables across all the Parseable instances.
</Callout>

## Configure OIDC Role in Parseable

Once the environment variables are setup,

* Login with admin access.
* Navigate to Users from the left sidebar.
* Click Create Role:
  * Provide a name for the role.
  * Assign the required privileges.
* After creating the role, click Set Default OIDC Role:
  * Select the newly created role from the dropdown.
  * Click Set Default OIDC Role.

<Callout type="info">
  The option to set a default OIDC role will appear only if the OIDC provider is correctly configured.
</Callout>

## Login using SSO

Now logout of Parseable and the next time you try to login using OAuth you'll be redirected to Authentik to login to Parseable

## Troubleshooting

In case of 401 error check for one of the following:

* Incorrect client\_id or client\_secret
* An invalid or malformed code during the exchange
* A redirect URI mismatch between Parseable and Authentik.


# Azure AD / Entra ID (/docs/integrations/auth/azure-ad)



Configure Microsoft Entra ID (formerly Azure AD) for Parseable authentication.

## Overview

Integrate Azure AD with Parseable to:

* **Microsoft SSO** - Use Microsoft 365 identities
* **Enterprise Integration** - Connect with existing Azure infrastructure
* **Conditional Access** - Apply Azure AD security policies
* **Group-Based Access** - Use Azure AD groups for authorization

## Prerequisites

* Azure subscription
* Azure AD tenant
* Global Administrator or Application Administrator role
* Parseable instance with OIDC support

## Azure AD Configuration

### Register Application

1. Go to **Azure Portal** → **Azure Active Directory**
2. Click **App registrations** → **New registration**
3. Configure:
   * **Name**: Parseable
   * **Supported account types**: Choose appropriate option
   * **Redirect URI**: Web - `https://your-parseable.com/callback`
4. Click **Register**

### Configure Authentication

1. Go to **Authentication**
2. Add platform if needed
3. Configure:
   * **Redirect URIs**: `https://your-parseable.com/callback`
   * **Front-channel logout URL**: `https://your-parseable.com`
   * **ID tokens**: Check this box
4. Click **Save**

### Create Client Secret

1. Go to **Certificates & secrets**
2. Click **New client secret**
3. Add description and expiry
4. Click **Add**
5. **Copy the secret value immediately** (shown only once)

### Get Application Details

From **Overview**, copy:

* **Application (client) ID**
* **Directory (tenant) ID**

## Parseable Configuration

### Environment Variables

```bash
P_OIDC_CLIENT_ID=your-application-id
P_OIDC_CLIENT_SECRET=your-client-secret
P_OIDC_ISSUER=https://login.microsoftonline.com/{tenant-id}/v2.0
P_OIDC_REDIRECT_URI=https://your-parseable.com/callback
```

### Docker Compose

```yaml
version: '3.8'
services:
  parseable:
    image: parseable/parseable:latest
    environment:
      - P_OIDC_CLIENT_ID=${AZURE_CLIENT_ID}
      - P_OIDC_CLIENT_SECRET=${AZURE_CLIENT_SECRET}
      - P_OIDC_ISSUER=https://login.microsoftonline.com/${AZURE_TENANT_ID}/v2.0
      - P_OIDC_REDIRECT_URI=https://your-parseable.com/callback
```

## OIDC Endpoints

Azure AD v2.0 endpoints:

| Endpoint      | URL                                                                |
| ------------- | ------------------------------------------------------------------ |
| Issuer        | `https://login.microsoftonline.com/{tenant}/v2.0`                  |
| Authorization | `https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize` |
| Token         | `https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token`     |
| JWKS          | `https://login.microsoftonline.com/{tenant}/discovery/v2.0/keys`   |

## Group Claims

Include group membership in tokens:

1. Go to **Token configuration**
2. Click **Add groups claim**
3. Select group types to include
4. Configure token properties
5. Click **Add**

## API Permissions

Add required permissions:

1. Go to **API permissions**
2. Click **Add a permission**
3. Select **Microsoft Graph**
4. Add:
   * `openid`
   * `profile`
   * `email`
5. Click **Grant admin consent**

## Best Practices

1. **Use Managed Identity** - For Azure-hosted Parseable
2. **Configure Conditional Access** - Apply security policies
3. **Enable MFA** - Require multi-factor authentication
4. **Monitor Sign-ins** - Review Azure AD sign-in logs

## Troubleshooting

### AADSTS Error Codes

| Code          | Description        | Solution            |
| ------------- | ------------------ | ------------------- |
| AADSTS50011   | Reply URL mismatch | Check redirect URI  |
| AADSTS700016  | App not found      | Verify client ID    |
| AADSTS7000215 | Invalid secret     | Check client secret |

### Token Issues

1. Verify tenant ID is correct
2. Check v2.0 endpoint is used
3. Verify permissions are granted

## Next Steps

* Configure [OAuth](/docs/user-guide/openid) for other providers
* Set up [RBAC](/docs/user-guide/rbac) in Parseable
* Review [security best practices](/docs/user-guide/rbac)


# Google Workspace (/docs/integrations/auth/google-workspace)



Configure Google Workspace (formerly G Suite) for Parseable authentication.

## Overview

Integrate Google Workspace with Parseable to:

* **Google SSO** - Use Google Workspace identities
* **Domain Restriction** - Limit access to your domain
* **Simple Setup** - Quick OAuth configuration
* **Familiar Login** - Users sign in with Google

## Prerequisites

* Google Workspace account (or Google Cloud project)
* Admin access to Google Cloud Console
* Parseable instance with OIDC support

## Google Cloud Configuration

### Create OAuth Client

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Select or create a project
3. Go to **APIs & Services** → **Credentials**
4. Click **Create Credentials** → **OAuth client ID**

### Configure OAuth Consent Screen

If prompted, configure the consent screen:

1. Go to **OAuth consent screen**
2. Select **Internal** (for Workspace) or **External**
3. Fill in:
   * **App name**: Parseable
   * **User support email**: Your email
   * **Developer contact**: Your email
4. Add scopes: `email`, `profile`, `openid`
5. Click **Save and Continue**

### Create Client ID

1. **Application type**: Web application
2. **Name**: Parseable
3. **Authorized redirect URIs**: `https://your-parseable.com/callback`
4. Click **Create**
5. Copy **Client ID** and **Client Secret**

## Parseable Configuration

### Environment Variables

```bash
P_OIDC_CLIENT_ID=your-client-id.apps.googleusercontent.com
P_OIDC_CLIENT_SECRET=your-client-secret
P_OIDC_ISSUER=https://accounts.google.com
P_OIDC_REDIRECT_URI=https://your-parseable.com/callback
```

### Docker Compose

```yaml
version: '3.8'
services:
  parseable:
    image: parseable/parseable:latest
    environment:
      - P_OIDC_CLIENT_ID=${GOOGLE_CLIENT_ID}
      - P_OIDC_CLIENT_SECRET=${GOOGLE_CLIENT_SECRET}
      - P_OIDC_ISSUER=https://accounts.google.com
      - P_OIDC_REDIRECT_URI=https://your-parseable.com/callback
```

## OIDC Endpoints

Google OIDC endpoints:

| Endpoint      | URL                                                |
| ------------- | -------------------------------------------------- |
| Issuer        | `https://accounts.google.com`                      |
| Authorization | `https://accounts.google.com/o/oauth2/v2/auth`     |
| Token         | `https://oauth2.googleapis.com/token`              |
| UserInfo      | `https://openidconnect.googleapis.com/v1/userinfo` |
| JWKS          | `https://www.googleapis.com/oauth2/v3/certs`       |

## Domain Restriction

Restrict access to your Google Workspace domain:

### In Google Cloud Console

1. Go to **OAuth consent screen**
2. Set **User type** to **Internal**
3. Only users in your Workspace domain can access

### In Parseable (if supported)

Configure allowed domains in Parseable settings.

## Best Practices

1. **Use Internal Type** - For Workspace-only access
2. **Verify Domain** - Add and verify your domain
3. **Limit Scopes** - Request only needed permissions
4. **Monitor Usage** - Check OAuth usage in Cloud Console

## Troubleshooting

### Access Blocked

1. Verify OAuth consent screen is configured
2. Check app is published (for external)
3. Verify user is in allowed domain

### Invalid Client

1. Check client ID format (ends with `.apps.googleusercontent.com`)
2. Verify client secret is correct
3. Check redirect URI matches exactly

## Next Steps

* Configure [OAuth](/docs/user-guide/openid) for other providers
* Set up [RBAC](/docs/user-guide/rbac) in Parseable
* Review [security best practices](/docs/user-guide/rbac)


# Keycloak (/docs/integrations/auth/keycloak)



Configure Keycloak as an identity provider for Parseable using OpenID Connect.

## Overview

Integrate Keycloak with Parseable to:

* **Single Sign-On** - Use existing Keycloak identities
* **Role-Based Access** - Map Keycloak roles to Parseable permissions
* **Centralized Auth** - Manage users in one place
* **Multi-Factor Auth** - Leverage Keycloak's MFA capabilities

## Prerequisites

* Keycloak server running
* Admin access to Keycloak
* Parseable instance with OIDC support

## Keycloak Configuration

### Create Realm (Optional)

1. Log in to Keycloak Admin Console
2. Click **Create Realm**
3. Name it (e.g., `parseable`)
4. Click **Create**

### Create Client

1. Go to **Clients** → **Create client**
2. Configure:
   * **Client ID**: `parseable`
   * **Client Protocol**: `openid-connect`
3. Click **Next**
4. Configure capability:
   * **Client authentication**: On
   * **Authorization**: Off
5. Click **Next**
6. Configure URLs:
   * **Root URL**: `https://your-parseable.com`
   * **Valid redirect URIs**: `https://your-parseable.com/callback`
   * **Web origins**: `https://your-parseable.com`
7. Click **Save**

### Get Client Secret

1. Go to **Clients** → **parseable** → **Credentials**
2. Copy the **Client secret**

### Configure Mappers (Optional)

Map Keycloak roles to Parseable:

1. Go to **Clients** → **parseable** → **Client scopes**
2. Click **parseable-dedicated**
3. Add mapper:
   * **Name**: `roles`
   * **Mapper type**: `User Realm Role`
   * **Token Claim Name**: `roles`
   * **Add to ID token**: On

## Parseable Configuration

### Environment Variables

```bash
P_OIDC_CLIENT_ID=parseable
P_OIDC_CLIENT_SECRET=your-client-secret
P_OIDC_ISSUER=https://keycloak.example.com/realms/parseable
P_OIDC_REDIRECT_URI=https://your-parseable.com/callback
```

### Docker Compose

```yaml
version: '3.8'
services:
  parseable:
    image: parseable/parseable:latest
    environment:
      - P_OIDC_CLIENT_ID=parseable
      - P_OIDC_CLIENT_SECRET=${KEYCLOAK_CLIENT_SECRET}
      - P_OIDC_ISSUER=https://keycloak.example.com/realms/parseable
      - P_OIDC_REDIRECT_URI=https://your-parseable.com/callback
```

## OIDC Endpoints

Keycloak OIDC endpoints follow this pattern:

| Endpoint      | URL                                                                |
| ------------- | ------------------------------------------------------------------ |
| Issuer        | `https://keycloak/realms/{realm}`                                  |
| Authorization | `https://keycloak/realms/{realm}/protocol/openid-connect/auth`     |
| Token         | `https://keycloak/realms/{realm}/protocol/openid-connect/token`    |
| UserInfo      | `https://keycloak/realms/{realm}/protocol/openid-connect/userinfo` |
| JWKS          | `https://keycloak/realms/{realm}/protocol/openid-connect/certs`    |

## Role Mapping

Map Keycloak roles to Parseable roles:

| Keycloak Role | Parseable Permission |
| ------------- | -------------------- |
| `admin`       | Full access          |
| `editor`      | Read/write streams   |
| `viewer`      | Read-only access     |

## Best Practices

1. **Use Dedicated Realm** - Isolate Parseable users
2. **Enable MFA** - Add security with multi-factor auth
3. **Configure Session Timeout** - Set appropriate session lengths
4. **Use Groups** - Organize users with Keycloak groups

## Troubleshooting

### Login Fails

1. Verify client ID and secret
2. Check redirect URI matches exactly
3. Verify issuer URL is correct
4. Check Keycloak logs

### Role Mapping Issues

1. Verify mapper configuration
2. Check token contains roles claim
3. Verify role names match

## Next Steps

* Configure [OAuth](/docs/user-guide/openid) for other providers
* Set up [RBAC](/docs/user-guide/rbac) in Parseable
* Review [security best practices](/docs/user-guide/rbac)


# LDAP (/docs/integrations/auth/ldap)



Configure LDAP (Lightweight Directory Access Protocol) for Parseable authentication.

## Overview

Integrate LDAP with Parseable to:

* **Directory Integration** - Use existing LDAP/AD users
* **Centralized Auth** - Single source of truth for users
* **Group-Based Access** - Map LDAP groups to permissions
* **Enterprise Ready** - Support for Active Directory

## Prerequisites

* LDAP server (OpenLDAP, Active Directory, etc.)
* LDAP bind credentials
* Network access from Parseable to LDAP server
* Parseable Enterprise (LDAP support may require enterprise features)

## LDAP Configuration

### Connection Settings

```bash
# LDAP Server Configuration
P_LDAP_URL=ldap://ldap.example.com:389
P_LDAP_BIND_DN=cn=admin,dc=example,dc=com
P_LDAP_BIND_PASSWORD=your-bind-password
P_LDAP_BASE_DN=dc=example,dc=com
P_LDAP_USER_FILTER=(uid={username})
```

### TLS/SSL Configuration

For secure LDAP (LDAPS):

```bash
P_LDAP_URL=ldaps://ldap.example.com:636
P_LDAP_TLS_ENABLED=true
P_LDAP_TLS_SKIP_VERIFY=false
P_LDAP_TLS_CA_CERT=/path/to/ca.crt
```

### Docker Compose

```yaml
version: '3.8'
services:
  parseable:
    image: parseable/parseable:latest
    environment:
      - P_LDAP_URL=ldap://ldap.example.com:389
      - P_LDAP_BIND_DN=cn=admin,dc=example,dc=com
      - P_LDAP_BIND_PASSWORD=${LDAP_PASSWORD}
      - P_LDAP_BASE_DN=dc=example,dc=com
      - P_LDAP_USER_FILTER=(uid={username})
    volumes:
      - ./certs:/etc/parseable/certs
```

## Active Directory Configuration

For Microsoft Active Directory:

```bash
P_LDAP_URL=ldap://ad.example.com:389
P_LDAP_BIND_DN=CN=Service Account,OU=Service Accounts,DC=example,DC=com
P_LDAP_BIND_PASSWORD=your-password
P_LDAP_BASE_DN=DC=example,DC=com
P_LDAP_USER_FILTER=(sAMAccountName={username})
P_LDAP_GROUP_FILTER=(member={dn})
```

## Configuration Options

| Parameter                | Description                   |
| ------------------------ | ----------------------------- |
| `P_LDAP_URL`             | LDAP server URL               |
| `P_LDAP_BIND_DN`         | Bind DN for LDAP queries      |
| `P_LDAP_BIND_PASSWORD`   | Bind password                 |
| `P_LDAP_BASE_DN`         | Base DN for searches          |
| `P_LDAP_USER_FILTER`     | Filter to find users          |
| `P_LDAP_GROUP_FILTER`    | Filter to find groups         |
| `P_LDAP_TLS_ENABLED`     | Enable TLS                    |
| `P_LDAP_TLS_SKIP_VERIFY` | Skip certificate verification |

## User Filter Examples

### OpenLDAP

```
(uid={username})
```

### Active Directory

```
(sAMAccountName={username})
```

### By Email

```
(mail={username})
```

### Multiple Attributes

```
(|(uid={username})(mail={username}))
```

## Group Mapping

Map LDAP groups to Parseable roles:

```bash
P_LDAP_GROUP_BASE_DN=ou=groups,dc=example,dc=com
P_LDAP_GROUP_FILTER=(member={dn})
P_LDAP_ADMIN_GROUP=cn=parseable-admins,ou=groups,dc=example,dc=com
P_LDAP_EDITOR_GROUP=cn=parseable-editors,ou=groups,dc=example,dc=com
```

## Testing LDAP Connection

Test with `ldapsearch`:

```bash
# Test bind
ldapsearch -x -H ldap://ldap.example.com:389 \
  -D "cn=admin,dc=example,dc=com" \
  -w password \
  -b "dc=example,dc=com" \
  "(uid=testuser)"

# Test with TLS
ldapsearch -x -H ldaps://ldap.example.com:636 \
  -D "cn=admin,dc=example,dc=com" \
  -w password \
  -b "dc=example,dc=com" \
  "(uid=testuser)"
```

## Best Practices

1. **Use LDAPS** - Always use TLS in production
2. **Service Account** - Use dedicated bind account
3. **Minimal Permissions** - Bind account needs only read access
4. **Connection Pooling** - Enable for performance
5. **Failover** - Configure multiple LDAP servers

## Troubleshooting

### Connection Failed

1. Verify LDAP server is accessible
2. Check firewall rules (port 389 or 636)
3. Verify bind DN and password
4. Check TLS certificate

### User Not Found

1. Verify base DN is correct
2. Check user filter syntax
3. Test with ldapsearch
4. Verify user exists in LDAP

### Group Mapping Issues

1. Verify group filter syntax
2. Check group base DN
3. Verify user is member of group

## Next Steps

* Configure [OAuth](/docs/user-guide/openid) for OIDC providers
* Set up [RBAC](/docs/user-guide/rbac) in Parseable
* Review [security best practices](/docs/user-guide/rbac)


# Okta (/docs/integrations/auth/okta)



Configure Okta as an identity provider for Parseable using OpenID Connect.

## Overview

Integrate Okta with Parseable to:

* **Enterprise SSO** - Use Okta for authentication
* **User Management** - Centralized user provisioning
* **MFA Support** - Leverage Okta's security features
* **Compliance** - Meet enterprise security requirements

## Prerequisites

* Okta organization
* Admin access to Okta
* Parseable instance with OIDC support

## Okta Configuration

### Create Application

1. Log in to Okta Admin Console
2. Go to **Applications** → **Applications**
3. Click **Create App Integration**
4. Select:
   * **Sign-in method**: OIDC - OpenID Connect
   * **Application type**: Web Application
5. Click **Next**

### Configure Application

1. **App integration name**: Parseable
2. **Grant type**: Authorization Code
3. **Sign-in redirect URIs**: `https://your-parseable.com/callback`
4. **Sign-out redirect URIs**: `https://your-parseable.com`
5. **Controlled access**: Select appropriate option
6. Click **Save**

### Get Credentials

1. Go to your application's **General** tab
2. Copy:
   * **Client ID**
   * **Client Secret**
3. Note your Okta domain (e.g., `dev-123456.okta.com`)

### Assign Users

1. Go to **Assignments** tab
2. Click **Assign** → **Assign to People** or **Assign to Groups**
3. Select users/groups
4. Click **Done**

## Parseable Configuration

### Environment Variables

```bash
P_OIDC_CLIENT_ID=your-client-id
P_OIDC_CLIENT_SECRET=your-client-secret
P_OIDC_ISSUER=https://dev-123456.okta.com
P_OIDC_REDIRECT_URI=https://your-parseable.com/callback
```

### Docker Compose

```yaml
version: '3.8'
services:
  parseable:
    image: parseable/parseable:latest
    environment:
      - P_OIDC_CLIENT_ID=${OKTA_CLIENT_ID}
      - P_OIDC_CLIENT_SECRET=${OKTA_CLIENT_SECRET}
      - P_OIDC_ISSUER=https://dev-123456.okta.com
      - P_OIDC_REDIRECT_URI=https://your-parseable.com/callback
```

## OIDC Endpoints

Okta OIDC endpoints:

| Endpoint      | URL                                             |
| ------------- | ----------------------------------------------- |
| Issuer        | `https://{domain}.okta.com`                     |
| Authorization | `https://{domain}.okta.com/oauth2/v1/authorize` |
| Token         | `https://{domain}.okta.com/oauth2/v1/token`     |
| UserInfo      | `https://{domain}.okta.com/oauth2/v1/userinfo`  |
| JWKS          | `https://{domain}.okta.com/oauth2/v1/keys`      |

## Custom Authorization Server

For custom claims, use a custom authorization server:

```bash
P_OIDC_ISSUER=https://dev-123456.okta.com/oauth2/default
```

## Best Practices

1. **Use Groups** - Manage access with Okta groups
2. **Enable MFA** - Require multi-factor authentication
3. **Configure Session** - Set appropriate session policies
4. **Audit Logs** - Monitor authentication events

## Troubleshooting

### Login Redirect Loop

1. Verify redirect URI matches exactly
2. Check client ID and secret
3. Verify issuer URL format

### User Not Authorized

1. Check user is assigned to application
2. Verify group assignments
3. Check Okta system logs

## Next Steps

* Configure [OAuth](/docs/user-guide/openid) for other providers
* Set up [RBAC](/docs/user-guide/rbac) in Parseable
* Review [security best practices](/docs/user-guide/rbac)


# Apache Superset (/docs/integrations/visualization/apache-superset)



Connect Parseable to Apache Superset for powerful data exploration, visualization, and dashboarding.

## Overview

Integrate Parseable with Apache Superset to:

* **Data Exploration** - Explore log data with an intuitive interface
* **Rich Visualizations** - Create charts, graphs, and maps
* **Interactive Dashboards** - Build real-time monitoring dashboards
* **SQL Lab** - Run ad-hoc queries on your log data

## Prerequisites

* Apache Superset instance
* Parseable instance with data
* Python 3.11.6 or higher

## Installation

### Install Parseable SQLAlchemy Driver

Install the Parseable connector for Apache Superset:

```bash
# Create and activate a virtual environment (recommended)
python -m venv superset-env
source superset-env/bin/activate  # On Windows: superset-env\Scripts\activate

# Install Apache Superset
pip install apache-superset

# Install Parseable SQLAlchemy driver
pip install sqlalchemy-parseable

# Initialize Superset
superset db upgrade
superset fab create-admin
superset init

# Run Superset
superset run -p 8088 --with-threads --reload --debugger
```

## Connection Setup

### Add Database Connection

1. Log in to Apache Superset at `http://localhost:8088`
2. Go to **Data** → **Databases** → **+ Database**
3. Select **Other** as the database type
4. Use the following SQLAlchemy URI format:

```
parseable://username:password@host:port/dataset_name
```

### Example Connection String

```
parseable://admin:admin@demo.parseable.com:443/ingress-nginx
```

For local Parseable instance:

```
parseable://admin:admin@localhost:8000/application-logs
```

## Creating Visualizations

### Add Dataset

1. Go to **Data** → **Datasets**
2. Click **+ Dataset**
3. Select your Parseable database
4. Choose a dataset as the table
5. Click **Add**

### Create Chart

1. Go to **Charts** → **+ Chart**
2. Select your dataset
3. Choose a visualization type:
   * **Time-series** for log trends
   * **Bar Chart** for categorical data
   * **Table** for detailed views
   * **Big Number** for KPIs

### Example: Error Rate Over Time

1. Create a new chart with Time-series visualization
2. Configure:
   * **Time Column**: `p_timestamp`
   * **Metric**: `COUNT(*)`
   * **Filter**: `level = 'error'`
   * **Time Grain**: `hour`

## Building Dashboards

### Create Dashboard

1. Go to **Dashboards** → **+ Dashboard**
2. Add charts by dragging from the chart list
3. Arrange and resize as needed
4. Add filters for interactivity
5. Save and publish

### Dashboard Filters

Add cross-filtering to your dashboard:

1. Edit dashboard
2. Click **Filter** icon
3. Add filter components:
   * Time range filter
   * Stream selector
   * Log level filter

## SQL Lab Queries

Use SQL Lab for ad-hoc analysis:

```sql
-- Error count by service
SELECT 
  service,
  COUNT(*) as error_count
FROM "application-logs"
WHERE level = 'error'
  AND p_timestamp > NOW() - INTERVAL '24 hours'
GROUP BY service
ORDER BY error_count DESC
LIMIT 10;

-- Response time percentiles
SELECT 
  percentile_cont(0.50) WITHIN GROUP (ORDER BY response_time) as p50,
  percentile_cont(0.95) WITHIN GROUP (ORDER BY response_time) as p95,
  percentile_cont(0.99) WITHIN GROUP (ORDER BY response_time) as p99
FROM "api-logs"
WHERE p_timestamp > NOW() - INTERVAL '1 hour';
```

## Best Practices

1. **Use Caching** - Enable query caching for better performance
2. **Optimize Queries** - Use time filters to limit data scanned
3. **Create Virtual Datasets** - Pre-aggregate data for complex dashboards
4. **Set Refresh Intervals** - Configure appropriate auto-refresh rates

## Troubleshooting

### Connection Issues

1. Verify Parseable is accessible from Superset
2. Check credentials are correct
3. Ensure PostgreSQL port is exposed

### Slow Queries

1. Add time range filters
2. Use LIMIT clauses
3. Enable query caching

## Next Steps

* Create [dashboards](/docs/user-guide/dashboards) in Parseable
* Set up [alerts](/docs/user-guide/alerting) for anomalies
* Explore [Grafana](/docs/integrations/visualization/grafana) integration


# Grafana Data Source (/docs/integrations/visualization/grafana)



Parseable data source plugin allows you to query and visualize log data stored in Parseable server, in your Grafana dashboard.

## Pre-requisites

* Parseable server setup and receiving logs from your application.
* Grafana installed and running.

## Installation

There are several ways to install the plugin:

* Grafana UI: Install the plugin from your Grafana instance (Configuration > Data sources > Add Data source). Add Parseable as a data source at the data source configuration page.

* Grafana CLI: Install the plugin using the command grafana-cli plugins install parseable-parseable-datasource. Then restart Grafana.

* Grafana Helm Chart: Install the plugin by modifying the Grafana Chart `values.yaml` file. Add the following lines under `plugins` section.

```yaml
plugins:
  # - digrich-bubblechart-panel
  # - grafana-clock-panel
  ## You can also use other plugin download URL, as long as they are valid zip ## files, and specify the name of the plugin after the semicolon. Like this:
    - https://grafana.com/api/plugins/parseable-parseable-datasource/versions/1.0.2/download;parseable-parseable-datasource
```

Add the following lines under `datasources` section.

```yaml
## Configure grafana datasources
## ref: http://docs.grafana.org/administration/provisioning/#datasources
##
datasources:
 datasources.yaml:
   apiVersion: 1
   datasources:
   - name: Parseable
     type: parseable-parseable-datasource
     url: http://parseable.parseable
     access: proxy
     isDefault: true
     basicAuth: true
     basicAuthUser: admin
     secureJsonData:
        basicAuthPassword: admin    
```

Please remember to update the `url`, `basicAuthUser` and `basicAuthPassword` values with your Parseable server instance details.

If you're deploying Grafana and would like to install the plugin at the same time, you can use the `GF_INSTALL_PLUGINS` environment variable. For example, `GF_INSTALL_PLUGINS=parseable-parseable-datasource 1.0.2`. Then restart Grafana.

If you're provisioning Grafana using [config management tools like Ansible](https://grafana.com/docs/grafana/latest/administration/provisioning/#datasources), you can manage data sources in Grafana by adding YAML configuration files in the `provisioning/datasources` directory. Refer [Grafana documentation](https://grafana.com/docs/grafana/latest/administration/provisioning/#datasources) for more details.

## Configuration

Configure the data source specifying URL and port like `https://demo.parseable.com:443`. Parseable supports basic auth, so toggle the `Basic Auth` option under Auth section and enter the username and password under ` Basic Auth Details` section. If you're using Parseable demo server as the backend, use `admin, admin` as the credentials.

Push the `Save & Test` button, if there is an error message, check the credentials and connection.

## Usage

Once the plugin is configured with correct Parseable server instance. You can start using it to query and visualize logs. Use the query editor to write your own queries.

### Alerts

Grafana allows you to set up alerts to continuously monitor your data and notify you when specific conditions are met. It ensures that you are promptly informed about any critical issues, allowing for quick resolution and maintaining system reliability.

#### Setting Up an Alert

* Navigate to `your-domain:port/alerting/new/alerting`.
* Add a unique rule name to identify the alert.
* Add a query that returns numerical values, as Grafana supports alerts only on numerical data.
* Specify threshold behavior for the defined rule query.
* Define the evaluation behavior (e.g., eval frequency, grouping).
* Save the alert.

#### Managing Alerts

You can list, update, or delete all the alerts you have created by navigating to `your-domain:port/alerting/list`.

#### Alert Notification Channels

Set alert notification channels to receive alerts by navigating to `your-domain:port/alerting/notifications/receivers/new`. Grafana supports multiple integration targets, including Alertmanager, Email, Slack, Telegram, Webhook, Microsoft Teams, etc.

#### Notification Policies

Define notification policies to ensure you receive alerts on your preferred channels by configuring settings in `your-domain:port/alerting/routes`.

You can also check the alert status in the Grafana UI by navigating to the list page. There, you can view the current status of alerts, last fired time, last evaluated time, and rule query results.

## Workarounds for Non-Numeric Data

In Grafana, alerting is primarily designed for numeric data since it relies on evaluating numerical thresholds and conditions. This means that most alert rules are based on numerical metrics, such as CPU usage, memory consumption, error rates, etc. However, you can get creative with how you process and transform other types of data into numeric forms suitable for alerting.

For example, you can map statuses like "OK", "WARN", and "ERROR" to values like 0, 1, and 2 respectively.

```sql
SELECT
  ...
  CASE
    WHEN status = 'OK' THEN 0
    WHEN status = 'WARN' THEN 1
    WHEN status = 'ERROR' THEN 2
  END as status_value
FROM
  table_name
```


# Looker (/docs/integrations/visualization/looker)



Connect Parseable to Looker for enterprise business intelligence and analytics.

## Overview

Integrate Parseable with Looker to:

* **Semantic Modeling** - Define metrics and dimensions with LookML
* **Self-Service Analytics** - Enable teams to explore data
* **Embedded Analytics** - Embed dashboards in applications
* **Governed Metrics** - Maintain consistent metric definitions

## Integration Options

<Callout type="info">
  Parseable does not have a native Looker connector. Use one of the following methods to integrate.
</Callout>

### Option 1: Export Data via API

Export data from Parseable and load into a Looker-supported database:

```python
import requests
import pandas as pd

# Query Parseable
response = requests.post(
    "http://your-parseable-host:8000/api/v1/query",
    auth=("username", "password"),
    json={
        "query": "SELECT * FROM \"application-logs\" WHERE p_timestamp > NOW() - INTERVAL '24 hours'",
        "startTime": "2024-01-01T00:00:00Z",
        "endTime": "2024-01-02T00:00:00Z"
    }
)

# Load into your data warehouse (BigQuery, Snowflake, etc.)
df = pd.DataFrame(response.json())
# Then use your preferred method to load into the data warehouse
```

### Option 2: Use Apache Superset

For real-time connectivity to Parseable, we recommend using [Apache Superset](/docs/integrations/visualization/apache-superset) which has native Parseable support via the `sqlalchemy-parseable` driver.

### Option 3: Arrow Flight (Advanced)

Parseable exposes an Arrow Flight endpoint on port 8002 (`P_FLIGHT_PORT`) for high-performance data transfer. You can build a custom pipeline to fetch data via Arrow Flight and load into your Looker-connected data warehouse.

## Best Practices

1. **Schedule Data Exports** - Set up automated pipelines to export Parseable data to your data warehouse
2. **Use Incremental Loads** - Only export new data since the last sync
3. **Filter at Source** - Apply time range filters in Parseable queries to reduce data volume
4. **Consider Native Options** - For real-time dashboards, use [Apache Superset](/docs/integrations/visualization/apache-superset) or Parseable's built-in [dashboards](/docs/user-guide/dashboards)

## Next Steps

* Create [dashboards](/docs/user-guide/dashboards) in Parseable's built-in UI
* Set up [alerts](/docs/user-guide/alerting) for monitoring
* Explore [Apache Superset](/docs/integrations/visualization/apache-superset) for native integration


# Metabase (/docs/integrations/visualization/metabase)



# Metabase Integration

Metabase is an open-source business intelligence tool that allows you to create dashboards and visualizations from your data.

## Coming Soon

Documentation for Metabase integration is coming soon. In the meantime, you can connect Metabase to Parseable using the PostgreSQL-compatible interface.

## Quick Setup

1. In Metabase, add a new database connection
2. Select PostgreSQL as the database type
3. Enter your Parseable server details
4. Use your Parseable credentials for authentication

For more details, please refer to the [Metabase documentation](https://www.metabase.com/docs/latest/).


# Redash (/docs/integrations/visualization/redash)



Connect Parseable to Redash for SQL-based querying and dashboard creation.

## Overview

Integrate Parseable with Redash to:

* **SQL Queries** - Write and save SQL queries against log data
* **Visualizations** - Create charts from query results
* **Dashboards** - Combine visualizations into dashboards
* **Alerts** - Set up query-based alerts

## Integration Options

<Callout type="info">
  Parseable does not have a native Redash connector. Use one of the following methods to integrate.
</Callout>

### Option 1: Custom Query Runner

You can create a custom Redash query runner that uses Parseable's HTTP API. This requires modifying your Redash installation.

### Option 2: Export to Supported Database

Export data from Parseable to a Redash-supported database (PostgreSQL, MySQL, etc.):

```python
import requests
import pandas as pd
from sqlalchemy import create_engine

# Query Parseable
response = requests.post(
    "http://your-parseable-host:8000/api/v1/query",
    auth=("username", "password"),
    json={
        "query": "SELECT * FROM \"application-logs\" WHERE p_timestamp > NOW() - INTERVAL '24 hours'",
        "startTime": "2024-01-01T00:00:00Z",
        "endTime": "2024-01-02T00:00:00Z"
    }
)

# Load into PostgreSQL for Redash
df = pd.DataFrame(response.json())
engine = create_engine('postgresql://user:pass@localhost/analytics')
df.to_sql('parseable_logs', engine, if_exists='replace', index=False)
```

### Option 3: Use Apache Superset

For real-time connectivity to Parseable, we recommend using [Apache Superset](/docs/integrations/visualization/apache-superset) which has native Parseable support via the `sqlalchemy-parseable` driver and offers similar functionality to Redash.

## Example Parseable Queries

These SQL queries can be used with Parseable's Query API:

**Error Count by Hour:**

```sql
SELECT 
  date_trunc('hour', p_timestamp) as hour,
  COUNT(*) as error_count
FROM "application-logs"
WHERE level = 'error'
  AND p_timestamp > NOW() - INTERVAL '24 hours'
GROUP BY hour
ORDER BY hour;
```

**Top Error Messages:**

```sql
SELECT 
  message,
  COUNT(*) as count
FROM "application-logs"
WHERE level = 'error'
  AND p_timestamp > NOW() - INTERVAL '1 hour'
GROUP BY message
ORDER BY count DESC
LIMIT 10;
```

## Best Practices

1. **Schedule Data Syncs** - Automate exports from Parseable to your analytics database
2. **Use Incremental Loads** - Only export new data since the last sync
3. **Filter at Source** - Apply time range filters in Parseable queries to reduce data volume
4. **Consider Native Options** - For real-time dashboards, use [Apache Superset](/docs/integrations/visualization/apache-superset) or Parseable's built-in [dashboards](/docs/user-guide/dashboards)

## Next Steps

* Create [dashboards](/docs/user-guide/dashboards) in Parseable's built-in UI
* Set up [alerts](/docs/user-guide/alerting) for monitoring
* Explore [Apache Superset](/docs/integrations/visualization/apache-superset) for native integration


# Tableau (/docs/integrations/visualization/tableau)



Connect Parseable to Tableau for enterprise-grade analytics and visualization.

## Overview

Integrate Parseable with Tableau to:

* **Enterprise Analytics** - Leverage Tableau's powerful analytics engine
* **Rich Visualizations** - Create sophisticated charts and dashboards
* **Data Blending** - Combine log data with other data sources
* **Sharing** - Publish and share insights across your organization

## Integration Options

Parseable can be connected to Tableau through the following methods:

### Option 1: Export Data via API

Export data from Parseable using the Query API and import into Tableau:

```python
import requests
import pandas as pd

# Query Parseable
response = requests.post(
    "http://your-parseable-host:8000/api/v1/query",
    auth=("username", "password"),
    json={
        "query": "SELECT * FROM \"application-logs\" WHERE p_timestamp > NOW() - INTERVAL '24 hours'",
        "startTime": "2024-01-01T00:00:00Z",
        "endTime": "2024-01-02T00:00:00Z"
    }
)

# Convert to DataFrame and save as CSV
df = pd.DataFrame(response.json())
df.to_csv("parseable_logs.csv", index=False)
```

Then import the CSV into Tableau Desktop.

### Option 2: Use Apache Superset

For real-time connectivity, we recommend using [Apache Superset](/docs/integrations/visualization/apache-superset) which has native Parseable support via the `sqlalchemy-parseable` driver.

### Option 3: Arrow Flight (Advanced)

Parseable exposes an Arrow Flight endpoint on port 8002 (`P_FLIGHT_PORT`) for high-performance data transfer. You can use Arrow Flight clients to fetch data and load into Tableau.

## Working with Exported Data

Once you have your data in Tableau (via CSV export or other methods):

### Time Series Analysis

1. Drag `p_timestamp` to Columns
2. Right-click and select appropriate date part (Hour, Day, etc.)
3. Drag `Number of Records` to Rows
4. Add filters for specific log levels or services

### Log Level Distribution

1. Drag `level` to Columns
2. Drag `Number of Records` to Rows
3. Change mark type to **Bar**
4. Add color by `level`

## Best Practices

1. **Schedule Exports** - Automate data exports using cron jobs or scheduled tasks
2. **Filter Early** - Apply time range filters in the Parseable query to reduce data volume
3. **Use Incremental Exports** - Only export new data since the last export
4. **Consider Apache Superset** - For real-time dashboards, use [Apache Superset](/docs/integrations/visualization/apache-superset) with native Parseable support

## Next Steps

* Create [dashboards](/docs/user-guide/dashboards) in Parseable's built-in UI
* Set up [alerts](/docs/user-guide/alerting) for anomalies
* Explore [Apache Superset](/docs/integrations/visualization/apache-superset) for native integration


# Modelling Data (/docs/overview/key-concepts/data-model)



import { Accordion, Accordions } from 'fumadocs-ui/components/accordion';

It is important to understand how to model the observability data effectively in Parseable. This helps in optimal storage, compression and faster query performance. This section will cover the key concepts of data modelling in Parseable.

## Dataset

A dataset is a logical collection of data designed to ensure optimal storage compression and fast retrieval via query. Datasets are identified by a unique name. Each dataset has its schema, which includes the fields and their types. Role based access control, alerts, retention and notifications are all supported at the dataset level granularity.

Datasets are the primary unit of data storage in Parseable. Any MELT (Metrics, Events, Logs, Traces) data is ingested into one or other dataset.

### Creating a dataset

You can create a dataset using the "Create Dataset" button on Datasets page. You'll be prompted to enter the dataset name, schema type, and partition column.

You can set the schema type to be [static](#static) (schema has to be explicitly provided at the time of creation of dataset) or [dynamic](#dynamic) (let server infer the schema from the incoming data). Once set, the schema type cannot be changed later. Read more about schema types in the [Dataset Schema](#dataset-schema) section.

Partition column is an optional field. If you want to partition the dataset based on a specific field, you can specify that field here. If you don't specify a partition field, Parseable will use the internal `p_timestamp` field as the partition field. Read more about partitioning in the [Partitioning](/docs/key-concepts/partitioning) section.

### Mapping sources to datasets

A source is anything that generates data, i.e. agents like FluentBit, FluentD, Vector, LogStash, agents from the OTel ecosystem, or the application itself. While ingesting data, you'll need to specify the dataset name to which the data should be sent. This allows mapping sources to datasets. Technically it is possible to map any number of data sources any number of data sources. Parseable allows this to ensure flexibility for varying use cases.

But, it is important to critically think about mapping data sources to datasets. This is a key design decision that can impact the performance and usability of your observability data. Too many unrelated columns in a dataset can lead to poor compression and slower query performance. On the other hand, too many datasets can lead to increased complexity in managing the data.

When deciding how to map sources to datasets, consider the following:

* **Schema similarity**: If the sources have similar schema, it is better to map them to a single dataset. This allows for better compression and faster query performance. Similar here means fields are matching for 80 percent or more of the events. If the schema is too different, it is better to create separate datasets for each source.

* **Query patterns**: If you frequently query across multiple sources, it is better to map them to a single dataset. This allows you to query the data easily without having to join multiple datasets.

* **Data retention**: If the sources have different data retention requirements, it is better to create separate datasets for each source. This allows you to set different retention policies for each dataset.

* **Data ownership**: If different teams own different sources, it is better to create separate datasets for each source. This allows you to set different access controls for each dataset and manage the data better.

Let's understand this with some examples:

* **Kubernetes infrastructure logs**: Kubernetes infrastructure logs (e.g. kubelet, kube-proxy, etc.) can be mapped to a single dataset. This allows you to query the logs across all the Kubernetes components easily. Since these logs have similar schema, they fit well into a single dataset.

* **Application logs with similar schema**: If you have logs from multiple applications that log in a common format for example [go-log](https://pkg.go.dev/log), you can create a single dataset for all of them. This allows you to query the logs across applications easily.

* **Application logs with different schemas**: If you have logs from multiple applications that have completely different schemas, you can create a separate dataset for each application. This allows you to enforce a specific schema for each dataset and query them independently.

* **Aggregated data**: If you have aggregated data (e.g. metrics, traces) that you want to store, you can create a separate dataset for that. This allows you to query the aggregated data separately from the raw logs.

<Callout type="warn">
  Beyond 800 columns in a dataset, consider splitting the dataset into multiple datasets based on schema similarity or query patterns. Beyond 1000 columns, the server will reject the ingestion request with an error.
</Callout>

## Dataset vs index

Traditional indices in systems like Elasticsearch are build to ingest textual data, index each field and allow for fast search and retrieval. This works well for pure search use cases, where you want to search for specific keywords or phrases in the data.

But applying this concept to huge volumes of observability data (logs, metrics, traces) is not practical. Observability data is often structured, semi-structured or unstructured, and indexing every field can lead to excessive storage costs for little to no performance gain.

Parseable datasets are designed to handle large volumes of observability data efficiently. They focus on optimal storage compression and fast retrieval via query, rather than indexing every field. This allows Parseable to handle high cardinality data, such as logs with many unique fields, without the performance and storage overhead of traditional indices.

## Dataset schema

Schema defines the fields in an event and their types. Parseable supports two types of schema - dynamic and static. You can choose the schema type while creating the dataset. Additionally, if you want to enforce a specific schema, you'll need to send that schema at the time of creating the dataset.

### Dynamic

Datasets by default have dynamic schema. This means you don't need to define a schema for a dataset. The Parseable server detects the schema from first event. If there are subsequent events (with new schema), it updates internal schema accordingly.

Log data formats evolve over time, and users prefer a dynamic schema approach, where they don't have to worry about schema changes, and they are still able to ingest events to a given dataset.

<Callout type="info">
  For dynamic schema, Parseable doesn't allow changing the type of an existing column whose type is already set. For example, if a column is detected as string in the first event, it can't be changed to int or timestamp in a later event. If you'd like to enforce a specific schema, please use static schema.
</Callout>

### Static

In some cases, you may want to enforce a specific schema for a dataset. You can do this by setting the static schema type while creating the dataset. This schema will be enforced for all the events ingested to the dataset. You'll need to provide the schema in the form of a JSON object with field names and their types, with the create dataset API call. The following types are supported in the schema: `string`, `int`, `float`, `datetime`,`date`, `boolean`.

## FAQ

Some of common questions related to datasets are answered below. If you have any other questions, please reach out to us on [Slack](http://logg.ing/community) or [GitHub Discussions](http://github.com/parseablehq/parseable/discussions).

<Accordions>
  <Accordion id="dataset-vs-index" title="Is a dataset equivalent to an index in Elasticsearch?">
    A dataset is not equivalent to an index in Elasticsearch. While both are used to store and retrieve data, datasets in Parseable are designed specifically for observability data (logs, metrics, traces) and focus on optimal storage compression and fast retrieval via query. Datasets can handle high cardinality data without the performance and storage overhead of traditional indices. Refer to the [Dataset vs index](#dataset-vs-index) section for more details.
  </Accordion>

  <Accordion id="new-vs-old-dataset" title="How do I decide between creating a new dataset or using an existing one?">
    General principle is to create a new dataset if the data has a different schema or if you want to enforce a specific schema. If the data has similar schema and you want to query it together, you can use an existing dataset. Refer to the [Mapping sources to datasets](#mapping-sources-to-datasets) section for more details.
  </Accordion>

  <Accordion id="static-vs-dynamic-schema" title="How do I decide static vs dynamic schema?">
    If in doubt, use static schema. Static schema allows you to enforce a specific schema for the dataset, which can help in better compression and faster query performance. Dynamic schema is useful when you don't want to worry about schema changes and want to ingest events without specifying the schema. Refer to the [Dataset Schema](#dataset-schema) section for more details.
  </Accordion>

  <Accordion id="when-to-use-partitions" title="When should I use partitioning?">
    Partitioning is useful when you want to optimize query performance for specific fields. If you frequently query on a specific field, you can partition the dataset based on that field. This allows Parseable to store the data in a way that makes it faster to retrieve the data for that field. Refer to the [Partitioning](/docs/key-concepts/partitioning) section for more details.
  </Accordion>

  <Accordion id="how-many-columns" title="How many columns are too many in datasets?">
    We recommend keeping the number of columns in a dataset to a reasonable limit, ideally less than 200. Too many columns can lead to poor compression and slower query performance. If you have more than 200 columns, query performance may degrade, and you may need to consider splitting the dataset into multiple datasets based on schema similarity or query patterns. Beyond 250 columns, the server will reject the ingestion request with an error.
  </Accordion>
</Accordions>


# Key Concepts (/docs/overview/key-concepts)



import { IconChartCohort,IconDirections,IconCloudDataConnection,IconBrandInertia,IconFileTypeSql,IconServerBolt
 } from '@tabler/icons-react';

Dive deeper into the key concepts of Parseable to understand how it works, its architecture, and how it can help you with your observability needs. Whether you're new to Parseable or looking to deepen your understanding, these concepts will provide a solid foundation for using Parseable effectively.

<Cards>
  <Card href="/docs/overview/key-concepts/data-model" icon={<IconChartCohort className="text-purple-600" />} title="Modelling Data">
    Learn when to create datasets, how to aggregate observability data, use schemas, and manage your data effectively.
  </Card>

  <Card href="/docs/overview/key-concepts/ingestion" icon={<IconBrandInertia className="text-purple-600" />} title="Ingestion">
    Learn how to ingest, manage and query OpenTelemetry logs, metrics or traces natively. Zero configuration needed.
  </Card>

  <Card href="/docs/overview/key-concepts/storage" icon={<IconCloudDataConnection className="text-purple-600" />} title="Storage">
    Achieve storage efficiency and cost with object stores like S3, GCS, Azure Blob as the primary storage layer.
  </Card>

  <Card href="/docs/overview/key-concepts/query" icon={<IconFileTypeSql className="text-purple-600" />} title="Query">
    Acheive fast query response with Rust based design, modern query techniques, and intelligent caching on SSDs / NVMe and memory.
  </Card>

  <Card href="/docs/overview/key-concepts/partitioning" icon={<IconDirections className="text-purple-600" />} title="Partitioning">
    Optimize query performance by partitioning datasets based on frequently filtered columns.
  </Card>

  <Card href="/docs/key-concepts/high-availability" icon={<IconServerBolt className="text-purple-600" />} title="High Availability">
    Deploy across public or private clouds, containers, VMs, or bare metal environments with complete data security and privacy.
  </Card>
</Cards>


# Ingestion (/docs/overview/key-concepts/ingestion)



You can send Log events to Parseable via HTTP POST requests with data as JSON payload. You can use the HTTP output plugins of all the common logging agents like [FluentBit](/docs/ingest-data/logging-agents/fluent-bit), [Vector](/docs/ingest-data/logging-agents/vector), [syslog-ng](/docs/ingest-data/logging-agents/syslog), [LogStash](/docs/ingest-data/logging-agents/logstash), among others to send log events to Parseable.

You can also directly integrate Parseable with your application via [REST API](/docs/api/v1/ingest).

<Callout type="info">
  Parseable supports custom HTTP headers with the following conventions:

  * Headers with the format `X-P-*` are automatically stored as columns in your dataset
  * The `X-P-` prefix is removed when creating the column name
  * Up to 10 custom header fields are supported per request
  * Column names are limited to 100 characters maximum (longer names will be automatically truncated)

  Example: A header `X-P-Environment: production` will create a column named `Environment` with the value `production`.
</Callout>

## Flattening

Nested JSON objects are automatically flattened. For example, the following JSON object

```json
{
  "foo": {
    "bar": "baz"
  }
}
```

will be flattened to

```json
{
  "foo_bar": "baz"
}
```

before it gets stored. While querying, this field should be referred to as foo\_bar. For example, select `foo_bar` from `<dataset-name>`. The flattened field will be available in the schema as well.

## Batching and Compression

Wherever applicable, we recommend enabling the log agent's compression and batching features to reduce network traffic and improve ingestion performance. The maximum payload size in Parseable is 10 MiB (10485760 Bytes). The payload can contain single log event as a JSON object or multiple log events in a JSON array. There is no limit to the number of batched events in a single call.

## Timestamp

Correct time is critical to understand the proper sequence of events. Timestamps are important for debugging, analytics, and deriving transactions. We recommend that you include a timestamp in your log events formatted in RFC3339 format.

Parseable uses the event-received timestamp and adds it to the log event in the field `p_timestamp`. This ensures there is a time reference in the log event, even if the original event doesn't have a timestamp.

## Staging

Staging in Parseable refers to the process of storing log data on locally attached storage before it is pushed to a long term and persistent store like S3 or something similar. Staging acts as a buffer for incoming events and allows a stable approach to pushing events to the persistent store.

Once an HTTP call is received on the Parseable server, events are parsed and converted to Arrow format in memory. This Arrow data is then written to the staging directory (defaults to `$PWD/staging`). Every minute, the server converts the Arrow data to Parquet format and pushes it to the persistent store. We chose a minute as the default interval, so there is a clear boundary between events, and the prefix structure on S3 is predictable.

The query flow in Parseable allows transparent access to the data in the staging directory. This means that the data in the staging directory is queryable in real-time. As a user, you won't see any difference in the data fetched from the staging directory or the persistent store.

The staging directory can be configured using the `P_STAGING_DIR` environment variable, as explained in the environment vars section.

## Planning for Production

When planning for the production deployment of Parseable, the two most important considerations from a staging perspective are:

Storage size: Ensure that the staging area has sufficient capacity to handle the anticipated log volume. This prevents data loss due to disk space exhaustion. To calculate the storage size, consider the average log event size, the expected log volume for 5-10 minutes. This is done as under high loads, the conversion to Parquet and subsequent push to S3 may lag behind.

Local storage redundancy: Data in staging has not been committed to persistent store, it is important to have the staging itself reliable and redundant. This way, the staging data is protected from data loss due to simple disk failures. If using AWS, choose from services like EBS (Elastic Block Store) or EFS (Elastic File System), and mount these volumes on the Parseable server. Similarly, on Azure chose from Managed Disks or Azure Files. If you're using a private cloud, a reliable mounted volume from a NAS or SAN can be used.


# Partitioning (/docs/overview/key-concepts/partitioning)



## Context

Partitioning in databases generally refers to the splitting of data to achieve goals like high availability, scalability, or performance. Sometimes it is also confused with another data-splitting approach called **Sharding**. Sharding means spreading the data based on a shard key onto separate server instances to spread load.

## Partitioning in Parseable

Partitioning is the splitting of log data based on specific columns and value pairs to improve query performance and storage efficiency. The decision to choose specific columns for partitioning is based on the access patterns of the data. By partitioning log data, you can optimize query performance, reduce the amount of data scanned during queries, and improve storage efficiency.

### When should you use partitioning?

Partitioning is useful when you have a clear understanding of the most common data access patterns for a given log dataset. More specifically, when the columns where users are most likely to `filter` or `group by` are well known.

Also, a relatively larger dataset (at least few TBs or more) is better suited for partitioning. For tiny datasets, the overhead of managing partitions might outweigh the benefits.

### Selecting a column for partitioning

The first step is to find which column users are most likely to `filter` or `group by`. Once you have this information, it is important to know the variance in the column values (i.e. the number of unique values in the column). For example, if you have a column `log_level` with only a few unique values like `ERR`, `WARN`, and `INFO`, it would be a good candidate for partitioning. But if there is a column called `log_message` where each log event has a unique message, partitioning on this column will in fact make things worse.

**Important**: In Parseable, you can select only one column per dataset for partitioning.

### How to set up partitioning?

You can specify a single column for partitioning while creating a dataset on the Parseable Console (Create Dataset >> Custom Partition Field). Once the dataset is created, Parseable will automatically create physical partitions based on the values in this column.

You can also edit the partition column for an existing dataset (Dataset >> Manage >> Info >> Custom Partition Field). Note that this will have effect on all the new data that is ingested into the dataset, and not the existing data.

### How does partitioning work?

When a dataset is created with partitioning enabled, Parseable will create physical partitions based on the values in the specified column. For example, if you have a column `log_level` with the values `ERR`, `WARN`, and `INFO`, Parseable will create three physical partitions, one for each value.

When a query is run with a filter on `log_level`, Parseable will only scan the relevant partition(s) and not the entire dataset. This significantly reduces the amount of data scanned during queries and improves query performance.

Let's understand this better with an example. Let's say you have log events with columns `timestamp`, `log_level`, `service_name`, `log_message` and `os`. If one of the most common data query patterns is to filter events by `log_level` (i.e., most queries are of the form `select * from logs where log_level = '...'`), then you should consider partitioning by the `log_level` column.

Physically on the storage (S3 bucket or disk), you'll see the data organized by the partition column values. For example, if you have partitioning on `log_level`, you'll see the data organized like this:

```sql
  log_level=ERR
  log_level=WARN
  log_level=INFO
```

If you frequently filter by both `log_level` and another column like `os`, you'll need to decide which one provides the most query benefit as your partition column, since only one column can be used for partitioning.

### Partitioning best practices

* **Choose the right column:** Choose the column that is most frequently used in query filters.

* **Understand the data distribution:** Ensure that the column you choose has a good distribution of values with relatively low cardinality (few unique values).

* **Avoid high cardinality columns:** Partitioning on a column with high cardinality (i.e., many unique values) can lead to too many small partitions, which is inefficient.

* **Consider query patterns:** Select a partition column that aligns with your most common query filters.

* **Monitor and adjust:** Monitor the query performance and adjust the partition column as needed if query patterns change.


# Query (/docs/overview/key-concepts/query)



Parseable uses [Apache DataFusion](https://datafusion.apache.org/) as its query engine, providing PostgreSQL-compatible SQL for telemetry data analysis.

## How It Works

1. Query is parsed and an execution plan is created
2. Data manifest file filters relevant [Parquet](https://parquet.apache.org/) files based on column metadata and time range
3. DataFusion reads only the required data via S3 `GetRange` API
4. Results are returned with minimal I/O and cost

## Supported Functions

Parseable supports all DataFusion SQL functions:

* [Aggregate Functions](https://datafusion.apache.org/user-guide/sql/aggregate_functions.html) - COUNT, SUM, AVG, etc.
* [Window Functions](https://datafusion.apache.org/user-guide/sql/window_functions.html) - ROW\_NUMBER, RANK, etc.
* [Scalar Functions](https://datafusion.apache.org/user-guide/sql/scalar_functions.html) - String, Math, Date/Time, etc.

## Key Capabilities

| Feature              | Description                                                |
| -------------------- | ---------------------------------------------------------- |
| PostgreSQL syntax    | Familiar SQL with regex operators (`~`, `~*`, `!~`, `!~*`) |
| Query analysis       | `EXPLAIN ANALYZE` for performance insights                 |
| Time-range filtering | Efficient filtering via `p_timestamp`                      |
| AI query builder     | Natural language to SQL (Enterprise)                       |

***

**References:**

* [SQL Editor User Guide](/docs/user-guide/sql-editor) - Query examples and usage
* [Text to SQL](/docs/user-guide/ai-native/text-to-sql) - AI-powered query generation
* [Query API](/docs/api) - REST API documentation


# Storage (/docs/overview/key-concepts/storage)



### Overview

Parseable is object store–first: every byte that flows through the platform is persisted in inexpensive, infinitely scalable commodity storage such as Amazon S3, Google Cloud Storage, Azure Blob, or any S3‑compatible service (MinIO, Wasabi, DigitalOcean Spaces, etc.).

We lean on two community crates:

`objectstore` – a vendor‑agnostic Rust SDK that abstracts away the quirks of each provider (authentication, region handling, presigned URLs, retry semantics).

`limitstore` – a thin wrapper that throttles concurrent calls so we never overwhelm the remote API or your network egress budget.

Together they give us uniform APIs, predictable throughput, and consistent error handling across clouds.


# Installation (/docs/self-hosted/installation)



Parseable is available in two variants: Distributed and Standalone. Each variant is tailored to meet different deployment needs, from small-scale testing environments to large-scale production systems.

While distributed deployment is recommended for production use, the standalone variant is ideal for quick setup and testing.

## Distributed

<Callout type="info">
  Parseable distributed cluster is recommended for production grade deployment. It requires an object store as persistent storage.
</Callout>

In a Distributed deployment, multiple Ingestion nodes work together to ingest data, allowing for better scalability and load distribution. This setup supports ingestion from either a single high-volume data source or multiple independent sources, making it the recommended choice for handling large data streams efficiently.

* [Kubernetes](/docs/self-hosted/installation/distributed/k8s-helm)
* [Docker Compose](/docs/self-hosted/installation/distributed/docker-compose)
* [Bare Metal and VMs](/docs/self-hosted/installation/distributed/linux)

## Standalone

<Callout type="info">
  Parseable standalone server can be run with local store argument to use the disk attached on the machine as store. This is not recommended for production deployments.
</Callout>

The Standalone variant of the Parseable Observability Platform is designed for quick value realization, making it ideal for hobbyists and first-time users. In this mode Parseable operates with a single ingestion node, handling all data ingestion from various data sources. This setup is ideal for smaller workloads or testing environments where high availability and horizontal scaling are not primary concerns.

* [Kubernetes](/docs/self-hosted/installation/standalone/k8s)
* [Docker](/docs/self-hosted/installation/standalone/docker)
* [Bare Metal and VMs](/docs/self-hosted/installation/standalone/linux)


# AWS S3 (/docs/self-hosted/storage-targets/aws-s3)



Configure AWS S3 as the storage backend for Parseable to store and query your observability data.

## Overview

Using AWS S3 with Parseable provides:

* **Scalable Storage** - Virtually unlimited storage capacity
* **Cost Effective** - Pay only for what you use
* **Durability** - 99.999999999% (11 9's) durability
* **Integration** - Native AWS ecosystem integration

## Prerequisites

* AWS account with S3 access
* S3 bucket created for Parseable data (must be fully empty for new clusters)
* AWS credentials with S3 read/write permissions
* For optimum performance, ensure the S3 bucket is in the same region as your compute instances

### IAM Permissions

Create an IAM policy with the required S3 permissions:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject",
        "s3:ListBucket",
        "s3:GetBucketLocation"
      ],
      "Resource": [
        "arn:aws:s3:::your-parseable-bucket",
        "arn:aws:s3:::your-parseable-bucket/*"
      ]
    }
  ]
}
```

## Parseable Configuration

### Environment Variables

Configure Parseable to use S3 storage:

```bash
# S3 Storage Configuration
P_S3_URL=https://s3.us-east-1.amazonaws.com
P_S3_BUCKET=your-parseable-bucket
P_S3_REGION=us-east-1
P_S3_ACCESS_KEY=your-access-key
P_S3_SECRET_KEY=your-secret-key

# Optional: S3 path prefix
P_S3_PATH_PREFIX=parseable-data/
```

### Docker Compose

```yaml
version: '3.8'
services:
  parseable:
    image: parseable/parseable:latest
    ports:
      - "8000:8000"
    environment:
      - P_S3_URL=https://s3.us-east-1.amazonaws.com
      - P_S3_BUCKET=your-parseable-bucket
      - P_S3_REGION=us-east-1
      - P_S3_ACCESS_KEY=${AWS_ACCESS_KEY_ID}
      - P_S3_SECRET_KEY=${AWS_SECRET_ACCESS_KEY}
      - P_USERNAME=admin
      - P_PASSWORD=admin
    command: ["parseable", "s3-store"]
```

### Instance Metadata Service (IMDS)

For Parseable instances running on EC2, AWS credentials can be sourced from the Instance Metadata Service (IMDS), avoiding the need for explicit access keys:

* Ensure that `Instance Metadata Service (IMDS)` is enabled when creating the EC2 instance (under Advanced details section)
* Select the Metadata version to `V1` and `V2` (token optional)
* Set `P_AWS_IMDSV1_FALLBACK` to true if you want to use the V1 method
* Use `P_AWS_METADATA_ENDPOINT` to specify a custom endpoint URL if needed

Refer to the [AWS metadata service docs](https://docs.aws.amazon.com/sdkref/latest/guide/feature-imds-credentials.html) for more details.

### Kubernetes with IRSA

Use IAM Roles for Service Accounts (IRSA) for secure authentication:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: parseable
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::123456789012:role/ParseableS3Role
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: parseable
spec:
  template:
    spec:
      serviceAccountName: parseable
      containers:
        - name: parseable
          image: parseable/parseable:latest
          env:
            - name: P_S3_URL
              value: "https://s3.us-east-1.amazonaws.com"
            - name: P_S3_BUCKET
              value: "your-parseable-bucket"
            - name: P_S3_REGION
              value: "us-east-1"
          args: ["parseable", "s3-store"]
```

## S3 Bucket Configuration

### Bucket Policy (Optional)

Restrict bucket access to specific IAM roles:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:role/ParseableS3Role"
      },
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::your-parseable-bucket",
        "arn:aws:s3:::your-parseable-bucket/*"
      ]
    }
  ]
}
```

### Lifecycle Rules

Configure lifecycle rules for cost optimization:

```json
{
  "Rules": [
    {
      "ID": "TransitionToIA",
      "Status": "Enabled",
      "Filter": {
        "Prefix": "parseable-data/"
      },
      "Transitions": [
        {
          "Days": 30,
          "StorageClass": "STANDARD_IA"
        },
        {
          "Days": 90,
          "StorageClass": "GLACIER"
        }
      ]
    }
  ]
}
```

### Server-Side Encryption

Enable default encryption on the bucket:

```bash
aws s3api put-bucket-encryption \
  --bucket your-parseable-bucket \
  --server-side-encryption-configuration '{
    "Rules": [
      {
        "ApplyServerSideEncryptionByDefault": {
          "SSEAlgorithm": "aws:kms",
          "KMSMasterKeyID": "your-kms-key-id"
        }
      }
    ]
  }'
```

### SSE-C (Customer-Provided Keys)

Parseable supports [server-side encryption with customer-provided keys (SSE-C)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html). With SSE-C, you store your data encrypted with your own encryption keys while Amazon S3 manages encryption/decryption transparently.

<Callout type="info">
  SSE-C requires HTTPS. Amazon S3 will reject requests made over HTTP when using SSE-C.
</Callout>

Generate a 256-bit AES key and Base64 encode it:

```bash
ENCRYPTION_KEY=$(openssl rand -base64 32)
echo "Encryption Key: $ENCRYPTION_KEY"
```

Add the Base64 encoded encryption key to the environment variable:

```bash
P_S3_SSEC_ENCRYPTION_KEY=SSE-C:AES256:$ENCRYPTION_KEY
```

For distributed deployments, set `P_S3_SSEC_ENCRYPTION_KEY` on both Query and Ingestor nodes.

<Callout type="warn">
  If you lose the encryption key, you'll lose access to the log data. We recommend secure storage such as [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/).
</Callout>

## Configuration Options

| Parameter          | Description                    |
| ------------------ | ------------------------------ |
| `P_S3_URL`         | S3 endpoint URL                |
| `P_S3_BUCKET`      | S3 bucket name                 |
| `P_S3_REGION`      | AWS region                     |
| `P_S3_ACCESS_KEY`  | AWS access key ID              |
| `P_S3_SECRET_KEY`  | AWS secret access key          |
| `P_S3_PATH_PREFIX` | Optional path prefix in bucket |

## S3-Compatible Storage

Parseable also works with S3-compatible storage providers:

### MinIO

```bash
P_S3_URL=http://minio:9000
P_S3_BUCKET=parseable
P_S3_REGION=us-east-1
P_S3_ACCESS_KEY=minioadmin
P_S3_SECRET_KEY=minioadmin
```

### DigitalOcean Spaces

```bash
P_S3_URL=https://nyc3.digitaloceanspaces.com
P_S3_BUCKET=your-space-name
P_S3_REGION=nyc3
P_S3_ACCESS_KEY=your-spaces-key
P_S3_SECRET_KEY=your-spaces-secret
```

### Cloudflare R2

```bash
P_S3_URL=https://account-id.r2.cloudflarestorage.com
P_S3_BUCKET=your-bucket
P_S3_REGION=auto
P_S3_ACCESS_KEY=your-r2-access-key
P_S3_SECRET_KEY=your-r2-secret-key
```

## Best Practices

1. **Use IRSA in EKS** - Avoid hardcoding credentials
2. **Enable Encryption** - Use SSE-S3 or SSE-KMS
3. **Configure Lifecycle Rules** - Optimize storage costs
4. **Use VPC Endpoints** - Reduce data transfer costs
5. **Enable Versioning** - Protect against accidental deletion
6. **Monitor Costs** - Set up billing alerts

## Troubleshooting

### Access Denied Errors

1. Verify IAM permissions are correct
2. Check bucket policy allows access
3. Verify credentials are not expired
4. Check bucket region matches configuration

### Connection Issues

1. Verify S3 endpoint URL is correct
2. Check network connectivity to S3
3. Verify VPC endpoints if using private networking
4. Check security group rules

### Performance Issues

1. Use S3 Transfer Acceleration for global access
2. Consider using S3 Express One Zone for low latency
3. Optimize object sizes for your workload

## Next Steps

* Configure [CloudWatch integration](/docs/ingest-data/cloud/aws-cloudwatch) for AWS logs
* Set up [alerts](/docs/user-guide/alerting) for storage metrics
* Create [dashboards](/docs/user-guide/dashboards) for monitoring


# Azure Blob Storage (/docs/self-hosted/storage-targets/azure-blob-storage)



Configure Azure Blob Storage as the storage backend for Parseable.

## Overview

Using Azure Blob Storage with Parseable provides:

* **Scalable Storage** - Virtually unlimited capacity
* **Cost Effective** - Multiple storage tiers
* **Durability** - Geo-redundant storage options
* **Azure Integration** - Native Azure ecosystem support

## Prerequisites

* Azure subscription
* Storage account created
* Container for Parseable data
* Access credentials or managed identity

## Parseable Configuration

### Environment Variables

```bash
# Azure Blob Storage Configuration
P_BLOB_URL=https://youraccount.blob.core.windows.net
P_BLOB_CONTAINER=parseable-data
P_BLOB_ACCOUNT=yourstorageaccount
P_BLOB_ACCESS_KEY=your-access-key

# Or use connection string
P_BLOB_CONNECTION_STRING=DefaultEndpointsProtocol=https;AccountName=...
```

### Docker Compose

```yaml
version: '3.8'
services:
  parseable:
    image: parseable/parseable:latest
    ports:
      - "8000:8000"
    environment:
      - P_BLOB_URL=https://youraccount.blob.core.windows.net
      - P_BLOB_CONTAINER=parseable-data
      - P_BLOB_ACCOUNT=${AZURE_STORAGE_ACCOUNT}
      - P_BLOB_ACCESS_KEY=${AZURE_STORAGE_KEY}
      - P_USERNAME=admin
      - P_PASSWORD=admin
    command: ["parseable", "blob-store"]
```

### Kubernetes with Managed Identity

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: parseable
  annotations:
    azure.workload.identity/client-id: your-client-id
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: parseable
spec:
  template:
    metadata:
      labels:
        azure.workload.identity/use: "true"
    spec:
      serviceAccountName: parseable
      containers:
        - name: parseable
          image: parseable/parseable:latest
          env:
            - name: P_BLOB_URL
              value: "https://youraccount.blob.core.windows.net"
            - name: P_BLOB_CONTAINER
              value: "parseable-data"
          args: ["parseable", "blob-store"]
```

## Storage Account Setup

### Create Storage Account

```bash
# Create resource group
az group create --name parseable-rg --location eastus

# Create storage account
az storage account create \
  --name parseablestorage \
  --resource-group parseable-rg \
  --location eastus \
  --sku Standard_LRS \
  --kind StorageV2

# Create container
az storage container create \
  --name parseable-data \
  --account-name parseablestorage
```

### Access Control

Grant access using RBAC:

```bash
# Assign Storage Blob Data Contributor role
az role assignment create \
  --role "Storage Blob Data Contributor" \
  --assignee your-principal-id \
  --scope /subscriptions/.../resourceGroups/parseable-rg/providers/Microsoft.Storage/storageAccounts/parseablestorage
```

## Storage Tiers

Configure lifecycle management for cost optimization:

```json
{
  "rules": [
    {
      "name": "MoveToCool",
      "type": "Lifecycle",
      "definition": {
        "filters": {
          "blobTypes": ["blockBlob"],
          "prefixMatch": ["parseable-data/"]
        },
        "actions": {
          "baseBlob": {
            "tierToCool": { "daysAfterModificationGreaterThan": 30 },
            "tierToArchive": { "daysAfterModificationGreaterThan": 90 }
          }
        }
      }
    }
  ]
}
```

## Configuration Options

| Parameter                  | Description                |
| -------------------------- | -------------------------- |
| `P_BLOB_URL`               | Blob storage endpoint URL  |
| `P_BLOB_CONTAINER`         | Container name             |
| `P_BLOB_ACCOUNT`           | Storage account name       |
| `P_BLOB_ACCESS_KEY`        | Storage account access key |
| `P_BLOB_CONNECTION_STRING` | Full connection string     |

## Best Practices

1. **Use Managed Identity** - Avoid storing credentials
2. **Enable Soft Delete** - Protect against accidental deletion
3. **Configure Lifecycle** - Optimize storage costs
4. **Use Private Endpoints** - Secure network access
5. **Enable Versioning** - Track changes

## Troubleshooting

### Access Denied

1. Verify credentials are correct
2. Check RBAC permissions
3. Verify container exists
4. Check network rules

### Performance Issues

1. Use Premium storage for high throughput
2. Enable hierarchical namespace
3. Check network latency

## Next Steps

* Configure [Azure Event Hubs](/docs/ingest-data/cloud/azure-event-hubs) for streaming
* Set up [alerts](/docs/user-guide/alerting) for storage metrics
* Create [dashboards](/docs/user-guide/dashboards) for monitoring


# DigitalOcean Spaces (/docs/self-hosted/storage-targets/digitalocean-spaces)



Configure DigitalOcean Spaces as the storage backend for Parseable.

## Overview

Using DigitalOcean Spaces with Parseable provides:

* **S3 Compatible** - Works with S3-compatible tools
* **Cost Effective** - Simple, predictable pricing
* **CDN Included** - Built-in content delivery
* **Easy Setup** - Simple configuration

## Prerequisites

* DigitalOcean account
* Spaces bucket created
* Spaces access keys
* Parseable instance

## Parseable Configuration

### Environment Variables

```bash
# DigitalOcean Spaces Configuration
P_S3_URL=https://nyc3.digitaloceanspaces.com
P_S3_BUCKET=parseable-data
P_S3_REGION=nyc3
P_S3_ACCESS_KEY=your-spaces-key
P_S3_SECRET_KEY=your-spaces-secret
```

### Docker Compose

```yaml
version: '3.8'
services:
  parseable:
    image: parseable/parseable:latest
    ports:
      - "8000:8000"
    environment:
      - P_S3_URL=https://nyc3.digitaloceanspaces.com
      - P_S3_BUCKET=parseable-data
      - P_S3_REGION=nyc3
      - P_S3_ACCESS_KEY=${DO_SPACES_KEY}
      - P_S3_SECRET_KEY=${DO_SPACES_SECRET}
      - P_USERNAME=admin
      - P_PASSWORD=admin
    command: ["parseable", "s3-store"]
```

## Spaces Setup

### Create Space

1. Go to **Spaces** in DigitalOcean console
2. Click **Create a Space**
3. Choose datacenter region
4. Name your Space (e.g., `parseable-data`)
5. Choose file listing permissions
6. Click **Create a Space**

### Generate Access Keys

1. Go to **API** → **Spaces Keys**
2. Click **Generate New Key**
3. Name your key
4. Copy the Key and Secret

## Available Regions

| Region | Endpoint                              |
| ------ | ------------------------------------- |
| NYC3   | `https://nyc3.digitaloceanspaces.com` |
| SFO3   | `https://sfo3.digitaloceanspaces.com` |
| AMS3   | `https://ams3.digitaloceanspaces.com` |
| SGP1   | `https://sgp1.digitaloceanspaces.com` |
| FRA1   | `https://fra1.digitaloceanspaces.com` |

## Configuration Options

| Parameter         | Description         |
| ----------------- | ------------------- |
| `P_S3_URL`        | Spaces endpoint URL |
| `P_S3_BUCKET`     | Space name          |
| `P_S3_REGION`     | Datacenter region   |
| `P_S3_ACCESS_KEY` | Spaces access key   |
| `P_S3_SECRET_KEY` | Spaces secret key   |

## Lifecycle Rules

Configure lifecycle rules via s3cmd or API:

```bash
# Install s3cmd
pip install s3cmd

# Configure s3cmd
s3cmd --configure

# Set lifecycle policy
s3cmd setlifecycle lifecycle.xml s3://parseable-data
```

### Lifecycle XML

```xml
<LifecycleConfiguration>
  <Rule>
    <ID>MoveToInfrequentAccess</ID>
    <Status>Enabled</Status>
    <Transition>
      <Days>30</Days>
      <StorageClass>GLACIER</StorageClass>
    </Transition>
  </Rule>
</LifecycleConfiguration>
```

## Best Practices

1. **Choose Nearest Region** - Reduce latency
2. **Enable CDN** - For read-heavy workloads
3. **Use CORS** - If accessing from browsers
4. **Monitor Usage** - Track storage and bandwidth
5. **Secure Keys** - Use environment variables

## Troubleshooting

### Access Denied

1. Verify access keys are correct
2. Check Space permissions
3. Verify endpoint URL matches region
4. Check key hasn't been revoked

### Connection Issues

1. Verify network connectivity
2. Check firewall rules
3. Verify endpoint URL format

## Next Steps

* Set up [alerts](/docs/user-guide/alerting) for storage metrics
* Create [dashboards](/docs/user-guide/dashboards) for monitoring
* Configure [AWS S3](/docs/self-hosted/storage-targets/aws-s3) as alternative


# Google Cloud Storage (/docs/self-hosted/storage-targets/gcp-storage)



Configure Google Cloud Storage (GCS) as the storage backend for Parseable.

## Overview

Using GCS with Parseable provides:

* **Scalable Storage** - Virtually unlimited capacity
* **Cost Effective** - Multiple storage classes
* **Durability** - 99.999999999% durability
* **GCP Integration** - Native Google Cloud support

## Prerequisites

* Google Cloud project
* GCS bucket created
* Service account with Storage permissions
* Parseable instance

## Parseable Configuration

### Environment Variables

```bash
# GCS Configuration
P_GCS_URL=https://storage.googleapis.com
P_GCS_BUCKET=parseable-data
P_GCS_REGION=us-central1

# Service account key (if not using workload identity)
GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json
```

### Docker Compose

```yaml
version: '3.8'
services:
  parseable:
    image: parseable/parseable:latest
    ports:
      - "8000:8000"
    environment:
      - P_GCS_URL=https://storage.googleapis.com
      - P_GCS_BUCKET=parseable-data
      - P_GCS_REGION=us-central1
      - P_USERNAME=admin
      - P_PASSWORD=admin
    volumes:
      - ./service-account.json:/etc/gcp/key.json
    command: ["parseable", "gcs-store"]
```

### Kubernetes with Workload Identity

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: parseable
  annotations:
    iam.gke.io/gcp-service-account: parseable@project.iam.gserviceaccount.com
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: parseable
spec:
  template:
    spec:
      serviceAccountName: parseable
      containers:
        - name: parseable
          image: parseable/parseable:latest
          env:
            - name: P_GCS_URL
              value: "https://storage.googleapis.com"
            - name: P_GCS_BUCKET
              value: "parseable-data"
          args: ["parseable", "gcs-store"]
```

## GCS Bucket Setup

### Create Bucket

```bash
# Create bucket
gsutil mb -l us-central1 gs://parseable-data

# Set lifecycle policy
gsutil lifecycle set lifecycle.json gs://parseable-data
```

### Lifecycle Policy

```json
{
  "rule": [
    {
      "action": {"type": "SetStorageClass", "storageClass": "NEARLINE"},
      "condition": {"age": 30}
    },
    {
      "action": {"type": "SetStorageClass", "storageClass": "COLDLINE"},
      "condition": {"age": 90}
    },
    {
      "action": {"type": "SetStorageClass", "storageClass": "ARCHIVE"},
      "condition": {"age": 365}
    }
  ]
}
```

### IAM Permissions

```bash
# Create service account
gcloud iam service-accounts create parseable \
  --display-name="Parseable Storage"

# Grant Storage Object Admin
gsutil iam ch \
  serviceAccount:parseable@project.iam.gserviceaccount.com:objectAdmin \
  gs://parseable-data
```

## Configuration Options

| Parameter      | Description      |
| -------------- | ---------------- |
| `P_GCS_URL`    | GCS endpoint URL |
| `P_GCS_BUCKET` | Bucket name      |
| `P_GCS_REGION` | Bucket region    |

## Storage Classes

| Class    | Use Case            | Retrieval Cost |
| -------- | ------------------- | -------------- |
| Standard | Frequently accessed | None           |
| Nearline | Monthly access      | Low            |
| Coldline | Quarterly access    | Medium         |
| Archive  | Yearly access       | High           |

## Best Practices

1. **Use Workload Identity** - Avoid service account keys
2. **Configure Lifecycle** - Optimize storage costs
3. **Enable Versioning** - Protect against deletion
4. **Use Uniform Access** - Simplify permissions
5. **Set Retention Policies** - Compliance requirements

## Troubleshooting

### Access Denied

1. Verify service account permissions
2. Check bucket IAM policy
3. Verify workload identity binding
4. Check project permissions

### Performance Issues

1. Use regional buckets for low latency
2. Enable parallel uploads
3. Check network configuration

## Next Steps

* Configure [GCP Pub/Sub](/docs/ingest-data/cloud/gcp-pubsub) for streaming
* Set up [alerts](/docs/user-guide/alerting) for storage metrics
* Create [dashboards](/docs/user-guide/dashboards) for monitoring


# Auto instrumentation guide (/docs/user-guide/agent-observability/auto-instrumentation)



In this page we cover how to set up auto instrumentation of LLM calls using OpenTelemetry. This is the recommended approach for most users as it requires minimal code changes and provides rich trace data out of the box. If you need more control, you can also use manual instrumentation with the OpenTelemetry SDK.

## Auto instrumentation with OpenAI SDK

If you are using the OpenAI Python SDK, the official OpenTelemetry distro can instrument all LLM calls with zero code changes.

**1. Install dependencies**

```bash
pip install opentelemetry-distro opentelemetry-exporter-otlp
opentelemetry-bootstrap -a install
```

**2. Set environment variables**

```bash
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
export OTEL_SERVICE_NAME=my-agent
export OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT=true
export OTEL_TRACES_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
```

**3. Run your application with the auto-instrumentation wrapper**

```bash
opentelemetry-instrument python my_agent.py
```

That is it. Every `openai.chat.completions.create()` call will emit `gen_ai.*` spans automatically.

## Auto instrumentation with other SDKs

For broader provider support (Anthropic, Cohere, Mistral, Bedrock, VertexAI, and more), use OpenLLMetry (Traceloop SDK) or OpenLIT. These require only two lines of code added to your application entry point.

**Option 1: OpenLLMetry (Traceloop SDK)**

```bash
pip install traceloop-sdk
```

```python
from traceloop.sdk import Traceloop

Traceloop.init()  # Call once at application startup
```

**Option 2: OpenLIT**

```bash
pip install openlit
```

```python
import openlit

openlit.init()  # Call once at application startup
```

Both libraries auto-patch supported LLM client libraries and emit standard `gen_ai.*` OTel spans. Configure the OTLP exporter endpoint using the same environment variables shown in Path A.

## Verify data ingestion

Once your application is running, verify that trace data is arriving in Parseable:

```sql
SELECT COUNT(*) AS span_count,
       MIN(p_timestamp) AS first_seen,
       MAX(p_timestamp) AS last_seen
FROM "genai-traces"
WHERE p_timestamp > NOW() - INTERVAL '1 hour';
```

If `span_count` is greater than zero, your LLM call instrumentation is working.

## Next steps

Explore the [Schema Reference](/docs/user-guide/agent-observability/schema-reference) and [SQL Query Templates](/docs/user-guide/agent-observability/sql-queries) to start querying your data.


# Agent Observability (/docs/user-guide/agent-observability)











import { IconRocket, IconDatabase, IconCode, IconTerminal2 } from '@tabler/icons-react';

<OfferingPills pro enterprise className="mb-4" />

AI agents interact with LLMs, tools, and API - all in one workflow. In essence, agents are complex distributed applications, and require end-to-end visibility across all systems for effective observability.

Take for example a customer support agent that uses a vector database for knowledge retrieval, an LLM for response generation, and a third-party API for order management.

If the agent produces an incorrect response, you need to know whether the issue was with the knowledge retrieval, the LLM generation, or the API call. Furthermore, if the issue was with say the vector database responding slowly, you want to know why the vector database was slow - was it a CPU bottleneck, memory pressure, or something else.

## Agent observability with Parseable

Parseable enables agent observability using zero SDK, OTel native instrumentation. Instead of proprietary SDKs and formats, Parseable ingests standard OpenTelemetry `gen_ai.*` semantic convention traces and correlates logs.

<img alt="Agent observability dashboard showing invocations, token usage, cost tracking, and tool breakdown" src={__img0} placeholder="blur" />

## Key differentiators

### Unified waterfall view

With Parseable you can see every operation in an agent's workflow: the problem statement, each LLM call with full conversation content, each tool execution with input/output, and the agent completion summary. All correlated via `trace_id`.

<img alt="Session detail showing the agent waterfall with LLM calls, tool executions, token counts, and AI responses" src={__img1} placeholder="blur" />

### Session drill down

Browse all agent sessions with prompts, instructions, models, and status. Filter by agent, time range, or tags to find exactly the sessions you need.

<img alt="Sessions drill-down showing agent sessions with trace IDs, prompts, instructions, and models" src={__img2} placeholder="blur" />

### Server side cost enrichment

Parseable automatically computes `p_genai_cost_usd`, `p_genai_tokens_total`, `p_genai_tokens_per_sec`, and `p_genai_duration_ms` at ingest time, so you never need client-side cost tracking.

### Security and PII detection

Automatically detect PII leaks in agent sessions — credit card numbers, SSNs, addresses, and more — with risk levels and regulatory impact flags.

<img alt="Security tab showing PII leak detection with risk levels and regulatory impact" src={__img3} placeholder="blur" />

### SQL querying

Run standard SQL directly on your agent traces and logs. No proprietary query language, no dashboards only access. Slice and dice your agent data any way you want, and join with your own datasets for deeper analysis.

### Open standards for extensibility

No vendor lock-in. Deploy on your own infrastructure, retain full ownership of your data, and integrate with the OTel ecosystem you already use.

## Instrumentation paths

### Path A: Auto instrumentation with OpenAI SDK

In this approach, you get zero code change, auto instrumentation of all LLM calls, including conversation content, token counts, and latency. This is the fastest way to get LLM call traces flowing into Parseable, and is ideal if you are using the OpenAI Python SDK.

Refer the [OpenAI SDK quickstart guide](/docs/user-guide/agent-observability/auto-instrumentation#auto-instrumentation-with-openai-sdk) for detailed instructions on setting up auto instrumentation with the OpenAI Python SDK.

### Path B: Auto instrumentation with other SDKs

For broader provider support (Anthropic, Cohere, Mistral, Bedrock, VertexAI, and more), use OpenLLMetry (Traceloop SDK) or OpenLIT. These require only two lines of code added to your application entry point.

Refer to the [Other SDKs quickstart guide](/docs/user-guide/agent-observability/auto-instrumentation#auto-instrumentation-with-other-sdks) for detailed instructions on setting up auto instrumentation with OpenLLMetry or OpenLIT.

### Path C: Manual instrumentation using OTel SDK

For maximum control, you can manually create spans with `gen_ai.*` attributes using the OpenTelemetry SDK directly.
This requires more code changes, but allows you to instrument any provider or custom LLM client, and to add custom attributes as needed.

Manual instrumentation is also necessary for:

1. **Agent-level spans** — `invoke_agent` spans that wrap the entire agent loop are not created by auto-instrumentors
2. **Tool execution spans** — `execute_tool` spans for tool/command execution are application-specific
3. **Thinking/reasoning blocks** — Claude's `thinking_blocks` and DeepSeek's `reasoning_content` are provider-specific extensions not captured by auto-instrumentors
4. **Full control** — manual instrumentation gives you exact control over what attributes are set, what content is captured, and how spans are structured

Typically manual instrumentation replaces auto-instrumentation entirely (disable auto with `OTEL_PYTHON_DISABLED_INSTRUMENTATIONS=openai_v2`).

Refer the [manual instrumentation guide](/docs/user-guide/agent-observability/manual-instrumentation) for detailed instructions on how to structure spans and what attributes to capture for complete agent observability.

## Language support matrix

| Language   | Path A: OpenAI SDK | Path B: Other providers SDK | Path C: OTEL SDK |
| ---------- | ------------------ | --------------------------- | ---------------- |
| Python     | Yes                | Yes (Traceloop, OpenLIT)    | Yes              |
| TypeScript | Yes                | Yes (Traceloop)             | Yes              |
| Java       | No                 | No                          | Yes              |
| Go         | No                 | No                          | Yes              |
| .NET       | No                 | No                          | Yes              |

***

## Collector configuration

After the instrumentation is set up in your application, configure how telemetry data is sent to Parseable. We recommend using an OpenTelemetry Collector for buffering, batching, and reliability, but you can also export directly from your application for simpler setups.

### OTel Collector (Recommended)

Deploy an OpenTelemetry Collector between your application and Parseable for buffering, batching, and reliability. Save the following as `parseable-genai-collector.yaml`:

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

processors:
  batch:
    timeout: 5s
    send_batch_size: 256

exporters:
  otlphttp/parseable:
    endpoint: ${PARSEABLE_URL}
    encoding: json
    headers:
      Authorization: "Basic ${PARSEABLE_AUTH}"
      X-P-Stream: "${STREAM_NAME}"
      X-P-Log-Source: "otel-traces"
      X-P-Dataset-Tag: "agent-observability"

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlphttp/parseable]
```

Run the collector:

```bash
export PARSEABLE_URL=${PARSEABLE_URL}          # e.g. https://ingest.parseable.com
export PARSEABLE_AUTH=${PARSEABLE_AUTH}          # base64(username:password)
export STREAM_NAME=${PARSEABLE_DATASET_NAME}

otelcol-contrib --config parseable-genai-collector.yaml
```

### Direct to Parseable

For simpler setups, you can export traces directly from your application to Parseable by setting OTLP environment variables. No collector process is needed.

```bash
export OTEL_EXPORTER_OTLP_ENDPOINT=${PARSEABLE_URL}
export OTEL_EXPORTER_OTLP_HEADERS="Authorization=Basic ${PARSEABLE_AUTH},X-P-Stream=${PARSEABLE_DATASET_NAME},X-P-Log-Source=otel-traces,X-P-Dataset-Tag=agent-observability"
export OTEL_SERVICE_NAME=my-agent
export OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT=true
```

## Next steps

<Cards>
  <Card href="/docs/user-guide/agent-observability/quickstart" icon={<IconRocket className="text-purple-600" />} title="Quickstart">
    Get LLM call traces flowing into Parseable in under 5 minutes
  </Card>

  <Card href="/docs/user-guide/agent-observability/instrumentation-guide" icon={<IconTerminal2 className="text-purple-600" />} title="Instrumentation Guide">
    Complete reference for instrumenting any GenAI agent with OpenTelemetry traces and correlated logs.
  </Card>

  <Card href="/docs/user-guide/agent-observability/schema-reference" icon={<IconDatabase className="text-purple-600" />} title="Schema Reference">
    Complete column reference for the flattened GenAI trace.
  </Card>

  <Card href="/docs/user-guide/agent-observability/sql-queries" icon={<IconCode className="text-purple-600" />} title="SQL Query Templates">
    Sample SQL queries for common agent observability tasks like.
  </Card>
</Cards>


# Manual instrumentation guide (/docs/user-guide/agent-observability/manual-instrumentation)



This page is reference manual on how to manually instrument your agent with OTel spans and logs. If you are looking for a quick way to get LLM call traces flowing into Parseable, refer to the [Quickstart guide](/docs/user-guide/agent-observability/quickstart) which uses auto-instrumentation or two-line SDK initialization.

## Instrumentation overview

For each agent run, you want to capture:

| What                                                                                             | Where it goes                                                                | Why                                                       |
| ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Agent run** — which agent ran, total tokens, total cost, exit status                           | OTel **`invoke_agent` span**                                                 | End-to-end agent observability, run-level dashboards      |
| **LLM call metadata** — model name, token counts, latency, temperature, finish reason, errors    | OTel **`chat` span**                                                         | Per-call dashboards, aggregation, alerting, cost tracking |
| **Full conversation content** — system prompts, user messages, assistant responses, tool results | OTel **log records** (correlated to `chat` spans)                            | Conversation reconstruction, debugging, quality analysis  |
| **Tool calls** — which tools the LLM called, with full arguments                                 | OTel **log records** (correlated to `chat` spans) + **`execute_tool` spans** | Tool usage analytics, debugging                           |
| **Thinking/reasoning** — Claude's chain-of-thought reasoning blocks                              | OTel **log records** (correlated to `chat` spans)                            | Reasoning analysis, debugging                             |

The OpenTelemetry GenAI semantic conventions define how to structure this data. This guide shows exactly how to implement it.

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│  Your Agent Application (Python)                        │
│                                                         │
│  ┌──────────────────────────────────────────────────┐   │
│  │ opentelemetry-instrument CLI wrapper             │   │
│  │ (auto-configures TracerProvider, LoggerProvider, │   │
│  │  sets up OTLP exporters)                         │   │
│  └──────────────────────────────────────────────────┘   │
│                                                         │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Your code (manual instrumentation):             │    │
│  │  - _tracer.start_as_current_span(...)  → spans  │    │
│  │  - _otel_logger.emit(...)              → logs   │    │
│  └─────────────────────────────────────────────────┘    │
│                    │                                    │
│                    │ OTLP (protobuf)                    │
│                    ▼                                    │
│  ┌─────────────────────────────────────────────────┐    │
│  │ BatchSpanProcessor + BatchLogRecordProcessor    │    │
│  │ (buffers, batches, exports periodically)        │    │
│  └─────────────────────────────────────────────────┘    │
└────────────────────│────────────────────────────────────┘
                     │ OTLP HTTP (:4318) or gRPC (:4317)
                     ▼
┌─────────────────────────────────────────────────────────┐
│  OTel Collector                                         │
│  - Receives traces + logs via OTLP                      │
│  - Batches and exports to backend(s)                    │
│  - Routes traces and logs to separate streams           │
└────────────────────│────────────────────────────────────┘
                     │ OTLP/HTTP (JSON)
                     ▼
┌─────────────────────────────────────────────────────────┐
│  Parseable                                              │
│  - genai-traces stream (flattened spans)                │
│  - genai-logs stream (flattened log records)            │
│  - SQL-queryable, with server-side cost enrichment      │
└─────────────────────────────────────────────────────────┘
```

### What each layer does

| Layer                                            | Responsibility                                                                                                                                                           |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `opentelemetry-instrument` CLI                   | Bootstraps the SDK — creates `TracerProvider`, `LoggerProvider`, configures OTLP exporters. You do not call `set_tracer_provider()` or `set_logger_provider()` manually. |
| Your code (manual instrumentation)               | Creates spans (`_tracer.start_as_current_span(...)`) and emits log records (`_otel_logger.emit(...)`). This is where all GenAI-specific attributes and content are set.  |
| `BatchSpanProcessor` / `BatchLogRecordProcessor` | Accumulates spans and logs in memory, exports them in batches via OTLP. Configured automatically by the CLI.                                                             |
| OTel Collector                                   | Receives OTLP data, applies processors (batching, filtering), and exports to one or more backends. Converts protobuf to JSON for Parseable.                              |
| Parseable                                        | Stores traces and logs as flattened, SQL-queryable records. Enriches with computed columns (`p_genai_cost_usd`, `p_genai_tokens_total`, etc.).                           |

## The opentelemetry-instrument CLI

The `opentelemetry-instrument` CLI is the simplest way to bootstrap the OTel SDK. It is installed as part of the `opentelemetry-distro` package and is the recommended approach for Python applications.

### What It Does

When you run `opentelemetry-instrument python my_agent.py`, the CLI:

1. Creates a `TracerProvider` with a `BatchSpanProcessor` and OTLP exporter
2. Creates a `LoggerProvider` with a `BatchLogRecordProcessor` and OTLP exporter
3. Sets both as the global providers (so `trace.get_tracer()` and `get_logger_provider()` return them)
4. Optionally loads auto-instrumentors for installed libraries (OpenAI, httpx, etc.)
5. Runs your application

### What You Do NOT Do

Because the CLI handles provider setup:

* Do NOT call `set_tracer_provider()` — it's already set
* Do NOT call `set_logger_provider()` — it's already set
* Do NOT create `BatchSpanProcessor` or `OTLPSpanExporter` — already configured
* Do NOT create `BatchLogRecordProcessor` or `OTLPLogExporter` — already configured
* Just call `trace.get_tracer(...)` and `get_logger_provider().get_logger(...)` — they return the pre-configured providers

### Manual Provider Setup (Without CLI)

If you cannot use the CLI (e.g., embedded in a larger application), you can set up providers manually:

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk._logs import LoggerProvider
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.exporter.otlp.proto.http._log_exporter import OTLPLogExporter
from opentelemetry._logs import set_logger_provider

# Traces
tracer_provider = TracerProvider()
tracer_provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter()))
trace.set_tracer_provider(tracer_provider)

# Logs
logger_provider = LoggerProvider()
logger_provider.add_log_record_processor(BatchLogRecordProcessor(OTLPLogExporter()))
set_logger_provider(logger_provider)
```

This is the manual equivalent of what the CLI does. Use the CLI when possible.

## Setup: Packages, Environment, Launch

### Packages

```bash
pip install opentelemetry-distro opentelemetry-exporter-otlp
opentelemetry-bootstrap -a install
```

| Package                              | Purpose                                                                                                                         |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| `opentelemetry-distro`               | Provides `opentelemetry-instrument` CLI and auto-discovery                                                                      |
| `opentelemetry-exporter-otlp`        | OTLP exporter (HTTP/protobuf and gRPC)                                                                                          |
| `opentelemetry-bootstrap -a install` | Installs auto-instrumentors for detected libraries (e.g., `opentelemetry-instrumentation-openai-v2` if OpenAI SDK is installed) |

### Environment Variables

```bash
# Required: where the OTel Collector listens
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318

# Required: OTLP protocol
export OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf

# Required: identifies your application in traces
export OTEL_SERVICE_NAME=my-genai-agent

# Required: disable auto-instrumentor to prevent duplicates
export OTEL_PYTHON_DISABLED_INSTRUMENTATIONS=openai_v2
```

| Variable                                             | Purpose                                                                                                                      | Required                                                        |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| `OTEL_EXPORTER_OTLP_ENDPOINT`                        | Collector address. `4318` for HTTP, `4317` for gRPC.                                                                         | Yes                                                             |
| `OTEL_EXPORTER_OTLP_PROTOCOL`                        | `http/protobuf` (HTTP) or `grpc`                                                                                             | Yes                                                             |
| `OTEL_SERVICE_NAME`                                  | Service name that appears on every span and log record as a resource attribute                                               | Yes                                                             |
| `OTEL_PYTHON_DISABLED_INSTRUMENTATIONS`              | Comma-separated list of auto-instrumentors to skip. Set to `openai_v2` to prevent the OpenAI auto-instrumentor from loading. | Yes (if `opentelemetry-instrumentation-openai-v2` is installed) |
| `OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT` | Controls whether *auto*-instrumentors capture message content. Irrelevant when auto is disabled, but harmless to set.        | No                                                              |

### Launch Command

```bash
opentelemetry-instrument \
    --traces_exporter otlp \
    --logs_exporter otlp \
    --metrics_exporter none \
    python my_agent.py
```

| Flag                 | Value  | Purpose                                                        |
| -------------------- | ------ | -------------------------------------------------------------- |
| `--traces_exporter`  | `otlp` | Export spans via OTLP                                          |
| `--logs_exporter`    | `otlp` | Export log records via OTLP                                    |
| `--metrics_exporter` | `none` | Disable metrics (optional — set to `otlp` if you want metrics) |

The CLI reads `OTEL_EXPORTER_OTLP_ENDPOINT` and `OTEL_EXPORTER_OTLP_PROTOCOL` to configure the exporters.

## Instrumentation Code

This is a complete, agent-agnostic reference for instrumenting any Python application that calls LLM APIs. The instrumentation uses three span types per the [OTel GenAI Agent Spans](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/) spec.

### Module-Level Setup

You need a tracer and logger in the agent orchestration module (for `invoke_agent` and `execute_tool` spans + logs), and a tracer and logger in the LLM call module (for `chat` spans and log records):

**Agent orchestration module** (e.g., `agents.py`):

```python
from opentelemetry import trace
from opentelemetry._logs import get_logger_provider, SeverityNumber

_tracer = trace.get_tracer("my-agent", "1.1.0")
_otel_logger = get_logger_provider().get_logger("my-agent", "1.1.0")
```

**LLM call module** (e.g., `models.py`):

```python
import json
from opentelemetry import trace
from opentelemetry._logs import get_logger_provider, SeverityNumber

_tracer = trace.get_tracer("my-agent.llm", "1.1.0")
_otel_logger = get_logger_provider().get_logger("my-agent.llm", "1.1.0")
```

* The first argument is the **instrumentation scope name**. Use a dotted name that identifies which part of your application is emitting telemetry. Both spans and logs will carry this as `scope_name`.
* The second argument is the **instrumentation scope version**. Bump this when you change what attributes/events you emit.
* `get_logger_provider()` returns the provider already configured by the CLI. Do NOT create your own.

### Instrumenting the Agent Run (invoke\_agent)

Wrap the entire agent loop in an `invoke_agent` span. All `chat` and `execute_tool` spans created inside this context automatically become children via OTel context propagation.

```python
def run_agent(model_name: str, provider: str, problem: str):
    """Example: wrap an agent run with an invoke_agent span."""

    span_name = "invoke_agent my-agent"
    with _tracer.start_as_current_span(span_name, kind=trace.SpanKind.CLIENT) as span:
        span.set_attribute("gen_ai.operation.name", "invoke_agent")
        span.set_attribute("gen_ai.agent.name", "my-agent")
        span.set_attribute("gen_ai.provider.name", provider)
        span.set_attribute("gen_ai.request.model", model_name)

        # ── Emit the problem statement that triggered this agent run ──
        _otel_logger.emit(
            body=problem,
            severity_number=SeverityNumber.INFO,
            event_name="gen_ai.user.message",
            attributes={
                "gen_ai.operation.name": "invoke_agent",
                "gen_ai.provider.name": provider,
                "gen_ai.request.model": model_name,
                "gen_ai.agent.name": "my-agent",
                "gen_ai.event.name": "gen_ai.user.message",
                "role": "user",
            },
        )

        # ── Your agent loop ──
        done = False
        while not done:
            llm_response = call_llm(model_name, messages)    # creates a child "chat" span
            tool_result = execute_tool(llm_response.action)   # creates a child "execute_tool" span
            done = llm_response.is_done

        # ── After loop: set aggregate response attributes ──
        span.set_attribute("gen_ai.usage.input_tokens", total_input_tokens)
        span.set_attribute("gen_ai.usage.output_tokens", total_output_tokens)
        span.set_attribute("gen_ai.response.finish_reasons", json.dumps(["exit_command"]))

        # ── Emit agent completion summary ──
        _otel_logger.emit(
            body=json.dumps({"exit_status": "exit_command",
                             "total_input_tokens": total_input_tokens,
                             "total_output_tokens": total_output_tokens}),
            severity_number=SeverityNumber.INFO,
            event_name="gen_ai.agent.finish",
            attributes={
                "gen_ai.operation.name": "invoke_agent",
                "gen_ai.agent.name": "my-agent",
                "gen_ai.provider.name": provider,
                "gen_ai.request.model": model_name,
                "gen_ai.event.name": "gen_ai.agent.finish",
                "gen_ai.usage.input_tokens": total_input_tokens,
                "gen_ai.usage.output_tokens": total_output_tokens,
            },
        )
```

**Key points:**

* `kind=trace.SpanKind.CLIENT` — the agent is a client of the LLM service
* Token counts on `invoke_agent` are **totals** across all LLM calls in the run
* `gen_ai.agent.name` lives here, NOT on individual `chat` spans
* `gen_ai.provider.name` replaces the older `gen_ai.system` attribute per current spec
* The `gen_ai.user.message` log emits the problem statement so it appears in the trace waterfall
* The `gen_ai.agent.finish` log emits a completion summary with exit status and total token counts

### Instrumenting Tool Execution (execute\_tool)

Wrap each tool/command execution in an `execute_tool` span:

```python
def execute_tool(action: str, tool_call_id: str | None = None):
    """Example: wrap a tool execution with an execute_tool span."""

    tool_name = action.strip().split()[0] if action.strip() else "unknown"
    span_name = f"execute_tool {tool_name}"
    with _tracer.start_as_current_span(span_name, kind=trace.SpanKind.INTERNAL) as span:
        span.set_attribute("gen_ai.operation.name", "execute_tool")
        span.set_attribute("gen_ai.tool.name", tool_name)
        span.set_attribute("gen_ai.tool.type", "function")
        if tool_call_id:
            span.set_attribute("gen_ai.tool.call.id", tool_call_id)

        # Emit tool input log (the command being run)
        _otel_logger.emit(
            body=action,
            severity_number=SeverityNumber.INFO,
            event_name="gen_ai.tool.input",
            attributes={
                "gen_ai.operation.name": "execute_tool",
                "gen_ai.tool.name": tool_name,
                "gen_ai.tool.type": "function",
                "gen_ai.tool.call.id": tool_call_id or "",
                "gen_ai.event.name": "gen_ai.tool.input",
            },
        )

        try:
            result = env.communicate(action)
        except TimeoutError as e:
            span.set_attribute("error.type", type(e).__name__)
            span.set_status(trace.StatusCode.ERROR, "Command timed out")
            raise

        # Emit tool output log (the observation)
        _otel_logger.emit(
            body=result or "",
            severity_number=SeverityNumber.INFO,
            event_name="gen_ai.tool.output",
            attributes={
                "gen_ai.operation.name": "execute_tool",
                "gen_ai.tool.name": tool_name,
                "gen_ai.tool.type": "function",
                "gen_ai.tool.call.id": tool_call_id or "",
                "gen_ai.event.name": "gen_ai.tool.output",
            },
        )

        return result
```

**Key points:**

* `kind=trace.SpanKind.INTERNAL` — tool execution is an internal operation
* `gen_ai.tool.call.id` links this execution back to the LLM's tool call request (from function calling mode)
* Error status is set on timeout or failure, making failed tool executions queryable
* `gen_ai.tool.input` log captures the command sent to the tool
* `gen_ai.tool.output` log captures the tool's observation/result

### Instrumenting an LLM Call (chat)

Wrap your LLM call in a span. Emit log records inside the span context.

```python
def call_llm(model: str, messages: list[dict], temperature: float = 0.0, **kwargs):
    """Example: instrument any LLM call with OTel traces + logs."""

    with _tracer.start_as_current_span(f"chat {model}", kind=trace.SpanKind.CLIENT) as span:

        # ── Step 1: Set request attributes on span ──
        span.set_attribute("gen_ai.operation.name", "chat")
        span.set_attribute("gen_ai.request.model", model)
        span.set_attribute("gen_ai.provider.name", "openai")  # or "anthropic", etc.
        if temperature is not None:
            span.set_attribute("gen_ai.request.temperature", temperature)

        # ── Step 2: Emit input message log records ──
        for msg in messages:
            role = msg.get("role", "user")
            content = msg.get("content", "")
            body = content if isinstance(content, str) else json.dumps(content)
            _otel_logger.emit(
                body=body,
                severity_number=SeverityNumber.INFO,
                event_name=f"gen_ai.{role}.message",
                attributes={
                    "gen_ai.provider.name": "openai",
                    "gen_ai.request.model": model,
                    "gen_ai.event.name": f"gen_ai.{role}.message",
                    "role": role,
                },
            )

        # ── Step 3: Call the LLM ──
        try:
            response = your_llm_client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                **kwargs,
            )
        except Exception as e:
            span.set_status(trace.StatusCode.ERROR, str(e))
            span.set_attribute("error.type", type(e).__name__)
            raise

        # ── Step 4: Set response attributes on span ──
        if response.model:
            span.set_attribute("gen_ai.response.model", response.model)
        if response.id:
            span.set_attribute("gen_ai.response.id", response.id)
        if response.usage:
            span.set_attribute("gen_ai.usage.input_tokens", response.usage.prompt_tokens)
            span.set_attribute("gen_ai.usage.output_tokens", response.usage.completion_tokens)

        # ── Step 5: Emit response log records ──
        finish_reasons = []
        for i, choice in enumerate(response.choices):
            # Choice content
            _otel_logger.emit(
                body=choice.message.content or "",
                severity_number=SeverityNumber.INFO,
                event_name="gen_ai.choice",
                attributes={
                    "gen_ai.provider.name": "openai",
                    "gen_ai.request.model": model,
                    "gen_ai.event.name": "gen_ai.choice",
                    "index": i,
                    "finish_reason": choice.finish_reason or "",
                },
            )
            if choice.finish_reason:
                finish_reasons.append(choice.finish_reason)

            # Tool calls (if present)
            if choice.message.tool_calls:
                tool_call_ids = []
                for tc in choice.message.tool_calls:
                    tc_dict = tc.model_dump() if hasattr(tc, "model_dump") else tc
                    if tc_dict.get("id"):
                        tool_call_ids.append(tc_dict["id"])
                    _otel_logger.emit(
                        body=json.dumps(tc_dict.get("function", tc_dict)),
                        severity_number=SeverityNumber.INFO,
                        event_name="gen_ai.tool.call",
                        attributes={
                            "gen_ai.provider.name": "openai",
                            "gen_ai.request.model": model,
                            "gen_ai.event.name": "gen_ai.tool.call",
                            "gen_ai.tool.name": tc_dict.get("function", {}).get("name", ""),
                            "gen_ai.tool.call.id": tc_dict.get("id", ""),
                        },
                    )

                # Set tool call IDs on the chat span for cross-span correlation
                # with execute_tool spans. Single ID stored as string, multiple
                # IDs JSON-encoded as array.
                if tool_call_ids:
                    span.set_attribute(
                        "gen_ai.tool.call.id",
                        tool_call_ids[0] if len(tool_call_ids) == 1 else json.dumps(tool_call_ids),
                    )

            # Thinking/reasoning blocks (Claude, DeepSeek, etc.)
            thinking_blocks = getattr(choice.message, "thinking_blocks", None)
            if thinking_blocks:
                for tb in thinking_blocks:
                    thinking_text = tb.get("thinking", "") if isinstance(tb, dict) else str(tb)
                    _otel_logger.emit(
                        body=thinking_text,
                        severity_number=SeverityNumber.INFO,
                        event_name="gen_ai.thinking",
                        attributes={
                            "gen_ai.provider.name": "openai",
                            "gen_ai.request.model": model,
                            "gen_ai.event.name": "gen_ai.thinking",
                        },
                    )

        # ── Step 6: Finalize span ──
        if finish_reasons:
            span.set_attribute("gen_ai.response.finish_reasons", json.dumps(finish_reasons))
        span.set_status(trace.StatusCode.OK)

        return response
```

### What Gets Produced Per Agent Run

**Three span types** (in the traces pipeline):

**`invoke_agent` span** — one per agent run:

| Attribute                        | Example                          |
| -------------------------------- | -------------------------------- |
| `span_name`                      | `"invoke_agent my-agent"`        |
| `gen_ai.operation.name`          | `"invoke_agent"`                 |
| `gen_ai.agent.name`              | `"my-agent"`                     |
| `gen_ai.provider.name`           | `"openai"`                       |
| `gen_ai.request.model`           | `"gpt-4o"`                       |
| `gen_ai.usage.input_tokens`      | `45200` (total across all steps) |
| `gen_ai.usage.output_tokens`     | `3800` (total across all steps)  |
| `gen_ai.response.finish_reasons` | `["exit_command"]`               |
| `span_kind`                      | `CLIENT`                         |
| `scope_name`                     | `"my-agent"`                     |
| `service.name`                   | `"my-genai-agent"`               |

**`chat` span** — one per LLM call (child of `invoke_agent`):

| Attribute                        | Example                                                                            |
| -------------------------------- | ---------------------------------------------------------------------------------- |
| `span_name`                      | `"chat gpt-4o"`                                                                    |
| `gen_ai.operation.name`          | `"chat"`                                                                           |
| `gen_ai.request.model`           | `"gpt-4o"`                                                                         |
| `gen_ai.provider.name`           | `"openai"`                                                                         |
| `gen_ai.response.model`          | `"gpt-4o-2024-11-20"`                                                              |
| `gen_ai.response.id`             | `"chatcmpl-AZk8j..."`                                                              |
| `gen_ai.usage.input_tokens`      | `1250`                                                                             |
| `gen_ai.usage.output_tokens`     | `380`                                                                              |
| `gen_ai.request.temperature`     | `0.0`                                                                              |
| `gen_ai.response.finish_reasons` | `["stop"]`                                                                         |
| `gen_ai.tool.call.id`            | `"call_abc123"` (single) or `["call_abc123","call_def456"]` (multiple, JSON array) |
| `span_kind`                      | `CLIENT`                                                                           |
| `span_status`                    | `OK` or `ERROR`                                                                    |
| `error.type`                     | `"RateLimitError"` (only on error)                                                 |
| `scope_name`                     | `"my-agent.llm"`                                                                   |

**`execute_tool` span** — one per tool execution (child of `invoke_agent`):

| Attribute               | Example                                       |
| ----------------------- | --------------------------------------------- |
| `span_name`             | `"execute_tool find_file"`                    |
| `gen_ai.operation.name` | `"execute_tool"`                              |
| `gen_ai.tool.name`      | `"find_file"`                                 |
| `gen_ai.tool.type`      | `"function"`                                  |
| `gen_ai.tool.call.id`   | `"call_abc123"` (when using function calling) |
| `span_kind`             | `INTERNAL`                                    |
| `span_status`           | `OK` or `ERROR`                               |
| `error.type`            | `"CommandTimeoutError"` (only on error)       |
| `scope_name`            | `"my-agent"`                                  |

<Callout type="info">
  The `gen_ai.tool.call.id` attribute on `chat` spans enables cross-span correlation — you can JOIN a `chat` span to its corresponding `execute_tool` spans via the shared tool call ID.
</Callout>

**Multiple log records** (in the logs pipeline), carrying matching `trace_id` + `span_id` from their respective spans. Log records are emitted in all three span types:

**`invoke_agent` log records:**

| `event_name`          | `body` content                   | When                  |
| --------------------- | -------------------------------- | --------------------- |
| `gen_ai.user.message` | Problem statement text           | At start of agent run |
| `gen_ai.agent.finish` | JSON: exit status + total tokens | At end of agent run   |

**`chat` log records:**

| `event_name`               | `body` content                    | When                                             |
| -------------------------- | --------------------------------- | ------------------------------------------------ |
| `gen_ai.system.message`    | Full system prompt                | For each system message in input                 |
| `gen_ai.user.message`      | Full user message                 | For each user message in input                   |
| `gen_ai.assistant.message` | Prior assistant response          | For each assistant message in input (multi-turn) |
| `gen_ai.tool.message`      | Tool result text                  | For each tool result message in input            |
| `gen_ai.choice`            | Full LLM response text            | For each response choice                         |
| `gen_ai.tool.call`         | Tool call JSON (name + arguments) | For each tool call in the response               |
| `gen_ai.thinking`          | Full reasoning/thinking text      | For each thinking block (Claude, DeepSeek, etc.) |

**`execute_tool` log records:**

| `event_name`         | `body` content             | When                  |
| -------------------- | -------------------------- | --------------------- |
| `gen_ai.tool.input`  | Tool command/action string | Before tool execution |
| `gen_ai.tool.output` | Tool observation/result    | After tool execution  |

## OTel Collector Configuration

The OTel Collector sits between your application and the backend. It receives OTLP data and routes traces and logs to separate backend streams.

### Minimal Configuration

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

processors:
  batch:
    timeout: 5s
    send_batch_size: 100

exporters:
  # Traces -> Parseable
  otlphttp/traces:
    endpoint: https://your-parseable-instance:8000
    encoding: json
    headers:
      Authorization: "Basic <credentials>"
      X-P-Stream: "genai-traces"
      X-P-Log-Source: "otel-traces"

  # Logs -> Parseable
  otlphttp/logs:
    endpoint: https://your-parseable-instance:8000
    encoding: json
    headers:
      Authorization: "Basic <credentials>"
      X-P-Stream: "genai-logs"
      X-P-Log-Source: "otel-logs"

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlphttp/traces]
    logs:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlphttp/logs]
```

### Key Points

* **Two pipelines** — traces and logs are separate OTel signals. The collector routes them independently.
* **One receiver** — both signals arrive at the same OTLP endpoint from the SDK.
* **JSON encoding** — the collector converts OTel protobuf to JSON before sending to the backend. This is what the backend flattens into queryable records.
* **Batch processor** — accumulates records and sends them in batches. Tune `timeout` and `send_batch_size` for your throughput. For development, lower values (1s, 10 records) give faster feedback. For production, higher values reduce network overhead.

### Running the Collector

Docker:

```bash
docker run -d --name otel-collector \
  -p 4317:4317 -p 4318:4318 \
  -v $(pwd)/otel-collector-config.yaml:/etc/otelcol/config.yaml \
  otel/opentelemetry-collector-contrib:latest
```

Binary:

```bash
otelcol-contrib --config otel-collector-config.yaml
```

## Semantic Conventions

All attribute names follow the [OpenTelemetry GenAI Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/). This matters because backends, dashboards, and tools that understand these conventions will automatically recognize and display GenAI data correctly.

### Span Attributes by Span Type

**`invoke_agent` spans:**

| Attribute                        | Type   | Required      | Description                                               |
| -------------------------------- | ------ | ------------- | --------------------------------------------------------- |
| `gen_ai.operation.name`          | string | Yes           | Always `"invoke_agent"`                                   |
| `gen_ai.agent.name`              | string | Yes           | Agent identifier                                          |
| `gen_ai.provider.name`           | string | Yes           | LLM provider: `"openai"`, `"anthropic"`, `"google"`, etc. |
| `gen_ai.request.model`           | string | Yes           | Model name used by the agent                              |
| `gen_ai.usage.input_tokens`      | int    | On completion | Total prompt tokens across all LLM calls                  |
| `gen_ai.usage.output_tokens`     | int    | On completion | Total completion tokens across all LLM calls              |
| `gen_ai.response.finish_reasons` | string | On completion | JSON array: `["exit_command"]`, `["stop"]`, etc.          |

**`chat` spans:**

| Attribute                        | Type   | Required              | Description                                                                                                            |
| -------------------------------- | ------ | --------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `gen_ai.operation.name`          | string | Yes                   | Always `"chat"` for chat completions                                                                                   |
| `gen_ai.provider.name`           | string | Yes                   | LLM provider: `"openai"`, `"anthropic"`, `"google"`, etc.                                                              |
| `gen_ai.request.model`           | string | Yes                   | Model name as passed to the API                                                                                        |
| `gen_ai.response.model`          | string | On success            | Model name as returned by the API (may differ from request)                                                            |
| `gen_ai.response.id`             | string | On success            | Provider-assigned response ID                                                                                          |
| `gen_ai.usage.input_tokens`      | int    | On success            | Prompt token count for this call                                                                                       |
| `gen_ai.usage.output_tokens`     | int    | On success            | Completion token count for this call                                                                                   |
| `gen_ai.request.temperature`     | float  | If set                | Sampling temperature                                                                                                   |
| `gen_ai.request.top_p`           | float  | If set                | Nucleus sampling parameter                                                                                             |
| `gen_ai.request.max_tokens`      | int    | If set                | Maximum output tokens                                                                                                  |
| `gen_ai.response.finish_reasons` | string | On success            | JSON array of finish reasons: `["stop"]`, `["tool_calls"]`                                                             |
| `gen_ai.tool.call.id`            | string | If tool calls present | Tool call ID(s) for cross-span correlation with `execute_tool` spans. Single ID as string; multiple IDs as JSON array. |
| `error.type`                     | string | On error              | Exception class name                                                                                                   |

**`execute_tool` spans:**

| Attribute               | Type   | Required     | Description                                                                |
| ----------------------- | ------ | ------------ | -------------------------------------------------------------------------- |
| `gen_ai.operation.name` | string | Yes          | Always `"execute_tool"`                                                    |
| `gen_ai.tool.name`      | string | Yes          | Tool/command name (e.g., `"find_file"`, `"open_file"`)                     |
| `gen_ai.tool.type`      | string | Yes          | Always `"function"`                                                        |
| `gen_ai.tool.call.id`   | string | If available | Tool call ID from function calling mode (links to LLM's tool call request) |
| `error.type`            | string | On error     | Exception class name (e.g., `"CommandTimeoutError"`)                       |

<Callout type="info">
  The older `gen_ai.system` attribute has been replaced by `gen_ai.provider.name` per the current OTel GenAI semantic conventions.
</Callout>

### Log Record Event Names

**`chat` span events:**

| `event_name`               | Semantic Convention   | Description                                        |
| -------------------------- | --------------------- | -------------------------------------------------- |
| `gen_ai.system.message`    | GenAI message event   | System prompt                                      |
| `gen_ai.user.message`      | GenAI message event   | User input                                         |
| `gen_ai.assistant.message` | GenAI message event   | Prior assistant response (multi-turn)              |
| `gen_ai.tool.message`      | GenAI message event   | Tool/function result                               |
| `gen_ai.choice`            | GenAI choice event    | LLM response content                               |
| `gen_ai.tool.call`         | GenAI tool call event | Tool/function invocation                           |
| `gen_ai.thinking`          | Custom extension      | Reasoning/thinking block (not yet in OTel semconv) |

**`invoke_agent` span events:**

| `event_name`          | Semantic Convention | Description                                           |
| --------------------- | ------------------- | ----------------------------------------------------- |
| `gen_ai.user.message` | GenAI message event | Problem statement that triggered the agent run        |
| `gen_ai.agent.finish` | Custom extension    | Agent completion summary (exit status + total tokens) |

**`execute_tool` span events:**

| `event_name`         | Semantic Convention | Description                                     |
| -------------------- | ------------------- | ----------------------------------------------- |
| `gen_ai.tool.input`  | Custom extension    | Tool command/action sent for execution          |
| `gen_ai.tool.output` | Custom extension    | Tool observation/result returned from execution |

### Log Record Attributes

Every log record carries:

| Attribute               | Type   | Description                                                                                   |
| ----------------------- | ------ | --------------------------------------------------------------------------------------------- |
| `gen_ai.operation.name` | string | `"chat"`, `"invoke_agent"`, or `"execute_tool"` — identifies which span type emitted this log |
| `gen_ai.event.name`     | string | Duplicates `event_name` for queryability as a flat column                                     |

**Additional attributes on `chat` log records:**

| Attribute                    | Type   | Description                                                     |
| ---------------------------- | ------ | --------------------------------------------------------------- |
| `gen_ai.provider.name`       | string | LLM provider (`openai`, `anthropic`, `google`, `mistral`, etc.) |
| `gen_ai.request.model`       | string | Model name as requested                                         |
| `gen_ai.request.temperature` | float  | Temperature (if set)                                            |
| `gen_ai.request.top_p`       | float  | Top-p (if set)                                                  |
| `gen_ai.request.max_tokens`  | int    | Max output tokens (if set)                                      |

**Additional attributes on `invoke_agent` log records:**

| Attribute                    | Type   | Description                                         |
| ---------------------------- | ------ | --------------------------------------------------- |
| `gen_ai.provider.name`       | string | LLM provider                                        |
| `gen_ai.request.model`       | string | Model name                                          |
| `gen_ai.agent.name`          | string | Agent identifier (e.g., `"swe-agent"`)              |
| `role`                       | string | `"user"` (on `gen_ai.user.message` only)            |
| `gen_ai.usage.input_tokens`  | int    | Total input tokens (on `gen_ai.agent.finish` only)  |
| `gen_ai.usage.output_tokens` | int    | Total output tokens (on `gen_ai.agent.finish` only) |

**Additional attributes on `execute_tool` log records:**

| Attribute             | Type   | Description                                               |
| --------------------- | ------ | --------------------------------------------------------- |
| `gen_ai.tool.name`    | string | Tool/command name                                         |
| `gen_ai.tool.type`    | string | Always `"function"`                                       |
| `gen_ai.tool.call.id` | string | Tool call ID (empty string if not using function calling) |

**Event-specific attributes (chat logs only):**

| Attribute             | Present on              | Type   | Description                           |
| --------------------- | ----------------------- | ------ | ------------------------------------- |
| `role`                | `gen_ai.{role}.message` | string | `system`, `user`, `assistant`, `tool` |
| `index`               | `gen_ai.choice`         | int    | Choice index (0-based)                |
| `finish_reason`       | `gen_ai.choice`         | string | `stop`, `tool_calls`, `length`, etc.  |
| `gen_ai.tool.name`    | `gen_ai.tool.call`      | string | Function/tool name                    |
| `gen_ai.tool.call.id` | `gen_ai.tool.call`      | string | Tool call ID                          |

### The body Field

The `body` of each log record is the **full, untruncated content**:

**`chat` span logs:**

| Event                      | `body` contains                                     |
| -------------------------- | --------------------------------------------------- |
| `gen_ai.system.message`    | Complete system prompt (can be thousands of tokens) |
| `gen_ai.user.message`      | Complete user message                               |
| `gen_ai.assistant.message` | Complete prior assistant response                   |
| `gen_ai.tool.message`      | Complete tool result                                |
| `gen_ai.choice`            | Complete LLM response text                          |
| `gen_ai.tool.call`         | JSON: `{"name": "...", "arguments": "..."}`         |
| `gen_ai.thinking`          | Complete reasoning/thinking text                    |

**`invoke_agent` span logs:**

| Event                 | `body` contains                                                                   |
| --------------------- | --------------------------------------------------------------------------------- |
| `gen_ai.user.message` | Complete problem statement that triggered the agent run                           |
| `gen_ai.agent.finish` | JSON: `{"exit_status": "...", "total_input_tokens": N, "total_output_tokens": N}` |

**`execute_tool` span logs:**

| Event                | `body` contains                     |
| -------------------- | ----------------------------------- |
| `gen_ai.tool.input`  | Complete tool command/action string |
| `gen_ai.tool.output` | Complete tool observation/result    |

No truncation. No size limits from the instrumentation side. The body carries whatever the LLM returned, whatever was sent to it, or whatever the tool produced.

## Scenarios

### Simple Chat Completion (OpenAI)

```python
response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is 2+2?"},
    ],
)
```

**Produces:**

* 1 span: `chat gpt-4o` with token counts, latency, status OK
* 3 log records: `gen_ai.system.message`, `gen_ai.user.message`, `gen_ai.choice`
* All share the same `trace_id` + `span_id`

### Multi-Turn Conversation

```python
messages = [
    {"role": "system", "content": "You are a math tutor."},
    {"role": "user", "content": "What is 10*5?"},
    {"role": "assistant", "content": "50"},
    {"role": "user", "content": "Divide by 2"},
]
response = call_llm("gpt-4o", messages)
```

**Produces:**

* 1 span: `chat gpt-4o`
* 5 log records: `gen_ai.system.message`, `gen_ai.user.message`, `gen_ai.assistant.message`, `gen_ai.user.message`, `gen_ai.choice`
* The full conversation history is captured. You can reconstruct it by querying log records for this span, ordered by timestamp.

### Tool/Function Calling

The LLM responds with tool calls instead of (or in addition to) text content.

**Produces:**

* 1 span: `chat gpt-4o`, `finish_reasons: ["tool_calls"]`
* N input message logs
* 1 choice log (may have empty body if the LLM only returned tool calls)
* 1+ `gen_ai.tool.call` logs — each with the tool name and JSON arguments in `body`

### Claude Thinking/Reasoning Blocks

Claude (and some other models) return a `thinking_blocks` array alongside the response content. Each thinking block contains the model's chain-of-thought reasoning.

**Produces:**

* 1 span: `chat claude-sonnet-4-20250514`
* N input message logs
* 1 choice log (the actual response text)
* 1+ `gen_ai.thinking` logs — each with the full reasoning text in `body`

This is the primary reason for manual instrumentation. Auto-instrumentors do not capture thinking blocks because they are a provider-specific extension not (yet) in the OpenAI SDK's standard response format.

### Error: Rate Limit

```python
try:
    response = call_llm(...)
except RateLimitError as e:
    # The span still exists with ERROR status
    pass
```

**Produces:**

* 1 span: `chat gpt-4o`, `span_status=ERROR`, `error.type=RateLimitError`
* N input message logs (emitted before the call, so they still exist)
* 0 choice/tool/thinking logs (call failed before response)
* All logs still have `trace_id` + `span_id` — you can see what was sent to the LLM even though it failed

### Error: Context Window Exceeded

The LLM returns a 400 because the input is too long.

**Produces:**

* Same as above — span with ERROR status, input message logs but no response logs.
* `error.type=ContextWindowExceededError`
* This is queryable: find all spans where `error.type = 'ContextWindowExceededError'`, then JOIN with logs to see what input caused it.

### Streaming Responses

**Current limitation:** The instrumentation code shown above works with non-streaming responses. For streaming (`stream=True`), you need to:

1. Open the span before the stream starts
2. Accumulate the streamed chunks into a full response
3. Emit log records and set span attributes after the stream completes
4. Close the span

The span remains open during streaming, so all log records emitted during or after streaming will be correlated.

```python
with _tracer.start_as_current_span(f"chat {model}", kind=trace.SpanKind.CLIENT) as span:
    span.set_attribute("gen_ai.request.model", model)
    # ... emit input message logs ...

    stream = client.chat.completions.create(model=model, messages=messages, stream=True)
    chunks = []
    for chunk in stream:
        chunks.append(chunk)

    # Reconstruct full response from chunks, then emit logs
    full_response_text = "".join(c.choices[0].delta.content or "" for c in chunks if c.choices)
    _otel_logger.emit(body=full_response_text, event_name="gen_ai.choice", ...)

    # Token usage may not be available in streaming mode (provider-dependent)
    span.set_status(trace.StatusCode.OK)
```

### Retries

If your agent retries failed LLM calls (e.g., on rate limit errors), each attempt produces its own span. The retry loop should be **outside** the span context:

```python
for attempt in range(max_retries):
    try:
        response = call_llm(model, messages)  # Each call creates its own span
        break
    except RateLimitError:
        time.sleep(backoff)
```

This produces N spans (one per attempt), each with its own status. Failed attempts have `ERROR` status, the successful attempt has `OK`.

### Multiple LLM Providers

The `gen_ai.provider.name` attribute distinguishes providers. If your agent calls OpenAI for some tasks and Anthropic for others:

* OpenAI calls: `gen_ai.provider.name = "openai"`
* Anthropic calls: `gen_ai.provider.name = "anthropic"`

You can filter and aggregate by provider in queries.

### Wrapper Libraries (LiteLLM, LangChain)

If your agent uses a wrapper library like LiteLLM that abstracts over multiple providers:

* Instrument at the **wrapper call site**, not inside the wrapper library
* The model name you pass to the wrapper becomes `gen_ai.request.model`
* The `gen_ai.provider.name` should reflect the actual underlying provider (if known)
* The response object structure may differ from the raw OpenAI SDK — adapt the attribute extraction accordingly

## Limitations and Edge Cases

### Thinking Blocks Are Provider-Specific

The `gen_ai.thinking` event is not part of the official OTel GenAI semantic conventions. It is a custom extension. Different providers expose reasoning differently:

| Provider           | How thinking is exposed                                     | How to extract                                      |
| ------------------ | ----------------------------------------------------------- | --------------------------------------------------- |
| Anthropic (Claude) | `response.choices[i].message.thinking_blocks` (via LiteLLM) | Iterate `thinking_blocks`, extract `"thinking"` key |
| DeepSeek           | `response.choices[i].message.reasoning_content`             | Extract `reasoning_content` field                   |
| OpenAI o1/o3       | Internal reasoning not exposed in API response              | Cannot be captured                                  |

If the provider does not expose reasoning, there will be no `gen_ai.thinking` log records. This is expected behavior, not a bug.

### Token Counts May Be Absent

Some scenarios where `gen_ai.usage.input_tokens` and `gen_ai.usage.output_tokens` are not available:

| Scenario                       | Why                                                | Impact                       |
| ------------------------------ | -------------------------------------------------- | ---------------------------- |
| Error spans                    | API call failed before returning usage             | Span has no token attributes |
| Streaming without usage chunks | Some providers don't send usage in streaming mode  | Span has no token attributes |
| Local/self-hosted models       | Some local model servers don't return usage        | Span has no token attributes |
| Wrapper library filtering      | Some wrappers strip usage from the response object | Span has no token attributes |

**Backend impact:** Token-based aggregations (cost, total tokens) should handle NULL gracefully.

### The body Field Can Be Very Large

System prompts in agent applications can be 10,000+ tokens. LLM responses can be similarly large. Tool call arguments can contain large JSON payloads. Thinking blocks can be tens of thousands of tokens.

There is **no truncation** in the instrumentation. The full content is emitted as the log record body. This is intentional — truncation would make conversation reconstruction incomplete.

**Backend impact:** The logs stream will be significantly larger (in bytes) than the traces stream. Plan storage and indexing accordingly.

### Log Records Without Span Context

If `_otel_logger.emit()` is called **outside** a `start_as_current_span()` context, the log record will have empty `trace_id` and `span_id`. This means:

* The log record exists in the logs stream but cannot be correlated with any span
* This is a bug in the instrumentation code — all GenAI log emissions should be inside a span context

The manual instrumentation approach prevents this by design: all `emit()` calls are inside the `with _tracer.start_as_current_span(...):` block.

### Concurrent/Async LLM Calls

OTel context propagation is thread-local (and async-task-local in asyncio). If your agent makes concurrent LLM calls:

* **Threading:** Each thread has its own context. Spans in different threads don't interfere. Each call gets its own `trace_id`/`span_id`.
* **asyncio:** OTel SDK supports async context propagation via `contextvars`. Each coroutine gets its own context.
* **Multiprocessing:** Each process has its own TracerProvider/LoggerProvider. Spans from different processes have different `trace_id`s.

Concurrency does not break correlation — each LLM call's logs are always linked to that call's span.

### Provider-Specific Response Formats

Different LLM providers return responses in slightly different formats. The instrumentation code must handle these differences:

| Provider                    | `response.model` | `response.usage`               | Tool calls            | Thinking                   |
| --------------------------- | ---------------- | ------------------------------ | --------------------- | -------------------------- |
| OpenAI                      | Always present   | Always present (non-streaming) | `.message.tool_calls` | N/A                        |
| Anthropic (via LiteLLM)     | Always present   | Always present                 | `.message.tool_calls` | `.message.thinking_blocks` |
| Google (via LiteLLM)        | Always present   | Always present                 | `.message.tool_calls` | N/A                        |
| Local models (Ollama, vLLM) | May differ       | May be absent                  | Varies                | N/A                        |

Guard all attribute extraction with `hasattr()` / `getattr()` / `is not None` checks.

### The opentelemetry-instrument CLI Must Wrap the Process

The CLI sets up providers at process startup. If your application forks or spawns subprocesses, those subprocesses will NOT have the providers configured. Each process that emits telemetry must be launched with `opentelemetry-instrument`, or must set up providers manually.

### Collector Must Be Running

If the OTel Collector is not running when the application starts:

* The SDK will buffer spans and log records in memory
* It will periodically retry exporting
* If the buffer fills up, the oldest records are dropped (configurable via `OTEL_BSP_MAX_QUEUE_SIZE`, default 2048 for spans)
* No application errors are raised — telemetry loss is silent

For production, ensure the collector is running before the application starts. For development, data loss during collector restarts is acceptable.

### Scope Name Consistency

Both `_tracer` and `_otel_logger` should use the **same scope name**. This makes it easy to filter both spans and logs by scope:

```python
_tracer = trace.get_tracer("my-agent.llm", "1.0.0")
_otel_logger = get_logger_provider().get_logger("my-agent.llm", "1.0.0")
```

If they use different scope names, correlation still works (via `trace_id`/`span_id`), but filtering by `scope_name` in queries will not match both signals.

## Troubleshooting

### No spans or logs appearing

1. **Is the collector running?** Check `curl http://localhost:4318/v1/traces` — should return a response (even an error response means it's listening).
2. **Is the CLI wrapping the process?** Run `opentelemetry-instrument --help` to verify it's installed. Check that your launch command uses `opentelemetry-instrument python ...`, not just `python ...`.
3. **Are exporters configured?** Check that `--traces_exporter otlp --logs_exporter otlp` are passed to the CLI.
4. **Is the endpoint correct?** `OTEL_EXPORTER_OTLP_ENDPOINT` must match where the collector is listening.

### Duplicate spans per LLM call

The auto-instrumentor is still active. Verify:

```bash
echo $OTEL_PYTHON_DISABLED_INSTRUMENTATIONS
# Should output: openai_v2
```

If `opentelemetry-instrumentation-openai-v2` is installed and not disabled, it will create its own spans alongside your manual spans.

### Log records have empty trace\_id/span\_id

Log records are being emitted outside a span context. Ensure every `_otel_logger.emit()` call is inside a `with _tracer.start_as_current_span(...):` block.

### "Overriding of current LoggerProvider is not allowed"

You are calling `set_logger_provider()` in your application code, but the CLI already set up a LoggerProvider. Remove the manual `set_logger_provider()` call. Use `get_logger_provider()` instead.

### Spans appear but logs do not

1. Check that `--logs_exporter otlp` is passed to the CLI (not `none`).
2. Check that the collector config has a `logs` pipeline (not just `traces`).
3. Verify that `_otel_logger.emit()` is being called — add a `print()` before the emit to confirm the code path is reached.

### Logs appear but with wrong event\_name

The `event_name` parameter in `_otel_logger.emit()` must be a keyword argument. If passed positionally, it may be interpreted as a different parameter. Always use `event_name=...`.

## Verification Checklist

After setting up instrumentation, verify end-to-end:

| Check                                    | How                                                                                                                         | Expected                                                                                                              |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Three span types present**             | Query traces and check `gen_ai.operation.name` values                                                                       | `invoke_agent`, `chat`, `execute_tool` all present                                                                    |
| **Span hierarchy correct**               | Pick a trace. Check that `chat` and `execute_tool` spans have `parent_span_id` matching the `invoke_agent` span's `span_id` | All child spans point to the `invoke_agent` parent                                                                    |
| **One `invoke_agent` per run**           | Count `invoke_agent` spans                                                                                                  | 1 per agent run                                                                                                       |
| **One `chat` span per LLM call**         | Count `chat` spans vs. LLM calls made                                                                                       | 1:1 ratio                                                                                                             |
| **One `execute_tool` per tool exec**     | Count `execute_tool` spans vs. tool executions                                                                              | 1:1 ratio                                                                                                             |
| **`gen_ai.agent.name` on invoke\_agent** | Check span attributes                                                                                                       | Present on `invoke_agent` span, NOT on `chat` spans                                                                   |
| **`gen_ai.provider.name` on chat spans** | Check span for `gen_ai.provider.name` (not `gen_ai.system`)                                                                 | Present on every `chat` span                                                                                          |
| **`gen_ai.tool.name` on execute\_tool**  | Check span attributes                                                                                                       | Tool name present                                                                                                     |
| **Request attributes present**           | Check `chat` span for `gen_ai.request.model`, `gen_ai.provider.name`                                                        | Present on every `chat` span                                                                                          |
| **Response attributes present**          | Check `chat` span for `gen_ai.usage.input_tokens`, `gen_ai.usage.output_tokens`                                             | Present on successful `chat` spans                                                                                    |
| **Aggregate tokens on invoke\_agent**    | Check `invoke_agent` span for `gen_ai.usage.input_tokens`                                                                   | Total across all LLM calls                                                                                            |
| **Error spans captured**                 | Trigger a timeout. Check for `execute_tool` span with `span_status_code = 2`.                                               | Span exists with `error.type`                                                                                         |
| **Log records exist**                    | Query logs for same `trace_id` as an `invoke_agent` span                                                                    | Multiple log records                                                                                                  |
| **Trace-log correlation**                | Pick a `chat` span. Query logs where `trace_id` and `span_id` match.                                                        | Logs link to the correct `chat` span                                                                                  |
| **All chat event types present**         | Check `event_name` values on `chat` logs                                                                                    | `gen_ai.system.message`, `gen_ai.user.message`, `gen_ai.choice`, and optionally `gen_ai.tool.call`, `gen_ai.thinking` |
| **invoke\_agent logs present**           | Check logs with `gen_ai.operation.name = "invoke_agent"`                                                                    | `gen_ai.user.message` (problem statement) and `gen_ai.agent.finish` (completion summary)                              |
| **execute\_tool logs present**           | Check logs with `gen_ai.operation.name = "execute_tool"`                                                                    | `gen_ai.tool.input` and `gen_ai.tool.output` paired for each tool execution                                           |
| **All three operation types in logs**    | Group logs by `gen_ai.operation.name`                                                                                       | `invoke_agent`, `chat`, and `execute_tool` all present                                                                |
| **Body is untruncated**                  | Check `body` field on a `gen_ai.choice` log record                                                                          | Full LLM response text, not truncated                                                                                 |
| **No duplicates**                        | Check that each LLM call produces exactly 1 `chat` span and 1 `gen_ai.choice` log per response choice                       | No doubles                                                                                                            |


# Schema Reference (/docs/user-guide/agent-observability/schema-reference)



When Parseable receives GenAI traces at the `/v1/traces` endpoint, it flattens the nested OTel JSON into a single row per span event. This page documents every column you can query.

## Span Hierarchy

A single agent invocation produces a tree of spans sharing the same `span_trace_id`:

```
span_trace_id: abc123
|
+-- [root] agent_run (gen_ai.operation.name = "agent")
      |
      +-- chat gpt-4o (gen_ai.operation.name = "chat")
      |     +-- event: gen_ai.prompt   (event_name row)
      |     +-- event: gen_ai.completion (event_name row)
      |
      +-- execute_tool search_api (gen_ai.operation.name = "execute_tool")
      |
      +-- chat gpt-4o (gen_ai.operation.name = "chat")
            +-- event: gen_ai.prompt   (event_name row)
            +-- event: gen_ai.completion (event_name row)
```

Key points:

* **Span rows** have `event_name IS NULL`. These contain the `gen_ai.*` attributes, token counts, and Parseable-enriched columns.
* **Event rows** have `event_name` set (e.g., `gen_ai.prompt` or `gen_ai.completion`). These contain the message content in `event_gen_ai.prompt` or `event_gen_ai.completion`. Event rows are only present when content capture is enabled (`OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT=true`).
* Use `span_parent_span_id` to reconstruct the call tree within a trace.

***

## Core Trace Columns

These are standard OpenTelemetry span fields, present on every row.

| Column                          | Type      | Description                                                                        |
| ------------------------------- | --------- | ---------------------------------------------------------------------------------- |
| `span_trace_id`                 | String    | Unique identifier for the entire trace (shared across all spans in one agent run). |
| `span_span_id`                  | String    | Unique identifier for this individual span.                                        |
| `span_parent_span_id`           | String    | Span ID of the parent span. Empty string for root spans.                           |
| `span_name`                     | String    | Human-readable span name (e.g., `chat gpt-4o`, `execute_tool search`).             |
| `span_kind`                     | Int       | OTel span kind numeric value (0=Unspecified, 1=Internal, 2=Server, 3=Client).      |
| `span_kind_description`         | String    | Human-readable span kind (e.g., `SPAN_KIND_CLIENT`).                               |
| `span_start_time_unix_nano`     | BigInt    | Span start time in nanoseconds since epoch.                                        |
| `span_end_time_unix_nano`       | BigInt    | Span end time in nanoseconds since epoch.                                          |
| `span_status_code`              | Int       | Status code: 0=Unset, 1=OK, 2=Error.                                               |
| `span_status_description`       | String    | Human-readable status (e.g., `STATUS_CODE_OK`).                                    |
| `span_status_message`           | String    | Error message when `span_status_code = 2`.                                         |
| `span_trace_state`              | String    | W3C trace state string.                                                            |
| `span_flags`                    | Int       | Span flags bitmask.                                                                |
| `span_flags_description`        | String    | Human-readable span flags.                                                         |
| `span_dropped_attributes_count` | Int       | Number of attributes dropped due to limits.                                        |
| `span_dropped_events_count`     | Int       | Number of events dropped due to limits.                                            |
| `span_dropped_links_count`      | Int       | Number of links dropped due to limits.                                             |
| `p_timestamp`                   | Timestamp | Parseable ingest timestamp.                                                        |
| `p_metadata`                    | String    | Parseable metadata field.                                                          |
| `p_tags`                        | String    | Parseable tags field.                                                              |
| `service.name`                  | String    | OTel resource attribute identifying the service.                                   |
| `scope_name`                    | String    | Instrumentation scope name.                                                        |
| `scope_version`                 | String    | Instrumentation scope version.                                                     |
| `schema_url`                    | String    | OTel schema URL.                                                                   |

***

## GenAI Identity and Operation

Columns that identify the GenAI operation being performed.

| Column                   | Type   | Description                                                                          |
| ------------------------ | ------ | ------------------------------------------------------------------------------------ |
| `gen_ai.operation.name`  | String | Type of operation: `chat`, `text_completion`, `embeddings`, `execute_tool`, `agent`. |
| `gen_ai.system`          | String | GenAI provider system identifier (e.g., `openai`, `anthropic`, `cohere`).            |
| `gen_ai.provider.name`   | String | Provider name when different from system.                                            |
| `gen_ai.conversation.id` | String | Unique identifier for a multi-turn conversation thread.                              |

***

## Model Request

Columns capturing the parameters sent to the model.

| Column                             | Type   | Description                                                 |
| ---------------------------------- | ------ | ----------------------------------------------------------- |
| `gen_ai.request.model`             | String | Model requested (e.g., `gpt-4o`, `claude-3-opus-20240229`). |
| `gen_ai.request.temperature`       | Float  | Sampling temperature.                                       |
| `gen_ai.request.top_p`             | Float  | Nucleus sampling parameter.                                 |
| `gen_ai.request.top_k`             | Int    | Top-k sampling parameter.                                   |
| `gen_ai.request.max_tokens`        | Int    | Maximum tokens requested for the response.                  |
| `gen_ai.request.seed`              | Int    | Random seed for reproducibility.                            |
| `gen_ai.request.frequency_penalty` | Float  | Frequency penalty parameter.                                |
| `gen_ai.request.presence_penalty`  | Float  | Presence penalty parameter.                                 |
| `gen_ai.request.stop_sequences`    | String | Stop sequences (JSON array as string).                      |

***

## Model Response

Columns capturing what the model returned.

| Column                           | Type   | Description                                                                           |
| -------------------------------- | ------ | ------------------------------------------------------------------------------------- |
| `gen_ai.response.id`             | String | Provider-assigned response ID (e.g., `chatcmpl-abc123`).                              |
| `gen_ai.response.model`          | String | Actual model used (may differ from requested, e.g., `gpt-4o-2024-08-06`).             |
| `gen_ai.response.finish_reasons` | String | Reason the model stopped generating (JSON array, e.g., `["stop"]`, `["tool_calls"]`). |

***

## Token Usage

Columns tracking token consumption per span.

| Column                                               | Type | Description                                                  |
| ---------------------------------------------------- | ---- | ------------------------------------------------------------ |
| `gen_ai.usage.input_tokens`                          | Int  | Number of input (prompt) tokens consumed.                    |
| `gen_ai.usage.output_tokens`                         | Int  | Number of output (completion) tokens generated.              |
| `gen_ai.usage.input_token_details.cached_tokens`     | Int  | Number of input tokens served from cache.                    |
| `gen_ai.usage.output_token_details.reasoning_tokens` | Int  | Number of output tokens used for chain-of-thought reasoning. |

***

## Agent

Columns specific to agent-level spans (where `gen_ai.operation.name = 'agent'`).

| Column                     | Type   | Description                                        |
| -------------------------- | ------ | -------------------------------------------------- |
| `gen_ai.agent.name`        | String | Name of the agent.                                 |
| `gen_ai.agent.id`          | String | Unique identifier for the agent instance.          |
| `gen_ai.agent.description` | String | Human-readable description of the agent's purpose. |

***

## Tool Execution

Columns specific to tool call spans (where `gen_ai.operation.name = 'execute_tool'`).

| Column                       | Type   | Description                                                       |
| ---------------------------- | ------ | ----------------------------------------------------------------- |
| `gen_ai.tool.name`           | String | Name of the tool invoked (e.g., `search_api`, `calculator`).      |
| `gen_ai.tool.type`           | String | Type of tool (e.g., `function`, `retrieval`, `code_interpreter`). |
| `gen_ai.tool.call.id`        | String | Provider-assigned tool call ID.                                   |
| `gen_ai.tool.call.arguments` | String | JSON string of arguments passed to the tool.                      |
| `gen_ai.tool.call.result`    | String | JSON string or text of the tool execution result.                 |

***

## Content Columns (Opt-In)

These columns are only populated when content capture is enabled via `OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT=true`. They appear on **event rows** (where `event_name` is not null).

| Column                           | Type   | Description                                                                              |
| -------------------------------- | ------ | ---------------------------------------------------------------------------------------- |
| `event_name`                     | String | Event type: `gen_ai.prompt`, `gen_ai.completion`, `gen_ai.tool.message`, etc.            |
| `event_gen_ai.prompt`            | String | The full prompt or user message content. Present on `gen_ai.prompt` events.              |
| `event_gen_ai.completion`        | String | The full completion or assistant message content. Present on `gen_ai.completion` events. |
| `event_time_unix_nano`           | BigInt | Event timestamp in nanoseconds since epoch.                                              |
| `event_dropped_attributes_count` | Int    | Number of event attributes dropped due to limits.                                        |

***

## Parseable-Enriched Columns

These columns are computed server-side by Parseable at ingest time. They do not exist in the raw OTel data.

| Column                   | Type  | Description                                                                                                                  |
| ------------------------ | ----- | ---------------------------------------------------------------------------------------------------------------------------- |
| `p_genai_cost_usd`       | Float | Estimated cost in USD for this span, computed from the model name and token counts using Parseable's built-in pricing table. |
| `p_genai_tokens_total`   | Int   | Sum of `gen_ai.usage.input_tokens` + `gen_ai.usage.output_tokens`.                                                           |
| `p_genai_tokens_per_sec` | Float | Throughput: `output_tokens / (span_duration_seconds)`. Useful for comparing model and provider performance.                  |
| `p_genai_duration_ms`    | Float | Span duration in milliseconds, computed from `span_end_time_unix_nano - span_start_time_unix_nano`.                          |


# SQL Query Templates (/docs/user-guide/agent-observability/sql-queries)



Ready-to-use SQL queries for common agent observability tasks. All queries assume a dataset named `genai-traces`. Replace with your actual dataset name if different.

:::tip
Span rows have `event_name IS NULL`. Most analytics queries should include this filter to avoid double-counting with event rows (which carry prompt/completion content).
:::

***

## 1. LLM Call Summary (Last 24 Hours)

Get a per-model overview of call volume, token usage, latency, cost, and error rate.

```sql
SELECT
    "gen_ai.request.model" AS model,
    COUNT(*) AS call_count,
    SUM("gen_ai.usage.input_tokens") AS total_input_tokens,
    SUM("gen_ai.usage.output_tokens") AS total_output_tokens,
    ROUND(AVG(p_genai_duration_ms), 2) AS avg_latency_ms,
    ROUND(SUM(p_genai_cost_usd), 6) AS total_cost_usd,
    ROUND(100.0 * SUM(CASE WHEN span_status_code = 2 THEN 1 ELSE 0 END) / COUNT(*), 2) AS error_rate_pct
FROM "genai-traces"
WHERE p_timestamp > NOW() - INTERVAL '24 hours'
    AND event_name IS NULL
    AND "gen_ai.operation.name" = 'chat'
GROUP BY "gen_ai.request.model"
ORDER BY total_cost_usd DESC;
```

***

## 2. Agent Run Reconstruction

Reconstruct every span in a single agent run, ordered chronologically. Replace `<TRACE_ID>` with an actual trace ID.

```sql
SELECT
    span_name,
    "gen_ai.operation.name" AS operation,
    ROUND(p_genai_duration_ms, 2) AS duration_ms,
    "gen_ai.usage.input_tokens" AS input_tokens,
    "gen_ai.usage.output_tokens" AS output_tokens,
    ROUND(p_genai_cost_usd, 6) AS cost_usd,
    span_status_description AS status,
    span_parent_span_id
FROM "genai-traces"
WHERE span_trace_id = '<TRACE_ID>'
    AND event_name IS NULL
ORDER BY span_start_time_unix_nano;
```

***

## 3. Token Usage and Cost Over Time

Hourly breakdown of token consumption and cost by model over the last 7 days.

```sql
SELECT
    DATE_TRUNC('hour', p_timestamp) AS hour,
    "gen_ai.request.model" AS model,
    SUM("gen_ai.usage.input_tokens") AS input_tokens,
    SUM("gen_ai.usage.output_tokens") AS output_tokens,
    SUM(p_genai_tokens_total) AS total_tokens,
    ROUND(SUM(p_genai_cost_usd), 4) AS cost_usd
FROM "genai-traces"
WHERE p_timestamp > NOW() - INTERVAL '7 days'
    AND event_name IS NULL
    AND "gen_ai.usage.input_tokens" IS NOT NULL
GROUP BY hour, "gen_ai.request.model"
ORDER BY hour DESC, cost_usd DESC;
```

***

## 4. Tool Usage Analysis

Understand which tools are called most often, their average duration, and failure rate.

```sql
SELECT
    "gen_ai.tool.name" AS tool,
    COUNT(*) AS invocations,
    ROUND(AVG(p_genai_duration_ms), 2) AS avg_duration_ms,
    ROUND(100.0 * SUM(CASE WHEN span_status_code = 2 THEN 1 ELSE 0 END) / COUNT(*), 2) AS failure_rate_pct
FROM "genai-traces"
WHERE "gen_ai.operation.name" = 'execute_tool'
    AND p_timestamp > NOW() - INTERVAL '24 hours'
GROUP BY "gen_ai.tool.name"
ORDER BY invocations DESC;
```

***

## 5. Error Analysis

Surface the most recent errors across all models and operations.

```sql
SELECT
    p_timestamp,
    "gen_ai.request.model" AS model,
    "gen_ai.operation.name" AS operation,
    span_status_message AS error_message,
    span_trace_id,
    span_span_id,
    "gen_ai.agent.name" AS agent
FROM "genai-traces"
WHERE span_status_code = 2
    AND p_timestamp > NOW() - INTERVAL '24 hours'
ORDER BY p_timestamp DESC
LIMIT 50;
```

***

## 6. Conversation Threads

Aggregate multi-turn conversations to see total LLM calls, tool calls, token usage, and cost per conversation.

```sql
SELECT
    "gen_ai.conversation.id" AS conversation,
    COUNT(CASE WHEN "gen_ai.operation.name" = 'chat' THEN 1 END) AS llm_calls,
    COUNT(CASE WHEN "gen_ai.operation.name" = 'execute_tool' THEN 1 END) AS tool_calls,
    SUM(p_genai_tokens_total) AS total_tokens,
    ROUND(SUM(p_genai_cost_usd), 4) AS total_cost_usd,
    MIN(p_timestamp) AS started_at,
    MAX(p_timestamp) AS ended_at
FROM "genai-traces"
WHERE "gen_ai.conversation.id" IS NOT NULL
    AND event_name IS NULL
    AND p_timestamp > NOW() - INTERVAL '24 hours'
GROUP BY "gen_ai.conversation.id"
ORDER BY total_cost_usd DESC;
```

***

## 7. Model Comparison

Compare models side-by-side on latency, throughput, and cost over the last 7 days.

```sql
SELECT
    "gen_ai.request.model" AS model,
    COUNT(*) AS calls,
    ROUND(AVG(p_genai_duration_ms), 2) AS avg_latency_ms,
    ROUND(PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY p_genai_duration_ms), 2) AS p95_latency_ms,
    ROUND(AVG(p_genai_tokens_per_sec), 2) AS avg_tokens_per_sec,
    ROUND(SUM(p_genai_cost_usd), 4) AS total_cost_usd,
    ROUND(AVG(p_genai_cost_usd), 6) AS avg_cost_per_call
FROM "genai-traces"
WHERE event_name IS NULL
    AND "gen_ai.operation.name" = 'chat'
    AND p_timestamp > NOW() - INTERVAL '7 days'
GROUP BY "gen_ai.request.model"
ORDER BY total_cost_usd DESC;
```

***

## 8. Slowest Calls (P95 Outliers)

Find the slowest LLM calls to identify latency bottlenecks.

```sql
SELECT
    p_timestamp,
    "gen_ai.request.model" AS model,
    span_name,
    ROUND(p_genai_duration_ms, 2) AS duration_ms,
    "gen_ai.usage.input_tokens" AS input_tokens,
    "gen_ai.usage.output_tokens" AS output_tokens,
    ROUND(p_genai_tokens_per_sec, 2) AS tokens_per_sec,
    span_trace_id
FROM "genai-traces"
WHERE event_name IS NULL
    AND "gen_ai.operation.name" = 'chat'
    AND p_timestamp > NOW() - INTERVAL '24 hours'
ORDER BY p_genai_duration_ms DESC
LIMIT 20;
```


# Anomaly Detection (/docs/user-guide/alerting/anomaly)





<OfferingPills pro enterprise className="mb-4" />

## Anomaly Detection Alerts

Get an alert if your latest data looks unusual compared to recent trends.

### Configuration

* **Use historical data of**: Training period for the ML model (e.g., 1 day, 1 week, 1 month)
* **Repeat evaluation every**: How often to check for anomalies (e.g., every 10 minutes)
* **Group By behavior**: When using Group By with Anomaly Detection, the system analyzes each group independently. Alerts trigger separately for each group that shows anomalous behavior. You can preview anomalies for individual groups using the dropdown selector in the top-right corner of the preview panel.

<img alt="" src={__img0} />


# Forecasting (/docs/user-guide/alerting/forecasting)





<OfferingPills pro enterprise className="mb-4" />

## Forecasting Alerts

We predict future data and alert you if it's expected to cross your limit.

### Configuration

* **Use historical data of**: Historical period for prediction model (e.g., 1 day, 1 week)
* **Repeat evaluation every**: How often to run predictions (e.g., every 10 minutes)
* **Forecast the next**: Time window to predict ahead (e.g., 3 hours, 1 day)
* **Group By behavior**: When using Group By with Forecasting, the system analyzes each group independently. Alerts trigger separately for each group that shows anomalous behavior. You can preview anomalies for individual groups using the dropdown selector in the top-right corner of the preview panel.

<img alt="" src={__img0} />


# Alerts (/docs/user-guide/alerting)













<OfferingPills pro enterprise className="mb-4" />

Parseable offers realtime alerting based on contents of incoming events. Each dataset can have several alerts and each alert is evaluated independently.

<img alt="" src={__img0} placeholder="blur" />

## How to set-up alerts

1. Navigate to the Alerts page from the side navigation menu
2. Click on "Create Alert" to set up a new alert
3. Set the "Preview", it could be either chart or table for 10m, 1h, 5h 1d or any custom timerange.
   <img alt="" src={__img1} placeholder="blur" />

### Configure Alert Rules

Configure the alert rules for all alert types:

* **Dataset**: Select the log dataset or dataset you want to monitor
* **Monitor**: Choose the specific field to track (e.g., `response_time`, `error_count`, `status_code`)
* **Filter** (Optional): Add conditions to narrow down the data (e.g., `status = 500`, `environment = production`)
* **Group By** (Optional): Group results by specific fields for more granular alerting (e.g., group by `service_name` or `region`)

<img alt="" src={__img2} />

### Configure Targets

Targets are the destinations where notifications are sent when an alert is triggered. Parseable supports Webhook, Slack, and Alertmanager targets.

The list of configured targets can be seen under Settings > Alert Targets.

<img alt="" src={__img3} />

### Add Title and Save

* **Title**: Give your alert a descriptive name (e.g., "High CPU Usage", "API Error Rate")
* **Severity**: Select the appropriate level: Low, Medium, High, or Critical
* **Tags** (Optional): Add tags to categorize your alerts

Click **"Save"** to create your alert.

## Managing Alerts

<img alt="" src={__img4} placeholder="blur" />

After creating alerts, you can manage them from the Alerts page:

* **Evaluate alert**: Manually trigger an evaluation
* **Disable alert**: Temporarily disable without deleting
* **Mute notifications**: Stop notifications during maintenance
* **Edit alert**: Modify configuration
* **Delete Alert**: Permanently remove


# Standard Threshold (/docs/user-guide/alerting/standard-threshold)





## Threshold Alerts

Get notified when a metric crosses a set limit.

### Configuration

* **Evaluate the last**: Time window to analyze (e.g., 10 minutes, 1 hour, 1 day)
* **Repeat evaluation every**: How often to check the condition (e.g., every 10 minutes)
* **Trigger when result is**: Set the comparison operator (`>`, `<`, `=`, `>=`, `<=`, `!=`) and threshold value

<img alt="" src={__img0} />


# AI Native (/docs/user-guide/ai-native)











<OfferingPills pro enterprise className="mb-4" />

Parseable brings AI-native capabilities to your observability workflow, helping you get answers faster and reduce mean time to resolution.

## Features

### Keystone

Ask questions about your telemetry data in natural language. Keystone uses multiple AI agents to find the best answer across your datasets.

<img alt="Keystone" src={__img0} />

[Learn more about Keystone →](/docs/user-guide/ai-native/keystone)

### Dataset Summarization

Get AI-powered summaries of your datasets to quickly identify patterns, anomalies, and potential issues.

<img alt="Summarization" src={__img1} placeholder="blur" />

[Learn more about Summarization →](/docs/user-guide/ai-native/summary)

### Text to SQL

Generate SQL queries from plain English descriptions. The AI assistant can also fix broken queries and explain complex SQL.

<img alt="Text to SQL" src={__img2} placeholder="blur" />

[Learn more about Text to SQL →](/docs/user-guide/ai-native/text-to-sql)

See also: [Parseable AI Assistant](/docs/llm/text-to-sql) for advanced LLM configuration options.

## Configuration

To enable AI features, configure your LLM provider:

1. Go to **Settings** > **AI Assistant**
2. Choose your preferred LLM provider (OpenAI GPT or Anthropic Claude)
3. Add your API key
4. Save your preferences

<img alt="LLM Configuration" src={__img3} placeholder="blur" />


# Keystone (/docs/user-guide/ai-native/keystone)









<OfferingPills pro enterprise className="mb-4" />

## Introduction

The core idea behind Keystone is to let you get to the answers you are looking in the shortest possible time. Specifically, Keystone is built to help you explore and analyze your observability data using natural language questions.

But why natural language? Because it allows you to ask questions without needing to know the underlying data structure or query languages. Traditionally, dashboards have served this purpose to show you trends and metrics. However, dashboards are limited to predefined views and often require you to know what you're looking for in advance.

For example, if you're a SRE investigating a sudden spike in error rates, you might start with a dashboard showing overall error trends. But what if you need to drill down into specific error codes, affected services, or time periods? You might find yourself switching between multiple dashboards, each providing only a piece of the puzzle - this slows down the investigation significantly.

This is where Keystone comes in. By allowing you to ask specific questions in natural language, Keystone can quickly guide you to the relevant data, generate the necessary queries, and even visualize the results. This not only speeds up your investigation but also empowers you to explore your data more intuitively.

## How Keystone works

Keystone uses three specific agents working together to answer your questions:

* **Overview Agent**: Identifies which datasets contain the data you need and time-range. The overview agent is also the leader that orchestrates the other agents to get you the best answer.
* **SQL Agent**: Generates and runs multiple SQL queries to find the best answer. It also works with the overview agent to validate the results from each query.
* **Charting Agent**: Creates visualizations if asked by users to explain the results.

<img alt="Keystone Architecture" src={__img0} placeholder="blur" />

<iframe width="560" height="315" src="https://www.youtube.com/embed/cvX01iZZ_tE?si=Mp6VR2pTjkbLaFHy" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />

### Sample Q\&A workflow

Let's walk through a typical workflow of using Keystone to answer a question.

#### User asks a question

Start by asking a question in natural language:

```
What are the top 5 error codes in the last 24 hours?
```

#### Dataset & time range selection

Keystone processes the question and extracts two key pieces of information:

* Relevant datasets: Which datasets contain the data needed
* Time-range: The time period to query (e.g., last 24 hours, last week)

You'll be presented with these selections for validation before proceeding.

<img alt="Dataset & Time-Range Selection" src={__img1} />

#### Query generation & execution within guardrails

Once you validate the selection

1. The Q\&A agent collaborates with the SQL agent
2. Multiple SQL queries are generated to approach your question from different angles
3. All queries are executed against the selected datasets
4. The overview agent validates the results from each query, acting as a guardrail to ensure accuracy
5. The best answer is curated based on which query results most accurately address your question

#### Answer & visualization

* A natural language answer to your question
* Raw data results from the query
* Optional visualizations (charts/graphs) for clearer understanding

## Configuration

To enable Keystone, configure your LLM provider in your Parseable instance:

* Go to **Settings** > **AI Assistant**.
* Choose your preferred LLM provider (OpenAI GPT or Anthropic Claude).
* Add your API key.
* Save your preferences.

Note that Keystone currently supports the following models and providers:

* **OpenAI**: GPT-4 and GPT-3.5 models
* **Anthropic**: Claude models

<img alt="LLM Configuration" src={__img2} placeholder="blur" />


# Dataset Summarization (/docs/user-guide/ai-native/summary)





<OfferingPills pro enterprise className="mb-4" />

Parseable's AI-powered summarization feature simplifies data analysis and debugging by automatically generating concise overviews of your datasets.

## How It Works

1. Select any dataset within Parseable
2. Click on `Summarize my data` to generate a concise overview
3. The AI identifies key patterns, anomalies, and potential faults
4. Receive actionable recommendations and SQL queries to drill deeper

<img alt="Summarization UI" src={__img0} placeholder="blur" />

## Benefits

* **Quick Insights**: Gain insights without manually combing through extensive datasets
* **Reduced Troubleshooting Time**: Pinpoint anomalies and root causes effortlessly
* **Simplified Collaboration**: Share clear, concise summaries across your team
* **Proactive Issue Resolution**: Leverage AI-driven recommendations to address issues before they escalate

## Example Use Case

When troubleshooting elevated error rates in your logs, the summarization feature can instantly highlight:

* Unusual spikes in errors between specific timestamps
* Affected services and hosts
* Suggested SQL queries to drill down further, such as:

```sql
SELECT host, COUNT(*) as error_count
FROM logs
WHERE status='error' AND timestamp BETWEEN '2025-07-20T00:00:00' AND '2025-07-20T06:00:00'
GROUP BY host
ORDER BY error_count DESC;
```

## Configuration

The summarization feature is available out of the box with your Enterprise license. No additional configuration is required beyond setting up your preferred LLM provider in the settings page.


# Text to SQL (/docs/user-guide/ai-native/text-to-sql)













<OfferingPills pro enterprise className="mb-4" />

Parseable's LLM based query builder allows you to generate SQL queries based on your natural language query. This feature is available in the Prism and can be accessed from the SQL editor. It can also help with fixing your queries by suggesting corrections based on the query you have written.

## 1. Choosing Your LLM Provider

**Parseable supports multiple AI models out of the box.**

* Go to **Settings** > **AI Assistant**.
* Choose your preferred LLM provider (e.g., OpenAI GPT, Anthropic Claude).
* Add your API key.
* Save your preferences.

<img alt="" src={__img0} placeholder="blur" />

You can change this any time to fit team policies, costs, or performance needs.

## 2. Generating SQL from Plain English

**How to:**

* In your SQL editor, look for the "Generate with AI" button at the bottom.
  <img alt="" src={__img1} placeholder="blur" />

* Type your question or description in plain language.
  **Examples:**

  * `Show me all error logs for the last hour grouped by host`
  * `Find top 5 most common user agents in the backend table`
  * `Summarize response statuses per environment tag`

**What happens:**
The AI will generate a ready-to-run SQL query for your prompt. You can copy, run, or tweak the result.

## 3. Using AI for Query Help

**Ask the AI anything in your SQL workflow:**

* **Write a new query:**
  `Generate with AI` > "Show all 5xx errors grouped by host in the last hour."
* **Fix a query:**
  Paste a broken query, then prompt, "Fix this query, it's giving a syntax error."
* **Explain a query:**
  Ask, "Explain what this query does."
* **Tweak logic:**
  "Can you add a filter for status = 500?"

The assistant uses your current datasets and history for context, so results are relevant.

## 4. Using Chat History

* All prompts and AI responses are saved automatically.
* Click the **History** tab in the assistant panel to view previous conversations.
* Rerun, reuse, or refine past queries from here.
* Useful for incident reviews, recurring analytics, and keeping a record of troubleshooting steps.

<img alt="" src={__img2} placeholder="blur" />

## 5. The Library

* Save any query you want to reuse in the **Library**.
* From the Library pane, you can:
  * Run saved queries directly
  * Edit or improve them with the AI assistant
  * Ask the assistant to explain saved queries

The Library is searchable and can be personal or shared with your team.

<img alt="" src={__img3} placeholder="blur" />

## 6. Let AI Fix Your Query

**When a query fails:**

* Click "Fix with AI" on the error message or use the AI assistant with your broken SQL.
* The AI analyzes your schema and query, returning a corrected version (e.g., fixing wrong field names, aggregation functions, or syntax).

This is especially useful in high-pressure situations or when exploring unfamiliar datasets.

<img alt="" src={__img4} placeholder="blur" />

## Example Workflow

1. **Troubleshoot an issue:**
   You notice a spike in latency. Type a plain English prompt describing what you need.
2. **Get a query:**
   AI generates the SQL for you.
3. **Edit and run:**
   Tweak or run the query.
4. **Query fails?**
   Use "Fix with AI" to automatically correct it.
5. **Save to Library:**
   Store your working query for future reuse, and ask the AI to explain it for documentation.


# Docker Compose (/docs/self-hosted/installation/distributed/docker-compose)



This document explains how to set up Parseable in **high availability mode** with Docker Compose, with `s3-store` mode. This mode is used to store logs on S3 or compatible object storage.

## Prerequisites

Docker and Docker Compose, installed on your machine. Refer to this doc to install Docker if you haven't already.

## Download Docker Compose File

Download the Docker Compose file.

```bash
mkdir parseable
cd parseable
wget https://www.parseable.com/parseable/docker-compose.yaml
```

## Run Parseable

This Compose file contains the configuration for Parseable, along with the required environment variables. You can modify the environment variables in the file as needed. It also includes a [MinIO](https://min.io/) service for S3 compatible storage. This compose creates 4 Parseable ingest services and 1 Parseable query service.

Once you've setup the env as per your requirements, you can start Parseable cluster using the following command:

```bash
docker compose up 
```

## Access Parseable

Once Parseable is up and running, you can access it at `http://localhost:8000` (assuming you've set `P_ADDR` to `:8000` in the env file). Credentials to login to Parseable are set via `P_USERNAME` and `P_PASSWORD` fields in the compose file.

### Troubleshoot

#### Running docker on AWS EC2

When trying to fetch credentials over IMDSv2 inside of docker container the client can hang indefinitely. This can happen due to AWS not allowing more than 1 hop in IMDSv2 endpoint response. You can change this configuration, please refer to the consideration section of [retrieve instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html#imds-considerations).

#### Memory constraints

For errors like `High memory usage detected: 90.6% (threshold: 80.0%)`, you can override these values by setting the values of `P_MEMORY_THRESHOLD` and `P_CPU_THRESHOLD` environment variables as `100`. By default, the memory and cpu thresholds are set to 80%.


# Kubernetes (/docs/self-hosted/installation/distributed/k8s-helm)



This page explains the steps required to setup Parseable in a distributed mode on Kubernetes via Helm.

## Prerequisites

* `kubectl` and `helm` installed and configured to point to relevant Kubernetes cluster.
* Use S3 or a compatible object store such as MinIO to store logs.

## Set up object store

<Callout type="info">
  The MinIO installation steps below are for testing purposes only. For production level deployment please refer to the [MinIO documentation](https://min.io/docs/minio).
</Callout>

This step is required only if you want to setup MinIO as the backend for Parseable. Please skip this step if you have another object store, like S3, already available.
Make sure you configure `storageClass` in the helm install command.

```bash
helm repo add minio https://charts.min.io/
helm install --namespace minio --create-namespace --set "buckets[0].name=parseable,buckets[0].policy=none,buckets[0].purge=false,rootUser=minioadmin,rootPassword=minioadmin,replicas=1,persistence.enabled=true,persistence.storageClass="",resources.requests.memory=128Mi,mode=standalone" minio minio/minio
kubectl port-forward svc/minio-console -n minio 9001:9001
```

You can now access the MinIO console at `http://localhost:9001`. You should see a bucket called `parseable` created.

### Create configuration secret

Create a secret file with the configuration for Parseable. Note that the values set below are based on the MinIO installation above. If you are using a different object store, please update the values accordingly.

```bash
cat << EOF > parseable-env-secret
s3.url=http://minio.minio.svc.cluster.local:9000
s3.access.key=minioadmin
s3.secret.key=minioadmin
s3.region=us-east-1
s3.bucket=parseable
addr=0.0.0.0:8000
staging.dir=./staging
fs.dir=./data
username=admin
password=admin
EOF
```

You can add additional environment variables to the `parseable-env-secret` file as needed. You can find the details of all the environment variables in the [Environment Variables](/docs/self-hosted/configuration) section.

After this, create the secret in Kubernetes.

```bash
kubectl create ns parseable
kubectl create secret generic parseable-env-secret --from-env-file=parseable-env-secret -n parseable
```

### Install Parseable

```bash
helm repo add parseable https://charts.parseable.com/
helm install parseable parseable/parseable -n parseable --set "parseable.highAvailability.enabled=true" --set "parseable.store=s3-store" --set "parseable.s3ModeSecret.enabled=true"
```

<Callout type="info">
  Note that `parseable.highAvailability.enabled=true` flag enables high availability mode. By default, the helm chart installs 3 Parseable ingest services and 1 Parseable query service. It also creates a ClusterIP service for Parseable ingestors.
</Callout>

### Access Parseable

Since we're running Parseable in a distributed mode, the ingestor service and querier services are different. Any log agent or client should send events to the `parseable-ingestor-service` service. To expose the ingress service, you can use the following command:

```bash
kubectl port-forward svc/parseable-ingestor-service 8000:80 -n parseable
```

To access thePrism, you'll need to expose the `parseable-querier-service` service:

```bash
kubectl port-forward svc/parseable-querier-service 8001:80 -n parseable
```

You should now be able to point your browser to `http://localhost:8001` and see the Parseable login page. You can login with the values set in `username` and `password` fields in the `parseable-env-secret` file above.

## Migration

This section is for users using Parseable helm chart version `1.3.1` or previous. Parseable release `v1.4.0` introduced a hot-tier mechanism for query nodes. Accordingly, the query nodes in the helm chart are now deployed as a StatefulSet instead of a Deployment. The helm chart version `1.4.0` and above removes the Deployment and creates a StatefulSet for query nodes.

Since distributed mode always runs with S3 store mode, the data is stored remotely and there is no manual migration required. If you face any issues during the upgrade, please reach out to us in the [community Slack](https://logg.ing/community).


# Linux (/docs/self-hosted/installation/distributed/linux)



This page explains the steps required to setup systemd service for Parseable distributed cluster in S3 storage mode.

## Prerequisites

* Parseable binary is available at `/usr/local/bin/`. Download the relevant binary from the release page.
* S3 or compatible object store URL, access key, secret key, and bucket name to be used as storage.
* Identify at least two servers to run Parseable ingestor and query services.

## Set up Parseable query server

Log on to the query node and create a configuration file for the query. Please ensure to replace the placeholders with the relevant values.

```bash
cat <<EOT >> /etc/default/parseable
P_USERNAME=admin
P_PASSWORD=admin
P_STAGING_DIR="/var/lib/parseable/staging"
P_ADDR=0.0.0.0:8000
P_S3_URL="https://s3.<region>.amazonaws.com"
P_S3_BUCKET=<s3-bucket>
P_S3_ACCESS_KEY=<access-key>
P_S3_SECRET_KEY=<secret-key>
P_S3_REGION=<region>
P_MODE=query
EOT
```

You can add additional environment variables to the `/etc/default/parseable` file as needed. You can find the details of all the environment variables in the [Environment Variables](/docs/self-hosted/configuration) section.

Download `parseable.s3.service` in `/etc/systemd/system/`:

```bash
cd /etc/systemd/system/
curl -O https://raw.githubusercontent.com/parseablehq/parseable/main/systemd/parseable.s3.service
```

### Start/Stop the query service

Once the service file is created, reload the systemd daemon and start the service.

```bash
systemctl enable parseable.s3.service
service parseable.s3 start
```

You can check the status of the service using the following command:

```bash
service parseable.s3 status
```

You can now access Parseable at the address [http://localhost:8000](http://localhost:8000) (default configuration). If you added P\_ADDR in config file, please access the correct URL accordingly.

To check logs, use journalctl, like:

```bash
journalctl -eu parseable.s3.service
```

In case you want to disable / uninstall Parseable, run the below command:

```bash
systemctl disable parseable.s3.service
```

### Set up Parseable ingestor server

Log on to each ingestor node and create a configuration file for the ingestor. Please make sure to replace the placeholders with the appropriate values.

```bash
cat <<EOT >> /etc/default/parseable
P_USERNAME=admin
P_PASSWORD=admin
P_STAGING_DIR="/var/lib/parseable/staging"
P_ADDR=0.0.0.0:8000
P_S3_URL="https://s3.<region>.amazonaws.com"
P_S3_BUCKET=<s3-bucket>
P_S3_ACCESS_KEY=<access-key>
P_S3_SECRET_KEY=<secret-key>
P_S3_REGION=<region>
P_MODE=ingest
P_INGESTOR_ENDPOINT="<public IP of this server>:<port>"
EOT
```

Download `parseable.s3.service` in `/etc/systemd/system/`:

```bash
cd /etc/systemd/system/
curl -O https://raw.githubusercontent.com/parseablehq/parseable/main/systemd/parseable.s3.service
```

#### Start/Stop the ingest service

Once the service file is created, reload the systemd daemon and start the service.

```bash
systemctl enable parseable.s3.service
service parseable.s3 start
```

You can check the status of the service using the following command.

```bash
service parseable.s3 status
```

You can now access Parseable at the address [http://localhost:8000](http://localhost:8000) (default configuration). If you added P\_ADDR to the config file, please access the correct URL accordingly.

To check logs, use journalctl, like:

```bash
journalctl -eu parseable.s3.service
```

In case you want to disable / uninstall Parseable, run the below command:

```bash
systemctl disable parseable.s3.service
```


# AWS ECS (/docs/self-hosted/installation/standalone/aws-ecs)



This guide will help you setup Parseable on AWS ECS with Fargate. Amazon ECS is a highly scalable and fast container management service that makes it easy to run, stop, and manage containers on a cluster. Amazon ECS can use EC2 or Fargate to manage the underlying infrastructure.

AWS Fargate is a serverless technology that you can use with ECS to run containers without having to manage servers or clusters of Amazon EC2 instances. Read more about Fargate in the [AWS documentation](https://aws.amazon.com/fargate/).

## Prerequisites

* AWS account with access to ECS and Fargate.
* VPC and Security Group are configured to allow inbound traffic on port 80/443.
* Define the Task IAM role and set policies according to [Task IAM Roles](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html).

Refer the [ECS Prerequisites section of AWS documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/prerequisites.html) for specific details on VPC and Security Group configuration.

### Create a ECS cluster

On the AWS management console, navigate to ECS and click on Clusters. Click on Create Cluster. Enter a name for the cluster and click on Create.

AWS Docs - [Create a Cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started-fargate.html#get-started-windows-fargate-cluster)

### Create Task Definition

To create Parseable task definition, choose Task Definitions in the navigation pane. Then Choose **Create new Task Definition** and then **Create new revision with JSON**.

Copy the following JSON to a local text editor and replace the values for `P_S3_BUCKET`, `P_S3_ACCESS_KEY`, `P_S3_SECRET_KEY`, `P_S3_REGION`, `P_USERNAME` and `P_PASSWORD` with your own values. Also replace the image value with the relevant Parseable Docker image version.

Then paste the updated JSON in the Task Definition text box and click on Save.

```json
{
    "family": "parseable-server", 
    "networkMode": "awsvpc", 
    "containerDefinitions": [
        {
            "name": "parseable", 
            "image": "parseable/parseable:latest", 
            "portMappings": [
                {
                    "containerPort": 80, 
                    "hostPort": 80, 
                    "protocol": "tcp"
                }
            ], 
            "environment": [
                {
                    "name": "P_ADDR",
                    "value": "0.0.0.0:80"
                },
                {
                    "name": "P_S3_URL",
                    "value": "https://s3.<region>.amazonaws.com"
                },
                {
                    "name": "P_S3_BUCKET",
                    "value": "<replace-with-bucket-name>"
                },
                {
                    "name": "P_S3_REGION",
                    "value": "<replace-with-region>"
                },
                {
                    "name": "P_USERNAME",
                    "value": "<replace-with-difficult-to-guess-string>"
                },
                {
                    "name": "P_PASSWORD",
                    "value": "<replace-with-difficult-to-guess-string>"
                }
            ],
            "essential": true, 
            "command": [
                "parseable", "s3-store"
            ]
        }
    ], 
    "requiresCompatibilities": [
        "FARGATE"
    ], 
    "cpu": "4000", 
    "memory": "4096"
}
```

You can add additional environment variables to the task definition as needed. You can find the details of all the environment variables in the [Environment Variables](/docs/self-hosted/configuration) section.

### Create Service

Create a service using the task definition.

* In the navigation pane, choose Clusters, and then select the cluster you created in the first step.

* From the Services tab, choose Create.

* Under Deployment configuration, specify how your application is deployed.

  * For Task definition, choose the task definition from family `parseable-server` and revision 1.

  * For Service name, enter a name for your service.

  * For Desired tasks, enter 1 (we recommend starting with 1 task).

* Choose Deploy.

### Access Parseable

You can access Parseable using the public IP address of the task. To find the public IP address, choose the task from the Tasks tab. Then choose the Configuration tab and look for the public IP address.


# AWS EKS (/docs/self-hosted/installation/standalone/aws-eks)



This page explains additional EKS specific features and configuration options for Parseable. For general Parseable installation instructions, see [installation documentation](/docs/self-hosted/installation).

## Setup IAM roles for service accounts (IRSA)

IAM roles for service accounts provide the ability to manage credentials for Parseable, similar to the way that Amazon EC2 instance profiles provide credentials to Amazon EC2 instances. Instead of creating and distributing your AWS credentials to the Parseable container or using the Amazon EC2 instance's role, you associate an IAM role with a Kubernetes service account and configure Parseable to use the service account.

Read more in the [AWS documentation](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html).

Here are the steps to set up IRSA for Parseable:

### Create IAM OIDC provider

Refer to the [AWS documentation](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html).

### Create an IAM Policy

Parseable requires the below permissions to run on S3. (replace `bucket-name` with your bucket name). Complete list of S3 actions is available [here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-actions.html).

```bash
cat >parseable-policy.json <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetBucketLocation",
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject",
                "s3:ListObjectsV2"
            ],
            "Resource": [
                "arn:aws:s3:::bucket-name",
                "arn:aws:s3:::bucket-name/*"
            ]
        }
    ]
}
EOF
```

```bash
aws iam create-policy --policy-name parseable-policy --policy-document file://parseable-policy.json
```

### Create an IAM role and associate it with a Kubernetes service account

We'll use `eksctl` for this step. You can also use the AWS CLI. Use the below command to create the IAM role and the service account. Replace `my-service-account` with the name of the Kubernetes service account that you want `eksctl` to create and associate with an IAM role. Replace `default` with the namespace that you want `eksctl` to create the service account in. Replace `my-cluster` with the name of your cluster. Replace `111122223333` with your account ID.

```bash
eksctl create iamserviceaccount --name my-service-account --namespace default --cluster my-cluster --role-name "parseable-role" --attach-policy-arn arn:aws:iam::111122223333:policy/parseable-policy --approve
```

### Configure Parseable to use the service account

You can now refer to the standard Kubernetes documentation for Parseable installation, with Helm Chart or the Kubernetes Operator. Just ensure to use the service account you created above.

If you're using Parseable Helm Chart, set `serviceAccount.create` to `false` and `serviceAccount.name` to the name of the service account you created above. For example `my-service-account`.

If you're using the Parseable Operator, set `serviceAccountName` under the `k8sConfig` section. Refer to a sample CR example [here](https://github.com/parseablehq/operator/blob/main/config/samples/parseable-persistent.yaml).


# Docker (/docs/self-hosted/installation/standalone/docker)



This document explains how to set up Parseable in standalone mode on Docker with `s3-store` mode. This mode is used to store logs on S3 or compatible object storage.

## Prerequisites

* S3 or a compatible object storage URL.
* Credentials to read / write access the object storage.
* Bucket created on object storage.
* Docker is now installed on your machine. Refer to [this doc](https://www.docker.com/products/docker-desktop/) to install Docker if you haven't already.

## Setup env file

We'll create an env file with all the config fields for Parseable. Use the command below to create the file. Note that fields need to be set after you create the file.

```bash
cat << EOF > parseable-env
P_STAGING_DIR=/staging
P_ADDR=0.0.0.0:8000
P_USERNAME=<username-to-be-set-for-parseable>
P_PASSWORD=<password-to-be-set-for-parseable>
P_S3_URL=<s3-url>
P_S3_BUCKET=<s3-bucket>
P_S3_ACCESS_KEY=<access-key>
P_S3_SECRET_KEY=<secret-key>
P_S3_REGION=<region>
EOF
```

You can add additional environment variables to the `parseable-env` file as needed. You can find the details of all the environment variables in the [Environment Variables](/docs/self-hosted/configuration) section.

## Run Parseable

Parseable needs a local directory for staging log data, before sending it to object storage (configurable via `P_STAGING_DIR` field in the env file). Assuming you've set the `P_STAGING_DIR` field to `/staging` and want to mount that volume to a local path `/parseable/staging`, run the below command.

```bash
mkdir /parseable/staging

docker run \
  -p 8000:8000 \
  --env-file parseable-env \
  -v /parseable/staging:/staging \
  parseable/parseable:latest \
  parseable s3-store
```

<Callout type="info">
  Since Parseable runs as user parseable inside the container, you'll need to make sure that the local path /data/parseable is owned by user parseable (`uid: 10001`). You can do that by running `chown -R 10001:10001 /data/parseable` on the host machine.
</Callout>

## Access Parseable

Once Parseable is up and running, you can access it at `http://localhost:8000` (assuming you've set `P_ADDR` to `:8000` in the env file). Credentials to login to Parseable are set via `P_USERNAME` and `P_PASSWORD` fields in the env file.

## Troubleshoot

### Running docker on AWS EC2

When trying to fetch credentials over IMDSv2 inside a docker container the client can hang indefinitely. This can happen due to AWS not allowing more than 1 hop in IMDSv2 endpoint response. You can change this configuration, please refer to the consideration section of [retrieve instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html#imds-considerations).


# Kubernetes (/docs/self-hosted/installation/standalone/k8s)



This page explains the steps required to setup Parseable (in S3 or Local mode) on Kubernetes via Helm.

### Prerequisites

* `kubectl` and `helm` installed and configured to point to relevant Kubernetes clusters.

### Setup Parseable with Local Storage

#### Create configuration secret

Create a secret file with the configuration for Parseable.

```bash
cat << EOF > parseable-env-secret
addr=0.0.0.0:8000
staging.dir=./staging
fs.dir=./data
username=admin
password=admin
EOF
```

You can add additional environment variables to the `parseable-env-secret` file as needed. You can find the details of all the environment variables in the [Environment Variables](/docs/self-hosted/configuration) section.

Then create the secret in Kubernetes.

```bash
kubectl create ns parseable
kubectl create secret generic parseable-env-secret --from-env-file=parseable-env-secret -n parseable
```

#### Install Parseable

```bash
helm repo add parseable https://charts.parseable.com
helm install parseable parseable/parseable -n parseable --set "parseable.local=true"
kubectl port-forward svc/parseable 8000:80 -n parseable
```

You should now be able to point your browser to `http://localhost:8000` and see the Parseable login page. You can login with the values set in the username and password fields in the `parseable-env-secret` file above.

### Setup Parseable with S3 Storage

#### Setup object store

This step is required only if you want to setup [MinIO](https://min.io/) as the backend for Parseable. Please skip this step if you have another object store, like S3, already available.

```bash
helm repo add minio https://charts.min.io/
helm install --namespace minio --create-namespace --set "buckets[0].name=parseable,buckets[0].policy=none,buckets[0].purge=false,rootUser=minioadmin,rootPassword=minioadmin,replicas=1,persistence.enabled=false,resources.requests.memory=128Mi,mode=standalone" minio minio/minio
kubectl port-forward svc/minio-console -n minio 9001:9001
```

You can now access the MinIO console on [http://localhost:9001](http://localhost:9001). You should see a bucket called `parseable` created.

<Callout type="info">
  MinIO installation steps above are for testing purposes only. For production, please refer to the [MinIO documentation](https://min.io/docs/minio).
</Callout>

#### Create configuration secret

Create a secret file with the configuration for Parseable. Note that the values set below are based on the MinIO installation above. If you are using a different object store, please update the values accordingly.

```bash
cat << EOF > parseable-env-secret
s3.url=http://minio.minio.svc.cluster.local:9000
s3.access.key=minioadmin
s3.secret.key=minioadmin
s3.region=us-east-1
s3.bucket=parseable
addr=0.0.0.0:8000
staging.dir=./staging
fs.dir=./data
username=admin
password=admin
EOF
```

Then create the secret in Kubernetes.

```bash
kubectl create ns parseable
kubectl create secret generic parseable-env-secret --from-env-file=parseable-env-secret -n parseable
```

#### Install Parseable

```bash
helm repo add parseable https://charts.parseable.com
helm install parseable parseable/parseable -n parseable
kubectl port-forward svc/parseable 8000:80 -n parseable
```

You should now be able to point your browser to `http://localhost:8000` and see the Parseable login page. You can login with the values set in the username and password fields in the `parseable-env-secret` file above.


# Linux (/docs/self-hosted/installation/standalone/linux)



This page explains the steps required to setup a systemd service for Parseable server in both S3 and local store mode.

<Callout type="warn">
  The local store mode is recommended for testing purposes only. For production use, we recommend using S3 storage.
</Callout>

## Prerequisites

Parseable binary is available at `/usr/local/bin/`. Download the relevant binary from the release page.

## Create configuration

```bash
cat <<EOT >> /etc/default/parseable
P_USERNAME="parseable"
P_PASSWORD="parseable"
P_ADDR="0.0.0.0:8000"
P_STAGING_DIR="/var/lib/parseable/staging"
P_FS_DIR="/var/lib/parseable/data"
EOT
```

You can add additional environment variables to the `/etc/default/parseable` file as needed. You can find the details of all the environment variables in the [Environment Variables](/docs/self-hosted/configuration) section.

Download `parseable.local.service` in `/etc/systemd/system/`:

```bash
( cd /etc/systemd/system/; curl -O https://raw.githubusercontent.com/parseablehq/parseable/main/systemd/parseable.local.service )
```

### Start/Stop the service

Once the service file is created, reload the systemd daemon and start the service.

```bash
systemctl enable parseable.local.service
service parseable start
```

You can check the status of the service using the following command.

```bash
service parseable status
```

You can now access Parseable at the address `http://localhost:8000` (default configuration). If you added `P_ADDR` to the config file, please access the correct URL accordingly.

To check logs, use `journalctl`, like:

```bash
journalctl -eu parseable.local.service
```

If you want to disable / uninstall Parseable, run the below command.

```bash
systemctl disable parseable.local.service
```

## Setup Parseable with S3 Storage

Prerequisites

* Parseable binary is available at `/usr/local/bin/`. Download the relevant binary from the [release page](https://github.com/parseablehq/parseable/releases).
* S3 or compatible object store URL, access key, secret key, and bucket name to be used as storage.

## Create configuration

Please ensure to replace the placeholders with the relevant values.

```bash
cat <<EOT >> /etc/default/parseable
P_USERNAME=<username>
P_PASSWORD=<password>
P_ADDR="0.0.0.0:8000"
P_STAGING_DIR="/var/lib/parseable/staging"
P_S3_BUCKET=<s3-bucket>
P_S3_ACCESS_KEY=<access-key>
P_S3_SECRET_KEY=<secret-key>
P_S3_REGION=<region>
P_S3_URL="https://s3.<region>.amazonaws.com"
EOT
```

Download `parseable.s3.service` in `/etc/systemd/system/`:

```bash
cd /etc/systemd/system/
curl -O https://raw.githubusercontent.com/parseablehq/parseable/main/systemd/parseable.s3.service
```

### Start/Stop the service

Once the service file is created, reload the systemd daemon and start the service.

```bash
systemctl enable parseable.s3.service
service parseable start
```

You can check the status of the service using the following command.

```bash
service parseable status
```

You can now access Parseable at the address `http://localhost:8000` (default configuration). If you added `P_ADDR` to the config file, please access the correct URL accordingly.

To check logs, use `journalctl`, like:

```bash
journalctl -eu parseable.s3.service
```

In case you want to disable or uninstall Parseable, run the below given command.

```bash
systemctl disable parseable.s3.service
```


# Delete a log dataset (/docs/api/v1/logstream/stream_name/delete)



{/* Define variables for path parameters */}

export const stream_name = "stream_name";

{/* This file was generated by Fumadocs. Do not edit this file directly. Any changes should be made by running the generation command again. */}

This endpoint is used to delete an existing log dataset.
When a log dataset is deleted, all associated data is permanently removed.

<APIPage document={"public/parseable-api-schema-cleaned.yaml"} operations={[{"path":"/api/v1/logstream/{stream_name}","method":"delete"}]} webhooks={[]} hasHead={false} />


# Send logs to a dataset (/docs/api/v1/logstream/stream_name/post)



{/* Define variables for path parameters */}

export const stream_name = "stream_name";

{/* This file was generated by Fumadocs. Do not edit this file directly. Any changes should be made by running the generation command again. */}

**Log Ingestion API via Stream Endpoint**\
In this approach, you need to create a dataset first using the **Create Stream API**.\
Once the dataset is created, you can send logs to the dataset ingestion API endpoint:\
**http\://INGESTION\_ENDPOINT/api/v1/logstream/`stream_name`**\
This API does not require any headers for specifying the dataset name.

<APIPage document={"public/parseable-api-schema-cleaned.yaml"} operations={[{"path":"/api/v1/logstream/{stream_name}","method":"post"}]} webhooks={[]} hasHead={false} />


# Create a log dataset (/docs/api/v1/logstream/stream_name/put)



{/* Define variables for path parameters */}

export const stream_name = "stream_name";

{/* This file was generated by Fumadocs. Do not edit this file directly. Any changes should be made by running the generation command again. */}

This endpoint is used to create a new log dataset within Parseable.\
A **log dataset** is a group of similar logs. For example, you can create a log dataset for a specific application's logs, another log dataset for your database logs, and so on. You can create as many log streams as needed to organize and manage logs efficiently.

<APIPage document={"public/parseable-api-schema-cleaned.yaml"} operations={[{"path":"/api/v1/logstream/{stream_name}","method":"put"}]} webhooks={[]} hasHead={false} />
