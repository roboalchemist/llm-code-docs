# Source: https://docs.datadoghq.com/security/default_rules/def-006-oxv.md

---
title: Slack data export download
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Slack data export download
---

# Slack data export download
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1213-data-from-information-repositories](https://attack.mitre.org/techniques/T1213) 
## Goal{% #goal %}

Detect when a Slack export, such as a channel export, manual export, or manual user export, is downloaded.

## Strategy{% #strategy %}

This rule monitors Slack events for when a channel export, manual export, or manual user export is downloaded. These export actions involve downloading a significant amount of Slack data, including conversations, files, and user information. Unauthorized exports could indicate a potential data breach, insider threat, or misuse of administrative privileges.

Potential risks associated with these export actions include:

- Unauthorized access to and exfiltration of sensitive company data.
- Insider threats downloading and sharing confidential information.
- Exposure of private conversations, files, and user details to unauthorized parties.

## Triage and response{% #triage-and-response %}

1. Determine if the export download is expected by:

   - Contacting the user or admin `{{@usr.email}}` who initiated the export to verify the legitimacy of the request.
   - Reviewing the context and scope of the export, including:
     - The type of data exported (e.g., specific channels or user data).
     - The time and date of the export and the business justification for the action.
   - Checking Slack logs for other unusual or suspicious activity by the user, such as mass downloads, file sharing, or privilege escalation.

1. If the export is unauthorized or unexpected:

   - Begin your organization's incident response process and investigate further.
   - Analyze the exported data for sensitive information, and determine the scope of exposure.
   - Monitor for any further attempts to export data or download sensitive information across the workspace.

## Changelog{% #changelog %}

- 21 August 2025 - Updated rule query to include single export case.
