# Source: https://docs.datadoghq.com/security/default_rules/def-000-5fo.md

---
title: Azure AI API keys listed outside of known AI web portals
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure AI API keys listed outside of
  known AI web portals
---

# Azure AI API keys listed outside of known AI web portals

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1555-credentials-from-password-stores](https://attack.mitre.org/techniques/T1555)
## Goal{% #goal %}

Detect when an account lists keys outside of the standard web applications for Azure AI and ML services.

## Strategy{% #strategy %}

Monitor Azure activity logs for when an account lists keys do not come from known web applications for the Azure Portal or ML, AI, or OpenAI Studio. This may indicate an attacker listing keys with compromised Azure tokens through the Azure CLI, direct web requests, or other tooling. Compromised keys may be used in attacks such as LLM hijacking (LLMjacking). The following application identifiers has been excluded:

- `d7304df8-741f-47d3-9bc2-df0e24e2071f` (ML Studio)
- `cb2ff863-7f30-4ced-ab89-a00194bcf6d9` (AI Studio)
- `dc807dec-d211-4b3f-bc8a-43b3443c4874` (Open AI Studio)
- `c44b4083-3bb0-49c1-b47d-974e53cbdf3c` (Azure Portal)
- `4e09c6ac-4372-45b7-a977-e9f89e673e32` (Speech Studio)

## Triage and response{% #triage-and-response %}

1. Verify if the user or service principal is expected to be working with Azure AI and ML services, and if they are using these services outside of available web portals.
   - Use the value `{{@identity.claims.appid}}` in the Enterprise Application section of Microsoft Entra to gather further context about the application used.
1. If the activity is not expected, investigate activity around the user and IP generating this event.
