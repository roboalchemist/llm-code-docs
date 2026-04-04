# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/oci/oci.notificationdataplane_subscription.dataset.md

---
title: Subscription (Data Plane)
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Subscription (Data Plane)
---

# Subscription (Data Plane)

A Subscription (Data Plane) in OCI represents a customer's active agreement to use Oracle Cloud services. It defines the entitlements, service limits, and regions available to the tenant. This resource is essential for managing billing, service access, and usage tracking across the cloud environment.

```
oci.notificationdataplane_subscription
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                                                                                          | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key               | core | string     |
| cloud_account_id   | core | string     | The identifier of the related cloud account. The concept of an account might have different names in different cloud providers. AWS is calling it account, GCP calls it project and Azure uses the term subscription.                                              |
| cloud_account_name | core | string     | The name of the account this resource belongs to.                                                                                                                                                                                                                  |
| cloud_provider     | core | string     | The name of the cloud provider.                                                                                                                                                                                                                                    |
| cloud_tags         | core | hstore     |
| compartment_id     | core | string     | The value to assign to the compartment_id property of this SubscriptionSummary.                                                                                                                                                                                    |
| created_at         | core | timestamp  | Time when the resource has been created.                                                                                                                                                                                                                           |
| created_time       | core | int64      | The value to assign to the created_time property of this SubscriptionSummary.                                                                                                                                                                                      |
| deliver_policy     | core | string     |
| endpoint           | core | string     | The value to assign to the endpoint property of this SubscriptionSummary.                                                                                                                                                                                          |
| etag               | core | string     | The value to assign to the etag property of this SubscriptionSummary.                                                                                                                                                                                              |
| freeform_tags      | core | hstore     | The value to assign to the freeform_tags property of this SubscriptionSummary.                                                                                                                                                                                     |
| id                 | core | string     | The value to assign to the id property of this SubscriptionSummary.                                                                                                                                                                                                |
| lifecycle_state    | core | string     | The value to assign to the lifecycle_state property of this SubscriptionSummary. Allowed values for this property are: "PENDING", "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'. Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'. |
| name               | core | string     | The name of this resource.                                                                                                                                                                                                                                         |
| protocol           | core | string     | The value to assign to the protocol property of this SubscriptionSummary.                                                                                                                                                                                          |
| region_id          | core | string     | The region this resource resides within.                                                                                                                                                                                                                           |
| resource_type      | core | string     | The name of the resource type.                                                                                                                                                                                                                                     |
| tags               | core | hstore_csv |
| time_created       | core | timestamp  | The value to assign to the time_created property of this Instance.                                                                                                                                                                                                 |
| topic_id           | core | string     | The value to assign to the topic_id property of this SubscriptionSummary.                                                                                                                                                                                          |
| updated_at         | core | timestamp  | Time when the resource has been updated the last time.                                                                                                                                                                                                             |
| zone_id            | core | string     | The zone this resource resides within.                                                                                                                                                                                                                             |
