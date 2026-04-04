# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/s3_bucket_logging_disabled.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/s3_bucket_logging_disabled.md

---
title: S3 bucket logging disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > S3 bucket logging disabled
---

# S3 bucket logging disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `4552b71f-0a2a-4bc4-92dd-ed7ec1b4674c`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#cfn-s3-bucket-loggingconfig)

### Description{% #description %}

S3 buckets should have server access logging enabled to create an audit trail of requests and changes. This helps detect unauthorized access or data exfiltration and supports forensic analysis and compliance.

In CloudFormation, `AWS::S3::Bucket` resources must include the `LoggingConfiguration` property with a valid `DestinationBucketName` (and optional `LogFilePrefix`) pointing to the bucket that will receive access logs. Resources missing `LoggingConfiguration` will be flagged. Ensure the destination bucket exists, is appropriately restricted for log retention, and permits S3 log delivery to prevent log loss or tampering.

Secure configuration example:

```yaml
MyBucket:
  Type: AWS::S3::Bucket
  Properties:
    BucketName: my-source-bucket
    LoggingConfiguration:
      DestinationBucketName: my-logs-bucket
      LogFilePrefix: access-logs/
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: A sample template
Resources:
  RecordServiceS3Bucket:
    Type: "AWS::S3::Bucket"
    DeletionPolicy: Retain
    Properties:
      ReplicationConfiguration:
        Role:
          "Fn::GetAtt":
            - WorkItemBucketBackupRole
            - Arn
        Rules:
          - Destination:
              Bucket:
                "Fn::Join":
                  - ""
                  - - "arn:aws:s3:::"
                    - "Fn::Join":
                        - "-"
                        - - Ref: "AWS::Region"
                          - Ref: "AWS::StackName"
                          - replicationbucket
              StorageClass: STANDARD
            Id: Backup
            Prefix: ""
            Status: Enabled
      VersioningConfiguration:
        Status: Enabled
      LoggingConfiguration:
        DestinationBucketName: !Ref LoggingBucket
        LogFilePrefix: loga/
  WorkItemBucketBackupRole:
    Type: "AWS::IAM::Role"
    Properties:
      AssumeRolePolicyDocument:
        Statement:
          - Action:
              - "sts:AssumeRole"
            Effect: Allow
            Principal:
              Service:
                - s3.amazonaws.com
  BucketBackupPolicy:
    Type: "AWS::IAM::Policy"
    Properties:
      PolicyDocument:
        Statement:
          - Action:
              - "s3:GetReplicationConfiguration"
              - "s3:ListBucket"
            Effect: Allow
            Resource:
              - "Fn::Join":
                  - ""
                  - - "arn:aws:s3:::"
                    - Ref: RecordServiceS3Bucket
          - Action:
              - "s3:GetObjectVersion"
              - "s3:GetObjectVersionAcl"
            Effect: Allow
            Resource:
              - "Fn::Join":
                  - ""
                  - - "arn:aws:s3:::"
                    - Ref: RecordServiceS3Bucket
                    - /*
          - Action:
              - "s3:ReplicateObject"
              - "s3:ReplicateDelete"
            Effect: Allow
            Resource:
              - "Fn::Join":
                  - ""
                  - - "arn:aws:s3:::"
                    - "Fn::Join":
                        - "-"
                        - - Ref: "AWS::Region"
                          - Ref: "AWS::StackName"
                          - replicationbucket
                    - /*
      PolicyName: BucketBackupPolicy
      Roles:
        - Ref: WorkItemBucketBackupRole
```

