# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/aurora_with_disabled_at_rest_encryption.md

---
title: Aurora with disabled at rest encryption
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Aurora with disabled at rest encryption
---

# Aurora with disabled at rest encryption

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `1a690d1d-0ae7-49fa-b2db-b75ae0dd1d3e`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/rds_cluster#storage_encrypted)

### Description{% #description %}

Amazon Aurora clusters should have encryption at rest enabled to protect sensitive data stored in the database. When `storage_encrypted` is set to `false` or omitted, data stored in the underlying storage is vulnerable to unauthorized access if the storage media is compromised or improperly disposed of. Enabling encryption at rest helps maintain data confidentiality and supports compliance with regulatory requirements for data protection. To address this vulnerability, set the `storage_encrypted` attribute to true in your `aws_rds_cluster` resource, as shown in the secure example:

```terraform
resource "aws_rds_cluster" "my_cluster" {
  // other configuration
  storage_encrypted = true
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
provider "aws" {
  region = "us-west-2"  # Replace with your desired AWS region
}

resource "aws_rds_cluster" "my_cluster" {
  cluster_identifier            = "my-cluster"
  engine                       = "aurora-mysql"
  engine_version               = "5.7.mysql_aurora.2.08.0"
  master_username              = "admin"
  master_password              = "password"
  backup_retention_period      = 7
  preferred_backup_window      = "02:00-03:00"
  deletion_protection          = false
  skip_final_snapshot          = true
  apply_immediately            = true
  storage_encrypted            = true
}

resource "aws_rds_cluster_instance" "my_cluster_instance" {
  identifier                    = "my-cluster-instance"
  cluster_identifier            = aws_rds_cluster.my_cluster.id
  engine                        = "aurora-mysql"
  instance_class                = "db.r5.large"
  publicly_accessible           = false
  availability_zone             = "us-west-2a"  # Replace with your desired availability zone
}

output "cluster_endpoint" {
  value = aws_rds_cluster.my_cluster.endpoint
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
provider "aws" {
  region = "us-west-2"  # Replace with your desired AWS region
}

resource "aws_rds_cluster" "my_cluster" {
  cluster_identifier            = "my-cluster"
  engine                       = "aurora-mysql"
  engine_version               = "5.7.mysql_aurora.2.08.0"
  master_username              = "admin"
  master_password              = "password"
  backup_retention_period      = 7
  preferred_backup_window      = "02:00-03:00"
  deletion_protection          = false
  skip_final_snapshot          = true
  apply_immediately            = true
}

resource "aws_rds_cluster_instance" "my_cluster_instance" {
  identifier                    = "my-cluster-instance"
  cluster_identifier            = aws_rds_cluster.my_cluster.id
  engine                        = "aurora-mysql"
  instance_class                = "db.r5.large"
  publicly_accessible           = false
  availability_zone             = "us-west-2a"  # Replace with your desired availability zone
}

output "cluster_endpoint" {
  value = aws_rds_cluster.my_cluster.endpoint
}
```

```terraform
provider "aws" {
  region = "us-west-2"  # Replace with your desired AWS region
}

resource "aws_rds_cluster" "my_cluster" {
  cluster_identifier            = "my-cluster"
  engine                       = "aurora-mysql"
  engine_version               = "5.7.mysql_aurora.2.08.0"
  master_username              = "admin"
  master_password              = "password"
  backup_retention_period      = 7
  preferred_backup_window      = "02:00-03:00"
  deletion_protection          = false
  skip_final_snapshot          = true
  apply_immediately            = true
  storage_encrypted            = false
}

resource "aws_rds_cluster_instance" "my_cluster_instance" {
  identifier                    = "my-cluster-instance"
  cluster_identifier            = aws_rds_cluster.my_cluster.id
  engine                        = "aurora-mysql"
  instance_class                = "db.r5.large"
  publicly_accessible           = false
  availability_zone             = "us-west-2a"  # Replace with your desired availability zone
}

output "cluster_endpoint" {
  value = aws_rds_cluster.my_cluster.endpoint
}
```
