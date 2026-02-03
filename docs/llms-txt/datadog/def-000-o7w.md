# Source: https://docs.datadoghq.com/security/default_rules/def-000-o7w.md

---
title: >-
  Bedrock model invocation logging should be enabled and stored in
  restricted-access S3 buckets
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Bedrock model invocation logging should
  be enabled and stored in restricted-access S3 buckets
---

# Bedrock model invocation logging should be enabled and stored in restricted-access S3 buckets
 
## Description{% #description %}

Enable Amazon Bedrock model invocation logging to monitor and audit model usage for security, compliance, and operational purposes. Ensure that logs are not stored in publicly accessible S3 buckets to prevent unauthorized access to sensitive model invocation data.

## Remediation{% #remediation %}

Configure Bedrock model invocation logging with at least one data type enabled (text, image, embedding, or video) and ensure the destination is either CloudWatch Logs or a non-public S3 bucket. For detailed configuration steps, refer to the [Monitor model invocation logging in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) documentation.
