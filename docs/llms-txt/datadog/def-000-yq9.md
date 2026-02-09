# Source: https://docs.datadoghq.com/security/default_rules/def-000-yq9.md

---
title: 'Trend Micro Vision One Endpoint Security alert: Suspicious file detected'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Trend Micro Vision One Endpoint
  Security alert: Suspicious file detected
---

# Trend Micro Vision One Endpoint Security alert: Suspicious file detected

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1204-user-execution](https://attack.mitre.org/techniques/T1204) 
## Goal{% #goal %}

Identify incidents where a suspicious file is detected on an endpoint.

## Strategy{% #strategy %}

Monitor events for instances where a suspicious file is detected on an endpoint. This scenario suggests potential threats or unauthorized activities, indicating a need for further investigation to determine if the file poses a security risk or indicates a compromise. Correlate these events with file details such as type, path, and actions taken to assess the potential threat. Evaluate whether the suspicious file indicates unauthorized activity or is part of a broader compromise requiring immediate investigation.

## Triage and Response{% #triage-and-response %}

1. Identify the affected endpoint using its name (`{{@source_host_name}}`) and IP address (`{{@endpoint_ip}}`).
1. Review the file type ({{@file_type}}`) and file path (`{{@file_path}}`) to understand the nature and location of the suspicious file.
1. Determine the action taken on the file to assess any immediate impacts or threats.
1. Isolate the endpoint to prevent further potential issues related to the suspicious file.
1. Remove or quarantine the suspicious file and perform a scan to ensure no additional threats are present.
