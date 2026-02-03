# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/user_with_privilege_escalation_by_actions_iam_createaccesskey.md

---
title: User with privilege escalation by actions 'iam:CreateAccessKey'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > User with privilege escalation by actions
  'iam:CreateAccessKey'
---

# User with privilege escalation by actions 'iam:CreateAccessKey'

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `113208f2-a886-4526-9ecc-f3218600e12c`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_user_policy#policy)

### Description{% #description %}

Granting a user the `iam:CreateAccessKey` action with a resource set to `"*"` allows that user to create access keys for any IAM user in the AWS account. This over-privileged configuration, as shown below, introduces a privilege escalation risk, as the user could generate access keys for higher-privileged users and gain unauthorized access to sensitive resources:

```
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
```

To mitigate this risk, limit the action and resource to the specific user needing access, or scope the permissions more narrowly to avoid unauthorized key creation.

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
resource "aws_iam_user" "cosmic" {
  name = "cosmic"
}

resource "aws_iam_user_policy" "test_inline_policy" {
  name = "test_inline_policy"
  user = aws_iam_user.cosmic.name

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


resource "aws_iam_policy_attachment" "test-attach" {
  name       = "test-attachment"
  users      = [aws_iam_user.cosmic.name]
  roles      = [aws_iam_role.role.name]
  groups     = [aws_iam_group.group.name]
}
```
