# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/group_with_privilege_escalation_by_actions_iam_addusertogroup.md

---
title: Group with privilege escalation by actions 'iam:AddUserToGroup'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Group with privilege escalation by actions
  'iam:AddUserToGroup'
---

# Group with privilege escalation by actions 'iam:AddUserToGroup'

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `970ed7a2-0aca-4425-acf1-0453c9ecbca1`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_group_policy#policy)

### Description{% #description %}

Granting the `iam:AddUserToGroup` action with the `Resource` attribute set to `*` in an AWS IAM policy allows any user to add themselves or any other user to any IAM group within the AWS account. This wide permission can enable unauthorized privilege escalation, as users could gain access to groups with higher-level privileges, potentially bypassing intended access controls. If left unaddressed, attackers or compromised users may escalate their privileges and gain broader access to sensitive resources, severely impacting the security of the environment. To mitigate this risk, restrict the `Resource` field to specific group ARNs and ensure only trusted users have the ability to manage IAM group memberships.

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
          "iam:AddUserToGroup",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}
```
