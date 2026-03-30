# Source: https://docs.datadoghq.com/security/default_rules/def-000-lcz.md

---
title: Slack enterprise workspace created or deleted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Slack enterprise workspace created or
  deleted
---

# Slack enterprise workspace created or deleted
Classification:attackTactic:[TA0040-impact](https://attack.mitre.org/tactics/TA0040)Technique:[T1531-account-access-removal](https://attack.mitre.org/techniques/T1531)
## Goal{% #goal %}

Detects Slack workspace creation or deletion events.

## Strategy{% #strategy %}

This rule monitors Slack audit logs for `@evt.name:workspace_created` and `@evt.name:workspace_deleted` events from the `audit-logs-service`.

## Triage & Response{% #triage--response %}

- Verify if `{{@usr.email}}` has authorization to create or delete workspaces.
- Check if the workspace action aligns with business requirements.
- Review the user's permissions and role assignments.
- Assess the impact on data access and organizational structure.
