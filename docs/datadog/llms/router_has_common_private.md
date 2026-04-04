# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/nifcloud/router_has_common_private.md

---
title: Beta - Nifcloud router has common private network
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - Nifcloud router has common private
  network
---

# Beta - Nifcloud router has common private network

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `30c2760c-740e-4672-9d7f-2c29e0cb385d`

**Cloud Provider:** Nifcloud

**Platform:** Terraform

**Severity:** Low

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/nifcloud/nifcloud/latest/docs/resources/router#network_id)

### Description{% #description %}

The `nifcloud_router` is configured to use the common private network (`net-COMMON_PRIVATE`). This rule detects `nifcloud_router` resources where `network_interface[_].network_id` or `network_interface.network_id` is set to `net-COMMON_PRIVATE`. The router should use a dedicated private LAN to isolate the private-side network from the shared network.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "nifcloud_router" "negative" {
  security_group  = nifcloud_security_group.example.group_name

  network_interface {
    network_id = nifcloud_private_lan.main.id
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "nifcloud_router" "positive" {
  security_group  = nifcloud_security_group.example.group_name

  network_interface {
    network_id = "net-COMMON_GLOBAL"
  }

  network_interface {
    network_id = "net-COMMON_PRIVATE"
  }
}
```

```terraform
resource "nifcloud_router" "positive" {
  security_group  = nifcloud_security_group.example.group_name

  network_interface {
    network_id = "net-COMMON_PRIVATE"
  }
}
```
