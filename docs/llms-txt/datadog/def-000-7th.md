# Source: https://docs.datadoghq.com/security/default_rules/def-000-7th.md

---
title: Atlassian Tor client activity detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Atlassian Tor client activity detected
---

# Atlassian Tor client activity detected
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detect when Tor client activity is seen in Atlassian audit logs.

## Strategy{% #strategy %}

This rule monitors Atlassian audit logs to determine when an activity had originated from a Tor client. Datadog enriches all ingested logs with [expert-curated threat intelligence](https://docs.datadoghq.com/security/cloud_siem/ingest_and_enrich/threat_intelligence/) in real time. An attacker may use a Tor client to anonymize their true origin.

## Triage and response{% #triage-and-response %}

1. Determine if the actions taken by the identity `{{@usr.email}}` are legitimate by looking at past activity and the type of logs occurring.
1. If the results of the triage indicate that `{{@usr.email}}` was not aware of this activity, begin your company's incident response process, and start an investigation.
