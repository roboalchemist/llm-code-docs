# Source: https://docs.datadoghq.com/security/default_rules/def-000-jdv.md

---
title: Okta Identity Provider creation or modification
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Okta Identity Provider creation or
  modification
---

# Okta Identity Provider creation or modification
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1556-modify-authentication-process](https://attack.mitre.org/techniques/T1556)
## Goal{% #goal %}

Detect when an Okta Identity Provider has been created or modified.

## Strategy{% #strategy %}

This rule monitors when an Okta Identity Provider has been created or modified. Okta's security team [reported](https://sec.okta.com/articles/2023/08/cross-tenant-impersonation-prevention-and-detection) a series of social engineering attacks in which attackers configured a second Identity Provider to act as an "impersonation app" to access applications within the compromised customer organization on behalf of other users.

## Triage and response{% #triage-and-response %}

1. Contact the user `{{@usr.email}}` to ensure the change `{{@evt.name}}` is authorized.
1. If the user was unaware of the change:
   - Determine if any other activity occurred from this user. Look for deviations in user agents, IP addresses and network metadata.
   - Begin your organization's incident response process and investigate for any account takeovers.

## Changelog{% #changelog %}

12 August 2025 - Updated rule query to focus on creation, modification, and activation fields. Group by was updated to the name of the IDP integration being modified.
