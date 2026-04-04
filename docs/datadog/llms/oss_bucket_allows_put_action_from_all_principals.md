# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/oss_bucket_allows_put_action_from_all_principals.md

---
title: OSS bucket allows put action from all principals
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > OSS bucket allows put action from all
  principals
---

# OSS bucket allows put action from all principals

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `fe286195-e75c-4359-bd58-00847c4f855a`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** Critical

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/oss_bucket#policy)

### Description{% #description %}

OSS bucket (`alicloud_oss_bucket`) policies must not allow the `Put` action from all principals. This prevents accidental exposure of private data and unauthorized uploads, overwrites, or deletions. The rule flags policies where `Effect` is `Allow`, `Action` includes `Put`, and `Principal` is set to `*` (i.e., applies to all identities). To secure access, restrict `Principal` to specific identities or scope access with conditions.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_oss_bucket" "bucket-policy3" {
  bucket = "bucket-3-policy"
  acl    = "private"

  policy = <<POLICY
  {"Statement": [
    {
        "Action": [
            "oss:PutObjectAcl", "oss:PutObject"
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
resource "alicloud_oss_bucket" "bucket-policy2" {
  bucket = "bucket-2-policy"
  acl    = "private"

  policy = <<POLICY
  {"Statement": [
    {
        "Action": [
            "oss:PutObjectAcl", "oss:PutObject"
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
resource "alicloud_oss_bucket" "bucket-policy1" {
  bucket = "bucket-1-policy"
  acl    = "private"

  policy = <<POLICY
  {"Statement": [
    {
        "Action": [
            "oss:AbortMultipartUpload"
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
resource "alicloud_oss_bucket" "bucket-policy5" {
  bucket = "bucket-5-policy"
  acl    = "private"

  policy = <<POLICY
  {"Statement": [
    {
        "Action": [
            "oss:PutObject", "oss:RestoreObject"
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

```terraform
resource "alicloud_oss_bucket" "bucket-policy4" {
  bucket = "bucket-4-policy"
  acl    = "private"

  policy = <<POLICY
  {"Statement": [
    {
        "Action": [
            "oss:PutObjectAcl", "oss:PutObject"
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
