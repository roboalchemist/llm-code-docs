# Source: https://docs.datadoghq.com/security/default_rules/def-000-a8k.md

---
title: Windows persistence via sticky key backdoor
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows persistence via sticky key
  backdoor
---

# Windows persistence via sticky key backdoor

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1546-event-triggered-execution](https://attack.mitre.org/techniques/T1546) 
## Goal{% #goal %}

Detects attempts to create a sticky key backdoor by replacing the legitimate sethc.exe with cmd.exe, enabling command prompt access from the login screen.

## Strategy{% #strategy %}

This rule monitors Windows command line activity for operations that replace the Windows Sticky Keys executable (sethc.exe) with the command prompt (cmd.exe). This technique, often referred to as a "sticky key backdoor", allows attackers to gain SYSTEM-level command prompt access directly from the Windows login screen without authentication by pressing the Shift key five times. The sticky key accessibility feature is designed to help users with physical disabilities, but when compromised, it becomes a powerful persistence mechanism that allows attackers to regain privileged access even after credentials are changed. This method is particularly dangerous because it operates at the login screen, before authentication, and with the highest system privileges.

## Triage & Response{% #triage--response %}

- Verify the integrity of the sethc.exe file on the affected `{{host}}` system by checking its digital signature and comparing its hash with a known good version.
- Identify which user or process executed the command to replace sethc.exe.
- Determine when the modification occurred and review other activities performed by the same user or process.
- Examine authentication logs to identify potential unauthorized access that occurred after the backdoor installation.
