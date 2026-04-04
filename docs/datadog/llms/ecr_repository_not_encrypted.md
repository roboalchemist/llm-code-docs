# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/ecr_repository_not_encrypted.md

---
title: ECR repository not encrypted with CMK
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > ECR repository not encrypted with CMK
---

# ECR repository not encrypted with CMK

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `0e32d561-4b5a-4664-a6e3-a3fa85649157`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Low

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecr_repository#encryption_configuration)

### Description{% #description %}

Amazon Elastic Container Registry (ECR) repositories should use customer-managed AWS KMS keys for encryption to ensure stronger access control, auditing, and compliance with organizational security requirements. By default, ECR repositories may only use AES256 encryption or omit the `encryption_configuration` block, which limits key management capabilities and centralized control over key lifecycle and access policies. A secure Terraform configuration example specifies a KMS key:

```
encryption_configuration {
  encryption_type = "KMS"
  kms_key = "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
}
```

Without this, sensitive container images may be at greater risk of unauthorized access or inability to meet regulatory requirements for key rotation and audit.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_ecr_repository" "foo2" {
  name                 = "bar"
  image_tag_mutability = "IMMUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  encryption_configuration {
    encryption_type = "KMS"
    kms_key = "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_ecr_repository" "foo" {
  name                 = "bar"
  image_tag_mutability = "IMMUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}

resource "aws_ecr_repository" "fooX" {
  name                 = "barX"
  image_tag_mutability = "IMMUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  encryption_configuration {
    encryption_type = "AES256"
  }
}
```
