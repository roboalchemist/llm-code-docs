# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sfn_activity.dataset.md

---
title: Step Functions Activity
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Step Functions Activity
---

# Step Functions Activity

This table represents the Step Functions Activity resource from Amazon Web Services.

```
aws.sfn_activity
```

## Fields

| Title                    | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Description |
| ------------------------ | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string     |
| account_id               | core | string     |
| activity_arn             | core | string     | The Amazon Resource Name (ARN) that identifies the activity.                                                                                                                                                                                                                                                                                                                                                                                              |
| creation_date            | core | timestamp  | The date the activity is created.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| encryption_configuration | core | json       | Settings for configured server-side encryption.                                                                                                                                                                                                                                                                                                                                                                                                           |
| name                     | core | string     | The name of the activity. A name must <i>not</i> contain: <ul> <li> white space </li> <li> brackets <code>&lt; &gt; { } [ ]</code> </li> <li> wildcard characters <code>? *</code> </li> <li> special characters <code>" # % \ ^ | ~ ` $ &amp; , ; : /</code> </li> <li> control characters (<code>U+0000-001F</code>, <code>U+007F-009F</code>) </li> </ul> To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _. |
| tags                     | core | hstore_csv |
