# Source: https://docs.datadoghq.com/security/default_rules/def-000-p4l.md

---
title: GitHub SAML/OIDC has been disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > GitHub SAML/OIDC has been disabled
---

# GitHub SAML/OIDC has been disabled
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Detect when GitHub OIDC/SAML single sign-on (SSO) has been modified.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for when OIDC/SAML SSO has been modified. GitHub allows for use of a SSO solution to increase security and centralize identity and access for the web application that your team uses. Disabling these settings could lead to a degradation in the organization's security posture.

## Triage and response{% #triage-and-response %}

1. Determine if the change taken by `{{@github.actor}}` is authorized.
1. If the change was not authorized or was unexpected, begin your organization's incident response process and investigate.
