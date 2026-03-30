# Source: https://docs.datadoghq.com/security/default_rules/def-000-yl4.md

---
title: Slack two factor authentication requirement changed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Slack two factor authentication
  requirement changed
---

# Slack two factor authentication requirement changed
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1556-modify-authentication-process](https://attack.mitre.org/techniques/T1556)
## Goal{% #goal %}

Detect when Slacks two factor requirement has been changed.

## Strategy{% #strategy %}

This rule monitors Slack audit logs for when a two-factor requirement has been changed. Attackers may try to modify authentication processes to access user credentials or gain unauthorized access to other accounts.

## Triage and response{% #triage-and-response %}

1. Determine if the change taken by `{{@usr.email}}` is authorized.
1. If the change was not authorized or was unexpected, begin your organization's incident response process and investigate.
