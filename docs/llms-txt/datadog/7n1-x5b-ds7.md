# Source: https://docs.datadoghq.com/security/default_rules/7n1-x5b-ds7.md

---
title: Microsoft 365 OneDrive anonymous link created
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Microsoft 365 OneDrive anonymous link
  created
---

# Microsoft 365 OneDrive anonymous link created
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1213-data-from-information-repositories](https://attack.mitre.org/techniques/T1213)
## Goal{% #goal %}

Detect when a user creates an anonymous link for a Microsoft 365 document in OneDrive. This would allow any unauthenticated user to access this document, if they had the link.

## Strategy{% #strategy %}

This rule monitors the Microsoft 365 logs for the event name `AnonymousLinkCreated`.

## Triage and response{% #triage-and-response %}

Determine whether this document should be available anonymously.

## Changelog{% #changelog %}

4 October 2022 - Updated severity.
