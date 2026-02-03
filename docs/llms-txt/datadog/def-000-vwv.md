# Source: https://docs.datadoghq.com/security/default_rules/def-000-vwv.md

---
title: Palo Alto Networks Firewall - crypto mining activity observed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Palo Alto Networks Firewall - crypto
  mining activity observed
---

# Palo Alto Networks Firewall - crypto mining activity observed
Classification:attackTactic:[TA0040-impact](https://attack.mitre.org/tactics/TA0040)Technique:[T1496-resource-hijacking](https://attack.mitre.org/techniques/T1496) 
## Goal{% #goal %}

Detect when Palo Alto Networks (PAN) Firewall detects cryptomining activity.

## Strategy{% #strategy %}

This rule monitors when PAN Firewall threat logs detect cryptomining activity. Threat logs display entries when traffic matches one of the [security profiles](https://docs.paloaltonetworks.com/pan-os/9-1/pan-os-admin/policy/security-profiles#id6272be37-1ce2-4374-a431-bfb1db9da9e0) attached to a security rule on the firewall.

## Triage and response{% #triage-and-response %}

1. Determine if this network traffic is expected for this host `{{host}}`.
   - Look for a consistent connections over time.
   - Work with the system owners to understand if it is normal.
   - Investigate if there are any relevant host based alerts.
1. If the network traffic is unexpected, begin your organization's incident response process and investigate.
1. If it is a false positive, consider including the IP or host in a suppression list. See [Best practices for creating detection rules with Datadog Cloud SIEM](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#fine-tune-security-signals-to-reduce-noise) for more information.
