# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/secretsmanager_secret_encrypted_with_aws_managed_key.md

---
title: Secrets Manager secret encrypted with AWS-managed key
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Secrets Manager secret encrypted with
  AWS-managed key
---

# Secrets Manager secret encrypted with AWS-managed key

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `b0d3ef3f-845d-4b1b-83d6-63a5a380375f`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/secretsmanager_secret#kms_key_id)

### Description{% #description %}

AWS Secrets Manager secrets should be encrypted with customer-managed KMS keys rather than the default AWS-managed keys. Relying on AWS managed keys limits an organization's ability to control, rotate, and audit encryption keys, which are important factors in enforcing robust security policies and compliance requirements. Without customer-managed KMS keys, there may be a greater risk of unauthorized access or insufficient key lifecycle management. If left unaddressed, sensitive information stored in Secrets Manager could be compromised due to weaker or less transparent key management practices.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_secretsmanager_secret" "test222" {
  name       = "test-cloudrail-1"
  kms_key_id = "alias/MyAlias"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
provider "aws" {
  region = "us-east-1"
}

data "aws_kms_key" "by_alias" {
  key_id = "alias/aws/secretsmanager"
}

resource "aws_secretsmanager_secret" "test" {
  name       = "test-cloudrail-1"
  kms_key_id = data.aws_kms_key.by_alias.arn
}
```

```terraform
resource "aws_secretsmanager_secret" "test2" {
  name       = "test-cloudrail-1"
  kms_key_id = "alias/aws/secretsmanager"
}
```
