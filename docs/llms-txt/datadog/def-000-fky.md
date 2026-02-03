# Source: https://docs.datadoghq.com/security/default_rules/def-000-fky.md

---
title: Tor client IP address identified within Azure environment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Tor client IP address identified within
  Azure environment
---

# Tor client IP address identified within Azure environment
Classification:attackTactic:[TA0011-command-and-control](https://attack.mitre.org/tactics/TA0011)Technique:[T1573-encrypted-channel](https://attack.mitre.org/techniques/T1573) 
## Goal{% #goal %}

Detect when Tor client activity is seen in Azure logs.

## Strategy{% #strategy %}

This rule monitors Azure logs to determine when an activity originated from a Tor client. Datadog enriches all ingested logs with [expert-curated threat intelligence](https://docs.datadoghq.com/security/cloud_siem/ingest_and_enrich/threat_intelligence/) in real time. An attacker may use a Tor client to anonymize their true origin.

## Triage and response{% #triage-and-response %}

1. Determine if the actions taken by the identity `{{@usr.id}}` are legitimate by looking at past activity and the type of API calls occurring.
1. If the results of the triage indicate that an attacker has taken the action, begin your company's incident response process and an investigation.

## Changelog{% #changelog %}

- 17 August 2023 - Updated query to replace attribute `@threat_intel.results.subcategory:tor` with `@threat_intel.results.category:tor`.
