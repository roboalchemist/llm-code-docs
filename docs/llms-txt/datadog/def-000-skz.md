# Source: https://docs.datadoghq.com/security/default_rules/def-000-skz.md

---
title: S3 Block Public Access feature should be enabled at the account level
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > S3 Block Public Access feature should
  be enabled at the account level
---

# S3 Block Public Access feature should be enabled at the account level

## Description{% #description %}

Amazon S3 provides the 'Block public access' (BPA) account feature to help restrict unintended public access to S3 data. By default, S3 buckets and objects are created without public access, but a person or system with sufficient permissions can enable public access at the bucket or object level. When you enable this feature with all four options enabled, it prevent buckets and the objects within from becoming publicly accessible, reducing the risk of accidental or malicious data exposure. Blocking public access should be an organizational decision based on data sensitivity, least privilege, and use case. If data stored in an S3 bucket is required to be available publicly, best practice is to use an intermediary system like Amazon CloudFront with origin access control (OAC) enabled.

For this control to pass, all four BPA options must be enabled:

- `BlockPublicAcls`
- `IgnorePublicAcls`
- `BlockPublicPolicy`
- `RestrictPublicBuckets`

## Remediation{% #remediation %}

For guidance on configuring Block Public Access settings, refer to the [Blocking Public Access to S3 Resources](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/block-public-access-account.html) section of the Amazon Simple Storage Service User Guide. For guidance on using Amazon CloudFront to securely share S3 data publicly, refer to the [Restrict access to an Amazon S3 origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) section of the Amazon CloudFront Developer Guide.
