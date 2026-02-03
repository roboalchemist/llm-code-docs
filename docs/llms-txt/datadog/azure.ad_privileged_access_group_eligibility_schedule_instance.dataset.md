# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.ad_privileged_access_group_eligibility_schedule_instance.dataset.md

---
title: Ad Privileged Access Group Eligibility Schedule Instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Ad Privileged Access Group
  Eligibility Schedule Instance
---

# Ad Privileged Access Group Eligibility Schedule Instance

This table represents the ad_privileged_access_group_eligibility_schedule_instance resource from Microsoft Azure.

```
azure.ad_privileged_access_group_eligibility_schedule_instance
```

## Fields

| Title                   | ID   | Type       | Data Type                                                                                                                                                                                                                                                | Description |
| ----------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string     |
| access_id               | core | string     | The identifier of the membership or ownership eligibility relationship to the group. Required. The possible values are: owner, member. Supports $filter (eq).                                                                                            |
| eligibility_schedule_id | core | string     | The identifier of the privilegedAccessGroupEligibilitySchedule from which this instance was created. Required. Supports $filter (eq, ne).                                                                                                                |
| end_date_time           | core | string     | When the schedule instance ends. Required.                                                                                                                                                                                                               |
| group_id                | core | string     | The identifier of the group representing the scope of the membership or ownership eligibility through PIM for Groups. Required. Supports $filter (eq).                                                                                                   |
| id                      | core | string     | The unique identifier for an entity. Read-only.                                                                                                                                                                                                          |
| location                | core | string     |
| member_type             | core | string     | Indicates whether the assignment is derived from a group assignment. It can further imply whether the calling principal can manage the assignment schedule. Required. The possible values are: direct, group, unknownFutureValue. Supports $filter (eq). |
| name                    | core | string     |
| principal               | core | json       | References the principal that's in the scope of the membership or ownership eligibility request through the group that's governed by PIM. Supports $expand.                                                                                              |
| principal_id            | core | string     | The identifier of the principal whose membership or ownership eligibility to the group is managed through PIM for Groups. Required. Supports $filter (eq).                                                                                               |
| resource_group          | core | string     |
| start_date_time         | core | string     | When this instance starts. Required.                                                                                                                                                                                                                     |
| subscription_id         | core | string     |
| subscription_name       | core | string     |
| tags                    | core | hstore_csv |
