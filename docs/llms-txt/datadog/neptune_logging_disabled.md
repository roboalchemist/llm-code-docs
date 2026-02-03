# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/neptune_logging_disabled.md

---
title: Neptune logging is disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Neptune logging is disabled
---

# Neptune logging is disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `45cff7b6-3b80-40c1-ba7b-2cf480678bb8`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/neptune_cluster#enable_cloudwatch_logs_exports)

### Description{% #description %}

Enabling Neptune logging ensures that audit and error logs are exported to Amazon CloudWatch, which is critical for monitoring, troubleshooting, and security auditing of Neptune database activity. If the `enable_cloudwatch_logs_exports` attribute is not set with values such as `["audit"]` or `["audit", "error"]`, as shown below, no logs will be exported by default, leaving potentially malicious or unauthorized database actions undetected:

```gdscript3
resource "aws_neptune_cluster" "example" {
  ...
  enable_cloudwatch_logs_exports = ["audit", "error"]
}
```

Without these logs, it becomes challenging to investigate incidents, meet compliance requirements, or identify operational issues, increasing the risk of undetected attacks or data breaches.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_neptune_cluster" "negative1" {
  cluster_identifier                  = "neptune-cluster"
  engine                              = "neptune"
  backup_retention_period             = 5
  preferred_backup_window             = "10:10-11:11"
  skip_final_snapshot                 = true
  iam_database_authentication_enabled = true
  apply_immediately                   = true
  enable_cloudwatch_logs_exports      = ["audit"]
}

resource "aws_neptune_cluster" "negative2" {
  cluster_identifier                  = "neptune-cluster"
  engine                              = "neptune"
  backup_retention_period             = 5
  preferred_backup_window             = "10:10-11:11"
  skip_final_snapshot                 = true
  iam_database_authentication_enabled = true
  apply_immediately                   = true
  enable_cloudwatch_logs_exports      = ["audit", "error"]
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_neptune_cluster" "postive2" {
  cluster_identifier                  = "neptune-cluster"
  engine                              = "neptune"
  backup_retention_period             = 5
  preferred_backup_window             = "10:10-11:11"
  skip_final_snapshot                 = true
  iam_database_authentication_enabled = true
  apply_immediately                   = true
  enable_cloudwatch_logs_exports      = []
}
```

```terraform
resource "aws_neptune_cluster" "postive3" {
  cluster_identifier                  = "neptune-cluster"
  engine                              = "neptune"
  backup_retention_period             = 5
  preferred_backup_window             = "10:10-11:11"
  skip_final_snapshot                 = true
  iam_database_authentication_enabled = true
  apply_immediately                   = true
  enable_cloudwatch_logs_exports      = ["error"]
}
```

```terraform
resource "aws_neptune_cluster" "postive1" {
  cluster_identifier                  = "neptune-cluster"
  engine                              = "neptune"
  backup_retention_period             = 5
  preferred_backup_window             = "10:10-11:11"
  skip_final_snapshot                 = true
  iam_database_authentication_enabled = true
  apply_immediately                   = true
}
```
