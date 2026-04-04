# Source: https://docs.datadoghq.com/security/default_rules/def-000-ljl.md

---
title: Cisco Secure Endpoint malicious activity detected in system scan
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Cisco Secure Endpoint malicious
  activity detected in system scan
---

# Cisco Secure Endpoint malicious activity detected in system scan

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1204-user-execution](https://attack.mitre.org/techniques/T1204)
## Goal{% #goal %}

This rule is designed to identify and flag instances of potential malicious activity detected during system scans conducted by Cisco Secure Endpoint.

## Strategy{% #strategy %}

This rule monitors and reports the presence of a positive number of malicious detections identified during comprehensive system scans executed by Cisco Secure Endpoint.

## Triage and response{% #triage-and-response %}

1. Investigate the system scan by hostname: `{{@event.computer.hostname}}`.
1. Investigate more about the system scan by scan description (`{{@event.scan.description}}`) and number of malicious detections (`{{@event.scan.malicious_detections}}`).
1. Initiate containment measures to isolate affected systems or endpoints from the network if confirmed as a security threat.
1. Execute remediation actions, such as deploying security patches, updating antivirus definitions, or performing system scans to remove any detected malware.
1. Take necessary and appropriate actions based on the company procedures.
