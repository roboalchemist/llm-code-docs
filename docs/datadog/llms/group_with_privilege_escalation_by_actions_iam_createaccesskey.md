# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/group_with_privilege_escalation_by_actions_iam_createaccesskey.md

---
title: Group with privilege escalation by actions 'iam:CreateAccessKey'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Group with privilege escalation by actions
  'iam:CreateAccessKey'
---

# Group with privilege escalation by actions 'iam:CreateAccessKey'

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `846646e3-2af1-428c-ac5d-271eccfa6faf`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_group_policy#policy)

### Description{% #description %}

This check identifies IAM group policies that grant the `iam:CreateAccessKey` permission with the resource set to `"*"`, which allows users in the group to create access keys for any IAM user in the AWS account. This represents a serious privilege escalation vulnerability because any member of the group could create access keys for higher-privilege users and gain unauthorized access to sensitive resources. If left unaddressed, attackers or malicious insiders could leverage this permission to take control of other users' accounts, compromise the environment, or bypass existing security controls. Restricting `iam:CreateAccessKey` to only necessary users and scoping its resource access is critical to reducing the risk of privilege escalation.

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
          "iam:CreateAccessKey",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}
```
