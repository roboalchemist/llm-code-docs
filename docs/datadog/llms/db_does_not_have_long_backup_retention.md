# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/nifcloud/db_does_not_have_long_backup_retention.md

---
title: Beta - Nifcloud RDB has backup retention less than 2 days
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - Nifcloud RDB has backup retention less
  than 2 days
---

# Beta - Nifcloud RDB has backup retention less than 2 days

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `e5071f76-cbe7-468d-bb2b-d10f02d2b713`

**Cloud Provider:** Nifcloud

**Platform:** Terraform

**Severity:** Medium

**Category:** Backup

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/nifcloud/nifcloud/latest/docs/resources/db_instance#backup_retention_period)

### Description{% #description %}

The RDB backup retention period is less than 2 days. The `nifcloud_db_instance` resource must include the `backup_retention_period` attribute set to at least 2 (days). Resources missing this attribute or with a value less than 2 will be reported as `MissingAttribute` or `IncorrectValue`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "nifcloud_db_instance" "negative" {
  identifier              = "example"
  instance_class          = "db.large8"
  backup_retention_period = 5
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "nifcloud_db_instance" "positive" {
  identifier              = "example"
  instance_class          = "db.large8"
  backup_retention_period = 1
}
```

```terraform
resource "nifcloud_db_instance" "positive" {
  identifier              = "example"
  instance_class          = "db.large8"
}
```
