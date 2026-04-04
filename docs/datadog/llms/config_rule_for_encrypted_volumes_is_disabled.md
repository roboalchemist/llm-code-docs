# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/config_rule_for_encrypted_volumes_is_disabled.md

---
title: Config rule for encrypted volumes disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Config rule for encrypted volumes disabled
---

# Config rule for encrypted volumes disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `abdb29d4-5ca1-4e91-800b-b3569bbd788c`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/config_config_rule)

### Description{% #description %}

This check verifies if AWS Config rules include the `ENCRYPTED_VOLUMES` source identifier, which monitors whether EBS volumes that are attached to EC2 instances are encrypted. Without this rule in place, organizations may unknowingly deploy unencrypted EBS volumes, potentially exposing sensitive data to unauthorized access in case of data breaches or improper access controls.

To address this vulnerability, ensure at least one AWS Config rule uses `ENCRYPTED_VOLUMES` as the source identifier, as shown below:

```terraform
resource "aws_config_config_rule" "encrypted_volumes" {
  name = "encrypted_vols_rule"

  source {
    owner             = "AWS"
    source_identifier = "ENCRYPTED_VOLUMES"
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_config_config_rule" "negative1" {
  name = "encrypted_vols_rule"

  source {
    owner             = "AWS"
    source_identifier = "ENCRYPTED_VOLUMES"
  }
}

resource "aws_config_config_rule" "negative2" {
  name = "another_rule"

  source {
    owner             = "AWS"
    source_identifier = "IAM_PASSWORD_POLICY"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_config_config_rule" "positive1" {
  name = "some_rule"

  source {
    owner             = "AWS"
    source_identifier = "IAM_PASSWORD_POLICY"
  }
}

resource "aws_config_config_rule" "positive2" {
  name = "another_rule"

  source {
    owner             = "AWS"
    source_identifier = "IAM_PASSWORD_POLICY"
  }
}
```
