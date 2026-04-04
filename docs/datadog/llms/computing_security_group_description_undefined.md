# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/nifcloud/computing_security_group_description_undefined.md

---
title: Beta - Nifcloud computing undefined description to security group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - Nifcloud computing undefined
  description to security group
---

# Beta - Nifcloud computing undefined description to security group

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `41c127a9-3a85-4bc3-a333-ed374eb9c3e4`

**Cloud Provider:** Nifcloud

**Platform:** Terraform

**Severity:** Low

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/nifcloud/nifcloud/latest/docs/resources/security_group#description)

### Description{% #description %}

Missing `description` for `nifcloud_security_group` resources. The `description` attribute must be present to support auditing and to document the purpose and intent of the security group. Resources without a `description` hinder security reviews and operational tracing.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "nifcloud_security_group" "negative" {
  group_name  = "http"
  description = "Allow inbound HTTP traffic"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "nifcloud_security_group" "positive" {
  group_name  = "http"
}
```
