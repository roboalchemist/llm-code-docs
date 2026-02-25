# Source: https://docs.datadoghq.com/security/default_rules/kc5-vk1-ysw.md

---
title: A new Microsoft 365 application was installed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > A new Microsoft 365 application was
  installed
---

# A new Microsoft 365 application was installed
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1136-create-account](https://attack.mitre.org/techniques/T1136)
## Goal{% #goal %}

Detect when a new Microsoft 365 app is installed as a means of establishing persistence.

## Strategy{% #strategy %}

Monitor Microsoft 365 audit logs to look for events with an `@evt.name` value of `Add application.` and event `@evt.outcome` of `Success`.

## Triage and response{% #triage-and-response %}

1. Determine if the user `{{@usr.email}}` intended to install `{{@ObjectId}}`.
1. If `{{@usr.email}}` is not responsible for installing `{{@ObjectId}}`, investigate `{{@usr.email}}` for anomalous activity. If necessary, initiate your company's incident response (IR) process.
