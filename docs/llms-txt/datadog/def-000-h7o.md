# Source: https://docs.datadoghq.com/security/default_rules/def-000-h7o.md

---
title: Windows device installation blocked
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Windows device installation blocked
---

# Windows device installation blocked

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1200-hardware-additions](https://attack.mitre.org/techniques/T1200)
## Goal{% #goal %}

Detects when Windows blocks hardware device installations, potentially indicating unauthorized physical access attempts.

## Strategy{% #strategy %}

Monitoring of Windows device installation events, where `@evt.id` is `6423`. This event is generated when Windows Group Policy or device installation restrictions prevent a hardware device from being installed. Blocked device installations can indicate attempts to introduce unauthorized hardware such as USB devices, network adapters, or other peripheral devices that could be used for data exfiltration, malware delivery, or establishing unauthorized network connections.

## Triage and response{% #triage-and-response %}

- Determine what type of device was blocked from installation on `{{host}}` and verify if it represents a legitimate business need.
- Check if the device installation attempt corresponds to authorized hardware deployment or maintenance activities.
- Review physical access logs and security camera footage to identify who may have attempted to connect unauthorized hardware.
- Examine the device details to assess potential security risks such as USB-based attacks or rogue network devices.
- Verify that device installation policies are properly configured and working as intended to prevent unauthorized hardware access.
