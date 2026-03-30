# Source: https://docs.datadoghq.com/security/default_rules/def-000-ocy.md

---
title: iboss allowed malware activity detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > iboss allowed malware activity detected
---

# iboss allowed malware activity detected

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1204-user-execution](https://attack.mitre.org/techniques/T1204)
## Goal{% #goal %}

Detects instances where malware was detected but allowed through the iboss security gateway, potentially exposing endpoints to infection.

## Strategy{% #strategy %}

Monitor security events with iboss to identify risky traffic and exposed users or devices where malicious content is allowed.

## Triage and Response{% #triage-and-response %}

1. Identify the user `{{@usr.name}}` and the device `{{@computerName}}` involved in the malware-allowed event.
1. Review the client IP address `{{@network.client.ip}}` for any signs of suspicious or malicious activity.
1. Isolate the endpoint if necessary, perform a malware scan, and apply remediation steps.
1. Investigate potential policy gaps or misconfigurations that allowed the threat.
