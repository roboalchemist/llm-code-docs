# Source: https://docs.datadoghq.com/security/default_rules/def-000-otd.md

---
title: Snowflake anomalous querying of data by user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Snowflake anomalous querying of data by
  user
---

# Snowflake anomalous querying of data by user
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1530-data-from-cloud-storage](https://attack.mitre.org/techniques/T1530)
## Goal{% #goal %}

Detect anomalous amount of data queried by a user account in your Snowflake environment.

## Strategy{% #strategy %}

This rule allows you to detect when an account queries a anomalous amount of data in Snowflake.

## Triage and response{% #triage-and-response %}

1. Inspect the logs to identify the user or service account and the table accessed.
1. Investigate whether that user role is expected to access the specific table.
1. Reach out to user if there are no signs of compromise and validate business use case.
1. If there are signs of compromise, disable the user and rotate credentials.
