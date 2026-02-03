# Source: https://docs.datadoghq.com/security/default_rules/def-000-rev.md

---
title: Azure AD Privileged Identity Management member assigned
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure AD Privileged Identity Management
  member assigned
---

# Azure AD Privileged Identity Management member assigned
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detect whenever a user assigns an administrative role in Azure Privileged Identity Management (PIM).

## Strategy{% #strategy %}

Monitor Azure Active Directory and generate a signal when a user assigns an administrative role to a PIM member.

The field `@usr.id` is the user that actioned the change, and the field `@properties.targetResources.userPrincipalName` is the user being assigned the administrative privileges.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@usr.id}}` should have assigned the administrative role.
1. If the API call was not made by the user:

- Rotate user credentials.
- Determine what other API calls were made by the user.
- Begin your organization's incident response (IR) process and investigate.
If the API call was made legitimately:
- Determine if `{{@usr.id}}` was authorized to make the change.
- Follow Microsoft's [best practices](https://docs.microsoft.com/en-us/azure/active-directory/roles/best-practices) where possible to ensure the user was assigned the correct level of privileges for their function.

## Changelog{% #changelog %}

- 19 December 2023 - Updated group by values to include `@properties.targetResources.userPrincipalName`
