# Source: https://docs.datadoghq.com/security/default_rules/def-000-ce3.md

---
title: Windows MSI installation from web
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Windows MSI installation from web
---

# Windows MSI installation from web

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1218-system-binary-proxy-execution](https://attack.mitre.org/techniques/T1218)
## Goal{% #goal %}

Detects Windows Installer package installations initiated directly from web URLs, potentially indicating malicious software distribution.

## Strategy{% #strategy %}

This rule monitors Windows MSI Installer events where `@evt.id` is `1040` from the `MsiInstaller` provider when `@Event.EventData.Data` contains URL patterns (`://`), excluding legitimate Datadog agent installations. Direct MSI installation from web URLs can indicate malicious software distribution where attackers host malicious installer packages on remote servers and trick users into executing them. This technique bypasses traditional file-based detection methods since the malicious code is executed directly from a web resource without being written to disk first.

## Triage and response{% #triage-and-response %}

- Examine the source URL and determine if it represents a legitimate software vendor or appears to be a suspicious or malicious domain on `{{host}}`.
- Review the MSI package contents and installation behavior to identify any malicious components or unwanted software being installed.
- Check if the installation was initiated by user action or through automated processes that may indicate system compromise.
- Analyze network logs to understand how the user was directed to the malicious URL, such as through phishing emails or compromised websites.
- Verify if the installed software created persistence mechanisms, network connections, or other suspicious activities on the system.
