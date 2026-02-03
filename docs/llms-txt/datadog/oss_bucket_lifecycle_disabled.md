# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/oss_bucket_lifecycle_disabled.md

---
title: OSS bucket lifecycle rule disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > OSS bucket lifecycle rule disabled
---

# OSS bucket lifecycle rule disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `7db8bd7e-9772-478c-9ec5-4bc202c5686f`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** Low

**Category:** Backup

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/oss_bucket#lifecycle_rule)

### Description{% #description %}

`alicloud_oss_bucket` resources should include a `lifecycle_rule` block with `enabled` set to `true`. If the `lifecycle_rule` block is missing, the policy reports a `MissingAttribute` issue. If the block exists but `enabled` is `false`, the policy reports an `IncorrectValue` issue and recommends changing `enabled` from `false` to `true`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_oss_bucket" "oss_bucket_lifecycle_enabled1" {
  bucket = "bucket-170309-lifecycle"
  acl    = "public-read"

  lifecycle_rule {
    id      = "rule-days"
    prefix  = "path1/"
    enabled = true

    expiration {
      days = 365
    }
  }
  lifecycle_rule {
    id      = "rule-date"
    prefix  = "path2/"
    enabled = true

    expiration {
      date = "2018-01-12"
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "alicloud_oss_bucket" "oss_bucket_lifecycle_enabled3" {
  bucket = "bucket-170309-versioning"
  acl    = "private"

  versioning {
    status = "Enabled"
  }
}
```

```terraform
resource "alicloud_oss_bucket" "oss_bucket_lifecycle_enabled2" {
  bucket = "bucket-170309-lifecycle"
  acl    = "public-read"

  lifecycle_rule {
    id      = "rule-days"
    prefix  = "path1/"
    enabled = false

    expiration {
      days = 365
    }
  }
  lifecycle_rule {
    id      = "rule-date"
    prefix  = "path2/"
    enabled = true

    expiration {
      date = "2018-01-12"
    }
  }
}
```
