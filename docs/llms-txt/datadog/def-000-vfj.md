# Source: https://docs.datadoghq.com/security/default_rules/def-000-vfj.md

---
title: AWS S3 Object encryption with SSE-C
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > AWS S3 Object encryption with SSE-C
---

# AWS S3 Object encryption with SSE-C
Classification:attackTactic:[TA0040-impact](https://attack.mitre.org/tactics/TA0040)Technique:[T1486-data-encrypted-for-impact](https://attack.mitre.org/techniques/T1486)
## WARNING: This rule is being deprecated on 6 April 2026.{% #warning-this-rule-is-being-deprecated-on-6-april-2026 %}

- See the [Advanced Notice](https://aws.amazon.com/blogs/storage/advanced-notice-amazon-s3-to-disable-the-use-of-sse-c-encryption-by-default-for-all-new-buckets-and-select-existing-buckets-in-april-2026/) article from AWS.

## Goal{% #goal %}

Detects attempts to encrypt AWS S3 objects using server-side encryption with customer-provided keys (SSE-C).

## Strategy{% #strategy %}

This rule monitors CloudTrail logs for S3 object operations (`CopyObject` and `PutObject`) where customer-provided encryption keys are used. When external encryption is applied to S3 objects, the rule detects this by examining the `@requestParameters.x-amz-server-side-encryption-customer-algorithm` attribute. This activity warrants attention since attackers can leverage SSE-C encryption with their own keys to make objects inaccessible to legitimate owners, essentially enabling ransomware-style attacks.

## Triage & Response{% #triage--response %}

1. Verify if the detected activity aligns with approved change management processes or expected administrative actions.
1. Examine the actor `{{@userIdentity.arn}}` and `{{@userIdentity.accessKeyId}}` to determine if they are authorized to perform encryption operations on the affected S3 buckets.
1. Check if the affected S3 bucket `{{@requestParameters.bucketName}}` contains sensitive or critical data that would be valuable for ransomware targets.
1. Revoke the access key `{{@userIdentity.accessKeyId}}` if determined to be unauthorized or compromised.
1. Restore affected objects from backups if available and confirmed encrypted without authorization.
1. Implement S3 bucket policies to restrict the use of SSE-C encryption to approved roles and service accounts only.
