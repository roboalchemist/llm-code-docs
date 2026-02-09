# Source: https://docs.datadoghq.com/security/default_rules/def-000-fxj.md

---
title: Snowflake new data transfer to location
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Snowflake new data transfer to location
---

# Snowflake new data transfer to location
Classification:attackTactic:[TA0010-exfiltration](https://attack.mitre.org/tactics/TA0010)Technique:[T1537-transfer-data-to-cloud-account](https://attack.mitre.org/techniques/T1537) 
## Goal{% #goal %}

Detect anomalous transfer of data to an external cloud provider in your Snowflake environment.

## Strategy{% #strategy %}

This rule allows you to detect when an external data transfer occurs to an unexpected cloud provider in Snowflake. Data transfers include `@source_cloud`, `@bytes_transferred`, and `@source_region` that can be compared with the `@target_cloud` and `@target_region`. This behavior can be traced to known data transfers from expected cloud environments. If the source and target destinations do not match, consider further investigation to determine if this is a potential indicator of data exfiltration.

## Triage and response{% #triage-and-response %}

1. Inspect the logs to identify the target cloud, target region, and transfer type.
1. Investigate whether that cloud region is expected.
1. Using the transfer type and start time, correlate the behavior with other logs to determine user, query, and other useful information.
1. If there are signs of compromise, disable the user associated with the transfer and rotate credentials.
