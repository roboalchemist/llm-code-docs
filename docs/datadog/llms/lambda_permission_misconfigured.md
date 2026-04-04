# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/lambda_permission_misconfigured.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/lambda_permission_misconfigured.md

---
title: Lambda permission misconfigured
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Lambda permission misconfigured
---

# Lambda permission misconfigured

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `9b83114b-b2a1-4534-990d-06da015e47aa`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Low

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/pt_br/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html)

### Description{% #description %}

Lambda permissions must explicitly allow only the invocation action to enforce least privilege and prevent unintended access to other function operations or configuration. In AWS CloudFormation, the `Action` property in `AWS::Lambda::Permission` resources must be set exactly to `lambda:InvokeFunction`. Resources missing `Action` or with any other value will be flagged as a security risk.

Secure CloudFormation example:

```yaml
MyFunctionPermission:
  Type: AWS::Lambda::Permission
  Properties:
    FunctionName: !GetAtt MyFunction.Arn
    Action: lambda:InvokeFunction
    Principal: sns.amazonaws.com
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
Resources:
  s3Permission:
    Type: AWS::Lambda::Permission
    Properties:
      FunctionName: !GetAtt function.Arn
      Action: lambda:InvokeFunction
      Principal: s3.amazonaws.com
      SourceAccount: !Ref 'AWS::AccountId'
      SourceArn: !GetAtt bucket.Arn
```

```json
{
  "Resources": {
    "s3Permission": {
      "Type": "AWS::Lambda::Permission",
      "Properties": {
        "FunctionName": "function.Arn",
        "Action": "lambda:InvokeFunction",
        "Principal": "s3.amazonaws.com",
        "SourceAccount": "AWS::AccountId",
        "SourceArn": "bucket.Arn"
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "Resources": {
    "s3Permission": {
      "Type": "AWS::Lambda::Permission",
      "Properties": {
        "SourceArn": "bucket.Arn",
        "FunctionName": "function.Arn",
        "Action": "lambda:GetFunction",
        "Principal": "s3.amazonaws.com",
        "SourceAccount": "AWS::AccountId"
      }
    }
  }
}
```

```yaml
Resources:
  s3Permission:
    Type: AWS::Lambda::Permission
    Properties:
      FunctionName: !GetAtt function.Arn
      Action: lambda:GetFunction
      Principal: s3.amazonaws.com
      SourceAccount: !Ref 'AWS::AccountId'
      SourceArn: !GetAtt bucket.Arn
```
