# Source: https://docs.datadoghq.com/security/default_rules/azr-i96-fmv.md

---
title: CloudTrail log file validation should be enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > CloudTrail log file validation should
  be enabled
---

# CloudTrail log file validation should be enabled

## Description{% #description %}

CloudTrail log file validation generates a digitally signed digest file containing a hash of each log that CloudTrail writes to S3. This feature helps verify whether a log file was changed, deleted, or remains unchanged after delivery, thereby enhancing the integrity of CloudTrail logs. Enabling log file validation on all trails is recommended.

## Remediation{% #remediation %}

For instructions on enabling log file validation for CloudTrail, refer to the [AWS CloudTrail Log File Validation Guide](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-enabling.html).
