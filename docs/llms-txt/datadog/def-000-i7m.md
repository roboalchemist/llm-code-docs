# Source: https://docs.datadoghq.com/security/default_rules/def-000-i7m.md

---
title: Windows self extraction directive file created
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows self extraction directive file
  created
---

# Windows self extraction directive file created

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1218-system-binary-proxy-execution](https://attack.mitre.org/techniques/T1218)
## Goal{% #goal %}

Detects creation or access of Self Extraction Directive files that may be used for defense evasion through system binary proxy execution.

## Strategy{% #strategy %}

This rule monitors Windows file access events where `@evt.id` is `4663` or network share access events where `@evt.id` is `5145` when the target file `@Event.EventData.Data.RelativeTargetName` has a `.sed` extension. Self Extraction Directive files are configuration files used by legitimate utilities like `IExpress.exe` to create self-extracting archives. Attackers can abuse this functionality to create seemingly legitimate executable files that extract and execute malicious payloads, bypassing security controls that trust signed system binaries or allow-listed applications.

## Triage and response{% #triage-and-response %}

- Examine the `.sed` file contents on `{{host}}` to understand what files will be extracted and which commands will be executed.
- Review the source process that created or accessed the `.sed` file to determine if it represents legitimate software packaging versus malicious activity.
- Check for corresponding `IExpress.exe` execution or other self-extraction utility usage around the same timeframe.
- Analyze any resulting executable files created from the self-extraction process for malicious content or suspicious behavior.
- Verify if the user account has legitimate business need to create self-extracting archives or software packages.
