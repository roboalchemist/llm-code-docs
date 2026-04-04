# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/nifcloud/nas_security_group_description_undefined.md

---
title: Beta - Nifcloud NAS undefined description to NAS security group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - Nifcloud NAS undefined description to
  NAS security group
---

# Beta - Nifcloud NAS undefined description to NAS security group

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `e840c54a-7a4c-405f-b8c1-c49a54b87d11`

**Cloud Provider:** Nifcloud

**Platform:** Terraform

**Severity:** Low

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/nifcloud/nifcloud/latest/docs/resources/nas_security_group#description)

### Description{% #description %}

Missing description for `nifcloud_nas_security_group`. Detects `nifcloud_nas_security_group` resources that do not include the `description` attribute. A `description` is required for auditing and inventory purposes; provide a meaningful `description` to clarify the resource's purpose.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "nifcloud_nas_security_group" "negative" {
  group_name  = "app"
  description = "Allow from app traffic"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "nifcloud_nas_security_group" "positive" {
  group_name  = "app"
}
```
