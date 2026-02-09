# Source: https://docs.datadoghq.com/security/default_rules/def-000-7qi.md

---
title: CodeBuild projects should have logging enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > CodeBuild projects should have logging
  enabled
---

# CodeBuild projects should have logging enabled
 
## Description{% #description %}

This control verifies that a CodeBuild project environment has logging enabled, requiring at least one log option, either to S3 or CloudWatch. Enabling logging is essential for potential forensic analysis in the event of a security incident. Correlating unusual activities in CodeBuild projects with threat detections enhances the reliability of those detections.

## Remediation{% #remediation %}

For guidance on configuring logging settings, refer to the [Logging and monitoring in AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/logging-monitoring.html) section of the AWS CodeBuild User Guide.
