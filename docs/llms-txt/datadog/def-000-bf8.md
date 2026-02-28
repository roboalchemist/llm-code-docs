# Source: https://docs.datadoghq.com/security/default_rules/def-000-bf8.md

---
title: AWS IAM Roles Anywhere trust anchor created
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS IAM Roles Anywhere trust anchor
  created
---

# AWS IAM Roles Anywhere trust anchor created
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Detect when an IAM Roles Anywhere trust anchor is created.

## Strategy{% #strategy %}

This rule monitors CloudTrail logs for `CreateTrustAnchor` API calls. An attacker may attempt to establish persistence by creating an IAM Roles Anywhere trust anchor. The IAM Roles Anywhere service allows workloads that do not run in AWS to assume roles by presenting a client-side X.509 certificate signed by a trusted certificate authority, called a "trust anchor".

## Triage & response{% #triage--response %}

1. Determine if the API call: `{{@evt.name}}` should have been performed by the user: `{{@userIdentity.arn}}`:
   - Contact the user to confirm if they made the API call.
1. If the API call was not made by the user:
   - Rotate the user credentials.
   - Determine what actions the user took and which new access keys the user created.
   - Begin your organization's incident response process and investigate.
1. If the API call was made legitimately by the user:
   - Confirm if an IAM Roles Anywhere trust anchor is the proper authentication mechanism for the resource.

## Changelog{% #changelog %}

- 4 June 2025 - Updated rule case to `Medium`.
