# Source: https://docs.datadoghq.com/security/default_rules/def-000-a7l.md

---
title: GitHub OAuth access token compromise
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > GitHub OAuth access token compromise
---

# GitHub OAuth access token compromise
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1528-steal-application-access-token](https://attack.mitre.org/techniques/T1528)
## Goal{% #goal %}

Detect when an OAuth access token is used from multiple autonomous system numbers (ASNs) and multiple user agents.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for anomalous activity related to usage of an OAuth access token. By looking at ASNs and user agents, it profiles the expected use of that OAuth token and alerts when the activity deviates from more than two ASNs or two user agents per user in the defined threshold.

## Triage and response{% #triage-and-response %}

1. Determine if the behavior is unusual for the user:
   - Is the `{{@network.client.geoip.as.name}}` different than expected? And the `{{@user_agent}}`?
   - Speak with the user to verify if the OAuth access token behavior is expected.
1. If the activity is suspicious:
   - [Block the user in GitHub](https://docs.github.com/en/enterprise-cloud@latest/communities/maintaining-your-safety-on-github/blocking-a-user-from-your-organization#blocking-a-user-in-the-organization-settings) to prevent further access.
   - Begin your organization's incident response process and investigate.

## Changelog{% #changelog %}

- 25 November 2024 - Updated to exclude common public cloud providers.
- 29 July 2025 - Updated to group by ASN domain rather than ASN name, only alert when domain information is present, and filter out use of known corporate VPNs.
