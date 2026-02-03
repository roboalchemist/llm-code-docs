# Source: https://docs.datadoghq.com/security/default_rules/def-000-1so.md

---
title: Tor client IP address identified within Google Cloud environment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Tor client IP address identified within
  Google Cloud environment
---

# Tor client IP address identified within Google Cloud environment
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1090-proxy](https://attack.mitre.org/techniques/T1090) 
## Goal{% #goal %}

Detect when Tor client activity is seen in Google Cloud Audit Logs.

## Strategy{% #strategy %}

This rule monitors Google Cloud Audit Logs to determine when an activity had originated from a Tor client. Datadog enriches all ingested logs with [expert-curated threat intelligence](https://docs.datadoghq.com/security/cloud_siem/ingest_and_enrich/threat_intelligence/) in real time. An attacker may use a Tor client to anonymize their true origin.

## Triage and response{% #triage-and-response %}

1. Investigate other activities performed by the identity `{{@usr.id}}` using the Cloud SIEM - User Investigation dashboard.
1. If the results of the triage indicate that an attacker had taken the action, begin your company's incident response process and an investigation.

## Changelog{% #changelog %}

- 18 December 2024 - Updated query to replace attribute @threat_intel.results.subcategory:tor with @threat_intel.results.category:tor.
