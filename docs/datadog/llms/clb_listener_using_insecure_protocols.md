# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/tencentcloud/clb_listener_using_insecure_protocols.md

---
title: Beta - CLB listener using insecure protocols
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - CLB listener using insecure protocols
---

# Beta - CLB listener using insecure protocols

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `fe08b81c-12e9-4b5e-9006-4218fca750fd`

**Cloud Provider:** TencentCloud

**Platform:** Terraform

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/tencentcloudstack/tencentcloud/latest/docs/resources/clb_listener#protocol)

### Description{% #description %}

The CLB listener `protocol` must not be set to insecure protocols such as `TCP`, `UDP`, or `HTTP`. This rule checks `tencentcloud_clb_listener` resources and flags any instance where the `protocol` is one of these insecure values. Resources configured with these protocols are considered insecure and are reported.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "tencentcloud_clb_listener" "listener" {
  clb_id        = "lb-0lh5au7v"
  listener_name = "test_listener"
  protocol      = "HTTPS"
  port          = 443
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "tencentcloud_clb_listener" "listener" {
  clb_id        = "lb-0lh5au7v"
  listener_name = "test_listener"
  protocol      = "TCP"
  port          = 8080
}
```

```terraform
resource "tencentcloud_clb_listener" "listener" {
  clb_id        = "lb-0lh5au7v"
  listener_name = "test_listener"
  protocol      = "UDP"
  port          = 8090
}
```

```terraform
resource "tencentcloud_clb_listener" "listener" {
  clb_id        = "lb-0lh5au7v"
  listener_name = "test_listener"
  protocol      = "HTTP"
  port          = 80
}
```
