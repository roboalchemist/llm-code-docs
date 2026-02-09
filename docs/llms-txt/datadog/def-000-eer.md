# Source: https://docs.datadoghq.com/security/default_rules/def-000-eer.md

---
title: Snowflake external access occurred
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Snowflake external access occurred
---

# Snowflake external access occurred
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1199-trusted-relationship](https://attack.mitre.org/techniques/T1199) 
## Goal{% #goal %}

Detect when an external access event occurs in your Snowflake environment.

## Strategy{% #strategy %}

This rule allows you to detect when a new external access event occurs in Snowflake. Review any suspicious entries of external access performed by procedure or user-defined function (UDF) handler code within the last 365 days through the External Access History table. Unexpected use of external access for your environment is a potential indicator of compromise.

## Triage and response{% #triage-and-response %}

1. Inspect the logs to identify the source cloud, source region, target cloud, target region, and query ID.
1. Investigate whether the source and target cloud locations are expected.
1. Using the query ID, correlate the behavior with Query History logs to determine the user, query, and other useful information.
1. If there are signs of compromise, disable the user associated with the external access integration and rotate credentials.
