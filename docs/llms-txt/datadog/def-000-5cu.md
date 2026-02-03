# Source: https://docs.datadoghq.com/security/default_rules/def-000-5cu.md

---
title: Azure AD new verified domain added to tenant
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure AD new verified domain added to
  tenant
---

# Azure AD new verified domain added to tenant
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detect when an account adds a new domain to the tenant. This may indicate an attacker preparing a domain to later use in a trusted domain (also known as federated) attack.

## Strategy{% #strategy %}

Monitor Azure AD audit logs for the following events:

- `Add unverified domain`
- `Verify domain`

## Triage and Response{% #triage-and-response %}

1. Check if the user is a known administrator or if the action aligns with their normal activities.
1. Review recent sign-ins (Azure AD Sign-in Logs) to see if the user's authentication patterns are unusual (for example, logins from unexpected locations or multiple failed login attempts).
1. Review if federation settings have been configured for the domain. If federated authentication is configured, ensure this an expected configuration. Federated domains are able to authenticate users on behalf of your Azure AD tenant.
1. If the domain addition is unauthorized, remove it immediately.
1. If the action was performed by a compromised account, disable the account and reset its credentials.
