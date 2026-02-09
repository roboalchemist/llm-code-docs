# Source: https://docs.datadoghq.com/security/default_rules/def-000-6er.md

---
title: Suricata high number of requests detected from single IP address
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Suricata high number of requests
  detected from single IP address
---

# Suricata high number of requests detected from single IP address
Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110) 
## Goal{% #goal %}

Detect an unusually high number of requests are made from a single IP address, which could indicate a potential brute force attack, Denial-of-Service (DoS) attempt, or other malicious activities aimed at overwhelming or exploiting the server.

## Strategy{% #strategy %}

Monitor Suricata logs where a single IP address generates a high number of requests within a short period. This detection rule aims to identify potential threats early, allowing for timely investigation and mitigation to protect server resources and maintain service availability.

## Triage and response{% #triage-and-response %}

1. Analyse the pattern and volume of requests to distinguish between legitimate traffic and potential attacks.
1. Investigate the source IP `{{@network.client.ip}}` address to determine if the activity is malicious.
1. Implement immediate measures to block or limit the impact of the suspicious activity if confirmed as a threat.
