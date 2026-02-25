# Source: https://docs.datadoghq.com/security/default_rules/def-000-hmz.md

---
title: Azure AI service high volume of chat requests
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure AI service high volume of chat
  requests
---

# Azure AI service high volume of chat requests

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1526-cloud-service-discovery](https://attack.mitre.org/techniques/T1526)
## Goal{% #goal %}

Detect when there is a spike in volume of chat requests to Azure AI services.

## Strategy{% #strategy %}

Monitor Azure activity logs for when a chat is completed for a specific resource within Azure AI services. This may indicate an attacker exploiting the chat function by performing model degradation, cost exploitation, malicious automation, and other techniques.

## Triage and response{% #triage-and-response %}

1. Verify if the user or service principal is expected to be working with specific models and Azure AI services.
1. If the activity is not expected, investigate activity around the user and IP generating this event.
