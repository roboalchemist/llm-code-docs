# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/rds_cluster_with_backup_disabled.md

---
title: RDS cluster with backup disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > RDS cluster with backup disabled
---

# RDS cluster with backup disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `e542bd46-58c4-4e0f-a52a-1fb4f9548e02`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Backup

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/rds_cluster#backup_retention_period)

### Description{% #description %}

RDS cluster backup retention period should be explicitly defined. When creating an AWS RDS cluster using Terraform, omitting the `backup_retention_period` parameter allows the database to default to the minimum backup retention, which could be zero or just one day depending on the engine. This short or undefined retention window risks losing the ability to restore data to a specific point in time, potentially resulting in irreversible data loss in the event of accidental deletion, corruption, or ransomware attacks. Explicitly setting a sufficient retention period ensures backups are available for recovery as required by business continuity or compliance requirements.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_rds_cluster" "postgresql" {
  cluster_identifier      = "aurora-cluster-demo"
  engine                  = "aurora-postgresql"
  availability_zones      = ["us-west-2a", "us-west-2b", "us-west-2c"]
  database_name           = "mydb"
  master_username         = "foo"
  master_password         = "bar"
  backup_retention_period = 5
  preferred_backup_window = "07:00-09:00"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_rds_cluster" "postgresql" {
  cluster_identifier      = "aurora-cluster-demo"
  engine                  = "aurora-postgresql"
  availability_zones      = ["us-west-2a", "us-west-2b", "us-west-2c"]
  database_name           = "mydb"
  master_username         = "foo"
  master_password         = "bar"
  preferred_backup_window = "07:00-09:00"
}
```
