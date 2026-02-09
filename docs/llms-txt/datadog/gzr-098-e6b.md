# Source: https://docs.datadoghq.com/security/default_rules/gzr-098-e6b.md

---
title: An AWS S3 bucket lifecycle expiration policy was set to disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > An AWS S3 bucket lifecycle expiration
  policy was set to disabled
---

# An AWS S3 bucket lifecycle expiration policy was set to disabled
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Detect if an AWS S3 lifecycle expiration policy is set to disabled in your CloudTrail logs.

## Strategy{% #strategy %}

Check if `@requestParameters.LifecycleConfiguration.Rule.Expiration.Days`, `@requestParameters.LifecycleConfiguration.Status:Disabled` and `@evt.name:PutBucketLifecycle` fields are present in your S3 Lifecycle configuration log. If these fields are present together, a bucket's lifecycle configuration has been turned off.

## Triage & Response{% #triage--response %}

1. Determine if `{{@evt.name}}` should have occurred on the `{{@requestParameters.bucketName}}` by `username:` `{{@userIdentity.sessionContext.sessionIssuer.userName}}`, `accountId:` `{{@userIdentity.accountId}}` of `type:` `{{@userIdentity.assumed_role}}`.
1. If the `{{@requestParameters.bucketName}}` should not be disabled, escalate to engineering so they can re-enable it.
