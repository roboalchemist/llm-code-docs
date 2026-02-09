# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/api_gateway_access_logging_disabled.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/api_gateway_access_logging_disabled.md

---
title: API Gateway V2 stage access logging settings not defined
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > API Gateway V2 stage access logging settings
  not defined
---

# API Gateway V2 stage access logging settings not defined

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `80d45af4-4920-4236-a56e-b7ef419d1941`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-accesslogsettings)

### Description{% #description %}

API Gateway stages must have access logging and route-level/method-level request logging enabled so request activity is recorded for auditing, troubleshooting, and detecting abuse or suspicious behavior.

For HTTP APIs (`AWS::ApiGatewayV2::Stage`), `AccessLogSettings` must be defined and `DefaultRouteSettings.LoggingLevel` must be present and not set to `OFF` (use values like `INFO` or `ERROR`).

For REST APIs (`AWS::ApiGateway::Stage`), `AccessLogSetting` must be defined and each relevant entry in `MethodSettings` must include a `LoggingLevel` that is not `OFF`.

Resources missing these properties or with `LoggingLevel` set to `OFF` will be flagged.

Secure configuration examples:

```yaml
MyHttpApiStage:
  Type: AWS::ApiGatewayV2::Stage
  Properties:
    StageName: prod
    AccessLogSettings:
      DestinationArn: arn:aws:logs:us-east-1:123456789012:log-group:/aws/apigateway/http-api
      Format: '$context.identity.sourceIp - $context.requestId - $context.requestTime'
    DefaultRouteSettings:
      LoggingLevel: INFO
```

```yaml
MyRestApiStage:
  Type: AWS::ApiGateway::Stage
  Properties:
    StageName: prod
    AccessLogSetting:
      DestinationArn: arn:aws:logs:us-east-1:123456789012:log-group:/aws/apigateway/rest-api
      Format: '$context.identity.sourceIp - $context.requestId - $context.requestTime'
    MethodSettings:
      - ResourcePath: "/*"
        HttpMethod: "*"
        LoggingLevel: INFO
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "Router53"
Resources:
  MyStage:
    Type: 'AWS::ApiGatewayV2::Stage'
    Properties:
      StageName: Prod
      Description: Prod Stage
      DeploymentId: !Ref MyDeployment
      ApiId: !Ref CFNWebSocket
      DefaultRouteSettings:
        DetailedMetricsEnabled: true
        LoggingLevel: INFO
        DataTraceEnabled: false
        ThrottlingBurstLimit: 10
        ThrottlingRateLimit: 10
      AccessLogSettings:
        DestinationArn: 'arn:aws:logs:us-east-1:123456789:log-group:my-log-group'
        Format: >-
          {"requestId":"$context.requestId", "ip": "$context.identity.sourceIp",
          "caller":"$context.identity.caller",
          "user":"$context.identity.user","requestTime":"$context.requestTime",
          "eventType":"$context.eventType","routeKey":"$context.routeKey",
          "status":"$context.status","connectionId":"$context.connectionId"}
```

```yaml
Resources:
  Prod:
    Type: AWS::ApiGateway::Stage
    Properties:
      StageName: Prod
      Description: Prod Stage
      RestApiId: !Ref MyRestApi
      DeploymentId: !Ref TestDeployment
      DocumentationVersion: ""
      MethodSettings:
        LoggingLevel: "ON"
      AccessLogSetting:
        DestinationArn: "dest"
        Format: "format"
```

```json
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "MyStage": {
            "Type": "AWS::ApiGateway::Stage",
            "Properties": {
                "StageName": "Prod",
                "Description": "Prod Stage",
                "AccessLogSetting": {
                    "DestinationArn": "dest",
                    "Format": "format"
                },
                "DeploymentId": {
                    "Ref": "MyDeployment"
                },
                "MethodSettings": {
                  "DetailedMetricsEnabled": true,
                  "LoggingLevel": "INFO",
                  "DataTraceEnabled": false,
                  "ThrottlingBurstLimit": 10,
                  "ThrottlingRateLimit": 10
                },
                "RestApiId": {
                    "Ref": "CFNWebSocket"
                }
            }
        }
    }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
Resources:
  Prod:
    Type: AWS::ApiGateway::Stage
    Properties:
      StageName: Prod
      Description: Prod Stage
      AccessLogSetting: 
        DestinationArn: "dest"
        Format: "format"
      RestApiId: !Ref MyRestApi
      DeploymentId: !Ref TestDeployment
      DocumentationVersion: ""
      MethodSettings:
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "MyStage": {
      "Type": "AWS::ApiGatewayV2::Stage",
      "Properties": {
        "StageName": "Prod",
        "Description": "Prod Stage",
        "AccessLogSettings": {
            "DestinationArn": "dest",
            "Format": "format"
        },
        "DeploymentId": {
          "Ref": "MyDeployment"
        },
        "ApiId": {
          "Ref": "CFNWebSocket"
        },
        "DefaultRouteSettings": {
          "DetailedMetricsEnabled": true,
          "LoggingLevel": "OFF",
          "DataTraceEnabled": false,
          "ThrottlingBurstLimit": 10,
          "ThrottlingRateLimit": 10
        }
      }
    }
  }
}
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "MyStage": {
      "Type": "AWS::ApiGateway::Stage",
      "Properties": {
        "StageName": "Prod",
        "Description": "Prod Stage",
        "AccessLogSetting": {
            "DestinationArn": "dest",
            "Format": "format"
        },
        "DeploymentId": {
          "Ref": "MyDeployment"
        },
        "RestApiId": {
          "Ref": "CFNWebSocket"
        },
        "MethodSettings": {
        }
      }
    }
  }
}
```
