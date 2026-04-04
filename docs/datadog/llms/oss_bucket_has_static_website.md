# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/oss_bucket_has_static_website.md

---
title: OSS bucket has static website
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > OSS bucket has static website
---

# OSS bucket has static website

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `2b13c6ff-b87a-484d-86fd-21ef6e97d426`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** High

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/oss_bucket#website)

### Description{% #description %}

Checks whether any static websites are hosted on OSS buckets by detecting the `website` attribute in `alicloud_oss_bucket` resources. Buckets with the `website` attribute are flagged, as static website hosting may lead to unintended public exposure or accidental content hosting. The rule reports an `IncorrectValue` when `website` is present. Be aware of any website configurations in use.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_oss_bucket" "bucket-acl1" {
  bucket = "bucket-1-acl"
  acl    = "private"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "alicloud_oss_bucket" "bucket-website1" {
  bucket = "bucket-1-website"

  website {
    index_document = "index.html"
    error_document = "error.html"
  }
}
```
