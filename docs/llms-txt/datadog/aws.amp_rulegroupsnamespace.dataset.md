# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.amp_rulegroupsnamespace.dataset.md

---
title: AMP Rule Groups Namespace
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AMP Rule Groups Namespace
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.amp_rulegroupsnamespace.dataset/index.html
---

# AMP Rule Groups Namespace

This table represents the AMP Rule Groups Namespace resource from Amazon Web Services.

```
aws.amp_rulegroupsnamespace
```

## Fields

| Title       | ID   | Type      | Data Type                                                                                                                                                                       | Description |
| ----------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key        | core | string    |
| account_id  | core | string    |
| arn         | core | string    | The ARN of the rule groups namespace. For example, <code>arn:aws:aps:&lt;region&gt;:123456789012:rulegroupsnamespace/ws-example1-1234-abcd-5678-ef90abcd1234/rulesfile1</code>. |
| created_at  | core | timestamp | The date and time that the rule groups namespace was created.                                                                                                                   |
| modified_at | core | timestamp | The date and time that the rule groups namespace was most recently changed.                                                                                                     |
| name        | core | string    | The name of the rule groups namespace.                                                                                                                                          |
| status      | core | json      | The current status of the rule groups namespace.                                                                                                                                |
| tags        | core | hstore    |
