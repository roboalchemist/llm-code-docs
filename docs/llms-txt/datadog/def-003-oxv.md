# Source: https://docs.datadoghq.com/security/default_rules/def-003-oxv.md

---
title: Slack malicious content detected in uploaded file
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Slack malicious content detected in
  uploaded file
---

# Slack malicious content detected in uploaded file
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1204-user-execution](https://attack.mitre.org/techniques/T1204) 
## Goal{% #goal %}

Detect when a malicious file is shared or uploaded within Slack.

## Strategy{% #strategy %}

This rule monitors Slack for file uploads or shares that are flagged as potentially malicious. Files can be detected as malicious through integrated security tools or antivirus scanning mechanisms. Sharing of malicious files could lead to malware infections, data breaches, or other security risks if users inadvertently download or interact with the file.

## Triage and response{% #triage-and-response %}

1. Determine if the file is truly malicious by:

   - Reviewing the details of the flagged file, including file type, name, and hash, using security tools or integrated antivirus solutions.
   - Identifying the user `{{@usr.email}}` who uploaded or shared the file and contacting them to determine if the file was shared intentionally or if their account may be compromised.
   - Checking the activity logs of the user, including recent file uploads, message history, and other behaviors that could indicate compromised credentials or malicious intent.

1. If the file is confirmed as malicious:

   - Begin your organization's incident response process to contain and investigate further.
   - Quarantine the file: Remove the malicious file from Slack, ensuring no one else can download or access it.
   - Instruct all users who interacted with the file to:
     - Refrain from downloading the file.
     - Run antivirus or endpoint detection tools on their systems to check for potential compromise.
   - Review and block any additional files from the same source, and monitor Slack for similar uploads from the user or others in the organization.
   - Investigate if the user's account has been compromised, and if so, reset credentials and enforce multi-factor authentication (MFA).
