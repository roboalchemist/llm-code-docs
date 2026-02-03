# Source: https://docs.datadoghq.com/security/default_rules/def-000-u8a.md

---
title: Email with spam category opened by user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Email with spam category opened by user
---

# Email with spam category opened by user
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1566-phishing](https://attack.mitre.org/techniques/T1566) 
## Goal{% #goal %}

Detect when a spam email is opened.

## Strategy{% #strategy %}

This rule monitors Abnormal logs to detect when a spam email is opened by a user.

## Triage and response{% #triage-and-response %}

1. Investigate the user, `{{@messages.toAddresses}}`, who was impacted by the email.
1. If confirmed as a threat, implement measures to block or limit the impact of the suspicious activity.
1. Follow company procedures for handling malicious files, including isolating the endpoint, running antivirus/antimalware scans, analyzing logs, and updating security policies.
