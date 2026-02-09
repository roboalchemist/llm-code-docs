# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.controltower_enabled_baseline.dataset.md

---
title: Control Tower Enabled Baseline
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Control Tower Enabled Baseline
---

# Control Tower Enabled Baseline

Control Tower Enabled Baseline in AWS represents a summary of a baseline configuration that has been enabled within AWS Control Tower. A baseline is a set of guardrails, policies, and configurations applied to accounts to ensure they meet governance and compliance requirements. This resource provides details about which baseline is active, helping administrators track and manage standardized configurations across multiple accounts in an AWS environment.

```
aws.controltower_enabled_baseline
```

## Fields

| Title                | ID   | Type       | Data Type                                                                                          | Description |
| -------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string     |
| account_id           | core | string     |
| arn                  | core | string     | The ARN of the EnabledBaseline resource                                                            |
| baseline_identifier  | core | string     | The specific baseline that is enabled as part of the EnabledBaseline resource.                     |
| baseline_version     | core | string     | The enabled version of the baseline.                                                               |
| drift_status_summary | core | json       | The drift status of the enabled baseline.                                                          |
| parent_identifier    | core | string     | An ARN that represents an object returned by ListEnabledBaseline, to describe an enabled baseline. |
| status_summary       | core | json       | The deployment summary of an EnabledControl or EnabledBaseline resource.                           |
| tags                 | core | hstore_csv |
| target_identifier    | core | string     | The target upon which the baseline is enabled.                                                     |
