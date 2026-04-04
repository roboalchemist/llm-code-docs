# Source: https://docs.datadoghq.com/security/default_rules/def-000-c5t.md

---
title: Windows suspicious computer name containing Samtheadmin
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows suspicious computer name
  containing Samtheadmin
---

# Windows suspicious computer name containing Samtheadmin

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detects systems or accounts named "samtheadmin" that indicate compromise through unauthorized privilege escalation and persistence.

## Strategy{% #strategy %}

This rule monitors Windows events for the specific string patterns "samtheadmin" or "SAMTHEADMIN" in both `@Event.EventData.Data.SamAccountName` and `@Event.EventData.Data.TargetUserName` fields. These naming patterns are associated with targeted attack campaigns where adversaries create administrative accounts or rename systems during post-exploitation activities.

The "samtheadmin" naming convention is a strong indicator of compromise as legitimate administrators avoid using such obvious administrative naming conventions that draw attention to privileged accounts.

## Triage & Response{% #triage--response %}

- Verify the suspicious account or computer name existence on `{{host}}`.
- Determine when the account was created or system was renamed.
- Review authentication logs for activity involving the suspicious account.
- Examine assigned privileges and group memberships for privilege escalation.
- Search for concurrent suspicious account creation activities.
- Investigate lateral movement attempts from the compromised system.
- Reset all administrative credentials that may have been compromised.
- Isolate affected systems from the network.
