# Source: https://docs.datadoghq.com/security/default_rules/def-000-w8o.md

---
title: Windows BITS transfer job download from direct IP
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows BITS transfer job download from
  direct IP
---

# Windows BITS transfer job download from direct IP

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1071-application-layer-protocol](https://attack.mitre.org/techniques/T1071) 
## Goal{% #goal %}

Detects BITS transfer jobs that download files directly from IP addresses rather than domain names.

## Strategy{% #strategy %}

This rule monitors Windows event ID `16403`, which records when BITS transfer jobs are created. BITS is a Windows service that provides file transfer functionality and can operate in the background and resume after interruptions. This capability is concerning because BITS runs with SYSTEM privileges and can continue transfers even when users are logged off.

The query focuses on the `@Event.EventData.Data.RemoteName` field, looking for URL patterns that start with HTTP or HTTPS and are followed by numeric IP addresses (beginning with digits 1-9). The detection specifically targets transfers where files are downloaded directly from IP addresses rather than domain names, while excluding private IP address ranges.

Direct IP address usage in BITS transfers is uncommon for legitimate software, as domain names provide better reliability through DNS resolution. Attackers often use direct IP addresses to avoid DNS-based detection mechanisms and to maintain access to command and control infrastructure even if domain names are blocked.

## Triage & Response{% #triage--response %}

- Examine the BITS job details on `{{host}}`, focusing on the remote URL `{{@Event.EventData.Data.RemoteName}}`, local destination path, and job status.
- Determine which user account or process initiated the BITS job and assess if it aligns with authorized activity.
- Analyze the downloaded file using sandbox analysis or antivirus scanning to detect malicious code.
- Check for unusual process executions or scheduled tasks created near the time of the BITS job creation.
- Review BITS persistence locations, including registry keys such as `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`, Windows Update service properties, and Task Scheduler entries.
- Isolate the affected system from the network if malicious activity is confirmed.
- Remove the BITS job using `Remove-BitsTransfer` and delete any downloaded malicious files.
- Block the IP address at the network perimeter to prevent future connections.
