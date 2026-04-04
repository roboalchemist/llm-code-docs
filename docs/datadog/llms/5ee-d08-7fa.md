# Source: https://docs.datadoghq.com/security/default_rules/5ee-d08-7fa.md

---
title: AWS root account activity
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > AWS root account activity
---

# AWS root account activity
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detect AWS root user activity.

## Strategy{% #strategy %}

Monitor CloudTrail and detect when any `@userIdentity.type` has a value of `Root`, but is not invoked by an AWS service or SAML provider.

## Triage and response{% #triage-and-response %}

1. Determine if the root API Call: `{{@evt.name}}` is expected.
1. If the action wasn't legitimate, rotate the credentials, enable 2FA, and open an investigation.

- For best practices, check out the [AWS Root Account Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html) documentation.
- For compliance, check out the [CIS AWS Foundations Benchmark controls](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cis-controls.html) documentation.
