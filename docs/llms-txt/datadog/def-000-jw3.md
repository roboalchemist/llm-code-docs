# Source: https://docs.datadoghq.com/security/default_rules/def-000-jw3.md

---
title: Windows protected storage service access
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows protected storage service
  access
---

# Windows protected storage service access

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0008-lateral-movement](https://attack.mitre.org/tactics/TA0008)Technique:[T1021-remote-services](https://attack.mitre.org/techniques/T1021)
## Goal{% #goal %}

Detects access to the Windows Protected Storage Service (PSS), which manages sensitive user credentials and encrypted data.

## Strategy{% #strategy %}

This detection monitors Windows Security event logs for Event ID 5145 (A network share object was checked to see whether client can be granted desired access). Specifically, it looks for access to the "protected_storage" named pipe through the IPC$ share, which is commonly used for remote service interaction.

The Protected Storage Service is a critical Windows component that manages and protects sensitive data like passwords, certificates, and private keys. Attackers target this service to extract credentials stored in the system. Direct access to the protected_storage named pipe is unusual and typically indicates an attempt to interact with the service in ways that may facilitate credential theft.

## Triage & Response{% #triage--response %}

- Identify the `{{host}}` system where the Protected Storage Service access occurred.
- Determine which account attempted to access the service by reviewing the event details.
- Examine the source IP address of the connection to determine if it was local or remote.
- Check authentication logs to identify if the account was recently authenticated or potentially compromised.
- Review process execution logs to identify which process was used to access the protected storage service.
- Investigate whether the process is running with SYSTEM privileges or under a high-privilege account.
- Look for other credential theft indicators such as attempts to dump LSASS memory.
- Isolate the affected system if credential theft is suspected to prevent further lateral movement.
- Reset passwords for accounts that may have had credentials stored in the Protected Storage Service.

## Changelog{% #changelog %}

- 5 August 2025 - Updated severity.
