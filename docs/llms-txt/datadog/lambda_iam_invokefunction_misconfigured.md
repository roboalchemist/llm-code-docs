# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/lambda_iam_invokefunction_misconfigured.md

---
title: Lambda IAM InvokeFunction misconfigured
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Lambda IAM InvokeFunction misconfigured
---

# Lambda IAM InvokeFunction misconfigured

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `0ca1017d-3b80-423e-bb9c-6cd5898d34bd`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Low

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_permission)

### Description{% #description %}

AWS Lambda permissions must be carefully defined so that the `Action` field in the IAM policy explicitly specifies allowed actions, such as `"lambda:InvokeFunction"`. If the `Action` field is omitted or set too broadly, it could inadvertently grant unnecessary permissions, allowing unintended users or services to perform privileged operations on the Lambda function. This misconfiguration increases the risk of unauthorized invocation or modification of Lambda functions, potentially leading to security breaches or the execution of malicious code.

A secure Terraform configuration ensures the `Action` is correctly specified:

```
policy = jsonencode({
  Version = "2012-10-17"
  Statement = [
    {
      Action = [
        "lambda:InvokeFunction",
      ]
      Effect   = "Allow"
      Resource = [
        "arn:aws:lambda:*:*:function:example-function",
        "arn:aws:lambda:*:*:function:example-function:*"
      ]
    },
  ]
})
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_lambda_function" "negative3" {
  function_name = "negative3"
  role          = "negative3_role"
}

resource "aws_iam_policy" "negative3policy" {
  name        = "negative3policy"
  path        = "/"
  description = "negative3 Policy"

  # Terraform's "jsonencode" function converts a
  # Terraform expression result to valid JSON syntax.
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "s3:*",
        ]
        Effect   = "Allow"
        Resource = [
            aws_lambda_function.negative3.arn,
            "${aws_lambda_function.negative3.arn}:*"
        ]
      },
    ]
  })
}
```

```terraform
resource "aws_iam_policy" "negative2policy" {
  name        = "negative2policy"
  path        = "/"
  description = "negative2 Policy"

  # Terraform's "jsonencode" function converts a
  # Terraform expression result to valid JSON syntax.
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "s3:*",
        ]
        Effect   = "Allow"
        Resource = ["*"]
      },
    ]
  })
}
```

```terraform
resource "aws_iam_policy" "negative1policy" {
  name        = "negative1policy"
  path        = "/"
  description = "negative1 Policy"

  # Terraform's "jsonencode" function converts a
  # Terraform expression result to valid JSON syntax.
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "lambda:InvokeFunction",
        ]
        Effect   = "Allow"
        Resource = [
            "arn:aws:lambda:*:*:function:negative1",
            "arn:aws:lambda:*:*:function:negative1:*"
        ]
      },
    ]
  })
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_iam_policy" "positive6policy" {
  name        = "positive6policy"
  path        = "/"
  description = "positive6 Policy"

  # Terraform's "jsonencode" function converts a
  # Terraform expression result to valid JSON syntax.
  policy = jsonencode({
    Version = "2022-20-27"
    Statement = [
      {
        Action = [
          "lambda:*",
        ]
        Effect   = "Allow"
        Resource = [
            "arn:aws:lambda:*:*:function:*:*"
        ]
      },
    ]
  })
}
```

```terraform
resource "aws_iam_policy" "positive2policy" {
  name        = "positive2policy"
  path        = "/"
  description = "Positive2 Policy"

  # Terraform's "jsonencode" function converts a
  # Terraform expression result to valid JSON syntax.
  policy = jsonencode({
    Version = "2022-20-27"
    Statement = [
      {
        Action = [
          "lambda:InvokeFunction",
        ]
        Effect   = "Allow"
        Resource = [
            "arn:aws:lambda:*:*:function:positive2*:*"
        ]
      },
    ]
  })
}
```

```terraform
resource "aws_iam_policy" "positive3policy" {
  name        = "positive3policy"
  path        = "/"
  description = "positive3 Policy"

  # Terraform's "jsonencode" function converts a
  # Terraform expression result to valid JSON syntax.
  policy = jsonencode({
    Version = "2022-20-27"
    Statement = [
      {
        Action = [
          "lambda:InvokeFunction",
        ]
        Effect   = "Allow"
        Resource = [
            "arn:aws:lambda:*:*:function:*:*"
        ]
      },
    ]
  })
}
```
