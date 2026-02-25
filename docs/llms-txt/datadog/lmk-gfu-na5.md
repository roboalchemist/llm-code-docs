# Source: https://docs.datadoghq.com/security/default_rules/lmk-gfu-na5.md

---
title: Microsoft 365 Anomalous Amount of Downloaded files
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Microsoft 365 Anomalous Amount of
  Downloaded files
---

# Microsoft 365 Anomalous Amount of Downloaded files
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1213-data-from-information-repositories](https://attack.mitre.org/techniques/T1213)
## Goal{% #goal %}

Detect when a Microsoft 365 user downloads an anomalous amount of files. This could be an indicator of data exfilteration.

## Strategy{% #strategy %}

Monitor Microsoft 365 audit logs to look for an anomalous amount of logs with an `@evt.name` value of `@evt.name:FileDownloaded`.

## Triage and response{% #triage-and-response %}

1. Determine if the user `{{@usr.email}}` intended to download the files.
1. If `{{@usr.email}}` is not responsible for file downloads, investigate `{{@usr.email}}` for anomalous activity. If necessary, initiate your company's incident response (IR) process.
