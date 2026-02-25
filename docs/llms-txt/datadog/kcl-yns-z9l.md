# Source: https://docs.datadoghq.com/security/default_rules/kcl-yns-z9l.md

---
title: Salesforce login from disabled account
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Salesforce login from disabled account
---

# Salesforce login from disabled account
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110)
## Goal{% #goal %}

Detect when a disabled account attempts to log into Salesforce

## Strategy{% #strategy %}

Inspect Salesforce logs and determine if there is a login attempt (`@evt.name:LoginEvent`) from from a disabled account (`@status:\"User is Inactive\"`). If more than ten attempts to authenticate to a disabled account a `MEDIUM` severity signal is created.

## Triage and response{% #triage-and-response %}

Determine if the IP (`@network.client.ip`) has attempted to log into other accounts.
