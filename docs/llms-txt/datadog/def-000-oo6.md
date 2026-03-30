# Source: https://docs.datadoghq.com/security/default_rules/def-000-oo6.md

---
title: Windows hidden local user creation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Windows hidden local user creation
---

# Windows hidden local user creation

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1136-create-account](https://attack.mitre.org/techniques/T1136)
## Goal{% #goal %}

Detects the creation of a hidden local user account, which is often used by attackers for persistence and privilege escalation.

## Strategy{% #strategy %}

This detection monitors Windows Security event logs for Event ID 4720 (A user account was created) with specific focus on accounts that end with a dollar sign (`$`). The detection excludes the legitimate HomeGroupUser$ account while looking for other accounts with the $ suffix.

Hidden user accounts typically have names ending with "$" to mimic system accounts, making them less visible in user interfaces and management tools. This naming convention is an evasion technique used by attackers to blend their persistence mechanisms with legitimate system accounts.

## Triage & Response{% #triage--response %}

- Identify the `{{host}}` system where the hidden user account was created.
- Examine the name of the newly created hidden account in the `TargetUserName` field.
- Identify which account created the hidden user by reviewing the `SubjectUserName` field.
- Check for account modifications such as modifying the `UserAccountControl` attribute to further conceal the account.
- Review if the account was added to privileged groups by examining group membership change events.
- Look for logon success events associated with the account to determine if it's actively being used.
- Examine any scheduled tasks or services configured to run under this account's context.
- Review registry modifications and service installations related to the hidden user.
- Disable the account immediately if the creation is unauthorized.
- Remove the account from any privileged groups and investigate other systems for similar hidden accounts.
- Investigate the system and user who created the account for other compromise indicators.

## Changelog{% #changelog %}

- 5 August 2025 - Updated severity.
