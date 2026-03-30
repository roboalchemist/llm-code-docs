# Source: https://www.elastic.co/docs/deploy-manage/deploy

﻿---
title: Deploy
description: Whether you're planning to use Elastic's pre-built solutions or Serverless projects, build your own applications with Elasticsearch, or analyze your data...
url: https://www.elastic.co/docs/deploy-manage/deploy
products:
  - Elastic Cloud Serverless
  - Elastic Stack
  - Elasticsearch
---

# Deploy
Whether you're planning to use Elastic's pre-built solutions or Serverless projects, build your own applications with Elasticsearch, or analyze your data using Kibana tools, you need to deploy Elastic first.
This page will help you understand your deployment options and choose the approach that best fits your needs.

## Core components

All deployments include **Elasticsearch**. Elasticsearch is the distributed search and analytics engine, scalable data store, and vector database at the heart of all Elastic solutions.
In most cases, you also need to deploy **Kibana**. Kibana provides the user interface for all Elastic solutions and Serverless projects. It’s a powerful tool for visualizing and analyzing your data, and for managing and monitoring the Elastic Stack. Although Kibana is not required to use Elasticsearch, it's required for most use cases, and is included by default when you deploy using certain deployment methods.
Your choice of deployment type determines how you'll set up and manage these core components, as well as any additional components you need.
<admonition title="Other Elastic Stack components">
  This section focuses on deploying and managing Elasticsearch and Kibana, as well as supporting orchestration technologies. However, depending on your use case, you might need to deploy [other Elastic Stack components](https://www.elastic.co/docs/get-started/the-stack). For example, you might need to add components to ingest logs or metrics.To learn how to deploy optional Elastic Stack components, refer to the following sections:
  - [Fleet and Elastic Agent](https://www.elastic.co/docs/reference/fleet)
  - [APM](https://www.elastic.co/docs/solutions/observability/apm)
  - [Beats](https://www.elastic.co/docs/reference/beats)
  - [Logstash](https://www.elastic.co/docs/reference/logstash)
</admonition>


## Choosing your deployment type

**Quick start options**
- [**Elastic Cloud**](https://www.elastic.co/docs/deploy-manage/deploy/elastic-cloud): Get a hosted solution up and running in minutes.
  - [**Elastic Cloud Hosted**](https://www.elastic.co/docs/deploy-manage/deploy/elastic-cloud/cloud-hosted): Our hosted Elastic Stack offering, deployed in the cloud with your provider of choice. Sign up for a [14-day free trial](https://cloud.elastic.co/registration).
- [**Elastic Cloud Serverless**](https://www.elastic.co/docs/deploy-manage/deploy/elastic-cloud/serverless): Create serverless projects for autoscaled and fully managed Elastic deployments. Sign up for a [14-day free trial](https://cloud.elastic.co/serverless-registration).
- [**Local development**](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/local-development-installation-quickstart): Get started quickly with Elasticsearch and Kibana in Docker for local development and testing.

**Advanced options**
- [**Self-managed**](https://www.elastic.co/docs/deploy-manage/deploy/self-managed): Install, configure, and run Elastic on your own premises.
- [**Elastic Cloud Enterprise**](https://www.elastic.co/docs/deploy-manage/deploy/cloud-enterprise): Deploy Elastic Cloud on public or private clouds, virtual machines, or your own premises.
- [**Elastic Cloud on Kubernetes**](https://www.elastic.co/docs/deploy-manage/deploy/cloud-on-k8s): Deploy Elastic Cloud on Kubernetes.

<tip>
  Documentation will specify when certain features or configurations are not applicable to specific deployment types.
</tip>


### Who manages the infrastructure?


#### Managed by Elastic

If you want to focus on using Elastic products rather than managing infrastructure, choose one of the following options:
- **Elastic Cloud Serverless**: Zero operational overhead, automatic scaling and updates, latest features
- **Elastic Cloud Hosted**: Balance of control and managed operations, choice of resources and regions

Both of these options use [Elastic Cloud](https://www.elastic.co/docs/deploy-manage/deploy/elastic-cloud) as the orchestration platform.

#### Self-hosted options

If you need to run Elastic on your infrastructure, choose between a fully self-managed deployment or using an orchestrator:
- **Fully self-managed**: Complete control and responsibility for your Elastic deployment
- **With orchestration**:
  - **Elastic Cloud on Kubernetes (ECK)**: If you need Kubernetes-native orchestration
- **Elastic Cloud Enterprise (ECE)**: If you need a multi-tenant orchestration platform

<admonition title="Use cloud services in your self-hosted environment with Cloud Connect">
  With [Cloud Connect](https://www.elastic.co/docs/deploy-manage/cloud-connect), you can use Elastic-managed cloud services in your self-managed, ECE, or ECK environment without having to install and manage their infrastructure yourself. In this way, you can get faster access to new features without adding to your operational overhead.
</admonition>


### About orchestration

An orchestrator automates the deployment and management of multiple Elastic clusters, handling tasks like scaling, upgrades, and monitoring.
Consider orchestration in the following cases:
- You need to manage multiple Elastic clusters
- You want automated operations at scale
- You have a Kubernetes environment (ECK)
- You need to build a multi-tenant platform (ECE)

Orchestrators manage the lifecycle of your Elastic deployments but don't change how the core products work. When using an orchestrated deployment:
- You'll still use the same Elasticsearch and Kibana features and configurations
- Most product documentation remains applicable
- You can add other Elastic products as needed
- The orchestrator handles operational tasks while you focus on using and configuring the products


### Versioning and compatibility

In Elastic Cloud Serverless, you automatically get access to the latest versions of Elastic features and you don't need to manage version compatibility.
With other deployment types (fully self-managed, ECH, ECE, and ECK), you control which Elastic Stack versions you deploy and when you upgrade. The ECE and ECK orchestrators themselves also receive regular version updates, independent of the Elastic Stack versions they manage.
Consider this when choosing your deployment type:
- Choose Elastic Cloud Serverless if you want automatic access to the latest features and don't want to manage version compatibility
- Choose other deployment types if you need more control over version management

<tip>
  Learn more about [versioning and availability](https://www.elastic.co/docs/get-started/versioning-availability).
</tip>


### Cost considerations

- **Elastic Cloud Serverless**: Pay for what you use
- **Elastic Cloud Hosted**: Subscription-based with resource allocation
- **Self-hosted options**, **including fully self-managed, ECE, and ECK**: Infrastructure costs plus operational overhead mean a higher total cost of ownership (TCO)

<tip>
  For a detailed comparison of features and capabilities across deployment types, see the [Detailed deployment comparison](https://www.elastic.co/docs/deploy-manage/deploy/deployment-comparison).
</tip>