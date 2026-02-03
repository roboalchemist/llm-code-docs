# Source: https://docs.datadoghq.com/security/default_rules/yvc-dgl-9nb.md

---
title: Google Cloud IAM Role updated
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Google Cloud IAM Role updated
---

# Google Cloud IAM Role updated
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detect when a Google Cloud IAM role is updated.

## Strategy{% #strategy %}

Monitor Google Cloud IAM activity audit logs to determine when the following method is invoked:

- `google.iam.admin.v1.UpdateRole`

## Triage and response{% #triage-and-response %}

1. Investigate the user {{@usr.id}} who performed the role update on {{@data.protoPayload.resourceName}} and ensure the permissions in `@data.protoPayload.response.included_permissions` are scoped properly.
1. Review the users associated with the role and ensure they should have the permissions attached to the role.

## Changelog{% #changelog %}

- 25 September 2024 - Updated query to replace attribute `@threat_intel.results.category:anonymizer`.
