# Source: https://docs.datadoghq.com/security/default_rules/def-000-0nh.md

---
title: DNSFilter threat request allowed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > DNSFilter threat request allowed
---

# DNSFilter threat request allowed

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0011-command-and-control](https://attack.mitre.org/tactics/TA0011)Technique:[T1071-application-layer-protocol](https://attack.mitre.org/techniques/T1071) 
## Goal{% #goal %}

Trigger an alert when allowed threat requests are detected.

## Strategy{% #strategy %}

This rule continuously monitors DNSFilter traffic logs and triggers an alert when allowed threat requests are detected. It helps identify devices that may be accessing harmful domains because of weak or misconfigured DNS policies.

## Triage and Response{% #triage-and-response %}

1. Identify the request address `{{@network.client.ip}}` making the allowed threat-flagged DNS requests and review the accessed domain.
1. Review the threat categories involved to understand the nature of the risk.
1. Check the policy `{{@policy_name}}` applied to the source to determine why these threats were not blocked.
1. If threats are severe, isolate the system, run a malware scan, and block the domain or IP.
1. Update DNSFilter blocklists or filtering policies as needed, and continue monitoring for recurring blocked activity.
1. Conduct user awareness training if needed, focusing on safe browsing habits and how to avoid suspicious links.
