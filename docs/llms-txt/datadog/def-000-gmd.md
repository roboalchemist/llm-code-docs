# Source: https://docs.datadoghq.com/security/default_rules/def-000-gmd.md

---
title: GitLab successive project or repository downloads
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitLab successive project or repository
  downloads
---

# GitLab successive project or repository downloads

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0010-exfiltration](https://attack.mitre.org/tactics/TA0010)Technique:[T1567-exfiltration-over-web-service](https://attack.mitre.org/techniques/T1567)
## Goal{% #goal %}

Detects when a GitLab user downloads multiple projects or repositories within a short time period. Such activity may indicate a data exfiltration attempt.

## Strategy{% #strategy %}

This rule monitors the `project_export_file_download_started` and `repository_download_operation` GitLab audit events. The detection groups events by user within a 5-minute evaluation window and triggers when a user exceeds the download thresholds.

## Triage & Response{% #triage--response %}

- Verify if `{{@usr.name}}` has a legitimate business need to download multiple projects or repositories in rapid succession.
- Examine the specific projects and repositories downloaded to determine their sensitivity and business value.
- Review the user's recent access patterns and authentication logs to identify any signs of account compromise.
- Investigate whether the downloaded content was subsequently transferred outside the organization through other channels.
