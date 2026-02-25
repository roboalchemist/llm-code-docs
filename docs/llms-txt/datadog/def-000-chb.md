# Source: https://docs.datadoghq.com/security/default_rules/def-000-chb.md

---
title: Potential Google Cloud cryptomining attack from Tor IP
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Potential Google Cloud cryptomining
  attack from Tor IP
---

# Potential Google Cloud cryptomining attack from Tor IP
Classification:attackTactic:[TA0040-impact](https://attack.mitre.org/tactics/TA0040)Technique:[T1496-resource-hijacking](https://attack.mitre.org/techniques/T1496)
## Goal{% #goal %}

Detect when a Google Compute Engine cryptomining attack is observed from a Tor IP.

## Strategy{% #strategy %}

This rule monitors Google Cloud Audit Logs to determine when a compute network creation, compute image creation, or firewall rule creation event coincides with the creation of a compute engine and originates from a Tor client. Datadog enriches all ingested logs with [expert-curated threat intelligence](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#fine-tune-security-signals-to-reduce-noise) in real time. An attacker may use a Tor client to anonymize their true origin.

## Triage and response{% #triage-and-response %}

1. Determine if the actions `{{@evt.name}}` taken by the user `{{@usr.id}}` from Tor IP address: `{{@network.client.ip}}` are legitimate by looking at past activity and the type of API calls occurring.
1. Furthermore, use the Cloud SIEM - IP Investigation & User Investigation dashboards to see if the IP address: `{{@network.client.ip}}` & `{{@usr.id}}` have taken other actions.
1. If the results of the triage indicate that an attacker has taken the action, begin your company's incident response process and investigate.

## Changelog{% #changelog %}

- 17 August 2023 - Updated query to replace attribute `@threat_intel.results.subcategory:tor` with `@threat_intel.results.category:tor`.
