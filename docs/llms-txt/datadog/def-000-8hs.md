# Source: https://docs.datadoghq.com/security/default_rules/def-000-8hs.md

---
title: Windows syskey registry keys access
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Windows syskey registry keys access
---

# Windows syskey registry keys access

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1012-query-registry](https://attack.mitre.org/techniques/T1012)
## Goal{% #goal %}

Detects access to Windows syskey registry keys, which could indicate attempts to extract system credentials or boot keys for offline credential theft.

## Strategy{% #strategy %}

This rule monitors Windows event logs for registry access events (Event IDs `4656` or `4663`) targeting specific registry keys related to the Windows syskey functionality. These registry keys store encryption information that protects credentials stored in the SAM database. Access to these keys is concerning because attackers often target them to extract the syskey/bootkey, which can then be used to decrypt password hashes from the SAM database in offline attacks.

## Triage & Response{% #triage--response %}

- Identify the user account that accessed the syskey registry keys on `{{host}}`.
- Determine if the access was part of authorized security testing or system maintenance.
- Review process information associated with the registry access to identify the responsible application.
- Check for other suspicious activities around the same timeframe, such as credential dumping tools execution or unusual file access patterns.
- Examine file creation events for evidence of registry hive exports or credential data exfiltration.
