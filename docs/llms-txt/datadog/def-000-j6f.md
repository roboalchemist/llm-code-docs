# Source: https://docs.datadoghq.com/security/default_rules/def-000-j6f.md

---
title: Cisco Umbrella - access to personal network detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Cisco Umbrella - access to personal
  network detected
---

# Cisco Umbrella - access to personal network detected
Classification:attackTactic:[TA0011-command-and-control](https://attack.mitre.org/tactics/TA0011)Technique:[T1071-application-layer-protocol](https://attack.mitre.org/techniques/T1071)
## Goal{% #goal %}

Detect allowed access to personal network through proxy.

## Strategy{% #strategy %}

This rule monitors Cisco Umbrella proxy logs to determine when a host accesses content related to personal VPNs or dynamic and residential IPs, possibly indicating that a user has accessed their personal network.

## Triage and response{% #triage-and-response %}

1. Assess whether the site identified in the logs is allowed according to the organization's acceptable use policy.
1. Contact the user associated with the device to determine if they actively browsed to the sites identified in the log.
1. If users should not be accessing the site, block the URL via Cisco Umbrella.
1. If required, begin your organization's incident response process and investigate.
