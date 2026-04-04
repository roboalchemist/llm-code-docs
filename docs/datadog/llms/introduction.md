# Source: https://docs.datadoghq.com/cloudprem/introduction.md

---
title: Introduction to CloudPrem
description: Learn about CloudPrem architecture, components, and supported features
breadcrumbs: Docs > CloudPrem > Introduction to CloudPrem
---

# Introduction to CloudPrem

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### CloudPrem is in Preview

Join the CloudPrem Preview to access new self-hosted log management features.

[Request Access](https://www.datadoghq.com/product-preview/cloudprem/)
{% /callout %}

## Overview{% #overview %}

CloudPrem is Datadog BYOC log management solution. It runs in your own infrastructure, indexes and stores logs in your object storage, execute search and analytics queries and connects to Datadog UI to give a fully integrated experience with Datadog products. CloudPrem is designed for organizations with specific requirements:

- Data residency, privacy, and regulatory requirements
- High volume requirements

Here is a high-level overview of how CloudPrem works:

{% image
   source="https://datadog-docs.imgix.net/images/cloudprem/overview_diagram_cloudprem.d0b179faac15e3d8e1a64ccfd3da100a.png?auto=format"
   alt="CloudPrem architecture overview showing how logs flow from sources through CloudPrem to the Datadog platform" /%}

The diagram illustrates the CloudPrem hybrid architecture, highlighting how data is processed and stored within your infrastructure:

- **Ingestion**: Logs are collected from Datadog Agents and other sources using standard protocols.
- **Your Infrastructure**: The CloudPrem platform runs entirely inside your infrastructure. It processes and stores logs in your own storage (S3, Azure Blob, MinIO).
- **Datadog SaaS**: The Datadog platform is CloudPrem's Control Plane, it hosts the Datadog UI and communicates with CloudPrem via a secure connection to send log queries and receive results.

- [Architecture - Understand how CloudPrem components work together](https://docs.datadoghq.com/cloudprem/introduction/architecture/)
- [Network - Understand how CloudPrem communicates with Datadog](https://docs.datadoghq.com/cloudprem/introduction/network/)
- [Supported Features - See which Log Explorer features are available in CloudPrem](https://docs.datadoghq.com/cloudprem/introduction/features/)

## Get started{% #get-started %}

- [Quickstart - Run CloudPrem locally in 5 minutes](https://docs.datadoghq.com/cloudprem/quickstart/)
- [Installation - Deploy CloudPrem on AWS, Azure, or custom Kubernetes](https://docs.datadoghq.com/cloudprem/install/)
- [Ingest Logs - Configure the Datadog Agent to send logs to CloudPrem](https://docs.datadoghq.com/cloudprem/ingest/agent/)
