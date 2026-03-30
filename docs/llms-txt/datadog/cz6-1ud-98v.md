# Source: https://docs.datadoghq.com/security/default_rules/cz6-1ud-98v.md

---
title: Anomalous amount of Salesforce query results
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Anomalous amount of Salesforce query
  results
---

# Anomalous amount of Salesforce query results
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1213-data-from-information-repositories](https://attack.mitre.org/techniques/T1213)
## Goal{% #goal %}

Detect when there is a spike in Salesforce query results for a user. A large query can be an early warning sign of a user attempting to exfiltrate Salesforce data.

## Strategy{% #strategy %}

Inspect and baseline Salesforce logs and determine if there is a spike in the number of rows returned (`@rows_returned`).

## Triage and response{% #triage-and-response %}

Determine if the user should be legitimately performing large queries.
