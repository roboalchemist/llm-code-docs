# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/eks_cluster_log_disabled.md

---
title: EKS cluster logging is not enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > EKS cluster logging is not enabled
---

# EKS cluster logging is not enabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `37304d3f-f852-40b8-ae3f-725e87a7cedf`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/eks_cluster#enabled_cluster_log_types)

### Description{% #description %}

Amazon EKS control plane logging should be enabled to capture important events and API calls within the Kubernetes control plane. Without explicit configuration of the `enabled_cluster_log_types` attribute, as shown below, critical logs like API, audit, and authenticator events will not be sent to CloudWatch, making it difficult to monitor cluster activity or investigate potential security incidents.

```
enabled_cluster_log_types = ["api", "audit", "authenticator", "controllerManager", "scheduler"]
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
variable "cluster_name" {
  default = "example"
  type    = string
}

resource "aws_eks_cluster" "negative1" {
  depends_on = [aws_cloudwatch_log_group.example]

  enabled_cluster_log_types = ["api", "audit", "authenticator", "controllerManager", "scheduler"]
  name                      = var.cluster_name
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
variable "cluster_name" {
  default = "example"
  type    = string
}

resource "aws_eks_cluster" "positive1" {
  depends_on = [aws_cloudwatch_log_group.example]
  name                      = var.cluster_name
}
```
