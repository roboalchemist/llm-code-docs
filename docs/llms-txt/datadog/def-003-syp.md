# Source: https://docs.datadoghq.com/security/default_rules/def-003-syp.md

---
title: Activity observed from malicious IP
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Activity observed from malicious IP
---

# Activity observed from malicious IP

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:threat-intelTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detect activity from a malicious IP address based on Datadog threat intelligence feeds.

## Strategy{% #strategy %}

This rule lets you monitor events where the `@evt.outcome` is successful and the `@network.client.ip` value has been categorized as malicious.

## Triage and response{% #triage-and-response %}

1. Determine if the source IP `{{@network.client.ip}}` is anomalous within the organization:
   - Is the geo-location, ASN, or domain uncommon for the organization?
   - Use the Cloud SIEM - IP Investigation dashboard to see if the IP address has taken other actions.
1. Investigate the `@evt.name` field to determine the actions taken and potential severity of a compromise.
1. If the IP is deemed malicious:
   - Confirm that no successful authentication attempts have been made.
   - If a successful authentication attempt is observed, begin your company's incident response process.
