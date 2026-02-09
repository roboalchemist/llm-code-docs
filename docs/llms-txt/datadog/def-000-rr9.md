# Source: https://docs.datadoghq.com/security/default_rules/def-000-rr9.md

---
title: GitHub PAT impossible travel event correlated with new user agent observed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitHub PAT impossible travel event
  correlated with new user agent observed
---

# GitHub PAT impossible travel event correlated with new user agent observed
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detects GitHub Personal Access Token (PAT) abuse through correlation of impossible travel patterns with new user agent activity. Identifies potential credential compromise when a PAT is used from geographically impossible locations within a short timeframe alongside previously unseen user agents.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs through signal correlation, combining two detection patterns over a 2-hour evaluation window. The correlation tracks events by `@hashed_token` to identify when the same PAT exhibits both impossible travel behavior and new user agent usage.

## Triage & Response{% #triage--response %}

- Examine the geographic locations, including any relevant threat intelligence, associated with the IP address used by the PAT to verify if the travel pattern is physically impossible for the legitimate user.
- Review the new user agent strings, `{{@http.useragent}}`, detected for `{{@hashed_token}}` to determine if they represent legitimate applications or suspicious tooling.
- Identify the GitHub user account, `{{@github.actor}}`, associated with the compromised PAT and review recent repository access patterns and API calls.
- Check for any unauthorized repository cloning, code modifications, or administrative actions performed using the suspected compromised PAT.
- Verify with the legitimate PAT owner whether they recently traveled or changed their development environment to account for the geographic and user agent changes.
