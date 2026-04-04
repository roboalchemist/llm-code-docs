# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.activity_log_alert.dataset.md

---
title: Activity Log Alert
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Activity Log Alert
---

# Activity Log Alert

This table represents the Activity Log Alert resource from Microsoft Azure.

```
azure.activity_log_alert
```

## Fields

| Title             | ID   | Type          | Data Type                                                                                                                                                                                                 | Description |
| ----------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string        |
| actions           | core | json          | The actions that will activate when the condition is met.                                                                                                                                                 |
| condition         | core | json          | The condition that will cause this alert to activate.                                                                                                                                                     |
| description       | core | string        | A description of this Activity Log Alert rule.                                                                                                                                                            |
| enabled           | core | bool          | Indicates whether this Activity Log Alert rule is enabled. If an Activity Log Alert rule is not enabled, then none of its actions will be activated.                                                      |
| id                | core | string        | The resource Id.                                                                                                                                                                                          |
| location          | core | string        | The location of the resource. Azure Activity Log Alert rules are supported on Global, West Europe and North Europe regions.                                                                               |
| name              | core | string        | The name of the resource.                                                                                                                                                                                 |
| resource_group    | core | string        |
| scopes            | core | array<string> | A list of resource IDs that will be used as prefixes. The alert will only apply to Activity Log events with resource IDs that fall under one of these prefixes. This list must include at least one item. |
| subscription_id   | core | string        |
| subscription_name | core | string        |
| tags              | core | hstore_csv    |
| type              | core | string        | The type of the resource.                                                                                                                                                                                 |
