# Source: https://docs.datadoghq.com/security/default_rules/def-000-pkl.md

---
title: GitLab personal access token generated
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > GitLab personal access token generated
---

# GitLab personal access token generated
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Detects when a user creates a personal access token in GitLab. Personal access tokens provide programmatic access to perform actions on behalf of the user.

## Strategy{% #strategy %}

This rule monitors GitLab audit events where `@evt.name` is `personal_access_token_created`. Personal access tokens grant API access to GitLab resources accessible by the connected user, making them valuable for attackers seeking to maintain persistent access to source code repositories and CI/CD pipelines.

## Triage & Response{% #triage--response %}

- Identify the `{{@usr.name}}` associated with the activity.
- Review the scope and permissions granted to the newly created token to ensure they align with the user's role and responsibilities.
- Examine the IP address and user agent associated with the token creation to identify any suspicious access patterns.
- Check if the token creation coincides with other suspicious activities from the same user account or IP address.
- Validate that the user account creating the token has not been compromised by reviewing recent authentication and activity logs.
