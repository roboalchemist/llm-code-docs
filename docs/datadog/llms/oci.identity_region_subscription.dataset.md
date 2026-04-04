# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/oci/oci.identity_region_subscription.dataset.md

---
title: Region Subscription
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Region Subscription
---

# Region Subscription

A Region Subscription in Oracle Cloud Infrastructure represents the association of a tenancy with a specific OCI region. It indicates which regions are enabled for use within the tenancy, allowing resources to be created and managed in those geographic locations. Subscribing to a region is required before deploying services there.

```
oci.identity_region_subscription
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                                                                        | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key               | core | string     |
| cloud_account_id   | core | string     | The identifier of the related cloud account. The concept of an account might have different names in different cloud providers. AWS is calling it account, GCP calls it project and Azure uses the term subscription.                            |
| cloud_account_name | core | string     | The name of the account this resource belongs to.                                                                                                                                                                                                |
| cloud_provider     | core | string     | The name of the cloud provider.                                                                                                                                                                                                                  |
| cloud_tags         | core | hstore     |
| compartment_id     | core | string     | Compartment containing the resource. Used for Access control, logical grouping, and authorization boundaries.                                                                                                                                    |
| created_at         | core | timestamp  | Time when the resource has been created.                                                                                                                                                                                                         |
| freeform_tags      | core | hstore     | The value to assign to the freeform_tags property of this Instance.                                                                                                                                                                              |
| is_home_region     | core | bool       | The value to assign to the is_home_region property of this RegionSubscription.                                                                                                                                                                   |
| name               | core | string     | The name of this resource.                                                                                                                                                                                                                       |
| region_id          | core | string     | The region this resource resides within.                                                                                                                                                                                                         |
| region_name        | core | string     | The value to assign to the region_name property of this RegionSubscription.                                                                                                                                                                      |
| resource_type      | core | string     | The name of the resource type.                                                                                                                                                                                                                   |
| status             | core | string     | The value to assign to the status property of this RegionSubscription. Allowed values for this property are: "READY", "IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'. Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'. |
| tags               | core | hstore_csv |
| time_created       | core | timestamp  | The value to assign to the time_created property of this Instance.                                                                                                                                                                               |
| updated_at         | core | timestamp  | Time when the resource has been updated the last time.                                                                                                                                                                                           |
| zone_id            | core | string     | The zone this resource resides within.                                                                                                                                                                                                           |
