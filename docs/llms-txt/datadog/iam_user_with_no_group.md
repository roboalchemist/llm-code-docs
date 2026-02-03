# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/iam_user_with_no_group.md

---
title: IAM user with no group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > IAM user with no group
---

# IAM user with no group

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `06933df4-0ea7-461c-b9b5-104d27390e0e`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Low

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-iam.html#scenario-iam-policy)

### Description{% #description %}

IAM users should be assigned to IAM groups to enforce least privilege and simplify permission and lifecycle management. Users not placed in groups are harder to audit and more likely to receive excessive or inconsistent permissions. The `Groups` property on `AWS::IAM::User` resources must be defined and include at least one group name. Resources missing the `Groups` property or where `Groups` is empty will be flagged.

Secure example:

```yaml
MyUser:
  Type: AWS::IAM::User
  Properties:
    UserName: johndoe
    Groups:
      - Admins
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: A sample template
Resources:
  addUserToGroup2:
    Type: AWS::IAM::User
    Properties:
      Groups:
        - QAGroup
      LoginProfile:
          Password: myP@ssW0rd
      Path: "/"
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
      Tags:
        - QAUser
      UserName: TestUser
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "A sample template",
  "Resources": {
    "addUserToGroup2": {
      "Type": "AWS::IAM::User",
      "Properties": {
        "Groups": [
          "QAGroup"
        ],
        "LoginProfile": {
          "Password": "myP@ssW0rd"
        },
        "Path": "/",
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
                  "Effect": "Deny",
                  "Action": [
                    "sqs:*"
                  ],
                  "NotResource": [
                    "myqueue.Arn"
                  ]
                }
              ]
            }
          }
        ],
        "Tags": [
          "QAUser"
        ],
        "UserName": "TestUser"
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: A sample template
Resources:
    emptyGroup:
      Type: AWS::IAM::User
      Properties:
        Groups: []
        Path: "/"
        LoginProfile:
          Password: myP@ssW0rd
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
        Tags:
          - QAUser
        UserName: TestUser
```

```json
{
  "Resources": {
    "MyUser": {
      "Type": "AWS::IAM::User",
      "Properties": {
        "Policies": [
          {
            "PolicyName": "giveaccesstoqueueonly",
            "PolicyDocument": {
              "Version": "2012-10-17",
              "Statement": [
                {
                  "Action": [
                    "sqs:*"
                  ],
                  "Resource": [
                    "myqueue.Arn"
                  ],
                  "Effect": "Allow"
                },
                {
                  "Effect": "Deny",
                  "Action": [
                    "sqs:*"
                  ],
                  "NotResource": [
                    "myqueue.Arn"
                  ]
                }
              ]
            }
          }
        ],
        "Tags": [
          "QAUser"
        ],
        "UserName": "TestUser",
        "Path": "/",
        "LoginProfile": {
          "Password": "myP@ssW0rd"
        }
      }
    }
  },
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "A sample template"
}
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "A sample template",
  "Resources": {
    "emptyGroup": {
      "Type": "AWS::IAM::User",
      "Properties": {
        "Groups": [],
        "Path": "/",
        "LoginProfile": {
          "Password": "myP@ssW0rd"
        },
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
                  "Effect": "Deny",
                  "Action": [
                    "sqs:*"
                  ],
                  "NotResource": [
                    "myqueue.Arn"
                  ]
                }
              ]
            }
          }
        ],
        "Tags": [
          "QAUser"
        ],
        "UserName": "TestUser"
      }
    }
  }
}
```
