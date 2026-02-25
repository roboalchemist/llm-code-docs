# Source: https://docs.datadoghq.com/security/default_rules/def-000-uf9.md

---
title: Microsoft 365 mailbox audit logging bypass
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Microsoft 365 mailbox audit logging
  bypass
---

# Microsoft 365 mailbox audit logging bypass
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect when a user configures a mailbox audit logging bypass.

## Strategy{% #strategy %}

Monitor Microsoft 365 Exchange audit logs to look for the operation [`Set-MailboxAuditBypassAssociation`](https://learn.microsoft.com/en-us/powershell/module/exchange/set-mailboxauditbypassassociation?view=exchange-ps). When this operation is configured, no activity is logged, such as a user or account accessing or taking other actions in a mailbox. Attackers may configure this setting to evade existing defenses.

## Triage and response{% #triage-and-response %}

1. Inspect the `@Parameters.Identity` attribute to determine which user or account will bypass mailbox audit logging.
1. Determine if there is a legitimate use case for the mailbox audit bypass by contacting the user `{{@usr.email}}`.
1. If `{{@usr.email}}` is not aware of the mailbox audit bypass:
   - Investigate other activities performed by the user `{{@usr.email}}` and `@Parameters.Identity` using the Cloud SIEM - User Investigation dashboard.
   - Begin your organization's incident response process and investigate.

## Changelog{% #changelog %}

- 17 August 2023 - Updated query to replace attribute `@threat_intel.results.subcategory:tor` with `@threat_intel.results.category:tor`.
- 18 December 2025 - Removed corporate VPNs as a threat intel source.
