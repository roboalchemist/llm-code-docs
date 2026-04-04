# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.organizations_policy_statement.dataset.md

---
title: Organizations Policy Statement
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Organizations Policy Statement
---

# Organizations Policy Statement

This table represents the Organizations Policy Statement resource from Amazon Web Services.

```
aws.organizations_policy_statement
```

## Fields

| Title                | ID   | Type       | Data Type                                                                                                                 | Description |
| -------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string     |
| account_id           | core | string     |
| content              | core | string     | The text content of the policy.                                                                                           |
| policy_statement_arn | core | string     |
| policy_summary       | core | json       | A structure that contains additional details about the policy.                                                            |
| tags                 | core | hstore_csv |
| targets              | core | json       | A list of structures, each of which contains details about one of the entities to which the specified policy is attached. |
