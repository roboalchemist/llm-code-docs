# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/user_with_privilege_escalation_by_actions_iam_putgrouppolicy.md

---
title: User with privilege escalation by actions 'iam:PutGroupPolicy'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > User with privilege escalation by actions
  'iam:PutGroupPolicy'
---

# User with privilege escalation by actions 'iam:PutGroupPolicy'

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `8bfbf7ab-d5e8-4100-8618-798956e101e0`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_user_policy#policy)

### Description{% #description %}

Granting an IAM user the `iam:PutGroupPolicy` action with `"Resource": "*"` allows them to attach arbitrary inline policies to any IAM group in the AWS account, leading to potential privilege escalation. With this permission, a user could assign powerful or administrative permissions to groups they belong to, effectively bypassing intended security boundaries. To prevent this, it's important to restrict IAM user actions to the minimum necessary and avoid using wildcards in sensitive permissions, as shown below:

```
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
          "iam:PutGroupPolicy",
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
