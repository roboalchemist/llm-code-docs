# Source: https://docs.datadoghq.com/security/default_rules/def-000-2bb.md

---
title: Windows suspicious Teams application related ObjectAccess event
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows suspicious Teams application
  related ObjectAccess event
---

# Windows suspicious Teams application related ObjectAccess event
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1528-steal-application-access-token](https://attack.mitre.org/techniques/T1528)
## Goal{% #goal %}

Detects suspicious access to Microsoft Teams storage locations that may indicate credential or token theft attempts.

## Strategy{% #strategy %}

This rule monitors Windows event logs for object access events related to sensitive Microsoft Teams storage locations. It specifically looks for Windows Event ID `4663` (An attempt was made to access an object) where the ObjectName contains either Teams local storage level database files or Microsoft Teams Cookies. These locations store authentication tokens, session data, and other sensitive information that is valuable to attackers. Unauthorized access to these files could indicate an attempt to steal Microsoft Teams access tokens, which can be used to impersonate users, access sensitive communications, or pivot to other Microsoft 365 services.

## Triage & Response{% #triage--response %}

- Examine the complete object access event on `{{host}}` to determine which specific Teams-related files were accessed.
- Determine if the access was made by legitimate Teams processes or by unexpected applications.
- Inspect process creation events around the time of suspicious access to identify potential malware execution.
- Check for evidence of data exfiltration from the system following the suspicious access.
- Revoke and reissue all active Microsoft 365 tokens for the compromised account.
