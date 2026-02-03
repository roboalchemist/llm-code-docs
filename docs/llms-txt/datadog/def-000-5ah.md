# Source: https://docs.datadoghq.com/security/default_rules/def-000-5ah.md

---
title: Delinea Privilege Manager detected a password disclosure event
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Delinea Privilege Manager detected a
  password disclosure event
---

# Delinea Privilege Manager detected a password disclosure event

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1555-credentials-from-password-stores](https://attack.mitre.org/techniques/T1555) 
## Goal{% #goal %}

Detects password disclosure events.

## Strategy{% #strategy %}

This rule monitors the Delinea Privilege Manager logs to detect password disclosure events.

## Triage and Response{% #triage-and-response %}

1. Investigate the password disclosure event log associated with the managed user: `{{@ManagedUserName}}`.
1. Assess whether the managed user account (username: `{{@ManagedUserName}}`, ID:`{{@_ManagedUserId}}`) is associated with a critical system or application.
1. Identify the user to confirm the identity and permissions of the user who disclosed the password.
1. If the password is disclosed for a critical system, contact the disclosing user to confirm whether the password disclosure was intentional and authorized.
1. If the disclosure was unauthorized, proceed with account remediation.
1. Reset the password for the managed user account (username: `{{@ManagedUserName}}`, ID:`{{@_ManagedUserId}}`) to prevent potential misuse.
1. Evaluate and improve access policies to prevent future occurrences.
