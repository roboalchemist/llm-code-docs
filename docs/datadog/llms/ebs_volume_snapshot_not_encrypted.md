# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/ebs_volume_snapshot_not_encrypted.md

---
title: EBS volume snapshot not encrypted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > EBS volume snapshot not encrypted
---

# EBS volume snapshot not encrypted

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `e6b4b943-6883-47a9-9739-7ada9568f8ca`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/ebs_snapshot#encrypted)

### Description{% #description %}

EBS volume snapshots should be encrypted to protect sensitive data at rest from unauthorized access. When an EBS volume is unencrypted, snapshots derived from it remain unencrypted as well, potentially exposing sensitive information if accessed by malicious actors. The security impact includes potential data breaches, compliance violations, and unauthorized data access even if the original volume is no longer in use.

To ensure proper encryption, create your EBS volumes with encryption enabled, as shown below:

```
resource "aws_ebs_volume" "secure_example" {
  availability_zone = "us-west-2a"
  size              = 40
  encrypted         = true

  tags = {
    Name = "HelloWorld"
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_ebs_volume" "negative1" {
  availability_zone = "us-west-2a"
  size              = 40
  encrypted         = true

  tags = {
    Name = "HelloWorld"
  }
}

resource "aws_ebs_snapshot" "negative1" {
  volume_id = aws_ebs_volume.negative1.id
  tags {
    Name = "Production"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_ebs_volume" "positive2" {
  availability_zone = "us-west-2a"
  size              = 40

  tags = {
    Name = "HelloWorld"
  }
}

resource "aws_ebs_snapshot" "positive2" {
  volume_id = aws_ebs_volume.positive2.id
  tags {
    Name = "Production"
  }
}
```

```terraform
resource "aws_ebs_volume" "positive1" {
  availability_zone = "us-west-2a"
  size              = 40
  encrypted         = false

  tags = {
    Name = "HelloWorld"
  }
}

resource "aws_ebs_snapshot" "positive1" {
  volume_id = aws_ebs_volume.positive1.id
  tags {
    Name = "Production"
  }
}
```
