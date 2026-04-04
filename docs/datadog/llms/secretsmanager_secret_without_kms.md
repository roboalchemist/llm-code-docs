# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/secretsmanager_secret_without_kms.md

---
title: Secrets Manager secret without KMS
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Secrets Manager secret without KMS
---

# Secrets Manager secret without KMS

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `a2f548f2-188c-4fff-b172-e9a6acb216bd`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/secretsmanager_secret#kms_key_id)

### Description{% #description %}

By default, AWS Secrets Manager encrypts secrets using the default AWS-managed key, which may not provide the desired level of control over key rotation, access policies, or auditability. Without explicitly specifying a `kms_key_id` in your Terraform resource, as shown below, secrets will not use a customer-managed AWS KMS key (CMK) for encryption:

```
resource "aws_secretsmanager_secret" "example" {
  name = "example"
}
```

This misconfiguration can increase the exposure of sensitive data and limit your ability to implement strict access controls. To reduce risk, explicitly provide a `kms_key_id` attribute referencing a CMK:

```
resource "aws_secretsmanager_secret" "example" {
  name       = "example"
  kms_key_id = "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_secretsmanager_secret" "example" {
  name = "example"
  kms_key_id = "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_secretsmanager_secret" "example" {
  name = "example"
}
```
