# Source: https://docs.datadoghq.com/security/default_rules/def-000-8yj.md

---
title: OneLogin API activity from malicious IP address
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > OneLogin API activity from malicious IP
  address
---

# OneLogin API activity from malicious IP address
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detect and investigate OneLogin API activity originating from suspicious IP addresses, which may indicate potential unauthorized access attempts or malicious API interactions.

## Strategy{% #strategy %}

This rule monitors activities within OneLogin, focusing specifically on actions initiated by users via the API. It flags activities where the source IP address has been identified with suspicious or malicious indicators, such as associations with botnet proxies, known malicious intent, or anonymization services like Tor.

## Triage and Response{% #triage-and-response %}

1. Verify user activity: Check if the user associated with the alert (`{{@usr.name}}`) has a legitimate reason for API interactions from the flagged IP.

1. Investigate suspicious IP:

   - Review logs related to the flagged IP to determine if it has been involved in other potentially malicious actions.
   - Use threat intelligence sources or IP investigation tools to gather context on the flagged IP's reputation and any recent malicious activity.

1. Containment and remediation:

   - If the activity is confirmed unauthorized, consider blocking the IP address at the network level.
   - Review and rotate API keys or admin credentials associated with the suspicious activity to prevent further unauthorized access.
