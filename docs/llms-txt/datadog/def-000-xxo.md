# Source: https://docs.datadoghq.com/security/default_rules/def-000-xxo.md

---
title: Zendesk API token is created
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Zendesk API token is created
---

# Zendesk API token is created
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Detect when an API token is created in Zendesk Admin Center.

## Strategy{% #strategy %}

Monitor Zendesk audit logs to look for events with an `@source_label` value of `"Zendesk API: Active API tokens"` and `@evt.category:create`. API tokens are auto-generated passwords in the Zendesk Admin Center. API tokens can be used to impersonate anyone in the account, including admins.

## Triage and response{% #triage-and-response %}

1. Determine if the user `{{@usr.name}}` intended to create a new API token.
1. If the API token is not required for a legitimate business use case, delete the token.
