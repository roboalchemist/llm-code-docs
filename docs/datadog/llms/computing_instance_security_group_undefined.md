# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/nifcloud/computing_instance_security_group_undefined.md

---
title: Beta - Nifcloud computing undefined security group to instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - Nifcloud computing undefined security
  group to instance
---

# Beta - Nifcloud computing undefined security group to instance

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `89218b48-75c9-4cb3-aaba-5299e852e8bc`

**Cloud Provider:** Nifcloud

**Platform:** Terraform

**Severity:** High

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/nifcloud/nifcloud/latest/docs/resources/instance#security_group)

### Description{% #description %}

Missing `security_group` on `nifcloud_instance` resources. The `nifcloud_instance` resource should include a `security_group` to enforce network-level access controls. Instances that do not set a `security_group` are flagged as `MissingAttribute`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "nifcloud_instance" "negative" {
  image_id        = data.nifcloud_image.ubuntu.id
  security_group  = nifcloud_security_group.example.group_name
  network_interface {
    network_id = "net-COMMON_GLOBAL"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "nifcloud_instance" "positive" {
  image_id        = data.nifcloud_image.ubuntu.id
  network_interface {
    network_id = "net-COMMON_GLOBAL"
  }
}
```
