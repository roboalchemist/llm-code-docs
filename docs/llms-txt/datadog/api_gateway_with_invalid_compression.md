# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/api_gateway_with_invalid_compression.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/api_gateway_with_invalid_compression.md

---
title: API Gateway with invalid compression
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > API Gateway with invalid compression
---

# API Gateway with invalid compression

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `d6653eee-2d4d-4e6a-976f-6794a497999a`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Low

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html)

### Description{% #description %}

API Gateway should have a valid compression threshold to ensure large responses are compressed, which reduces bandwidth use and helps limit data exposure and amplification risks from large uncompressed payloads. The `AWS::ApiGateway::RestApi` resource must include the `Properties.MinimumCompressionSize` property as an integer between `0` and `10485759` (inclusive). Resources missing this property or with values less than `0` or greater than `10485759` will be flagged.

Secure configuration example:

```yaml
MyApi:
  Type: AWS::ApiGateway::RestApi
  Properties:
    Name: MyApi
    MinimumCompressionSize: 1024
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  RestApi:
    Type: AWS::ApiGateway::RestApi
    Properties:
      Body:
        swagger: 2.0
        info:
            version: 0.0.1
            title: test
        basePath: /pete
        schemes:
            - https
        definitions:
            Empty:
                type: object
      MinimumCompressionSize: 0
      Name: myApi
      Parameters:
          endpointConfigurationTypes: REGIONAL
```

```json
{
  "Resources": {
    "RestApi2": {
      "Type": "AWS::ApiGateway::RestApi",
      "Properties": {
        "Body": {
          "swagger": 2,
          "info": {
            "version": "0.0.1",
            "title": "test"
          },
          "basePath": "/pete",
          "schemes": [
            "https"
          ],
          "definitions": {
            "Empty": {
              "type": "object"
            }
          }
        },
        "MinimumCompressionSize": 0,
        "Name": "myApi",
        "Parameters": {
          "endpointConfigurationTypes": "REGIONAL"
        }
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  RestApi4:
    Type: AWS::ApiGateway::RestApi
    Properties:
      Body:
        swagger: 2.0
        info:
            version: 0.0.1
            title: test
        basePath: /pete
        schemes:
            - https
        definitions:
            Empty:
                type: object
      MinimumCompressionSize: 10485760
      Name: myApi
      Parameters:
          endpointConfigurationTypes: REGIONAL
```

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  RestApi5:
    Type: AWS::ApiGateway::RestApi
    Properties:
      Body:
        swagger: 2.0
        info:
            version: 0.0.1
            title: test
        basePath: /pete
        schemes:
            - https
        definitions:
            Empty:
                type: object
      Name: myApi
      Parameters:
          endpointConfigurationTypes: REGIONAL
```

```json
{
  "Resources": {
    "RestApi7": {
      "Type": "AWS::ApiGateway::RestApi",
      "Properties": {
        "Body": {
          "swagger": 2,
          "info": {
            "version": "0.0.1",
            "title": "test"
          },
          "basePath": "/pete",
          "schemes": [
            "https"
          ],
          "definitions": {
            "Empty": {
              "type": "object"
            }
          }
        },
        "MinimumCompressionSize": 10485760,
        "Name": "myApi",
        "Parameters": {
          "endpointConfigurationTypes": "REGIONAL"
        }
      }
    }
  }
}
```
