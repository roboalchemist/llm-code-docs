# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/cloudtrail_log_files_not_encrypted_with_kms.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/cloudtrail_log_files_not_encrypted_with_kms.md

---
title: CloudTrail log files not encrypted with KMS
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > CloudTrail log files not encrypted with KMS
---

# CloudTrail log files not encrypted with KMS

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `050a9ba8-d1cb-4c61-a5e8-8805a70d3b85`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Low

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-kmskeyid)

### Description{% #description %}

CloudTrail log files must be encrypted with an AWS KMS customer-managed key to protect the confidentiality and integrity of audit logs and enable key access control and rotation.

The CloudFormation resource type `AWS::CloudTrail::Trail` must define the `KMSKeyId` property with a non-empty value (AWS KMS key ARN, key ID, alias, or a reference to an `AWS::KMS::Key`). Resources missing `KMSKeyId` or with it set to `null` or an empty string will be flagged.

Create or reference a customer-managed AWS KMS key and assign it to `KMSKeyId` (using `!Ref`, `!GetAtt`, or an ARN) so CloudTrail delivers logs encrypted under that key.

Secure CloudFormation example:

```yaml
MyKmsKey:
  Type: AWS::KMS::Key
  Properties:
    Description: KMS key for CloudTrail log encryption

MyTrail:
  Type: AWS::CloudTrail::Trail
  Properties:
    IsLogging: true
    S3BucketName: my-trail-bucket
    KMSKeyId: !Ref MyKmsKey
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
      KMSKeyId: arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012
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
    "myTrail": {
      "DependsOn": [
        "BucketPolicy",
        "TopicPolicy"
      ],
      "Type": "AWS::CloudTrail::Trail",
      "Properties": {
        "KMSKeyId": "arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012",
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
      }
    },
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
              "Action": "s3:PutObject",
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
              }
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
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "myTrail": {
      "Type": "AWS::CloudTrail::Trail",
      "Properties": {
        "SnsTopicName": "",
        "IsLogging": false,
        "IsMultiRegionTrail": false,
        "KMSKeyId": "",
        "EnableLogFileValidation": false
      }
    }
  }
}
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
    "myTrail": {
      "DependsOn": [
        "BucketPolicy",
        "TopicPolicy"
      ],
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
      }
    },
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
        }
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
      IsMultiRegionTrail: true
```
