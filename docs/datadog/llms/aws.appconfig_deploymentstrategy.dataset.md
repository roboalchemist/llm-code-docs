# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.appconfig_deploymentstrategy.dataset.md

---
title: Appconfig Deploymentstrategy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Appconfig Deploymentstrategy
---

# Appconfig Deploymentstrategy

This table represents the appconfig_deploymentstrategy resource from Amazon Web Services.

```
aws.appconfig_deploymentstrategy
```

## Fields

| Title                          | ID   | Type       | Data Type                                                                                                                                              | Description |
| ------------------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                           | core | string     |
| account_id                     | core | string     |
| deployment_duration_in_minutes | core | int64      | Total amount of time the deployment lasted.                                                                                                            |
| description                    | core | string     | The description of the deployment strategy.                                                                                                            |
| final_bake_time_in_minutes     | core | int64      | The amount of time that AppConfig monitored for alarms before considering the deployment to be complete and no longer eligible for automatic rollback. |
| growth_factor                  | core | float64    | The percentage of targets that received a deployed configuration during each interval.                                                                 |
| growth_type                    | core | string     | The algorithm used to define how percentage grew over time.                                                                                            |
| id                             | core | string     | The deployment strategy ID.                                                                                                                            |
| name                           | core | string     | The name of the deployment strategy.                                                                                                                   |
| replicate_to                   | core | string     | Save the deployment strategy to a Systems Manager (SSM) document.                                                                                      |
| tags                           | core | hstore_csv |
