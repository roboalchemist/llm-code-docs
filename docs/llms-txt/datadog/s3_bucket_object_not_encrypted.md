# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/s3_bucket_object_not_encrypted.md

---
title: S3 bucket object not encrypted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > S3 bucket object not encrypted
---

# S3 bucket object not encrypted

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `5fb49a69-8d46-4495-a2f8-9c8c622b2b6e`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_object#server_side_encryption)

### Description{% #description %}

This check verifies that S3 bucket objects have server-side encryption enabled to protect sensitive data at rest. Unencrypted S3 objects could expose confidential information if unauthorized access occurs, potentially leading to data breaches and compliance violations. Server-side encryption is a critical security control that should be implemented for all objects stored in S3 buckets.

The vulnerability occurs when the `server_side_encryption` attribute is missing in an `aws_s3_bucket_object` resource, as shown in this insecure example:

```hcl
resource "aws_s3_bucket_object" "examplebucket_object" {
  key    = "someobject"
  bucket = aws_s3_bucket.examplebucket.id
  source = "index.html"
}
```

To remediate this issue, add the `server_side_encryption` attribute with an appropriate encryption algorithm such as `AES256` or `aws:kms`:

```hcl
resource "aws_s3_bucket_object" "examplebucket_object" {
  key                    = "someobject"
  bucket                 = aws_s3_bucket.examplebucket.id
  source                 = "index.html"
  server_side_encryption = "AES256"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_s3_bucket" "examplebucket" {
  bucket = "examplebuckettftest"
  acl    = "private"

  versioning {
    enabled = true
  }

  object_lock_configuration {
    object_lock_enabled = "Enabled"
  }
}

resource "aws_s3_bucket_object" "examplebucket_object" {
  key                    = "someobject"
  bucket                 = aws_s3_bucket.examplebucket.id
  source                 = "index.html"
  server_side_encryption = "AES256"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_s3_bucket" "examplebucket" {
  bucket = "examplebuckettftest"
  acl    = "private"

  versioning {
    enabled = true
  }

  object_lock_configuration {
    object_lock_enabled = "Enabled"
  }
}

resource "aws_s3_bucket_object" "examplebucket_object" {
  key                    = "someobject"
  bucket                 = aws_s3_bucket.examplebucket.id
  source                 = "index.html"
}
```
