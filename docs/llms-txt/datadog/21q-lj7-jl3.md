# Source: https://docs.datadoghq.com/security/default_rules/21q-lj7-jl3.md

---
title: Azure Service Principal was assigned a role
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure Service Principal was assigned a
  role
---

# Azure Service Principal was assigned a role
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Detect an Azure service principal being assigned an Azure role.

## Strategy{% #strategy %}

Monitor Azure Activity logs for the following operations:

- `@evt.name:"MICROSOFT.AUTHORIZATION/ROLEASSIGNMENTS/WRITE"`
- `@properties.requestbody:*ServicePrincipal*`

## Triage and response{% #triage-and-response %}

1. Determine if this activity is legitimate by investigating the:

- Source IP of this activity: `{{@network.client.ip}}`
- The user who made this request: `@identity.claims.name`
- The role that was assigned to the application or service principal.
If this user should not be assigning this Azure role and if the service principal should not be assigned this role:
- Revoke access of compromised credentials.
- Remove unauthorized app registration and/or service principal.
- Investigate other activities performed by the source IP `{{@network.client.ip}}` in the IP Investigation Dashboard.
- Investigate other activities performed by the user `{{@usr.id}}` in the User Investigation Dashboard.
