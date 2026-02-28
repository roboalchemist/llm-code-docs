# Source: https://docs.datadoghq.com/security/default_rules/def-000-xw3.md

---
title: Anomalous failed SSH authentication attempts by a single IP address
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Anomalous failed SSH authentication
  attempts by a single IP address
---

# Anomalous failed SSH authentication attempts by a single IP address
Classification:anomalyTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110)
## Goal{% #goal %}

Detect when an anomalous number of failed SSH authentication attempts have been made by a single IP address.

## Strategy{% #strategy %}

This rule monitors Zeek SSH logs for when there has been an anomalous number of failed SSH authentication attempts by a single IP address. Attackers may try to brute force access to a server to gain direct or lateral access to a victim's environment.

## Triage and response{% #triage-and-response %}

1. Verify whether the client IP `{{@network.client.ip}}` is internal or external.
1. For internal IPs, identify the corresponding host and collaborate with the owner to investigate any host-based alerts, addressing potential compromises.
1. For external IPs, assess the IP address reputation, specifically looking for associations with SSH-based attacks, and determine if the destination host should be accessible via external IPs over SSH.
