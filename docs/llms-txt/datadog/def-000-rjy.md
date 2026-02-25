# Source: https://docs.datadoghq.com/security/default_rules/def-000-rjy.md

---
title: Azure AD sign in from AADinternals default user agent
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure AD sign in from AADinternals
  default user agent
---

# Azure AD sign in from AADinternals default user agent
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1059-command-and-scripting-interpreter](https://attack.mitre.org/techniques/T1059)
## Goal{% #goal %}

Detect when the [AADInternals](https://aadinternals.com/aadinternals/#introduction) default user agent is seen in Azure AD sign-in logs.

## Strategy{% #strategy %}

This rule monitors Azure AD sign-in logs for the default user agent `AADInternals` (this default user agent can be altered). AADInternals toolkit is a PowerShell module containing tools for administering and exploiting Azure AD and Office 365. It is listed in MITRE ATT&CK with id [S0677](https://attack.mitre.org/software/S0677/) and has been associated with a number of threat groups.

## Triage and response{% #triage-and-response %}

1. Determine if your organization has authorized the use of the AADInternals toolkit.
1. If the results of triage indicate that this tool is not used by your organization, begin your company's incident response process and an investigation.
   - If appropriate, disable the affected identity and revoke any sign-in sessions.
   - Investigate any actions taken by the identity `{{@usr.id}}` during the identified time frame.
