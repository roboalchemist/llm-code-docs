# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/role_with_privilege_escalation_by_actions_iam_putrolepolicy.md

---
title: Role with privilege escalation by actions 'iam:PutRolePolicy'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Role with privilege escalation by actions
  'iam:PutRolePolicy'
---

# Role with privilege escalation by actions 'iam:PutRolePolicy'

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `eb64f1e9-f67d-4e35-8a3c-3d6a2f9efea7`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy#policy)

### Description{% #description %}

Granting a role the `iam:PutRolePolicy` action with the `Resource` set to `"*"` in Terraform, as in the following configuration, allows any principal with this role to attach arbitrary permissions to any IAM role, leading to potential privilege escalation. An attacker could exploit this to grant themselves or others broad or administrative permissions, compromising the security of the AWS environment. It is critical to scope IAM permissions as narrowly as possible, restricting both actions and resources to mitigate this risk.

```
policy = jsonencode({
  Version = "2012-10-17"
  Statement = [
    {
      Action = [
        "iam:PutRolePolicy",
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
          "iam:PutRolePolicy",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}
```
