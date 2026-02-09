# Source: https://docs.datadoghq.com/security/default_rules/def-000-fn6.md

---
title: Tor client IP address identified within AWS environment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Tor client IP address identified within
  AWS environment
---

# Tor client IP address identified within AWS environment
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detect when Tor client activity is seen in AWS CloudTrail management plane logs.

## Strategy{% #strategy %}

This rule monitors AWS CloudTrail management plane logs to determine when an activity had originated from a Tor client. Datadog enriches all ingested logs with [expert-curated threat intelligence](https://docs.datadoghq.com/security/cloud_siem/ingest_and_enrich/threat_intelligence/) in real time. An attacker may use a Tor client to anonymize their true origin.

## Triage and response{% #triage-and-response %}

1. Determine if the actions taken by the identity `{{@userIdentity.arn}}` are legitimate by looking at past activity and the type of API calls occurring.
1. If the results of the triage indicate that an attacker has taken the action, begin your company's incident response process and an investigation.

## Changelog{% #changelog %}

- 17 August 2023 - Updated query to replace attribute `@threat_intel.results.subcategory:tor` with `@threat_intel.results.category:tor`.
