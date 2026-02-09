# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/oss_bucket_logging_disabled.md

---
title: OSS bucket logging disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > OSS bucket logging disabled
---

# OSS bucket logging disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `05db341e-de7d-4972-a106-3e2bd5ee53e1`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** Medium

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/oss_bucket#logging)

### Description{% #description %}

OSS buckets should have logging enabled to improve visibility into resource and object access. The `alicloud_oss_bucket` resource must include a `logging` block with `logging_isenable` set to `true`. If the `logging` block is missing or `logging_isenable` is `false`, access logging is not enabled. To remediate, add the block or update `logging_isenable` from `false` to `true`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_oss_bucket" "bucket_logging1" {
  bucket = "bucket-170309-logging"

  logging {
    target_bucket = alicloud_oss_bucket.bucket-target.id
    target_prefix = "log/"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "alicloud_oss_bucket" "bucket_logging1" {
  bucket = "bucket-170309-logging"
  logging_isenable = false

  logging {
    target_bucket = alicloud_oss_bucket.bucket-target.id
    target_prefix = "log/"
  }
}
```

```terraform
resource "alicloud_oss_bucket" "bucket_logging2" {
  bucket = "bucket-170309-acl"
  acl    = "public-read"
}
```
