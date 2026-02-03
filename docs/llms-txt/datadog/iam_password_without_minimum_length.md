# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/iam_password_without_minimum_length.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/iam_password_without_minimum_length.md

---
title: IAM password without minimum length
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > IAM password without minimum length
---

# IAM password without minimum length

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `b1b20ae3-8fa7-4af5-a74d-a2145920fcb1`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Low

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-iam.html#scenario-iam-user)

### Description{% #description %}

IAM user console passwords defined in AWS CloudFormation should be strong to reduce the risk of account compromise through brute force, credential stuffing, or simple credential reuse. For `AWS::IAM::User` resources, `Properties.LoginProfile.Password` must be a string with a minimum length of `14` characters. Passwords shorter than `14` characters will be flagged unless they reference a secret via an AWS Secrets Manager dynamic reference. Avoid embedding plaintext passwords in templates. Instead, reference secrets stored in AWS Secrets Manager or SSM Parameter Store, or rely on IAM-managed workflows and password policies.

Secure example with a sufficiently long password (or a secret reference) in CloudFormation:

```yaml
MyUser:
  Type: AWS::IAM::User
  Properties:
    UserName: example-user
    LoginProfile:
      Password: "S3cureP@ssw0rd2025"
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
        Password: myP@ssW0rd123asw
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
      - PolicyName: giveaccesstotopiconly
        PolicyDocument:
          Version: '2012-10-17'
          Statement:
          - Effect: Allow
            Action:
            - sns:*
            Resource:
            - !Ref mytopic
          - Effect: Deny
            Action:
            - sns:*
            NotResource:
            - !Ref mytopic
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
          "Password": "myP@ssW0rd123asw"
        },
        "Policies": [
          {
            "PolicyName": "giveaccesstoqueueonly",
            "PolicyDocument": {
              "Version": "2012-10-17",
              "Statement": [
                {
                  "Resource": [
                    "myqueue.Arn"
                  ],
                  "Effect": "Allow",
                  "Action": [
                    "sqs:*"
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
          },
          {
            "PolicyName": "giveaccesstotopiconly",
            "PolicyDocument": {
              "Version": "2012-10-17",
              "Statement": [
                {
                  "Effect": "Allow",
                  "Action": [
                    "sns:*"
                  ],
                  "Resource": [
                    "mytopic"
                  ]
                },
                {
                  "Action": [
                    "sns:*"
                  ],
                  "NotResource": [
                    "mytopic"
                  ],
                  "Effect": "Deny"
                }
              ]
            }
          }
        ]
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

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
          },
          {
            "PolicyName": "giveaccesstotopiconly",
            "PolicyDocument": {
              "Version": "2012-10-17",
              "Statement": [
                {
                  "Effect": "Allow",
                  "Action": [
                    "sns:*"
                  ],
                  "Resource": [
                    "mytopic"
                  ]
                },
                {
                  "Effect": "Deny",
                  "Action": [
                    "sns:*"
                  ],
                  "NotResource": [
                    "mytopic"
                  ]
                }
              ]
            }
          }
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
  myuser:
    Type: AWS::IAM::User
    Properties:
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
      - PolicyName: giveaccesstotopiconly
        PolicyDocument:
          Version: '2012-10-17'
          Statement:
          - Effect: Allow
            Action:
            - sns:*
            Resource:
            - !Ref mytopic
          - Effect: Deny
            Action:
            - sns:*
            NotResource:
            - !Ref mytopic
```
