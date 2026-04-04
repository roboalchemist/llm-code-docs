# Source: https://docs.datadoghq.com/security/default_rules/748-vvi-4ye.md

---
title: S3 bucket access logging should be enabled on the CloudTrail S3 bucket
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > S3 bucket access logging should be
  enabled on the CloudTrail S3 bucket
---

# S3 bucket access logging should be enabled on the CloudTrail S3 bucket

## Description{% #description %}

S3 Bucket Access Logging generates a log with access records for each request made to your S3 bucket. These logs include details such as request type, specified resources, and the request's processing time and date. Enabling bucket access logging, particularly on the CloudTrail S3 bucket, is recommended to enhance security and support incident response activities by capturing all events affecting bucket objects.

## Remediation{% #remediation %}

For instructions on enabling S3 Bucket Access Logging, refer to the [AWS S3 Server Access Logging Guide](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerLogs.html).
