# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/group_with_privilege_escalation_by_actions_glue_updatedevendpoint.md

---
title: Group with privilege escalation by actions 'glue:UpdateDevEndpoint'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Group with privilege escalation by actions
  'glue:UpdateDevEndpoint'
---

# Group with privilege escalation by actions 'glue:UpdateDevEndpoint'

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `8f3c16b3-354d-45db-8ad5-5066778a9485`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_group_policy#policy)

### Description{% #description %}

This check identifies IAM group policies that grant the `glue:UpdateDevEndpoint` action with the resource set to `"*"`, as shown in the following insecure example:

```
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
```

Allowing unrestricted access to `glue:UpdateDevEndpoint` enables users in the group to potentially attach arbitrary IAM roles to a Glue development endpoint, which can be leveraged for privilege escalation. If left unaddressed, attackers with this permission may exploit it to gain elevated permissions or access sensitive resources by executing malicious code or gaining unauthorized access to other AWS services. This misconfiguration can result in significant security risks, including compromise of AWS account resources and loss of sensitive information.

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
          "glue:UpdateDevEndpoint",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}
```
