# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ses_rule_set.dataset.md

---
title: SES Rule Set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SES Rule Set
---

# SES Rule Set

This table represents the SES Rule Set resource from Amazon Web Services.

```
aws.ses_rule_set
```

## Fields

| Title                  | ID   | Type       | Data Type                                                | Description |
| ---------------------- | ---- | ---------- | -------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| created_date           | core | timestamp  | The date of when then rule set was created.              |
| last_modification_date | core | timestamp  | The date of when the rule set was last modified.         |
| rule_set_arn           | core | string     | The Amazon Resource Name (ARN) of the rule set resource. |
| rule_set_id            | core | string     | The identifier of the rule set resource.                 |
| rule_set_name          | core | string     | A user-friendly name for the rule set resource.          |
| rules                  | core | json       | The rules contained in the rule set.                     |
| tags                   | core | hstore_csv |
