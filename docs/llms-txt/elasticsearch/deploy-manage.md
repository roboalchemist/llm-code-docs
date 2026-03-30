# Source: https://www.elastic.co/docs/deploy-manage

﻿---
title: Deploy and manage
description: Deploy and manage your Elastic environment. Learn how to design resilient clusters, secure access, monitor performance, and maintain your Elastic Stack components across different deployment options.
url: https://www.elastic.co/docs/deploy-manage
products:
  - Elastic Cloud Enterprise
  - Elastic Cloud Hosted
  - Kibana
---

# Deploy and manage
To get started with Elastic, you need to choose a deployment method and deploy Elastic Stack components.
In this section, you'll learn about how to deploy and manage all aspects of your Elastic environment. You'll learn how to design resilient, highly available clusters and deployments, and how to maintain and scale your environment to grow with your use case.
This section focuses on deploying and managing the core components of the Elastic Stack: Elasticsearch and Kibana. It also documents deploying and managing supporting orchestration technologies. However, depending on your use case, you might need to deploy other components. [Learn more](https://www.elastic.co/docs/get-started/the-stack).
<tip>
  To get started quickly, you can set up a [local development and testing environment](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/local-development-installation-quickstart), or sign up for a [Serverless](https://cloud.elastic.co/serverless-registration) or [Hosted](https://cloud.elastic.co/registration) trial in Elastic Cloud.
</tip>


## Design and deploy

Learn how to design and deploy a production-ready Elastic environment.
- [Deploy](https://www.elastic.co/docs/deploy-manage/deploy): Understand your deployment options and choose the approach that best fits your needs.
  If you already know how you want to deploy, you can jump to the documentation for your preferred deployment method:
  - [Elastic Cloud Serverless](https://www.elastic.co/docs/deploy-manage/deploy/elastic-cloud/serverless)
- [Elastic Cloud Hosted](https://www.elastic.co/docs/deploy-manage/deploy/elastic-cloud/cloud-hosted)
- [Elastic Cloud Enterprise](https://www.elastic.co/docs/deploy-manage/deploy/cloud-enterprise)
- [Elastic Cloud on Kubernetes](https://www.elastic.co/docs/deploy-manage/deploy/cloud-on-k8s)
- [Self-managed](https://www.elastic.co/docs/deploy-manage/deploy/self-managed)
- [Distributed architecture](https://www.elastic.co/docs/deploy-manage/distributed-architecture): Learn about the architecture of Elasticsearch and Kibana, and how Elastic stores and retrieves data and executes tasks in clusters with multiple nodes.
- [Production guidance](https://www.elastic.co/docs/deploy-manage/production-guidance): Review tips and guidance that you can use to design a production environment that matches your workloads, policies, and deployment needs.
- [Reference architectures](https://www.elastic.co/docs/deploy-manage/reference-architectures): Explore blueprints for deploying clusters tailored to different use cases.
- [Backup, high availability, and resilience tools](https://www.elastic.co/docs/deploy-manage/tools): Learn about the tools available to safeguard data, ensure continuous availability, and maintain resilience in your Elasticsearch environment.
- [Autoscaling](https://www.elastic.co/docs/deploy-manage/autoscaling): Learn how to configure your [orchestrated](/docs/deploy-manage/deploy#about-orchestration) deployment to scale based on policies and cluster signals. Applies to Elastic Cloud Hosted, Elastic Cloud Enterprise, and Elastic Cloud on Kubernetes deployments.
- [Cloud Connect](https://www.elastic.co/docs/deploy-manage/cloud-connect): Learn how to use Elastic Cloud services in your self-hosted environment.

<admonition title="Serverless does it for you">
  If you deploy an Elastic Cloud Serverless project, then you don't need to learn about Elastic architecture, production design, resilience, or scaling concepts. Serverless automatically scales and backs up your cluster for you, and is ready for production out of the box.
</admonition>


## Secure and control access

Learn how to secure your Elastic environment to restrict access to only authorized parties, and allow communication between your environment and external parties.
- [Security](https://www.elastic.co/docs/deploy-manage/security): Learn about security features that prevent bad actors from tampering with your data, and encrypt communications to, from, and within your cluster.
- [Users and roles](https://www.elastic.co/docs/deploy-manage/users-roles): Manage user authentication and authorization at the level of your Cloud organization, your orchestrator, or your deployment or cluster.
- [Spaces](https://www.elastic.co/docs/deploy-manage/manage-spaces): Learn how to organize content in Kibana, and restrict access to this content to specific users.
- [Elastic API keys](https://www.elastic.co/docs/deploy-manage/api-keys): Authenticate and authorize programmatic access to your deployments and Elasticsearch resources.
- [Connectors](https://www.elastic.co/docs/deploy-manage/manage-connectors): Manage connection information between Elastic and third-party systems.
- [Remote clusters](https://www.elastic.co/docs/deploy-manage/remote-clusters): Enable communication between Elasticsearch clusters to support [cross-cluster replication](https://www.elastic.co/docs/deploy-manage/tools/cross-cluster-replication) and [cross-cluster search](https://www.elastic.co/docs/explore-analyze/cross-cluster-search).


## Administer and maintain

Monitor the performance of your Elastic environment, administer your organization and license, and maintain the health of your environment.
- [Monitoring](https://www.elastic.co/docs/deploy-manage/monitor): View health and performance data for Elastic components, and receive recommendations and insights.
- [Manage your Cloud organization](https://www.elastic.co/docs/deploy-manage/cloud-organization): Administer your Elastic Cloud organization, including billing, organizational contacts, and service monitoring.
- [Licenses and subscriptions](https://www.elastic.co/docs/deploy-manage/license): Learn how to manage your Elastic license or subscription.
- [Maintenance](https://www.elastic.co/docs/deploy-manage/maintenance): Learn how to isolate or deactivate parts of your Elastic environment to perform maintenance, or restart parts of Elastic.
- [Uninstall](https://www.elastic.co/docs/deploy-manage/uninstall): Uninstall one or more Elastic components.


## Upgrade

You can [upgrade your Elastic environment](https://www.elastic.co/docs/deploy-manage/upgrade) to gain access to the latest features. Learn how to upgrade your cluster or deployment to the latest Elastic Stack version, or upgrade your Elastic Cloud Enterprise orchestrator or Elastic Cloud on Kubernetes operator to the latest version.