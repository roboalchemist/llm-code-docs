# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/docdb_cluster_without_kms.md

---
title: DocumentDB cluster without KMS
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > DocumentDB cluster without KMS
---

# DocumentDB cluster without KMS

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `4766d3ea-241c-4ee6-93ff-c380c996bd1a`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/docdb_cluster#kms_key_id)

### Description{% #description %}

AWS DocumentDB clusters should be encrypted with a KMS encryption key to protect sensitive data at rest. Without proper encryption, your database contents could be exposed if unauthorized access to the storage occurs, potentially leading to data breaches and compliance violations. To secure your DocumentDB cluster, you must enable storage encryption and specify a KMS key ID, as shown in the following secure example:

```terraform
resource "aws_docdb_cluster" "docdb" {
  cluster_identifier = "my-docdb-cluster"
  storage_encrypted = true
  kms_key_id = "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
  // other configuration...
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_docdb_cluster" "docdb" {
  cluster_identifier      = "my-docdb-cluster"
  engine                  = "docdb"
  master_username         = "foo"
  master_password         = "mustbeeightchars"
  backup_retention_period = 5
  preferred_backup_window = "07:00-09:00"
  skip_final_snapshot     = true
  storage_encrypted = true
  kms_key_id = "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_docdb_cluster" "docdb" {
  cluster_identifier      = "my-docdb-cluster"
  engine                  = "docdb"
  master_username         = "foo"
  master_password         = "mustbeeightchars"
  backup_retention_period = 5
  preferred_backup_window = "07:00-09:00"
  skip_final_snapshot     = true
}
```
