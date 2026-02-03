# Source: https://docs.datadoghq.com/security/default_rules/def-000-x1d.md

---
title: AWS IAM activity by S3 browser utility
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > AWS IAM activity by S3 browser utility
---

# AWS IAM activity by S3 browser utility
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detect IAM activity associated with the S3 browser utility.

## Strategy{% #strategy %}

This rule monitors AWS CloudTrail and detects IAM activity associated with the S3 browser utility. S3 browser is a freeware Windows client for Amazon S3 and Amazon CloudFront. This tool has been used by the threat group GUI-vil in order to persist or escalate privileges in a victim's AWS account. Details about this threat group can be seen in the [Permiso blog post](https://permiso.io/blog/s/unmasking-guivil-new-cloud-threat-actor/).

This rule monitors the following API calls:

- CreateUser
- CreateLoginProfile
- CreateAccessKey
- PutUserPolicy

## Triage and response{% #triage-and-response %}

1. Determine if `{{@userIdentity.arn}}` should be attempting to use the S3 browser utility.
   - Investigate any other actions carried out by the potentially compromised identity `{{@userIdentity.arn}}` using the Cloud SIEM investigator.
1. If the activity is determined to be malicious:
   - Rotate the affected credentials.
   - Remove any new IAM users, access keys, or LoginProfiles.
   - Begin your organization's incident response process and investigate.
