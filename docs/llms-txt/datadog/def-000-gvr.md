# Source: https://docs.datadoghq.com/security/default_rules/def-000-gvr.md

---
title: Windows critical hive in suspicious location access bits cleared
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows critical hive in suspicious
  location access bits cleared
---

# Windows critical hive in suspicious location access bits cleared

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1003-os-credential-dumping](https://attack.mitre.org/techniques/T1003)
## Goal{% #goal %}

Detects when critical registry hives containing credentials are copied to temporary locations and have their access bits cleared.

## Strategy{% #strategy %}

This rule monitors Windows Kernel-General events where `@evt.id` is `16` when the `@Event.EventData.Data.HiveName` contains references to `SAM` or `SECURITY` registry hives in temporary file paths. When attackers dump credentials from Windows systems, they often copy critical registry hives like `SAM` and `SECURITY` to temporary locations to avoid file locks, then clear the access bits before extraction. This technique is commonly used by credential dumping tools to access password hashes and security secrets stored in these protected registry hives.

## Triage and response{% #triage-and-response %}

- Examine the temporary file path containing the copied registry hive on `{{host}}` to determine if the files still exist and analyze their contents.
- Check for credential dumping tool execution or suspicious process activity around the same timeframe as the hive access.
- Review system and security logs for signs of unauthorized access or privilege escalation that may have enabled the registry hive copying.
- Analyze network activity for potential exfiltration of credential data following the hive access.
- Force password resets for local and domain accounts that may have been compromised through credential extraction.
