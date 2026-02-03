# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/iot_policy_allows_action_as_wildcard.md

---
title: IoT policy allows action as a wildcard
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > IoT policy allows action as a wildcard
---

# IoT policy allows action as a wildcard

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `4d32780f-43a4-424a-a06d-943c543576a5`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policy.html)

### Description{% #description %}

IoT policies that grant the wildcard action `*` with an `Allow` effect are overly permissive and can enable principals to perform any IoT operation. This increases the risk of device takeover, unauthorized message publishing or subscribing, and configuration changes.

In AWS CloudFormation, inspect `AWS::IoT::Policy` resources' `Properties.PolicyDocument.Statement` entries. A `Statement` with `Effect: Allow` and `Action` equal to `*` (or containing `*` in an action array) is a misconfiguration. This rule flags those statements. Follow least privilege by enumerating only the specific `iot:*` actions required and scoping the `Resource` ARNs to the minimum necessary.

Example secure configuration restricting actions and resources:

```yaml
MyIotPolicy:
  Type: AWS::IoT::Policy
  Properties:
    PolicyDocument:
      Version: "2012-10-17"
      Statement:
        - Effect: Allow
          Action:
            - "iot:Connect"
            - "iot:Publish"
            - "iot:Subscribe"
            - "iot:Receive"
          Resource: "arn:aws:iot:us-west-2:123456789012:client/my-device-*"
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: 2010-09-09
Description: A sample template
Resources:
    IoTPolicy:
      Type: AWS::IoT::Policy
      Properties:
        PolicyDocument:
          Version: '2012-10-17'
          Statement:
          - Effect: Allow
            Action:
            - iot:Connect
            Resource:
            - arn:aws:iot:us-east-1:123456789012:client/client1
        PolicyName: PolicyName
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Description": "A sample template",
  "Resources": {
    "IoTPolicy": {
      "Type": "AWS::IoT::Policy",
      "Properties": {
        "PolicyDocument": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Action": [
                "iot:Connect"
              ],
              "Resource": [
                "arn:aws:iot:us-east-1:123456789012:client/client1"
              ]
            }
          ]
        },
        "PolicyName": "PolicyName"
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "Resources": {
    "IoTPolicy": {
      "Type": "AWS::IoT::Policy",
      "Properties": {
        "PolicyDocument": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Action": "*",
              "Resource": [
                "arn:aws:iot:us-east-1:123456789012:client/client"
              ]
            },
            {
              "Effect": "Deny",
              "Action": [
                "sqs:*"
              ],
              "NotResource": "my-hardcoded-arn"
            }
          ]
        },
        "PolicyName": "PolicyName"
      }
    }
  },
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Description": "A sample template"
}
```

```yaml
AWSTemplateFormatVersion: 2010-09-09
Description: A sample template
Resources:
    IoTPolicy:
      Type: AWS::IoT::Policy
      Properties:
        PolicyDocument:
          Version: '2012-10-17'
          Statement:
          - Effect: Allow
            Action: "*"
            Resource:
            - arn:aws:iot:us-east-1:123456789012:client/client
          - Effect: Deny
            Action:
            - sqs:*
            NotResource: my-hardcoded-arn
        PolicyName: PolicyName
```
