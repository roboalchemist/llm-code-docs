# Source: https://docs.datadoghq.com/security/default_rules/def-000-ak0.md

---
title: Fortinet Fortimanager alert
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Fortinet Fortimanager alert
---

# Fortinet Fortimanager alert

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attack 
## Goal{% #goal %}

Detects security threats identified by Fortinet FortiManager UTM security products including malware infections, intrusion attempts, network anomalies, and data loss prevention violations.

## Strategy{% #strategy %}

This rule monitors Fortinet FortiManager UTM security events where protective actions were not automatically taken. It aggregates security alerts from multiple FortiManager security modules including antivirus, intrusion prevention system, anomaly detection, and data loss prevention. The detection focuses on events where threats were detected but not blocked, dropped, or cleared, indicating potential security incidents that require investigation.

## Triage & Response{% #triage--response %}

- Examine the specific threat type detected by reviewing the `{{@eventtype}}` and `{{@subtype}}` fields to understand the nature of the security event.
- Investigate the affected systems by analyzing traffic patterns to and from `{{@network.destination.ip}}` or `{{@network.client.ip}}` depending on the event type.
- Validate the legitimacy of the flagged activity by examining the specific signatures, files, or data involved in the security event.
- Check for additional security events involving the same IP addresses or hosts to identify potential compromise or ongoing attack campaigns.
- Assess the potential impact based on the severity level and implement appropriate containment measures if malicious activity is confirmed.
- Review why the FortiManager security control did not automatically block or mitigate the detected threat.
