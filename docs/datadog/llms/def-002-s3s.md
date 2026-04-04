# Source: https://docs.datadoghq.com/security/default_rules/def-002-s3s.md

---
title: >-
  Publicly accessible EC2 instance has access to an S3 bucket with sensitive
  data
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Publicly accessible EC2 instance has
  access to an S3 bucket with sensitive data
---

# Publicly accessible EC2 instance has access to an S3 bucket with sensitive data

## Description{% #description %}

A publicly accessible EC2 instance has a role that allows access to an S3 bucket containing sensitive data. This could lead to data exfiltration or data leakage. Sensitive data could include personally identifiable information (PII), credentials, financial information, and network or device information. For more details on how sensitive data is detected, see the [official documentation](https://docs.datadoghq.com/security/cloud_security_management/agentless_scanning/#data-security).

## Remediation{% #remediation %}

1. Assess whether this instance needs to be accessible from the internet. If not, restrict access to the instance by updating the security group or network ACL to only allow access from trusted sources.
1. Restrict access to the S3 bucket containing sensitive data to only the necessary users or roles by reviewing IAM policies and bucket resource policies. For more information on restricting access to an S3 bucket, see the [official documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security_iam_service-with-iam.html).
