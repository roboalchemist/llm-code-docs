# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/oss_bucket_transfer_acceleration_disabled.md

---
title: OSS bucket transfer acceleration disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > OSS bucket transfer acceleration disabled
---

# OSS bucket transfer acceleration disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `8f98334a-99aa-4d85-b72a-1399ca010413`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** Low

**Category:** Availability

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/oss_bucket#transfer_acceleration)

### Description{% #description %}

An OSS bucket should have `transfer_acceleration.enabled` set to `true`. This rule inspects `alicloud_oss_bucket` resources and reports when the `transfer_acceleration` block is missing or when `transfer_acceleration.enabled` is `false`. It recommends adding a `transfer_acceleration` block with `enabled = true` or updating the existing value to `true`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_oss_bucket" "bucket-accelerate3" {
  bucket = "bucket_name"

  transfer_acceleration {
    enabled = true
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "alicloud_oss_bucket" "bucket-accelerate2" {
  bucket = "bucket_name"
}
```

```terraform
resource "alicloud_oss_bucket" "bucket-accelerate" {
  bucket = "bucket_name"

  transfer_acceleration {
    enabled = false
  }
}
```
