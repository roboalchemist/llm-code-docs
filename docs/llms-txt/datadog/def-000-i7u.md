# Source: https://docs.datadoghq.com/security/default_rules/def-000-i7u.md

---
title: DNSFilter high volume of `ANY` requests from a source
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > DNSFilter high volume of `ANY` requests
  from a source
---

# DNSFilter high volume of `ANY` requests from a source

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0011-command-and-control](https://attack.mitre.org/tactics/TA0011)Technique:[T1071-application-layer-protocol](https://attack.mitre.org/techniques/T1071) 
## Goal{% #goal %}

Trigger an alert when a high volume of ANY type allowed requests is detected from a source.

## Strategy{% #strategy %}

This rule continuously monitors DNSFilter Traffic logs and triggers an alert when a high volume of allowed ANY-type requests is detected from a source. It helps identify devices that are sending an unusually high number of DNS queries using the **ANY** request type. A high volume of ANY type DNS requests may indicate DNS amplification attacks, as legitimate clients rarely use ANY queries in large volumes.

## Triage and Response{% #triage-and-response %}

1. Review DNSFilter Traffic logs to identify the source associated with generation of the high number of **ANY**-type DNS queries.
1. Analyze domain, user `{{@usr.name}}`, and policy `{{@policy_name}}` to understand patterns, user info, and policy related to this behavior.
1. If malicious domains are identified, isolate the device, perform a malware scan, and block associated domains or IPs.
1. Update DNSFilter blocklists or filtering policies as needed, and continue monitoring for recurring blocked activity.
