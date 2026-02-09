# Source: https://docs.datadoghq.com/security/default_rules/def-000-zt4.md

---
title: Cisco Umbrella - allowed request to unsafe URL category
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Cisco Umbrella - allowed request to
  unsafe URL category
---

# Cisco Umbrella - allowed request to unsafe URL category
Classification:attackTactic:[TA0011-command-and-control](https://attack.mitre.org/tactics/TA0011)Technique:[T1071-application-layer-protocol](https://attack.mitre.org/techniques/T1071) 
## Goal{% #goal %}

Detect allowed requests to URLs associated with unsafe categories.

## Strategy{% #strategy %}

This rule monitors Cisco Umbrella proxy logs to determine when a host accesses URLs related to unsafe categories, such as Chat and Instant Messaging, Extreme content, Hacking, Illegal Activities, Illegal Downloads, Illegal Drugs, Terrorism and Violent Extremism, Child Abuse Content, Hate Speech, and Pornography. This indicates a potential risk to the network's security.

## Triage and response{% #triage-and-response %}

1. Assess whether the site identified in the logs is allowed according to the organization's acceptable use policy.
1. Contact the user associated with the device to determine if they actively browsed to the sites identified in the log.
1. If users should not be accessing the site, block the URL via Cisco Umbrella.
1. If required, begin your organization's incident response process and investigate.
