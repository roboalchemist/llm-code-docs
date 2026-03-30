# Source: https://docs.datadoghq.com/security/default_rules/sqa-ez2-ojw.md

---
title: Azure AD member assigned built-in Administrator role
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure AD member assigned built-in
  Administrator role
---

# Azure AD member assigned built-in Administrator role
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Detect an Azure Active Directory (Azure AD) member being added to a [built-in Administrative role](https://docs.microsoft.com/en-us/azure/active-directory/roles/permissions-reference).

## Strategy{% #strategy %}

Monitor Azure AD Audit logs for the following operations:

- `@evt.name:"Add member to role"`
- `@properties.targetResources.modifiedProperties.newValue:*Administrator*`

Azure AD uses roles to assign privileges to identities. There are over 80 roles available, the list below details some of the highest privileged roles that adversaries could target:

- [Application Administrator](https://docs.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#application-administrator)
- [Cloud Application Administrator](https://docs.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#cloud-application-administrator)
- [Exchange Administrator](https://docs.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#exchange-administrator)
- [Privileged Role Administrator](https://docs.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#privileged-role-administrator)
- [User Administrator](https://docs.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#user-administrator)
- [Sharepoint Administrator](https://docs.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#sharepoint-administrator)
- [Hybrid Identity Administrator](https://docs.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#hybrid-identity-administrator)

This [whitepaper](https://www.fireeye.com/content/dam/fireeye-www/blog/pdfs/wp-m-unc2452-2021-000343-01.pdf) from Mandiant describes the abuse of Azure AD privileged roles.

The field `@usr.id` is the identity that actioned the change, and the fields `@properties.targetResources.userPrincipalName` or `@properties.targetResources.displaylName` is the identity being assigned the administrative privileges.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@usr.id}}` should have made a `{{@evt.name}}` API call.
1. If the API call was not made by the user:

- Rotate user credentials.
- Determine what other API calls were made by the user.
- Begin your organization's incident response (IR) process and investigate.
If the API call was made legitimately by the user:
- Determine if `{{@usr.id}}` was authorized to make the change.
- Follow Microsoft's [best practices](https://docs.microsoft.com/en-us/azure/active-directory/roles/best-practices) where possible to ensure the user was assigned the correct level of privileges for their function.

## Changelog{% #changelog %}

- 19 December 2023 - Updated group by values to include `@properties.targetResources.userPrincipalName`
- 19 September 2024 - Updated with additional query to capture service principals being assigned administrative roles.
