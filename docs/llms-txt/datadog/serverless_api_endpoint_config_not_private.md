# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws_sam/serverless_api_endpoint_config_not_private.md

---
title: Serverless API endpoint config not private
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Serverless API endpoint config not private
---

# Serverless API endpoint config not private

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `6b5b0313-771b-4319-ad7a-122ee78700ef`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-api.html#sam-api-endpointconfiguration)

### Description{% #description %}

Serverless APIs should use a `PRIVATE` endpoint to avoid exposure to the public internet, since public endpoints can allow unauthenticated access and unintended invocation of backend services, leading to data exposure or service abuse. For `AWS::Serverless::Api` resources, the `Properties.EndpointConfiguration.Types` array must be defined and include the value `PRIVATE`. Resources missing `EndpointConfiguration`, missing `Types`, or where `Types` does not contain `PRIVATE` will be flagged.

Secure configuration example:

```yaml
MyApi:
  Type: AWS::Serverless::Api
  Properties:
    StageName: prod
    EndpointConfiguration:
      Types:
        - PRIVATE
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: AWS SAM template with a simple API definition
Resources:
  ApiGatewayApi4:
    Type: AWS::Serverless::Api
    Properties:
      StageName: prod
      TracingEnabled: true
      CacheClusterEnabled: true
      EndpointConfiguration:
        Types:
          - PRIVATE
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: AWS SAM template with a simple API definition
Resources:
  ApiGatewayApi2:
    Type: AWS::Serverless::Api
    Properties:
      StageName: prod
      TracingEnabled: true
      CacheClusterEnabled: true
      EndpointConfiguration:
        VpcEndpointIds:
          - !Ref ApiGatewayVPCEndpoint
```

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: AWS SAM template with a simple API definition
Resources:
  ApiGatewayApi3:
    Type: AWS::Serverless::Api
    Properties:
      StageName: prod
      TracingEnabled: true
      CacheClusterEnabled: true
      EndpointConfiguration:
        Types:
          - EDGE
```

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: AWS SAM template with a simple API definition
Resources:
  ApiGatewayApi:
    Type: AWS::Serverless::Api
    Properties:
      StageName: prod
      TracingEnabled: true
      CacheClusterEnabled: true
```
