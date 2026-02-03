# Source: https://docs.datadoghq.com/security/default_rules/def-000-dca.md

---
title: GitHub personal access token used by previously unseen user agent
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitHub personal access token used by
  previously unseen user agent
---

# GitHub personal access token used by previously unseen user agent
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1213-data-from-information-repositories](https://attack.mitre.org/techniques/T1213) 
## Goal{% #goal %}

Detects when a GitHub personal access token is used by a previously unseen user agent. Identifies potential unauthorized access or token compromise through anomalous client behavior.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for personal access token usage with new user agents. It tracks `@http.useragent` values grouped by `@hashed_token` to establish baseline user agent patterns for each token over a 7-day learning period. The detection triggers when a personal access token (classic or fine-grained) is used with a user agent that hasn't been observed before.

## Triage & Response{% #triage--response %}

- Examine the new user agent string for `{{@github.actor}}` to determine if it represents legitimate automation or a suspicious client.
- Verify if the token owner authorized the use of new tools or scripts that would generate different user agent strings.
- Review recent GitHub activity for the user to identify any suspicious repository access or data collection attempts.
