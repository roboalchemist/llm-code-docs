# Source: https://docs.datadoghq.com/security/default_rules/def-000-jhs.md

---
title: >-
  Delinea Privilege Manager unusual spike in bad-rated application action events
  from a single computer
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Delinea Privilege Manager unusual spike
  in bad-rated application action events from a single computer
---

# Delinea Privilege Manager unusual spike in bad-rated application action events from a single computer

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1204-user-execution](https://attack.mitre.org/techniques/T1204)
## Goal{% #goal %}

Detects an unusual spike in bad-rated application events from a single computer.

## Strategy{% #strategy %}

This rule monitors the Delinea Privilege Manager events to detect an unusual spike in bad-rated application events from a single computer.

## Triage and Response{% #triage-and-response %}

1. Review the logs of bad-rated application events from a computer name: `{{@ComputerName}}`(`{{@_ComputerId}}`).
1. Analyze the list of installed and executed applications.
1. Quarantine or isolate affected systems to mitigate potential risks.
1. Update application control policies to block the identified applications with bad security ratings.
