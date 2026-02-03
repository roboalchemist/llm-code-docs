# Source: https://docs.datadoghq.com/security/default_rules/gh5-qhe-h9m.md

---
title: Microsoft 365 SharePoint object shared with guest
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Microsoft 365 SharePoint object shared
  with guest
---

# Microsoft 365 SharePoint object shared with guest
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1213-data-from-information-repositories](https://attack.mitre.org/techniques/T1213) 
## Goal{% #goal %}

Detect when a user shares a Microsoft 365 Sharepoint document with a guest.

## Strategy{% #strategy %}

This rule monitors the Microsoft 365 logs for the event name `SharingInvitationCreated` when the `TargetUserOrGroupType` is `Guest`.

## Triage and response{% #triage-and-response %}

Determine whether this document should be shared with the external user.
