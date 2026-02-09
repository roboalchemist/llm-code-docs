# Source: https://docs.datadoghq.com/security/default_rules/def-000-a1l.md

---
title: GitHub PR review enforcement removed for main
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitHub PR review enforcement removed
  for main
---

# GitHub PR review enforcement removed for main
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Detects when a Github pull request review enforcement level is deactivated for a protected branch.

## Strategy{% #strategy %}

Monitor events related to changes in branch protection rules in GitHub repositories. Specifically, look for actions indicating that required pull request (PR) review enforcement has been disabled for a protected branch.

## Triage and Response{% #triage-and-response %}

1. Identify whether `{{@github.actor}}` should be disabling the PR review enforcement for `{{@name}}` branch in the `{{@github.repository}}` repository.
1. If the activity is suspicious:
   - [Block the user in GitHub](https://docs.github.com/en/enterprise-cloud@latest/communities/maintaining-your-safety-on-github/blocking-a-user-from-your-organization#blocking-a-user-in-the-organization-settings) to prevent further access.
   - Begin your organization's incident response process and investigate.
