# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/nifcloud/vpn_gateway_security_group_undefined.md

---
title: Beta - Nifcloud VPN gateway undefined security group to VPN gateway
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - Nifcloud VPN gateway undefined security
  group to VPN gateway
---

# Beta - Nifcloud VPN gateway undefined security group to VPN gateway

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `b3535a48-910c-47f8-8b3b-14222f29ef80`

**Cloud Provider:** Nifcloud

**Platform:** Terraform

**Severity:** High

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/nifcloud/nifcloud/latest/docs/resources/vpn_gateway#security_group)

### Description{% #description %}

VPN gateway is missing `security_group`. `nifcloud_vpn_gateway` resources should include a `security_group` attribute for security purposes. This rule detects `nifcloud_vpn_gateway` resources that do not include a `security_group`, which can leave the VPN gateway exposed or indicate an incomplete configuration.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "nifcloud_vpn_gateway" "negative" {
  security_group  = nifcloud_security_group.example.group_name

  network_interface {
    network_id = "net-COMMON_GLOBAL"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "nifcloud_vpn_gateway" "positive" {
  network_interface {
    network_id = "net-COMMON_GLOBAL"
  }
}
```
