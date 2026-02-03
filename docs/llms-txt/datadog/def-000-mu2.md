# Source: https://docs.datadoghq.com/security/default_rules/def-000-mu2.md

---
title: Windows SMB create remote file admin share
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows SMB create remote file admin
  share
---

# Windows SMB create remote file admin share

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0008-lateral-movement](https://attack.mitre.org/tactics/TA0008)Technique:[T1021-remote-services](https://attack.mitre.org/techniques/T1021) 
## Goal{% #goal %}

Detects when a non-machine account creates files on remote administrative shares (C$).

## Strategy{% #strategy %}

This detection monitors Windows event logs for network share access events (Event ID 5145) targeting administrative shares with write access permissions. The detection specifically looks for access to C$ shares with an access mask of 0x2 (write data) while filtering out machine account activity.

Administrative shares like C$ are hidden network shares that provide full access to the system drive. They are typically used by administrators for legitimate system management but are also frequently targeted by attackers for lateral movement. By monitoring for non-machine accounts writing files to these shares, Datadog detects potential malicious file deployment across a network.

## Triage & Response{% #triage--response %}

- Identify the `{{host}}` where the administrative share access occurred.
- Determine which user account performed the file creation by reviewing the event details.
- Examine what files were created on the administrative share and assess their content.
- Check if the user account has legitimate administrative rights and business justification.
- Review authentication logs for the account to identify any suspicious logon activities.
- Examine process creation logs on both the source and destination systems.
- Isolate affected systems and remove suspicious files if unauthorized activity is confirmed.

## Changelog{% #changelog %}

- 5 August 2025 - Updated severity.
