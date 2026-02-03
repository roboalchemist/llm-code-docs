# Source: https://docs.datadoghq.com/security/default_rules/def-000-axe.md

---
title: Microsoft 365 Exchange transport rule set up to automatically forward email
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Microsoft 365 Exchange transport rule
  set up to automatically forward email
---

# Microsoft 365 Exchange transport rule set up to automatically forward email
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1114-email-collection](https://attack.mitre.org/techniques/T1114) 
## Goal{% #goal %}

Detect when a user adds or modifies an Exchange transport rule to automatically forward emails.

## Strategy{% #strategy %}

Monitor Microsoft 365 Exchange audit logs to look for the operations [`New-TransportRule`](https://learn.microsoft.com/en-us/powershell/module/exchange/new-transportrule?view=exchange-ps) or [`Set-TransportRule`](https://learn.microsoft.com/en-us/powershell/module/exchange/set-transportrule?view=exchange-ps), where a value is set for `@Parameters.BlindCopyTo` or `@Parameters.RedirectMessageTo`. Attackers often create email forwarding rules to collect sensitive information and maintain persistence in the organization.

## Triage and response{% #triage-and-response %}

1. Inspect the `@Parameters.BlindCopyTo` or `@Parameters.RedirectMessageTo` and determine if the rule is sending email to an external non-company owned domain. Additional investigation points include the following:
   - Identify the `@AppId` value, to determine if it's unusual for the user.
   - Identify if there are suspicious keywords used like 'payment' and 'invoice'.
1. Determine if there is a legitimate use case for the mail forwarding rule by contacting the user `{{@usr.email}}`.
1. If `{{@usr.email}}` is not aware of the mail forwarding rule:
   - Investigate other activities performed by the user `{{@usr.email}}` using the Cloud SIEM - User Investigation dashboard.
   - Begin your organization's incident response process and investigate.

## Changelog{% #changelog %}

- 17 August 2023 - Updated query to replace attribute `@threat_intel.results.subcategory:tor` with `@threat_intel.results.category:tor`.
- 18 December 2025 - Removed corporate VPNs as a threat intel source.
