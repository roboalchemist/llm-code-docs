# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/group_with_privilege_escalation_by_actions_iam_updateassumerolepolicy_and_sts_assumerole.md

---
title: >-
  Group with privilege escalation by actions 'iam:UpdateAssumeRolePolicy' and
  'sts:AssumeRole'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Group with privilege escalation by actions
  'iam:UpdateAssumeRolePolicy' and 'sts:AssumeRole'
---

# Group with privilege escalation by actions 'iam:UpdateAssumeRolePolicy' and 'sts:AssumeRole'

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `78f1ec6f-5659-41ea-bd48-d0a142dce4f2`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_group_policy#policy)

### Description{% #description %}

This check identifies IAM groups that have been granted both the `iam:UpdateAssumeRolePolicy` and `sts:AssumeRole` actions with a wildcard resource (`"Resource": "*"`) in their attached policies. Granting these permissions together allows any user in the group to escalate their privileges by altering assume role policies and then assuming any role, potentially gaining unauthorized access to sensitive resources. If left unaddressed, this misconfiguration could enable attackers or malicious insiders to escalate permissions, compromise account security, and move laterally throughout your AWS environment.

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
resource "aws_iam_group" "cosmic" {
  name = "cosmic"
}

resource "aws_iam_group_policy" "test_inline_policy" {
  name = "test_inline_policy"
  group = aws_iam_group.cosmic.name

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "iam:UpdateAssumeRolePolicy",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}


resource "aws_iam_policy_attachment" "test-attach" {
  name       = "test-attachment"
  groups     = [aws_iam_group.cosmic.name]
  policy_arn = aws_iam_policy.policy.arn
}


resource "aws_iam_policy" "policy" {
  name        = "test-policy"
  description = "A test policy"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "sts:AssumeRole",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}
```
