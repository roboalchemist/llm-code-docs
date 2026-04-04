# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/oci/oci.logging_log_group.dataset.md

---
title: Log Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Log Group
---

# Log Group

A Log Group in Oracle Cloud Infrastructure (OCI) is a logical container used to organize and manage multiple logs that share the same lifecycle, access policies, and retention settings. It simplifies log management by grouping related logs together, making it easier to control permissions, configure retention rules, and streamline monitoring across different services or applications.

```
oci.logging_log_group
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                   | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| cloud_account_id   | core | string     | The identifier of the related cloud account. The concept of an account might have different names in different cloud providers. AWS is calling it account, GCP calls it project and Azure uses the term subscription.                                                                       |
| cloud_account_name | core | string     | The name of the account this resource belongs to.                                                                                                                                                                                                                                           |
| cloud_provider     | core | string     | The name of the cloud provider.                                                                                                                                                                                                                                                             |
| cloud_tags         | core | hstore     |
| compartment_id     | core | string     | The value to assign to the compartment_id property of this LogGroup.                                                                                                                                                                                                                        |
| created_at         | core | timestamp  | Time when the resource has been created.                                                                                                                                                                                                                                                    |
| description        | core | string     | The value to assign to the description property of this LogGroup.                                                                                                                                                                                                                           |
| freeform_tags      | core | hstore     | The value to assign to the freeform_tags property of this LogGroup.                                                                                                                                                                                                                         |
| id                 | core | string     | The value to assign to the id property of this LogGroup.                                                                                                                                                                                                                                    |
| lifecycle_state    | core | string     | The value to assign to the lifecycle_state property of this LogGroup. Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "INACTIVE", "DELETING", "FAILED", 'UNKNOWN_ENUM_VALUE'. Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'. |
| name               | core | string     | The name of this resource.                                                                                                                                                                                                                                                                  |
| region_id          | core | string     | The region this resource resides within.                                                                                                                                                                                                                                                    |
| resource_type      | core | string     | The name of the resource type.                                                                                                                                                                                                                                                              |
| tags               | core | hstore_csv |
| time_created       | core | timestamp  | The value to assign to the time_created property of this LogGroup.                                                                                                                                                                                                                          |
| time_last_modified | core | timestamp  | The value to assign to the time_last_modified property of this LogGroup.                                                                                                                                                                                                                    |
| updated_at         | core | timestamp  | Time when the resource has been updated the last time.                                                                                                                                                                                                                                      |
| zone_id            | core | string     | The zone this resource resides within.                                                                                                                                                                                                                                                      |
