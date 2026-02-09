# Source: https://docs.datadoghq.com/security/default_rules/1bw-akj-fk6.md

---
title: Microsoft 365 Unified Audit Logging Disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Microsoft 365 Unified Audit Logging
  Disabled
---

# Microsoft 365 Unified Audit Logging Disabled
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Detect when unified audit logging is disabled. An adversary or insider threat can disable audit logging as a means of defense evasion.

## Strategy{% #strategy %}

Monitor Microsoft 365 audit logs to look for events with an `@evt.name` value of `Set-AdminAuditLogConfig`, where `@Parameters.UnifiedAuditLogIngestionEnabled` is set to `False`.

## Triage and response{% #triage-and-response %}

1. Determine if the user `{{@usr.email}}` intended to disable audit logging.
1. If `{{@usr.email}}` is not responsible for disabling the audit logging, investigate `{{@usr.email}}` for anomalous activity. If necessary, initiate your company's incident response (IR) process.

## Changelog{% #changelog %}

- 6 January 2023 - Updated rule name and case.
