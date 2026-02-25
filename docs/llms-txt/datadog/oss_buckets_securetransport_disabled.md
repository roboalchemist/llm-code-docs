# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/oss_buckets_securetransport_disabled.md

---
title: OSS buckets secure transport disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > OSS buckets secure transport disabled
---

# OSS buckets secure transport disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `c01d10de-c468-4790-b3a0-fc887a56f289`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/oss_bucket#policy)

### Description{% #description %}

OSS buckets should have secure transport enabled. The bucket policy should deny requests when `acs:SecureTransport` is `false`, or allow requests only when `acs:SecureTransport` is `true`. This condition must apply to any principal. Enforcing this prevents acceptance of HTTP requests and ensures data is transferred over TLS.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_oss_bucket" "bucket-securetransport4"{
        policy = <<POLICY
{
        "Version": "1",
        "Statement":
        [
            {
                "Effect": "Allow",
                "Action":
                [
                    "oss:RestoreObject",
                    "oss:ListObjects",
                    "oss:AbortMultipartUpload",
                    "oss:PutObjectAcl",
                    "oss:GetObjectAcl",
                    "oss:ListParts",
                    "oss:DeleteObject",
                    "oss:PutObject",
                    "oss:GetObject",
                    "oss:GetVodPlaylist",
                    "oss:PostVodPlaylist",
                    "oss:PublishRtmpStream",
                    "oss:ListObjectVersions",
                    "oss:GetObjectVersion",
                    "oss:GetObjectVersionAcl",
                    "oss:RestoreObjectVersion"
                ],
                "Principal":
                [
                    "*"
                ],
                "Resource":
                [
                    "acs:oss:*:0000111122223334:af/*"
                ],
                "Condition":
                {
                    "Bool":
                    {
                        "acs:SecureTransport": [ "true" ]
                    }
                }
            }
        ]
}
POLICY

}

```

```terraform
resource "alicloud_oss_bucket" "bucket-securetransport2"{
        policy = <<POLICY
{
        "Version": "1",
        "Statement":
        [
            {
                "Effect": "Deny",
                "Action":
                [
                    "oss:RestoreObject",
                    "oss:ListObjects",
                    "oss:AbortMultipartUpload",
                    "oss:PutObjectAcl",
                    "oss:GetObjectAcl",
                    "oss:ListParts",
                    "oss:DeleteObject",
                    "oss:PutObject",
                    "oss:GetObject",
                    "oss:GetVodPlaylist",
                    "oss:PostVodPlaylist",
                    "oss:PublishRtmpStream",
                    "oss:ListObjectVersions",
                    "oss:GetObjectVersion",
                    "oss:GetObjectVersionAcl",
                    "oss:RestoreObjectVersion"
                ],
                "Principal":
                [
                    "*"
                ],
                "Resource":
                [
                    "acs:oss:*:0000111122223334:af/*"
                ],
                "Condition":
                {
                    "Bool":
                    {
                        "acs:SecureTransport": [ "false" ]
                    }
                }
            }
        ]
}
POLICY

}

```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "alicloud_oss_bucket" "bucket-securetransport3" {
  bucket = "bucket-170309-policy"
  acl    = "private"

  policy = <<POLICY
  {"Statement":
      [{"Action":
          ["oss:PutObject", "oss:GetObject", "oss:DeleteBucket"],
        "Effect":"Allow",
        "Resource":
            ["acs:oss:*:*:*"]}],
   "Version":"1"}
  POLICY
}
```

```terraform
resource "alicloud_oss_bucket" "bucket-securetransport1"{
        policy = <<POLICY
{
        "Version": "1",
        "Statement":
        [
            {
                "Effect": "Allow",
                "Action":
                [
                    "oss:RestoreObject",
                    "oss:ListObjects",
                    "oss:AbortMultipartUpload",
                    "oss:PutObjectAcl",
                    "oss:GetObjectAcl",
                    "oss:ListParts",
                    "oss:DeleteObject",
                    "oss:PutObject",
                    "oss:GetObject",
                    "oss:GetVodPlaylist",
                    "oss:PostVodPlaylist",
                    "oss:PublishRtmpStream",
                    "oss:ListObjectVersions",
                    "oss:GetObjectVersion",
                    "oss:GetObjectVersionAcl",
                    "oss:RestoreObjectVersion"
                ],
                "Principal":
                [
                    "*"
                ],
                "Resource":
                [
                    "acs:oss:*:0000111122223334:af/*"
                ],
                "Condition":
                {
                    "Bool":
                    {
                        "acs:SecureTransport": [ "false" ]
                    }
                }
            }
        ]
}
POLICY

}

```
