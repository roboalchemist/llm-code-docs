# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws_sam/serverless_function_environment_variables_not_encrypted.md

---
title: Serverless function environment variables not encrypted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Serverless function environment variables not
  encrypted
---

# Serverless function environment variables not encrypted

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `a7f8ac28-eed1-483d-87c8-4c325f022572`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html#sam-function-kmskeyarn)

### Description{% #description %}

Serverless functions that define environment variables must encrypt those variables with a customer-managed AWS KMS key to protect secrets and configuration data from exposure if the function configuration is accessed or leaked. For `AWS::Serverless::Function` resources that include `Properties.Environment.Variables`, the `Properties.KmsKeyArn` property must be defined and set to a valid KMS key ARN or alias (not `null`). Resources missing `KmsKeyArn` or where `KmsKeyArn` is `null` will be flagged. Example secure configuration referencing a KMS key:

```yaml
MyFunction:
  Type: AWS::Serverless::Function
  Properties:
    Runtime: nodejs14.x
    Handler: index.handler
    Environment:
      Variables:
        DB_PASSWORD: mypassword
    KmsKeyArn: !GetAtt MyKmsKey.Arn
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: AWS SAM template with a simple API definition
Resources:
  Function1:
    Type: AWS::Serverless::Function
    Properties:
      PackageType: Image
      ImageUri: account-id.dkr.ecr.region.amazonaws.com/ecr-repo-name:image-name
      ImageConfig:
        Command:
          - "app.lambda_handler"
        EntryPoint:
          - "entrypoint1"
        WorkingDirectory: "workDir"
      Tags:
        - Key: Type
          Value: AWS Serverless Function
      DeadLetterConfig:
        TargetArn: arn:aws:sqs:us-east-1:2324243535:aaa
        Type: SQS
      Environment:
        Variables:
          key: value
      KmsKeyArn: arn:aws:kms:us-west-1:123456789123:key/12345678-12cc-45bb-98aa-9876543210cc
      
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: AWS SAM template with a simple API definition
Resources:
  Function:
    Type: AWS::Serverless::Function
    Properties:
      PackageType: Image
      ImageUri: account-id.dkr.ecr.region.amazonaws.com/ecr-repo-name:image-name
      ImageConfig:
        Command:
          - "app.lambda_handler"
        EntryPoint:
          - "entrypoint1"
        WorkingDirectory: "workDir"
      Tags:
        - Key: Type
          Value: AWS Serverless Function
      DeadLetterConfig:
        TargetArn: arn:aws:sqs:us-east-1:2324243535:aaa
        Type: SQS
      Environment:
        Variables:
          key: value
      
```
