# Source: https://docs.datadoghq.com/security/default_rules/def-000-aa7.md

---
title: Azure administrative unit created
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Azure administrative unit created
---

# Azure administrative unit created

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detects the creation of Entra ID (Azure AD) Administrative Units (AUs). The use of this type of this policy may indicate suspicious activity if an environment is not utilizing AUs.

## Strategy{% #strategy %}

Monitor Azure Active Directory logs for `@properties.category:AdministrativeUnit` and `@evt.name: "Add administrative unit"` where the event is not a restricted administrative unit.

## Triage and response{% #triage-and-response %}

1. Review if administrative units are used by the organization.
1. Review evidence of anomalous activity for the user creating an administrative unit.
1. Determine if there is a legitimate reason for the user creating an administrative unit.
