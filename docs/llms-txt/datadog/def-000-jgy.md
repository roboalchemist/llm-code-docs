# Source: https://docs.datadoghq.com/security/default_rules/def-000-jgy.md

---
title: Microsoft 365 SendAs permissions added
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Microsoft 365 SendAs permissions added
---

# Microsoft 365 SendAs permissions added
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Detect when a user adds SendAs permissions.

## Strategy{% #strategy %}

Monitor Microsoft 365 audit logs to look for the operation [`Add-RecipientPermission`](https://learn.microsoft.com/en-us/powershell/module/exchange/add-recipientpermission?view=exchange-ps). SendAs permission allows a user or group members to send messages that appear to come from the specified mailbox, mail contact, mail user, or group. Attackers may configure this to allow them to impersonate a user and send messages on their behalf from their mailbox, allowing the attacker to persist in the organization or move laterally by phishing other users.

## Triage and response{% #triage-and-response %}

1. Inspect the `@Parameters.Trustee` field to determine if the email address is external to your organization.
1. Determine if there is a legitimate use case for adding SendAs permissions by contacting the user `{{@usr.email}}`.
1. If `{{@usr.email}}` is not aware of the action:
   - Investigate other activities performed by users at the following attributes `@usr.email`, `@Parameters.Trustee` and `@Parameters.Identity` using the Cloud SIEM - User Investigation dashboard.
   - Begin your organization's incident response process and investigate.

## Changelog{% #changelog %}

- 17 August 2023 - Updated query to replace attribute `@threat_intel.results.subcategory:tor` with `@threat_intel.results.category:tor`.
- 18 December 2025 - Removed corporate VPNs as a threat intel source.
