# Source: https://docs.datadoghq.com/security/default_rules/def-000-vpw.md

---
title: Okta Desktop Single Sign On (DSSO) from unexpected profile source
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Okta Desktop Single Sign On (DSSO) from
  unexpected profile source
---

# Okta Desktop Single Sign On (DSSO) from unexpected profile source
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detects Okta Desktop Single Sign On through a nonâpriority profile source.

## Strategy{% #strategy %}

This rule monitors Okta authentication events for `user.authentication.dsso_via_non_priority_source` events.

The `debugContext.debugData` object contains the prioritized profile source and the actual profile source used during the DSSO attempt for `{{@debugContext.debugData.oktaUserEmail}}`.

The highest priority profile source is typically expected in this flow. The presence of this log event might be benign or might indicate an attempt to authenticate the user from a compromised `Active Directory` domain or another source that establishes user profiles in Okta.

## Triage & Response{% #triage--response %}

- Examine surrounding login events for `{{@debugContext.debugData.oktaUserEmail}}` to confirm abnormal behavior.
- Identify the profile used, `{{@debugContext.debugData.incomingProfileSourceInstanceId}}`, and validate it is trusted and expected for the organization within the Okta Admin console.
- Analyze subsequent activity by `{{@debugContext.debugData.oktaUserEmail}}` after the DSSO event, including sensitive application access or administrative changes, to evaluate risk.
- If the access event is unexpected or resulted in suspicious activities, initiate your incident response plan.
