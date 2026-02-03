# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/general/output_without_description.md

---
title: Output without description
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Output without description
---

# Output without description

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `59312e8a-a64e-41e7-a252-618533dd1ea8`

**Cloud Provider:** Common

**Platform:** Terraform

**Severity:** Low

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://www.terraform.io/docs/language/values/outputs.html#description-output-value-documentation)

### Description{% #description %}

`output` entries must contain a valid `description`. The `description` must be defined, non-null, and not empty or whitespace-only.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
output "cluster_name" {
  value = "example"
  description = "cluster name"
}

resource "aws_eks_cluster" "negative1" {
  depends_on = [aws_cloudwatch_log_group.example]

  enabled_cluster_log_types = ["api", "audit", "authenticator", "controllerManager", "scheduler"]
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
output "cluster_name" {
  value = "example"
  description = " "
}

resource "aws_eks_cluster" "positive1" {
  depends_on = [aws_cloudwatch_log_group.example]
}
```

```terraform
output "cluster_name" {
  value = "example"
  description = ""
}

resource "aws_eks_cluster" "positive1" {
  depends_on = [aws_cloudwatch_log_group.example]
}
```

```terraform
output "cluster_name" {
  value = "example"
}

resource "aws_eks_cluster" "positive1" {
  depends_on = [aws_cloudwatch_log_group.example]
}
```
