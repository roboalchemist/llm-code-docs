# Source: https://docs.datadoghq.com/security/default_rules/def-000-8ui.md

---
title: A potentially malicious file was sent in a Microsoft Teams message
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > A potentially malicious file was sent
  in a Microsoft Teams message
---

# A potentially malicious file was sent in a Microsoft Teams message
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1199-trusted-relationship](https://attack.mitre.org/techniques/T1199)
## Goal{% #goal %}

Detect when a potentially malicious file is sent in Microsoft Teams. Threat actors sometimes send malicious files to unsuspecting users as a means of initial access.

## Strategy{% #strategy %}

Monitor Microsoft 365 Sharepoint audit logs to look for the operation [`FileUploaded`](https://learn.microsoft.com/en-us/purview/audit-log-activities). When a file is shared in Teams, it utilizes the underlying Microsoft Office APIs to upload the file using SharePoint. The Teams file uploads are audited within the Microsoft Office's activity log as SharePoint file operations. To differentiate Teams file uploads from those of other services, we use the `AppAccessContext.ClientAppName` attribute with the value of `Microsoft Teams Chat Files`. This detection identifies when a file with any of the following extensions is uploaded:

- exe
- msi
- bin
- dll
- bat
- ps1
- vbs
- js
- scr
- zip
- rar
- 7z
- cab
- tar
- gz
- bz2

## Triage and response{% #triage-and-response %}

1. Investigate the potentially malicious file: `{{@SourceFileName}}` that was sent by viewing the Sharepoint link: `{{@ObjectId}}` containing the file.
1. Determine if the user `{{@usr.email}}` intended to send the observed file.
1. If `{{@usr.email}}` didn't intend to send the observed file or happens to be a guest or external user:
   - Investigate other activities performed by the user `{{@usr.email}}` using the Cloud SIEM - User Investigation dashboard.
   - Begin your organization's incident response process and investigate.
