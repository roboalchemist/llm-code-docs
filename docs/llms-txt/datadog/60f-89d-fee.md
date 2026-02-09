# Source: https://docs.datadoghq.com/security/default_rules/60f-89d-fee.md

---
title: Google Cloud SQL database modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Google Cloud SQL database modified
---

# Google Cloud SQL database modified
Classification:complianceTactic:[TA0040-impact](https://attack.mitre.org/tactics/TA0040)Technique:[T1565-data-manipulation](https://attack.mitre.org/techniques/T1565) 
## Goal{% #goal %}

Detect when a Google Cloud SQL database has been modified.

## Strategy{% #strategy %}

This rule lets you monitor Google Cloud SQL admin activity audit logs to determine when one of the following methods is invoked:

- `cloudsql.instances.create`
- `cloudsql.instances.create`
- `cloudsql.users.update`

## Triage and response{% #triage-and-response %}

1. Review the Google Cloud SQL database and ensure it is configured properly with the correct permissions.
