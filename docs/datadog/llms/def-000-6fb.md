# Source: https://docs.datadoghq.com/security/default_rules/def-000-6fb.md

---
title: GitHub SSH key added by suspicious IP
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > GitHub SSH key added by suspicious IP
---

# GitHub SSH key added by suspicious IP
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Detect when a SSH key has been added from a suspicious IP.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for when a SSH key has been added from a suspicious IP. A [phishing campaign](https://github.blog/2022-09-21-security-alert-new-phishing-campaign-targets-github-users/) reported by Github's security team indicated that attackers may try to add a SSH key once they have gained unauthorized access to an account to maintain access. Using [Datadog threat intelligence](https://www.datadoghq.com/blog/datadog-threat-intelligence/) the signals raised will have originated from IP addresses deemed to be suspicious.

**Note:** By default GitHub does not display the source IP address for events in your organization's audit log. See this [post](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/displaying-ip-addresses-in-the-audit-log-for-your-organization) for further information.

## Triage and response{% #triage-and-response %}

1. Determine if the behavior is unusual for the user:
   - Is the `@actor_location.country_code` or `@http.useragent` different?
   - If IP addresses are available, is the `@network.client.ip` or `@network.client.geoip.as.domain` different than usual?
   - Speak with the user to verify if they added the SSH key.
1. If the activity is suspicious:
   - [Block the user in GitHub](https://docs.github.com/en/enterprise-cloud@latest/communities/maintaining-your-safety-on-github/blocking-a-user-from-your-organization#blocking-a-user-in-the-organization-settings) to prevent further access.
   - Begin your organization's incident response process and investigate.
