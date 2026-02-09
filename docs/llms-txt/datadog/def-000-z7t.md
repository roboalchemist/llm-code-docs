# Source: https://docs.datadoghq.com/security/default_rules/def-000-z7t.md

---
title: Windows password protected ZIP file opened with suspicious filenames
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows password protected ZIP file
  opened with suspicious filenames
---

# Windows password protected ZIP file opened with suspicious filenames

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1036-masquerading](https://attack.mitre.org/techniques/T1036) 
## Goal{% #goal %}

Detects password-protected ZIP files containing suspicious filenames that are commonly used in phishing attacks.

## Strategy{% #strategy %}

This rule monitors Windows event ID `5379` for shell extension handler operations involving ZIP folders with common social engineering keywords. It identifies when `@Event.EventData.Data.TargetName` contains `Microsoft_Windows_Shell_ZipFolder` along with suspicious terms.

Password-protected archives prevent security scanning while business-themed filenames create urgency for users to open the contents. These techniques combined are frequently used in malware distribution campaigns to bypass detection controls.

## Triage & Response{% #triage--response %}

- Examine the source of the ZIP file on `{{host}}` and how it was delivered.
- Review extracted file contents in a secure environment for malicious indicators.
- Monitor for unusual process executions or network activity following extraction.
- Search for similar password-protected archives across your environment.
- Remove malicious files and block distribution sources.
- Isolate `{{host}}` if compromise indicators are detected.
