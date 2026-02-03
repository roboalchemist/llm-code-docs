# Source: https://docs.datadoghq.com/security/default_rules/def-000-a8l.md

---
title: GitHub setting changed to fork private repository
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitHub setting changed to fork private
  repository
---

# GitHub setting changed to fork private repository
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1213-data-from-information-repositories](https://attack.mitre.org/techniques/T1213) 
## Goal{% #goal %}

Detects policy changes to allow forking of private GitHub repositories.

## Strategy{% #strategy %}

GitHub provides audit logs and webhook events that capture modifications to repository settings. Look for events where the fork setting for private repositories is enabled, which can pose a significant security risk by exposing sensitive code.

- `private_repository_forking.enable`

## Triage and Response{% #triage-and-response %}

1. Identify whether `{{@github.actor}}` is changing the forking policy for `{{@github.repository}}`.
1. If the activity is suspicious:
   - [Block the user in GitHub](https://docs.github.com/en/enterprise-cloud@latest/communities/maintaining-your-safety-on-github/blocking-a-user-from-your-organization#blocking-a-user-in-the-organization-settings) to prevent further access.
   - Begin your organization's incident response process and investigate.
