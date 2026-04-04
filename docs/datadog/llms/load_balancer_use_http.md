# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/nifcloud/load_balancer_use_http.md

---
title: Beta - Nifcloud LB use HTTP port
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - Nifcloud LB use HTTP port
---

# Beta - Nifcloud LB use HTTP port

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `94e47f3f-b90b-43a1-a36d-521580bae863`

**Cloud Provider:** Nifcloud

**Platform:** Terraform

**Severity:** High

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/nifcloud/nifcloud/latest/docs/resources/load_balancer#load_balancer_port)

### Description{% #description %}

The `nifcloud_load_balancer` is configured to use the HTTP port (`load_balancer_port` is set to `80`). It should be switched to HTTPS to benefit from TLS security features. The rule reports an `IncorrectValue` issue when `load_balancer_port` equals `80`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "nifcloud_load_balancer" "negative" {
  load_balancer_name = "example"
  instance_port      = 443
  load_balancer_port = 443
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "nifcloud_load_balancer" "positive" {
  load_balancer_name = "example"
  instance_port      = 80
  load_balancer_port = 80
}
```
