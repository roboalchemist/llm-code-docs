# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/s3_bucket_without_server_side_encryption.md

---
title: S3 bucket without server-side encryption
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > S3 bucket without server-side encryption
---

# S3 bucket without server-side encryption

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `b2e8752c-3497-4255-98d2-e4ae5b46bbf5`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/default-bucket-encryption.html)

### Description{% #description %}

S3 buckets should have server-side encryption enabled to protect data at rest from unauthorized access. Encryption also helps ensure objects remain encrypted if underlying storage media or backups are compromised.

In CloudFormation, `AWS::S3::Bucket` resources must define `Properties.BucketEncryption.ServerSideEncryptionConfiguration` as a non-empty list. Each entry should include `ServerSideEncryptionByDefault.SSEAlgorithm` set to `AES256` or `aws:kms`. If using `aws:kms`, also specify `ServerSideEncryptionByDefault.KMSMasterKeyID`. Resources missing this property, or with an empty `ServerSideEncryptionConfiguration`, will be flagged.

Secure configuration example:

```yaml
MyBucket:
  Type: AWS::S3::Bucket
  Properties:
    BucketEncryption:
      ServerSideEncryptionConfiguration:
        - ServerSideEncryptionByDefault:
            SSEAlgorithm: AES256
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
#this code is a correct code for which the query should not find any result
AWSTemplateFormatVersion: '2010-09-09'
Description: S3 bucket with default encryption
Resources:
  EncryptedS3Bucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      BucketName:
        'Fn::Sub': 'encryptedbucket-${AWS::Region}-${AWS::AccountId}'
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm: 'aws:kms'
              KMSMasterKeyID: KMS-KEY-ARN
    DeletionPolicy: Delete
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "S3 bucket with default encryption",
  "Resources": {
    "EncryptedS3Bucket": {
      "Type": "AWS::S3::Bucket",
      "Properties": {
        "BucketName": {
          "Fn::Sub": "encryptedbucket-${AWS::Region}-${AWS::AccountId}"
        },
        "BucketEncryption": {
          "ServerSideEncryptionConfiguration": [
            {
              "ServerSideEncryptionByDefault": {
                "SSEAlgorithm": "aws:kms",
                "KMSMasterKeyID": "KMS-KEY-ARN"
              }
            }
          ]
        }
      },
      "DeletionPolicy": "Delete"
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "Resources": {
    "S3Bucket": {
      "Type": "AWS::S3::Bucket",
      "Properties": {
        "BucketName": {
          "Fn::Sub": "bucket-${AWS::Region}-${AWS::AccountId}"
        }
      },
      "DeletionPolicy": "Delete"
    }
  },
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "S3 bucket without default encryption"
}
```

```yaml
#this is a problematic code where the query should report a result(s)
AWSTemplateFormatVersion: '2010-09-09'
Description: S3 bucket without default encryption
Resources:
  S3Bucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      BucketName:
        'Fn::Sub': 'bucket-${AWS::Region}-${AWS::AccountId}'
    DeletionPolicy: Delete
```
