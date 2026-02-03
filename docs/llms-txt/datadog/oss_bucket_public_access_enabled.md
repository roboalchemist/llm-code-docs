# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/oss_bucket_public_access_enabled.md

---
title: OSS bucket public access enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > OSS bucket public access enabled
---

# OSS bucket public access enabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `62232513-b16f-4010-83d7-51d0e1d45426`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** High

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/oss_bucket#acl)

### Description{% #description %}

OSS buckets should have public access disabled. This rule flags `alicloud_oss_bucket` resources where `acl` is set to `public-read` or `public-read-write`. To restrict access, set `acl = "private"` or remove the `acl` attribute.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_oss_bucket" "bucket_public_access_enabled4" {
  bucket = "bucket-170309-acl"
}
```

```terraform
resource "alicloud_oss_bucket" "bucket_public_access_enabled1" {
  bucket = "bucket-170309-acl"
  acl    = "private"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "alicloud_oss_bucket" "bucket_public_access_enabled3" {
  bucket = "bucket-170309-acl"
  acl    = "public-read-write"
}

resource "alicloud_oss_bucket" "bucket-logging" {
  bucket = "bucket-170309-logging"

  logging {
    target_bucket = alicloud_oss_bucket.bucket-target.id
    target_prefix = "log/"
  }
}
```

```terraform
resource "alicloud_oss_bucket" "bucket_public_access_enabled2" {
  bucket = "bucket-170309-acl"
  acl    = "public-read"
}
```
