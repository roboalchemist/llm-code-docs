# Source: https://docs.datadoghq.com/security/default_rules/def-000-bhv.md

---
title: Atlassian Confluence admin key usage
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Atlassian Confluence admin key usage
---

# Atlassian Confluence admin key usage
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detect when an Atlassian administrator uses the [admin key](https://support.atlassian.com/confluence-cloud/docs/bypass-access-restrictions-on-a-page-with-admin-key/) feature.

## Strategy{% #strategy %}

This rule monitors Confluence audit logs for when an administrator uses the admin key feature. This feature allows the user to access content they haven't been given permission to view. This could impact the confidentiality of data stored on the confluence site.

## Triage and response{% #triage-and-response %}

1. Determine if the user `{{@usr.name}}` intended use the admin key feature:
   - Is there a related ticket tracking this change?
   - Is `{{@usr.name}}` aware of this activity?
1. If the results of the triage indicate that `{{@usr.name}}` was not aware of this activity or it did not originate from a known network, begin your company's incident response process, and start an investigation.
