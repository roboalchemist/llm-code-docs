# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/iam_policy_grants_full_permissions.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/iam_policy_grants_full_permissions.md

---
title: IAM policy grants full permissions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > IAM policy grants full permissions
---

# IAM policy grants full permissions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `f62aa827-4ade-4dc4-89e4-1433d384a368`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** High

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html)

### Description{% #description %}

IAM policies that allow both `Action: "*"` and `Resource: "*"` grant unrestricted access, posing risks of privilege escalation and data exfiltration. This rule flags `AWS::IAM::Policy` resources in CloudFormation templates when a `PolicyDocument.Statement` has `Effect: "Allow"` and both `Action` and `Resource` are set to `"*"`, including when they appear in arrays. To enforce least privilege, restrict permissions to specific actions and ARNs, or apply conditions, roles, and permission boundaries.

Secure example:

```yaml
MyPolicy:
  Type: AWS::IAM::Policy
  Properties:
    PolicyName: ReadS3BucketPolicy
    PolicyDocument:
      Version: "2012-10-17"
      Statement:
        - Effect: Allow
          Action:
            - s3:GetObject
          Resource: arn:aws:s3:::my-bucket/*
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: A sample template
Resources:
  adminPolicy:
    Type: AWS::IAM::Policy
    Properties:
      PolicyName: mygrouppolicy
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
        - Effect: Allow
          Action: ["*"]
          Resource: arn:aws:iam::aws:policy/AdministratorAccess
      Groups:
      - myexistinggroup1
      - !Ref mygroup
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "A sample template",
  "Resources": {
    "adminPolicy": {
      "Type": "AWS::IAM::Policy",
      "Properties": {
        "PolicyName": "mygrouppolicy",
        "PolicyDocument": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Resource": "arn:aws:iam::aws:policy/AdministratorAccess",
              "Effect": "Allow",
              "Action": [
                "*"
              ]
            }
          ]
        },
        "Groups": [
          "myexistinggroup1",
          "mygroup"
        ]
      }
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: A sample template
Resources:
  adminPolicy:
    Type: AWS::IAM::Policy
    Properties:
      PolicyName: mygrouppolicy
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
        - Effect: Allow
          Action: 'ec2messages:GetEndpoint'
          Resource: ['*']
      Groups:
      - myexistinggroup1
      - !Ref mygroup
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "A sample template",
  "Resources": {
    "mypolicy2": {
      "Type": "AWS::IAM::Policy",
      "Properties": {
        "PolicyName": "mygrouppolicy",
        "PolicyDocument": {
          "Statement": [
            {
              "Effect": "Allow",
              "Action": "*",
              "Resource": "*"
            }
          ],
          "Version": "2012-10-17"
        },
        "Groups": [
          "myexistinggroup1",
          "mygroup"
        ]
      }
    },
    "mypolicy": {
      "Type": "AWS::IAM::Policy",
      "Properties": {
        "PolicyName": "mygrouppolicy",
        "PolicyDocument": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Action": [
                "*"
              ],
              "Resource": "*"
            }
          ]
        },
        "Groups": [
          "myexistinggroup1",
          "mygroup"
        ]
      }
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: A sample template
Resources:
  mypolicy:
    Type: AWS::IAM::Policy
    Properties:
      PolicyName: mygrouppolicy
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
        - Effect: Allow
          Action: ["*"]
          Resource: "*"
      Groups:
      - myexistinggroup1
      - !Ref mygroup
  mypolicy2:
    Type: AWS::IAM::Policy
    Properties:
      PolicyName: mygrouppolicy
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
        - Effect: Allow
          Action: "*"
          Resource: "*"
      Groups:
      - myexistinggroup1
      - !Ref mygroup
```
