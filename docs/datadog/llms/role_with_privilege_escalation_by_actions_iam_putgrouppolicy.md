# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/role_with_privilege_escalation_by_actions_iam_putgrouppolicy.md

---
title: Role with privilege escalation by actions 'iam:PutGroupPolicy'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Role with privilege escalation by actions
  'iam:PutGroupPolicy'
---

# Role with privilege escalation by actions 'iam:PutGroupPolicy'

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `d6047119-a0b2-4b59-a4f2-127a36fb685b`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy#policy)

### Description{% #description %}

Granting the `iam:PutGroupPolicy` action with the `Resource` value set to `"*"` in an IAM policy, as shown below, allows the role to attach arbitrary permissions to any IAM group in the account:

```
policy = jsonencode({
  Version = "2012-10-17"
  Statement = [
    {
      Action = [
        "iam:PutGroupPolicy",
      ]
      Effect   = "Allow"
      Resource = "*"
    },
  ]
})
```

This powerful permission can be abused for privilege escalation, as a malicious user assuming this role could grant themselves or others elevated privileges by attaching highly permissive group policies. To mitigate this risk, limit the scope of the `Resource` attribute to only the intended groups and restrict allowed actions to only those necessary for the role's function.

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
          "iam:PutGroupPolicy",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}
```
