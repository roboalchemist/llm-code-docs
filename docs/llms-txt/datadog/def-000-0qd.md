# Source: https://docs.datadoghq.com/security/default_rules/def-000-0qd.md

---
title: Windows active directory user assigned right to control user objects
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows active directory user assigned
  right to control user objects
---

# Windows active directory user assigned right to control user objects

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detects assignment of delegation privileges to user accounts that enable control over other user objects in Active Directory.

## Strategy{% #strategy %}

This rule monitors Windows Security Audit events, where `@evt.id` is `4704` when `SeEnableDelegationPrivilege` is assigned to a user account. This privilege allows a user to enable computer and user accounts to be trusted for delegation, which can be abused by attackers to impersonate other users and escalate privileges within the domain. The `SeEnableDelegationPrivilege` is typically reserved for highly privileged service accounts and should rarely be assigned to regular user accounts.

## Triage and response{% #triage-and-response %}

- Verify if the privilege assignment on `{{host}}` was authorized and follows proper change management procedures.
- Review the target user account to determine if it requires delegation privileges for legitimate business functions.
- Check for subsequent delegation configuration changes or suspicious authentication activity from the affected account.
- Examine the source of the privilege assignment to ensure it came from authorized administrative personnel.
- Monitor for potential abuse of the delegation privilege to impersonate other users or access sensitive resources.
