# Source: https://docs.datadoghq.com/security/default_rules/def-000-kfa.md

---
title: Anomalous amount of failed sign-in attempts by 1Password user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Anomalous amount of failed sign-in
  attempts by 1Password user
---

# Anomalous amount of failed sign-in attempts by 1Password user
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detect failed sign-in attempts from a 1Password user.

## Strategy{% #strategy %}

This rule monitors 1Password logs to identify when an user generates an anomalous amount of failed sign-in events.

## Triage and response{% #triage-and-response %}

Investigate and determine if user `{{@usr.email}}` with failed sign-in events `{{@evt.outcome}}`, attempting to authenticate from IP address `{{@network.client.ip}}` should have access.

## Changelog{% #changelog %}

Updated query by replacing `@evt.category:*failed*` with `@evt.outcome:*failed*`.
