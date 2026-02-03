# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/nifcloud/db_instance_has_common_private.md

---
title: Beta - Nifcloud RDB has common private network
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - Nifcloud RDB has common private network
---

# Beta - Nifcloud RDB has common private network

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `9bf57c23-fbab-4222-85f3-3f207a53c6a8`

**Cloud Provider:** Nifcloud

**Platform:** Terraform

**Severity:** Low

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/nifcloud/nifcloud/latest/docs/resources/db_instance#network_id)

### Description{% #description %}

`nifcloud_db_instance` is configured to use the common private LAN `net-COMMON_PRIVATE`. The resource's `network_id` should be a private LAN that isolates the private-side network from the shared network. This rule identifies `nifcloud_db_instance` resources that are using the common private network.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "nifcloud_db_instance" "negative" {
  identifier     = "example"
  instance_class = "db.large8"
  network_id     = nifcloud_private_lan.main.id
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "nifcloud_db_instance" "positive" {
  identifier     = "example"
  instance_class = "db.large8"
  network_id     = "net-COMMON_PRIVATE"
}
```
