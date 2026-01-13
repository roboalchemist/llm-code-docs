# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.deadline_monitor.dataset.md

---
title: Deadline Cloud Monitor
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Deadline Cloud Monitor
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.deadline_monitor.dataset/index.html
---

# Deadline Cloud Monitor

Deadline Cloud Monitor in AWS provides a summary view of monitoring resources for Deadline Cloud, a managed service for render farm management. It helps track and manage the health, status, and activity of render workloads, giving visibility into job progress and system performance.

```
aws.deadline_monitor
```

## Fields

| Title                           | ID   | Type      | Data Type                                                                                                                              | Description |
| ------------------------------- | ---- | --------- | -------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                            | core | string    |
| account_id                      | core | string    |
| created_at                      | core | timestamp | The UNIX timestamp of the date and time that the monitor was created.                                                                  |
| created_by                      | core | string    | The user name of the person that created the monitor.                                                                                  |
| identity_center_application_arn | core | string    | The Amazon Resource Name (ARN) that the IAM Identity Center assigned to the monitor when it was created.                               |
| identity_center_instance_arn    | core | string    | The Amazon Resource Name (ARN) of the IAM Identity Center instance responsible for authenticating monitor users.                       |
| monitor_id                      | core | string    | The unique identifier for the monitor.                                                                                                 |
| role_arn                        | core | string    | The Amazon Resource Name (ARN) of the IAM role for the monitor. Users of the monitor use this role to access Deadline Cloud resources. |
| subdomain                       | core | string    | The subdomain used for the monitor URL. The full URL of the monitor is subdomain.Region.deadlinecloud.amazonaws.com.                   |
| tags                            | core | hstore    |
| updated_at                      | core | timestamp | The UNIX timestamp of the date and time that the monitor was last updated.                                                             |
| updated_by                      | core | string    | The user name of the person that last updated the monitor.                                                                             |
| url                             | core | string    | The complete URL of the monitor. The full URL of the monitor is subdomain.Region.deadlinecloud.amazonaws.com.                          |
