# Source: https://docs.datadoghq.com/security/default_rules/def-000-cci.md

---
title: >-
  Bedrock custom models should not output model data to publicly accessible s3
  buckets
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Bedrock custom models should not output
  model data to publicly accessible s3 buckets
---

# Bedrock custom models should not output model data to publicly accessible s3 buckets
 
## Description{% #description %}

This control verifies that Amazon Bedrock custom models are **not** outputting model data to publicly accessible Amazon S3 buckets. Storing model outputs in publicly accessible locations poses significant security risks, including unauthorized data access, exposure of sensitive information, and potential data breaches. Ensuring output data is securely stored helps maintain the confidentiality and integrity of your AI/ML workflows.

## Remediation{% #remediation %}

Update the bucket permissions and policies to restrict public access permissions. For guidance, review the [Block Public Access to S3 Buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html) documentation.

For additional configuration and protection measures, please consult the [How can I secure the files in my Amazon S3 buckets?](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/) documentation.
