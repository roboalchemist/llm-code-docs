# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/oci/oci.identity_tenancy.dataset.md

---
title: Tenancy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Tenancy
---

# Tenancy

A Tenancy in Oracle Cloud Infrastructure (OCI) is the root compartment that represents an organization's account. It serves as the secure and isolated boundary for all OCI resources, users, and policies. Within a tenancy, administrators can create compartments, manage access, and organize resources for governance and billing.

```
oci.identity_tenancy
```

## Fields

| Title                                 | ID   | Type       | Data Type                                                                                                                                                                                                             | Description |
| ------------------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                  | core | string     |
| cloud_account_id                      | core | string     | The identifier of the related cloud account. The concept of an account might have different names in different cloud providers. AWS is calling it account, GCP calls it project and Azure uses the term subscription. |
| cloud_account_name                    | core | string     | The name of the account this resource belongs to.                                                                                                                                                                     |
| cloud_guard_configuration             | core | json       |
| cloud_provider                        | core | string     | The name of the cloud provider.                                                                                                                                                                                       |
| cloud_tags                            | core | hstore     |
| compartment_id                        | core | string     | Compartment containing the resource. Used for Access control, logical grouping, and authorization boundaries.                                                                                                         |
| created_at                            | core | timestamp  | Time when the resource has been created.                                                                                                                                                                              |
| description                           | core | string     | The value to assign to the description property of this Tenancy.                                                                                                                                                      |
| freeform_tags                         | core | hstore     | The value to assign to the freeform_tags property of this Tenancy.                                                                                                                                                    |
| id                                    | core | string     | The value to assign to the id property of this Tenancy.                                                                                                                                                               |
| name                                  | core | string     | The value to assign to the name property of this Tenancy.                                                                                                                                                             |
| region_id                             | core | string     | The region this resource resides within.                                                                                                                                                                              |
| resource_type                         | core | string     | The name of the resource type.                                                                                                                                                                                        |
| tags                                  | core | hstore_csv |
| time_created                          | core | timestamp  | The value to assign to the time_created property of this Instance.                                                                                                                                                    |
| updated_at                            | core | timestamp  | Time when the resource has been updated the last time.                                                                                                                                                                |
| upi_idcs_compatibility_layer_endpoint | core | string     | The value to assign to the upi_idcs_compatibility_layer_endpoint property of this Tenancy.                                                                                                                            |
| zone_id                               | core | string     | The zone this resource resides within.                                                                                                                                                                                |
