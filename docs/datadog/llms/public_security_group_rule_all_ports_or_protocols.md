# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/public_security_group_rule_all_ports_or_protocols.md

---
title: Public security group rule all ports or protocols
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Public security group rule all ports or
  protocols
---

# Public security group rule all ports or protocols

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `60587dbd-6b67-432e-90f7-a8cf1892d968`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** High

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/security_group_rule#cidr_ip)

### Description{% #description %}

Alicloud security group rules must not expose all ports or all protocols to the public. This rule flags `alicloud_security_group_rule` resources where:

- `cidr_ip` is `0.0.0.0/0` and `ip_protocol` is `all`, or
- `ip_protocol` is `tcp` or `udp` and `port_range` is `1/65535`, or
- `ip_protocol` is `icmp` or `gre` and `port_range` is `-1/-1`

These configurations expose resources to the public internet and significantly increase the attack surface.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_security_group" "default" {
  name = "default"
}

resource "alicloud_security_group_rule" "allow_all_tcp" {
  type              = "ingress"
  ip_protocol       = "icmp"
  nic_type          = "internet"
  policy            = "accept"
  port_range        = "-1/-1"
  priority          = 1
  security_group_id = alicloud_security_group.default.id
  cidr_ip           = "10.159.6.18/12"
}
```

```terraform
resource "alicloud_security_group" "default" {
  name = "default"
}

resource "alicloud_security_group_rule" "allow_all_tcp" {
  type              = "ingress"
  ip_protocol       = "tcp"
  nic_type          = "internet"
  policy            = "accept"
  port_range        = "1/65535"
  priority          = 1
  security_group_id = alicloud_security_group.default.id
  cidr_ip           = "10.159.6.18/12"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "alicloud_security_group" "default" {
  name = "default"
}

resource "alicloud_security_group_rule" "allow_all_tcp" {
  type              = "ingress"
  ip_protocol       = "gre"
  nic_type          = "internet"
  policy            = "accept"
  port_range        = "-1/-1"
  priority          = 1
  security_group_id = alicloud_security_group.default.id
  cidr_ip           = "0.0.0.0/0"
}
```

```terraform
resource "alicloud_security_group" "default" {
  name = "default"
}

resource "alicloud_security_group_rule" "allow_all_tcp" {
  type              = "ingress"
  ip_protocol       = "tcp"
  nic_type          = "internet"
  policy            = "accept"
  port_range        = "1/65535"
  priority          = 1
  security_group_id = alicloud_security_group.default.id
  cidr_ip           = "0.0.0.0/0"
}
```

```terraform
resource "alicloud_security_group" "default" {
  name = "default"
}

resource "alicloud_security_group_rule" "allow_all_tcp" {
  type              = "ingress"
  ip_protocol       = "all"
  nic_type          = "internet"
  policy            = "accept"
  port_range        = "-1/-1"
  priority          = 1
  security_group_id = alicloud_security_group.default.id
  cidr_ip           = "0.0.0.0/0"
}
```
