# Source: https://docs.datadoghq.com/security/default_rules/def-000-5yk.md

---
title: Windows PowerShell AADInternals cmdlets execution
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows PowerShell AADInternals cmdlets
  execution
---

# Windows PowerShell AADInternals cmdlets execution

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detects the execution of AADInternals PowerShell cmdlets.

## Strategy{% #strategy %}

This rule monitors PowerShell script block logging for commands that invoke AADInternals cmdlets. AADInternals is a PowerShell module created for testing and exploring Azure Active Directory security. While it has legitimate use cases for security professionals, it contains powerful capabilities that can be misused.

The query searches the `@Event.EventData.Data.ScriptBlockText` field for PowerShell script blocks that contain various AADInternals cmdlet patterns. These include cmdlets starting with verbs such as `Add-AADInt`, `Get-AADInt`, `Invoke-AADInt`, and many other variations.

AADInternals provides functionality to interact with Azure AD in ways that can bypass normal security controls. The module includes capabilities for token manipulation, extracting tenant information, password spraying, and other techniques that could lead to unauthorized access. Although security teams might use this tool for legitimate testing, its presence in production environments outside controlled testing activities is suspicious.

## Triage & Response{% #triage--response %}

- Identify the user account executing AADInternals cmdlets on `{{host}}`.
- Review the complete PowerShell script block to understand exactly which AADInternals functions were called.
- Examine Azure AD sign-in logs for unusual authentication patterns related to the user or from `{{host}}`.
- Review Azure activity logs for suspicious changes to configurations, permissions, or resource creations.
- Verify if sensitive information was extracted from your Azure environment.
- Look for evidence of persistence mechanisms being established in Azure AD, such as new service principals, applications, or modified role assignments.
- Rotate credentials for any service principals or accounts that might have been compromised.
- Review Azure AD privileged roles and memberships for unauthorized changes.
