# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/ssm_session_transit_encryption_disabled.md

---
title: SSM session transit encryption disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > SSM session transit encryption disabled
---

# SSM session transit encryption disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `ce60cc6b-6831-4bd7-84a2-cc7f8ee71433`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ssm_document#content)

### Description{% #description %}

When creating an `aws_ssm_document` of type `Session`, session data should be encrypted in transit to protect sensitive information from interception or exposure. By omitting critical encryption-related attributes such as `"s3EncryptionEnabled": true`, `"cloudWatchEncryptionEnabled": true`, and specifying a KMS key with `"kmsKeyId"`, unencrypted data could be transferred between AWS resources and users, increasing the risk of unauthorized access or data leakage. Ensuring encryption for SSM Session Manager sessions mitigates these risks by enforcing secure data transport and proper visibility restrictions.

A secure Terraform configuration looks like the following:

```hcl
resource "aws_ssm_document" "secure_session" {
  name          = "secure_session_document"
  document_type = "Session"

  content = <<DOC
  {
    "schemaVersion": "1.2",
    "description": "Secure SSM session with encrypted data transfer.",
    "inputs": {
      "s3EncryptionEnabled": true,
      "cloudWatchEncryptionEnabled": true,
      "cloudWatchStreamingEnabled": true,
      "runAsEnabled": false,
      "kmsKeyId": "${var.kms_key_id}"
    }
  }
DOC
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_ssm_document" "negative" {
  name          = "test_document"
  document_type = "Session"

  content = <<DOC
  {
    "schemaVersion": "1.2",
    "description": "Check ip configuration of a Linux instance.",
    "inputs": {
      "s3EncryptionEnabled": true,
      "cloudWatchEncryptionEnabled": true,
      "cloudWatchStreamingEnabled": true,
      "runAsEnabled": false,
      "kmsKeyId": "${var.kms_key_id}"
    }
  }
DOC
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_ssm_document" "positive2" {
  name          = "test_document"
  document_type = "Session"

  content = <<DOC
  {
    "schemaVersion": "1.2",
    "description": "Check ip configuration of a Linux instance.",
    "inputs": {
      "s3EncryptionEnabled": true,
      "cloudWatchEncryptionEnabled": true,
      "cloudWatchStreamingEnabled": true,
      "runAsEnabled": false
    }
  }
DOC
}
```

```terraform
resource "aws_ssm_document" "positive1" {
  name          = "test_document"
  document_type = "Session"

  content = <<DOC
  {
    "schemaVersion": "1.2",
    "description": "Check ip configuration of a Linux instance."
  }
DOC
}
```
