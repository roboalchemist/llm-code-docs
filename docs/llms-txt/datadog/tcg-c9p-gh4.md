# Source: https://docs.datadoghq.com/security/default_rules/tcg-c9p-gh4.md

---
title: Default encryption should be enabled on S3 buckets
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Default encryption should be enabled on
  S3 buckets
---

# Default encryption should be enabled on S3 buckets
 
## Description{% #description %}

Amazon S3 provides a variety of no-cost or low-cost encryption options to protect data at rest.

## Rationale{% #rationale %}

Encrypting data at rest reduces the likelihood that it is unintentionally exposed and can nullify the impact of disclosure if the encryption remains unbroken.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Login to AWS Management Console and open the Amazon S3 console using [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/)
1. Select the Check box next to the Bucket.
1. Click on Properties.
1. Click on Default Encryption.
1. Select either SSE-S3, SSE-KMS, or DSSE-KMS.
1. If applicable, select an AWS KMS key or enter the key's ARN.
1. Click Save.
1. Repeat for all the buckets in your AWS account lacking encryption.

### From the command line{% #from-the-command-line %}

Run one of the following commands:

`aws s3api put-bucket-encryption --bucket <bucket name> --server-side-encryption-configuration ''{"Rules": [{"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}]}''`

or:

`aws s3api put-bucket-encryption --bucket <bucket name> --server-side-encryption-configuration ''{"Rules": [{"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "aws:kms","KMSMasterKeyID": <key arn>}}]}''`

or:

`aws s3api put-bucket-encryption --bucket <bucket name> --server-side-encryption-configuration ''{"Rules": [{"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "aws:kms:dsse","KMSMasterKeyID": <key arn>}}]}''`

**Note**: The `KMSMasterKeyID` can be set to the master key of your choosing; `aws/s3` is an AWS preconfigured default.

## References{% #references %}

1. [https://docs.aws.amazon.com/AmazonS3/latest/user-guide/default-bucket-encryption.html](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/default-bucket-encryption.html)
1. [https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html#bucket-encryption-related-resources](https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html#bucket-encryption-related-resources)

**Additional Information**: S3 bucket encryption only applies to objects as they are placed in the bucket. Enabling S3 bucket encryption does not encrypt objects previously stored within the bucket.
