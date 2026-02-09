# Source: https://docs.datadoghq.com/security/default_rules/def-000-3vo.md

---
title: Credential access via registry hive dumping
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Credential access via registry hive
  dumping
---

# Credential access via registry hive dumping

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1003-os-credential-dumping](https://attack.mitre.org/techniques/T1003) 
## Goal{% #goal %}

Detect when a registry hive is dumped.

## Strategy{% #strategy %}

Command line utilities like `reg.exe` can be used to dump Security and/or SAM hives. Attackers have dumped these hives in an attempt to extract credentials.

## Triage and response{% #triage-and-response %}

1. Identify which hive is being dumped, and if it is authorized or expected.
1. If it's not authorized, isolate the host from the network.
1. Follow your organization's internal processes for investigating and remediating compromised systems.
