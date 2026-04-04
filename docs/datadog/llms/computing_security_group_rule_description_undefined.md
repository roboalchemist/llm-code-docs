# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/nifcloud/computing_security_group_rule_description_undefined.md

---
title: Beta - Nifcloud computing undefined description to security group rule
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - Nifcloud computing undefined
  description to security group rule
---

# Beta - Nifcloud computing undefined description to security group rule

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `e4610872-0b1c-4fb7-ab57-d81c0afdb291`

**Cloud Provider:** Nifcloud

**Platform:** Terraform

**Severity:** Low

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/nifcloud/nifcloud/latest/docs/resources/security_group_rule#description)

### Description{% #description %}

The `nifcloud_security_group_rule` resource must include a `description` attribute for auditing and traceability. This rule identifies `nifcloud_security_group_rule` instances that do not include a `description` and reports them as `MissingAttribute`. The rule returns `documentId`, `resourceType`, `resourceName`, `searchKey`, `issueType`, `keyExpectedValue`, and `keyActualValue` in the result.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "nifcloud_security_group_rule" "negative" {
  security_group_names = ["http"]
  type                 = "IN"
  description          = "HTTP from VPC"
  from_port            = 80
  to_port              = 80
  protocol             = "TCP"
  cidr_ip              = nifcloud_private_lan.main.cidr_block
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "nifcloud_security_group_rule" "positive" {
  security_group_names = ["http"]
  type                 = "IN"
  from_port            = 80
  to_port              = 80
  protocol             = "TCP"
  cidr_ip              = nifcloud_private_lan.main.cidr_block
}
```
