# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/general/variable_without_type.md

---
title: Variable without type
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Variable without type
---

# Variable without type

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `fc5109bf-01fd-49fb-8bde-4492b543c34a`

**Cloud Provider:** Common

**Platform:** Terraform

**Severity:** Low

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://www.terraform.io/docs/language/values/variables.html#input-variable-documentation)

### Description{% #description %}

All variables must include a valid `type` attribute. The `type` must be defined, not null, and not an empty string after trimming whitespace.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
variable "cluster_name" {
  default = "example"
  description = "cluster name"
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
  type    = " "
  description = "test"
}

resource "aws_eks_cluster" "positive1" {
  depends_on = [aws_cloudwatch_log_group.example]
  name                      = var.cluster_name
}
```

```terraform
variable "cluster_name" {
  default = "example"
  type    = ""
  description = "test"
}

resource "aws_eks_cluster" "positive1" {
  depends_on = [aws_cloudwatch_log_group.example]
  name                      = var.cluster_name
}
```

```terraform
variable "cluster_name" {
  default = "example"
  description = "test"
}

resource "aws_eks_cluster" "positive1" {
  depends_on = [aws_cloudwatch_log_group.example]
  name                      = var.cluster_name
}
```
