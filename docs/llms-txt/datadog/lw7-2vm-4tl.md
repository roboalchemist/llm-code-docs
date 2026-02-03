# Source: https://docs.datadoghq.com/security/default_rules/lw7-2vm-4tl.md

---
title: Exchange Online mail forwarding rule enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Exchange Online mail forwarding rule
  enabled
---

# Exchange Online mail forwarding rule enabled
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1137-office-application-startup](https://attack.mitre.org/techniques/T1137) 
## Goal{% #goal %}

Detect when a user sets up a mail forwarding rule to another email address. An adversary or insider threat could set a forwarding rule to forward all emails to an external email address.

## Strategy{% #strategy %}

Monitor Microsoft 365 audit logs to look for events with `@evt.name` value of `Set-Mailbox`, where a value is set for `@Parameters.ForwardingSmtpAddress` and the `@evt.outcome` is `True`.

## Triage and response{% #triage-and-response %}

1. Inspect the `@Parameters.ForwardingSmtpAddress` for `{{@usr.email}}` to see if it is sending email to an external non-company owned domain.
1. Determine if there is a legitimate use case for the mail forwarding rule.
1. If `{{@usr.email}}` is not aware of the mail forwarding rule, investigate all `{{@usr.email}}` accounts for anomalous activity.
