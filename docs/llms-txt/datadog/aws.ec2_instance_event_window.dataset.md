# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_instance_event_window.dataset.md

---
title: EC2 Instance Event Window
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 Instance Event Window
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ec2_instance_event_window.dataset/index.html
---

# EC2 Instance Event Window

An EC2 Instance Event Window in AWS defines a scheduled time range during which planned maintenance or service events for EC2 instances can occur. By creating and associating event windows with instances, you can control when disruptive events such as reboots or retirements are applied, helping minimize impact on workloads by aligning them with your preferred maintenance periods.

```
aws.ec2_instance_event_window
```

## Fields

| Title                    | ID   | Type   | Data Type                                             | Description |
| ------------------------ | ---- | ------ | ----------------------------------------------------- | ----------- |
| _key                     | core | string |
| account_id               | core | string |
| association_target       | core | json   | One or more targets associated with the event window. |
| cron_expression          | core | string | The cron expression defined for the event window.     |
| instance_event_window_id | core | string | The ID of the event window.                           |
| name                     | core | string | The name of the event window.                         |
| state                    | core | string | The current state of the event window.                |
| tags                     | core | hstore |
| time_ranges              | core | json   | One or more time ranges defined for the event window. |
