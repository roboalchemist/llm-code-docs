# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/nifcloud/computing_instance_has_public_ingress_sgr.md

---
title: Beta - Nifcloud computing has public ingress security group rule
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - Nifcloud computing has public ingress
  security group rule
---

# Beta - Nifcloud computing has public ingress security group rule

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `b2ea2367-8dc9-4231-a035-d0b28bfa3dde`

**Cloud Provider:** Nifcloud

**Platform:** Terraform

**Severity:** High

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/nifcloud/nifcloud/latest/docs/resources/security_group_rule#cidr_ip)

### Description{% #description %}

An ingress `nifcloud_security_group_rule` allows traffic from a `/0` CIDR. The policy detects `nifcloud_security_group_rule` resources whose `cidr_ip` is `/0` (allowing traffic from anywhere) and flags them as insecure. The rule reports the following attributes: `documentId`, `resourceType`, `resourceName`, `searchKey`, `issueType`, `keyExpectedValue`, and `keyActualValue`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "nifcloud_security_group_rule" "negative" {
  security_group_names = ["http"]
  type                 = "IN"
  description          = "HTTP from VPC"
  from_port            = 80
  to_port              = 80
  protocol             = "TCP"
  cidr_ip              = "10.0.0.0/16"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "nifcloud_security_group_rule" "positive" {
  security_group_names = ["http"]
  type                 = "IN"
  description          = "HTTP from VPC"
  from_port            = 80
  to_port              = 80
  protocol             = "TCP"
  cidr_ip              = "0.0.0.0/0"
}
```
