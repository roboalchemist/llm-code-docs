# Source: https://docs.datadoghq.com/security/default_rules/def-000-4hw.md

---
title: Google Workspace Tor client detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Google Workspace Tor client detected
---

# Google Workspace Tor client detected
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1090-proxy](https://attack.mitre.org/techniques/T1090) 
## Goal{% #goal %}

Detect when Tor client activity is seen in Google Workspace.

## Strategy{% #strategy %}

This rule monitors Google Workspace logs to determine when an activity originated from a Tor client. Datadog enriches all ingested logs with [expert-curated threat intelligence](https://docs.datadoghq.com/security/cloud_siem/ingest_and_enrich/threat_intelligence/) in real time. An attacker may use a Tor client to anonymize their true origin.

## Triage and response{% #triage-and-response %}

1. Determine if the actions taken by the identity `{{@usr.email}}` are legitimate by looking at past activity and the type of API calls occurring.
1. If the results of the triage indicate that an attacker has taken the action, begin your company's incident response process and an investigation.

## Changelog{% #changelog %}

- 17 August 2023 - Updated query to replace attribute `@threat_intel.results.subcategory:tor` with `@threat_intel.results.category:tor`.
