# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/oci/oci.events_rule.dataset.md

---
title: Event Rule
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Event Rule
---

# Event Rule

An Event Rule in Oracle Cloud Infrastructure (OCI) is used to detect specific events within your tenancy and trigger automated actions in response. It listens for events from OCI services, such as resource changes or lifecycle state updates, and routes them to defined targets like Functions, Notifications, or Streaming. This enables event-driven automation, allowing you to respond quickly to changes without manual intervention. Event Rules help streamline operations, enforce governance, and integrate OCI services with external systems.

```
oci.events_rule
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                          | Description |
| ------------------ | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| actions            | core | json       | The value to assign to the actions property of this Rule.                                                                                                                                                                                                                                          |
| cloud_account_id   | core | string     | The identifier of the related cloud account. The concept of an account might have different names in different cloud providers. AWS is calling it account, GCP calls it project and Azure uses the term subscription.                                                                              |
| cloud_account_name | core | string     | The name of the account this resource belongs to.                                                                                                                                                                                                                                                  |
| cloud_provider     | core | string     | The name of the cloud provider.                                                                                                                                                                                                                                                                    |
| cloud_tags         | core | hstore     |
| compartment_id     | core | string     | The value to assign to the compartment_id property of this Rule.                                                                                                                                                                                                                                   |
| condition          | core | string     | The value to assign to the condition property of this Rule.                                                                                                                                                                                                                                        |
| created_at         | core | timestamp  | Time when the resource has been created.                                                                                                                                                                                                                                                           |
| description        | core | string     | The value to assign to the description property of this Rule.                                                                                                                                                                                                                                      |
| freeform_tags      | core | hstore     | The value to assign to the freeform_tags property of this Rule.                                                                                                                                                                                                                                    |
| id                 | core | string     | The value to assign to the id property of this Rule.                                                                                                                                                                                                                                               |
| is_enabled         | core | bool       | The value to assign to the is_enabled property of this Rule.                                                                                                                                                                                                                                       |
| lifecycle_message  | core | string     | The value to assign to the lifecycle_message property of this Rule.                                                                                                                                                                                                                                |
| lifecycle_state    | core | string     | The value to assign to the lifecycle_state property of this Rule. Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'. Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'. |
| name               | core | string     | The name of this resource.                                                                                                                                                                                                                                                                         |
| region_id          | core | string     | The region this resource resides within.                                                                                                                                                                                                                                                           |
| resource_type      | core | string     | The name of the resource type.                                                                                                                                                                                                                                                                     |
| tags               | core | hstore_csv |
| time_created       | core | timestamp  | The value to assign to the time_created property of this Rule.                                                                                                                                                                                                                                     |
| updated_at         | core | timestamp  | Time when the resource has been updated the last time.                                                                                                                                                                                                                                             |
| zone_id            | core | string     | The zone this resource resides within.                                                                                                                                                                                                                                                             |
