# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/nifcloud/router_security_group_undefined.md

---
title: Beta - Nifcloud router undefined security group to router
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - Nifcloud router undefined security
  group to router
---

# Beta - Nifcloud router undefined security group to router

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `e7dada38-af20-4899-8955-dabea84ab1f0`

**Cloud Provider:** Nifcloud

**Platform:** Terraform

**Severity:** High

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/nifcloud/nifcloud/latest/docs/resources/router#security_group)

### Description{% #description %}

`nifcloud_router` resources must include a `security_group` attribute. Routers without a `security_group` lack explicit network access controls and may be insecure. This rule flags any `nifcloud_router` missing `security_group` and reports attributes: `documentId`, `resourceType`, `resourceName`, `searchKey`, `issueType`, `keyExpectedValue`, `keyActualValue`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "nifcloud_router" "negative" {
  security_group = nifcloud_security_group.router.group_name

  network_interface {
    network_id = "net-COMMON_GLOBAL"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "nifcloud_router" "positive" {
  network_interface {
    network_id = "net-COMMON_GLOBAL"
  }
}
```
