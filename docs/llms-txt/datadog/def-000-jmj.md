# Source: https://docs.datadoghq.com/security/default_rules/def-000-jmj.md

---
title: Unusual ntdsutil usage
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Unusual ntdsutil usage
---

# Unusual ntdsutil usage

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1003-os-credential-dumping](https://attack.mitre.org/techniques/T1003)
## Goal{% #goal %}

Detect when Ntdsutil is used in a suspicious manner, typically to access the `Ntds.dit` file.

## Strategy{% #strategy %}

Threat actors are known to utilize tools found natively in a victim's environment to accomplish their objectives. Ntdsutil, a legitimate Windows binary, has been abused by malicious actors in the past to gain access to the `Ntds.dit` file.

## Triage and response{% #triage-and-response %}

1. Identify if the usage of Ntdsutil is authorized, and confirm if the `Ntds.dit` file was downloaded.
1. If it's not authorized, isolate the host from the network.
1. Follow your organization's internal processes for investigating and remediating compromised systems.
