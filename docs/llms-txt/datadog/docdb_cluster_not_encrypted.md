# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/docdb_cluster_not_encrypted.md

---
title: DocumentDB cluster not encrypted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > DocumentDB cluster not encrypted
---

# DocumentDB cluster not encrypted

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `bc1f9009-84a0-490f-ae09-3e0ea6d74ad6`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/docdb_cluster#storage_encrypted)

### Description{% #description %}

This check verifies whether Amazon DocumentDB cluster storage encryption is enabled. DocumentDB clusters store sensitive data and should have storage encryption enabled to protect data at rest. When storage encryption is disabled or not configured, data stored in the cluster is vulnerable to unauthorized access if the underlying storage is compromised.

To properly secure a DocumentDB cluster, ensure the `storage_encrypted` attribute is explicitly set to `true`, as shown in the example below:

```terraform
resource "aws_docdb_cluster" "docdb" {
  cluster_identifier = "my-docdb-cluster"
  // ... other configuration ...
  storage_encrypted = true
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

resource "aws_docdb_cluster" "docdb_2" {
  cluster_identifier      = "my-docdb-cluster"
  engine                  = "docdb"
  master_username         = "foo"
  master_password         = "mustbeeightchars"
  backup_retention_period = 5
  preferred_backup_window = "07:00-09:00"
  skip_final_snapshot     = true
  storage_encrypted = false
}
```
