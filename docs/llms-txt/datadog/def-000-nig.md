# Source: https://docs.datadoghq.com/security/default_rules/def-000-nig.md

---
title: Palo Alto Cortex XDR malware alert detected on multiple hosts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Palo Alto Cortex XDR malware alert
  detected on multiple hosts
---

# Palo Alto Cortex XDR malware alert detected on multiple hosts

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1204-user-execution](https://attack.mitre.org/techniques/T1204)
## Goal{% #goal %}

Detect when Palo Alto Cortex XDR raises similar alerts across multiple hosts.

## Strategy{% #strategy %}

Monitor and notify on multiple alerts reported by Palo Alto Cortex XDR across multiple hosts. See [Triage Alerts](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-Pro-Administrator-Guide/Triage-Alerts) in the Cortex Help Center for more information.

## Triage and response{% #triage-and-response %}

1. Review the data shown in the alert such as the command-line arguments (CMD) and process information.
1. Analyze the chain of execution in the [Causality View](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-Pro-Administrator-Guide/Causality-View?tocId=P~LbLfyYTq5uqm8P42H~Vg).
1. Review the [Timeline View](https://docs-cortex.paloaltonetworks.com/r/YbiZQ1gMe2U_T3gk_1iz9A/kxSYmRQ4iNaHEriVggg6Iw) of the sequence of events over time.
1. If deemed malicious, consider responding by isolating the endpoint from the network.
1. Remediate the endpoint and return the endpoint from isolation.
1. Inspect the information again to identify any behavioral details that you can use to [create a BIOC](https://docs-cortex.paloaltonetworks.com/r/YbiZQ1gMe2U_T3gk_1iz9A/RAkZHye3j~X0Wr5jA6aYOQ) rule and [create a correlation rule](https://docs-cortex.paloaltonetworks.com/r/YbiZQ1gMe2U_T3gk_1iz9A/Bac5ng7yWaJ~2EW6cWlFfw).
