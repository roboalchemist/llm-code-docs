# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/api_gateway_without_security_policy.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/api_gateway_without_security_policy.md

---
title: API Gateway without security policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > API Gateway without security policy
---

# API Gateway without security policy

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `8275fab0-68ec-4705-bbf4-86975edb170e`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-securitypolicy)

### Description{% #description %}

API Gateway custom domain names must enforce TLS 1.2 to avoid allowing older TLS/SSL versions that are susceptible to downgrade attacks and weak ciphers, thereby protecting confidentiality and integrity of client-server connections. In CloudFormation, the `AWS::ApiGateway::DomainName` resource must include the `SecurityPolicy` property set to `TLS_1_2`. Resources missing `SecurityPolicy` or with any value other than `TLS_1_2` will be flagged.

Secure CloudFormation example:

```yaml
MyDomainName:
  Type: AWS::ApiGateway::DomainName
  Properties:
    DomainName: api.example.com
    SecurityPolicy: TLS_1_2
    RegionalCertificateArn: arn:aws:acm:us-east-1:123456789012:certificate/abcd-ef01-2345
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "Router53"
Parameters:
  cfnDomainName:
    Type: String
  certificateArn:
    Type: String
  type:
    Type: String
Resources:
  myDomainName:
    Type: AWS::ApiGateway::DomainName
    Properties:
      CertificateArn: !Ref certificateArn
      DomainName: !Ref cfnDomainName
      EndpointConfiguration:
        Types:
          - !Ref type
      RegionalCertificateArn: !Ref certificateArn
      SecurityPolicy: "TLS_1_2"
Outputs:
  DomainName:
    Value: !Ref myDomainName
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "Router53",
  "Parameters": {
    "cfnDomainName": {
      "Type": "String"
    },
    "certificateArn": {
      "Type": "String"
    },
    "type": {
      "Type": "String"
    }
  },
  "Resources": {
    "myDomainName": {
      "Type": "AWS::ApiGateway::DomainName",
      "Properties": {
        "DomainName": "cfnDomainName",
        "EndpointConfiguration": {
          "Types": [
            "type"
          ]
        },
        "RegionalCertificateArn": "certificateArn",
        "SecurityPolicy": "TLS_1_2",
        "CertificateArn": "certificateArn"
      }
    }
  },
  "Outputs": {
    "DomainName": {
      "Value": "myDomainName"
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "Router53"
Parameters:
  cfnDomainName:
    Type: String
  certificateArn:
    Type: String
  type:
    Type: String
Resources:
  myDomainName1:
    Type: AWS::ApiGateway::DomainName
    Properties:
      CertificateArn: !Ref certificateArn
      DomainName: !Ref cfnDomainName
      EndpointConfiguration:
        Types:
          - !Ref type
      RegionalCertificateArn: !Ref certificateArn
Outputs:
  DomainName:
    Value: !Ref myDomainName
```

```json
{
  "Description": "Router53",
  "Parameters": {
    "cfnDomainName": {
      "Type": "String"
    },
    "certificateArn": {
      "Type": "String"
    },
    "type": {
      "Type": "String"
    }
  },
  "Resources": {
    "myDomainName": {
      "Type": "AWS::ApiGateway::DomainName",
      "Properties": {
        "CertificateArn": "certificateArn",
        "DomainName": "cfnDomainName",
        "EndpointConfiguration": {
          "Types": [
            "type"
          ]
        },
        "RegionalCertificateArn": "certificateArn",
        "SecurityPolicy": "TLS_1_0"
      }
    }
  },
  "Outputs": {
    "DomainName": {
      "Value": "myDomainName"
    }
  },
  "AWSTemplateFormatVersion": "2010-09-09"
}
```

```json
{
  "Parameters": {
    "type": {
      "Type": "String"
    },
    "cfnDomainName": {
      "Type": "String"
    },
    "certificateArn": {
      "Type": "String"
    }
  },
  "Resources": {
    "myDomainName1": {
      "Properties": {
        "DomainName": "cfnDomainName",
        "EndpointConfiguration": {
          "Types": [
            "type"
          ]
        },
        "RegionalCertificateArn": "certificateArn",
        "CertificateArn": "certificateArn"
      },
      "Type": "AWS::ApiGateway::DomainName"
    }
  },
  "Outputs": {
    "DomainName": {
      "Value": "myDomainName"
    }
  },
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "Router53"
}
```
