# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws_sam/serverless_function_without_tags.md

---
title: Serverless function without tags
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Serverless function without tags
---

# Serverless function without tags

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `a71ecabe-03b6-456a-b3bc-d1a39aa20c98`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Low

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html#sam-function-tags)

### Description{% #description %}

AWS Serverless Application Model (AWS SAM) functions should include tags to support asset inventory and incident response. Check `AWS::Serverless::Function` resources and ensure the `Properties.Tags` map is defined and not `null`. Resources missing the `Tags` property or with `Tags: null` will be flagged.

Secure configuration example:

```yaml
MyFunction:
  Type: AWS::Serverless::Function
  Properties:
    Handler: index.handler
    Runtime: nodejs14.x
    Tags:
      Environment: production
      Owner: devops
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
```
