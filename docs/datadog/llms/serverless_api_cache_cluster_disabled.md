# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws_sam/serverless_api_cache_cluster_disabled.md

---
title: Serverless API cache cluster disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Serverless API cache cluster disabled
---

# Serverless API cache cluster disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `60a05ede-0a68-4d0d-a58f-f538cf55ff79`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Low

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-api.html#sam-api-cacheclusterenabled)

### Description{% #description %}

Amazon API Gateway caching should be enabled for Serverless APIs to reduce backend load and lower latency, helping prevent request amplification that can degrade performance or cause service outages. The `CacheClusterEnabled` property on `AWS::Serverless::Api` resources must be defined and set to `true`. Resources where `CacheClusterEnabled` is missing, `null`, or set to `false` will be flagged. Also consider configuring `CacheClusterSize` to provision adequate cache capacity for your expected traffic.

Secure configuration example:

```yaml
MyApi:
  Type: AWS::Serverless::Api
  Properties:
    StageName: Prod
    CacheClusterEnabled: true
```

## Compliant Code Examples{% #compliant-code-examples %}

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
      CacheClusterEnabled: false
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
```
