# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/iam_policies_with_full_privileges.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/iam_policies_with_full_privileges.md

---
title: IAM policies with full privileges
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > IAM policies with full privileges
---

# IAM policies with full privileges

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `953b3cdb-ce13-428a-aa12-318726506661`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html)

### Description{% #description %}

IAM policy statements that allow `Action: '*'` on `Resource: '*'` grant full administrative privileges across the account and enable privilege escalation, data exfiltration, and account takeover. This rule checks `AWS::IAM::Policy` resources' `Properties.PolicyDocument.Statement` entries and flags statements where `Effect` is `Allow` and both `Action` and `Resource` are the wildcard `'*'` (either as a single string or contained in an array). Replace full wildcards with explicit action lists and scoped resource ARNs, or apply IAM condition keys to restrict the policy to the minimum required scope. Statements that do not include both wildcards will not be flagged.

Secure example limiting S3 access to a single bucket:

```yaml
MyS3Policy:
  Type: AWS::IAM::Policy
  Properties:
    PolicyName: ReadOnlyS3
    PolicyDocument:
      Version: '2012-10-17'
      Statement:
        - Effect: Allow
          Action:
            - s3:GetObject
            - s3:ListBucket
          Resource:
            - arn:aws:s3:::my-bucket
            - arn:aws:s3:::my-bucket/*
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: A sample template
Resources:
  MyPolicy:
    Type: AWS::IAM::Policy
    Properties:
      PolicyName: mygrouppolicy
      PolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Action:
              - s3:GetObject
              - s3:PutObject
              - s3:PutObjectAcl
            Resource: arn:aws:s3:::myAWSBucket/*
      Groups:
        - myexistinggroup1
        - !Ref mygroup
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "A sample template",
  "Resources": {
    "MyPolicy": {
      "Properties": {
        "PolicyName": "mygrouppolicy",
        "PolicyDocument": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:PutObjectAcl"
              ],
              "Resource": "arn:aws:s3:::myAWSBucket/*"
            }
          ]
        },
        "Groups": [
          "myexistinggroup1",
          "mygroup"
        ]
      },
      "Type": "AWS::IAM::Policy"
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
    },
    "mypolicy2": {
      "Type": "AWS::IAM::Policy",
      "Properties": {
        "PolicyName": "mygrouppolicy",
        "PolicyDocument": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Action": "*",
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
