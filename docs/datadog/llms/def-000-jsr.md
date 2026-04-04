# Source: https://docs.datadoghq.com/security/default_rules/def-000-jsr.md

---
title: Windows PowerShell web access installation using PsScript
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows PowerShell web access
  installation using PsScript
---

# Windows PowerShell web access installation using PsScript

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1059-command-and-scripting-interpreter](https://attack.mitre.org/techniques/T1059)
## Goal{% #goal %}

Detects the installation and configuration of Windows PowerShell Web Access, which can be used by attackers to establish a web-based PowerShell remote access backdoor.

## Strategy{% #strategy %}

This rule monitors Windows event logs for PowerShell script block executions that include commands related to PowerShell Web Access setup and configuration. The detection targets script blocks containing `Install-WindowsFeature` combined with `WindowsPowerShellWebAccess`, `Install-PswaWebApplication`, or `Add-PswaAuthorizationRule` commands. Additionally, it looks for authorization parameter settings like `-UserName *` or `-ComputerName *`. PowerShell Web Access provides a web-based PowerShell interface that allows users to run PowerShell commands remotely through a web browser.

## Triage & Response{% #triage--response %}

- Examine the complete PowerShell script block content to understand the full scope of the PowerShell Web Access configuration on `{{host}}`.
- Verify if the PowerShell Web Access installation was authorized and part of a documented change.
- Review the authorization rules that were created to determine which users and computers were granted access.
- If unauthorized, uninstall the PowerShell Web Access feature using `Uninstall-WindowsFeature -Name WindowsPowerShellWebAccess`.
- Review the authentication events for any users who may have accessed the system through PowerShell Web Access.
