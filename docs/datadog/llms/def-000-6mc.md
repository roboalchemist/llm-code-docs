# Source: https://docs.datadoghq.com/security/default_rules/def-000-6mc.md

---
title: GitHub anomalous number of repositories cloned by user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitHub anomalous number of repositories
  cloned by user
---

# GitHub anomalous number of repositories cloned by user
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1213-data-from-information-repositories](https://attack.mitre.org/techniques/T1213)
## Goal{% #goal %}

Detect when a GitHub member has cloned an anomalous number of repositories.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for when a GitHub member has cloned an anomalous number of repositories. An attacker with unauthorized access or insider threat may try to clone repositories to their system in an effort to collect data for exfiltration or gaining contextual awareness of the environment.

**Note:** During the onboarding of new staff it is likely that there will be a spike in cloning activity.

## Triage and response{% #triage-and-response %}

1. Determine if the behavior is unusual for the user:
   - Is the `@actor_location.country_code` or `@http.useragent` different?
   - If IP addresses are available, is the `@network.client.ip` or `@network.client.geoip.as.domain` different than usual?
1. If the activity is suspicious:
   - [Block the user in GitHub](https://docs.github.com/en/enterprise-cloud@latest/communities/maintaining-your-safety-on-github/blocking-a-user-from-your-organization#blocking-a-user-in-the-organization-settings) to prevent further access.
   - Begin your organization's incident response process and investigate.
