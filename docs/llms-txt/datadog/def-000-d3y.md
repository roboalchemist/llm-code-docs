# Source: https://docs.datadoghq.com/security/default_rules/def-000-d3y.md

---
title: GitHub activity from automated scraping tool
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitHub activity from automated scraping
  tool
---

# GitHub activity from automated scraping tool
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1213-data-from-information-repositories](https://attack.mitre.org/techniques/T1213)
## Goal{% #goal %}

Detects GitHub API requests from automated scraping tools that may be collecting sensitive repository data.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for API requests containing common user agents from scraping tools. Automated scraping tools often use distinctive user agent strings and generate high-volume API requests that differ from normal user behavior patterns.

## Triage & Response{% #triage--response %}

- Examine the GitHub API requests from `{{@github.actor}}` to determine the scope and nature of data being accessed.
- Review the repositories, organizations, and resources targeted by the automated tool to assess potential data exposure risks.
- Identify if the scraping activity is authorized by checking with repository owners and organization administrators.
- Rotate the access keys involved in this behavior, if needed.
