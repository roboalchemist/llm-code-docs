# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/api_gateway_xray_disabled.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/api_gateway_xray_disabled.md

---
title: API Gateway X-Ray disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > API Gateway X-Ray disabled
---

# API Gateway X-Ray disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `4ab10c48-bedb-4deb-8f3b-ff12783b61de`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Low

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.html#cfn-apigateway-stage-tracingenabled)

### Description{% #description %}

Failing to enable AWS X-Ray tracing on API Gateway stages prevents collection of end-to-end request traces, which hinders latency analysis, root-cause investigation, and detection of suspicious cross-service behavior. The `TracingEnabled` property on `AWS::ApiGateway::Stage` resources must be defined and set to `true`. Resources that omit `TracingEnabled` or set it to `false` (boolean `false` or the string `"false"`) will be flagged.

Secure configuration example:

```yaml
MyStage:
  Type: AWS::ApiGateway::Stage
  Properties:
    StageName: prod
    RestApiId: !Ref MyApi
    TracingEnabled: true
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "BatchJobDefinition"
Resources:
  ProdNeg1:
    Type: AWS::ApiGateway::Stage
    Properties:
      StageName: Prod
      Description: Prod Stage
      RestApiId: !Ref MyRestApi
      DeploymentId: !Ref TestDeployment
      DocumentationVersion: !Ref MyDocumentationVersion
      ClientCertificateId: !Ref ClientCertificate
      TracingEnabled: true
      Variables:
        Stack: Prod
      MethodSettings:
        - ResourcePath: /
          HttpMethod: GET
          MetricsEnabled: 'true'
          DataTraceEnabled: 'false'
        - ResourcePath: /stack
          HttpMethod: POST
          MetricsEnabled: 'true'
          DataTraceEnabled: 'false'
          ThrottlingBurstLimit: '999'
        - ResourcePath: /stack
          HttpMethod: GET
          MetricsEnabled: 'true'
          DataTraceEnabled: 'false'
          ThrottlingBurstLimit: '555'
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "ProdNeg2": {
      "Type": "AWS::ApiGateway::Stage",
      "Properties": {
        "StageName": "Prod",
        "RestApiId": {
          "Ref": "MyRestApi"
        },
        "DeploymentId": {
          "Ref": "TestDeployment"
        },
        "DocumentationVersion": {
          "Ref": "MyDocumentationVersion"
        },
        "ClientCertificateId": {
          "Ref": "ClientCertificate"
        },
        "Variables": {
          "Stack": "Prod"
        },
        "TracingEnabled": "true",
        "MethodSettings": [
          {
            "ResourcePath": "/",
            "HttpMethod": "GET",
            "MetricsEnabled": "true",
            "DataTraceEnabled": "false"
          },
          {
            "ResourcePath": "/stack",
            "HttpMethod": "POST",
            "MetricsEnabled": "true",
            "DataTraceEnabled": "false",
            "ThrottlingBurstLimit": "999"
          },
          {
            "ResourcePath": "/stack",
            "HttpMethod": "GET",
            "MetricsEnabled": "true",
            "DataTraceEnabled": "false",
            "ThrottlingBurstLimit": "555"
          }
        ]
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "BatchJobDefinition"
Resources:
  ProdPos4:
    Type: AWS::ApiGateway::Stage
    Properties:
      StageName: Prod
      Description: Prod Stage
      RestApiId: !Ref MyRestApi
      DeploymentId: !Ref TestDeployment
      DocumentationVersion: !Ref MyDocumentationVersion
      ClientCertificateId: !Ref ClientCertificate
      Variables:
        Stack: Prod
      MethodSettings:
        - ResourcePath: /
          HttpMethod: GET
          MetricsEnabled: 'true'
          DataTraceEnabled: 'false'
        - ResourcePath: /stack
          HttpMethod: POST
          MetricsEnabled: 'true'
          DataTraceEnabled: 'false'
          ThrottlingBurstLimit: '999'
        - ResourcePath: /stack
          HttpMethod: GET
          MetricsEnabled: 'true'
          DataTraceEnabled: 'false'
          ThrottlingBurstLimit: '555'
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "ProdPos1": {
      "Type": "AWS::ApiGateway::Stage",
      "Properties": {
        "StageName": "Prod",
        "RestApiId": {
          "Ref": "MyRestApi"
        },
        "DeploymentId": {
          "Ref": "TestDeployment"
        },
        "DocumentationVersion": {
          "Ref": "MyDocumentationVersion"
        },
        "ClientCertificateId": {
          "Ref": "ClientCertificate"
        },
        "Variables": {
          "Stack": "Prod"
        },
        "TracingEnabled": "false",
        "MethodSettings": [
          {
            "ResourcePath": "/",
            "HttpMethod": "GET",
            "MetricsEnabled": "true",
            "DataTraceEnabled": "false"
          },
          {
            "ResourcePath": "/stack",
            "HttpMethod": "POST",
            "MetricsEnabled": "true",
            "DataTraceEnabled": "false",
            "ThrottlingBurstLimit": "999"
          },
          {
            "ResourcePath": "/stack",
            "HttpMethod": "GET",
            "MetricsEnabled": "true",
            "DataTraceEnabled": "false",
            "ThrottlingBurstLimit": "555"
          }
        ]
      }
    }
  }
}
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "ProdPos2": {
      "Type": "AWS::ApiGateway::Stage",
      "Properties": {
        "StageName": "Prod",
        "RestApiId": {
          "Ref": "MyRestApi"
        },
        "DeploymentId": {
          "Ref": "TestDeployment"
        },
        "DocumentationVersion": {
          "Ref": "MyDocumentationVersion"
        },
        "ClientCertificateId": {
          "Ref": "ClientCertificate"
        },
        "Variables": {
          "Stack": "Prod"
        },
        "MethodSettings": [
          {
            "ResourcePath": "/",
            "HttpMethod": "GET",
            "MetricsEnabled": "true",
            "DataTraceEnabled": "false"
          },
          {
            "ResourcePath": "/stack",
            "HttpMethod": "POST",
            "MetricsEnabled": "true",
            "DataTraceEnabled": "false",
            "ThrottlingBurstLimit": "999"
          },
          {
            "ResourcePath": "/stack",
            "HttpMethod": "GET",
            "MetricsEnabled": "true",
            "DataTraceEnabled": "false",
            "ThrottlingBurstLimit": "555"
          }
        ]
      }
    }
  }
}
```
