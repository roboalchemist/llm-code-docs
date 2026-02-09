# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/iam_policies_attached_to_user.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/iam_policies_attached_to_user.md

---
title: IAM policies attached to a user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > IAM policies attached to a user
---

# IAM policies attached to a user

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `edc95c10-7366-4f30-9b4b-f995c84eceb5`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html)

### Description{% #description %}

Directly attaching IAM policies to individual users increases management complexity and raises the risk of privilege sprawl and inconsistent access control. Centralizing permissions onto groups or roles makes audits and least-privilege enforcement easier. This rule checks AWS CloudFormation `AWS::IAM::User` resources and requires that `Properties.Policies` (inline policies) and `Properties.ManagedPolicyArns` (managed policy ARNs) are undefined or empty. Resources that define non-empty `Policies` or `ManagedPolicyArns` will be flagged; instead attach managed or inline policies to `AWS::IAM::Group` or `AWS::IAM::Role` and assign users to those groups or have them assume roles to receive permissions.

Secure configuration example (attach policies to a group and add the user to the group):

```yaml
MyUserGroup:
  Type: AWS::IAM::Group
  Properties:
    GroupName: my-group
    ManagedPolicyArns:
      - arn:aws:iam::aws:policy/ReadOnlyAccess

MyUser:
  Type: AWS::IAM::User
  Properties:
    UserName: my-user
    Groups:
      - !Ref MyUserGroup
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: A sample template
Resources:
    myuser:
      Type: AWS::IAM::User
      Properties:
        Path: "/"
        LoginProfile:
          Password: myP@ssW0rd
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "A sample template",
  "Resources": {
    "myuser": {
      "Type": "AWS::IAM::User",
      "Properties": {
        "Path": "/",
        "LoginProfile": {
          "Password": "myP@ssW0rd"
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
    "myuser": {
      "Type": "AWS::IAM::User",
      "Properties": {
        "Path": "/",
        "LoginProfile": {
          "Password": "myP@ssW0rd"
        },
        "ManagedPoliciesArns": [
          "arn:aws:iam::123456789012:policy/UsersManageOwnCredentials",
          "arn:aws:iam::123456789012:policy/division_abc/subdivision_xyz/UsersManageOwnCredentials"
        ],
        "Policies": [
          {
            "PolicyName": "giveaccesstoqueueonly",
            "PolicyDocument": {
              "Version": "2012-10-17",
              "Statement": [
                {
                  "Effect": "Allow",
                  "Action": [
                    "sqs:*"
                  ],
                  "Resource": [
                    "myqueue.Arn"
                  ]
                },
                {
                  "NotResource": [
                    "myqueue.Arn"
                  ],
                  "Effect": "Deny",
                  "Action": [
                    "sqs:*"
                  ]
                }
              ]
            }
          }
        ]
      }
    }
  },
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "A sample template"
}
```

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: A sample template
Resources:
    myuser:
      Type: AWS::IAM::User
      Properties:
        Path: "/"
        LoginProfile:
          Password: myP@ssW0rd
        ManagedPoliciesArns: [
          "arn:aws:iam::123456789012:policy/UsersManageOwnCredentials",
          "arn:aws:iam::123456789012:policy/division_abc/subdivision_xyz/UsersManageOwnCredentials"
        ]
        Policies:
        - PolicyName: giveaccesstoqueueonly
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
            - Effect: Allow
              Action:
              - sqs:*
              Resource:
              - !GetAtt myqueue.Arn
            - Effect: Deny
              Action:
              - sqs:*
              NotResource:
              - !GetAtt myqueue.Arn
```
