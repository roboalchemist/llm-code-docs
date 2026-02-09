# Source: https://docs.datadoghq.com/security/default_rules/def-000-nf7.md

---
title: GitHub IP allow list
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > GitHub IP allow list
---

# GitHub IP allow list
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Detect when a GitHub IP allowlist setting has been modified.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for when an IP allowlist setting has been modified. By default, authorized users can access your organization's resources from any IP address. You can restrict access to your organization's private resources by configuring a list that allows or denies access from specific IP addresses. Modifying these settings could lead to a degradation in the organization's security posture.

## Triage and response{% #triage-and-response %}

1. Determine if the change taken by `{{@github.actor}}` is authorized.
1. If the change was not authorized or was unexpected, begin your organization's incident response process and investigate.
