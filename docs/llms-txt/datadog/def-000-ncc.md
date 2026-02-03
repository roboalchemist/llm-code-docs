# Source: https://docs.datadoghq.com/security/default_rules/def-000-ncc.md

---
title: Administrative privileges assigned to a user, group or role
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Administrative privileges assigned to a
  user, group or role
---

# Administrative privileges assigned to a user, group or role

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detects when administrative privileges are assigned to user accounts, groups, or roles.

## Strategy{% #strategy %}

This rule monitors OCSF-transformed logs where `@ocsf.class_uid` is `3005` (User Access Management) or `3006` (Group Management) for administrative privilege assignment activities. It triggers when events include `@ocsf.activity_name` set to `Assign Privileges` and `@ocsf.privileges` containing `ADMIN_PRIVILEGES_ASSIGNED`. Administrative privilege assignments are significant security events that could indicate legitimate administrative actions or potential privilege escalation attacks. Monitoring these activities across all connected systems is critical for maintaining proper access controls.

## Triage and response{% #triage-and-response %}

- Verify if the privilege assignment to `{{@ocsf.user.name}}` was authorized through your organization's access management process.
- Review the specific privileges granted and determine if they align with the user's legitimate business role and responsibilities.
- Examine the timing and context of the privilege assignment to identify if it occurred during normal business hours or as part of scheduled administrative activities.
- Check for any concurrent suspicious activities from the same user account across connected systems and platforms.
- Validate that the privilege assignment was performed by an authorized administrator with proper approval documentation.
- Determine if the newly assigned privileges have been used since the assignment and review any actions taken with the elevated permissions.
