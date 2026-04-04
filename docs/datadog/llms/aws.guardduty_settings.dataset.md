# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.guardduty_settings.dataset.md

---
title: GuardDuty Settings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > GuardDuty Settings
---

# GuardDuty Settings

GuardDuty Settings in AWS define how Amazon GuardDuty manages malware protection and scanning within your environment. This includes configuration details for automated malware scans, scan frequency, and integration with other GuardDuty findings. It helps ensure that workloads are continuously monitored for malicious files and threats, providing visibility and security insights without requiring manual setup.

```
aws.guardduty_settings
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                | Description |
| ------------------------- | ---- | ---------- | ------------------------------------------------------------------------ | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| administrator             | core | json       | The administrator account details.                                       |
| ebs_snapshot_preservation | core | string     | An enum value representing possible snapshot preservation settings.      |
| master                    | core | json       | The administrator account details.                                       |
| scan_resource_criteria    | core | json       | Represents the criteria to be used in the filter for scanning resources. |
| tags                      | core | hstore_csv |
