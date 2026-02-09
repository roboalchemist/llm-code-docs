# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/oci/oci.notificationdataplane_subscription_summary.dataset.md

---
title: Notification Subscription Summary
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Notification Subscription Summary
---

# Notification Subscription Summary

This table represents the Notification Subscription Summary resource from Oracle Cloud Infrastructure.

```
oci.notificationdataplane_subscription_summary
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
| delivery_policy    | core | json       | The value to assign to the delivery_policy property of this SubscriptionSummary.                                                                                                                                                                                   |
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