```json
{
  "Resources": {
    "RecordServiceS3Bucket": {
      "Properties": {
        "ReplicationConfiguration": {
          "Role": {
            "Fn::GetAtt": [
              "WorkItemBucketBackupRole",
              "Arn"
            ]
          },
          "Rules": [
            {
              "Status": "Enabled",
              "Destination": {
                "Bucket": {
                  "Fn::Join": [
                    "",
                    [
                      "arn:aws:s3:::",
                      {
                        "Fn::Join": [
                          "-",
                          [
                            {
                              "Ref": "AWS::Region"
                            },
                            {
                              "Ref": "AWS::StackName"
                            },
                            "replicationbucket"
                          ]
                        ]
                      }
                    ]
                  ]
                },
                "StorageClass": "STANDARD"
              },
              "Id": "Backup",
              "Prefix": ""
            }
          ]
        },
        "VersioningConfiguration": {
          "Status": "Enabled"
        },
        "LoggingConfiguration": {
          "DestinationBucketName": "LoggingBucket",
          "LogFilePrefix": "loga/"
        }
      },
      "Type": "AWS::S3::Bucket",
      "DeletionPolicy": "Retain"
    },
    "WorkItemBucketBackupRole": {
      "Type": "AWS::IAM::Role",
      "Properties": {
        "AssumeRolePolicyDocument": {
          "Statement": [
            {
              "Principal": {
                "Service": [
                  "s3.amazonaws.com"
                ]
              },
              "Action": [
                "sts:AssumeRole"
              ],
              "Effect": "Allow"
            }
          ]
        }
      }
    },
    "BucketBackupPolicy": {
      "Type": "AWS::IAM::Policy",
      "Properties": {
        "PolicyDocument": {
          "Statement": [
            {
              "Action": [
                "s3:GetReplicationConfiguration",
                "s3:ListBucket"
              ],
              "Effect": "Allow",
              "Resource": [
                {
                  "Fn::Join": [
                    "",
                    [
                      "arn:aws:s3:::",
                      {
                        "Ref": "RecordServiceS3Bucket"
                      }
                    ]
                  ]
                }
              ]
            },
            {
              "Action": [
                "s3:GetObjectVersion",
                "s3:GetObjectVersionAcl"
              ],
              "Effect": "Allow",
              "Resource": [
                {
                  "Fn::Join": [
                    "",
                    [
                      "arn:aws:s3:::",
                      {
                        "Ref": "RecordServiceS3Bucket"
                      },
                      "/*"
                    ]
                  ]
                }
              ]
            },
            {
              "Action": [
                "s3:ReplicateObject",
                "s3:ReplicateDelete"
              ],
              "Effect": "Allow",
              "Resource": [
                {
                  "Fn::Join": [
                    "",
                    [
                      "arn:aws:s3:::",
                      {
                        "Fn::Join": [
                          "-",
                          [
                            {
                              "Ref": "AWS::Region"
                            },
                            {
                              "Ref": "AWS::StackName"
                            },
                            "replicationbucket"
                          ]
                        ]
                      },
                      "/*"
                    ]
                  ]
                }
              ]
            }
          ]
        },
        "PolicyName": "BucketBackupPolicy",
        "Roles": [
          {
            "Ref": "WorkItemBucketBackupRole"
          }
        ]
      }
    }
  },
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "A sample template"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "Description": "A sample template",
  "Resources": {
    "WorkItemBucketBackupRole": {
      "Type": "AWS::IAM::Role",
      "Properties": {
        "AssumeRolePolicyDocument": {
          "Statement": [
            {
              "Action": [
                "sts:AssumeRole"
              ],
              "Effect": "Allow",
              "Principal": {
                "Service": [
                  "s3.amazonaws.com"
                ]
              }
            }
          ]
        }
      }
    },
    "BucketBackupPolicy": {
      "Type": "AWS::IAM::Policy",
      "Properties": {
        "PolicyDocument": {
          "Statement": [
            {
              "Resource": [
                {
                  "Fn::Join": [
                    "",
                    [
                      "arn:aws:s3:::",
                      {
                        "Ref": "RecordServiceS3Bucket"
                      }
                    ]
                  ]
                }
              ],
              "Action": [
                "s3:GetReplicationConfiguration",
                "s3:ListBucket"
              ],
              "Effect": "Allow"
            },
            {
              "Action": [
                "s3:GetObjectVersion",
                "s3:GetObjectVersionAcl"
              ],
              "Effect": "Allow",
              "Resource": [
                {
                  "Fn::Join": [
                    "",
                    [
                      "arn:aws:s3:::",
                      {
                        "Ref": "RecordServiceS3Bucket"
                      },
                      "/*"
                    ]
                  ]
                }
              ]
            },
            {
              "Action": [
                "s3:ReplicateObject",
                "s3:ReplicateDelete"
              ],
              "Effect": "Allow",
              "Resource": [
                {
                  "Fn::Join": [
                    "",
                    [
                      "arn:aws:s3:::",
                      {
                        "Fn::Join": [
                          "-",
                          [
                            {
                              "Ref": "AWS::Region"
                            },
                            {
                              "Ref": "AWS::StackName"
                            },
                            "replicationbucket"
                          ]
                        ]
                      },
                      "/*"
                    ]
                  ]
                }
              ]
            }
          ]
        },
        "PolicyName": "BucketBackupPolicy",
        "Roles": [
          {
            "Ref": "WorkItemBucketBackupRole"
          }
        ]
      }
    },
    "mybucket": {
      "Properties": {
        "ReplicationConfiguration": {
          "Role": {
            "Fn::GetAtt": [
              "WorkItemBucketBackupRole",
              "Arn"
            ]
          },
          "Rules": [
            {
              "Prefix": "",
              "Status": "Enabled",
              "Destination": {
                "Bucket": {
                  "Fn::Join": [
                    "",
                    [
                      "arn:aws:s3:::",
                      {
                        "Fn::Join": [
                          "-",
                          [
                            {
                              "Ref": "AWS::Region"
                            },
                            {
                              "Ref": "AWS::StackName"
                            },
                            "replicationbucket"
                          ]
                        ]
                      }
                    ]
                  ]
                },
                "StorageClass": "STANDARD"
              },
              "Id": "Backup"
            }
          ]
        },
        "VersioningConfiguration": {
          "Status": "Enabled"
        }
      },
      "Type": "AWS::S3::Bucket",
      "DeletionPolicy": "Retain"
    }
  },
  "AWSTemplateFormatVersion": "2010-09-09"
}
```

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: A sample template
Resources:
  mybucket:
    Type: "AWS::S3::Bucket"
    DeletionPolicy: Retain
    Properties:
      ReplicationConfiguration:
        Role:
          "Fn::GetAtt":
            - WorkItemBucketBackupRole
            - Arn
        Rules:
          - Destination:
              Bucket:
                "Fn::Join":
                  - ""
                  - - "arn:aws:s3:::"
                    - "Fn::Join":
                        - "-"
                        - - Ref: "AWS::Region"
                          - Ref: "AWS::StackName"
                          - replicationbucket
              StorageClass: STANDARD
            Id: Backup
            Prefix: ""
            Status: Enabled
      VersioningConfiguration:
        Status: Enabled
  WorkItemBucketBackupRole:
    Type: "AWS::IAM::Role"
    Properties:
      AssumeRolePolicyDocument:
        Statement:
          - Action:
              - "sts:AssumeRole"
            Effect: Allow
            Principal:
              Service:
                - s3.amazonaws.com
  BucketBackupPolicy:
    Type: "AWS::IAM::Policy"
    Properties:
      PolicyDocument:
        Statement:
          - Action:
              - "s3:GetReplicationConfiguration"
              - "s3:ListBucket"
            Effect: Allow
            Resource:
              - "Fn::Join":
                  - ""
                  - - "arn:aws:s3:::"
                    - Ref: RecordServiceS3Bucket
          - Action:
              - "s3:GetObjectVersion"
              - "s3:GetObjectVersionAcl"
            Effect: Allow
            Resource:
              - "Fn::Join":
                  - ""
                  - - "arn:aws:s3:::"
                    - Ref: RecordServiceS3Bucket
                    - /*
          - Action:
              - "s3:ReplicateObject"
              - "s3:ReplicateDelete"
            Effect: Allow
            Resource:
              - "Fn::Join":
                  - ""
                  - - "arn:aws:s3:::"
                    - "Fn::Join":
                        - "-"
                        - - Ref: "AWS::Region"
                          - Ref: "AWS::StackName"
                          - replicationbucket
                    - /*
      PolicyName: BucketBackupPolicy
      Roles:
        - Ref: WorkItemBucketBackupRole
```
