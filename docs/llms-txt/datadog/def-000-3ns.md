# Source: https://docs.datadoghq.com/security/default_rules/def-000-3ns.md

---
title: Windows BITS transfer job downloaded to suspicious folder
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows BITS transfer job downloaded to
  suspicious folder
---

# Windows BITS transfer job downloaded to suspicious folder

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1071-application-layer-protocol](https://attack.mitre.org/techniques/T1071) 
## Goal{% #goal %}

Detects BITS transfer jobs that download files to suspicious folders such as Desktop, Public, or PerfLogs.

## Strategy{% #strategy %}

This rule monitors for Windows event ID `16403`, which records when BITS transfer jobs are created. BITS is a Windows service that provides file transfer functionality and can operate in the background and resume after interruptions. This capability is particularly concerning because BITS runs with `SYSTEM` privileges and can continue transfers even when users are logged off.

The query examines the `@Event.EventData.Data.LocalName` field to identify suspicious destination paths including Desktop, Public, or PerfLogs folders. Legitimate software rarely uses BITS to download directly to user-accessible locations such as these. Instead, most legitimate applications download to temporary locations first before moving files to their final destination.

When attackers use BITS to download files to these unusual locations, they gain immediate user visibility and execution opportunities. Downloads to locations like Desktop provide easy access to malicious payloads, while Public folders offer executable access to all users on the system.

## Triage & Response{% #triage--response %}

- Identify the specific BITS job on `{{host}}` and examine both the source URL and exact destination path in the suspicious folder.
- Determine which user account or process initiated the BITS job by reviewing the security context.
- Analyze the downloaded file for malicious content using sandbox analysis or antivirus scanning.
- Examine process creation events that might be associated with executing the downloaded file.
- Verify if other systems in the environment have similar BITS jobs downloading to suspicious locations.
- Check for persistence mechanisms established via the downloaded files, including scheduled tasks, registry autorun keys, startup folder items, and Windows services.
- Remove any suspicious BITS jobs with `Remove-BitsTransfer` and delete associated downloaded files.
- Implement application control policies to prevent execution from user-accessible folders.
