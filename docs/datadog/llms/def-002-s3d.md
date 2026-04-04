# Source: https://docs.datadoghq.com/security/default_rules/def-002-s3d.md

---
title: Publicly accessible S3 bucket stores sensitive data
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Publicly accessible S3 bucket stores
  sensitive data
---

# Publicly accessible S3 bucket stores sensitive data

## Description{% #description %}

A publicly accessible S3 bucket contains sensitive data. This could lead to data exfiltration or data leakage. Sensitive data could include personally identifiable information (PII), credentials, financial information, and network or device information. For more details on how sensitive data is detected, see the [official documentation](https://docs.datadoghq.com/security/cloud_security_management/agentless_scanning/#data-security).

## Remediation{% #remediation %}

1. Update the S3 bucket configuration to disable public access. See the [official documentation](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/block-public-access-account.html) for more information on how to disable public access.
1. Restrict access to the S3 bucket containing sensitive data to only the necessary users or roles by reviewing IAM policies and bucket resource policies. For more information on restricting access to an S3 bucket, see the [official documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security_iam_service-with-iam.html).
