# Source: https://docs.datadoghq.com/security/default_rules/def-000-xhs.md

---
title: Windows ANONYMOUS LOGON local account created
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows ANONYMOUS LOGON local account
  created
---

# Windows ANONYMOUS LOGON local account created

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1136-create-account](https://attack.mitre.org/techniques/T1136) 
## Goal{% #goal %}

Detects the creation of a local user account containing "ANONYMOUS LOGON" in the name.

## Strategy{% #strategy %}

This rule monitors Windows Security event logs for user account creation events with suspicious naming patterns. It specifically looks for Windows Event ID `4720` (User Account Created) where the SamAccountName contains both "ANONYMOUS" and "LOGON" strings. These naming patterns are suspicious as they attempt to mimic legitimate Windows system accounts. The creation of accounts with these naming patterns is uncommon in legitimate scenarios, and indicates an attacker attempting to establish persistence by creating accounts that blend in with system accounts, but grant interactive access.

## Triage & Response{% #triage--response %}

- Examine the `{{host}}` system to verify the account creation event and identify who created the account.
- Review the privileges assigned to the newly created account to determine its potential access level.
- Check if the account has been added to any privileged groups such as Administrators or Remote Desktop Users.
- Reset credentials for any potentially compromised administrator accounts that may have been used to create the suspicious account.
