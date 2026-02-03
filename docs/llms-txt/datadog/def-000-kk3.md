# Source: https://docs.datadoghq.com/security/default_rules/def-000-kk3.md

---
title: Tor client IP address identified in Slack
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Tor client IP address identified in
  Slack
---

# Tor client IP address identified in Slack
Classification:attackTactic:[TA0011-command-and-control](https://attack.mitre.org/tactics/TA0011)Technique:[T1090-proxy](https://attack.mitre.org/techniques/T1090) 
## Goal{% #goal %}

Detect when Tor client activity is seen in Slack audit logs.

## Strategy{% #strategy %}

This rule monitors Slack audit logs to determine when an activity had originated from a Tor client. Datadog enriches all ingested logs with [expert-curated threat intelligence](https://docs.datadoghq.com/security/cloud_siem/ingest_and_enrich/threat_intelligence/) in real time. An attacker may use a Tor client to anonymize their true origin.

## Triage and response{% #triage-and-response %}

1. Determine if the actions taken by the identity `{{@usr.email}}` are legitimate by looking at past activity and the type of logs occurring.
1. If the results of the triage indicate that an attacker has taken the action, begin your organization's incident response process and investigate.
