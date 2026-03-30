# Source: https://docs.datadoghq.com/security/default_rules/def-000-xvd.md

---
title: Microsoft 365 eDiscovery content search started
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Microsoft 365 eDiscovery content search
  started
---

# Microsoft 365 eDiscovery content search started
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1213-data-from-information-repositories](https://attack.mitre.org/techniques/T1213)
## Goal{% #goal %}

Detect when a new content search has been created.

## Strategy{% #strategy %}

Monitor Microsoft 365 audit logs to look for the operations `SearchStarted` or `New-ComplianceSearch`. The Content Search eDiscovery feature in the Microsoft 365 Compliance portal allows users to search for email, documents, and instant messaging conversations in collaboration tools such as Microsoft Teams and Microsoft 365 Groups.

## Triage and response{% #triage-and-response %}

1. Inspect the `@Query` field to determine if the search criteria warrants further investigation.
1. Determine if there is a legitimate use case for the content search by contacting the user `{{@usr.email}}`.
1. If `{{@usr.email}}` is not aware of the content search:
   - Investigate other activities performed by the user `{{@usr.email}}` using the Cloud SIEM - User Investigation dashboard.
   - Begin your organization's incident response process and investigate.
