# Source: https://docs.datadoghq.com/security/default_rules/def-000-pdi.md

---
title: AWS IAM activity from EC2 instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > AWS IAM activity from EC2 instance
---

# AWS IAM activity from EC2 instance
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detect when an AWS EC2 instance role makes API calls to AWS IAM.

## Strategy{% #strategy %}

This rule lets you monitor CloudTrail to detect when an AWS EC2 instance role makes certain API calls to IAM. An attacker who has managed to retrieve temporary access keys assigned to a EC2 instance may try to retain access or escalate privileges by the making the following API calls:

- CreateUser
- AttachUserPolicy
- CreateLoginProfile
- UpdateLoginProfile
- CreateAccessKey
- CreateGroup
- AttachGroupPolicy
- CreateRole
- AttachRolePolicy

## Triage and response{% #triage-and-response %}

1. Determine if `{{@userIdentity.session_name}}` should be attempting to make the identified API calls.

- Use the Cloud SIEM - Host Investigation dashboard to assess host activity.
Contact the team that owns the service the host is part of, to confirm it should make these API calls.If this is abnormal behavior for the host:
- Revoke role temporary credentials.
- Investigate to see what API calls might have been made that were successful throughout the rest of the environment.
