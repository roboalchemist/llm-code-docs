# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/sns_topic_not_encrypted.md

---
title: SNS topic not encrypted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > SNS topic not encrypted
---

# SNS topic not encrypted

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `28545147-2fc6-42d5-a1f9-cf226658e591`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/sns_topic#kms_master_key_id)

### Description{% #description %}

Amazon SNS topics should be encrypted at rest using AWS KMS to protect sensitive message content. Without encryption, data stored in SNS topics is vulnerable to unauthorized access if the service or underlying storage is compromised. Use the `kms_master_key_id` attribute to specify a KMS key for encryption, as shown in this example: `kms_master_key_id = "alias/MyAlias"`. Leaving this attribute empty or unspecified (as in `kms_master_key_id = ""`) results in unencrypted SNS topics, exposing sensitive data to potential security breaches.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
provider "aws2" {
  region = "us-east-1"
}

resource "aws_sns_topic" "test2" {
  name              = "sns_ecnrypted"
  kms_master_key_id = "alias/MyAlias"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
provider "aws" {
  region = "us-east-1"
}

resource "aws_sns_topic" "test" {
  name = "sns_not_ecnrypted"
}
```

```terraform
resource "aws_sns_topic" "user_updates" {
  name              = "user-updates-topic"
  kms_master_key_id = ""
}
```
