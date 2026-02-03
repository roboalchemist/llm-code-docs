# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/oci/oci.identity_compartment.dataset.md

---
title: Compartment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Compartment
---

# Compartment

A Compartment in Oracle Cloud Infrastructure (OCI) is a logical container used to organize and isolate cloud resources. It helps manage access control, resource grouping, and governance by allowing administrators to apply policies at the compartment level. Compartments can be nested, enabling flexible structuring of resources to match organizational needs.

```
oci.identity_compartment
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                                                                                                           | Description |
| ------------------ | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| cloud_account_id   | core | string     | The identifier of the related cloud account. The concept of an account might have different names in different cloud providers. AWS is calling it account, GCP calls it project and Azure uses the term subscription.                                                               |
| cloud_account_name | core | string     | The name of the account this resource belongs to.                                                                                                                                                                                                                                   |
| cloud_provider     | core | string     | The name of the cloud provider.                                                                                                                                                                                                                                                     |
| cloud_tags         | core | hstore     |
| compartment_id     | core | string     | The value to assign to the compartment_id property of this Compartment.                                                                                                                                                                                                             |
| created_at         | core | timestamp  | Time when the resource has been created.                                                                                                                                                                                                                                            |
| description        | core | string     | The value to assign to the description property of this Compartment.                                                                                                                                                                                                                |
| freeform_tags      | core | hstore     | The value to assign to the freeform_tags property of this Compartment.                                                                                                                                                                                                              |
| id                 | core | string     | The value to assign to the id property of this Compartment.                                                                                                                                                                                                                         |
| inactive_status    | core | int64      | The value to assign to the inactive_status property of this Compartment.                                                                                                                                                                                                            |
| is_accessible      | core | bool       | The value to assign to the is_accessible property of this Compartment.                                                                                                                                                                                                              |
| lifecycle_state    | core | string     | The value to assign to the lifecycle_state property of this Compartment. Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'. Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'. |
| name               | core | string     | The value to assign to the name property of this Compartment.                                                                                                                                                                                                                       |
| region_id          | core | string     | The region this resource resides within.                                                                                                                                                                                                                                            |
| resource_type      | core | string     | The name of the resource type.                                                                                                                                                                                                                                                      |
| tags               | core | hstore_csv |
| time_created       | core | timestamp  | The value to assign to the time_created property of this Compartment.                                                                                                                                                                                                               |
| updated_at         | core | timestamp  | Time when the resource has been updated the last time.                                                                                                                                                                                                                              |
| zone_id            | core | string     | The zone this resource resides within.                                                                                                                                                                                                                                              |
