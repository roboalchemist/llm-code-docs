# Source: https://docs.datadoghq.com/security/default_rules/def-000-ag8.md

---
title: RDS cluster exports snapshots to publicly accessible S3 bucket
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > RDS cluster exports snapshots to
  publicly accessible S3 bucket
---

# RDS cluster exports snapshots to publicly accessible S3 bucket

## Description{% #description %}

A private RDS cluster is exporting database snapshots to a publicly accessible S3 bucket. This configuration can expose sensitive data to unauthorized users.

## Remediation{% #remediation %}

1. Update the S3 bucket configuration to disable public access. See the [official documentation](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/block-public-access-account.html) for more information on how to disable public access.
1. Restrict access to the S3 bucket containing the snapshots to only the necessary users or roles by reviewing IAM policies and bucket resource policies. For more information on restricting access to an S3 bucket, see the [official documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security_iam_service-with-iam.html).
