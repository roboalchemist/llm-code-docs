# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/cloudtrail_logging_disabled.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/cloudtrail_logging_disabled.md

---
title: CloudTrail logging disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > CloudTrail logging disabled
---

# CloudTrail logging disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `5c0b06d5-b7a4-484c-aeb0-75a836269ff0`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-islogging)

### Description{% #description %}

CloudTrail must have logging enabled to provide an audit trail of API activity. Without logging, you cannot reliably detect unauthorized actions, investigate incidents, or meet audit and compliance requirements. The `IsLogging` property on `AWS::CloudTrail::Trail` resources must be defined and set to `true`. Resources missing `IsLogging` or with `IsLogging` set to `false` will be flagged.

Secure configuration example:

```yaml
MyTrail:
  Type: AWS::CloudTrail::Trail
  Properties:
    IsLogging: true
    S3BucketName: my-trail-bucket
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
      EnableLogFileValidation: true
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
      "Type": "String",
      "Description": "Email address to notify when new logs are published."
    }
  },
  "Resources": {
    "BucketPolicy": {
      "Type": "AWS::S3::BucketPolicy",
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
        "Topics": [
          {
            "Ref": "Topic"
          }
        ],
        "PolicyDocument": {
          "Version": "2008-10-17",
          "Statement": [
            {
              "Sid": "AWSCloudTrailSNSPolicy",
              "Effect": "Allow",
              "Principal": {
                "Service": "cloudtrail.amazonaws.com"
              },
              "Resource": "*",
              "Action": "SNS:Publish"
            }
          ]
        }
      }
    },
    "myTrail2": {
      "DependsOn": [
        "BucketPolicy",
        "TopicPolicy"
      ],
      "Type": "AWS::CloudTrail::Trail",
      "Properties": {
        "IsLogging": true,
        "IsMultiRegionTrail": true,
        "EnableLogFileValidation": true,
        "S3BucketName": {
          "Ref": "S3Bucket"
        },
        "SnsTopicName": {
          "Fn::GetAtt": [
            "Topic",
            "TopicName"
          ]
        }
      }
    },
    "S3Bucket": {
      "DeletionPolicy": "Retain",
      "Type": "AWS::S3::Bucket",
      "Properties": {}
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "Resources": {
    "S3Bucket": {
      "DeletionPolicy": "Retain",
      "Type": "AWS::S3::Bucket",
      "Properties": {}
    },
    "BucketPolicy": {
      "Type": "AWS::S3::BucketPolicy",
      "Properties": {
        "Bucket": {
          "Ref": "S3Bucket"
        },
        "PolicyDocument": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Sid": "AWSCloudTrailAclCheck",
              "Effect": "Allow",
              "Principal": {
                "Service": "cloudtrail.amazonaws.com"
              },
              "Action": "s3:GetBucketAcl",
              "Resource": "arn:aws:s3:::${S3Bucket}"
            },
            {
              "Resource": "arn:aws:s3:::${S3Bucket}/AWSLogs/${AWS::AccountId}/*",
              "Condition": {
                "StringEquals": {
                  "s3:x-amz-acl": "bucket-owner-full-control"
                }
              },
              "Sid": "AWSCloudTrailWrite",
              "Effect": "Allow",
              "Principal": {
                "Service": "cloudtrail.amazonaws.com"
              },
              "Action": "s3:PutObject"
            }
          ]
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
              "Sid": "AWSCloudTrailSNSPolicy",
              "Effect": "Allow",
              "Principal": {
                "Service": "cloudtrail.amazonaws.com"
              },
              "Resource": "*",
              "Action": "SNS:Publish"
            }
          ]
        }
      },
      "Type": "AWS::SNS::TopicPolicy"
    },
    "myTrail5": {
      "DependsOn": [
        "BucketPolicy",
        "TopicPolicy"
      ],
      "Type": "AWS::CloudTrail::Trail",
      "Properties": {
        "IsMultiRegionTrail": true,
        "S3BucketName": {
          "Ref": "S3Bucket"
        },
        "SnsTopicName": {
          "Fn::GetAtt": [
            "Topic",
            "TopicName"
          ]
        },
        "IsLogging": false
      }
    },
    "myTrail6": {
      "DependsOn": [
        "BucketPolicy",
        "TopicPolicy"
      ],
      "Type": "AWS::CloudTrail::Trail",
      "Properties": {
        "EnableLogFileValidation": false,
        "S3BucketName": {
          "Ref": "S3Bucket"
        },
        "SnsTopicName": {
          "Fn::GetAtt": [
            "Topic",
            "TopicName"
          ]
        },
        "IsLogging": false,
        "IsMultiRegionTrail": true
      }
    }
  },
  "AWSTemplateFormatVersion": "2010-09-09",
  "Parameters": {
    "OperatorEmail": {
      "Description": "Email address to notify when new logs are published.",
      "Type": "String"
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
  myTrail3:
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
      IsLogging: false
      IsMultiRegionTrail: true
  myTrail4:
    DependsOn:
      - BucketPolicy
      - TopicPolicy
    Type: AWS::CloudTrail::Trail
    Properties:
      EnableLogFileValidation: false
      S3BucketName:
        Ref: S3Bucket
      SnsTopicName:
        Fn::GetAtt:
          - Topic
          - TopicName
      IsLogging: false
      IsMultiRegionTrail: true
```
