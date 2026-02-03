# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/api_gateway_endpoint_config_is_not_private.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/api_gateway_endpoint_config_is_not_private.md

---
title: API Gateway endpoint config is not private
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > API Gateway endpoint config is not private
---

# API Gateway endpoint config is not private

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `4a8daf95-709d-4a36-9132-d3e19878fa34`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-restapi-endpointconfiguration.html#cfn-apigateway-restapi-endpointconfiguration-types)

### Description{% #description %}

API Gateway REST APIs should be configured with a `PRIVATE` endpoint to avoid unintended exposure to the public internet. Publicly accessible APIs increase attack surface and can enable unauthorized access to internal services or sensitive data.

For CloudFormation, the `AWS::ApiGateway::RestApi` resource must define the `EndpointConfiguration` property and its `Types` list must include `PRIVATE`. Resources missing `EndpointConfiguration`, missing `Types`, or whose `Types` list does not contain `PRIVATE` will be flagged.

Secure configuration example:

```yaml
MyPrivateApi:
  Type: AWS::ApiGateway::RestApi
  Properties:
    Name: my-private-api
    EndpointConfiguration:
      Types:
        - PRIVATE
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: 2010-09-09
Resources:
    MyRestApi:
        Type: AWS::ApiGateway::RestApi
        Properties:
          EndpointConfiguration:
            Types:
              - PRIVATE
          Name: myRestApi
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Resources": {
    "MyRestApi": {
      "Type": "AWS::ApiGateway::RestApi",
      "Properties": {
        "EndpointConfiguration": {
          "Types": [
            "PRIVATE"
          ]
        },
        "Name": "myRestApi"
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Resources": {
    "MyRestApi": {
      "Type": "AWS::ApiGateway::RestApi",
      "Properties": {
        "Name": "myRestApi"
      }
    },
    "MyRestApi2": {
      "Type": "AWS::ApiGateway::RestApi",
      "Properties": {
        "EndpointConfiguration": {
          "Types": [
            "EDGE"
          ]
        },
        "Name": "myRestApi2"
      }
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: 2010-09-09
Resources:
    MyRestApi:
        Type: AWS::ApiGateway::RestApi
        Properties:
          Name: myRestApi
    MyRestApi2:
        Type: AWS::ApiGateway::RestApi
        Properties:
          EndpointConfiguration:
            Types:
              - EDGE
          Name: myRestApi2
```
