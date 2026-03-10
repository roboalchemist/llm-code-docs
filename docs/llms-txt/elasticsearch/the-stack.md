# Source: https://www.elastic.co/docs/get-started/the-stack

﻿---
title: The Elastic Stack
description: The {{stack}} is a group of products that work together to securely store, search, analyze, and visualize your data.
url: https://www.elastic.co/docs/get-started/the-stack
products:
  - Elastic Stack
applies_to:
  - Elastic Cloud Serverless: Generally available
  - Elastic Stack: Generally available
---

# The Elastic Stack
All Elastic [deployments and projects](https://www.elastic.co/docs/get-started/deployment-options) share the same open source foundation:
- [Elasticsearch](#stack-components-elasticsearch): The distributed data store and search engine that handles indexing, querying, and analytics.
- [Kibana](#stack-components-kibana): The user interface with dashboards, visualizations, and management tools.

Depending on your use case, you might need to install more products that work together with Elasticsearch and Kibana (referred to as the [Elastic Stack](https://www.elastic.co/elastic-stack) or ELK). For example:
- [Elastic Agent](#stack-components-agent): A lightweight data shipper that collects and forwards data to Elasticsearch.
- [Logstash](#stack-components-logstash): The data ingestion and transformation engine, often used for more complex ETL (extract, transform, load) pipelines.


The Elastic Stack includes products for [ingesting](#_ingest), [storing](#_store), and [exploring](#_consume) data at scale:
![Components of the Elastic Stack](https://www.elastic.co/docs/get-started/images/platform-components-diagram.svg)
Continue reading to learn how these products work together.

## Store, search, and analyze

All deployments include Elasticsearch.
Elasticsearch is the distributed search and analytics engine, scalable data store, and vector database at the heart of all Elastic deployments and solutions.
You can use the Elasticsearch clients to access data directly by using common programming languages.

### Elasticsearch

Elasticsearch is a data store and [vector database](https://www.elastic.co/elasticsearch/vector-database) that provides near real-time search and analytics for all types of data.
Whether you have structured or unstructured text, time series (timestamped) data, vectors, or geospatial data, Elasticsearch can efficiently store and index it in a way that supports fast searches.
It also includes multiple query languages, aggregations, and robust features for [querying and filtering](https://www.elastic.co/docs/explore-analyze/query-filter) your data.
Elasticsearch is built to be a resilient and scalable distributed system.
It runs as a cluster of one or more servers, called nodes.
When you add data to an index, which is the fundamental unit of storage in Elasticsearch, it's divided into pieces called shards, which are spread across the various nodes in the cluster.
This architecture allows Elasticsearch to handle large volumes of data and ensures that your data remains available even if a node fails.
If you use Elastic Cloud Serverless, it has a unique [Search AI Lake cloud-native architecture](https://www.elastic.co/cloud/serverless/search-ai-lake) and automates the nodes, shards, and replicas for you.
Elasticsearch also includes [AI-powered features](https://www.elastic.co/docs/explore-analyze/ai-features) and built-in natural language processing (NLP) models that enable you to make predictions, run inference, and integrate with LLMs faster.
Nearly every aspect of Elasticsearch can be configured and managed programmatically through its REST APIs.
This allows you to automate repetitive tasks and integrate Elastic management into your existing operational workflows.
For example, you can use the APIs to manage indices, update cluster settings, run complex queries, and configure security.
This API-first approach is fundamental to enabling infrastructure-as-code practices and managing deployments at scale.
Learn more about [the Elasticsearch data store](https://www.elastic.co/docs/manage-data/data-store), its [distributed architecture](https://www.elastic.co/docs/deploy-manage/distributed-architecture), and [APIs](https://www.elastic.co/docs/reference/elasticsearch/rest-apis).

### Elasticsearch clients

The clients provide a convenient mechanism to manage API requests and responses to and from Elasticsearch from popular languages such as Java, Ruby, Go, and Python.
Both official and community contributed clients are available.
[Learn more about the Elasticsearch clients](https://www.elastic.co/docs/reference/elasticsearch-clients).

## Explore and visualize

Use Kibana to explore, manage, and visualize the data that's stored in Elasticsearch and to manage components of the Elastic Stack.

### Kibana

Kibana provides the user interface for all Elastic [solutions](https://www.elastic.co/docs/get-started/introduction) and Serverless projects.
It's a powerful tool for visualizing and analyzing your data and for managing and monitoring the Elastic Stack.
Although you can use Elasticsearch without it, Kibana is required for most use cases and is included by default when you deploy using some deployment types, including Elastic Cloud Serverless.
With Kibana, you can:
- Use [Discover](https://www.elastic.co/docs/explore-analyze/discover) to interactively search and filter your raw data.
- Build custom [visualizations](https://www.elastic.co/docs/explore-analyze/visualize) like charts, graphs, and metrics with tools like **Lens**, which offers a drag-and-drop experience.
- Assemble your visualizations into interactive [dashboards](https://www.elastic.co/docs/explore-analyze/dashboards) to get a comprehensive overview of your information.
- Perform [geospatial analysis](https://www.elastic.co/docs/explore-analyze/geospatial-analysis) and add maps to your dashboards.
- Configure notifications for significant data events and track incidents with [alerts and cases](https://www.elastic.co/docs/explore-analyze/alerting).
- Manage resources such as processors, pipelines, data streams, trained models, and more.

Each solution or project type provides access to customized features in Kibana such as built-in dashboards and [AI assistants](https://www.elastic.co/docs/explore-analyze/ai-features/ai-chat-experiences/ai-assistant).
Kibana also has [query tools](https://www.elastic.co/docs/explore-analyze/query-filter/tools) such as **Console**, which provides an interactive way to send requests directly to the Elasticsearch API and view the responses.
For secure, automated access, you can create and manage API keys to authenticate your scripts and applications.
Learn more in [Explore and analyze data with Kibana](https://www.elastic.co/docs/explore-analyze).

## Ingest

Before you can search it, visualize it, and use it for insights, you must get your data into Elasticsearch.
There are multiple methods for ingesting data.
The best approach depends on the type of data and your specific use case.
For example, you can collect and ship logs, metrics, and other types of data with Elastic Agent or collect detailed performance information with APM.
If you want to transform and enrich data before it's stored, you can use Elasticsearch ingest pipelines or Logstash.
Trying to decide which ingest components to use? Refer to [Ingest: Bring your data to Elastic](https://www.elastic.co/docs/manage-data/ingest) and [Ingest tools overview](https://www.elastic.co/docs/manage-data/ingest/tools).

### Elastic Agent and Integrations

Elastic Agent is a single, unified way to add monitoring for logs, metrics, and other types of data to a host.
It can also protect hosts from security threats, query data from operating systems, and forward data from remote services or hardware.
Each agent has a single policy to which you can add [integrations](https://www.elastic.co/docs/reference/integrations) for new data sources, security protections, and more.
You can also use [Elastic Agent processors](https://www.elastic.co/docs/reference/fleet/agent-processors) to sanitize or enrich your data.
To monitor the state of all your Elastic Agents, manage agent policies, and upgrade Elastic Agent binaries or integrations, refer to [Central management in Fleet](/docs/reference/fleet#central-management).
[Learn more about Elastic Agent](https://www.elastic.co/docs/reference/fleet).

### APM

APM is an application performance monitoring system.
It allows you to monitor software services and applications in real-time by collecting detailed performance information on response time for incoming requests, database queries, calls to caches, external HTTP requests, and more.
This makes it easy to pinpoint and fix performance problems quickly.
[Learn more about APM](https://www.elastic.co/docs/solutions/observability/apm).

### OpenTelemetry Collector

[OpenTelemetry](https://opentelemetry.io/docs) is a vendor-neutral observability framework for collecting, processing, and exporting telemetry data. Elastic is a member of the Cloud Native Computing Foundation (CNCF) and active contributor to the OpenTelemetry project.
In addition to supporting upstream OTel development, Elastic provides [Elastic Distributions of OpenTelemetry](https://www.elastic.co/docs/reference/opentelemetry), specifically designed to work with Elastic Observability.
With EDOT, you can use vendor-neutral instrumentation and stream native OTel data such as standardized traces, metrics, and logs without proprietary agents.

### Beats

[Beats](https://www.elastic.co/docs/reference/beats) open source data shippers that you install as agents on your servers to send operational data to Elasticsearch. Elastic provides separate Beats for different types of data, such as logs, metrics, and uptime.
Beats has been replaced by Elastic Agent for most use cases. When you use Elastic Agent, you’re getting core Beats functionality, but with more added features. Where you might need to install multiple Beats shippers on a host depending on your data requirements, single Elastic Agent installed on a host can collect and transport multiple types of data.
[Learn more about Beats](https://www.elastic.co/docs/reference/beats).

### Elasticsearch ingest pipelines

Ingest pipelines let you perform common transformations on your data before indexing them into Elasticsearch.
You can configure one or more "processor" tasks to run sequentially, making specific changes to your documents before storing them in Elasticsearch.
[Learn more about ingest pipelines](https://www.elastic.co/docs/manage-data/ingest/transform-enrich/ingest-pipelines).

### Logstash

Logstash is a data collection engine with real-time pipelining capabilities.
It can dynamically unify data from disparate sources and normalize the data into destinations of your choice.
Logstash supports a broad array of input, filter, and output plugins, with many native codecs further simplifying the ingestion process.
[Learn more about Logstash](https://www.elastic.co/docs/reference/logstash).

## Installation details

<applies-to>
  - Elastic Cloud Serverless: Unavailable
</applies-to>

When installing the Elastic Stack, you must use the same version across the entire stack. For example, if you are using Elasticsearch 9.3.1, you install Beats 9.3.1, APM Server 9.3.1, Elasticsearch Hadoop 9.3.1, Kibana 9.3.1, and Logstash 9.3.1.
If you’re upgrading an existing installation, see [Upgrade your deployment, cluster, or orchestrator](https://www.elastic.co/docs/deploy-manage/upgrade) for information about how to ensure compatibility with 9.3.1.

If you're deploying the Elastic Stack in a self-managed cluster, then install the Elastic Stack products you want to use in the following order:
- [Elasticsearch](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/installing-elasticsearch)
- [Kibana](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/install-kibana)
- [Logstash](https://www.elastic.co/docs/reference/logstash)
- [Elastic Agent](https://www.elastic.co/docs/reference/fleet) or [Beats](https://www.elastic.co/docs/reference/beats)
- [APM](https://www.elastic.co/docs/solutions/observability/apm)
- [Elasticsearch Hadoop](https://www.elastic.co/docs/reference/elasticsearch-hadoop)

Installing in this order ensures that the components each product depends on are in place.
<tip>
  If you're deploying a production environment and you plan to use [trusted CA-signed certificates](/docs/deploy-manage/security/self-setup#manual-configuration) for Elasticsearch, then you should do so before you deploy Fleet and Elastic Agent. If new security certificates are configured, any Elastic Agents need to be reinstalled, so we recommend that you set up Fleet and Elastic Agent with the appropriate certificates in place.
</tip>