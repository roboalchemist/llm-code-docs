# Source: https://docs.datadoghq.com/security/default_rules/def-000-j1q.md

---
title: Salesforce login from unseen application
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Salesforce login from unseen
  application
---

# Salesforce login from unseen application
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detects Salesforce login attempts from previously unseen applications.

## Strategy{% #strategy %}

This rule monitors Salesforce login events where `@evt.name` is `Login` or `LoginEvent` with an `@application` field present. It uses new value detection to identify when any application that has not been previously observed attempts to authenticate to the Salesforce environment. New applications accessing Salesforce may indicate legitimate business expansion, new integrations, or potentially malicious applications attempting unauthorized access.

## Triage & Response{% #triage--response %}

- Examine the application name and details for `{{@application}}` to determine if it represents a legitimate business application or potentially malicious software.
- Review recent IT change requests and application deployments to verify if the new application was authorized and expected.
- Analyze the login patterns and user accounts associated with the new application to identify any suspicious authentication activity.
- Check if the new application has appropriate security configurations and follows organizational security policies.
- Verify with IT administrators or application owners whether the new application access was planned and authorized.

*This detection is based on data from [Drift/Salesforce Security Update](https://trust.salesloft.com/?uid=Drift%2FSalesforce+Security+Update) and [Widespread Data Theft Targets Salesforce Instances via Salesloft Drift](https://cloud.google.com/blog/topics/threat-intelligence/data-theft-salesforce-instances-via-salesloft-drift).*
