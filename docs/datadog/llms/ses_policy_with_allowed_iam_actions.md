# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/ses_policy_with_allowed_iam_actions.md

---
title: SES policy with allowed IAM actions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > SES policy with allowed IAM actions
---

# SES policy with allowed IAM actions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `34b921bd-90a0-402e-a0a5-dc73371fd963`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ses_identity_policy#policy)

### Description{% #description %}

Amazon SES identity policies that allow access to all principals ('AWS': '*') create a significant security risk by granting any AWS account permissions to perform the specified actions on your SES resources. This overly permissive configuration can lead to unauthorized email sending, potential data breaches, and could be exploited for phishing campaigns or reputation damage.

Instead, SES policies should explicitly specify the ARNs of trusted principals that require access. For example, replace `"AWS": "*"` with `"AWS": "arn:aws:iam::ACCOUNT_ID:root"` or a more specific IAM role or user to implement the principle of least privilege.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_ses_identity_policy" "negative1" {
  identity = aws_ses_domain_identity.example.arn
  name     = "example"
  policy   = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "*",
      "Principal": {
        "AWS": "arn:aws:iam::987654321145:root"
      },
      "Effect": "Allow",
      "Resource": "*",
      "Sid": ""
    }
  ]
}
EOF
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_ses_identity_policy" "positive1" {
  identity = aws_ses_domain_identity.example.arn
  name     = "example"
  policy   = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "*",
      "Principal": {
        "AWS": "*"
      },
      "Effect": "Allow",
      "Resource": "*",
      "Sid": ""
    }
  ]
}
EOF
}
```
