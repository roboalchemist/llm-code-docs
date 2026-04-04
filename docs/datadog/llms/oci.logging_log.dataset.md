# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/oci/oci.logging_log.dataset.md

---
title: Log
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Log
---

# Log

Log in Oracle Cloud Infrastructure is a resource that captures, stores, and manages log data from various OCI services and custom applications. It allows you to centralize logs for monitoring, troubleshooting, and auditing purposes. Logs can be ingested in real time, filtered, and routed to services like Logging Analytics or Object Storage for deeper analysis and long-term retention.

```
oci.logging_log
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                                                                                                              | Description |
| ------------------ | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| cloud_account_id   | core | string     | The identifier of the related cloud account. The concept of an account might have different names in different cloud providers. AWS is calling it account, GCP calls it project and Azure uses the term subscription.                                                                  |
| cloud_account_name | core | string     | The name of the account this resource belongs to.                                                                                                                                                                                                                                      |
| cloud_provider     | core | string     | The name of the cloud provider.                                                                                                                                                                                                                                                        |
| cloud_tags         | core | hstore     |
| compartment_id     | core | string     | The value to assign to the compartment_id property of this Log.                                                                                                                                                                                                                        |
| configuration      | core | json       | The value to assign to the configuration property of this Log.                                                                                                                                                                                                                         |
| created_at         | core | timestamp  | Time when the resource has been created.                                                                                                                                                                                                                                               |
| freeform_tags      | core | hstore     | The value to assign to the freeform_tags property of this Log.                                                                                                                                                                                                                         |
| id                 | core | string     | The value to assign to the id property of this Log.                                                                                                                                                                                                                                    |
| is_enabled         | core | bool       | The value to assign to the is_enabled property of this Log.                                                                                                                                                                                                                            |
| lifecycle_state    | core | string     | The value to assign to the lifecycle_state property of this Log. Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "INACTIVE", "DELETING", "FAILED", 'UNKNOWN_ENUM_VALUE'. Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'. |
| log_group_id       | core | string     | The value to assign to the log_group_id property of this Log.                                                                                                                                                                                                                          |
| log_type           | core | string     | The value to assign to the log_type property of this Log. Allowed values for this property are: "CUSTOM", "SERVICE", 'UNKNOWN_ENUM_VALUE'. Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.                                                       |
| name               | core | string     | The name of this resource.                                                                                                                                                                                                                                                             |
| region_id          | core | string     | The region this resource resides within.                                                                                                                                                                                                                                               |
| resource_type      | core | string     | The name of the resource type.                                                                                                                                                                                                                                                         |
| retention_duration | core | int64      | The value to assign to the retention_duration property of this Log.                                                                                                                                                                                                                    |
| tags               | core | hstore_csv |
| tenancy_id         | core | string     | The value to assign to the tenancy_id property of this Log.                                                                                                                                                                                                                            |
| time_created       | core | timestamp  | The value to assign to the time_created property of this Log.                                                                                                                                                                                                                          |
| time_last_modified | core | timestamp  | The value to assign to the time_last_modified property of this Log.                                                                                                                                                                                                                    |
| updated_at         | core | timestamp  | Time when the resource has been updated the last time.                                                                                                                                                                                                                                 |
| zone_id            | core | string     | The zone this resource resides within.                                                                                                                                                                                                                                                 |
