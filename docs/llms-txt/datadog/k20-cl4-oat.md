# Source: https://docs.datadoghq.com/security/default_rules/k20-cl4-oat.md

---
title: S3 buckets should have 'MFA Delete' enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > S3 buckets should have 'MFA Delete'
  enabled
---

# S3 buckets should have 'MFA Delete' enabled

## Description{% #description %}

Enabling `MFA Delete` on S3 buckets requires two forms of authentication whenever there is an attempt to change the versioning state or delete an object version. This additional layer of security is crucial in protecting against unauthorized or accidental deletions.

## Remediation{% #remediation %}

For configuration instructions on enabling `MFA Delete` using the AWS CLI, refer to [Setting Up MFA Delete](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html).
