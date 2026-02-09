# Source: https://docs.datadoghq.com/security/default_rules/3fe-1fm-dlw.md

---
title: AWS FSx Excessive File Denied
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > AWS FSx Excessive File Denied
---

# AWS FSx Excessive File Denied
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1526-cloud-service-discovery](https://attack.mitre.org/techniques/T1526) 
## Goal{% #goal %}

Detect and identify users accessing files they do not have permission to access.

## Strategy{% #strategy %}

Monitor AWS FSx logs and detect more than 10 occurrences where `@evt.id` is equal to `4656` and `@Event.System.Keywords` is equal to `0x8010000000000000`.

## Triage & Response{% #triage--response %}

1. Inspect the log and determine if the user should be accessing the file: `{{@ObjectName}}`.
1. If access is not legitimate, investigate user `({{@usr.id}})` activity.
