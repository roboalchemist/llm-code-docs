# Source: https://docs.datadoghq.com/security/default_rules/def-005-syp.md

---
title: Activity observed to a malicious domain
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Activity observed to a malicious domain
---

# Activity observed to a malicious domain

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:threat-intelTactic:[TA0011-command-and-control](https://attack.mitre.org/tactics/TA0011)Technique:[T1071-application-layer-protocol](https://attack.mitre.org/techniques/T1071)
## Goal{% #goal %}

Detect activity to a malicious domain based on Datadog threat intelligence feeds.

## Strategy{% #strategy %}

This rule lets you monitor DNS events where the `@network.client.ip` value has been categorized as malicious.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@dns.question.name}}` and `@network.client.ip` are anomalous within the organization:
   - Review DNS logs to confirm the requests to the malicious domain. Look for the frequency, timing, and any associated IP addresses.
   - Determine whether the requests are automated (e.g., malware or botnet) or manual (e.g., a user clicking a malicious link).
1. If the DNS request is deemed malicious:
   - Begin your company's incident response process.
