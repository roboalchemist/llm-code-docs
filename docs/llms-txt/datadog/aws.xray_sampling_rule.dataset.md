# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.xray_sampling_rule.dataset.md

---
title: X-Ray Sampling Rule
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > X-Ray Sampling Rule
---

# X-Ray Sampling Rule

This table represents the X-Ray Sampling Rule resource from Amazon Web Services.

```
aws.xray_sampling_rule
```

## Fields

| Title         | ID   | Type       | Data Type                        | Description |
| ------------- | ---- | ---------- | -------------------------------- | ----------- |
| _key          | core | string     |
| account_id    | core | string     |
| created_at    | core | timestamp  | When the rule was created.       |
| modified_at   | core | timestamp  | When the rule was last modified. |
| sampling_rule | core | json       | The sampling rule.               |
| tags          | core | hstore_csv |
