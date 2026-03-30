# Source: https://docs.datadoghq.com/security/default_rules/def-000-sqs.md

---
title: Atlassian Confluence space export
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Atlassian Confluence space export
---

# Atlassian Confluence space export
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1530-data-from-cloud-storage](https://attack.mitre.org/techniques/T1530)
## Goal{% #goal %}

Detect when a Confluence [space export](https://support.atlassian.com/confluence-cloud/docs/export-content-to-word-pdf-html-and-xml/) occurs.

## Strategy{% #strategy %}

This rule monitors Confluence audit logs for when a space export occurs. Space admins can export a space (or a group of individually selected pages in a space) to PDF, CSV, HTML, or XML.

Due to the sensitive nature of data documented on confluence, an attacker may export this data in order to mine for valuable information.

## Triage and response{% #triage-and-response %}

1. Determine if the user `{{@usr.name}}` intended make to enable the public link:
   - Is `{{@usr.name}}` aware of this activity?
1. If the results of the triage indicate that `{{@usr.name}}` was not aware of this activity or it did not originate from a known network, begin your company's incident response process, and start an investigation.
