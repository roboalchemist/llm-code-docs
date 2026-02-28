# Source: https://docs.datadoghq.com/security/default_rules/def-000-m3t.md

---
title: Microsoft 365 Inbound Connector added or modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Microsoft 365 Inbound Connector added
  or modified
---

# Microsoft 365 Inbound Connector added or modified
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect when a user adds or modifies a Microsoft 365 Inbound Connector.

## Strategy{% #strategy %}

Monitor Microsoft 365 Exchange audit logs to look for the operation [`New-InboundConnector`](https://learn.microsoft.com/en-us/powershell/module/exchange/new-inboundconnector?view=exchange-ps) or [`Set-InboundConnector`](https://learn.microsoft.com/en-us/powershell/module/exchange/set-inboundconnector?view=exchange-ps). Connectors are used for enabling mail flow between Microsoft 365 and email servers that you have in your on-premise environment. Attackers may create a new connector to send spam or phishing emails.

## Triage and response{% #triage-and-response %}

1. Inspect the `@Parameters.SenderIPAddresses` attribute to determine if the IP addresses match known ranges.
1. Determine if there is a legitimate use case for the Inbound Connector by contacting the user `{{@usr.email}}`.
1. If `{{@usr.email}}` is not aware of the Inbound Connector:
   - Investigate other activities performed by the user `{{@usr.email}}` using the Cloud SIEM - User Investigation dashboard.
   - Begin your organization's incident response process and investigate.

## Changelog{% #changelog %}

- 17 August 2023 - Updated query to replace attribute `@threat_intel.results.subcategory:tor` with `@threat_intel.results.category:tor`.
- 18 December 2025 - Removed corporate VPNs as a threat intel source.
