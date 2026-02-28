# Source: https://docs.datadoghq.com/security/default_rules/def-000-p9l.md

---
title: >-
  GitHub personal access token granted and used to clone large amount of
  repositories
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitHub personal access token granted
  and used to clone large amount of repositories
---

# GitHub personal access token granted and used to clone large amount of repositories
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect when a GitHub personal access token is used to clone repositories.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for when a personal access token is used to clone a repository. If a user clones five repositories, a medium severity alert is generated. If the a user clones ten or more repositories, a high severity alert is generated.

## Triage and response{% #triage-and-response %}

1. Determine if the multiple repository clones by `{{@github.actor}}` are an expected action.
1. If the change was not authorized or was unexpected, begin your organization's incident response process and investigate.

## Changelog{% #changelog %}

- 3 January 2025 - update detection rule severity from High to Medium and Medium to Low for the respective cases.
- 21 August 2025 - Updated rule query to filter on successful creation events only and count by distinct repositories affected.
