# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/nifcloud/computing_instance_has_common_private.md

---
title: Beta - Nifcloud computing has common private network
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - Nifcloud computing has common private
  network
---

# Beta - Nifcloud computing has common private network

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `df58dd45-8009-43c2-90f7-c90eb9d53ed9`

**Cloud Provider:** Nifcloud

**Platform:** Terraform

**Severity:** Low

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/nifcloud/nifcloud/latest/docs/resources/instance#network_id)

### Description{% #description %}

The instance uses the common private network. The `nifcloud_instance` resource's `network_interface.network_id` is set to `net-COMMON_PRIVATE`. The instance should use a private LAN to isolate the private-side network from the shared network.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "nifcloud_instance" "negative" {
  image_id        = data.nifcloud_image.ubuntu.id
  security_group  = nifcloud_security_group.example.group_name
  network_interface {
    network_id = nifcloud_private_lan.main.id
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "nifcloud_instance" "positive" {
  image_id        = data.nifcloud_image.ubuntu.id
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
resource "nifcloud_instance" "positive" {
  image_id        = data.nifcloud_image.ubuntu.id
  security_group  = nifcloud_security_group.example.group_name
  network_interface {
    network_id = "net-COMMON_PRIVATE"
  }
}
```
