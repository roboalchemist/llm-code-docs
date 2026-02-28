# Source: https://docs.datadoghq.com/security/default_rules/def-000-syp.md

---
title: 1Password activity observed from Tor client IP
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > 1Password activity observed from Tor
  client IP
---

# 1Password activity observed from Tor client IP
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detect when 1Password activity is observed from a Tor exit node.

## Strategy{% #strategy %}

This rule monitors 1Password logs to determine when an activity originated from a Tor client. Datadog enriches all ingested logs with [expert-curated threat intelligence](https://docs.datadoghq.com/security/cloud_siem/ingest_and_enrich/threat_intelligence/) in real-time. An attacker may use a Tor client to anonymize their true origin.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@usr.email}}` from IP address `{{@network.client.ip}}` should have made the `{{@evt.name}}` API call.
1. If the results of the triage indicate that an attacker has taken the action, begin your company's incident response process and an investigation.

## Changelog{% #changelog %}

- 17 August 2023 - Updated query to replace attribute `@threat_intel.results.subcategory:tor` with `@threat_intel.results.category:tor`.
