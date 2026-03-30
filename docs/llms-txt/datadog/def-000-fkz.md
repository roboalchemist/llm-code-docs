# Source: https://docs.datadoghq.com/security/default_rules/def-000-fkz.md

---
title: Windows important scheduled task deleted or disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows important scheduled task
  deleted or disabled
---

# Windows important scheduled task deleted or disabled

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1053-scheduled-task-or-job](https://attack.mitre.org/techniques/T1053)
## Goal{% #goal %}

Detects when critical Windows system scheduled tasks are deleted or disabled.

## Strategy{% #strategy %}

This detection monitors event logs for deletion (Event ID 4699) or disabling (Event ID 4701) of critical scheduled tasks related to system security and maintenance. For deletion events, it specifically filters out service account activity by excluding events where `SubjectUserName` ends with "$". The detection looks for tasks matching specific patterns such as paths containing Windows Defender, BitLocker, System Restore, Windows Update, and other security-related scheduled tasks.

These critical scheduled tasks are essential components of Windows security infrastructure, providing functions like automated backups, malware scanning, and system updates. Tampering with these tasks could indicate defense evasion tactics being employed by threat actors attempting to weaken security controls.

## Triage & Response{% #triage--response %}

- Identify the `{{host}}` where the critical scheduled task was deleted or disabled.
- Determine which user account performed the action by reviewing the event details.
- Verify if the action was part of legitimate system maintenance or authorized activity.
- Check which specific task was affected to understand the potential security impact.
- Look for other suspicious activities on the same host, such as the creation of new scheduled tasks.
- Investigate how the user gained sufficient privileges to modify these critical tasks.
- Restore the deleted or disabled scheduled task to ensure proper system security.
- Review authentication logs to determine if the user account may have been compromised.
