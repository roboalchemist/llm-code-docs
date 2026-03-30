# Source: https://docs.datadoghq.com/security/default_rules/def-000-5rx.md

---
title: GitLab new administrator added
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > GitLab new administrator added
---

# GitLab new administrator added

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Detects when a new administrator is added to a GitLab organization.

## Strategy{% #strategy %}

This rule monitors the `user_admin_status_updated` and `admin_role_assigned_to_user` GitLab audit events. These events indicate when user accounts are granted administrative privileges within the GitLab organization. Administrator access provides extensive control over repositories, user management, security settings, and organizational configurations, making unauthorized privilege escalation a significant security concern.

## Triage & Response{% #triage--response %}

- Verify if the administrator privilege assignment for `{{@usr.name}}` was authorized through proper change management processes.
- Check for any suspicious activity from the newly elevated administrator account following the privilege grant.
- Validate that the timing of the privilege escalation aligns with legitimate business requirements or personnel changes.
