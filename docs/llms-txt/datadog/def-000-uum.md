# Source: https://docs.datadoghq.com/security/default_rules/def-000-uum.md

---
title: Slack enterprise organization created or deleted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Slack enterprise organization created
  or deleted
---

# Slack enterprise organization created or deleted
Classification:attackTactic:[TA0040-impact](https://attack.mitre.org/tactics/TA0040)Technique:[T1531-account-access-removal](https://attack.mitre.org/techniques/T1531)
## Goal{% #goal %}

Detect when an organization has been created or deleted in Slack.

## Strategy{% #strategy %}

This rule monitors Slack audit logs for when an organization has been created or deleted.

## Triage and response{% #triage-and-response %}

1. Determine if the change taken by `{{@usr.email}}` is authorized.
1. If the change was not authorized or was unexpected, begin your organization's incident response process and investigate.

## Changelog{% #changelog %}

- 18 December 2025 - update detection rule severity from Low to High for organization deleted case.
