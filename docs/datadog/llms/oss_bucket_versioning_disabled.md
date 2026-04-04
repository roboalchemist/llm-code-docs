# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/oss_bucket_versioning_disabled.md

---
title: OSS bucket versioning disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > OSS bucket versioning disabled
---

# OSS bucket versioning disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `70919c0b-2548-4e6b-8d7a-3d84ab6dabba`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** Medium

**Category:** Backup

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/oss_bucket#versioning)

### Description{% #description %}

OSS bucket resources (`alicloud_oss_bucket`) should have `versioning.status` set to `Enabled`. This rule flags buckets where `versioning.status` is `Suspended`, or where the `versioning` block is missing. To remediate, add or update the `versioning` block so that `status = "Enabled"`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_oss_bucket" "bucket-versioning1" {
  bucket = "bucket-170309-versioning"
  acl    = "private"

  versioning {
    status = "Enabled"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "alicloud_oss_bucket" "bucket-versioning3" {
  bucket = "bucket-170309-versioning"
  acl    = "private"
}
```

```terraform
resource "alicloud_oss_bucket" "bucket-versioning2" {
  bucket = "bucket-170309-versioning"
  acl    = "private"

  versioning {
    status = "Suspended"
  }
}
```
