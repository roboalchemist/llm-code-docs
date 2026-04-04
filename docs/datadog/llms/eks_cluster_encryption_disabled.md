# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/eks_cluster_encryption_disabled.md

---
title: EKS cluster encryption disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > EKS cluster encryption disabled
---

# EKS cluster encryption disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `63ebcb19-2739-4d3f-aa5c-e8bbb9b85281`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/eks_cluster#encryption_config)

### Description{% #description %}

Amazon EKS clusters store sensitive information including certificate authorities and service account tokens. When encryption is disabled, this sensitive data is stored in plaintext, potentially exposing it to unauthorized access and data breaches. Enabling encryption using KMS keys for EKS clusters adds an essential layer of security by encrypting Kubernetes secrets stored in etcd.

Insecure example without encryption:

```gdscript3
resource "aws_eks_cluster" "positive1" {
  depends_on = [aws_cloudwatch_log_group.example]
  name = var.cluster_name
  // Missing encryption_config block
}
```

Secure example with encryption enabled:

```gdscript3
resource "aws_eks_cluster" "negative1" {
  depends_on = [aws_cloudwatch_log_group.example]
  name = var.cluster_name

  encryption_config {
    resources = ["secrets"]
    provider {
      key_arn = "your-kms-key-arn"
    }
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
variable "cluster_name" {
  default = "example"
  type    = string
}

resource "aws_eks_cluster" "negative1" {
  depends_on = [aws_cloudwatch_log_group.example]
  name                      = var.cluster_name

  encryption_config {
    resources = ["secrets"]
    provider {
      key_arn = "test"
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
variable "cluster_name" {
  default = "example"
  type    = string
}

resource "aws_eks_cluster" "positive2" {
  depends_on = [aws_cloudwatch_log_group.example]
  name                      = var.cluster_name

  encryption_config {
    resources = ["s"]
    provider {
      key_arn = "test"
    }
  }
}
```

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
