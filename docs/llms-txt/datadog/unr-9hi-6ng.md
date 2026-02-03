# Source: https://docs.datadoghq.com/security/default_rules/unr-9hi-6ng.md

---
title: AWS EC2 new event for application
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > AWS EC2 new event for application
---

# AWS EC2 new event for application
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1580-cloud-infrastructure-discovery](https://attack.mitre.org/techniques/T1580) 
## Goal{% #goal %}

Detects when an application on a host has a new, unrecognized API call.

## Strategy{% #strategy %}

Using the `New Value` detection method, find when an `application` has a new `@evt.name` on a `host`.

## Triage and response{% #triage-and-response %}

1. Determine if the `host: {{host}}` running the `application: {{application}}` should have done the following event(s)`{{@evt.name}}`:
   - If yes, you can `Archive` the signal.
   - If no, investigate further by clicking on the **Suggested Actions** tab for the signal
1. If necessary, initiate your company's incident response process.

## Changelog{% #changelog %}

- 14 November 2022 - Updated severity.
