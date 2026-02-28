# Source: https://docs.datadoghq.com/security/default_rules/def-000-imy.md

---
title: Atlassian Confluence global setting changed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Atlassian Confluence global setting
  changed
---

# Atlassian Confluence global setting changed
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect when a Confluence global setting has been changed.

## Strategy{% #strategy %}

This rule monitors Confluence audit logs for when a global setting has been changed. Global settings include configurations to allow users to share pages publicly and allow anonymous users access to the confluence site.

## Triage and response{% #triage-and-response %}

1. Determine if the user `{{@usr.name}}` intended make the global setting change:
   - Is there a related ticket tracking this change?
   - Is `{{@usr.name}}` aware of this activity?
1. If the results of the triage indicate that `{{@usr.name}}` was not aware of this activity or it did not originate from a known network, begin your company's incident response process, and start an investigation.
