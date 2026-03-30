# Source: https://docs.datadoghq.com/security/default_rules/def-000-t3z.md

---
title: AWS IAM Identity Center SSO configuration updated
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS IAM Identity Center SSO
  configuration updated
---

# AWS IAM Identity Center SSO configuration updated
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1556-modify-authentication-process](https://attack.mitre.org/techniques/T1556)
## Goal{% #goal %}

Detects when the configuration for the current SSO instance is modified. This rule monitors for changes to AWS SSO settings that could impact authentication and access control.

## Strategy{% #strategy %}

This rule monitors AWS CloudTrail logs for `UpdateSsoConfiguration` events originating from AWS IAM Identity Center. AWS SSO configuration updates can include changes to identity provider settings, authentication methods, and access control policies that govern how users authenticate and access AWS resources.

## Triage & Response{% #triage--response %}

1. Review the `@userIdentity.arn` to identify the user or role that made the configuration change.
1. Check if the change was made during a scheduled maintenance window or by an authorized administrator.
1. Verify if the configuration change aligns with documented change management procedures.
1. Examine the specific parameters modified in the SSO configuration to determine the scope of changes.
