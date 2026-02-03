# Source: https://docs.datadoghq.com/security/default_rules/def-000-ddt.md

---
title: 'Trend Micro Vision One Endpoint Security alert: Spyware or grayware detected'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Trend Micro Vision One Endpoint
  Security alert: Spyware or grayware detected
---

# Trend Micro Vision One Endpoint Security alert: Spyware or grayware detected

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1204-user-execution](https://attack.mitre.org/techniques/T1204) 
## Goal{% #goal %}

Detect incidents where spyware or grayware has been identified on endpoints.

## Strategy{% #strategy %}

Monitor alerts from Trend Micro Vision One Endpoint Security for detections of spyware or grayware. This indicates potential privacy breaches, unwanted monitoring, or less severe but still significant threats that can compromise endpoint security and user privacy. Correlate these alerts to evaluate the scope and impact, pinpointing the affected endpoints and understanding the potential threat vectors. This helps in assessing the seriousness of the threat and planning appropriate remediation actions.

## Triage and Response{% #triage-and-response %}

1. Identify the affected endpoint using its name (`{{@source_host_name}}`) and IP address (`{{@endpoint_ip}}`).
1. Review the virus name (`{{@virus_name}}`) to understand the specific spyware or grayware detected.
1. Isolate the affected endpoint to prevent any potential spread or further compromise.
1. Remove or quarantine the detected spyware or grayware to mitigate risks.
1. Perform a thorough scan on the endpoint to ensure no additional threats are present.
