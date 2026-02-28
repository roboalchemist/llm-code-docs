# Source: https://docs.datadoghq.com/security/default_rules/def-000-dgf.md

---
title: Snowflake known malicious client application session
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Snowflake known malicious client
  application session
---

# Snowflake known malicious client application session
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1199-trusted-relationship](https://attack.mitre.org/techniques/T1199)
## Goal{% #goal %}

Detect known malicious client applications interacting in your Snowflake environment.

## Strategy{% #strategy %}

This rule allows you to detect when a [malicious client application](https://community.snowflake.com/s/article/Communication-ID-0108977-Additional-Information) establishes a session in Snowflake. Client applications are set up to allow for automation and integrations. An attacker may have set up a session from an outside tool in order to access and exfiltrate data.

## Triage and response{% #triage-and-response %}

1. Inspect the logs to identify the client application, operating system, and timestamp.
1. Investigate whether that client application is expected in your environment.
1. If there are signs of compromise, disable the client application associated with the session and rotate credentials.
