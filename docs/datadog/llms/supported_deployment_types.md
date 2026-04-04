# Source: https://docs.datadoghq.com/security/cloud_security_management/setup/supported_deployment_types.md

---
title: Cloud Security Supported Deployment Types
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud Security > Setting up Cloud Security > Cloud
  Security Supported Deployment Types
---

# Cloud Security Supported Deployment Types

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% alert level="info" %}
Collecting events using Cloud Security Management will affect your billing. For more information, see [Datadog Pricing](https://www.datadoghq.com/pricing/?product=cloud-security-management#products).
{% /alert %}

The following table summarizes the Cloud Security features available relative to each deployment type.

| Deployment type     | Agent Required (7.46+) | Misconfigurations            | Vulnerabilities | Identity Risks | Agentless Scanning |
| ------------------- | ---------------------- | ---------------------------- | --------------- | -------------- | ------------------ |
| AWS Account         | yes                    | yes                          | yes             | yes            |
| Azure Account       | yes                    | Agentless Scanning (Preview) | yes             |
| GCP Account         | yes                    |
| Terraform           | yes                    |
| Docker              | yes                    | yes                          |
| Kubernetes          | yes                    | yes                          | yes             |
| Linux               | yes                    | yes                          | yes             |
| Amazon ECS/EKS      | yes                    | yes                          | yes             |
| Windows             | yes                    | yes                          |
| AWS Fargate ECS/EKS | yes                    |

The following table summarizes the scope of coverage available relative to each Cloud Security feature.

| Resources monitored             | Misconfigurations | Vulnerabilities | Identity Risks | Agentless scanning |
| ------------------------------- | ----------------- | --------------- | -------------- | ------------------ |
| Resources in AWS Account        | yes               | yes             | yes            |
| Resources in Azure Subscription | yes               |
| Resources in GCP Project        | yes               |
| Kubernetes Cluster              | yes               |
| Docker Host                     | yes               |
| Linux Host                      | yes               | yes             | yes            |
| Windows Host                    | yes               |
| Docker Container                |
| Container Image                 | yes               | yes             |
| IAM in AWS Account              | yes               |

**Note**: Cloud Security Misconfigurations additionally monitors common resources used in your cloud accounts that are running Windows and AWS Fargate, such as EC2 instances, RDS, S3, and ELB.
