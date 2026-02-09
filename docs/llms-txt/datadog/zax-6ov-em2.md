# Source: https://docs.datadoghq.com/security/default_rules/zax-6ov-em2.md

---
title: Azure user viewed CosmosDB connection string
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure user viewed CosmosDB connection
  string
---

# Azure user viewed CosmosDB connection string
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1580-cloud-infrastructure-discovery](https://attack.mitre.org/techniques/T1580) 
## Goal{% #goal %}

Detect when a user successfully requests to view a CosmoDB connection string with the Azure API. An attacker with the appropriate privileges can view a connection string and use it to access or modify data in the CosmoDB database.

## Strategy{% #strategy %}

Monitor Azure CosmoDB logs where `@evt.name` is `"MICROSOFT.DOCUMENTDB/DATABASEACCOUNTS/LISTCONNECTIONSTRINGS/ACTION"` and `@evt.outcome` is `Success`.

## Triage and response{% #triage-and-response %}

1. Verify that the user (`{{@usr.name}}`) should be viewing the connection string for the following CosmoDB database: (`{{@resourceId}}`).
1. If the activity is not expected, investigate the activity around the CosmoDB (`{{@resourceId}}`).
