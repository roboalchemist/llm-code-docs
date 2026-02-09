# Source: https://docs.datadoghq.com/security/default_rules/def-000-dpx.md

---
title: GitLab brute force attack
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > GitLab brute force attack
---

# GitLab brute force attack

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110) 
## Goal{% #goal %}

Detects GitLab brute force attacks where multiple failed login attempts are followed by successful actions.

## Strategy{% #strategy %}

This rule monitors GitLab audit events for patterns indicating brute force attacks. It tracks failed login attempts, then correlates these with any subsequent successful events from the same user account. The detection triggers when more than 5 failed login attempts are followed by at least one successful event within the evaluation window.

## Triage & Response{% #triage--response %}

- Examine the failed login attempts for `{{@usr.name}}` to determine the source IP addresses and timing patterns of the attack.
- Verify if the successful authentication following the failed attempts represents legitimate user activity or account compromise.
- Review the user account's recent activity to identify any suspicious actions performed after the successful login.
