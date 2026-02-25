# Source: https://docs.datadoghq.com/security/default_rules/def-000-ewq.md

---
title: Cisco Secure Endpoint high number of malicious files from single host
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Cisco Secure Endpoint high number of
  malicious files from single host
---

# Cisco Secure Endpoint high number of malicious files from single host

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1204-user-execution](https://attack.mitre.org/techniques/T1204)
## Goal{% #goal %}

Detect an unusually high number of unique malicious files from a single host.

## Strategy{% #strategy %}

This rule monitors events to detect a spike in the number of malicious files from single host.

## Triage and response{% #triage-and-response %}

1. Investigate the Host, `{{@event.computer.hostname}}`, in which the malicious files have been detected.
1. Analyze the endpoint for other potentially malicious activity.
1. Implement immediate measures to block or limit the impact of the suspicious activity if confirmed as a threat.
1. Follow company procedures for handling malicious files, including isolating the endpoint, running antivirus/antimalware scans, analyzing logs, and updating security policies.
