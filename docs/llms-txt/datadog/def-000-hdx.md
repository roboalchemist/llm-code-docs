# Source: https://docs.datadoghq.com/security/default_rules/def-000-hdx.md

---
title: GitHub organization was removed from enterprise
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitHub organization was removed from
  enterprise
---

# GitHub organization was removed from enterprise
Classification:attackTactic:[TA0040-impact](https://attack.mitre.org/tactics/TA0040)Technique:[T1531-account-access-removal](https://attack.mitre.org/techniques/T1531) 
## Goal{% #goal %}

Detect when a GitHub enterprise organization has been removed.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for when a GitHub enterprise organization has been removed. An enterprise account allows you to manage and enforce policies for all the organizations owned by the enterprise. The removal of an organization from an enterprise could remove existing security controls, reducing the overall security of the organization.

## Triage and response{% #triage-and-response %}

1. Determine if the change taken by `{{@github.actor}}` is authorized.
1. If the change was not authorized or was unexpected, begin your organization's incident response process and investigate.
