# Source: https://docs.datadoghq.com/security/default_rules/def-000-kny.md

---
title: Suricata baseline deviation from expected IP requests
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Suricata baseline deviation from
  expected IP requests
---

# Suricata baseline deviation from expected IP requests
Classification:anomaly 
## Goal{% #goal %}

Detect an unusually high number of unique IP addresses connecting to a server, which could indicate a Distributed Denial-of-Service (DDoS) attack, a scanning attempt, or other forms of malicious activities.

## Strategy{% #strategy %}

Monitor Suricata logs where a server is receiving connections from an unusually high number of unique IP addresses within a short period. This detection rule aims to identify potential threats early, allowing for timely investigation and mitigation to protect server resources and maintain service availability.

## Triage and response{% #triage-and-response %}

1. Assess the reputation of the source IP addresses for known threats.
1. Check if there are common characteristics among the source IPs (e.g., geographical clustering, similar ISP).
1. If malicious, reduce the impact by rate limiting, blocking, or filtering suspicious IPs.
1. Inform IT security teams and management about the incident and actions taken.
