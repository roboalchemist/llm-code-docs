# Source: https://docs.datadoghq.com/security/default_rules/def-000-tph.md

---
title: Windows remote access tool ScreenConnect file transfer
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows remote access tool
  ScreenConnect file transfer
---

# Windows remote access tool ScreenConnect file transfer

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0011-command-and-control](https://attack.mitre.org/tactics/TA0011)Technique:[T1105-ingress-tool-transfer](https://attack.mitre.org/techniques/T1105) 
## Goal{% #goal %}

Detects file transfer operations through ScreenConnect remote access software that may indicate unauthorized data movement.

## Strategy{% #strategy %}

This rule monitors ScreenConnect application events, where `@evt.id` is `201` from the `ScreenConnect` provider when `@Event.EventData.Data` contains `Transferred`, excluding legitimate elevated execution events. ScreenConnect is a legitimate remote access tool commonly used for IT support and system administration, but it can be abused by attackers for command and control activities and data exfiltration. The detection focuses on file transfer operations which may indicate unauthorized movement of sensitive data or deployment of malicious tools through the remote access session.

## Triage and response{% #triage-and-response %}

- Examine the specific files that were transferred through ScreenConnect on `{{host}}` and determine if they represent legitimate business data or potentially malicious content.
- Review the ScreenConnect session details to identify the remote user and source IP address initiating the file transfer.
- Check if the file transfer activity corresponds to authorized remote support tickets or IT maintenance activities.
- Analyze the transferred files for malicious content, sensitive data, or unauthorized software that may have been deployed or extracted.
- Verify that ScreenConnect usage follows organizational security policies and that the remote access session was properly authorized.
