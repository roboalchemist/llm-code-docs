# Source: https://docs.datadoghq.com/security/default_rules/def-000-q3r.md

---
title: GitHub user blocked from accessing organization repositories
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitHub user blocked from accessing
  organization repositories
---

# GitHub user blocked from accessing organization repositories
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detect when a GitHub user has been [blocked from accessing organization repositories](https://docs.github.com/en/communities/maintaining-your-safety-on-github/blocking-a-user-from-your-organization).

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for when a GitHub user has been blocked from accessing organization repositories. Organization owners and moderators can block anyone who is not a member of the organization from collaborating on the organization's repositories.

## Triage and response{% #triage-and-response %}

1. Determine if the change taken by `{{@github.actor}}` is authorized.
1. If the change was not authorized or was unexpected, begin your organization's incident response process and investigate.
