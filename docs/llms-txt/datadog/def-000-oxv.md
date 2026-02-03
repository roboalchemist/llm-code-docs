# Source: https://docs.datadoghq.com/security/default_rules/def-000-oxv.md

---
title: Slack data loss prevention rule modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Slack data loss prevention rule
  modified
---

# Slack data loss prevention rule modified
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Detect when a Slack DLP rule is disabled or DLP violation is deleted.

## Strategy{% #strategy %}

This rule monitors Slack audit logs for when a Slack DLP rule is disabled or DLP violation is deleted. [Slack DLP](https://slack.com/intl/en-gb/help/articles/12914005852819-Slack-Connect--Data-loss-prevention#:~:text=DLP%20admins%20can%20create%20custom,files%20from%20the%20DLP%20dashboard.) scans messages and files sent by members of your organisation in channels and direct messages for content that violates custom rules that you create.

## Triage and response{% #triage-and-response %}

1. Determine if the change taken by `{{@usr.email}}` is authorized.
1. If the change was not authorized or was unexpected, begin your organization's incident response process and investigate.

## Changelog{% #changelog %}

- 8 May 2024 - update detection rule severity from Low to Medium.
