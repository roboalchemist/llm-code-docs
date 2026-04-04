# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/role_with_privilege_escalation_by_actions_iam_putuserpolicy.md

---
title: Role with privilege escalation by actions 'iam:PutUserPolicy'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Role with privilege escalation by actions
  'iam:PutUserPolicy'
---

# Role with privilege escalation by actions 'iam:PutUserPolicy'

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `8f75840d-9ee7-42f3-b203-b40e3979eb12`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy#policy)

### Description{% #description %}

Allowing the `iam:PutUserPolicy` action with a `Resource` value of `"*"` in a Terraform AWS IAM role or policy configuration allows any user assigned the role to attach arbitrary policies to any users in the AWS account. This creates a significant privilege escalation vulnerability, as an attacker could grant themselves or others increased permissions, potentially leading to full administrative access. To mitigate this risk, the scope of the `PutUserPolicy` action should be strictly restricted to only the necessary resources and users.

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
          "iam:PutUserPolicy",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}
```
