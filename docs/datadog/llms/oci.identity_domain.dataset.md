# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/oci/oci.identity_domain.dataset.md

---
title: Identity Domain
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Identity Domain
---

# Identity Domain

An Identity Domain in Oracle Cloud Infrastructure is a security and identity management boundary that provides authentication, authorization, and user lifecycle management. It allows you to manage users, groups, and application access independently, supporting single sign-on, federation, and fine-grained access policies. Identity Domains help isolate workloads, enforce governance, and simplify identity administration across multiple environments.

```
oci.identity_domain
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                                                                                           | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| cloud_account_id   | core | string     | The identifier of the related cloud account. The concept of an account might have different names in different cloud providers. AWS is calling it account, GCP calls it project and Azure uses the term subscription.                                               |
| cloud_account_name | core | string     | The name of the account this resource belongs to.                                                                                                                                                                                                                   |
| cloud_provider     | core | string     | The name of the cloud provider.                                                                                                                                                                                                                                     |
| cloud_tags         | core | hstore     |
| compartment_id     | core | string     | The value to assign to the compartment_id property of this Domain.                                                                                                                                                                                                  |
| created_at         | core | timestamp  | Time when the resource has been created.                                                                                                                                                                                                                            |
| description        | core | string     | The value to assign to the description property of this Domain.                                                                                                                                                                                                     |
| freeform_tags      | core | hstore     | The value to assign to the freeform_tags property of this Domain.                                                                                                                                                                                                   |
| home_region        | core | string     | The value to assign to the home_region property of this Domain.                                                                                                                                                                                                     |
| home_region_url    | core | string     | The value to assign to the home_region_url property of this Domain.                                                                                                                                                                                                 |
| id                 | core | string     | The value to assign to the id property of this Domain.                                                                                                                                                                                                              |
| is_hidden_on_login | core | bool       | The value to assign to the is_hidden_on_login property of this Domain.                                                                                                                                                                                              |
| license_type       | core | string     | The value to assign to the license_type property of this Domain.                                                                                                                                                                                                    |
| lifecycle_details  | core | string     | The value to assign to the lifecycle_details property of this Domain. Allowed values for this property are: "DEACTIVATING", "ACTIVATING", "UPDATING", 'UNKNOWN_ENUM_VALUE'. Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.   |
| lifecycle_state    | core | string     | The value to assign to the lifecycle_state property of this Domain. Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "INACTIVE", 'UNKNOWN_ENUM_VALUE'. Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'. |
| name               | core | string     | The name of this resource.                                                                                                                                                                                                                                          |
| region_id          | core | string     | The region this resource resides within.                                                                                                                                                                                                                            |
| replica_regions    | core | json       | The value to assign to the replica_regions property of this Domain.                                                                                                                                                                                                 |
| resource_type      | core | string     | The name of the resource type.                                                                                                                                                                                                                                      |
| tags               | core | hstore_csv |
| time_created       | core | timestamp  | The value to assign to the time_created property of this Domain.                                                                                                                                                                                                    |
| type               | core | string     | The value to assign to the type property of this Domain. Allowed values for this property are: "DEFAULT", "SECONDARY", 'UNKNOWN_ENUM_VALUE'. Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.                                  |
| updated_at         | core | timestamp  | Time when the resource has been updated the last time.                                                                                                                                                                                                              |
| url                | core | string     | The value to assign to the url property of this Domain.                                                                                                                                                                                                             |
| zone_id            | core | string     | The zone this resource resides within.                                                                                                                                                                                                                              |
