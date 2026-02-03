# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/api_gateway_cache_encrypted_disabled.md

---
title: API Gateway cache encrypted disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > API Gateway cache encrypted disabled
---

# API Gateway cache encrypted disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `37cca703-b74c-48ba-ac81-595b53398e9b`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-stagedescription.html)

### Description{% #description %}

API Gateway stage caches can store sensitive response data. If caching is enabled but cache data is not encrypted, cached content at rest may be exposed via compromised storage or unauthorized access.

For CloudFormation, `AWS::ApiGateway::Deployment` resources must set `StageDescription.CacheDataEncrypted` to `true` whenever `StageDescription.CachingEnabled` is set to `true`. Resources missing the `CacheDataEncrypted` property or with `CacheDataEncrypted` set to `false` while caching is enabled will be flagged.

Secure configuration example:

```yaml
MyDeployment:
  Type: AWS::ApiGateway::Deployment
  Properties:
    RestApiId: !Ref MyApi
    StageName: prod
    StageDescription:
      CachingEnabled: true
      CacheDataEncrypted: true
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
Resources:
  Deployment:
    Type: 'AWS::ApiGateway::Deployment'
    Properties:
      RestApiId: !Ref MyApi
      Description: My deployment
      StageName: DummyStage
      StageDescription:
        CacheDataEncrypted: true
        CachingEnabled: true
```

```json
{
  "Resources": {
    "Deployment": {
      "Type": "AWS::ApiGateway::Deployment",
      "Properties": {
        "RestApiId": {
          "Ref": "MyApi"
        },
        "Description": "My deployment",
        "StageName": "DummyStage",
        "StageDescription": {
          "CacheDataEncrypted": true,
          "CachingEnabled": true
        }
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "Resources": {
    "Deployment": {
      "Type": "AWS::ApiGateway::Deployment",
      "Properties": {
        "RestApiId": {
          "Ref": "MyApi"
        },
        "Description": "My deployment",
        "StageName": "DummyStage",
        "StageDescription": {
          "CachingEnabled": true
        }
      }
    }
  }
}
```

```yaml
Resources:
  Deployment:
    Type: 'AWS::ApiGateway::Deployment'
    Properties:
      RestApiId: !Ref MyApi
      Description: My deployment
      StageName: DummyStage
      StageDescription:
        CacheDataEncrypted: false
        CachingEnabled: true
```

```json
{
  "Resources": {
    "Deployment": {
      "Type": "AWS::ApiGateway::Deployment",
      "Properties": {
        "RestApiId": {
          "Ref": "MyApi"
        },
        "Description": "My deployment",
        "StageName": "DummyStage",
        "StageDescription": {
          "CacheDataEncrypted": false,
          "CachingEnabled": true
        }
      }
    }
  }
}
```
