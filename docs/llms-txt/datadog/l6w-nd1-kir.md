# Source: https://docs.datadoghq.com/security/default_rules/l6w-nd1-kir.md

---
title: Potential Illicit Consent Grant attack via Azure registered application
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Potential Illicit Consent Grant attack
  via Azure registered application
---

# Potential Illicit Consent Grant attack via Azure registered application
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1566-phishing](https://attack.mitre.org/techniques/T1566)
## Goal{% #goal %}

Detects when a user grants an application consent to access their data. An adversary may create an Azure-registered application to access data such as contact information, emails, or documents.

## Strategy{% #strategy %}

Monitor Azure AD Audit logs for the following `@evt.name`:

- `Consent to application`

Monitor Microsoft 365 Audit logs for the following `@evt.name`:

- `Consent to application.`

Because these are thirty-party applications external to the organization, normal remediation steps like resetting passwords for breached accounts or requiring Multi-Factor Authentication (MFA) on accounts are not effective against this type of attack.

## Triage and response{% #triage-and-response %}

1. See the official [Microsoft playbook](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/detect-and-remediate-illicit-consent-grants?view=o365-worldwide) on responding to a potential Illicit Consent Grant.
1. If the activity is benign:
   - Use the linked blog post in the suggested actions panel to tune out false positives.
