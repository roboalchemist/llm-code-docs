# Source: https://docs.datadoghq.com/security/default_rules/def-000-cro.md

---
title: GitHub personal access token impossible travel detected from suspicious IP
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitHub personal access token impossible
  travel detected from suspicious IP
---

# GitHub personal access token impossible travel detected from suspicious IP
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detects GitHub Personal Access Token (PAT) usage from suspicious IP addresses with impossible travel patterns. Identifies potential credential theft when PATs are used from geographically distant locations within an impossible timeframe.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for personal access token usage from IP addresses flagged by threat intelligence as suspicious or malicious. The detection uses impossible travel analysis to identify when the same `@hashed_token` is used from locations that are geographically impossible to travel between within the observed timeframe.

## Triage & Response{% #triage--response %}

- Examine the GitHub audit logs for `{{@hashed_token}}` to identify all recent authentication events and determine the geographic locations involved in the impossible travel pattern.
- Review the threat intelligence context for the suspicious IP addresses to understand the nature of the threat and potential attack campaigns.
- Identify the GitHub user account associated with the personal access token and verify if the token usage from distant locations was authorized.
- Check for any repository access, code changes, or administrative actions performed using the compromised token during the suspicious activity timeframe.
- If malicious behavior is identified, revoke the compromised personal access token immediately and generate a new token with minimal required permissions for the user.
