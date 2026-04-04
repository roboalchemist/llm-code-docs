# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/nifcloud/db_security_group_description_undefined.md

---
title: Beta - Nifcloud RDB undefined description to DB security group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - Nifcloud RDB undefined description to
  DB security group
---

# Beta - Nifcloud RDB undefined description to DB security group

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `940ddce2-26bd-4e31-a9b4-382714f73231`

**Cloud Provider:** Nifcloud

**Platform:** Terraform

**Severity:** Low

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/nifcloud/nifcloud/latest/docs/resources/db_security_group#description)

### Description{% #description %}

Missing description for DB security group.

Resources of type `nifcloud_db_security_group` should include a `description` attribute for auditing and identification. This rule flags `nifcloud_db_security_group` resources that do not define a `description`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "nifcloud_db_security_group" "negative" {
  group_name        = "example"
  availability_zone = "east-11"
  description       = "Allow from app traffic"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "nifcloud_db_security_group" "positive" {
  group_name        = "example"
  availability_zone = "east-11"
}
```
