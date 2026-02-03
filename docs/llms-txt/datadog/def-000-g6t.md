# Source: https://docs.datadoghq.com/security/default_rules/def-000-g6t.md

---
title: Zoom user updated to privileged role
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Zoom user updated to privileged role
---

# Zoom user updated to privileged role

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

This detection identifies when Zoom user accounts are elevated to privileged roles (Admin or Co-Owner).

## Strategy{% #strategy %}

This detection monitors Zoom operation logs for user role elevation events. The rule focuses on events where a user's role is changed to either "Co-Owner" or "Admin" roles. The detection analyzes events with `@evt.category` of "User" and `@evt.name` values of "Update" or "Batch Update" containing specific messages indicating role changes to privileged positions. Events are grouped by the email address of the user making these changes (`@usr.email`).

Role elevation is significant because privileged accounts can perform sensitive actions such as managing users, modifying security settings, and changing organizational policies. Unauthorized elevation to these roles provides attackers with extensive capabilities to modify the Zoom environment and potentially maintain persistence.

## Triage & Response{% #triage--response %}

- Verify whether the role elevation was authorized through proper channels by checking change management documentation.
- Identify which administrator (`{{@usr.email}}`) performed the role change and confirm legitimacy.
- Examine the target user whose role was elevated to determine business need for privileged access.
- Review administrative actions performed by the newly privileged user following elevation.
- Examine Zoom audit logs for concurrent administrative actions indicating suspicious behavior.
- Ensure privileged account monitoring and implement documented approval process for role changes.

## Changelog{% #changelog %}

- 26 June 2025 - update detection rule to remove wildcard matching.
