# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ssm_windowtarget.dataset.md

---
title: Systems Manager Window Target
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Systems Manager Window Target
---

# Systems Manager Window Target

This table represents the Systems Manager Window Target resource from Amazon Web Services.

```
aws.ssm_windowtarget
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                                                                                                                                                                                                           | Description |
| ----------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| account_id        | core | string     |
| description       | core | string     | A description for the target.                                                                                                                                                                                                                                                       |
| name              | core | string     | The name for the maintenance window target.                                                                                                                                                                                                                                         |
| owner_information | core | string     | A user-provided value that will be included in any Amazon CloudWatch Events events that are raised while running tasks for these targets in this maintenance window.                                                                                                                |
| resource_type     | core | string     | The type of target that is being registered with the maintenance window.                                                                                                                                                                                                            |
| tags              | core | hstore_csv |
| targets           | core | json       | The targets, either managed nodes or tags. Specify managed nodes using the following format: <code>Key=instanceids,Values=&lt;instanceid1&gt;,&lt;instanceid2&gt;</code> Tags are specified using the following format: <code>Key=&lt;tag name&gt;,Values=&lt;tag value&gt;</code>. |
| window_id         | core | string     | The ID of the maintenance window to register the target with.                                                                                                                                                                                                                       |
| window_target_id  | core | string     | The ID of the target.                                                                                                                                                                                                                                                               |
