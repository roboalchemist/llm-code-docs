# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/neptune_snapshots_not_encrypted.md

---
title: Neptune cluster snapshot not encrypted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Neptune cluster snapshot not encrypted
---

# Neptune cluster snapshot not encrypted

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `g3l20gd0k-e5f6-7890-ab12-cd34ef567890`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/neptune_cluster_snapshot#storage_encrypted)

### Description{% #description %}

AWS Neptune is a fully managed graph database service that stores and queries highly connected data. When Neptune cluster snapshots are not encrypted, sensitive data stored in these snapshots could be vulnerable to unauthorized access, potentially exposing proprietary information, personal data, or other confidential content. Enabling encryption for Neptune cluster snapshots adds an additional layer of security that helps protect your data at rest.

Secure configuration example:

```terraform
resource "aws_neptune_cluster_snapshot" "good_example" {
  db_cluster_identifier          = "example-cluster"
  db_cluster_snapshot_identifier = "example-snapshot"
  storage_encrypted              = true
}
```

Vulnerable configuration example:

```terraform
resource "aws_neptune_cluster_snapshot" "bad_example" {
  db_cluster_identifier          = "example-cluster"
  db_cluster_snapshot_identifier = "example-snapshot"
  storage_encrypted              = false
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_neptune_cluster_snapshot" "good_example" {
  db_cluster_identifier          = "example-cluster"
  db_cluster_snapshot_identifier = "example-snapshot"
  storage_encrypted              = true # â Neptune snapshot encryption is enabled
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_neptune_cluster_snapshot" "bad_example" {
  db_cluster_identifier          = "example-cluster"
  db_cluster_snapshot_identifier = "example-snapshot"
  storage_encrypted              = false # â Neptune snapshot encryption is disabled
}
```
