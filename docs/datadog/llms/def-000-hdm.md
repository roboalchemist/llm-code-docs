# Source: https://docs.datadoghq.com/security/default_rules/def-000-hdm.md

---
title: Forcepoint Secure Web Gateway threat indicator detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Forcepoint Secure Web Gateway threat
  indicator detected
---

# Forcepoint Secure Web Gateway threat indicator detected

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0011-command-and-control](https://attack.mitre.org/tactics/TA0011)Technique:[T1071-application-layer-protocol](https://attack.mitre.org/techniques/T1071)
## Goal{% #goal %}

Identify that a threat indicator was detected within Forcepoint Secure Web Gateway.

## Strategy{% #strategy %}

This rule analyzes Forcepoint SWG logs to identify a detected threat indicator.

## Triage and Response{% #triage-and-response %}

1. Analyze the Forcepoint SWG logs and identify the user `{{@usr.name}}` associated with the occurrences of flagged threat indicator.
1. Review activities, accessed URLs, and files associated with the flagged threat indicators to understand the nature of the threat indicator.
1. Assess web categories and reputation scores of accessed URLs.
1. Examine patterns like DLP pattern or keyword to identify sensitive or regulated data involved in the flagged actions.
1. Quarantine flagged files or data uploads if they contain sensitive information.
1. Block further access to flagged URLs or applications if not already restricted.
1. Suspend or reset the user's account credentials if compromise is suspected.
