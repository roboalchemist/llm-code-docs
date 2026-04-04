# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/oss_bucket_cmk_encryption_disabled.md

---
title: OSS bucket encryption using CMK disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > OSS bucket encryption using CMK disabled
---

# OSS bucket encryption using CMK disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `f20e97f9-4919-43f1-9be9-f203cd339cdd`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** Medium

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/oss_bucket#server_side_encryption_rule)

### Description{% #description %}

`alicloud_oss_bucket` resources must have server-side encryption enabled and configured to use a customer-managed KMS key. The `server_side_encryption_rule` block must be present, and the `kms_master_key_id` attribute must be set. Absence of either is considered a policy violation.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_oss_bucket" "bucket_cmk_encryption1" {
  bucket = "bucket-170309-sserule"
  acl    = "private"

  server_side_encryption_rule {
    sse_algorithm     = "KMS"
    kms_master_key_id = "your kms key id"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "alicloud_oss_bucket" "bucket_cmk_encryption3" {
  bucket = "bucket-170309-sserule"
  acl    = "private"
}
```

```terraform
resource "alicloud_oss_bucket" "bucket_cmk_encryption2" {
  bucket = "bucket-170309-sserule"
  acl    = "private"

  server_side_encryption_rule {
    sse_algorithm = "AES256"
  }
}
```
