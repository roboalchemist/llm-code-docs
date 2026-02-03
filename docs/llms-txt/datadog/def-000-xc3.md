# Source: https://docs.datadoghq.com/security/default_rules/def-000-xc3.md

---
title: GitHub repository transfer
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > GitHub repository transfer
---

# GitHub repository transfer
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1213-data-from-information-repositories](https://attack.mitre.org/techniques/T1213) 
## Goal{% #goal %}

Detect when a GitHub repository transfer occurs.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for when a GitHub organization transfer occurs. Repositories can be transferred to other users or organization accounts.

## Triage and response{% #triage-and-response %}

1. Determine if the change taken by `{{@github.actor}}` is authorized.
1. If the change was not authorized or was unexpected, begin your organization's incident response process and investigate.

- 3 January 2025 - update detection rule severity from High to Medium for the two cases.
