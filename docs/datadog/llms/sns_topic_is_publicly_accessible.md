# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/sns_topic_is_publicly_accessible.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/sns_topic_is_publicly_accessible.md

---
title: SNS topic is publicly accessible
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > SNS topic is publicly accessible
---

# SNS topic is publicly accessible

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `ae53ce91-42b5-46bf-a84f-9a13366a4f13`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Critical

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html)

### Description{% #description %}

SNS topic policies must not grant `Allow` permissions to all principals because that effectively makes the topic public. This can allow unauthenticated users or arbitrary AWS accounts to publish to or subscribe from the topic, risking data exposure, spam, and abuse.

Check `AWS::SNS::TopicPolicy` resources' `Properties.PolicyDocument.Statement` entries. Any statement with `Effect: "Allow"` and `Principal: "*"`, or `Principal.AWS: "*"`, will be flagged.

To remediate, require explicit principals such as AWS account ARNs or service principals, or use scoped conditions for cross-account access rather than wildcard principals. Statements that list wildcard principals, or omit principal restrictions, should be corrected.

Secure configuration example (CloudFormation YAML):

```yaml
MyTopicPolicy:
  Type: AWS::SNS::TopicPolicy
  Properties:
    Topics:
      - !Ref MyTopic
    PolicyDocument:
      Version: '2012-10-17'
      Statement:
        - Effect: Allow
          Principal:
            AWS: arn:aws:iam::123456789012:root
          Action:
            - sns:Publish
          Resource: !Ref MyTopic
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: ''
Resources:
  snsPolicy:
      Type: AWS::SNS::TopicPolicy
      Properties:
        PolicyDocument:
          Statement: [
            {
              "Sid": "MyTopicPolicy",
              "Effect": "Allow",
              "Principal": "otherPrincipal",
              "Action": ["sns:Publish"],
              "Resource": "arn:aws:sns:MyTopic"
            }]
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "",
  "Resources": {
    "mysnspolicy0" : {
      "Type" : "AWS::SNS::TopicPolicy",
      "Properties" : {
        "PolicyDocument" :  {
          "Id" : "MyTopicPolicy",
          "Version" : "2012-10-17",
          "Statement" : [ {
            "Sid" : "My-statement-id",
            "Effect" : "Allow",
            "Principal" : "otherPrincipal",
            "Action" : "sns:Publish",
            "Resource" : "*"
          } ]
        },
        "Topics" : [ { "Ref" : "MySNSTopic" } ]
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "",
  "Resources": {
    "mysnspolicy0" : {
      "Type" : "AWS::SNS::TopicPolicy",
      "Properties" : {
        "PolicyDocument" :  {
          "Id" : "MyTopicPolicy",
          "Version" : "2012-10-17",
          "Statement" : [ {
            "Sid" : "My-statement-id",
            "Effect" : "Allow",
            "Principal" : "*",
            "Action" : "sns:Publish",
            "Resource" : "*"
          } ]
        },
        "Topics" : [ { "Ref" : "MySNSTopic" } ]
      }
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: ''
Resources:
  snsPolicy:
      Type: AWS::SNS::TopicPolicy
      Properties:
        PolicyDocument:
          Statement: [
            {
              "Sid": "MyTopicPolicy",
              "Effect": "Allow",
              "Principal": "*",
              "Action": ["sns:Publish"],
              "Resource": "arn:aws:sns:MyTopic"
            }]
```
