# Source: https://docs.datadoghq.com/security/default_rules/def-000-u8k.md

---
title: Windows WMI backdoor exchange transport agent
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows WMI backdoor exchange transport
  agent
---

# Windows WMI backdoor exchange transport agent

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1546-event-triggered-execution](https://attack.mitre.org/techniques/T1546)
## Goal{% #goal %}

Detects suspicious child process execution from Exchange Transport Service that may indicate WMI backdoor persistence mechanisms.

## Strategy{% #strategy %}

This rule monitors Windows process creation events where `@evt.id` is `4688` when the parent process `@Event.EventData.Data.ParentProcessName` is `EdgeTransport.exe` and excludes some legitimate child processes. The Exchange Transport Service typically has a limited set of legitimate child processes for normal mail flow operations. Attackers who compromise Exchange servers often establish persistence through WMI event subscriptions or transport agent modifications that cause the transport service to spawn additional processes for backdoor access or malicious code execution.

## Triage and response{% #triage-and-response %}

- Examine the specific child process spawned by `EdgeTransport.exe` on `{{host}}` to determine if it represents legitimate Exchange functionality or malicious activity.
- Review Exchange transport agent configurations and WMI event subscriptions to identify any unauthorized modifications or suspicious entries.
- Check Exchange server logs around the time of process creation for any transport agent loading events or configuration changes.
- Analyze the command-line arguments and process behavior of the spawned child process to understand its intended functionality.
- Verify if recent Exchange server maintenance, updates, or administrative changes could account for the unusual process execution pattern.
