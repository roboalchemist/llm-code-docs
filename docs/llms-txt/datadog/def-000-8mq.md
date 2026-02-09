# Source: https://docs.datadoghq.com/security/default_rules/def-000-8mq.md

---
title: Microsoft 365 Security and Compliance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Microsoft 365 Security and Compliance
---

# Microsoft 365 Security and Compliance
Classification:attack 
## Goal{% #goal %}

Detect when [Microsoft 365 Security and Compliance](https://learn.microsoft.com/en-us/microsoft-365/compliance/alert-policies?view=o365-worldwide) raises an alert.

## Strategy{% #strategy %}

You can use alert policies and the alert dashboard in the [Microsoft Purview compliance portal](https://compliance.microsoft.com/compliancealerts) or the [Microsoft 365 Defender portal](https://security.microsoft.com/alerts) to create alert policies and then view the alerts generated when users perform activities that match the conditions of an alert policy.

Alert signals include:

- All alerts generated based on Alert policies in Security & Compliance Center.
- Office 365 related alerts generated in [Office 365 Cloud App Security](https://learn.microsoft.com/en-us/office365/securitycompliance/office-365-cas-overview) and [Microsoft Cloud App Security](https://learn.microsoft.com/en-us/cloud-app-security/what-is-cloud-app-security).

## Triage and response{% #triage-and-response %}

1. Investigate the Microsoft 365 alert to determine if it is malicious or benign.
1. If the finding is deemed malicious, follow the [remediation guidance](https://learn.microsoft.com/en-us/microsoft-365/security/defender/alert-grading-playbooks?view=o365-worldwide) provided by Microsoft and also any internal incident response processes.
