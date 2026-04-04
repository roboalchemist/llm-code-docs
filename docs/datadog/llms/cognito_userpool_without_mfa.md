# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/cognito_userpool_without_mfa.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/cognito_userpool_without_mfa.md

---
title: Cognito user pool without MFA
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Cognito user pool without MFA
---

# Cognito user pool without MFA

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `74a18d1a-cf02-4a31-8791-ed0967ad7fdc`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Low

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html)

### Description{% #description %}

Cognito User Pools must enable or allow multi-factor authentication (MFA) to protect user accounts from compromised credentials and reduce the risk of account takeover and unauthorized access. The `MfaConfiguration` property in `AWS::Cognito::UserPool` must be defined and set to `ON` (enforce MFA for all users) or `OPTIONAL` (allow users to enable MFA). Resources that omit `MfaConfiguration` or set it to `OFF` will be flagged. When enabling or allowing MFA, also configure an MFA provider such as `SoftwareTokenMfaConfiguration` or `SmsConfiguration` so MFA can operate correctly.

Secure configuration example (CloudFormation YAML):

```yaml
MyUserPool:
  Type: AWS::Cognito::UserPool
  Properties:
    UserPoolName: my-user-pool
    MfaConfiguration: ON
    SoftwareTokenMfaConfiguration:
      Enabled: true
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
Resources:
  UserPool:
    Type: "AWS::Cognito::UserPool"
    Properties:
      UserPoolName: !Sub ${AuthName}-user-pool
      AutoVerifiedAttributes:
        - phone_number
      MfaConfiguration: "ON"
      SmsConfiguration:
        ExternalId: !Sub ${AuthName}-external
        SnsCallerArn: !GetAtt SNSRole.Arn
  UserPool2:
    Type: "AWS::Cognito::UserPool"
    Properties:
      UserPoolName: !Sub ${AuthName}-user-pool
      AutoVerifiedAttributes:
        - phone_number
      MfaConfiguration: "OPTIONAL"
      SmsConfiguration:
        ExternalId: !Sub ${AuthName}-external
        SnsCallerArn: !GetAtt SNSRole.Arn
```

```json
{
  "Resources": {
    "UserPool": {
      "Type": "AWS::Cognito::UserPool",
      "Properties": {
        "UserPoolName": "${AuthName}-user-pool",
        "AutoVerifiedAttributes": [
          "phone_number"
        ],
        "MfaConfiguration": "ON",
        "SmsConfiguration": {
          "ExternalId": "${AuthName}-external",
          "SnsCallerArn": "SNSRole.Arn"
        }
      }
    },
    "UserPool2": {
      "Type": "AWS::Cognito::UserPool",
      "Properties": {
        "UserPoolName": "${AuthName}-user-pool",
        "AutoVerifiedAttributes": [
          "phone_number"
        ],
        "MfaConfiguration": "OPTIONAL",
        "SmsConfiguration": {
          "ExternalId": "${AuthName}-external",
          "SnsCallerArn": "SNSRole.Arn"
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
    "UserPool2": {
      "Type": "AWS::Cognito::UserPool",
      "Properties": {
        "UserPoolName": "${AuthName}-user-pool",
        "AutoVerifiedAttributes": [
          "phone_number"
        ],
        "MfaConfiguration": "OFF",
        "SmsConfiguration": {
          "ExternalId": "${AuthName}-external",
          "SnsCallerArn": "SNSRole.Arn"
        }
      }
    },
    "UserPool4": {
      "Type": "AWS::Cognito::UserPool",
      "Properties": {
        "SmsConfiguration": {
          "ExternalId": "${AuthName}-external",
          "SnsCallerArn": "SNSRole.Arn"
        },
        "UserPoolName": "${AuthName}-user-pool",
        "AutoVerifiedAttributes": [
          "phone_number"
        ]
      }
    }
  }
}
```

```yaml
Resources:
  UserPool2:
    Type: "AWS::Cognito::UserPool"
    Properties:
      UserPoolName: !Sub ${AuthName}-user-pool
      AutoVerifiedAttributes:
        - phone_number
      MfaConfiguration: "OFF"
      SmsConfiguration:
        ExternalId: !Sub ${AuthName}-external
        SnsCallerArn: !GetAtt SNSRole.Arn
  UserPool4:
    Type: "AWS::Cognito::UserPool"
    Properties:
      UserPoolName: !Sub ${AuthName}-user-pool
      AutoVerifiedAttributes:
        - phone_number
      SmsConfiguration:
        ExternalId: !Sub ${AuthName}-external
        SnsCallerArn: !GetAtt SNSRole.Arn
```
