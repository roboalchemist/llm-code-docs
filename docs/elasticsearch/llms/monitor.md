# Source: https://www.elastic.co/docs/deploy-manage/monitor

﻿---
title: Monitoring
description: Keeping on top of the health of your cluster or deployment, as well as your orchestrator, is an important part of maintenance. It also helps you to identify...
url: https://www.elastic.co/docs/deploy-manage/monitor
products:
  - Elastic Cloud Hosted
  - Elasticsearch
applies_to:
  - Elastic Cloud Serverless: Generally available
  - Elastic Stack: Generally available
---

# Monitoring
Keeping on top of the health of your cluster or deployment, as well as your orchestrator, is an important part of maintenance. It also helps you to identify and troubleshoot issues. When you move to [production](https://www.elastic.co/docs/deploy-manage/production-guidance), detecting and resolving issues when they arise is a key component of keeping your deployment highly available.
Depending on your deployment type, you can use a variety of solutions for monitoring your Elastic components.

## Monitoring your cluster or deployment

You have several options for monitoring your cluster or deployment.
Use [AutoOps](https://www.elastic.co/docs/deploy-manage/monitor/autoops) to simplify cluster management through performance recommendations, resource utilization visibility, and real-time issue detection with resolution paths.
Alternatively, you can use [Stack Monitoring](https://www.elastic.co/docs/deploy-manage/monitor/stack-monitoring) to monitor logs and metrics across the Elastic Stack.
To help you decide between these two options, refer to [AutoOps and Stack Monitoring comparison](https://www.elastic.co/docs/deploy-manage/monitor/autoops-vs-stack-monitoring).
For ECE and Elastic Cloud Hosted deployments, there are also a number of out of the box monitoring tools available.
The following sections provide more details.

### AutoOps (recommended)

<applies-to>
  - Elastic Cloud Serverless: Generally available
  - Elastic Stack: Generally available
</applies-to>

AutoOps diagnoses issues in Elasticsearch by analyzing hundreds of metrics, providing root-cause analysis and accurate resolution paths. With AutoOps, customers can prevent and resolve issues, cut down administration time, and optimize resource utilization.
AutoOps is automatically available in [Elastic Cloud Hosted deployments](https://www.elastic.co/docs/deploy-manage/monitor/autoops/ec-autoops-how-to-access) and [Elastic Cloud Serverless projects](https://www.elastic.co/docs/deploy-manage/monitor/autoops/autoops-for-serverless), and can be set up for [ECE, ECK, and self-managed clusters](https://www.elastic.co/docs/deploy-manage/monitor/autoops/cc-autoops-as-cloud-connected) through Cloud Connect.
<admonition title="New! Expanded license support for AutoOps">
  AutoOps for ECE, ECK, and self-managed clusters is now available for free across all [self-managed license types](https://www.elastic.co/subscriptions).
</admonition>


### Stack monitoring

<applies-to>
  - Elastic Stack: Generally available
</applies-to>

Stack monitoring allows you to collect logs and metrics from various Elastic products, including Elasticsearch nodes, Logstash nodes, Kibana instances, APM Server, and Beats in your cluster. You can also collect logs.
All of the monitoring metrics are stored in Elasticsearch, which enables you to easily visualize the data in Kibana.
In Elastic Cloud Enterprise and Elastic Cloud Hosted, Elastic manages the installation and configuration of the monitoring agent for you, simplifying the stack monitoring setup process.
<tip>
  By default, the monitoring metrics are stored in local indices. In production, we strongly recommend using a [separate monitoring cluster](/docs/deploy-manage/monitor/stack-monitoring#production-architecture). Using a separate monitoring cluster prevents production cluster outages from impacting your ability to access your monitoring data. It also prevents monitoring activities from impacting the performance of your production cluster. For the same reason, we also recommend using a separate Kibana instance for viewing the monitoring data.
</tip>


### Cluster health and performance metrics

<applies-to>
  - Elastic Cloud Hosted: Generally available
  - Elastic Cloud Enterprise: Generally available
</applies-to>

Elastic Cloud Enterprise and Elastic Cloud Hosted provide out of the box tools for monitoring the health of your deployment and resolving health issues when they arise:
- [Cluster health information](/docs/deploy-manage/monitor/cloud-health-perf#ec-es-cluster-health), including [health warnings](/docs/deploy-manage/monitor/cloud-health-perf#ec-es-health-warnings)
- A [JVM memory pressure indicator](https://www.elastic.co/docs/deploy-manage/monitor/ec-memory-pressure)

Elastic Cloud Hosted only:
- [Cluster performance information](https://www.elastic.co/docs/deploy-manage/monitor/access-performance-metrics-on-elastic-cloud)
- [Preconfigured logs and metrics](/docs/deploy-manage/monitor/cloud-health-perf#ec-es-health-preconfigured)

Elastic Cloud Enterprise only:
- [Platform monitoring](https://www.elastic.co/docs/deploy-manage/monitor/orchestrators/ece-platform-monitoring), including logs, metrics, and proxy logs

<tip>
  Out of the box logs and metrics tools, including ECH preconfigured logs and metrics and ECE platform monitoring logs and metrics, are useful for providing information in a non-production environment. In a production environment, it’s important set up either AutoOps or stack monitoring to retain the logs and metrics that can be used to troubleshoot any health issues in your deployments. In the event of that you need to [contact our support team](/docs/troubleshoot#contact-us), they can use the retained data to help diagnose any problems that you may encounter.
</tip>

To learn more about the health and performance tools in Elastic Cloud, refer to [Cloud deployment health and performance metrics](https://www.elastic.co/docs/deploy-manage/monitor/cloud-health-perf).

## Kibana task manager monitoring

<applies-to>
  - Elastic Stack: Preview
</applies-to>

The Kibana [task manager](https://www.elastic.co/docs/deploy-manage/distributed-architecture/kibana-tasks-management) has an internal monitoring mechanism to keep track of a variety of metrics, which can be consumed with either the health monitoring API or the Kibana server log. [Learn how to configure thresholds and consume related to Kibana task manager](https://www.elastic.co/docs/deploy-manage/monitor/kibana-task-manager-health-monitoring).

## Monitoring your orchestrator

<applies-to>
  - Elastic Cloud on Kubernetes: Generally available
  - Elastic Cloud Enterprise: Generally available
</applies-to>

In addition to monitoring your cluster or deployment health and performance, you need to monitor your orchestrator. Monitoring is especially important for orchestrators hosted on infrastructure that you control.
Learn how to enable monitoring of your orchestrator:
- [ECK operator metrics](https://www.elastic.co/docs/deploy-manage/monitor/orchestrators/eck-metrics-configuration): Open and secure a metrics endpoint that can be used to monitor the operator’s performance and health. This endpoint can be scraped by third-party Kubernetes monitoring tools.
- [ECE platform monitoring](https://www.elastic.co/docs/deploy-manage/monitor/orchestrators/ece-platform-monitoring): Learn about how ECE collects monitoring data for your installation in the `logging-and-metrics` deployment, and how to access monitoring data.

<admonition title="Monitoring Elastic Cloud">
  Elastic monitors [Elastic Cloud](https://www.elastic.co/docs/deploy-manage/deploy/elastic-cloud) service metrics and performance as part of [our shared responsibility](https://www.elastic.co/cloud/shared-responsibility). We provide service availability information on our [service status page](https://www.elastic.co/docs/deploy-manage/cloud-organization/service-status).
</admonition>


## Logging

You can configure several types of logs in Elastic Stack that can help you to gain insight into Elastic Stack operations, diagnose issues, and track certain types of events. [Learn about the types of logs available, where to find them, and how to configure them](https://www.elastic.co/docs/deploy-manage/monitor/logging-configuration).