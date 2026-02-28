# Source: https://docs.datadoghq.com/security/default_rules/def-001-syp.md

---
title: Login activity observed from Tor client IP
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Login activity observed from Tor client
  IP
---

# Login activity observed from Tor client IP

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:threat-intelTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1090-proxy](https://attack.mitre.org/techniques/T1090)
## Goal{% #goal %}

Detect activity observed from a Tor exit node.

## Strategy{% #strategy %}

Monitors event logs and IP address associated with the application to determine whether activity is observed from a Tor client. Datadog enriches all ingested logs with [expert-curated threat intelligence](https://docs.datadoghq.com/security/cloud_siem/ingest_and_enrich/threat_intelligence/) in real-time.

## Triage and response{% #triage-and-response %}

1. Determine if the user: `{{@usr.name}}` from IP address: `{{@network.client.ip}}` should have performed activity: `{{@evt.name}}`.
1. Investigate the user's recent activity and login history to identify potential anomalies.
1. If the activity is deemed suspicious, consider escalating the incident to the security team for further investigation and potential remediation.
