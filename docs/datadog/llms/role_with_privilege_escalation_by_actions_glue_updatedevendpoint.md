# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/role_with_privilege_escalation_by_actions_glue_updatedevendpoint.md

---
title: Role with privilege escalation by actions 'glue:UpdateDevEndpoint'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Role with privilege escalation by actions
  'glue:UpdateDevEndpoint'
---

# Role with privilege escalation by actions 'glue:UpdateDevEndpoint'

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `eda48c88-2b7d-4e34-b6ca-04c0194aee17`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy#policy)

### Description{% #description %}

Granting the `glue:UpdateDevEndpoint` permission with the `Resource` set to `"*"` in an AWS IAM role introduces a privilege escalation risk. The `glue:UpdateDevEndpoint` action allows modification of existing AWS Glue DevEndpoints, including the ability to attach arbitrary IAM roles to these endpoints. An attacker with this permission could attach a role with higher privileges to a DevEndpoint and then use that role's credentials to perform unauthorized actions, bypassing intended security boundaries. If not addressed, this can lead to full account compromise or access to sensitive information by escalating the attacker's privileges within the AWS environment.

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
          "glue:UpdateDevEndpoint",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}
```
