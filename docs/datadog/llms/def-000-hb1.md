# Source: https://docs.datadoghq.com/security/default_rules/def-000-hb1.md

---
title: S3 bucket policies should restrict access from other AWS accounts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > S3 bucket policies should restrict
  access from other AWS accounts
---

# S3 bucket policies should restrict access from other AWS accounts

## Description{% #description %}

This check verifies whether an Amazon S3 general-purpose bucket policy restricts principals in other AWS accounts from executing unauthorized actions on resources within the S3 bucket. The check will not pass if the bucket policy permits any of the aforementioned actions for a principal in a different AWS account.

Enforcing the principle of least privilege is essential for mitigating security risks and minimizing the repercussions of errors or malicious activities. Allowing access from external accounts through an S3 bucket policy could lead to breaches through data exfiltration by malicious insiders or attackers.

By utilizing the blacklistedactionpatterns parameter, the rule evaluates successfully for S3 buckets. This parameter enables access to external accounts only for specific action patterns not included in the blacklistedactionpatterns list.

Risky Actions: s3:DeleteBucketPolicy, s3:PutBucketAcl, s3:PutBucketPolicy, s3:PutEncryptionConfiguration, s3:PutObjectAcl

## Remediation{% #remediation %}

To adjust an Amazon S3 bucket policy to revoke permissions, please refer to the [Adding a bucket policy using the Amazon S3 console section in the Amazon Simple Storage Service User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/add-bucket-policy.html).

When on the Edit bucket policy page, within the policy editing text box, choose one of the following actions:

- Erase the statements allowing access to denied actions by other AWS accounts.
- Eliminate the denied actions that are permitted in the statements.
