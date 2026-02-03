# Source: https://docs.datadoghq.com/security/default_rules/def-000-udg.md

---
title: Atlassian Confluence public link turned on
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Atlassian Confluence public link turned
  on
---

# Atlassian Confluence public link turned on
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1530-data-from-cloud-storage](https://attack.mitre.org/techniques/T1530) 
## Goal{% #goal %}

Detect when a [public link](https://support.atlassian.com/confluence-cloud/docs/share-content-externally-with-public-links/) for a page has been enabled.

## Strategy{% #strategy %}

This rule monitors Confluence audit logs for when a public link for a page has been enabled. A public link allows external users to view Confluence content. While this activity may be expected in some circumstances, monitoring this activity is valuable to ensure only authorized content is shared.

## Triage and response{% #triage-and-response %}

1. Determine if the user `{{@usr.name}}` intended make to enable the public link:
   - Is `{{@usr.name}}` aware of this activity?
1. If the results of the triage indicate that `{{@usr.name}}` was not aware of this activity or it did not originate from a known network, begin your company's incident response process, and start an investigation.
