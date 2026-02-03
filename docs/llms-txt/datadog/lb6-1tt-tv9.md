# Source: https://docs.datadoghq.com/security/default_rules/lb6-1tt-tv9.md

---
title: Azure Active Directory risky sign-in
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Azure Active Directory risky sign-in
---

# Azure Active Directory risky sign-in
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detect whenever Azure Identity Protection categorizes an Azure Active Directory login as risky.

## Strategy{% #strategy %}

Monitor Azure Active Directory sign in activity (`@evt.name:"Sign-in activity"`) and generate a signal when Azure identifies the user as risky or compromised (`@properties.riskState:"atRisk" OR "confirmedCompromised"`).

## Triage and response{% #triage-and-response %}

1. Analyze the location (`@network.client.geoip.subdivision.name`) of `{{@usr.id}}` to determine if they're logging into from their usual location.
1. If log in activity is not legitimate, disable `{{@usr.id}}` account.
1. Investigate any devices owned by `{{@usr.id}}`.

## Changelog{% #changelog %}

14 June 2022 - Updated rule query.
