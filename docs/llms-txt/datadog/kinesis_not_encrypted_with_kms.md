# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/kinesis_not_encrypted_with_kms.md

---
title: Kinesis not encrypted with KMS
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Kinesis not encrypted with KMS
---

# Kinesis not encrypted with KMS

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `862fe4bf-3eec-4767-a517-40f378886b88`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/kinesis_stream)

### Description{% #description %}

AWS Kinesis Streams contain potentially sensitive data that should be encrypted at rest using AWS KMS to enhance security. When Kinesis streams are not encrypted with KMS, data stored in them is vulnerable to unauthorized access if the underlying storage is compromised. To properly secure Kinesis streams, both the `encryption_type` must be set to `KMS` and a valid `kms_key_id` must be specified, as shown in the following example:

```
resource "aws_kinesis_stream" "secure_example" {
  name             = "terraform-kinesis-test"
  // ... other configurations ...
  
  encryption_type = "KMS"
  kms_key_id = "alias/aws/kinesis"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_kinesis_stream" "negative1" {
  name             = "terraform-kinesis-test"
  shard_count      = 1
  retention_period = 48

  shard_level_metrics = [
    "IncomingBytes",
    "OutgoingBytes",
  ]

  tags = {
    Environment = "test"
  }


  encryption_type = "KMS"

  kms_key_id = "alias/aws/kinesis"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_kinesis_stream" "positive1" {
  name             = "terraform-kinesis-test"
  shard_count      = 1
  retention_period = 48

  shard_level_metrics = [
    "IncomingBytes",
    "OutgoingBytes",
  ]

  tags = {
    Environment = "test"
  }
}




resource "aws_kinesis_stream" "positive2" {
  name             = "terraform-kinesis-test"
  shard_count      = 1
  retention_period = 48

  shard_level_metrics = [
    "IncomingBytes",
    "OutgoingBytes",
  ]

  tags = {
    Environment = "test"
  }


  encryption_type = "NONE"
}





resource "aws_kinesis_stream" "positive3" {
  name             = "terraform-kinesis-test"
  shard_count      = 1
  retention_period = 48

  shard_level_metrics = [
    "IncomingBytes",
    "OutgoingBytes",
  ]

  tags = {
    Environment = "test"
  }


  encryption_type = "KMS"
}
```
