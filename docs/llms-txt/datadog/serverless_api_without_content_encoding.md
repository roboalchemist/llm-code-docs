# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws_sam/serverless_api_without_content_encoding.md

---
title: Serverless API without content encoding
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Serverless API without content encoding
---

# Serverless API without content encoding

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `a2f2800e-614b-4bc8-89e6-fec8afd24800`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Low

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-api.html#sam-api-minimumcompressionsize)

### Description{% #description %}

Serverless APIs should enable response compression by configuring `MinimumCompressionSize` to reduce response sizes, lower bandwidth costs, and limit the risk of backend resource exhaustion from large uncompressed payloads. The `MinimumCompressionSize` property on `AWS::Serverless::Api` resources must be defined as an integer between `0` and `10485759` (that is, greater than `-1` and less than `10485760`). Resources missing this property or with values less than `0` or greater than `10485759` will be flagged. A typical secure configuration sets a threshold in bytes (for example, `1024`) to compress responses larger than that size:

```yaml
MyApi:
  Type: AWS::Serverless::Api
  Properties:
    StageName: prod
    MinimumCompressionSize: 1024
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
      AccessLogSetting:
        DestinationArn: 'arn:aws:logs:us-east-1:123456789:log-group:my-log-group'
        Format: >-
          {"requestId":"$context.requestId", "ip": "$context.identity.sourceIp",
          "caller":"$context.identity.caller",
          "user":"$context.identity.user","requestTime":"$context.requestTime",
          "eventType":"$context.eventType","routeKey":"$context.routeKey",
          "status":"$context.status","connectionId":"$context.connectionId"}
      MinimumCompressionSize: 114
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
      AccessLogSetting:
        DestinationArn: 'arn:aws:logs:us-east-1:123456789:log-group:my-log-group'
        Format: >-
          {"requestId":"$context.requestId", "ip": "$context.identity.sourceIp",
          "caller":"$context.identity.caller",
          "user":"$context.identity.user","requestTime":"$context.requestTime",
          "eventType":"$context.eventType","routeKey":"$context.routeKey",
          "status":"$context.status","connectionId":"$context.connectionId"}
      MinimumCompressionSize: -1
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
      AccessLogSetting:
        DestinationArn: 'arn:aws:logs:us-east-1:123456789:log-group:my-log-group'
        Format: >-
          {"requestId":"$context.requestId", "ip": "$context.identity.sourceIp",
          "caller":"$context.identity.caller",
          "user":"$context.identity.user","requestTime":"$context.requestTime",
          "eventType":"$context.eventType","routeKey":"$context.routeKey",
          "status":"$context.status","connectionId":"$context.connectionId"}
      MinimumCompressionSize: 11485759
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
      AccessLogSetting:
        DestinationArn: 'arn:aws:logs:us-east-1:123456789:log-group:my-log-group'
        Format: >-
          {"requestId":"$context.requestId", "ip": "$context.identity.sourceIp",
          "caller":"$context.identity.caller",
          "user":"$context.identity.user","requestTime":"$context.requestTime",
          "eventType":"$context.eventType","routeKey":"$context.routeKey",
          "status":"$context.status","connectionId":"$context.connectionId"}
```
