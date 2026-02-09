# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/oci/oci.identity_tag_default.dataset.md

---
title: Tag Default
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Tag Default
---

# Tag Default

Tag Default in Oracle Cloud Infrastructure is a resource that automatically applies a predefined tag key and value to all new resources within a compartment. It helps enforce consistent tagging policies across an organization by ensuring that every resource created inherits the specified tags without requiring manual input. This simplifies cost tracking, organization, and governance.

```
oci.identity_tag_default
```

## Fields

| Title               | ID   | Type       | Data Type                                                                                                                                                                                                                           | Description |
| ------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                | core | string     |
| cloud_account_id    | core | string     | The identifier of the related cloud account. The concept of an account might have different names in different cloud providers. AWS is calling it account, GCP calls it project and Azure uses the term subscription.               |
| cloud_account_name  | core | string     | The name of the account this resource belongs to.                                                                                                                                                                                   |
| cloud_provider      | core | string     | The name of the cloud provider.                                                                                                                                                                                                     |
| cloud_tags          | core | hstore     |
| compartment_id      | core | string     | The value to assign to the compartment_id property of this TagDefault.                                                                                                                                                              |
| created_at          | core | timestamp  | Time when the resource has been created.                                                                                                                                                                                            |
| freeform_tags       | core | hstore     | The value to assign to the freeform_tags property of this Instance.                                                                                                                                                                 |
| id                  | core | string     | The value to assign to the id property of this TagDefault.                                                                                                                                                                          |
| is_required         | core | bool       | The value to assign to the is_required property of this TagDefault.                                                                                                                                                                 |
| lifecycle_state     | core | string     | The value to assign to the lifecycle_state property of this TagDefault. Allowed values for this property are: "ACTIVE", 'UNKNOWN_ENUM_VALUE'. Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'. |
| locks               | core | json       | The value to assign to the locks property of this TagDefault.                                                                                                                                                                       |
| name                | core | string     | The name of this resource.                                                                                                                                                                                                          |
| region_id           | core | string     | The region this resource resides within.                                                                                                                                                                                            |
| resource_type       | core | string     | The name of the resource type.                                                                                                                                                                                                      |
| tag_definition_id   | core | string     | The value to assign to the tag_definition_id property of this TagDefault.                                                                                                                                                           |
| tag_definition_name | core | string     | The value to assign to the tag_definition_name property of this TagDefault.                                                                                                                                                         |
| tag_namespace_id    | core | string     | The value to assign to the tag_namespace_id property of this TagDefault.                                                                                                                                                            |
| tags                | core | hstore_csv |
| time_created        | core | timestamp  | The value to assign to the time_created property of this TagDefault.                                                                                                                                                                |
| updated_at          | core | timestamp  | Time when the resource has been updated the last time.                                                                                                                                                                              |
| value               | core | string     | The value to assign to the value property of this TagDefault.                                                                                                                                                                       |
| zone_id             | core | string     | The zone this resource resides within.                                                                                                                                                                                              |
