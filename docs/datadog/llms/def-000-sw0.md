# Source: https://docs.datadoghq.com/security/default_rules/def-000-sw0.md

---
title: Windows VolumeShadowCopy symlink creation via mklink
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows VolumeShadowCopy symlink
  creation via mklink
---

# Windows VolumeShadowCopy symlink creation via mklink

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1003-os-credential-dumping](https://attack.mitre.org/techniques/T1003)
## Goal{% #goal %}

Detects the creation of symbolic links to Volume Shadow Copies, which may indicate attempts to access or extract sensitive files and credentials from shadow copy backups.

## Strategy{% #strategy %}

This rule monitors Windows event logs for command line executions that create symbolic links (using the mklink command) to Volume Shadow Copy locations. The detection specifically looks for command lines containing both "mklink" and "HarddiskVolumeShadowCopy" strings. Attackers often use this technique to access files that are locked or in use by the operating system, typically for credential theft.

## Triage & Response{% #triage--response %}

- Examine the full command line to determine the symbolic link created and which Volume Shadow Copy was targeted on `{{host}}`.
- Identify the user account that executed the mklink command to determine if they are authorized to access shadow copies.
- Check for subsequent file access or copy operations that might indicate exfiltration of sensitive data from the shadow copies.
- Review the process ancestry to understand how the command was initiated and in what context.
- Look for evidence of credential dumping tools being used in conjunction with the shadow copy access.
