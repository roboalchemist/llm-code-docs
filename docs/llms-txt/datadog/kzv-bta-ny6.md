# Source: https://docs.datadoghq.com/security/default_rules/kzv-bta-ny6.md

---
title: Cloud credentials accessed by network utility
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Cloud credentials accessed by network
  utility
---

# Cloud credentials accessed by network utility
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1552-unsecured-credentials](https://attack.mitre.org/techniques/T1552)
## What happened{% #what-happened %}

The process `{{ @process.comm }}` made an IMDS request to an endpoint used to access temporary cloud credentials.

## Goal{% #goal %}

Detect when a network utility (like `cURL` or `Wget`) is used to access the cloud Instance Metadata Service (IMDS) in an interactive session.

## Strategy{% #strategy %}

The IMDS is a link-local HTTP endpoint that provides data about a given cloud instance. One function is to provide temporary security credentials so that they do not need to be stored on the host. Because IMDS can be used to fetch security credentials, attackers may use it to escalate privileges in order to access other cloud resources. This detection identifies when Linux network utilities are used in an interactive session to access the metadata service. It is unusual for this activity to occur interactively, especially in production environments.

## Triage & Response{% #triage--response %}

1. Determine whether or not this is expected behavior. For example, did an employee run commands for an approved reason, or did a configuration management utility use an interactive session?
1. If this behavior is unexpected, attempt to contain the compromise (possibly by terminating the workload, depending on the stage of attack) and look for indications of the initial compromise. Follow your organization's internal processes for investigating and remediating compromised systems.
1. Determine the nature of the attack and the tools involved. Investigate security signals (if present) occurring around the time of the event to establish an attack path.
1. Using cloud audit logs, identify if the attached identity was misused.
1. Find and repair the initial entry point.

## Changelog{% #changelog %}

- 26 September 2024 - Updated rule name, severity, and description

*Requires Agent version 7.27 or later.*
