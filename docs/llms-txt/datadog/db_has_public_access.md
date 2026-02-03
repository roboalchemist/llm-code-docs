# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/nifcloud/db_has_public_access.md

---
title: Beta - Nifcloud RDB has public DB access
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - Nifcloud RDB has public DB access
---

# Beta - Nifcloud RDB has public DB access

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `fb387023-e4bb-42a8-9a70-6708aa7ff21b`

**Cloud Provider:** Nifcloud

**Platform:** Terraform

**Severity:** High

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/nifcloud/nifcloud/latest/docs/resources/db_instance#publicly_accessible)

### Description{% #description %}

The RDB instance is configured to allow public network access. This rule detects `nifcloud_db_instance` resources where `publicly_accessible` is set to `true` and reports an `IncorrectValue` issue; network access should be limited to the minimum required for the application to function. Report attributes: `documentId`, `resourceType`, `resourceName`, `searchKey`, `issueType`, `keyExpectedValue`, `keyActualValue`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "nifcloud_db_instance" "negative" {
  identifier          = "example"
  instance_class      = "db.large8"
  publicly_accessible = false
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "nifcloud_db_instance" "positive" {
  identifier          = "example"
  instance_class      = "db.large8"
  publicly_accessible = true
}
```
