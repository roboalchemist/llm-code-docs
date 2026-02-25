# Source: https://docs.datadoghq.com/security/default_rules/6fj-qtv-ei2.md

---
title: Unusual Authentication by Microsoft 365 Azure AD Service Principal
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Unusual Authentication by Microsoft 365
  Azure AD Service Principal
---

# Unusual Authentication by Microsoft 365 Azure AD Service Principal
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detect when a Microsoft 365 Azure AD service principal uses an unusual authentication method.

## Strategy{% #strategy %}

Using the `New Value` detection method, find when a `Microsoft 365 Azure AD service principal` uses a new `@AuthenticationMethod`.

## Triage and response{% #triage-and-response %}

1. Determine if the service principal `{{@usr.id}}` should be authenticating using the `{{@AuthenticationMethod}}` authentication method and `{{@ExtendedProperties.RequestType}}` request type.
1. If `{{@usr.email}}` should not be authenticating using `{{@AuthenticationMethod}}`,
   - Investigate other activities performed by the user `{{@usr.id}}` using the Cloud SIEM - User Investigation dashboard
   - If necessary, initiate your company's incident response (IR) process.
