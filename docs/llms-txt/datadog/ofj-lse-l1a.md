# Source: https://docs.datadoghq.com/security/default_rules/ofj-lse-l1a.md

---
title: Azure New Owner added to Azure Active Directory application
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure New Owner added to Azure Active
  Directory application
---

# Azure New Owner added to Azure Active Directory application
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detect when a user is added as a new owner for an Active Directory application which could be used as a persistence mechanism.

## Strategy{% #strategy %}

Monitor Azure Active Directory logs for `@evt.name: "Add owner to application"` has an `@evt.outcome` of `success`.

## Triage and response{% #triage-and-response %}

1. Review evidence of anomalous activity for the user being added as an owner (`@properties.targetResources`) for the Active Directory application.
1. Determine if there is a legitimate reason for the user being added to the application.
