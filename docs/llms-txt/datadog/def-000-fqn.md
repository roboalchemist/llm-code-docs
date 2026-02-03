# Source: https://docs.datadoghq.com/security/default_rules/def-000-fqn.md

---
title: Windows malware protection engine crash
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Windows malware protection engine crash
---

# Windows malware protection engine crash

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1211-exploitation-for-defense-evasion](https://attack.mitre.org/techniques/T1211) 
## Goal{% #goal %}

Detects when the Windows Malware Protection Engine (MsMpEng) crashes.

## Strategy{% #strategy %}

This detection monitors Windows Error Reporting events where Event ID 1001 is recorded specifically targeting crashes related to the Malware Protection Engine processes. The detection looks for either "MsMpEng" or "mpengine" strings in the error report data, which are associated with the Windows Defender antivirus engine.

The Windows Malware Protection Engine is a critical security component responsible for scanning, detecting, and preventing malware infections. While occasional crashes may occur due to software issues, repeated or suspicious crashes could indicate exploitation attempts or deliberate tampering. Attackers may target antivirus components to disable security protections before deploying additional malicious code.

## Triage & Response{% #triage--response %}

- Identify the `{{host}}` where the Malware Protection Engine crash occurred.
- Review the crash details in the Windows Error Reporting event to determine the potential cause.
- Check if multiple crashes have occurred within a short timeframe, which may indicate a deliberate attack.
- Verify if Windows Defender is still running and functioning correctly on the affected system.
- Examine system logs for other suspicious activities occurring before or after the crash.
- Look for evidence of exploit attempts targeting Windows Defender vulnerabilities.
- Monitor for subsequent attempts to install malware or execute suspicious code.
- Ensure Windows Defender is properly restarted and updated to the latest version.
- Check for recently installed applications or system changes that might be causing conflicts.

## Changelog{% #changelog %}

- 5 August 2025 - Updated severity.
