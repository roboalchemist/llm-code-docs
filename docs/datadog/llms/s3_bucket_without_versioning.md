# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/s3_bucket_without_versioning.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/s3_bucket_without_versioning.md

---
title: S3 bucket without versioning
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > S3 bucket without versioning
---

# S3 bucket without versioning

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `a227ec01-f97a-4084-91a4-47b350c1db54`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Backup

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html)

### Description{% #description %}

S3 buckets should have object versioning enabled to protect data from accidental or malicious deletion. Versioning also preserves prior object states for recovery and auditing.

In CloudFormation, `AWS::S3::Bucket` resources must include `Properties.VersioningConfiguration.Status` set to `Enabled`. Resources that omit `VersioningConfiguration`, or have `VersioningConfiguration.Status` set to `Suspended`, will be flagged.

Secure configuration example:

```yaml
MyBucket:
  Type: AWS::S3::Bucket
  Properties:
    BucketName: my-bucket
    VersioningConfiguration:
      Status: Enabled
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
Resources:
  RecordServiceS3Bucket:
    Type: 'AWS::S3::Bucket'
    DeletionPolicy: Retain
    Properties:
      ReplicationConfiguration:
        Role:
          'Fn::GetAtt':
            - WorkItemBucketBackupRole
            - Arn
        Rules:
          - Destination:
              Bucket:
                'Fn::Join':
                  - ''
                  - - 'arn:aws:s3:::'
                    - 'Fn::Join':
                        - '-'
                        - - Ref: 'AWS::Region'
                          - Ref: 'AWS::StackName'
                          - replicationbucket
              StorageClass: STANDARD
            Id: Backup
            Prefix: ''
            Status: Enabled
      VersioningConfiguration:
        Status: Enabled
```

```json
{
  "Resources": {
    "RecordServiceS3Bucket": {
      "Type": "AWS::S3::Bucket",
      "DeletionPolicy": "Retain",
      "Properties": {
        "ReplicationConfiguration": {
          "Rules": [
            {
              "Id": "Backup",
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
              }
            }
          ],
          "Role": {
            "Fn::GetAtt": [
              "WorkItemBucketBackupRole",
              "Arn"
            ]
          }
        },
        "VersioningConfiguration": {
          "Status": "Enabled"
        }
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
Resources:
  RecordServiceS3Bucket2:
    Type: 'AWS::S3::Bucket'
    DeletionPolicy: Retain
    Properties:
      ReplicationConfiguration:
        Role:
          'Fn::GetAtt':
            - WorkItemBucketBackupRole
            - Arn
        Rules:
          - Destination:
              Bucket:
                'Fn::Join':
                  - ''
                  - - 'arn:aws:s3:::'
                    - 'Fn::Join':
                        - '-'
                        - - Ref: 'AWS::Region'
                          - Ref: 'AWS::StackName'
                          - replicationbucket
              StorageClass: STANDARD
            Id: Backup
            Prefix: ''
            Status: Enabled
      VersioningConfiguration:
        Status: Suspended
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
              "Id": "Backup",
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
              }
            }
          ]
        }
      },
      "Type": "AWS::S3::Bucket",
      "DeletionPolicy": "Retain"
    }
  }
}
```

```json
{
  "Resources": {
    "RecordServiceS3Bucket2": {
      "Type": "AWS::S3::Bucket",
      "DeletionPolicy": "Retain",
      "Properties": {
        "ReplicationConfiguration": {
          "Rules": [
            {
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
              "Prefix": "",
              "Status": "Enabled"
            }
          ],
          "Role": {
            "Fn::GetAtt": [
              "WorkItemBucketBackupRole",
              "Arn"
            ]
          }
        },
        "VersioningConfiguration": {
          "Status": "Suspended"
        }
      }
    }
  }
}
```
