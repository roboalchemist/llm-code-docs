# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/oss_bucket_allows_delete_from_all_principals.md

---
title: OSS bucket allows delete action from all principals
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > OSS bucket allows delete action from all
  principals
---

# OSS bucket allows delete action from all principals

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `8c0695d8-2378-4cd6-8243-7fd5894fa574`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** Critical

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/oss_bucket#policy)

### Description{% #description %}

An `alicloud_oss_bucket` should not allow the `DeleteBucket` action from all principals. Allowing this action may expose private data or enable unauthorized deletion or tampering. This rule asserts that `Effect` must not be `Allow` when `Action` is `DeleteBucket` and `Principal` is set to `"*"`. The policy evaluated is the `policy` attribute on the `alicloud_oss_bucket` resource.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_oss_bucket" "bucket-policy4" {
  bucket = "bucket-4-policy"
  acl    = "private"

  policy = <<POLICY
  {"Statement": [
    {
        "Action": [
            "oss:PutObject", "oss:DeleteBucket"
        ],
        "Effect": "Deny",
        "Principal": [
            "*"
        ],
        "Resource": [
            "acs:oss:*:174649585760xxxx:examplebucket"
        ]
    }
  ],
   "Version":"1"}
  POLICY
}
```

```terraform
resource "alicloud_oss_bucket" "bucket-policy3" {
  bucket = "bucket-3-policy"
  acl    = "private"

  policy = <<POLICY
  {"Statement": [
    {
        "Action": [
            "oss:PutObject", "oss:DeleteBucket"
        ],
        "Effect": "Allow",
        "Principal": [
            "20214760404935xxxx"
        ],
        "Resource": [
            "acs:oss:*:174649585760xxxx:examplebucket"
        ]
    }
  ],
   "Version":"1"}
  POLICY
}
```

```terraform
resource "alicloud_oss_bucket" "bucket-policy2" {
  bucket = "bucket-2-policy"
  acl    = "private"

  policy = <<POLICY
  {"Statement": [
    {
        "Action": [
            "oss:ListObjects"
        ],
        "Effect": "Allow",
        "Principal": [
            "*"
        ],
        "Resource": [
            "acs:oss:*:174649585760xxxx:examplebucket"
        ]
    }
  ],
   "Version":"1"}
  POLICY
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "alicloud_oss_bucket" "bucket-policy1" {
  bucket = "bucket-1-policy"
  acl    = "private"

  policy = <<POLICY
  {"Statement": [
    {
        "Action": [
            "oss:PutObject", "oss:DeleteBucket"
        ],
        "Effect": "Allow",
        "Principal": [
            "*"
        ],
        "Resource": [
            "acs:oss:*:174649585760xxxx:examplebucket"
        ]
    }
  ],
   "Version":"1"}
  POLICY
}
```
