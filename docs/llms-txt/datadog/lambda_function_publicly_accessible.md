# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/lambda_function_publicly_accessible.md

---
title: Lambda function publicly accessible
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Lambda function publicly accessible
---

# Lambda function publicly accessible

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `1btsf2f9-af8c-4dfc-a0f1-a03adb70deb2`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function)

### Description{% #description %}

AWS Lambda permissions with a principal value of `*` allow any AWS account or user to invoke the function, making it publicly accessible. This creates a significant security risk as unauthorized parties can trigger your Lambda function, potentially accessing sensitive data or consuming your AWS resources. To secure Lambda functions, specify the exact AWS account ARN in the `principal` field, as shown below, rather than using the wildcard `*`.

```
principal = "arn:aws:iam::123456789012:root"
```

The following is an example of an insecure configuration:

```
principal = "*"
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_lambda_permission" "restricted_lambda" {
  statement_id  = "AllowSpecificAccount"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.my_lambda.function_name
  principal     = "arn:aws:iam::123456789012:root"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_lambda_permission" "public_lambda" {
  statement_id  = "AllowPublicAccess"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.my_lambda.function_name
  principal     = "*"
}
```
