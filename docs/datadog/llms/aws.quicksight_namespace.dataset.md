# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.quicksight_namespace.dataset.md

---
title: QuickSight Namespace
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > QuickSight Namespace
---

# QuickSight Namespace

QuickSight Namespace is a logical container within Amazon QuickSight that allows you to isolate and manage users, groups, and assets separately from other namespaces in the same AWS account. It enables multi-tenant environments by providing dedicated spaces for different teams, departments, or customers, ensuring data and resource segregation while still using a single QuickSight account.

```
aws.quicksight_namespace
```

## Fields

| Title                               | ID   | Type       | Data Type                                                               | Description |
| ----------------------------------- | ---- | ---------- | ----------------------------------------------------------------------- | ----------- |
| _key                                | core | string     |
| account_id                          | core | string     |
| arn                                 | core | string     | The namespace ARN.                                                      |
| capacity_region                     | core | string     | The namespace Amazon Web Services Region.                               |
| creation_status                     | core | string     | The creation status of a namespace that is not yet completely created.  |
| iam_identity_center_application_arn | core | string     | The Amazon Resource Name (ARN) for the IAM Identity Center application. |
| iam_identity_center_instance_arn    | core | string     | The Amazon Resource Name (ARN) for the IAM Identity Center instance.    |
| identity_store                      | core | string     | The identity store used for the namespace.                              |
| name                                | core | string     | The name of the error.                                                  |
| namespace_error                     | core | json       | An error that occurred when the namespace was created.                  |
| tags                                | core | hstore_csv |
