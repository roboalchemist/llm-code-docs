# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/sns_topic_publicity_has_allow_and_not_action_simultaneously.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/sns_topic_publicity_has_allow_and_not_action_simultaneously.md

---
title: SNS topic publicity has Allow and NotAction simultaneously
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > SNS topic publicity has Allow and NotAction
  simultaneously
---

# SNS topic publicity has Allow and NotAction simultaneously

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `818f38ed-8446-4132-9c03-474d49e10195`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-iam.html#scenario-sns-policy)

### Description{% #description %}

SNS topic policy statements must not combine `Effect: "Allow"` with a `NotAction` element. Using `NotAction` with `Allow` effectively permits all actions except the ones excluded and can unintentionally grant broad access to the topic.

Check `AWS::SNS::TopicPolicy` resources' `Properties.PolicyDocument.Statement` entries. Any statement with `Effect: "Allow"` must include an explicit `Action` (for example, `sns:Publish`) rather than `NotAction`. Resources containing a statement where `Effect: "Allow"` and `NotAction` is present will be flagged. To block specific actions, use `Effect: "Deny"` with `NotAction`, or enumerate allowed actions explicitly in `Action`.

Secure configuration with explicit Action:

```yaml
MyTopicPolicy:
  Type: AWS::SNS::TopicPolicy
  Properties:
    PolicyDocument:
      Version: '2012-10-17'
      Statement:
        - Effect: Allow
          Principal:
            AWS: arn:aws:iam::123456789012:root
          Action:
            - sns:Publish
          Resource: arn:aws:sns:us-east-1:123456789012:my-topic
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: 2010-09-09
Description: A sample template
Resources:
  mysnspolicy:
    Type: AWS::SNS::TopicPolicy
    Properties:
      PolicyDocument:
        Id: MyTopicPolicy
        Version: '2012-10-17'
        Statement:
        - Sid: Mystatementid
          Effect: Allow
          Principal:
            AWS: !GetAtt myuser.Arn
          Action: sns:Publish
          Resource: "*"
      Topics:
      - !Ref mytopic
```

```json
{
  "Resources": {
    "mysnspolicy": {
      "Type": "AWS::SNS::TopicPolicy",
      "Properties": {
        "PolicyDocument": {
          "Id": "MyTopicPolicy",
          "Version": "2012-10-17",
          "Statement": [
            {
              "Sid": "Mystatementid",
              "Effect": "Allow",
              "Principal": {
                "AWS": "myuser.Arn"
              },
              "Action": "sns:Publish",
              "Resource": "*"
            }
          ]
        },
        "Topics": [
          "mytopic"
        ]
      }
    }
  },
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Description": "A sample template"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Description": "A sample template",
  "Resources": {
    "mysnspolicy": {
      "Type": "AWS::SNS::TopicPolicy",
      "Properties": {
        "PolicyDocument": {
          "Id": "MyTopicPolicy",
          "Version": "2012-10-17",
          "Statement": [
            {
              "NotAction": "s3:DeleteBucket",
              "Resource": "arn:aws:s3:::*",
              "Sid": "MyStatementId",
              "Effect": "Allow"
            },
            {
              "Sid": "MyStatementId2",
              "Effect": "Allow",
              "NotAction": "iam:*",
              "Resource": "*"
            }
          ]
        },
        "Topics": [
          "mytopic"
        ]
      }
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: 2010-09-09
Description: A sample template
Resources:
  mysnspolicy:
    Type: AWS::SNS::TopicPolicy
    Properties:
      PolicyDocument:
        Id: MyTopicPolicy
        Version: '2012-10-17'
        Statement:
        - Sid: MyStatementId
          Effect: Allow
          NotAction: "s3:DeleteBucket"
          Resource: "arn:aws:s3:::*"
        - Sid: MyStatementId2
          Effect: Allow
          NotAction: "iam:*"
          Resource: "*"
      Topics:
      - !Ref mytopic
```
