# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.verifiedpermissions_policy_store.dataset.md

---
title: Verified Permissions Policy Store
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Verified Permissions Policy Store
---

# Verified Permissions Policy Store

Verified Permissions Policy Store in AWS is a managed resource that holds and organizes authorization policies for applications. It provides a central location to define, manage, and retrieve policies that control access decisions. This store enables consistent enforcement of fine-grained permissions across services and applications, ensuring secure and scalable authorization management.

```
aws.verifiedpermissions_policy_store
```

## Fields

| Title               | ID   | Type       | Data Type                                                                                                                                                                                | Description |
| ------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                | core | string     |
| account_id          | core | string     |
| arn                 | core | string     | The Amazon Resource Name (ARN) of the policy store.                                                                                                                                      |
| cedar_version       | core | string     | The version of the Cedar language used with policies, policy templates, and schemas in this policy store. For more information, see Amazon Verified Permissions upgrade to Cedar v4 FAQ. |
| created_date        | core | timestamp  | The date and time that the policy store was originally created.                                                                                                                          |
| deletion_protection | core | string     | Specifies whether the policy store can be deleted. If enabled, the policy store can't be deleted. The default state is DISABLED.                                                         |
| description         | core | string     | Descriptive text that you can provide to help with identification of the current policy store.                                                                                           |
| last_updated_date   | core | timestamp  | The date and time that the policy store was last updated.                                                                                                                                |
| policy_store_id     | core | string     | The ID of the policy store;                                                                                                                                                              |
| tags                | core | hstore_csv |
| validation_settings | core | json       | The current validation settings for the policy store.                                                                                                                                    |
