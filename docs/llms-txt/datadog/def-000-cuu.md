# Source: https://docs.datadoghq.com/security/default_rules/def-000-cuu.md

---
title: Atlassian user added to organization administrative group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Atlassian user added to organization
  administrative group
---

# Atlassian user added to organization administrative group
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Detect when an Atlassian user is added to the organizational administrative group.

## Strategy{% #strategy %}

This rule monitors Atlassian organization audit logs for when a user is added to the [organizational administrative group](https://support.atlassian.com/user-management/docs/default-groups-and-permissions/). An attacker may try to assign a compromised identity to the organizational administrative group in order to elevate their privileges. This group contains users who manage all your sites and the organization.

## Triage and response{% #triage-and-response %}

1. Determine if the user `{{@usr.email}}` intended to assign the target user to the administrative group:
   - Is there a related ticket tracking this change?
   - Is `{{@usr.email}}` aware of this activity?
   - Is the network metadata associated with the activity unusual for this user?
1. If the results of the triage indicate that `{{@usr.email}}` was not aware of this activity or it did not originate from a known network, begin your company's incident response process, and start an investigation.
