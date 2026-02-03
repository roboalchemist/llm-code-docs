# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.resiliencehub_resiliency_policy.dataset.md

---
title: Resilience Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Resilience Policy
---

# Resilience Policy

A Resilience Policy in AWS Resilience Hub defines the recovery objectives for applications, such as Recovery Time Objective (RTO) and Recovery Point Objective (RPO). It helps set clear targets for how quickly and how much data an application should recover after a disruption. This policy guides resilience assessments and recommendations, ensuring applications meet business continuity requirements.

```
aws.resiliencehub_resiliency_policy
```

## Fields

| Title                    | ID   | Type       | Data Type                                                                                                                                                                                                                                                                      | Description |
| ------------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                     | core | string     |
| account_id               | core | string     |
| creation_time            | core | timestamp  | Date and time when the resiliency policy was created.                                                                                                                                                                                                                          |
| data_location_constraint | core | string     | Specifies a high-level geographical location constraint for where your resilience policy data can be stored.                                                                                                                                                                   |
| estimated_cost_tier      | core | string     | Specifies the estimated cost tier of the resiliency policy.                                                                                                                                                                                                                    |
| policy                   | core | string     | The resiliency policy.                                                                                                                                                                                                                                                         |
| policy_arn               | core | string     | Amazon Resource Name (ARN) of the resiliency policy. The format for this ARN is: arn:partition:resiliencehub:region:account:resiliency-policy/policy-id. For more information about ARNs, see Amazon Resource Names (ARNs) in the Amazon Web Services General Reference guide. |
| policy_description       | core | string     | Description of the resiliency policy.                                                                                                                                                                                                                                          |
| policy_name              | core | string     | The name of the policy                                                                                                                                                                                                                                                         |
| tags                     | core | hstore_csv |
| tier                     | core | string     | The tier for this resiliency policy, ranging from the highest severity (MissionCritical) to lowest (NonCritical).                                                                                                                                                              |
