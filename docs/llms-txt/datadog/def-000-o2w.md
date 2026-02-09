# Source: https://docs.datadoghq.com/security/default_rules/def-000-o2w.md

---
title: Windows active directory object WriteDAC access
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows active directory object
  WriteDAC access
---

# Windows active directory object WriteDAC access

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1222-file-and-directory-permissions-modification](https://attack.mitre.org/techniques/T1222) 
## Goal{% #goal %}

Detects an instance where a user or process modifies the Discretionary Access Control List (DACL) of an Active Directory (AD) object.

## Strategy{% #strategy %}

This detection monitors Windows Security event logs for occurrences of Event ID 4662 (An operation was performed on an object) with specific indicators of DACL modifications.

DACL modifications in Active Directory can be used to grant specific permissions to accounts, allowing attackers to maintain persistence even after credentials are changed. This technique is particularly concerning when applied to high-value objects like domain controllers or administrative groups.

## Triage & Response{% #triage--response %}

- Identify the `{{host}}` domain controller that recorded the DACL modification event.
- Examine which account performed the WriteDAC operation by reviewing the `SubjectUserName` field.
- Determine which AD object was modified by reviewing the `ObjectName` field.
- Check whether the object modified is a high-value target such as a user, group, or critical AD structure.
- Correlate with Event ID 4670 which indicates that permissions on an object were changed.
- Look for new or suspicious security principals added to the DACL using Active Directory tools.
- Review Event ID 4728, 4732, 4756 (Group Membership Changes) to check if the affected object was added to privileged groups.
- Check if the same account recently requested DCSync permissions.
- Determine whether the modification was part of normal administrative activity or unauthorized.
- Disable the account that performed the modification if suspicious activity is confirmed.
- Revert unauthorized ACL modifications using PowerShell or Active Directory tools.

## Changelog{% #changelog %}

- 5 August 2025 - Updated severity.
