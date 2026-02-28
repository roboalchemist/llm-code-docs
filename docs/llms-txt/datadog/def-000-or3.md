# Source: https://docs.datadoghq.com/security/default_rules/def-000-or3.md

---
title: Azure AD escalation from Global Administrator to User Access Administrator
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure AD escalation from Global
  Administrator to User Access Administrator
---

# Azure AD escalation from Global Administrator to User Access Administrator
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Detect when a Global Administrator elevates their Azure Active Directory permissions to User Access Administrator in Azure RBAC. This may indicate an attacker with Azure Active Directory privileges is seeking to gain control over Azure resources.

## Strategy{% #strategy %}

Monitor Azure Active Directory audit logs for the following events:

- `User has elevated their access to User Access Administrator for their Azure Resources`

## Triage and Response{% #triage-and-response %}

1. Verify if this activity is associated with expected administrator activities.
1. If not, investigate activity by the account associated with this alert (`{{@usr.id}}`) around the time of this event, including any permissions modifications made to Azure RBAC assignments.
