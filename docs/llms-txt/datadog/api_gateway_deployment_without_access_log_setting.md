# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/api_gateway_deployment_without_access_log_setting.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/api_gateway_deployment_without_access_log_setting.md

---
title: API Gateway deployment without access log setting
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > API Gateway deployment without access log
  setting
---

# API Gateway deployment without access log setting

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `06ec63e3-9f72-4fe2-a218-2eb9200b8db5`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-deployment.html)

### Description{% #description %}

API Gateway stages must have access logging enabled so request activity is recorded for detection, auditing, and incident investigation. Without access logs, malicious or anomalous traffic can go undetected and forensic analysis is limited.

In CloudFormation, when an `AWS::ApiGateway::Stage` resource references a deployment (its `Properties.DeploymentId.Ref` equals the deployment logical ID), the corresponding `AWS::ApiGateway::Deployment` must define `StageDescription` and include `StageDescription.AccessLogSetting`.

This rule flags deployments missing `StageDescription` or `StageDescription.AccessLogSetting`. It also verifies that an `AWS::ApiGateway::Stage` exists and that its `DeploymentId.Ref` matches the deployment; mismatched or missing stage associations are reported as incorrect configuration.

Secure configuration example:

```yaml
MyDeployment:
  Type: AWS::ApiGateway::Deployment
  Properties:
    StageDescription:
      AccessLogSetting:
        DestinationArn: arn:aws:logs:us-east-1:123456789012:log-group:/aws/api-gateway/my-api
        Format: '{"requestId":"$context.requestId","ip":"$context.identity.sourceIp","requestTime":"$context.requestTime","httpMethod":"$context.httpMethod","resourcePath":"$context.resourcePath","status":"$context.status"}'

MyStage:
  Type: AWS::ApiGateway::Stage
  Properties:
    StageName: prod
    DeploymentId:
      Ref: MyDeployment
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "ApiGateway"
Resources:
  GreetingApiProdStage:
    DependsOn:
    - ApiGatewayAccount
    Type: AWS::ApiGateway::Stage
    Properties:
      DeploymentId:
        Ref: ApiDeployment
      MethodSettings:
      - DataTraceEnabled: true
        HttpMethod: "*"
        LoggingLevel: INFO
        ResourcePath: "/*"
      RestApiId:
        Ref: GreetingApi
      StageName: prod
      Variables:
        LambdaAlias: PROD
  ApiDeployment:
    Type: AWS::ApiGateway::Deployment
    DependsOn:
    - GreetingRequest
    Properties:
      RestApiId:
        Ref: GreetingApi
      StageName: DummyStage
      StageDescription:
        AccessLogSetting:
          DestinationArn: "dest"
          Format: "format"
```

```json
{
  "Resources": {
    "GreetingApiProdStage": {
      "DependsOn": [
        "ApiGatewayAccount"
      ],
      "Type": "AWS::ApiGateway::Stage",
      "Properties": {
        "Variables": {
          "LambdaAlias": "PROD"
        },
        "DeploymentId": {
          "Ref": "ApiDeployment"
        },
        "MethodSettings": [
          {
            "HttpMethod": "*",
            "LoggingLevel": "INFO",
            "ResourcePath": "/*",
            "DataTraceEnabled": true
          }
        ],
        "RestApiId": {
          "Ref": "GreetingApi"
        },
        "StageName": "prod"
      }
    },
    "ApiDeployment": {
      "Type": "AWS::ApiGateway::Deployment",
      "DependsOn": [
        "GreetingRequest"
      ],
      "Properties": {
        "RestApiId": {
          "Ref": "GreetingApi"
        },
        "StageName": "DummyStage",
        "StageDescription": {
          "AccessLogSetting": {
            "DestinationArn": "dest",
            "Format": "format"
          }
        }
      }
    }
  },
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "ApiGateway"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "ApiGateway"
Resources:
  GreetingApiProdStage1:
    DependsOn:
    - ApiGatewayAccount
    Type: AWS::ApiGateway::Stage
    Properties:
      DeploymentId:
        Ref: ApiDeployment
      MethodSettings:
      - DataTraceEnabled: true
        HttpMethod: "*"
        LoggingLevel: INFO
        ResourcePath: "/*"
      RestApiId:
        Ref: GreetingApi
      StageName: prod
      Variables:
        LambdaAlias: PROD
  ApiDeployment1:
    Type: AWS::ApiGateway::Deployment
    DependsOn:
    - GreetingRequest
    Properties:
      RestApiId:
        Ref: GreetingApi
      StageName: DummyStage
```

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "ApiGateway"
Resources:
  GreetingApiProdStage2:
    DependsOn:
    - ApiGatewayAccount
    Type: AWS::ApiGateway::Stage
    Properties:
      DeploymentId:
        Ref: ApiDeployment
      MethodSettings:
      - DataTraceEnabled: true
        HttpMethod: "*"
        LoggingLevel: INFO
        ResourcePath: "/*"
      RestApiId:
        Ref: GreetingApi
      StageName: prod
      Variables:
        LambdaAlias: PROD
  ApiDeployment2:
    Type: AWS::ApiGateway::Deployment
    DependsOn:
    - GreetingRequest
    Properties:
      RestApiId:
        Ref: GreetingApi
      StageName: DummyStage
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "ApiGateway",
  "Resources": {
    "GreetingApiProdStage1": {
      "DependsOn": [
        "ApiGatewayAccount"
      ],
      "Type": "AWS::ApiGateway::Stage",
      "Properties": {
        "DeploymentId": {
          "Ref": "ApiDeployment"
        },
        "MethodSettings": [
          {
            "LoggingLevel": "INFO",
            "ResourcePath": "/*",
            "DataTraceEnabled": true,
            "HttpMethod": "*"
          }
        ],
        "RestApiId": {
          "Ref": "GreetingApi"
        },
        "StageName": "prod",
        "Variables": {
          "LambdaAlias": "PROD"
        }
      }
    },
    "ApiDeployment1": {
      "Type": "AWS::ApiGateway::Deployment",
      "DependsOn": [
        "GreetingRequest"
      ],
      "Properties": {
        "RestApiId": {
          "Ref": "GreetingApi"
        },
        "StageName": "DummyStage"
      }
    }
  }
}
```
