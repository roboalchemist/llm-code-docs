# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/db_snapshot_public.md

---
title: DB snapshot is public
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > DB snapshot is public
---

# DB snapshot is public

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `f0d8781f-1991-4958-9917-d39283b168a0`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/db_snapshot#shared_accounts-1)

### Description{% #description %}

AWS DB Snapshots contain a complete copy of your database, including all its data structures, stored procedures, and sensitive information. When a DB snapshot is made public by setting `shared_accounts` to include `all`, anyone with an AWS account can access and restore your database, potentially exposing confidential data or intellectual property. To mitigate this risk, always keep your DB snapshots private by ensuring the `shared_accounts` attribute is either not specified or set to an empty array. Compare the secure configuration (`shared_accounts = []`) with the vulnerable configuration (`shared_accounts = ["all"]`). Implementing proper access controls for DB snapshots is essential for protecting sensitive data and maintaining compliance with data protection regulations.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_db_snapshot" "private_snapshot" {
  db_snapshot_identifier = "private-db-snapshot"
  db_instance_identifier = "my-db-instance"
}
```

```terraform
resource "aws_db_snapshot" "private_snapshot" {
  db_snapshot_identifier = "private-db-snapshot"
  db_instance_identifier = "my-db-instance"
  shared_accounts        = []
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_db_snapshot" "public_snapshot" {
  db_snapshot_identifier = "public-db-snapshot"
  db_instance_identifier = "my-db-instance"
  shared_accounts        = ["all"]
}
```
