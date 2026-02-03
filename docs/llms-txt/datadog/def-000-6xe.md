# Source: https://docs.datadoghq.com/security/default_rules/def-000-6xe.md

---
title: Atlassian administrative API token activity observed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Atlassian administrative API token
  activity observed
---

# Atlassian administrative API token activity observed
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detect when Atlassian administrative [API token](https://support.atlassian.com/organization-administration/docs/manage-an-organization-with-the-admin-apis/) activity is observed.

## Strategy{% #strategy %}

This rule monitors Atlassian organization audit logs for when an administrator API token activity is observed. An attacker may create or revoke an API token either as a method of persisting within the Atlassian environment or degrading the security controls of an organization or disrupting operations. These API tokens allow users to manage organization settings and users via the [admin APIs](https://developer.atlassian.com/cloud/admin/rest-apis).

## Triage and response{% #triage-and-response %}

1. Determine if the user `{{@usr.email}}` intended to create or revoke a new API token:
   - Is there a related ticket tracking this change?
   - Is `{{@usr.email}}` aware of this activity?
   - Is the network metadata associated with the activity unusual for this user?
1. If the results of the triage indicate that `{{@usr.email}}` was not aware of this activity or it did not originate from a known network, begin your company's incident response process, and start an investigation.
