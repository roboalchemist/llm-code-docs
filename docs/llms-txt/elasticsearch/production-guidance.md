# Source: https://www.elastic.co/docs/deploy-manage/production-guidance

﻿---
title: Production guidance
description: Running the Elastic Stack in production requires careful planning to ensure resilience, performance, and scalability. This section outlines best practices...
url: https://www.elastic.co/docs/deploy-manage/production-guidance
products:
  - Elastic Cloud Hosted
applies_to:
  - Elastic Cloud Hosted: Generally available
  - Elastic Cloud on Kubernetes: Generally available
  - Elastic Cloud Enterprise: Generally available
  - Self-managed Elastic deployments: Generally available
---

# Production guidance
Running the Elastic Stack in production requires careful planning to ensure resilience, performance, and scalability. This section outlines best practices and recommendations for optimizing Elasticsearch and Kibana in production environments.
You’ll learn how to design highly available and resilient deployments, implement best practices for managing workloads, and apply performance optimizations to handle scaling demands efficiently.
For Elasticsearch, this includes strategies for fault tolerance, data replication, and workload distribution to maintain stability under load. For Kibana, you’ll explore how to deploy multiple Kibana instances within the same environment and make informed decisions about scaling horizontally or vertically based on the task manager metrics, which provide insights into background task execution and resource consumption.
By following this guidance, you can ensure your Elastic Stack deployment is robust, efficient, and prepared for production-scale workloads.
For detailed, component-specific guidance, refer to:
- [Run Elasticsearch in production](https://www.elastic.co/docs/deploy-manage/production-guidance/elasticsearch-in-production-environments)
- [Run Kibana in production](https://www.elastic.co/docs/deploy-manage/production-guidance/kibana-in-production-environments)


## Deployment types

Production guidelines and concepts described in this section apply to all [deployment types](/docs/deploy-manage/deploy#choosing-your-deployment-type)—including Elastic Cloud Hosted, Elastic Cloud Enterprise, Elastic Cloud on Kubernetes, and self-managed clusters—**except** Elastic Cloud Serverless.
However, certain parts may be relevant only to self-managed clusters, as orchestration systems automate some of the configurations discussed here. Check the [badges](/docs/get-started/versioning-availability#availability-of-features) on each document or section to confirm whether the content applies to your deployment type.
<note>
  **Elastic Cloud Serverless** projects are fully managed and automatically scaled by Elastic. Your project’s performance and general data retention are controlled by the [Search AI Lake settings](/docs/deploy-manage/deploy/elastic-cloud/project-settings#elasticsearch-manage-project-search-ai-lake-settings).
</note>


## Other Elastic products

If you are looking for production guidance for Elastic products other than Elasticsearch or Kibana, check out the following resources:
- [High availability on ECE orchestrator](https://www.elastic.co/docs/deploy-manage/deploy/cloud-enterprise/ece-ha)
- [APM scalability and performance](https://www.elastic.co/docs/troubleshoot/observability/apm/processing-performance)
- [Fleet server scalability](https://www.elastic.co/docs/reference/fleet/fleet-server-scalability)
- [Deploying and scaling Logstash](https://www.elastic.co/docs/reference/logstash/deploying-scaling-logstash)