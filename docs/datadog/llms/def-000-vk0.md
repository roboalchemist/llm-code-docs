# Source: https://docs.datadoghq.com/security/default_rules/def-000-vk0.md

---
title: >-
  Delinea Privilege Manager detected a newly discovered file marked as
  suspicious/bad by VirusTotal
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Delinea Privilege Manager detected a
  newly discovered file marked as suspicious/bad by VirusTotal
---

# Delinea Privilege Manager detected a newly discovered file marked as suspicious/bad by VirusTotal

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1204-user-execution](https://attack.mitre.org/techniques/T1204)
## Goal{% #goal %}

Notify when newly discovered files are flagged as suspicious/bad by the VirusTotal rating system.

## Strategy{% #strategy %}

This rule monitors the Delinea Privilege Manager events to detect newly discovered files flagged as suspicious/bad by the VirusTotal rating system.

## Triage and Response{% #triage-and-response %}

1. Investigate the newly discovered file event for filename: `{{@FileName}}`.
1. If the file is verified as malicious, isolate the affected system immediately.
1. Trace the origin of the file and check for its presence on other systems within the network.
1. Quarantine the file to prevent execution or further spread.
