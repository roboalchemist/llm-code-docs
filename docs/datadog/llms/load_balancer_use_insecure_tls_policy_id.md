# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/nifcloud/load_balancer_use_insecure_tls_policy_id.md

---
title: Beta - Nifcloud LB use insecure TLS policy ID
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - Nifcloud LB use insecure TLS policy ID
---

# Beta - Nifcloud LB use insecure TLS policy ID

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `944439c7-b4b8-476a-8f83-14641ea876ba`

**Cloud Provider:** Nifcloud

**Platform:** Terraform

**Severity:** High

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/nifcloud/nifcloud/latest/docs/resources/load_balancer#ssl_policy_id)

### Description{% #description %}

The load balancer uses an insecure TLS policy. This rule flags `nifcloud_load_balancer` resources that either omit `ssl_policy_id` or set `ssl_policy_id` to an outdated policy identifier (`1`, `2`, `3`, `5`, `8`). Resources must use `TLS v1.2+` for secure encryption.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "nifcloud_load_balancer" "negative" {
  load_balancer_name = "example"
  instance_port      = 443
  load_balancer_port = 443
  ssl_policy_id      = "4"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "nifcloud_load_balancer" "positive" {
  load_balancer_name = "example"
  instance_port      = 443
  load_balancer_port = 443
  ssl_policy_name    = "1"
}
```

```terraform
resource "nifcloud_load_balancer" "positive" {
  load_balancer_name = "example"
  instance_port      = 443
  load_balancer_port = 443
}
```
