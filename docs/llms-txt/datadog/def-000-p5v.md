# Source: https://docs.datadoghq.com/security/default_rules/def-000-p5v.md

---
title: GitHub personal access token (PAT) auto approve policy modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitHub personal access token (PAT) auto
  approve policy modified
---

# GitHub personal access token (PAT) auto approve policy modified
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect when a GitHub personal access token is set to auto approve.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for when a GitHub organization changes the auto approval policy on personal access tokens. Changes in personal access token (PAT) settings can be a sign of persistence from an actor that is generating PATs to maintain access to repositories.

## Triage and response{% #triage-and-response %}

1. Determine if the change taken by `{{@github.actor}}` is authorized.
1. If the change was not authorized or was unexpected, begin your organization's incident response process and investigate.
