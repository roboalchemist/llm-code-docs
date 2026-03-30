# Source: https://docs.datadoghq.com/security/default_rules/def-000-f2a.md

---
title: TruffleHog user agent observed in AWS
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > TruffleHog user agent observed in AWS
---

# TruffleHog user agent observed in AWS
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1552-unsecured-credentials](https://attack.mitre.org/techniques/T1552)
## Goal{% #goal %}

Detect when a TruffleHog user agent is seen in AWS CloudTrail management plane logs.

## Strategy{% #strategy %}

This rule monitors AWS CloudTrail management plane logs for the `GetCallerIdentity` API call with the user agent `TruffleHog`. TruffleHog is a tool designed to scan source code repositories for leaked secrets. There is a credential verification feature to verify if the credential is still active. For AWS it performs a `GetCallerIdentity` API call. While this tool can be used legitimately by teams to scan for leaked secrets internally, it may also be used by attackers to identify leaked credentials.

## Triage and response{% #triage-and-response %}

1. Determine if your organization is using the TruffleHog tool to scan for secrets.
1. If it is an internal tool, notify the relevant team so that the leaked key can be triaged appropriately.
1. If the results of the triage indicate that this tool is not used by your organization, begin your company's incident response process and an investigation.
   - If appropriate, disable or rotate the affected credential.
   - Investigate any actions taken by the identity `{{@userIdentity.arn}}`.
   - Work with the relevant teams to remove the key from any source code repositories.

## Changelog{% #changelog %}

- 10 November 2023 - updated severity of detection from `Low` to `High`
- 25 September 2025 - updated user agent to have wildcards around the `TruffleHog` string
