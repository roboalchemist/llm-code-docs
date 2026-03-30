# Source: https://docs.datadoghq.com/security/default_rules/def-000-ftu.md

---
title: Snowflake stage set to anomalous external cloud location
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Snowflake stage set to anomalous
  external cloud location
---

# Snowflake stage set to anomalous external cloud location
Classification:attackTactic:[TA0010-exfiltration](https://attack.mitre.org/tactics/TA0010)Technique:[T1537-transfer-data-to-cloud-account](https://attack.mitre.org/techniques/T1537)
## Goal{% #goal %}

Detect an anomalous stage transfer to an external cloud provider in your Snowflake environment.

## Strategy{% #strategy %}

Snowflake facilitates data export to cloud storage services through the "stage" functionality. This rule allows you to detect an external data transfer through a stage to an unexpected cloud provider in Snowflake. There may be cases in which setting a stage to an external stage URL is expected behavior; however, all URLs in the logs should be populated from your own infrastructure resources, such as a company-owned S3 bucket. An unknown external stage URL can be an indicator that an attacker has exfiltrated data to that URL.

## Triage and response{% #triage-and-response %}

1. Inspect the logs to identify the stage URL, timestamp, username and stage name.
1. Investigate whether that export bucket is expected and owned by the company.
1. If there are signs of compromise, disable the user associated with the stage and rotate credentials.
