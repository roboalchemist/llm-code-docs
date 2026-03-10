# Source: https://www.elastic.co/docs/deploy-manage/cloud-connect

﻿---
title: Cloud Connect
description: Cloud Connect enables you to use Elastic Cloud services in your ECE, ECK, or self-managed cluster without having to install and maintain their infrastructure...
url: https://www.elastic.co/docs/deploy-manage/cloud-connect
products:
  - Elastic Cloud Enterprise
  - Elastic Cloud on Kubernetes
  - Elasticsearch
applies_to:
  - Elastic Cloud on Kubernetes: Generally available
  - Elastic Cloud Enterprise: Generally available
  - Self-managed Elastic deployments: Generally available
---

# Cloud Connect
Cloud Connect enables you to use Elastic Cloud services in your [ECE](https://www.elastic.co/docs/deploy-manage/deploy/cloud-enterprise), [ECK](https://www.elastic.co/docs/deploy-manage/deploy/cloud-on-k8s), or [self-managed](https://www.elastic.co/docs/deploy-manage/deploy/self-managed) cluster without having to install and maintain their infrastructure yourself. In this way, you can get faster access to new features without adding to your operational overhead.
AutoOps is the first service available for use with Cloud Connect. More services are coming soon.

## AutoOps

[AutoOps](https://www.elastic.co/docs/deploy-manage/monitor/autoops) is a monitoring tool that helps you manage your cluster with real-time issue detection, performance recommendations, and resolution paths. By analyzing hundreds of Elasticsearch metrics, your configuration, and your usage patterns, AutoOps recommends operational and monitoring insights that deliver real savings in administration time and hardware cost.
AutoOps can be connected to clusters on Elasticsearch version 7.17 and later.
Learn how to set up and use [AutoOps for ECE, ECK, and self-managed clusters](https://www.elastic.co/docs/deploy-manage/monitor/autoops/cc-autoops-as-cloud-connected).
<admonition title="New! Expanded license support for AutoOps">
  AutoOps for ECE, ECK, and self-managed clusters is now available for free across all [self-managed license types](https://www.elastic.co/subscriptions).
</admonition>


## Elastic Inference Service (EIS)

[Elastic Inference Service](https://www.elastic.co/docs/explore-analyze/elastic-inference/eis) enables you to add AI-powered search and assistance to your Elasticsearch deployment without running models yourself.
You can use EIS to enable features such as:
- [Semantic search](https://www.elastic.co/docs/solutions/search/semantic-search)
- [AI Assistants](https://www.elastic.co/docs/explore-analyze/ai-features/ai-chat-experiences/ai-assistant)
- [Agent Builder](https://www.elastic.co/docs/explore-analyze/ai-features/elastic-agent-builder)
- [Attack Discovery](https://www.elastic.co/docs/solutions/security/ai/attack-discovery)

For a full list of EIS-powered features, refer to [AI features powered by EIS](/docs/explore-analyze/elastic-inference/eis#ai-features-powered-by-eis).
EIS can be connected to clusters on Elasticsearch version 9.3 and later.
Learn how to set up and use [Elastic Inference Service for self-managed clusters](https://www.elastic.co/docs/explore-analyze/elastic-inference/connect-self-managed-cluster-to-eis).

## FAQ

Find answers to your questions about Cloud Connect.
- [Does Cloud Connect require additional payment?](#cc-additional-payment)
- [Can I use Cloud Connect to connect my Elastic Cloud Hosted clusters to AutoOps?](#cc-ech)
- [Can I use Cloud Connect to connect my Elastic Cloud Hosted clusters to EIS?](#cc-ech-eis)
- [Are more services going to be available with Cloud Connect?](#cc-more-services)

<definitions>
  <definition term="Does Cloud Connect require additional payment?">
    Each cloud connected service has its own licensing and payment requirements.
    - AutoOps for ECE, ECK, and self-managed clusters is available for free across all [self-managed license types](https://www.elastic.co/subscriptions). It does not consume ECUs.
    - The Elastic Inference Service (EIS) for ECE, ECK, and self-managed clusters requires a [self-managed Enterprise license](https://www.elastic.co/subscriptions) or a self-managed free trial. Note that [EIS pricing](/docs/explore-analyze/elastic-inference/eis#pricing) is usage-based. Using EIS consumes ECUs.
  </definition>
  <definition term="Can I use Cloud Connect to connect my Elastic Cloud Hosted clusters to AutoOps?">
    This path is not supported. Currently, we only support using Cloud Connect to connect ECE, ECK, and self-managed clusters to AutoOps.
    For Elastic Cloud Hosted deployments, AutoOps is set up and enabled automatically in all supported [regions](https://www.elastic.co/docs/deploy-manage/monitor/autoops/ec-autoops-regions), and can be [accessed](https://www.elastic.co/docs/deploy-manage/monitor/autoops/ec-autoops-how-to-access) from the deployment overview page.
  </definition>
  <definition term="Can I use Cloud Connect to connect my Elastic Cloud Hosted clusters to EIS?">
    For Elastic Cloud Hosted deployments with an Enterprise license, EIS is set up and enabled automatically.
  </definition>
  <definition term="Are more services going to be available with Cloud Connect?">
    Yes. Cloud Connect will support additional services over time. After AutoOps and the Elastic Inference Service (EIS), the next planned cloud connected service is Synthetics.
  </definition>
</definitions>