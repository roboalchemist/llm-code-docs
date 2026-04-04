# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/athena_database_not_encrypted.md

---
title: Athena database not encrypted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Athena database not encrypted
---

# Athena database not encrypted

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `b2315cae-b110-4426-81e0-80bb8640cdd3`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/athena_database#encryption_configuration)

### Description{% #description %}

AWS Athena databases store query results in S3 buckets, and when not encrypted, sensitive data may be exposed to unauthorized access, potentially leading to data breaches and compliance violations. Encryption at rest protects this data using keys managed either by AWS or customer-managed KMS keys. To secure your implementation, add an `encryption_configuration` block to your `aws_athena_database` resource, as shown below:

```terraform
resource "aws_athena_database" "secure_example" {
  name   = "database_name"
  bucket = aws_s3_bucket.example.bucket

  encryption_configuration {
    encryption_option = "SSE_KMS"
    kms_key           = "your_kms_key_arn"
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_s3_bucket" "hoge" {
  bucket = "hoge"
}

resource "aws_athena_database" "hoge" {
  name   = "database_name"
  bucket = aws_s3_bucket.hoge.bucket

  encryption_configuration {
    encryption_option = "SSE_KMS"
    kms_key           = "SSE_KMS"
 }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_s3_bucket" "hoge" {
  bucket = "hoge"
}

resource "aws_athena_database" "hoge" {
  name   = "database_name"
  bucket = aws_s3_bucket.hoge.bucket
}
```
