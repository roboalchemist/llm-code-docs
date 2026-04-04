# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/public_lambda_via_api_gateway.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/public_lambda_via_api_gateway.md

---
title: Public Lambda function via API Gateway
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Public Lambda function via API Gateway
---

# Public Lambda function via API Gateway

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `57b12981-3816-4c31-b190-a1e614361dd2`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html)

### Description{% #description %}

Lambda permissions that grant API Gateway or the public principal access with a `SourceArn` ending in `/*/*` allow any API stage and method to invoke the function. This enables broad or unintended public invocation and can result in unauthorized executions, data exposure, and increased resource consumption.

In AWS CloudFormation, check `AWS::Lambda::Permission` resources where `Action` is `lambda:InvokeFunction` or `lambda:*` and `Principal` is `apigateway.amazonaws.com` or `*`. The `SourceArn` must not equal `/*/*` or end with `/*/*`. Resources missing `SourceArn` or containing a trailing `/*/*` will be flagged. Set `SourceArn` to a specific execute-api ARN that includes the API ID, stage, and method to limit invocation scope.

Secure configuration example:

```yaml
MyLambdaPermission:
  Type: AWS::Lambda::Permission
  Properties:
    FunctionName: !Ref MyFunction
    Action: "lambda:InvokeFunction"
    Principal: "apigateway.amazonaws.com"
    SourceArn: "arn:aws:execute-api:us-east-1:123456789012:api-id/prod/GET/myresource"
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "BatchJobDefinition"
Resources:
  s3Permission3:
    Type: AWS::Lambda::Permission
    Properties:
      FunctionName: !GetAtt function.Arn
      Action: lambda:InvokeFunction
      Principal: s3.amazonaws.com
      SourceAccount: !Ref 'AWS::AccountId'
      SourceArn: arn:aws:s3:eu-central-1:123456789012:bucketname
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "s3Permission": {
      "Type": "AWS::Lambda::Permission",
      "Properties": {
        "FunctionName": {
          "Fn::GetAtt": [
            "function",
            "Arn"
          ]
        },
        "Action": "lambda:InvokeFunction",
        "Principal": "s3.amazonaws.com",
        "SourceAccount": {
          "Ref": "AWS::AccountId"
        },
        "SourceArn": "arn:aws:s3:eu-central-1:123456789012:bucketname"
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "s3Permission": {
      "Type": "AWS::Lambda::Permission",
      "Properties": {
        "FunctionName": {
          "Fn::GetAtt": [
            "function",
            "Arn"
          ]
        },
        "Action": "lambda:InvokeFunction",
        "Principal": "apigateway.amazonaws.com",
        "SourceAccount": {
          "Ref": "AWS::AccountId"
        },
        "SourceArn": "arn:aws:s3:eu-central-1:123456789012/*/*"
      }
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "BatchJobDefinition"
Resources:
  s3Permission3:
    Type: AWS::Lambda::Permission
    Properties:
      FunctionName: !GetAtt function.Arn
      Action: lambda:InvokeFunction
      Principal: apigateway.amazonaws.com
      SourceAccount: !Ref 'AWS::AccountId'
      SourceArn: arn:aws:s3:eu-central-1:123456789012/*/*
```
