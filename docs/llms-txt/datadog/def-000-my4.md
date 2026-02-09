# Source: https://docs.datadoghq.com/security/default_rules/def-000-my4.md

---
title: Windows shadow copies deleted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Windows shadow copies deleted
---

# Windows shadow copies deleted

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0040-impact](https://attack.mitre.org/tactics/TA0040)Technique:[T1490-inhibit-system-recovery](https://attack.mitre.org/techniques/T1490) 
## Goal{% #goal %}

Detect when vssadmin is used to delete shadow copies.

## Strategy{% #strategy %}

Threat actors are known to use tools found natively in a victim's environment to accomplish their objectives. `Vssadmin.exe`, a native Windows utility, can be used to delete all shadow copies on a system.

## Triage and response{% #triage-and-response %}

1. Identify the user or service account deleting shadow copies, and confirm if this is authorized or expected.
1. If it's not authorized, isolate the host from the network.
1. Follow your organization's internal processes for investigating and remediating compromised systems.
