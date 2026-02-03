# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/cloudtrail_multi_region_disabled.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/cloudtrail_multi_region_disabled.md

---
title: CloudTrail multi-region disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > CloudTrail multi-region disabled
---

# CloudTrail multi-region disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `058ac855-989f-4378-ba4d-52d004020da7`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Low

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-ismultiregiontrail)

### Description{% #description %}

CloudTrail must be configured as a multi-region trail to capture management events from all AWS regions and avoid auditing gaps if a single region is compromised. The `IsMultiRegionTrail` property in `AWS::CloudTrail::Trail` resources must be defined and set to `true`. Resources missing this property or with `IsMultiRegionTrail` set to `false` will be flagged.

Secure configuration example:

```yaml
MyTrail:
  Type: AWS::CloudTrail::Trail
  Properties:
    IsMultiRegionTrail: true
    S3BucketName: my-cloudtrail-bucket
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Parameters:
  OperatorEmail:
    Description: "Email address to notify when new logs are published."
    Type: String
Resources:
  S3Bucket:
    DeletionPolicy: Retain
    Type: AWS::S3::Bucket
    Properties: {}
  BucketPolicy:
    Type: AWS::S3::BucketPolicy
    Properties:
      Bucket:
        Ref: S3Bucket
      PolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Sid: "AWSCloudTrailAclCheck"
            Effect: "Allow"
            Principal:
              Service: "cloudtrail.amazonaws.com"
            Action: "s3:GetBucketAcl"
            Resource: !Sub |-
              arn:aws:s3:::${S3Bucket}
          - Sid: "AWSCloudTrailWrite"
            Effect: "Allow"
            Principal:
              Service: "cloudtrail.amazonaws.com"
            Action: "s3:PutObject"
            Resource: !Sub |-
              arn:aws:s3:::${S3Bucket}/AWSLogs/${AWS::AccountId}/*
            Condition:
              StringEquals:
                s3:x-amz-acl: "bucket-owner-full-control"
  Topic:
    Type: AWS::SNS::Topic
    Properties:
      Subscription:
        - Endpoint:
            Ref: OperatorEmail
          Protocol: email
  TopicPolicy:
    Type: AWS::SNS::TopicPolicy
    Properties:
      Topics:
        - Ref: "Topic"
      PolicyDocument:
        Version: "2008-10-17"
        Statement:
          - Sid: "AWSCloudTrailSNSPolicy"
            Effect: "Allow"
            Principal:
              Service: "cloudtrail.amazonaws.com"
            Resource: "*"
            Action: "SNS:Publish"
  myTrail:
    DependsOn:
      - BucketPolicy
      - TopicPolicy
    Type: AWS::CloudTrail::Trail
    Properties:
      S3BucketName:
        Ref: S3Bucket
      SnsTopicName:
        Fn::GetAtt:
          - Topic
          - TopicName
      IsLogging: true
      IsMultiRegionTrail: true
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Parameters": {
    "OperatorEmail": {
      "Description": "Email address to notify when new logs are published.",
      "Type": "String"
    }
  },
  "Resources": {
    "TopicPolicy": {
      "Type": "AWS::SNS::TopicPolicy",
      "Properties": {
        "Topics": [
          {
            "Ref": "Topic"
          }
        ],
        "PolicyDocument": {
          "Version": "2008-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Principal": {
                "Service": "cloudtrail.amazonaws.com"
              },
              "Resource": "*",
              "Action": "SNS:Publish",
              "Sid": "AWSCloudTrailSNSPolicy"
            }
          ]
        }
      }
    },
    "myTrail": {
      "Type": "AWS::CloudTrail::Trail",
      "Properties": {
        "S3BucketName": {
          "Ref": "S3Bucket"
        },
        "SnsTopicName": {
          "Fn::GetAtt": [
            "Topic",
            "TopicName"
          ]
        },
        "IsLogging": true,
        "IsMultiRegionTrail": true
      },
      "DependsOn": [
        "BucketPolicy",
        "TopicPolicy"
      ]
    },
    "S3Bucket": {
      "Properties": {},
      "DeletionPolicy": "Retain",
      "Type": "AWS::S3::Bucket"
    },
    "BucketPolicy": {
      "Properties": {
        "Bucket": {
          "Ref": "S3Bucket"
        },
        "PolicyDocument": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Principal": {
                "Service": "cloudtrail.amazonaws.com"
              },
              "Action": "s3:GetBucketAcl",
              "Resource": "arn:aws:s3:::${S3Bucket}",
              "Sid": "AWSCloudTrailAclCheck",
              "Effect": "Allow"
            },
            {
              "Effect": "Allow",
              "Principal": {
                "Service": "cloudtrail.amazonaws.com"
              },
              "Action": "s3:PutObject",
              "Resource": "arn:aws:s3:::${S3Bucket}/AWSLogs/${AWS::AccountId}/*",
              "Condition": {
                "StringEquals": {
                  "s3:x-amz-acl": "bucket-owner-full-control"
                }
              },
              "Sid": "AWSCloudTrailWrite"
            }
          ]
        }
      },
      "Type": "AWS::S3::BucketPolicy"
    },
    "Topic": {
      "Type": "AWS::SNS::Topic",
      "Properties": {
        "Subscription": [
          {
            "Endpoint": {
              "Ref": "OperatorEmail"
            },
            "Protocol": "email"
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
  "Parameters": {
    "OperatorEmail": {
      "Description": "Email address to notify when new logs are published.",
      "Type": "String"
    }
  },
  "Resources": {
    "myTrail": {
      "DependsOn": [
        "BucketPolicy",
        "TopicPolicy"
      ],
      "Type": "AWS::CloudTrail::Trail",
      "Properties": {
        "IsMultiRegionTrail": false,
        "S3BucketName": {
          "Ref": "S3Bucket"
        },
        "SnsTopicName": {
          "Fn::GetAtt": [
            "Topic",
            "TopicName"
          ]
        },
        "IsLogging": true
      }
    },
    "myTrail2": {
      "Type": "AWS::CloudTrail::Trail",
      "Properties": {
        "S3BucketName": {
          "Ref": "S3Bucket"
        },
        "SnsTopicName": {
          "Fn::GetAtt": [
            "Topic",
            "TopicName"
          ]
        },
        "IsLogging": true
      },
      "DependsOn": [
        "BucketPolicy",
        "TopicPolicy"
      ]
    },
    "S3Bucket": {
      "Properties": {},
      "DeletionPolicy": "Retain",
      "Type": "AWS::S3::Bucket"
    },
    "BucketPolicy": {
      "Type": "AWS::S3::BucketPolicy",
      "Properties": {
        "PolicyDocument": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Resource": "arn:aws:s3:::${S3Bucket}",
              "Sid": "AWSCloudTrailAclCheck",
              "Effect": "Allow",
              "Principal": {
                "Service": "cloudtrail.amazonaws.com"
              },
              "Action": "s3:GetBucketAcl"
            },
            {
              "Sid": "AWSCloudTrailWrite",
              "Effect": "Allow",
              "Principal": {
                "Service": "cloudtrail.amazonaws.com"
              },
              "Action": "s3:PutObject",
              "Resource": "arn:aws:s3:::${S3Bucket}/AWSLogs/${AWS::AccountId}/*",
              "Condition": {
                "StringEquals": {
                  "s3:x-amz-acl": "bucket-owner-full-control"
                }
              }
            }
          ]
        },
        "Bucket": {
          "Ref": "S3Bucket"
        }
      }
    },
    "Topic": {
      "Type": "AWS::SNS::Topic",
      "Properties": {
        "Subscription": [
          {
            "Endpoint": {
              "Ref": "OperatorEmail"
            },
            "Protocol": "email"
          }
        ]
      }
    },
    "TopicPolicy": {
      "Type": "AWS::SNS::TopicPolicy",
      "Properties": {
        "PolicyDocument": {
          "Version": "2008-10-17",
          "Statement": [
            {
              "Principal": {
                "Service": "cloudtrail.amazonaws.com"
              },
              "Resource": "*",
              "Action": "SNS:Publish",
              "Sid": "AWSCloudTrailSNSPolicy",
              "Effect": "Allow"
            }
          ]
        },
        "Topics": [
          {
            "Ref": "Topic"
          }
        ]
      }
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Parameters:
  OperatorEmail:
    Description: "Email address to notify when new logs are published."
    Type: String
Resources:
  S3Bucket:
    DeletionPolicy: Retain
    Type: AWS::S3::Bucket
    Properties: {}
  BucketPolicy:
    Type: AWS::S3::BucketPolicy
    Properties:
      Bucket:
        Ref: S3Bucket
      PolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Sid: "AWSCloudTrailAclCheck"
            Effect: "Allow"
            Principal:
              Service: "cloudtrail.amazonaws.com"
            Action: "s3:GetBucketAcl"
            Resource: !Sub |-
              arn:aws:s3:::${S3Bucket}
          - Sid: "AWSCloudTrailWrite"
            Effect: "Allow"
            Principal:
              Service: "cloudtrail.amazonaws.com"
            Action: "s3:PutObject"
            Resource: !Sub |-
              arn:aws:s3:::${S3Bucket}/AWSLogs/${AWS::AccountId}/*
            Condition:
              StringEquals:
                s3:x-amz-acl: "bucket-owner-full-control"
  Topic:
    Type: AWS::SNS::Topic
    Properties:
      Subscription:
        - Endpoint:
            Ref: OperatorEmail
          Protocol: email
  TopicPolicy:
    Type: AWS::SNS::TopicPolicy
    Properties:
      Topics:
        - Ref: "Topic"
      PolicyDocument:
        Version: "2008-10-17"
        Statement:
          - Sid: "AWSCloudTrailSNSPolicy"
            Effect: "Allow"
            Principal:
              Service: "cloudtrail.amazonaws.com"
            Resource: "*"
            Action: "SNS:Publish"
  myTrail:
    DependsOn:
      - BucketPolicy
      - TopicPolicy
    Type: AWS::CloudTrail::Trail
    Properties:
      S3BucketName:
        Ref: S3Bucket
      SnsTopicName:
        Fn::GetAtt:
          - Topic
          - TopicName
      IsLogging: true
      IsMultiRegionTrail: false
  myTrail2:
    DependsOn:
      - BucketPolicy
      - TopicPolicy
    Type: AWS::CloudTrail::Trail
    Properties:
      S3BucketName:
        Ref: S3Bucket
      SnsTopicName:
        Fn::GetAtt:
          - Topic
          - TopicName
      IsLogging: true
```
