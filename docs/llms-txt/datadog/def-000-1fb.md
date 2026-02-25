# Source: https://docs.datadoghq.com/security/default_rules/def-000-1fb.md

---
title: Login attempt from new location detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Login attempt from new location
  detected
---

# Login attempt from new location detected
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detect when a user logs in to Abnormal Security from an atypical location.

## Strategy{% #strategy %}

This rule checks for user login API calls originating from an atypical location, which may indicate that an attacker has gained access to the user credentials and accessed the account.

## Triage and response{% #triage-and-response %}

1. Investigate the other actions performed by the user `{{@user.email}}`.
1. If confirmed as a threat, implement measures to block or limit the impact of the suspicious activity.
1. Follow company procedures for handling malicious files, including isolating the endpoint, running antivirus/antimalware scans, analyzing logs, and updating security policies.
