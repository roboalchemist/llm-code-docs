# Source: https://docs.datadoghq.com/security/default_rules/edj-z5a-yvu.md

---
title: Credential added to Azure AD application
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Credential added to Azure AD
  application
---

# Credential added to Azure AD application
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detects when a user adds a secret or certificate to an Azure Active Directory Application.

## Strategy{% #strategy %}

Monitor Azure AD Audit logs for the following `@evt.name`:

- `Update application â Certificates and secrets management`
- `Add service principal credentials`

Monitor Microsoft 365 Audit logs for the following `@evt.name`:

- `Update application â Certificates and secrets management`
- `Add service principal credentials.`

An attacker can add a secret or certificate to an application in order to connect to Azure AD as the application and perform API operation leveraging the application permissions that are assigned to it.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@usr.id}}` should have made a `{{@evt.name}}` API call.
1. If the API call was not made by the user:
   - Remove the suspicious key.
   - Invalidate all existing refresh tokens. This ensures the attacker is unable to connect to your tenant.
   - Begin your organization's Incident Response (IR) process.
1. If the API call was made by the user:
   - Ensure the change was authorized.
