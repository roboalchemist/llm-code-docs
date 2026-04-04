# Source: https://docs.datadoghq.com/security/default_rules/0kb-4zy-y2r.md

---
title: Anomalous API Gateway API key reads by user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Anomalous API Gateway API key reads by
  user
---

# Anomalous API Gateway API key reads by user
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1552-unsecured-credentials](https://attack.mitre.org/techniques/T1552)
## Goal{% #goal %}

Detect when a user is enumerating API Gateway API keys.

## Strategy{% #strategy %}

Baseline `GetApiKeys` events by `@userIdentity.session_name` to surface anomalous `GetApiKeys` calls.

## Triage and response{% #triage-and-response %}

1. Investigate activity for the following ARN `{{@userIdentity.arn}}` using `{{@userIdentity.session_name}}`.
1. Review any other security signals for `{{@userIdentity.arn}}`.
