# Source: https://docs.datadoghq.com/security/default_rules/def-000-mpx.md

---
title: GitHub branch protection disabled on branch
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitHub branch protection disabled on
  branch
---

# GitHub branch protection disabled on branch
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect when GitHub branch protection has been disabled on a branch.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for when GitHub branch protection has been disabled on a branch. Organizations can protect important branches by setting branch protection rules, which define whether collaborators can delete or force push to the branch and set requirements for any pushes to the branch, such as passing status checks or a linear commit history. Disabling this protection could lead to degradation in the security posture of an organization.

## Triage and response{% #triage-and-response %}

1. Determine if the change taken by `{{@github.actor}}` is authorized.
1. If the change was not authorized or was unexpected, begin your organization's incident response process and investigate.
