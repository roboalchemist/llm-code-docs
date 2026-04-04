# Source: https://docs.datadoghq.com/security/default_rules/def-000-ig1.md

---
title: Atlassian Confluence site export
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Atlassian Confluence site export
---

# Atlassian Confluence site export
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1530-data-from-cloud-storage](https://attack.mitre.org/techniques/T1530)
## Goal{% #goal %}

Detect when a Confluence [site export](https://support.atlassian.com/confluence-cloud/docs/create-a-site-backup/) occurs.

## Strategy{% #strategy %}

This rule monitors Confluence audit logs for when a site export occurs. A site export includes the following data:

- Each space's default classification level when applicable.
- Pages, including their classification level when applicable.
- Users and their group settings.
- Attachments (if selected).

Due to the sensitive nature of data documented on confluence, an attacker may export this data in order to mine for valuable information.

## Triage and response{% #triage-and-response %}

1. Determine if the user `{{@usr.name}}` intended make to enable the public link:
   - Is `{{@usr.name}}` aware of this activity?
1. If the results of the triage indicate that `{{@usr.name}}` was not aware of this activity or it did not originate from a known network, begin your company's incident response process, and start an investigation.
