# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/glue_security_configuration_encryption_disabled.md

---
title: Glue security configuration encryption disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Glue security configuration encryption
  disabled
---

# Glue security configuration encryption disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `ad5b4e97-2850-4adf-be17-1d293e0b85ee`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/glue_security_configuration#encryption_configuration)

### Description{% #description %}

AWS Glue Security Configuration requires proper encryption settings for all three components (CloudWatch, job bookmarks, and S3) with valid KMS key ARNs to ensure comprehensive data protection. When any of these components lacks proper encryption configuration or is missing the required KMS key ARN, it creates security vulnerabilities that could expose sensitive data. The impact of this misconfiguration includes potential unauthorized access to data, compliance violations, and increased risk of data breaches.

Secure configuration example:

```terraform
encryption_configuration {
  cloudwatch_encryption {
    cloudwatch_encryption_mode = "SSE-KMS"
    kms_key_arn = data.aws_kms_key.example.arn
  }
  job_bookmarks_encryption {
    job_bookmarks_encryption_mode = "CSE-KMS"
    kms_key_arn = data.aws_kms_key.example.arn
  }
  s3_encryption {
    s3_encryption_mode = "SSE-KMS"
    kms_key_arn = data.aws_kms_key.example.arn
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_glue_security_configuration" "negative1" {
  name = "example"

  encryption_configuration {
    cloudwatch_encryption {
      cloudwatch_encryption_mode = "SSE-KMS"
      kms_key_arn = data.aws_kms_key.example.arn
    }

    job_bookmarks_encryption {
      job_bookmarks_encryption_mode = "CSE-KMS"
      kms_key_arn = data.aws_kms_key.example.arn
    }

    s3_encryption {
      kms_key_arn        = data.aws_kms_key.example.arn
      s3_encryption_mode = "SSE-KMS"
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_glue_security_configuration" "positive2" {
  name = "example"

  encryption_configuration {
    cloudwatch_encryption {
      cloudwatch_encryption_mode = "SSE-KMS"
      kms_key_arn = data.aws_kms_key.example.arn
    }

    job_bookmarks_encryption {
      job_bookmarks_encryption_mode = "DISABLED"
      kms_key_arn = data.aws_kms_key.example.arn
    }

    s3_encryption {
      kms_key_arn        = data.aws_kms_key.example.arn
      s3_encryption_mode = "SSE-KMS"
    }
  }
}
```

```terraform
resource "aws_glue_security_configuration" "positive2" {
  name = "example"

  encryption_configuration {
    cloudwatch_encryption {
      cloudwatch_encryption_mode = "SSE-KMS"
      kms_key_arn = data.aws_kms_key.example.arn
    }

    job_bookmarks_encryption {
      kms_key_arn = data.aws_kms_key.example.arn
    }

    s3_encryption {
      kms_key_arn        = data.aws_kms_key.example.arn
      s3_encryption_mode = "SSE-KMS"
    }
  }
}
```

```terraform
resource "aws_glue_security_configuration" "positive1" {
  name = "example"

  encryption_configuration {
    cloudwatch_encryption {
      cloudwatch_encryption_mode = "SSE-KMS"
    }

    job_bookmarks_encryption {
      job_bookmarks_encryption_mode = "CSE-KMS"
      kms_key_arn = data.aws_kms_key.example.arn
    }

    s3_encryption {
      kms_key_arn        = data.aws_kms_key.example.arn
      s3_encryption_mode = "SSE-KMS"
    }
  }
}
```
