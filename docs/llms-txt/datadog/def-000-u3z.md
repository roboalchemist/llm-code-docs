# Source: https://docs.datadoghq.com/security/default_rules/def-000-u3z.md

---
title: Potential brute force attack detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Potential brute force attack detected
---

# Potential brute force attack detected
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110) 
## Goal{% #goal %}

Detect when a user fails to log in to Abnormal Security an unusually high number of times.

## Strategy{% #strategy %}

This rule monitors for failed user logins, which may indicate that an attacker has gained access to the user credentials and accessed the account.

## Triage and response{% #triage-and-response %}

1. Investigate the other actions performed by the user `{{@user.email}}`.
1. If confirmed as a threat, implement measures to block or limit the impact of the suspicious activity.
1. Follow company procedures for handling malicious files, including isolating the endpoint, running antivirus/antimalware scans, analyzing logs, and updating security policies.
