# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/nifcloud/nas_security_group_has_public_ingress_sgr.md

---
title: Beta - Nifcloud NAS has public ingress NAS security group rule
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - Nifcloud NAS has public ingress NAS
  security group rule
---

# Beta - Nifcloud NAS has public ingress NAS security group rule

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `8d7758a7-d9cd-499a-a83e-c9bdcbff728d`

**Cloud Provider:** Nifcloud

**Platform:** Terraform

**Severity:** High

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/nifcloud/nifcloud/latest/docs/resources/nas_security_group#cidr_ip)

### Description{% #description %}

An ingress `nifcloud_nas_security_group` rule allows traffic from `/0`. This permits access from the entire Internet and is overly permissive. Use a more restrictive CIDR range to limit allowed sources.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "nifcloud_nas_security_group" "negative" {
  group_name        = "nasgroup001"
  availability_zone = "east-11"

  rule {
    cidr_ip = "10.0.0.0/16"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "nifcloud_nas_security_group" "positive" {
  group_name        = "nasgroup001"
  availability_zone = "east-11"

  rule {
    cidr_ip = "0.0.0.0/0"
  }
}
```
