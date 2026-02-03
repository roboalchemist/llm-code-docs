# Source: https://docs.datadoghq.com/security/default_rules/def-000-r2s.md

---
title: GitLab project visibility changed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > GitLab project visibility changed
---

# GitLab project visibility changed

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1213-data-from-information-repositories](https://attack.mitre.org/techniques/T1213) 
## Goal{% #goal %}

Detects when the visibility level of a GitLab project is changed. Changes to public visibility may expose sensitive code and data to unauthorized users.

## Strategy{% #strategy %}

This rule monitors the `project_visibility_level_updated` GitLab audit event. The detection tracks when users modify project visibility settings, which can include changes that make previously private or internal projects publicly accessible.

## Triage & Response{% #triage--response %}

- Verify if `{{@usr.name}}` had legitimate authorization to change the project visibility settings.
- Examine the specific project that was modified and determine if it contains sensitive code or data that should not be publicly accessible.
- Review the project's previous visibility level to understand the scope of the exposure change.
- Check if the visibility change aligns with documented business requirements or approved change requests.
- Determine if any sensitive information, credentials, or proprietary code may have been inadvertently exposed through the visibility change.
