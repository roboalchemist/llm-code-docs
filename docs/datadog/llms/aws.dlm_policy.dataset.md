# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.dlm_policy.dataset.md

---
title: DLM Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DLM Policy
---

# DLM Policy

This table represents the DLM Policy resource from Amazon Web Services.

```
aws.dlm_policy
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                                                         | Description |
| ------------------ | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| date_created       | core | timestamp  | The local date and time when the lifecycle policy was created.                                                                                                                                                                    |
| date_modified      | core | timestamp  | The local date and time when the lifecycle policy was last modified.                                                                                                                                                              |
| default_policy     | core | bool       | Indicates whether the policy is a default lifecycle policy or a custom lifecycle policy. <ul> <li> <code>true</code> - the policy is a default policy. </li> <li> <code>false</code> - the policy is a custom policy. </li> </ul> |
| description        | core | string     | The description of the lifecycle policy.                                                                                                                                                                                          |
| execution_role_arn | core | string     | The Amazon Resource Name (ARN) of the IAM role used to run the operations specified by the lifecycle policy.                                                                                                                      |
| policy_arn         | core | string     | The Amazon Resource Name (ARN) of the policy.                                                                                                                                                                                     |
| policy_details     | core | json       | The configuration of the lifecycle policy                                                                                                                                                                                         |
| policy_id          | core | string     | The identifier of the lifecycle policy.                                                                                                                                                                                           |
| state              | core | string     | The activation state of the lifecycle policy.                                                                                                                                                                                     |
| status_message     | core | string     | The description of the status.                                                                                                                                                                                                    |
| tags               | core | hstore_csv |
