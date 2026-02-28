# Source: https://docs.datadoghq.com/security/default_rules/def-000-yhv.md

---
title: GitHub large amount of classic personal access token use via suspicious VPN
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitHub large amount of classic personal
  access token use via suspicious VPN
---

# GitHub large amount of classic personal access token use via suspicious VPN
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detects when a GitHub personal access token is used with a non-corporate VPN to access your GitHub instance. Identifies potential unauthorized access or token compromise through anomalous client behavior.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for personal access token usage with a suspicious VPN. It tracks a high number of actions taken by a single user across unique repositories.

## Triage & Response{% #triage--response %}

- Examine the ASN for `{{@github.actor}}` to determine if it represents legitimate automation or a suspicious client.
- Verify if the token owner authorized the use of new tools or scripts that would generate different user agent strings.
- Review recent GitHub activity for the user to identify any suspicious repository access or data collection attempts.
