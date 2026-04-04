# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/role_with_privilege_escalation_by_actions_iam_attachuserpolicy.md

---
title: Role with privilege escalation by actions 'iam:AttachUserPolicy'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Role with privilege escalation by actions
  'iam:AttachUserPolicy'
---

# Role with privilege escalation by actions 'iam:AttachUserPolicy'

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `7c96920c-6fd0-449d-9a52-0aa431b6beaf`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy#policy)

### Description{% #description %}

Allowing an IAM role the action `iam:AttachUserPolicy` with a wildcard resource (`Resource = "*"`) grants broad privileges, enabling the role to attach any managed policy to any user in the AWS account. This constitutes a significant privilege escalation risk, as it allows users or roles with this permission to grant themselves or others additional permissions, potentially escalating to administrative access. To mitigate this risk, restrict the `Resource` attribute to specific ARNs and only grant necessary actions, as in the following secure example:

```
resource "aws_iam_user" "cosmic2" {
  name = "cosmic2"
}

resource "aws_iam_user_policy" "inline_policy_run_instances2" {
  name = "inline_policy_run_instances"
  user = aws_iam_user.cosmic2.name

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "ec2:Describe*",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_iam_user" "cosmic2" {
  name = "cosmic2"
}

resource "aws_iam_user_policy" "inline_policy_run_instances2" {
  name = "inline_policy_run_instances"
  user = aws_iam_user.cosmic2.name

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "ec2:Describe*",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_iam_role" "cosmic" {
  name = "cosmic"
}

resource "aws_iam_role_policy" "test_inline_policy" {
  name = "test_inline_policy"
  role = aws_iam_role.cosmic.name

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "iam:AttachUserPolicy",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}
```
