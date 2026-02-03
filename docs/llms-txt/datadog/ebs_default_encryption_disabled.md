# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/ebs_default_encryption_disabled.md

---
title: EBS default encryption disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > EBS default encryption disabled
---

# EBS default encryption disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `3d3f6270-546b-443c-adb4-bb6fb2187ca6`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ebs_encryption_by_default)

### Description{% #description %}

AWS Elastic Block Store (EBS) volumes should have encryption enabled by default to protect sensitive data at rest. When EBS encryption is disabled, data stored on these volumes remains in plaintext, potentially exposing confidential information if the physical storage is compromised or if the volume is improperly decommissioned. To enable default encryption, ensure that the `enabled` attribute in the `aws_ebs_encryption_by_default` resource is set to `true` or omitted (as it defaults to `true`). A secure configuration looks like the following:

```
resource "aws_ebs_encryption_by_default" "example" {
  enabled = true
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_ebs_encryption_by_default" "negative1" {
  enabled = true
}

resource "aws_ebs_encryption_by_default" "negative2" {
  
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_ebs_encryption_by_default" "positive1" {
  enabled = false
}
```
