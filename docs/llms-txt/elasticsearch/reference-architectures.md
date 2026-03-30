# Source: https://www.elastic.co/docs/deploy-manage/reference-architectures

﻿---
title: Reference architectures
description: Elasticsearch reference architectures are blueprints for deploying Elasticsearch clusters tailored to different use cases. Whether you’re handling logs...
url: https://www.elastic.co/docs/deploy-manage/reference-architectures
products:
  - Elastic Cloud Enterprise
  - Elastic Cloud Hosted
  - Elastic Cloud on Kubernetes
  - Elasticsearch
applies_to:
  - Elastic Cloud Hosted: Generally available
  - Elastic Cloud on Kubernetes: Generally available
  - Elastic Cloud Enterprise: Generally available
  - Self-managed Elastic deployments: Generally available
---

# Reference architectures
Elasticsearch reference architectures are blueprints for deploying Elasticsearch clusters tailored to different use cases. Whether you’re handling logs or metrics these reference architectures focus on scalability, reliability, and cost efficiency. Use these guidelines to deploy Elasticsearch for your use case.
These architectures are designed by architects and engineers to provide standardized, proven solutions that help you to follow best practices when deploying Elasticsearch.
<tip>
  These architectures are specific to deploying Elastic on Elastic Cloud Hosted, Elastic Cloud on Kubernetes, Elastic Cloud Enterprise, or deploying a self-managed instance. If you are using Elastic Cloud Serverless, your Elasticsearch clusters are autoscaled and fully managed by Elastic. To learn about all of the deployment options, refer to the [Deploy and manage overview](https://www.elastic.co/docs/deploy-manage).
</tip>

These reference architectures are recommendations and should be adapted to fit your specific environment and needs. Each solution can vary based on the unique requirements and conditions of your deployment. In these architectures we discuss about how to deploy cluster components. For information about designing ingest architectures to feed content into your cluster, refer to [Ingest architectures](https://www.elastic.co/docs/manage-data/ingest/ingest-reference-architectures).

## Architectures


| Architecture                                                                                                                                                                                                             | When to use                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [*Hot/Frozen - High Availability*](https://www.elastic.co/docs/deploy-manage/reference-architectures/hotfrozen-high-availability)A high availability architecture that is cost optimized for large time-series datasets. | * Have a requirement for cost effective long term data storage (many months or years).* Provide insights and alerts using logs, metrics, traces, or various event types to ensure optimal performance and quick issue resolution for applications.* Apply Machine Learning and Search AI to assist in dealing with the large amount of data.* Deploy an architecture model that allows for maximum flexibility between storage cost and performance. |
| Additional architectures are on the way.Stay tuned for updates.                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |