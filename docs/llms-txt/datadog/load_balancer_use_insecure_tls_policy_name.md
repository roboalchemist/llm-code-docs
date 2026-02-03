# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/nifcloud/load_balancer_use_insecure_tls_policy_name.md

---
title: Beta - Nifcloud LB use insecure TLS policy name
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - Nifcloud LB use insecure TLS policy
  name
---

# Beta - Nifcloud LB use insecure TLS policy name

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `675e8eaa-2754-42b7-bf33-bfa295d1601d`

**Cloud Provider:** Nifcloud

**Platform:** Terraform

**Severity:** High

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/nifcloud/nifcloud/latest/docs/resources/load_balancer#ssl_policy_name)

### Description{% #description %}

The `lb` uses an insecure TLS policy. The `nifcloud_load_balancer` resource either omits the `ssl_policy_name` attribute or sets it to an outdated SSL policy. Configure `ssl_policy_name` to use a modern TLS policy (TLS v1.2 or newer) and avoid legacy SSL policies.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "nifcloud_load_balancer" "negative" {
  load_balancer_name = "example"
  instance_port      = 443
  load_balancer_port = 443
  ssl_policy_name    = "Standard Ciphers D ver1"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "nifcloud_load_balancer" "positive" {
  load_balancer_name = "example"
  instance_port      = 443
  load_balancer_port = 443
  ssl_policy_name    = "Standard Ciphers A ver1"
}
```

```terraform
resource "nifcloud_load_balancer" "positive" {
  load_balancer_name = "example"
  instance_port      = 443
  load_balancer_port = 443
}
```
