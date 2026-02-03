# Source: https://docs.datadoghq.com/security/default_rules/def-000-djb.md

---
title: GitHub mass deletion of repositories
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > GitHub mass deletion of repositories
---

# GitHub mass deletion of repositories
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Detects mass deletion of GitHub repositories or organization deletion events that could indicate potentially malicious destructive activities.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for organization deletion events through `org.delete` and repository destruction events through `repo.destroy`. The detection differentiates between user-initiated and bot-initiated repository deletions to provide appropriate severity levels.

## Triage & Response{% #triage--response %}

- Examine the GitHub audit logs for `{{@github.actor}}` to identify the specific user that initiated the activity.
- Verify if the user account associated with the deletion activity has legitimate administrative permissions and business justification for the destructive actions.
- Review recent authentication patterns and access anomalies for the account to determine if it may have been compromised.
- Check for any prior suspicious activities such as unusual data access, privilege escalation, or account modifications that could indicate compromise.
