# Source: https://docs.datadoghq.com/security/default_rules/def-000-n8u.md

---
title: Windows DHCP server error loaded CallOut DLL
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows DHCP server error loaded
  CallOut DLL
---

# Windows DHCP server error loaded CallOut DLL

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1574-hijack-execution-flow](https://attack.mitre.org/techniques/T1574) 
## Goal{% #goal %}

Detects Windows DHCP server errors when loading CallOut DLLs that may indicate DLL hijacking attempts targeting DHCP services.

## Strategy{% #strategy %}

This rule monitors Windows event logs where `@evt.id` is `1031`, `1032`, or `1034` from the `Microsoft-Windows-DHCP-Server` provider. These events indicate failures in the DHCP server's CallOut DLL operations, which can occur when attackers attempt to hijack the execution flow by placing malicious DLLs in locations where the DHCP server expects to find legitimate CallOut DLLs. CallOut DLLs are third-party extensions that provide additional functionality to DHCP servers, making them attractive targets for persistence and privilege escalation attacks.

## Triage and response{% #triage-and-response %}

- Examine the specific DHCP server error details on `{{host}}` to identify which CallOut DLL failed to load and the associated error code.
- Verify the legitimacy of any recently added or modified DLL files in DHCP server directories and common DLL search paths.
- Review recent system changes including software installations, updates, or configuration modifications that could have affected DHCP CallOut DLL functionality.
- Check for unusual process executions or file modifications in DHCP-related directories prior to the error events.
- Determine if the DHCP server errors correlate with any legitimate maintenance activities or if they represent unauthorized modification attempts.
