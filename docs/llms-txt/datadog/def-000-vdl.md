# Source: https://docs.datadoghq.com/security/default_rules/def-000-vdl.md

---
title: Azure AI API keys listed from previously unseen application
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure AI API keys listed from
  previously unseen application
---

# Azure AI API keys listed from previously unseen application

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1555-credentials-from-password-stores](https://attack.mitre.org/techniques/T1555)
## Goal{% #goal %}

Detect when a previously unseen application lists keys for Azure AI and ML services.

## Strategy{% #strategy %}

Monitor Azure activity logs for when a previously unseen application lists keys for Azure AI and ML services. This may indicate an attacker listing keys with compromised Azure tokens through the Azure CLI, direct web requests, or other tooling. Compromised keys may be used in attacks such as LLM hijacking (LLMjacking).

## Triage and response{% #triage-and-response %}

1. Verify if the user or service principal is expected to be working with Azure AI and ML services, and if they are using these services outside of available web portals.
   - Use the value `{{@identity.claims.appid}}` in the Enterprise Application section of Microsoft Entra to gather further context about the application used.
1. If the activity is not expected, investigate activity around the user and IP generating this event.
