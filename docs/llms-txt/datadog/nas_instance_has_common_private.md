# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/nifcloud/nas_instance_has_common_private.md

---
title: Beta - Nifcloud NAS has common private network
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - Nifcloud NAS has common private network
---

# Beta - Nifcloud NAS has common private network

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `4b801c38-ebb4-4c81-984b-1ba525d43adf`

**Cloud Provider:** Nifcloud

**Platform:** Terraform

**Severity:** Low

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/nifcloud/nifcloud/latest/docs/resources/nas_instance#network_id)

### Description{% #description %}

The NAS instance uses the shared private network `net-COMMON_PRIVATE` rather than an isolated private LAN. `nifcloud_nas_instance` resources should use a dedicated private LAN to isolate the private-side network from the shared network. This rule flags `nifcloud_nas_instance` resources that reference `net-COMMON_PRIVATE`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "nifcloud_nas_instance" "negative" {
  identifier        = "nas001"
  allocated_storage = 100
  protocol          = "nfs"
  type              = 0
  network_id        = nifcloud_private_lan.main.id
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "nifcloud_nas_instance" "positive" {
  identifier        = "nas001"
  allocated_storage = 100
  protocol          = "nfs"
  type              = 0
  network_id        = "net-COMMON_PRIVATE"
}
```
