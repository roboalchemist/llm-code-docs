# Source: https://docs.datadoghq.com/security/default_rules/def-000-eaa.md

---
title: Brute force attack detected against user account
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Brute force attack detected against
  user account
---

# Brute force attack detected against user account

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110) 
## Goal{% #goal %}

Detects successful brute force attacks against user accounts.

## Strategy{% #strategy %}

This rule monitors authentication logs across multiple platforms including Okta, AWS CloudTrail, Auth0, Microsoft 365. The detection logic identifies patterns where a user account has 10 or more failed login attempts within a 15-minute window, followed by at least one successful login for the same user account.

This pattern typically indicates an attacker successfully compromising credentials after multiple failed attempts, suggesting credential stuffing, password spraying, or traditional brute force attacks that eventually succeeded.

## Triage & Response{% #triage--response %}

- Examine the timeline of failed and successful login attempts for `{{@ocsf.actor.user.name}}` to understand the attack pattern and duration.
- Review the source IP addresses (`{{@ocsf.src_endpoint.ip}}`) and geographic locations of both failed and successful login attempts to identify suspicious access patterns.
- Check if the successful login occurred from the same IP address as the failed attempts or from a different location.
- Determine if `{{@ocsf.actor.user.name}}` has reported any suspicious activity or if the account shows signs of compromise.
- Verify the legitimacy of the successful login by contacting the user account owner directly through alternative communication channels.
- Review recent account activity after the successful login to identify any unauthorized actions or changes made to the compromised account.
- Check for concurrent login attempts against other user accounts from the same source IP addresses to identify broader attack campaigns.
