# Source: https://docs.datadoghq.com/security/default_rules/yg4-3in-tkd.md

---
title: CloudTrail logs should be encrypted at rest using KMS CMKs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > CloudTrail logs should be encrypted at
  rest using KMS CMKs
---

# CloudTrail logs should be encrypted at rest using KMS CMKs

## Description{% #description %}

AWS CloudTrail records AWS API calls, and configuring it to use AWS Key Management Service (KMS) for server-side encryption (SSE) enhances log security. KMS uses Hardware Security Modules (HSMs) for key protection, adding confidentiality controls. Setting up CloudTrail with SSE-KMS ensures only authorized users with S3 read and CMK decrypt permissions can access the logs.

## Remediation{% #remediation %}

For instructions on configuring CloudTrail to use SSE-KMS, refer to the [CloudTrail Log File Encryption Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/encrypting-cloudtrail-log-files-with-aws-kms.html).
