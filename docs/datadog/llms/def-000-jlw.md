# Source: https://docs.datadoghq.com/security/default_rules/def-000-jlw.md

---
title: Suricata high number of bytes out detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Suricata high number of bytes out
  detected
---

# Suricata high number of bytes out detected
Classification:attackTactic:[TA0010-exfiltration](https://attack.mitre.org/tactics/TA0010)
## Goal{% #goal %}

Detect scenarios where an unusually high number of bytes are being sent out from a server, which could indicate data exfiltration or other malicious activities.

## Strategy{% #strategy %}

Monitor Suricata logs where the outgoing data from a server seems unusual. This could be indicative of data exfiltration attempts, malware communication, or other suspicious activities that require immediate investigation.

## Triage and response{% #triage-and-response %}

1. Identify if the server typically handles high volumes of outbound traffic.
1. Verify whether the Client IP `{{@network.client.ip}}` is internal or external.
   - For internal IPs, identify the corresponding host and collaborate with the owner to investigate the unusual data transfer from the server.
   - For external IPs, assess the IP address reputation.
1. Review Client's IP `{{@network.client.ip}}`, port `{{@network.client.port}}`, and protocol `{{@suricata.proto}}` to identify unexpected destinations or sensitive data transfers.
1. If malicious activity is confirmed, block Client IP `{{@network.client.ip}}`, isolate the server, and capture traffic for analysis.
1. Inform IT security teams and management about the incident and actions taken.
