# Source: https://docs.datadoghq.com/security/default_rules/8pu-lqe-4ze.md

---
title: Azure user invited an external user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Azure user invited an external user
---

# Azure user invited an external user
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1136-create-account](https://attack.mitre.org/techniques/T1136)
## Goal{% #goal %}

Detect when an invitation is sent to an external user.

## Strategy{% #strategy %}

Monitor Azure Active Directory Audit logs and detect when any `@evt.name` is equal to `Invite external user` and the `@evt.outcome` is equal to `success`.

## Triage and response{% #triage-and-response %}

Review and determine if the invitation and its recipient are valid.
