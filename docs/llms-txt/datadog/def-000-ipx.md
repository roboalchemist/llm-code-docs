# Source: https://docs.datadoghq.com/security/default_rules/def-000-ipx.md

---
title: GitLab user changes associated email
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > GitLab user changes associated email
---

# GitLab user changes associated email

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detects when a GitLab user changes their associated email address and then signs in using the new email.

## Strategy{% #strategy %}

This rule monitors the `user_email_changed_and_user_signed_in` GitLab audit event. Email address changes can be used by attackers to maintain persistence after compromising an account.

## Triage and response{% #triage-and-response %}

- Verify if `{{@usr.name}}` has a legitimate business reason to change their email address in GitLab.
- Review authentication logs around the time of the email change to identify any unusual access patterns or geographic anomalies.
- Examine recent GitLab activity for the user account to determine if any unauthorized actions were performed after the email change.
- Validate that the new email address belongs to the organization's domain or is otherwise authorized for use.
